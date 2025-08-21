
# Table of Contents

1.  [Microphysics of nuclear burning](#org3661c6d)
    1.  [Summary of where we are](#org5bdfc2f)
        1.  [Mass conservation](#orgb8b66bb)
        2.  [Hydrostatic equilibrium](#org098b251)
        3.  [Equation of state](#orgaf1c396)
        4.  [Energy transport](#org2b68667)
        5.  [Energy conservation](#orgb70e4a9)
    2.  [The next step](#org5e543f3)
    3.  [Energy generation as a self-regulating process](#orgc1dcfb8)
    4.  [The nuclear timescale](#org3f410be)
    5.  [The energy reservoir: binding energy per nucleon](#org676c309)
        1.  [Q-value](#orgfee605b)
    6.  [Variety of possible nuclear reactions](#org9ccfe42)
        1.  [Charged-particles reactions](#org082b7dd)
        2.  [Reactions involving neutrons](#org2debdad)
        3.  [Weak reactions](#orgf3d8adb)
        4.  [Photodisintegrations](#orga3ca2f7)
    7.  [Nuclear reactions in stars](#org726ff57)
    8.  [Charged particle reactions](#org4f28a9c)
        1.  [Bohr's approximation](#orga03ff23)
        2.  [Electromagnetic potential term](#orge929dcd)
        3.  [Nuclear potential term](#org184dcc9)
        4.  [Combining electromagnetic and nuclear potential](#org2817e8f)
        5.  [Impossibility of nuclear reactions without QM](#org7906fc2)
        6.  [Charged particles reactions tunneling through the Coulomb barrier](#orgb2bc9d9)
    9.  [Thermonuclear reaction rates](#org3d36e6c)
2.  [Nuclear physics in stellar evolution codes](#org8e542bf)
3.  [Composition changes and stellar *evolution* term](#orgf5d8a52)
4.  [Appendix: Nuclear liquid drop model](#org3c30fb7)

**Materials:** Onno Pol's lecture notes Chapter 6.1 and 6.2, Kippenhahn
book Chapter 9 and 18, Cox & Giuli vol. I, Chapter 17.7, Clayton
Chapter 4, [Gamow 1928](https://ui.adsabs.harvard.edu/abs/1928Natur.122..805G/abstract), [Arnould & Takahashi 1999](https://ui.adsabs.harvard.edu/abs/1999RPPh...62..395A/abstract), [Jose & Iliadis 2011](https://ui.adsabs.harvard.edu/abs/2011RPPh...74i6901J/abstract)


<a id="org3661c6d"></a>

# Microphysics of nuclear burning


<a id="org5bdfc2f"></a>

## Summary of where we are

We have four equations of the stellar *structure* assuming spherical
symmetry, LTE, and hydrostatic ($\partial t \equiv 0$) equilibrium:


<a id="orgb8b66bb"></a>

### Mass conservation

<div class="latex" id="org7ee132d">
\begin{equation}\label{eq:mass_cont}
\frac{dr}{dm} = \frac{1}{4\pi r^{2}\rho}\ \ .
\end{equation}

</div>


<a id="org098b251"></a>

### Hydrostatic equilibrium

<div class="latex" id="orgfe9eadc">
\begin{equation}\label{eq:HSE}
\frac{dP}{dm} = -\frac{Gm}{4\pi r^{4}} \ \ ,
\end{equation}

</div>

which follows from the momentum conservation equation.


<a id="orgaf1c396"></a>

### Equation of state

<div class="latex" id="orgc2f68f1">
\begin{equation}
P_\mathrm{tot} = P_\mathrm{gas} + P_\mathrm{rad} = \frac{\rho}{\mu m_{u}}k_{B}T + P_{QM} + \frac{1}{3}aT^{4}  \ \ .
\end{equation}

</div>


<a id="org2b68667"></a>

### Energy transport

<div class="latex" id="orge61c165">
\begin{equation}
\frac{dT}{dm} = \frac{T}{P}\frac{dP}{dm}\nabla
\end{equation}

</div>

where $\nabla =\partial log(T)/\partial log(P)$ is the local temperature gradient, equal to
the radiative gradient in stably stratified regions:

<div class="latex" id="org66634f2">
\begin{equation}
\nabla \equiv \nabla_\mathrm{rad} = \frac{3 P}{16\pi acGm T^{4}}\kappa L
\end{equation}

</div>

with $\kappa = (1/\kappa_\mathrm{rad} + 1/\kappa_\mathrm{cond})^{-1}$ the combination
"in parallel" of the radiative and conductive opacity (assumed to be
known from atomic physics), and $L$ total luminosity in a radiative
region. In convective regions, $\nabla \equiv \nabla_\mathrm{ad}$ is the adiabatic
gradient (within &sim;10<sup>-7-8</sup> precision). We also
have a criterion (Schwarzschild or Ledoux) to determine which region
is which.


<a id="orgb70e4a9"></a>

### Energy conservation

<div class="latex" id="orge5655ae">
\begin{equation}
\frac{dL}{dm} = \varepsilon_\mathrm{nuc} -\varepsilon_{\nu} + \varepsilon_\mathrm{grav} \ \ .
\end{equation}

</div>

with $\varepsilon_\mathrm{grav} = T\partial s/\partial t$ the change in internal energy (typically &cong; 0 in
gravothermal equilibrium, that is for phases when the evolution is
much slower than $\tau_{KH}$), and $\varepsilon_{\nu}>0$ (neutrinos are an energy loss term).


<a id="org5e543f3"></a>

## The next step

With all the equations above we almost have a complete set of solvable
differential equations. What is left to discuss is the specific energy
generation per unit time $\varepsilon_\mathrm{nuc}$ due to nuclear burning
(which will occupy us in this and [the next lecture](./notes-lecture-nuclear-cycles.md)) and the specific
energy loss rate $\varepsilon_{\nu}$ due to neutrino losses (which we will treat
[later](./notes-lecture-neutrinos.md)).

In doing so, we will introduce another time-dependent equation
(besides the implicit dependence in $\varepsilon_\mathrm{grav}$): as nuclear
burning proceeds, the chemical composition changes, on a timescale
that we will see is extremely long compared to the thermal and
dynamical timescales.


<a id="orgc1dcfb8"></a>

## Energy generation as a self-regulating process

We have seen in the [virial theorem lecture](./notes-lecture-VirTheo.md) that one can derive from
first principle that stars have a "negative heat capacity" and obtain
a scaling between mass, radius and average temperature:

<div class="latex" id="org1a42007">
\begin{equation}
\langle T \rangle = \frac{2\mu m_{u}}{3} C \frac{GM^{}}{R} \propto \frac{\mu M}{R} \ \ ,
\end{equation}

</div>

where C was a constant depending on the details of the mass
distribution.

The star has a finite temperature, thus it radiates away thermal
energy at the surface in the form of a luminosity $L$. This means the
gravitational potential energy is decreasing (because of the virial
theorem!), thus it must contract leading to an increase in $T$. For
the Sun this would go on for &sim; 15 Myrs before it runs out of all of
its internal energy, which is way too short a timescale to explain
many Earthly observables.

We know this must stop either because the ideal gas EOS does not work
(QM effects &rarr; degeneracy pressure &rarr; white dwarfs), or because some
other energy source intervenes, balancing out the energy losses at the
surface. *Stars don't shine because they burn, stars burn because they
shine*.

Initially, people considered chemical reactions and radioactivity as a
possible energy sources, but it was shown very quickly that these are
insufficient.

-   **Q**: how would you show that these sources are insufficient? (**Hint**:
    consider the $\phi$ factor for the amount of mass released in the
    equations below)

It took major advances in quantum mechanics (QM) and
their application to atomic and nuclear theory to work out in the late
1930s that the energy source is nuclear burning, a result obtained by
[Hans Bethe](https://en.wikipedia.org/wiki/Hans_Bethe) and
collaborators.

In a sense, you can think  of a star as an *inertial confinement nuclear
reactor* where the confinement is provided by the self-gravity. This
also implies that nuclear burning in a star is a *self-regulating*
process: because nuclear reactions are a consequence of the energy
losses, during long-lived equilibrium phases of the stellar life, they
produce just enough energy to balance the losses! In other words,
$L_\mathrm{nuc} = L ( + L_{\nu})$.

If a star were to not produce enough energy to verify that (i.e.,
$L>L_\mathrm{nuc}$), then it will lose too much energy, meaning it
will contract, and increase it's temperature because of the virial
theorem, which in turn regulates the energy generation by nuclear
reactions (as we will see in a moment), until $L_\mathrm{nuc}$ reaches
$L$. Viceversa, if $L_\mathrm{nuc} > L$ for some reason (e.g., there
is a thermonuclear explosion in the star), than the extra energy
release will do work on the stellar gas and cause an expansion of the
star: by the virial theorem, an increase in $R$ lowers the mean
temperature until $L_\mathrm{nuc} = L$.


<a id="org3f410be"></a>

## The nuclear timescale

Naturally, nuclear energy generation consumes nuclear fuel: to provide
$L_\mathrm{nuc}$ the composition of the star slightly changes in time.
This drives the *evolution* of star.

We can estimate the timescale for this assuming the star is in
gravothermal equilibrium, so $L=L_\mathrm{nuc}$. The *nuclear timescale*
is the time it takes to lose the energy generated by nuclear
reactions:

<div class="latex" id="orgb5d1d2a">
\begin{equation}
\tau_\mathrm{nuc} = \varphi f_\mathrm{burn} \frac{Mc^{2}}{L_\mathrm{nuc}} \equiv \varphi f_\mathrm{burn} \frac{Mc^{2}}{L_{}} \ \ ,
\end{equation}

</div>

where $\phi$ is the fraction of rest mass of nuclei converted in energy
by nuclear burning, $f_\mathrm{burn}$ is the fraction of the stellar
mass $M$ that is affected by burning (we need a stellar model to
estimate that). For the Sun, $f_\mathrm{burn} \simeq 0.1$ from detailed
models (as you can verify with your `MESA-web` model!).

The fraction $\phi$ depends on the nuclear physics details. For hydrogen
burning into helium (the two lightest elements), the proton mass is $m_{p}
= 1.0081 m_{u}$ (where the atomic mass unit $m_{u}$ is defined in such a way
that the mass of $^{12}\mathrm{C}$ is exactly 12$m_{u}$ - this is more
convenient to measure experimentally to make a standard), and the mass
of helium 4 is $m(^{4}He) = 4.0039 m_{u}$, so the fraction of rest mass of 4
protons turning into a helium nucleus is:

<div class="latex" id="org1a2d21c">
\begin{equation}\label{eq:mass_defect}
\varphi = \frac{4m_{p} - m(^{4}\mathrm{He})}{4m_{p}} = \frac{2.85 \times 10^{-2} m_{u} c^{2}}{4m_{p}} \simeq 0.007 \ \ .
\end{equation}

</div>

Plugging in $\phi$ and $M_{\odot}$ and $L_{\odot}$ we get for the nuclear
timescale:

<div class="latex" id="org46dbffb">
\begin{equation}\label{eq:tau_nuc_scaling}
\tau_\mathrm{nuc} \simeq 10^{10} \frac{f_\mathrm{burn}}{0.1} \frac{M}{M_{\odot}} \frac{L}{L_{\odot}} \ \mathrm{yr} \ \ .
\end{equation}

</div>

So we now have estimates that allow us to see the complete
ordering for the main *global* timescales for stellar evolution:

<div class="latex" id="orgf50470f">
\begin{equation}\label{eq:timescale_ordering}
\tau_\mathrm{ff} \ll \tau_\mathrm{KH} \ll \tau_\mathrm{nuc} \ \ .
\end{equation}

</div>

Moreover, Eq. \ref{eq:tau_nuc_scaling} shows that when accounting for
nuclear energy generation (which we have implicitly assumed here to
give a value of &phi;), the nuclear timescale matches the timescale found
from geological evidence on Earth, and the ordering in
\ref{eq:timescale_ordering} tells us that the evolution of the Sun is
on a very slow timescale compared to thermal and dynamical timescale,
validating the assumptions we made so far to derive the equations for
stellar *structure* and allowing for a *quasi-static* approximation to
deal with the stellar *evolution*.

Let's now dive into the details of the nuclear physics that allow for
nuclear burning.


<a id="org676c309"></a>

## The energy reservoir: binding energy per nucleon

The energy reservoir that stars tap into is the nuclear binding
energy: nuclear reactions rearrange nucleons in nuclei to create more
bound configuration and extract binding energy as heat source.
Therefore, it is useful to consider the nuclear binding energy per
nucleon of all nuclei in the periodic table:

![img](./images/nuclear_binding.png "Nuclear binding energy per nucleon as a function of atomic mass $A=Z+N$, where $Z$ is the number of protons and $N$ the number of neutrons (therefore $A$ is the total number of baryons in a given nucleus, and $A\times m_{u}$ the mass). From [Renzo 2015](https://etd.adm.unipi.it/theses/available/etd-05062015-125630/unrestricted/Thesis_colored_10052015.pdf).")

This plot shows empirical data, and there are several notable features
coming from the internal structure of the nuclei that any model of
nuclear (strong) interactions needs to explain:

-   the binding energy per nucleon raises sharply with $A$ among the light
    nuclei;
-   the helium nucleus ($\alpha$ particle) has an exceptionally high binding
    energy per nucleon of &sim; 7.5MeV/nucleon;
-   there are peaks for nuclei with $A$ divisible by 4 and $N=Z$, that
    is nuclei that can be approximately thought as bound collections of
    $\alpha$ particles (for example $^{12}\mathrm{C}$ &sim; 3 $\alpha$ particles bound
    together, $^{16}\mathrm{O}$ &sim;4 $\alpha$ particles, etc..);
-   the nuclear binding energy is roughly constant at about &sim;
    8MeV/nucleon for most heavy nuclei;
-   the slight drop in $B/A$ after the maximum is caused by the Coulomb
    repulsion between the protons in heavy nuclei, and this is why those
    nuclei require a higher number of neutrons than protons to hold
    together, $N>Z$.
-   there is a local *maximum* of the binding energy per nucleon at the
    iron group, around $^{56}\mathrm{Fe}$ and $^{62}\mathrm{Ni}$.

The presence of a maximum implies that there cannot be energy release
from the *fusion* of nuclei heavier than iron: indeed those heavy nuclei
are typically fuel for nuclear fission reactors, where energy is
extracted breaking them apart. Stars, which do nuclear burning to
*release* energy and balance the losses at the surface, have no interest
in producing element heavier than iron during their stable/hydrostatic
lifetime. The question of the formation of elements heavier than iron
(which clearly exist!) is something that is actively worked on and
requires out-of-equilibrium processes that can only occur in the
presence of a neutron rich environment (e.g., AGB stellar winds,
neutron stars interacting with something else, etc.) - see also
[possible literature review projects](./projects.md).

Conversely, moving rightward on this chart, by fusing together light
nuclei, stars can release nuclear binding energy and sustain
themselves. This is also convenient since stars are mostly made of H
and He, so they have a lot of light elements available as energy
sources.

The change in binding energy per nucleon $\Delta(B/A)$ is what powers
stars, and we can write the binding energy as the difference between
the sum of the masses of the $Z$ protons ($m_{p}$) and $N=A-Z$ neutrons
($m_{n}$) minus the mass of the nucleus (measured experimentally):

<div class="latex" id="org94127c5">
\begin{equation}
B = \left(Zm_{p}+(A-Z)m_{n} - m_\mathrm{nucleus}\right)c^{2} \simeq \left(Zm_{H}+(A-Z)m_{n} - m_\mathrm{nucleus}\right)c^{2} >0 \ \ ,
\end{equation}

</div>

which is a positive quantity precisely because the strong interaction
between protons and neutrons keeps them bound. In the second step, we
approximate the proton mass with the hydrogen atom mass, making a
mistake of the order of &sim; 10 eV by neglecting the binding energy of
the electron (which is acceptable since we are dealing with MeV =
10<sup>6</sup>eV as the relevant nuclear scale).

Because of the apparent peaks in the $B/A$ vs. $A$ curve, stars will
tend to produce more of the elements with the most tight nuclei, whose
production releases more energy! *The nuclear structure determines the
most abundant chemicals in the Universe*.

Moreover, from the fact that there is a sharp jump form H to He, and
then the curve rapidly flattens, we know that the rate at which nuclei
are converted to achieve the equilibrium condition $L_\mathrm{nuc} = L$ will be
slower when H is converted into He, and then it will need to rapidly
speed up when He is converted in carbon and onwards (because the
energy release per nucleon significantly drops lowering the factor $\phi$
in $\tau_\mathrm{nuc}$).

In the very late evolutionary phases (post helium burning), the
required burning rate may become so high that $\tau_\mathrm{nuc}$ becomes shorter
than the *global* thermal timescale (but luckily not of the *local*
thermal timescale, so all the equations we have derived so far still
hold, since they are differential equations that describe *local*
quantities). We will return on this [later](https://www.as.arizona.edu/~mrenzo/materials/cores_of_massive_stars.pdf).


<a id="orgfee605b"></a>

### Q-value

For any nuclear reaction that may happen $a+X \rightarrow b+Y$ with $a, b, X, Y$
generic particles, it is useful to define the so called $Q$ value as the
mass difference between the reagents and the products:

<div class="latex" id="org079b738">
\begin{equation}
Q = \left((m_{a} + m_{X}) -(m_{b} + m_{Y}) \right)c^{2} = \Delta\left(\frac{B}{A}\right) \ \ ,
\end{equation}

</div>

which, if $Q>0$ is the energy *released* by the reaction which is thus
*exoenergetic* - of the kind that stars need to generate energy and
sustain themselves against gravity, or if $Q<0$ is the energy input
needed to get the *endoenergetic* reaction going (e.g. thermonuclear
fusion of iron).

**N.B.:** In exoenergetic nuclear reactions, the energy release comes from
the *mass defect*, caused by the increase in binding energy per nucleon:
the total mass of the outgoing particles is lower than the ones
incoming because their binding energy is higher or in other words
their total energy is more negative.

The energy release by nuclear reaction per unit time and unit mass is
just:

<div class="latex" id="orga653a75">
\begin{equation}\label{eq:eps_nuc}
\varepsilon_\mathrm{nuc} = \sum_{i} \frac{Q_{i} r_{i}}{\rho} \ \ ,
\end{equation}

</div>

where the sum runs over all the possible reactions, $r_{i}$ is the rate per
unit time and volume of the reactions, and the division by the mass
density $\rho$ gives the right dimensions [$\varepsilon_\mathrm{nuc}$] = [E]/([t][M]).

So, what is left to do is calculate the volumetric reaction rate $r_{i}$
that can occur in a star.


<a id="org9ccfe42"></a>

## Variety of possible nuclear reactions

A generic nuclear reaction $X+a \rightarrow Y+b$ is often written as $X(a,b)Y$
to make it easy to express chains of reactions, e.g.,
$X(a,b)Y(c,d)Z(e,f)A$&#x2026;

Depending on the nature of the incoming particle ($X$ and $a$ in our
generic reaction), or in other words on the microphysics that
determines the interaction, there can be of various kinds of
reactions.


<a id="org082b7dd"></a>

### Charged-particles reactions

When $X$ and $a$ are charged nuclei, then the reaction can only occur
if something allows them to overcome the Coulomb repulsion. These can
be resonant or not (the distinction will come back later).

Example:

<div class="latex" id="org603a50c">
\begin{equation}
 ^{12}\mathrm{C}(\alpha,\gamma)^{16}\mathrm{O}
\end{equation}

</div>


<a id="org2debdad"></a>

### Reactions involving neutrons

In this case the force involved is the strong force, and there is no
Coulomb repulsion to overcome. However, these require an environment
that is neutron rich, which is astrophysically a rare occurrence,
since the neutron is an unstable particle that decays in &sim;15 min to a
proton $n\rightarrow p+e^{-}+\bar{\nu_{e}}$. This half-life however can significantly
change for neutrons bound in nuclei as opposed to free neutrons, that
is the $\beta^{-}$ decay time of a neutron rich nucleus can be much longer
than the half-life of a free neutron.

Depending on the available flux of neutrons in the environment, we
distinguish:

-   **r-process** for rapid neutron captures (i.e., the rate of neutron
    captures is high w.r.t. the rate of neutron decays)
-   **s-process** for slow neutron captures (i.e., each nucleus captures at
    best one neutron before decaying).

These processes are involved in the formation of  elements heavier
than iron, but they require particular astrophysical environment
(e.g., the merger of two neutron stars or a neutron star with the core
of another star, or the envelope of an AGB star or the core of a fast
rotating massive star).


<a id="orgf3d8adb"></a>

### Weak reactions

These can typically be spotted by the presence of a neutrino and/or
the conversion of a nucleon from one eigenstate of isospin to another
(in simpler words: the conversion of a proton into a neutron or
viceversa).

Example:

<div class="latex" id="org1ec090a">
\begin{equation}
p+e^{-} \rightarrow n+\nu_{e} \ \ \mathrm{or} \ \ p(e^{-},\nu_{e})n
\end{equation}

</div>


<a id="orga3ca2f7"></a>

### Photodisintegrations

When one of the particles is a photon and the outgoing particles can
be seen as "fragments" of the ingoing nucleus. These require very
energetic incoming $\gamma$ ray photons, because their energy needs to be
comparable to the binding energy of nuclei, of the order of &sim;8MeV &times; A.
This can occur for example at the very late moments of massive star
evolution.

Example:

<div class="latex" id="org6ac0c48">
\begin{equation}
^{56}\mathrm{Fe}+\gamma \rightarrow 14\alpha
\end{equation}

</div>


<a id="org726ff57"></a>

## Nuclear reactions in stars

All of the types of reactions listed above (and more) can occur at
some point in the evolution (and explosion!) of stars. For example,
during hydrogen core burning (which we have used to estimate &phi; and
thus $\tau_\mathrm{nuc}$) the star burns 4 protons into &alpha; particles:

<div class="latex" id="org207cf1c">
\begin{equation}\label{eq:overall_h_burn}
4^{1}\mathrm{H}\rightarrow^{4}\mathrm{He}+2e^{+} + 2\nu_{e} \ \ ,
\end{equation}

</div>

where the positrons need to be there to conserve electric charge
throughout the process, and the neutrinos need to be there for
conserving the leptonic number (<del>1 for the leptons electron $e^{-}$, muon
$\mu^{-}$, tau $\tau^{-}$ and the corresponding neutrinos $\nu_{e}$, $\nu_{\mu}$, $\nu_{\tau}$ and -1
for their antiparticles positron $e^{</del>}$, positive muon $\mu^{+}$, and positive
$\tau^{+}$ and the corresponding antineutrinos).

**N.B.:** because of the phenomenon of neutrino oscillations (i.e., the
conversion of $\nu_{e} \leftrightarrow \nu_{\mu}$ or $\nu_{\tau}$) the leptonic
number conservation of each flavor ($e$, $\mu$, and $\tau$) is not exact in
nature, or in other words, the symmetry associated to this
conservation law is not exact. While this was discovered through the
"[missing solar neutrinos problem](https://www.nobelprize.org/prizes/themes/solving-the-mystery-of-the-missing-neutrinos/)", and it is thus related to
stellar/solar physics, it requires the propagation of neutrinos over
distances much longer than the size of nuclei, therefore, for the
purpose of treating nuclear reactions we can assume conservation of
the leptonic number of each species individually (while in the general
case only the *total* leptonic number summed over all flavors $e$, $\mu$,
and $\tau$, is conserved).

From Eq. \ref{eq:overall_h_burn} we can see that:

-   protons need to encounter each other. Statistically, 4 protons are
    unlikely to meet each other at a point in space for reaction Eq.
    \ref{eq:overall_h_burn} to occur. Eq. \ref{eq:overall_h_burn} is a
    compound reaction that "summarizes" the more complex burning
    process of H into He that we will detail [later](./notes-lecture-nuclear-cycles.md). Nevertheless, the
    process will necessarily involve charged particle reactions.
-   $\nu_{e}$ appear &rArr; there will be weak reactions involved
-   as already seen earlier, we can calculate the $\phi$ factor (cf. Eq.
    \ref{eq:mass_defect}), and thus the $Q$ value for the overall
    reaction $Q_\mathrm{H burn} \simeq 26.5$ MeV. Note that the $Q$ value
    does not really depend on the details of the burning process.

**N.B.:** we discuss Eq. \ref{eq:overall_h_burn} because H is the most
abundant element in the Universe, that most stars are made of, and
thus this is (typically) the first process occurring in stars. It is
also the one with the highest $Q$ value (cf. $B/A$ vs. $A$ plot!),
thus the one that for a given luminosity $L$ of the star can proceed at
the slowest rate and last the longest.


<a id="org4f28a9c"></a>

## Charged particle reactions

For the rest of this lecture we will focus mostly on charged particle
reactions: as we just saw these are involved since H core burning, and
they are the main reactions during the hydrostatic lifetime of stars.
Moreover, breakthroughs in QM (by [George Gamow](https://en.wikipedia.org/wiki/George_Gamow)) applied
to the interaction of charged particles are what opened the way to the
discovery that the energy source in stars are nuclear reactions.


<a id="orga03ff23"></a>

### Bohr's approximation

To discuss them, we will implicitly use *Bohr's approximation*, which is
not a completely accurate physical picture, but it is intuitive and
allows to describe the main processes occurring in nuclei. In this
approximation, we treat the generic reaction between charged particles
$X(a,b)Y$ as if it went through an intermediate step of forming a
compound nucleus $C$:

<div class="latex" id="org87fb803">
\begin{equation}
X + a \rightarrow C^{\star} \rightarrow Y + b \ \ ,
\end{equation}

</div>

where the nucleus $C$ is formed in an excited state $C^{\star}$ since in
the reference frame of $X$ the particle $a$ arrives with its own
kinetic energy and internal binding energy that (together with $X$'s
internal energy) are generally not exactly the total energy for the
compound nucleus $C$.

The second step is the decay of this fictional compound excited
particle $C^{\star}$ in the products $Y$ and $b$.

In this approximation, the second step of the decay does *not* depend on
the first step (in other words, $C^{\star}$ loses the memory of how it
formed) as long as the half-life of $C^{\star}$ is long compared to the
light-crossing time of $C^{\star}$ itself. This is because we consider
charged particles by hypothesis, so electromagnetic forces mediated by
photons are what determines the interactions of the building blocks of
$C^{\star}$, and on a timescale long compared to the light-crossing time
they will equilibrate and lose memory of how they came to be.

The light crossing time of a nucleus can be estimated starting from
the experimental result on the size of nuclei (something that also
needs to be explained by models of the strong force):

<div class="latex" id="orge69b443">
\begin{equation}
r_{n} = r_{0} A^{1/3} \simeq 1.4 \times 10^{-13} A^{1/3} \ \mathrm{cm} \Rightarrow \tau_\mathrm{light\ cross} = \frac{r_{n}}{c} \simeq 10^{-23} A^{1/3} \ \mathrm{s} \ \ .
\end{equation}

</div>

Any compound nucleus $C^{\star }$ with lifetime longer than this allows
us to use this two step approximation to treat the problem, where the
two incoming particles $X$ and $a$ come "into contact" (i.e., within their
$r_{n}$), form an excited compound nucleus $C^{\star}$, which then de-excites in
the final products $Y$ and $b$ independently of how it formed.

**N.B.:** the nuclear radius dependence on $A$ can be flipped around to
infer that the average density of nuclei is constant as $A$ increases:
$\rho_{n} \simeq Am_{u} / (4\pi/3 \times r_{n}^{3}) \simeq 2\times10^{14} A$ g cm<sup>-3</sup>.

**N.B.:** this is necessarily an oversimplified picture, since nuclei are
described by QM and don't have a "hard" boundary at $r_{n}$, but rather
their constituent nucleons have decaying wave-functions that solve the
Schrodinger equation with the nuclear potential for their
interactions. In reality, each particle can be described as a wave
with De Broglie wavelength $\lambda = h/p$, and a physically more accurate
picture should treat all the particles involved accounting for their
wave nature.

To understand how two charged nuclei, both with positive charge, can
"come into contact" within $r_{n}$, we need to consider the potential
governing their interaction:

<div class="latex" id="org944e993">
\begin{equation}
V \equiv V(r) = V_\mathrm{EM} + V_\mathrm{nuc} + \frac{\ell(\ell+1)\hbar^{2}}{2m_{aX}r^{2}} \ \ ,
\end{equation}

</div>

where the last term is the centrifugal potential in the rest-frame of
the target nucleus $X$ which depends on the reduced mass $m_{aX} =
m_{a}m_{X}/(m_{a}+m_{X})$ and quantum number $\ell$ which determines the order of the
wave-function of the system $a+X$. For simplicity, we can limit
ourselves to consider $\ell=0$: we already have a repulsive Coulomb term
to win over, and any extra repulsive term such a centrifugal barrier
is only going to lower the reaction rate. The most important reactions
are going to have $\ell = 0$, that is head-on collisions between $a$ and $X$.


<a id="orge929dcd"></a>

### Electromagnetic potential term

For the electromagnetic term we can write:

<div class="latex" id="org77e2788">
\begin{equation}
V_\mathrm{EM} = \frac{Z_{a}Z_{X}e^{2}}{r} - \{\mathrm{electron\ screening\ term}\} \ \ ,
\end{equation}

</div>

where the first part is positive and describes the Coulomb repulsion
between the two nuclei of charge $Z_{a}e$ and $Z_{X}e$ (both positive), and
the electron screening term *reduces* the repulsion of the nuclei: in
the stellar plasma we expect each nucleus to be statistically
surrounded by a "cloud" of electrons of radius of the order of the
Debye length of the plasma:

<div class="latex" id="org52e2cfe">
\begin{equation}
r_\mathrm{Debye} = \sqrt{\frac{k_{B}T}{4\pi e N\chi}} \ \ ,
\end{equation}

</div>

where $N$ is the total number of particles in absence of screening
(nuclei/ions+electrons), and $\chi = \sum_{i} Z_{i}^{2} (N_{i}/N) + N_{e}/N$ with $N_{i}$ and
$N_{e}$ number of ions and electrons in absence of screening.

For distances $r \gg r_\mathrm{Debye}$ between $a$ and $X$ the electron
screening reduces the Coulomb repulsion between the nuclei.


<a id="org184dcc9"></a>

### Nuclear potential term

Finally, for the nuclear potential, there isn't a well known
functional form from first principles, and it is typically derived
experimentally. This is because the interactions between nucleons
(=protons and neutrons) cannot be treated in a perturbative theory of
the strong force. For more details than necessary to understand
thermonuclear reactions, see also [this appendix](#org3c30fb7) and nuclear physics
textbooks such as "*Introductory nuclear physics*" by K. Krane.

Besides the nuclear physics details here, the important point is that
the nuclear potential is going to be attractive at short range
($V_\mathrm{nuc}(r\le r_{n})<0$), but it has a repulsive core (that is
there is a certain $r_\mathrm{nuc,core}$ below which $V_\mathrm{nuc}$
becomes very large and positive), otherwise the nuclei would not have
a finite approximately constant density, and goes to zero at large
distances (the strong force has a short range).


<a id="org2817e8f"></a>

### Combining electromagnetic and nuclear potential

Putting things together we can sketch the following graph for the
potential felt by particle a and generated by the strong and
electromagnetic force by particle $X$:

-   at distances $r \gg r_\mathrm{Debye}$ electron screening nullifies the
    repulsive Coulomb potential
-   for a relative energy at infinity of $E$, there is a distance of
    classical minimum approach $r_{c }\equiv r_{c}(E)$
-   just outside $r_{n }\equiv r_{n}(A)$ there is the maximum height of the Coulomb barrier
    $E_{C} = Z_{a} Z_{X} e^{2}/r_{n}$.
-   inside $r_{n}$ (the nuclear radius of particle X), the potential is
    attractive, and allows for bound states with quantized energy levels.
-   if the two nuclei get too close to each other, there is a repulsive
    core of the nuclear force that dominates over any electromagnetic
    effect.
-   For $0<E<E_{c}$, there are *metastable* energy level possible (represented
    in the figure by the purple bands). What makes them metastable is also
    what allows nuclear burning: quantum tunnelling through the Coulomb
    barrier.

![img](./images/nuc_pot.png "Top: Interaction potential generated by the nucleus $X$ and felt by the nucleus $a$ considering nuclear and electromagnetic interactions. For $r>r_\mathrm{Debye}$ the potential deviates from a $r^{-1}$ Coulomb potential (sketched in red) because of electron screening. The gray vertical band marks the repulsive core of the nuclear force (necessary to obtain a constant nuclear density), purple shading marks metastable states of the compound nucleus $C^{\star}$ where $a$ is trapped inside the nuclear potential well of $X$. Bottom: qualitative sketch of the wave function of particle $a$ in the potential caused by particle $X$ (blue). The region between $r_{n}$ and $r_{c}$ is the "classically forbidden region". The wavefunction needs to be smooth at both those radii and the solution where quantum tunnelling succeeds allow for a large amplitude of the wave function inside $r<r_{n}$. Modified from Fig. 6.2 of Onno Pols' lecture notes.")


<a id="org7906fc2"></a>

### Impossibility of nuclear reactions without QM

Without QM, for a nuclear reaction to happen the two charged particles
would need a relative energy at infinity higher than the maximum of
the Coulomb barrier, so that $r_{c} \leq r_{n}$. Assuming the energy is just
coming from the thermal energy of the gas:

<div class="latex" id="orgc12ece2">
\begin{equation}
E \simeq k_{B} T \geq E_{C} = \frac{Z_{a}Z_{X}e^{2}}{r_{n}} \geq \frac{e^{2}}{r_{0}} \Rightarrow T\geq \frac{e^{2}}{r_{0} k_{B}} \simeq 10^{10} \ \mathrm{K} \ \ ,
\end{equation}

</div>

where we assume $Z_{a} = Z_{x} = A = 1$ to minimize the Coulomb barier, so
$r_{n} \equiv r_{0} = 1.3 \times 10^{-13}$ cm. The temperature threshold we
have derived is much larger than the mean temperature in the Sun as
estimated with the Virial theorem. It is also much larger than the
central temperature of the Sun which one could estimate assuming $\langle T
\rangle - T_{surf,\odot} \sim T_{center,\odot} - \langle T \rangle$. *The Sun is not
hot enough to have nuclear energy generation without QM*.

**N.B.:** In a nuclear fusion experiment energies $E\geq E_{C}$ are reached,
however, the beams are *not* in thermal equilibrium. The key point is
*laboratory nuclear physics experiment occur at much higher energies
than nuclear reactions in stars*.


<a id="orgb2bc9d9"></a>

### Charged particles reactions tunneling through the Coulomb barrier

The piece of puzzle that allows for charged particles nuclear
reactions in stars is the QM *tunnel effect*, which was studied in the
context of the $C^{\star} \rightarrow Y+b$ decay in [Gamow 1928](https://ui.adsabs.harvard.edu/abs/1928Natur.122..805G/abstract).

**N.B.:** the *tunnel effect* is a purely wave mechanics phenomenon that has
to do with constructive interference of waves. The QM element is that
the particles involved here are waves!

From QM, we know that in the "classically forbidden region", where $E<V$
(so the classical kinetic energy term in $E=K+V$ would be $K<0$), the wave
function can still be non-zero. To calculate the wave-function $\Psi$ of
particle $a$ in the potential of $X$, we can make the following ansatz:

-   in the classically allowed region $r\geq r_{c}$ the wave function will have
    the form of a propagating wave with phase dependent on $(E-V(r))^{1/2}$;
-   in the classically allowed region with $r\leq r_{n}$, we assume the same
    functional form;
-   in the classically forbidden region $r_{n}< r < r_{c}$, we will have a
    superposition of evanescent waves with exponentially decaying
    amplitude

**N.B.:** The math simplifies significantly using the WKB
approximation, that is writing $\Psi = \exp(\Phi)$ and solving for $\Phi$ instead of
$\Psi$.

By imposing that the wave function $\Psi$ and its derivative $\partial_{r}\Psi$ are
continuous at the boundaries $r_{c}$ and $r_{n}$ one can find solutions that
have a non-zero amplitude *inside* $r_{n}$, that is tunneling solutions! The
continuity of $\Psi$ depends on the phase at the boundaries, for specific
values of $E$ it is possible to obtain solutions, these typically
correspond to metastable energy levels of the potential, with energy
$E_\mathrm{metastable} \pm \Delta E$ and $\Delta E \sim h/\tau$ the "width" in
energy depending on the $\tau$ the half-life of the metastable state.

These states are metastable because a bound system between $a$ and $X$
(i.e., $C^{\star}$) can result in the tunneling of a out of the potential
of $X$ (the decay $C^{\star} \rightarrow a+X$).

Therefore, the nuclear reaction rates are going to be extremely
sensitive to the relative energy of $a$ and $X$: if this relative
energy $E$ hits a *resonance* of the compound state $C^{\star}$, that is if
$E \sim E_\mathrm{metastable}$, the wave function of the system has
non-zero amplitude inside the nucleus, and since the probability of
finding a within $r\le r_{n}$ is proportional to $||\Psi||^{2}$, this means there
will be a non-zero probability of forming the compound nucleus.

In proximity of a resonance the cross section takes the typical shape
of a Lorentzian with width determined by the energy width of the
metastable state $C^{\star{}}$:

<div class="latex" id="org939641b">
\begin{equation}
\sigma_\mathrm{nuc} \propto \frac{1}{(E-E_\mathrm{metastable})^{2} +\left(\frac{\Delta E}{2}\right)^{2}} \ \ .
\end{equation}

</div>

Conversely, for non-resonant reactions, since the thermal energies are
of order of 100 of eV while the nuclear scale is at &sim;10MeV we can
neglect the energy dependence of $\sigma_\mathrm{nuc}$.

Finally, actually carrying out the calculation give a probability of tunneling

<div class="latex" id="org47d8b00">
\begin{equation}
P\propto \exp\left(-\int_{r_{n}}^{r_c} \frac{\sqrt{2m_{aX} (V(r) - E)}}{\hbar} dr \right) \equiv P_{0} \exp\left(-\frac{b}{\sqrt{E}}\right) \ \ ,
\end{equation}

</div>

with $b = 2\pi Z_{a} Z_{X} e^{2} (m_{aX}/2)^{1/2} / \hbar$.

**N.B.:** Nuclear resonances allow stars to work, and for example the
existence of a specific resonance in the nucleus of $^{12}\mathrm{C}$
(Hoyle state) is what allows helium to burn into carbon and ultimately
allows for life (as we will see in more detail in the [next lecture](./notes-lecture-nuclear-cycles.md))!

However, because nuclear physics experiments operate at so much higher
energy than stars, extrapolating to lower relative energies is
complicated and dangerous: it is easy to miss an unknown resonance
that would change significantly the rate.


<a id="org3d36e6c"></a>

## Thermonuclear reaction rates

Now that we have discussed how a charged particle nuclear reaction is
possible through quantum tunneling through the Coulomb barrier, to
complete our quest for $\varepsilon_\mathrm{nuc}$ we need to obtain the rate per
unit volume and time of each possible nuclear reaction.

What brings together the generic nuclei $a$ and $X$, giving them the
energy $E$ such as the probability of tunneling through the Coulomb
barrier is not negligible is the thermal motion of the gas they
compose: this is why we talk about *thermonuclear* reactions in a star
(and why the energy scale for these reactions is much lower than the
energy scale in laboratory experiments).

Once again, to put together an expression for the nuclear reaction
rate we can start from dimensional analysis trying to combine the
available pieces:

-   number density of reactants [$n_{a}$] = [$n_{X}$] = [L]<sup>-3</sup>
-   their relative velocity [$v$] = [L]/[t] (which is related to their
    relative energy at infinity $E$ which is of the order of the thermal
    energy, $v\sim(2k_{B}T/m_{aX})^{1/2}$)
-   the cross section for the reaction [$\sigma$] = [L<sup>2</sup>] (whose calculation
    will depend on the details of the QM problem outlined above and we
    know will depend on the relative energy of the particles, and thus
    ultimately their relative - thermal - velocity at infinity): $\sigma \equiv
      \sigma(v)$

With these ingredients we can make a rate of the number of reactions
$X(a,b)Y$ per unit time and volume with:

<div class="latex" id="org2c60622">
\begin{equation}
r_{aX} = \sigma(v) v n_{a} n_{X}  \ \ ,
\end{equation}

</div>

where we implicitly assumes that $a \neq X$. However, in a star sometimes
there are reactions among identical particles (for example the weak
reaction $p+p\rightarrow D+e^{+} +\nu_{e}$). In such cases we should make sure to not
double count particle pairs, so we can write more generally:

<div class="latex" id="orgfa80827">
\begin{equation}
r_{aX} = \frac{1}{1+\delta_{aX}} \sigma(v) v n_{a} n_{X}  \ \ ,
\end{equation}

</div>

where $\delta_{aX} = 1 \Leftrightarrow a=X$. This would be the expression if all particles
had the same relative velocity v. In reality, we know the stellar gas
is pretty close to LTE and thus the distribution in energy of
particles is given by the Maxwell-Boltzmann distribution, and to get
the effective rate of reactions we need to integrate over that.

The relative velocity is $v=|v_{a} - v_{X}|$ (the velocities of the two
species can be different if they have different masses), and
substituting to the number density the integral over the velocities of
the phase space densities $n_{i} \rightarrow \int dn_{i}(v)$ (**N.B.**: we have
already done this many times when deriving the EOS, just in momentum
instead of velocity), our expression for the rate becomes:

<div class="latex" id="orgf3c7b5f">
\begin{equation}
r_{aX} = \frac{1}{1+\delta_{aX}}\int\int dn_{a}(v_{a}) dn_{X}(v_{X}) \sigma(v)v  \ \ ,
\end{equation}

</div>

where $dn_{i}(v_{i})$ are Maxwell-Boltzmann distributions, unless we are
considering thermo-nuclear burning in a (partially) degenerate
environment.

-   **Q**: can you think of stellar situations where there is burning in a
    (partially) degenerate environment?

We can explicit the Maxwell-Boltzmann distribution assuming that the
nuclei are non-relativistic, since their thermal kinetic energy is of
the order of $k_{B}T \ll GeV \sim m_{u}/c^{2}$, and you can analytically verify
that the product of two Maxwell-Boltzmann distribution keeps the same
functional form by changing variables to express things in the center
of mass frame of the $a+X$ system, yielding:

<div class="latex" id="org5b45b13">
\begin{equation}
r_{aX} = \frac{1}{1+\delta_{aX}}4\pi N_{a}N_{X} \left(\frac{m_{aX}}{2\pi k_{B}T}\right)^{3/2}\int_{0}^{+\infty}\exp\left(-\frac{m_{aX}v^{2}}{k_{B}T}\right) \sigma(v)v v^{2}dv  \ \ .
\end{equation}

</div>

where again $m_{aX} = m_{a} m_{X} / (m_{a} + m_{X})$ is the reduced mass between $a$
and $X$, $v$ their relative velocity, $N_{a}$ and $N_{X}$ are the total
number of particles, and we get a factor of $v^{2}$ from assuming
isotropic motion and using spherical-polar coordinates in velocity
space, so $d^{3}v = 4\pi v^{2}dv$.

The term in the integral is the average over the distribution of
velocities of $\langle\sigma(v)v\rangle$, which has the dimension of [L<sup>2</sup>]&times;[L]/[t]
= [L<sup>3</sup>]/[t].

**N.B.:** this does *not* depend on the density $\rho$!

Often, this average quantity is approximated as a powerlaw from the
known value at a certain temperature $T_{0}$.

<div class="latex" id="org9cd99a9">
\begin{equation}
\langle \sigma(v)v \rangle = \langle \sigma(v)v \rangle_{T_{0}} \left(\frac{T}{T_{0}}\right)^{\xi}
\end{equation}

</div>

this is convenient because powerlaw dependencies are intuitive, and
often people will quote the exponent $\xi$ in arguments - be aware it is
a big oversimplification: in reality $\xi\equiv\xi(T)$ itself, but since $\sigma(v)$
is non-zero only for a small range of $T$, taking $\xi$ &cong; constant is not
that problematic.

**N.B.:** thermonuclear reaction rates, because of the probability of
tunneling through the Coulomb barrier are extremely sensitive to $T$.
This makes nuclear physics equations very *stiff* numerically and can be
a problem when computing stellar models.

Since velocity is not a great quantity to use in QM problems, and we
have seen above that to get nuclear reactions we do need to account
for QM effects, we can rewrite the rate above using that for $r\rightarrow +\infty$
the relative energy between $a$ and $X$ is purely kinetic (the
potential goes to zero faster than $r^{-1}$ because of electron
screening!). Thus $v=(2E/m_{aX})^{1/2}$, and we can also use that the cross
section $\sigma$ is proportional to the tunneling probability so $\sigma(E)\propto
exp(-b/E^{1/2})$:

<div class="latex" id="org89b517d">
\begin{equation}
r_{aX} \propto \frac{N_{a}N_{X}}{1+\delta_{aX}}\sqrt{\frac{2}{\pi}}\frac{1}{k_{B}T}\int_{0}^{+\infty}\exp\left(-\frac{E}{k_{B}T}-\frac{b}{\sqrt{E}}\right)  \ \ .
\end{equation}

</div>

We can graph the part within the integral to understand where the rate
is going to peak:

![img](./images/gamow_peak.png "Sketch of the "Gamow peak" resulting from the combination of the Maxwell-Boltzmann distribution of particles in (thermal) energy and the tunneling probability through the Coulomb repulsion. Credits: L. Trache.")

The product of an exponentially decreasing Maxwell-Boltzmann
distribution $\propto \exp(-E)$ times the exponentially growing tunneling
probability $\propto \exp(-1/E^{1/2})$ will result in a very peaked integrand,
the so called Gamow peak: even without nuclear resonances making the
cross section $\sigma$ peak (because $E$ is within the width of a metastable
energy level), the nuclear reaction rate is still very peaked around a
specific energy!


<a id="org8e542bf"></a>

# Nuclear physics in stellar evolution codes

When trying to model the structure and evolution of a star, we cannot
carry out all the integrals we wrote down here on-the-fly. Instead, we
rely on tabulated nuclear reaction rates as a function of $T$ and $\rho$.
Open-source nuclear reaction rates tables are available from the
[JINA/REACLIB database](https://reaclib.jinaweb.org/index.php).

This is a topic of active research, with certain reactions being
particularly uncertain (e.g., $^{12}\mathrm{C}(\alpha,\gamma)^{16}\mathrm{O}$ which
determines the C/O ratio in the Universe, or even the $3\alpha$ reaction
that determines the formation of carbon in the first place). See for
example [Shen et al. 2023](https://ui.adsabs.harvard.edu/abs/2023ApJ...945...41S/abstract).


<a id="orgf5d8a52"></a>

# Composition changes and stellar *evolution* term

We already wrote Eq. \ref{eq:eps_nuc} for the energy generation term
$\varepsilon_\mathrm{nuc}$ entering in the stellar structure equation describing
energy conservation ($dL/dm = \varepsilon_\mathrm{nuc} - \varepsilon_{\nu} +
\varepsilon_\mathrm{grav}$). With a theory (and experimental data) to calculate
the nuclear reaction rates $r_{i}$ for each possible reaction, we have
now a complete set of equations for the *structure* of a star at any
given point in time under the assumption of spherical symmetry (which
in nature can and is broken occasionally!).

However, because of nuclear reactions, the nuclei in the stellar
plasma progressively change (on a timescale $\sim \tau_\mathrm{nuc}$, which
is long compared to all other timescales, but short compared to the
age of the Universe!). This introduces the equations that drive the
*evolution* of stars.

The change in number density of each nuclear species $i$ per unit time
is determined by its *production* rate through all possible nuclear
reactions $j+k&rarr; i+&#x2026;$ that have $i$ as an outgoing particle, minus
the *destruction* rate $i+j\rightarrow \cdots$:

<div class="latex" id="orgea76b89">
\begin{equation}
\frac{dn_{i}}{dt} = \sum_{k,l} r_{k,l} - \sum_{i,j} (1+\delta_{ij})r_{ij} \ \,
\end{equation}

</div>

where the $\delta_{i,j}$ expresses that if $i=j$ (reaction of two nuclei of the
same species), then two nuclei are destroyed.

Using that $n_{i} = X_{i}\rho/(A_{i}m_{u})$ and what we have learned to determine
the rates $r_{ij}$ and $r_{kl}$ we can rewrite this as a function of
variables that already appear in our stellar structure equations:

<div class="latex" id="org7bc45d0">
\begin{equation}
\frac{dX_{i}}{dt} = A_{i}\frac{m_{u}}{\rho}\left(\sum_{k,l} r_{k,l} - \sum_{i,j} (1+\delta_{ij})r_{ij}\right) \equiv \frac{dX_{i}}{dt}(T,\rho, {X_{j}}) \ \ ,
\end{equation}

</div>

and we have one such equation for each species $i$ to consider. In
case there is also mixing (for example due to convection), then we
need to add to each of these equation a mixing term (advective or
diffusive).

This effectively completes the set of equations we need to study not
only the *structure* of stars but also their long-term *evolution*.


<a id="org3c30fb7"></a>

# Appendix: Nuclear liquid drop model

In the 1930s Gamow, and later Bethe, Weiszacker and collaborators
developed a model of the nuclear interactions based on the analogy
with a liquid drop, which explains most of the observed features
available at the time (e.g., the constant density of the nuclei, the
preference for $N=Z=A/2$, the existence of particularly bound nuclei
with certain even $N$ and $Z$ numbers).

**N.B.:** this is still a rough approximation that has been updated by
other models since then, but paints a physically intuitive picture
that has a wide range of applicability. Still today, most nuclear
potential models are either specialized to a narrow energy range (so
called *local* potentials), or involve a large number of experimentally
determined parameters like this model.

In the liquid drop model, the nuclear binding energy can be expressed
as:

<div class="latex" id="org582a25b">
\begin{equation}
\mathrm{BE}_\mathrm{nuc} = a_\mathrm{vol} A - a_\mathrm{surf} A^{2/3} - a_\mathrm{Coulomb} \frac{Z^{2}}{A^{1/3}} - a_\mathrm{sym} \frac{(N-Z)^{2}}{A} - a_\mathrm{coupling} \ \ ,
\end{equation}

</div>

where the coefficients a<sub>i</sub> are experimentally derived. Each term has a
specific interpretation, keeping in mind the empirical relation for
the nuclear radius $r_{n} \equiv r_{n}(A) \propto A^{1/3}$:

-   $a_\mathrm{vol}$ is the coefficient for a volume term, that is
    negative and expresses the fact that on short range nucleons attract
    ($F_{n}=- \nabla V_{n}$) each other and nuclei hold together.
-   $a_\mathrm{surf}$ is a surface correction on the previous term, and
    expresses the fact that nucleons at the edge of the nucleus feel the
    interaction with fewer other nucleons.
-   $a_\mathrm{Coulomb}$ expresses the electromagnetic repulsion between
    protons
-   $a_\mathrm{sym}$ expresses the fact that stable nuclei prefer to
    have $N=Z$ (unless $N>Z$ is necessary to increase $A$ without
    increasing the Coulomb term for heavy nuclei)
-   $a_\mathrm{coupling} \propto \pm A^{-3/4}$ which is >0 if both $N$ and $Z$ are
    even, <0 if both are odd, and zero otherwise. This term expresses
    the fact that stable nuclei tend to prefer filling the energy levels
    for protons and neutrons (think by analogy with atoms wanting to
    fill their electron levels to be stable), so they tend to prefer
    having an even number for each, one spin up and one spin down in
    each energy level. (**N.B.:** this means that there are some number of
    nucleons for which nuclei are particularly stable, these are the
    "magic numbers" that will come back in the [next lecture](./notes-lecture-nuclear-cycles.md))

