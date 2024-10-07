import numpy as np


def get_src_col(mist_eep_track_file):
    """ Reads a MIST evolutionary track

    Parameters:
    ----------
    mist_eep_track_file: `str` or `path` to the file you want to read

    Returns:
    -------

    data: `np.array` containing the data
    col:  `list` containing the columns header read from the file
    """
    data = np.genfromtxt(mist_eep_track_file, skip_header=12)
    # read header
    with open(mist_eep_track_file, "r") as f:
        for i, line in enumerate(f):
            if i == 11:
                line = line.replace("#", "")  # remove comment sign
                col = line.split()
                break
    return data, col


if __name__ == "__main__":
    print("Example of usage")
    fname = str(input("path to file to read? "))
    src, col = get_src_col(fname)
    print(" ")
    print("The data have been loaded in the numpy array src")
    print("and the column names in the header in the list col")
    print(" ")
    print("You can now access the data with:")
    print(" x = src[:, col.index(\"name of column\")]")
    print("For example, to get the total mass of the star")
    print(" m = src[:, col.index(\"star_mass\")]")
    print("")
    print("m =", src[:, col.index("star_mass")])
    print("You can list all the available variable names printing the list col")
    print(col)
    print("You can use this function by putting MIST_reader.py in your script folder")
    print("and using `from MIST_reader import get_src_col`")
