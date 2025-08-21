
# Table of Contents

1.  [Measuring masses](#org5ce916d)
    1.  [Binaries are common](#org8bf8b17)
        1.  [Visual binaries](#org62aa4e9)
        2.  [Astrometric binaries](#org1a25e34)
        3.  [Spectroscopic binaries](#orgd0a2ddf)
        4.  [Eclipsing binaries](#org53e52da)
    2.  [Dynamical mass determination](#orgd7d2254)
        1.  [Visual binaries](#orgec5f6da)
        2.  [Spectroscopic (and eclipsing) binaries](#orgb9fdbad)
    3.  [Mass-luminosity relation](#orge555307)
2.  [Homework](#org2d06ecf)
    1.  [Exercise 7.4 on Carroll & Ostie](#org30845f1)
    2.  [Exercise 7.6 on Carroll & Ostie](#org8fe5d1b)

**Materials**: Verbunt lecture notes (part 1), Sections 2.1-2.4 and 3.2 in
Tauris & Van den Heuvel 2023 book, Chapter 7 of Carroll & Ostie's
book, Chapter 3 in Prsa's book.


<a id="org5ce916d"></a>

# Measuring masses

This is typically a very hard problem: as we have seen, on the HRD/CMD
there is a tight correlation between a star's magnitude and color.
This holds for the majority (>90%) of stars, and thus for the longest
phase of evolution. The linear relation between color and magnitude
(that is effective temperature and luminosity) suggests there is one
single parameter that determines the position on a star on this
diagram. However, how do we determine what this parameter is, having
only these observational data? It is generally not possible without
relying on models. However, binaries can help!


<a id="org8bf8b17"></a>

## Binaries are common

The Sun is clearly not in a binary system. However, it is **not** uncommon
for stars to have gravitationally bound companion(s) orbiting around
them, which can be of great help to determine their properties.

In fact, in this case we have two stars presumably born at roughly the
same time, presumably with the same initial composition, and we can
derive physical properties comparing them to each other.

The figure below shows as a function of stellar mass (bottom x-axis)
or as a function of stellar spectroscopic type (top x-axis, we will
see that these are related soon!) the fraction of stars that have at
least one companion (so binaries, triples, etc., bold symbols) and the
fraction that has two or more companions (so triples, quadruples,
etc., thinner symbols). While this figure doesn't tell us how big and
how close the companion(s) are, it is increasingly harder to observe
companions next to bright stars, and observational bias favor higher
mass and closer companions.

![img](./images/bin-frac.png "Fraction of binaries and higher multiplicity as a function of mass (bottom x-axis) or spectral type (top x-axis), modified from [Offner et al. 2023](https://ui.adsabs.harvard.edu/abs/2023ASPC..534..275O/abstract).")

Let's review some types of binaries.


<a id="org62aa4e9"></a>

### Visual binaries

These are binaries that can be resolved (i.e., one can identify two
*distinct* point sources) by naked eye. Typically, this means
astrophysically very wide binaries that are unlikely to interact
beyond the fact that they are gravitationally bound and they orbit
each other. Nevertheless, they have an important historical role,
since Hershel observation of their motion of the sky over decades
proved that Kepler's law are valid beyond the Solar system.

[Mitchell 1767](https://ui.adsabs.harvard.edu/abs/1767RSPT...57..234M/abstract) also used statistical argument that all the visual
binaries visible at the time could not be just chance alignment, and
instead had to be somehow physically related to each other.

A classic example are Mizar & Alcor in the Big Dipper: the ability of
finding the "double star" in this asterism was used as an eyesight
test to become an astronomer in Hellenistic times. The name Alcor
comes from the arabic for "hard to see"! Nowadays with modern
telescopes we can see that Mizar is itself a quadruple system made of
two binaries orbiting each other, and Alcor may itself be a binary,
for a total of maybe 6 stars (e.g., [Mamjek et al. 2010](https://iopscience.iop.org/article/10.1088/0004-6256/139/3/919))!

![img](./images/zoom2.png "Zoom in on Mizar & Alcor from [Renzo 2019](http://hdl.handle.net/11245.1/ee92e82a-13e8-4add-a4ce-f2d3613e42c3)")


<a id="org1a25e34"></a>

### Astrometric binaries

Wide binaries where one of the two stars is too faint to be seen can
still be found by looking at the peculiar motion of the star that can
be seen on the sky. What matters is its *proper motion* (not the
apparent motion due to the Earth rotation around its axis and
revolution around the Sun) with respect to background
stars too far to be moving. For a single star, this is usually a
straight line (because the timescale for it to turn around the
Galactic center is typically &sim; hundreds of millions of years).
However, if the star is in a binary, what moves along a straight line
is the center of mass of the binary! The *photocenter* (i.e. the point
from where we can detect light) will "wiggle" around this straight
line due to orbital motion (and on top of the parallax periodic
wiggle).

This was first detected for the binary Sirius A and Sirius B by Bessel
in 1844 (the detection of photons from Sirius B followed in 1862 by
Clark). Nowadays, this is a very timely because of the precise
astrometric measurements by *Gaia*:

-   this has been used to find *Gaia* BH1 ([El Badry et al. 2023a](https://ui.adsabs.harvard.edu/abs/2023MNRAS.518.1057E/abstract)), BH2 ([El
    Badry 2023b](https://ui.adsabs.harvard.edu/abs/2023MNRAS.521.4323E/abstract)), and BH3 ([Gaia Collaboration, Panuzzo et al. 2024](https://ui.adsabs.harvard.edu/abs/2024A%26A...686L...2G/abstract)):
    these systems have stars orbiting around an otherwise undetectable
    Black Hole!
-   it can also be used to find stars in wide orbits around NS or other
    faint stars, and possibly even massive planets!

![img](./images/siriusAB.png "Path on the sky for Sirius A (thick line), Sirius B (thin line), and the center of mass (dashed line). Top right: absolute orbits around the center of mass. From [Lippincott 1961](https://ui.adsabs.harvard.edu/abs/1961ASPL....8..311L/abstract).")


<a id="orgd0a2ddf"></a>

### Spectroscopic binaries

![img](./images/RV_scheme.png "Schematic representation of the Doppler shift of spectral lines in binaries from which one can calculate radial velocities. Fig. 7.3 in Carrol & Ostie 2007 or 2.3 in Tauris & van den Heuvel 2023 books.")

1.  SB1

    In a spectrum, one star of the binary dominates, but we can see its
    orbital motion as Doppler shifting of the spectral lines. Even if we
    never see the less bright star, we can infer its presence from the
    orbital motion of the brighter star.
    
    **N.B.:** Radial velocity surveys that find massive and close-by planet
    are effectively finding SB1 binaries made of a star and a planet!

2.  SB2

    These are spectroscopic binaries where both stars are contributing
    light to the spectrum, meaning there will be two sets of spectral
    lines that are periodically Doppler shifted in couter-phase.


<a id="org53e52da"></a>

### Eclipsing binaries

These are binaries when at some point in the orbit one star passes in
front of the other. This blocks some of the light from one of the two
stars causing an eclipse and a dip in the light curve (i.e., the plot
of the luminosity of the system as a function of time).

This of course can only happen if the inclination of the orbital plane
of the binary w.r.t. the line of sight is not too large. Typically,
astronomers define the inclination of the orbital plane *i* w.r.t. the
plane of the sky, therefore the line-of-sight (which is perpendicular
to the plane of the sky by definition) has an angle &varphi; = &pi;/2 - *i* w.r.t.
the orbital plane. To have an eclipse, at least partial,

<div class="latex" id="org30e23b2">
\begin{equation}
\sin(\varphi) \leq \frac{R_{1} + R_{2}}{a} \ \ ,
\end{equation}

</div>

where we use that sin(&varphi;)=cos(i), and a &times; cos(i) is the projected
binary separation a on the plane of the sky, which is smaller than R<sub>1</sub>+R<sub>2</sub>
with R<sub>i</sub> stellar radii, leads to an eclipse. The eclipse will be total
if

<div class="latex" id="orgc6b7a6d">
\begin{equation}
\sin(\varphi) \leq \frac{R_{1} - R_{2}}{a}
\end{equation}

</div>

Note that in either case, the occurrence of an eclipse puts an
upper limit on sin(&varphi;), that is a direct observational constrain on the
inclination angle i.

The time duration of an eclipse can be used to determine the radii of
the two stars. Consider the following figure:

![img](./images/EB.png "Light cuve (visual magnitude as function of time) for an eclipsing binary with i=&pi;/2, figure 7.9 in Carrol & Ostie's book")

one can see that, labeling with 2 the geometrically smaller star
(darker gray) and assuming the orbit to be circular and the semi-major
axis to be a and the period P:

<div class="latex" id="org2537e31">
\begin{equation}
 \frac{t_{d} -t_{a}}{P} = \frac{2(R_{1}+R_{2})}{2\pi a} \ \ ,
\end{equation}

</div>

and

<div class="latex" id="orgd943bf5">
\begin{equation}
 \frac{t_{c} -t_{b}}{P}_{} = \frac{2(R_{1}-R_{2})}{2\pi a} \ \ .
\end{equation}

</div>

These equations allow to calculate R<sub>j</sub>/a and if also the masses are
known also the individual radii R<sub>j</sub> using Kepler's laws to get rid of
the orbital semi-major axis a.

-   **Q**: In the figure above, which star is assumed to be the hotter one?
-   **Q**: Can you see what happens to the light curve minima if we have an
    inclination of the binary orbit w.r.t. the plane of the sky?


<a id="orgd7d2254"></a>

## Dynamical mass determination


<a id="orgec5f6da"></a>

### Visual binaries

Using Kepler's laws, we can use binaries to measure observationally
masses without relying on hard, expensive, and uncertain stellar
models.

In particular the third law can be written as

<div class="latex" id="org885b4f3">
\begin{equation}
\label{eq:Kepler3}
   G(M_{1}+M_{2}) = n^{2} a^{3} \ \ ,
\end{equation}

</div>

where M<sub>i</sub> are the masses of the stars, n= 2&pi;/P is the angular velocity
(a.k.a. "true anomaly") and a is the semimajor axis of the orbit (of the
orbit of the reduced mass point &mu; = M<sub>1</sub>M<sub>2</sub>/(M<sub>1</sub>+M<sub>2</sub>) around the center of
mass).

**N.B.:** Often for solar-system application M<sub>2</sub> &Lt; M<sub>1</sub> = M<sub>o</sub>, so M<sub>2</sub> can
be neglected (e.g., if M<sub>2</sub> = M<sub>&oplus;</sub>). This is generally *not* the case
with star+star binaries.

For a visual binary (see above) where we can measure the semi-major
axes a<sub>i</sub> of both stars around the center of mass, we also have another
equation that follows from the definition of center of mass:

<div class="latex" id="orgcecf041">
\begin{equation}
\label{eq:semimajor_axes}
 M_{1} a_{1} = M_{2} a_{2} \ \ ,
\end{equation}

</div>

where a<sub>1</sub> + a<sub>2</sub> = a. If we know the distance d to the binary (d &Gt; a, so
we can consider both stars at the same distance), then the angular
size of the ellipse that each stars traces on the orbit of the sky is
&alpha;<sub>j</sub> = a<sub>j</sub>/d for j=1,2. In reality, the orbit is typically not on the
plane of the sky, but it has an inclination! This means what we can
see is not a<sub>j</sub> but the projection of it on the plane of the sky a<sub>j</sub>
sin(i). We can then solve these two equations for the individual
stellar masses (just having observations long enough to trace the
semi-major axes of wide visual binaries and knowing their distances,
for example because we have parallax measurements).

**N.B.:** even without knowing the distance d, using
Eq. \ref{eq:semimajor_axes} one can still determine the mass ratio q=M<sub>2</sub>/M<sub>1</sub>!


<a id="orgb9fdbad"></a>

### Spectroscopic (and eclipsing) binaries

In this case, we have access to more information thanks to the
variable "radial velocity/ies" (RV) of the stars, that is the
measurable Doppler shift of their spectral lines due to the orbital
motion.

However, what we can see though this is only the *projected* orbital
motion along the line of sight (because we only get Doppler shift
along the line of sight), this is why the terminology is "radial
velocities": it's velocities along the radii of the celestial sphere
centered on the observer!

Following standard nomenclature, let's call z the direction of the
line of sight, using xy for the plane of the sky. By definition the
radial velocity of each star is dz/dt. &nu; here is the true anomaly
(such that d&nu;/dt = n), &omega; is the argument of periastron - that is the
angle between the line of nodes (line where the plane of the sky,
assumed to contain the focus of the ellipse, and the plane of the
orbit intersect) and the direction of periastron.

![img](./images/bin_orbit.png "Geometry of a binary orbit. This is Fig. 3.3 in Tauris & van den Heuvel 2023 book.")

The one can calculate: z= rsin(i) sin(&nu;+&omega;) with r radius of the orbit
(which for an elliptical orbit is a function of time), the sin(i)
factor projects it on the plane of the sky and the sin(&nu;+&omega;) projects
on the line of sight. The radial velocity is therefore:

<div class="latex" id="org1188be0">
\begin{equation}\label{dzdt}
\frac{dz}{dt} = \left(r \cos(\nu+\omega)\frac{d\nu}{dt}+\frac{dr}{dt}\sin(\nu+\omega)\right)\sin(i) \ \ .
\end{equation}

</div>

**N.B.:** For a Keplerian, non-precessing, unperturbed orbit, &omega; is a constant.

Using Kepler's second law

<div class="latex" id="org44a3675">
\begin{equation}
\label{eq:Kepler2}
\frac{1}{2}r^{2}\frac{d\nu}{dt} = \frac{\pi ab}{P} = \frac{\pi a^{2} \sqrt{1-e^2}}{P} \ \ ,
\end{equation}

</div>

where P is the orbital period, a and b are semi-major and semi-minor
axes, and

<div class="latex" id="org97c3898">
\begin{equation}
e = \sqrt{1-b^{2}/a^{2}} \ \ ,
\end{equation}

</div>

is the eccentricity, and the relation between r&equiv; r(&nu;) for an ellipse:

<div class="latex" id="org57586a7">
\begin{equation}
r = \frac{a(1-e^{2})}{1+e\cos(\nu)} \ \ ,
\end{equation}

</div>

one can finally rewrite the radial velocity from Eq. \ref{dzdt} as

<div class="latex" id="orga25c33a">
\begin{equation}\label{eq:vrad}
v_\mathrm{rad} = \frac{dz}{dt} = K (ecos(\omega)+cos(\omega+\nu)) \ \
\end{equation}

</div>

where

<div class="latex" id="org34ea37b">
\begin{equation}
 K = \frac{2\pi a\sin(i)}{P\sqrt{1-e^{2}}} \ \,
\end{equation}

</div>

is the so-called *semi-amplitude* of the radial velocity, which apart
from the sin(i) factor depends only on observable quantities if one
can get spectra of many epochs (i.e., return to take spectra of the
same binary at many times, typically at least 7 spectra are required
for a decent fit to all these parameters):

-   P &rarr; from the time interval between repeating identical spectra
-   e &rarr; from the shape of the measured radial velocities as a function
    of time (i.e., radial velocity curve)
-   &omega; &rarr; similarly as e, it influences the shape of the radial velocity
    curve and can be deduced from it
-   $a\sin(i)$ &rarr; if the binary is SB2, then we can measure $K_{1}\equiv K_{1}(a_{1})$
    and $K_{2 }\equiv K_{2} (a_{2})$ and use the relation between $a_{1}+a_{2} = a$ to work
    out asin(i)
-   &nu; &rarr; this is less directly obtained by performing an orbital fit
    using other orbital parameters (mean anomaly and eccentric anomaly)

**N.B.:** In a real observation, one also needs to remove the component
along the line of sight due to the motion of the Earth around the Sun,
and the peculiar motion of the Sun (i.e., $v_\mathrm{rad}$ from Eq. \ref{eq:vrad}
$\rightarrow v_\mathrm{rad}-\gamma$ with &gamma; peculiar velocity of the observer).

![img](./images/example_RV_curve.png "Example of a radial velocity curve for a *circular* (e=0) binary in the SMC from the presently ongoing BLOeM survey ([Shenar et al. 2024](https://ui.adsabs.harvard.edu/abs/2024A%26A...690A.289S/abstract)). Black data points are measurements of the radial velocity from one spectrum (one epoch), these are phase-folded (from the inferred period one can determine the phase of the binary at each epoch and use it as x-axis). The red curve is a best fit model with the gray band showing a 3&sigma; uncertainty. The bottom panel shows the residuals between the models and the observations. Credits: Dr. N. Britavskiy. For more examples, see also Fig. 1 and 2 in [Mahy et al. 2022](https://ui.adsabs.harvard.edu/abs/2022A%26A...664A.159M/abstract).")

**Q**: - how would the radial velocity curve above change qualitatively if
the orbit had an eccentricity (e&ne;0)?

Therefore, for an SB2 binary we can observe dz<sub>j</sub>/dt = v<sub>rad, j</sub> for
each j=1,2 star, and we can determine K<sub>1</sub> and K<sub>2</sub>. using Eq.
\ref{eq:Kepler3} multiplied by sin<sup>3</sup>(i) to make the projection of
the semi-major axis of the orbit on the line of sight, a &times; sin(i):

<div class="latex" id="org1dfbbb2">
\begin{equation}
   G(M_{1}+M_{2})\sin^{3}(i) = n^{2} a^{3} \sin^{3}(i) \ \ ,
\end{equation}

</div>

and using \ref{eq:semimajor_axes} rewritten as

<div class="latex" id="org9900e12">
\begin{equation}
  \frac{a_{1} \sin(i)}{a_{2} \sin(i)} = \frac{M_{2}}{M_{1}} \ \ ,
\end{equation}

</div>

we can solve for M<sub>j</sub>sin<sup>3</sup>(i), where except for the inclination angle of
the orbit, we have the masses! In the case of an *eclipsing SB2 binary*,
from the eclipses we can measure the inclination angle and obtain a
direct measurement of the masses. These are the most precise mass
measurements (so-called "dynamical masses", because they are based on
orbital dynamics). They are only possible thanks to the occurrence in
nature of stellar binaries!

**N.B.:** The highest stellar masses measured with these method are about
&sim;80M<sub>o</sub> in the eclipsing SB2 binary WR20a (e.g., [Raauw 2004](https://ui.adsabs.harvard.edu/abs/2004A%26A...420L...9R/abstract),
[Bonannos 2004](https://ui.adsabs.harvard.edu/abs/2004ApJ...611L..33B/abstract)).

In the case of an SB1 binary, when only one spectrum is visible, we
can write

<div class="latex" id="orgaabb1f4">
\begin{equation}
a = a_{1} +a_{2} = a_{1}(1 + \frac{a_{2}}{a_{1}}) = a_{1} (1 + \frac{M_{1}}{M_{2}}) = a_{1} \frac{(M_{1}+M_{2})}{M_{2}} \ \ .
\end{equation}

</div>

Thus, we can rewrite Eq. \ref{eq:Kepler3} &times; sin<sup>3</sup>(i) as

<div class="latex" id="org9865d54">
\begin{equation}
 (M_{1} +M_{2}) \sin^{3}(i) \frac{M_{2}^{3}}{(M_{1} +M_{2})^{3}} = \frac{n^{2}}{G}a_{1}^{3} \sin^{3}(i) \ \,
\end{equation}

</div>

where the r.h.s. depends only on observables, and thus this allow us
to derive observationally the mass function

<div class="latex" id="orge6f76b3">
\begin{equation}
f(M_{1}, M_{2}) = \frac{M_{2}^{3 }\sin^{3}(i)}{(M_{1} + M_{2})^{2}} \ \ ,
\end{equation}

</div>

which together with an estimate of the mass-ratio provides a limit on M<sub>2</sub>.


<a id="orge555307"></a>

## Mass-luminosity relation

Using systems for which this mass and radius measurements are
possible, we can derive empirical mass-luminosity and mass-radius
relations:

![img](./images/mass_lum_mass_r_rel_pols.png "Mass-luminosity and Mass-radius empirical relations for a set of well measured SB2 eclipsing binaries. This is Fig. 1.3 in Onno Pols' lecture notes")

In the best astronomical tradition, this was initially fit with a
powerlaw, but as the range of stellar masses explored grew, this
became a broken powerlaw:

<div class="latex" id="org76892a5">
\begin{equation}
 L \propto M^{x}
\end{equation}

</div>

with x=4 for M&le;0.8M<sub>o</sub>, x=3 for 0.8M<sub>o</sub> <M<50M<sub>o</sub>, x=1 for M&ge;
50M<sub>o</sub>. These thresholds are extremely approximated, probably
metallicity dependent, as we will possibly see later in the course.
Moreover, and importantly, these hold only for so-called "main
sequence" stars, the one following also the L(T<sub>eff</sub>) relatively tight
relation on the color-magnitude diagram: evolved stars are a different
problem!


<a id="org2d06ecf"></a>

# Homework


<a id="org30845f1"></a>

## Exercise 7.4 on Carroll & Ostie

Sirius is a visual binary with a period of 49.94 yr. Its measured
trigonometric parallax is 0.37921" &plusmn; 0.00158" and, assuming that the
plane of the orbit is in the plane of the sky, the true angular
extent of the semimajor axis of the reduced mass is 7.61". The ratio
of the distances of Sirius A and Sirius B from the center of mass is
a a<sub>A</sub> /a<sub>B</sub> = 0.466.

1.  Find the mass of each member of the system.
2.  The absolute bolometric magnitude of Sirius A is 1.36, and Sirius B
    has an absolute bolometric magnitude of 8.79. Determine their
    luminosities. Express your answers in terms of the luminosity of
    the luminosity of the Sun
3.  The effective temperature of Sirius B is approximately 24790 K &plusmn;
    100 K. Estimate its radius, and compare your answer to the radii
    of the Sun and Earth. What kind of star is that hot with that radius?


<a id="org8fe5d1b"></a>

## Exercise 7.6 on Carroll & Ostie

From the light and velocity curves of an eclipsing, spectroscopic
binary star system, it is determined that the orbital period is 6.31
yr, and the maximum radial velocities of Stars A and B are 5.4 km s<sup>-1</sup>
and 22.4 km s<sup>−1</sup>, respectively. Furthermore, the time period between
first contact and minimum light (t<sub>b</sub> − t<sub>a</sub>) is 0.58 days, the length
of the primary minimum (t<sub>c</sub>− t<sub>b</sub>) is 0.64 days, and the apparent
bolometric magnitudes of maximum, primary minimum, and secondary
minimum are 5.40 magnitudes, 9.20 magnitudes, and 5.44 magnitudes,
respectively. From this information, and assuming circular orbits,
find:

1.  Ratio of stellar masses
2.  Sum of the masses (assume i = 90 degrees)
3.  Individual masses
4.  Individual radii (assume that the orbits are circular)
5.  Ratio of the effective temperatures of the two stars

