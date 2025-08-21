
# Table of Contents

1.  [Examples of past honor's projects](#org915e50e)
    1.  [Main sequence burning in massive population III stars](#orgc644ec1)
        1.  [Instructions](#orgbcb038a)



<a id="org915e50e"></a>

# Examples of past honor's projects

The honor's project consist in installing on your machine [MESA](https://docs.mesastar.org/en/latest/), and
use it to investigate something we will barely touch upon in class.

The list below contains some examples, if you are interested in doing
an honor's project for this class, please come talk to me to define a
scope that best fits your interests *and* the content of this class.


<a id="orgc644ec1"></a>

## Main sequence burning in massive population III stars

Nuclear burning in massive stars occurs through the CNO cycle, which
uses metals (Carbon, Nitrogen, and Oxygen) as catalysts to stick
together 4 protons, turn two of them into neutrons, and produce
helium. However, what happens when C, N, and O are *not* available?

One physical situation where we think this may have happened is for
Population III stars, the first stars formed from pristine material
from the Big Bang: those only had H and He (and maybe some trace Li
and Be), no C, N, or O was available in the gas cloud they formed
from. **N.B.:** we have not seen these stars, but clearly at some point
they must have existed! The only way to study how they evolved for now
is through numerical simulations.

In this project you will compute with the stellar evolution code [MESA](https://docs.mesastar.org/en/latest/)
the evolution of two 30M<sub>o</sub> non-rotating, non-magnetic, single
stars, one at solar metallicity Z<sub>o</sub> and one with Z=0, until the end
of hydrogen core burning, compare their evolution in terms of their
potentially observable surface properties *and* in terms of their
interior structure, and interpret the differences.


<a id="orgbcb038a"></a>

### Instructions

-   Follow the [MESA](https://docs.mesastar.org/en/latest/) documentation to install the code
-   Follow the tutorial to run MESA: this will be your Z<sub>o</sub> 15M<sub>o</sub> star!
-   By reading the documentation, figure out what to change to make
    this a 30M<sub>o</sub> star and run it until "terminal age main sequence"
    (end of H core burning).
-   By reading the documentation, figure out which options to change to
    set Z=0 (**hint**: there should be more than one!), and run a second,
    Z=0 30M<sub>o</sub> star (otherwise identical to the tutorial model)
-   Plot as many things as you wish to understand the physical
    differences between the two models and write up a short text (<4
    pages including figures) with your findings. Focus on the physical
    processes in the stellar interior and why they may differ, and put
    them in the context of the course material.

