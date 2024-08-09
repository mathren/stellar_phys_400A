# Author: Mathieu Renzo <mathren90@gmail.com>
# Keywords: files

# Copyright (C) 2019-2022 Mathieu Renzo

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses/.

__author__ = "Mathieu Renzo"

import numpy as np
import os
import sys
import glob
import time
import math


# import re
# for log_scrubber
import shlex

# imports below are optional #
try:
    from termcolor import colored
except ModuleNotFoundError:
    # print("no pretty colors, install termcolor for that")
    def colored(string, color):
        print(string)

try:
    import pyMesaUtils as pym
except ModuleNotFoundError:
    # print("pyMESA not found, install from https://github.com/rjfarmer/pyMesa")
    pass

# constants -------------------------------------------------------------------------------
global secyer, G_cgs, Lsun, Msun, Rsun_cm, clight, sigma_SB
try:
    """read constants from MESA, requires pyMESA and MESA installed"""
    const_lib, const_def = pym.loadMod("const")
    secyer = const_def.secyer.value
    G_cgs = const_def.standard_cgrav.value
    Lsun = const_def.Lsun.value
    Msun = const_def.Msun.value
    Rsun_cm = const_def.Rsun.value
    clight = const_def.clight.value
    sigma = const_def.boltz_sigma
    print(colored("successfully read constants from pyMesa", "blue"))
except:
    """if pyMESA not available, define by hand"""
    dayyer = float(365.25)
    secyer = float(dayyer * 24 * 60 * 60)
    G_cgs = float(6.67430e-8)  # in cgs
    mu_sun = float(1.3271244e26)
    Lsun = float(3.828e33)
    Msun = mu_sun / G_cgs
    Rsun_cm = float(6.957e10)   # in cm
    clight = float(2.99792458e10)  # cm/s
    boltzm = float(1.380649e-16)  # erg/ K
    planck_h = float(6.62607015e-27)  # Planck constant (erg s)
    hbar = planck_h/(2*math.pi)
    sigma_SB = float(
        (math.pi*math.pi * boltzm*boltzm*boltzm*boltzm)/ (60 * hbar*hbar*hbar * clight*clight)
        )
    print(colored("Hardcoded some constants", "yellow"))


# load files ------------------------------------------------------------------
def reader(myfile, ncols, nhead, fname=None):
    """This example shows how to read a large regular ascii file (consisting of ncolumns), store it in binary format.
    This provides a great speed up when reading larger files created with binary_c or MESA or whateve
    SdM  March 12, 2015
    """

    """15.04.2016 Mathieu: modified to fit my needs for binary_c as well"""

    """8.06.2022  Mathieu: heavy refactoring"""

    # The new binary file will be stored with the same name but with the extention.npy
    if fname == None:
        bin_fname = str(myfile[:-4]) + ".npy"
    else:
        bin_fname = fname
    # Just for fun... time the routine
    start_time = time.time()
    if not os.path.isfile(bin_fname):  # Check if .databin exists already...
        print("...    reading ascii file ", myfile)
        print("...    and storing it for you in binary format")
        print("...    patience please, next time will be way faster ")
        print("...    I promise")
        # If binary does not exist, read the original ascii file:
        if not os.path.isfile(myfile):
            print("File does not exist ", myfile)
            return
        # Read the first "ncol" columns of the file after skipping "nhead" lines, store in a numpy.array
        data = np.genfromtxt(myfile, skip_header=nhead)  # , usecols=range(ncols))
        # Save the numpy array to file in binary format
        np.save(bin_fname, data)
        # print "...    That took ", time.time() - start_time, "second"
    else:
        # print "... Great Binary file exists, reading data directly from ", bin_fname
        # If binary file exists load it directly.
        data = np.load(bin_fname)
        # print "   That took ", time.time() - start_time, "second"
    return data


def get_src_col(f, clean=True, convert=True, bin_fname=None):
    """
    Read MESA output (history or profiles) and optionally
    save a copy in binary format for faster access later.

    Parameters:
    ----------
    clean:   `bool` if True use log_scrubber to remove retry steps before converting to binary
              and parsing the output.
    convert: `bool`, if True the file f is saved to
              binary format for faster reading in the future.
    bin_fname:   `str` name of the binary file if needed

    Returns:
    --------
    src: `np.array`, shape (number of timesteps,
          number of columns), the data
    col: `list`, column names from the header
    """
    # print(f)
    # TODO: maybe one day I'll update this to be a pandas dataframe
    # read header
    with open(f, "r") as P:
        for i, line in enumerate(P):
            if i == 5:
                col = line.split()
                break
    # check if binary exists
    if bin_fname == None:
        bin_fname = str(str(f)[:-4]) + ".npy"
    if os.path.isfile(bin_fname):
        # read the column and binary
        src = reader(f, len(col), 6, bin_fname)
    else:  # binary file does not exist
        print("... Binary file does not yet exist")
        if ("history.data" in str(f)) and clean:
            scrub(f)
        if convert:
            src = reader(f, len(col), 6, bin_fname)
        else:
            src = np.genfromtxt(f, skip_header=6)
    return src, col


def read_MESA_header(fname):
    """reader for the header of MESA profile or history files.
    Parameters:
    ----------
    fname : `string`, path to the file to open
    Returns:
    --------
    src : `list` values, some cannot be converted to float
    col : `list`, columns names
    """
    with open(fname, "r") as f:
        for i, line in enumerate(f):
            if i == 1:
                col = line.split()
            if i == 2:
                src = line.split()
                break
    return src, col


def scrub(logName):
    # this uses the log_scrubber.py script from Bill Wolf
    # which is available here: https://zenodo.org/record/2619282
    print("... let me scrub this for you")
    # dirty fix for PPI ejecta files
    if "ejecta.data" in str(logName):
        dataStart = 1
    else:
        dataStart = 6
    ###################################################################
    # THIS SHOULDN'T NEED TO BE TOUCHED UNLESS YOU ARE SPEEDING IT UP #
    ###################################################################
    # Pull original data from history file
    f = open(logName, "r")
    fileLines = f.readlines()
    f.close()
    headerLines = fileLines[:dataStart]
    dataLines = fileLines[dataStart:]
    # Determine which column is the model_number column
    headers = shlex.split(headerLines[dataStart - 1])
    modelNumberCol = headers.index("model_number")
    # Get list of model numbers
    modelNumbers = [-1] * len(dataLines)
    for i in range(len(dataLines)):
        data = shlex.split(dataLines[i])
        modelNumbers[i] = int(float(data[modelNumberCol]))
    # Pick "good" data points from the end to the beginning
    modelNumbers.reverse()
    dataLines.reverse()
    dataOut = []
    for i in range(len(modelNumbers)):
        if len(dataOut) == 0:
            dataOut.append(dataLines[i])
            lastGoodModelNumber = modelNumbers[i]
            #        print 'model_number = ', modelNumbers[i], ': Accepted!'
        elif modelNumbers[i] < lastGoodModelNumber:
            dataOut.append(dataLines[i])
            lastGoodModelNumber = modelNumbers[i]
            #        print 'model_number = ', modelNumbers[i], '<', lastGoodModelNumber, ': Accepted!'
            # else:
            #        print 'model_number = ', modelNumbers[i], '>=', lastGoodModelNumber, ': REJECTED!'
    # Properly reorder data and make combined output list of lines
    dataOut.reverse()
    fileLinesOut = headerLines + dataOut
    # Output ordered data back into history file
    f = open(logName, "w")
    for line in fileLinesOut:
        f.write(line)
    f.close()
    print("Data in", logName, "has been scrubbed.")
