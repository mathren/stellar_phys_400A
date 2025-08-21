
# Table of Contents

1.  [Nuclear burning cycles](#orgb6a1cd5)
    1.  [Heuristic summary and $S$ factor](#org80e095f)
    2.  [Hydrogen burning](#orgfa574d6)
        1.  [pp chain](#orgcab0bc7)
        2.  [CN-NO bi-cycle](#org17573df)
        3.  [pp &rarr; CNO transition](#orgc488771)
    3.  [Helium burning](#orgc0fff53)
        1.  ["Triple &alpha;" reaction](#org9b61832)
        2.  [The nuclear astrophysics "holy grail": $^{12}\mathrm{C}(\alpha,\gamma)^{16}\mathrm{O}$](#org321c282)
    4.  [Heavier burning](#org8fe6f82)
        1.  [Carbon burning](#org1f72d08)
        2.  [Neon ignition and nuclear "magic numbers"](#orge200852)
        3.  [Oxygen](#orga3d5c2d)
        4.  [Silicon core burning](#orgf050e48)
2.  [Summary of energy scaling](#org360acb1)
3.  [Duration of each burning phase](#orgf47a946)
4.  [Energetically unimportant but observationally puzzling Lithium](#org94703c6)
5.  [Homework](#orgddcb4f8)

**Materials:** Onno Pol's lecture notes Chapter 6.1 and 6.2, Kippenhahn
book Chapter 9 and 18, Cox & Giuli vol. I, Chapter 17.7, Clayton,
Chapter 5, [Bethe 1939](https://journals.aps.org/pr/abstract/10.1103/PhysRev.55.434)


<a id="orgb6a1cd5"></a>

# Nuclear burning cycles


<a id="org80e095f"></a>

## Heuristic summary and $S$ factor

In the [previous lecture](./notes-lecture-nuclear-burning.md) we have developed some idea of the physics
involved in thermonuclear reactions. We can have a heuristic
derivation of the main results we obtained for a generic charged
particle reaction $X(a,b)Y$ by writing the cross section for the
reaction as:

<div class="latex" id="org25ecf0e">
\begin{equation}
\sigma = \pi \lambda_{X}^{2} \times \{ \mathrm{Probability\ of\ Tunneling}\} \times \{\mathrm{Probability\ of\ C^{\star}\ decay\ in\ Y+b}\}\ \ ,
\end{equation}

</div>

where the first term is akin to a geometric cross section using the de
Broglie wavelength of the target nucleus $X$. The product of the two
terms in curly brackets appears because of Bohr's approximation (so
that the two probabilities are independent of each other). Since $\lambda_{X} =
h/p \propto h/E^{1/2}$ (for non-relativistic ions) $\Rightarrow \lambda_{X}^{2 }\propto E^{-1}$ and thus:

<div class="latex" id="org8aa846b">
\begin{equation}\label{eq:heuristic_summary}
\sigma \equiv \sigma(E)\propto \frac{1}{E}\exp\left(\frac{-b}{\sqrt{E}}\right)S(E) \ \ ,
\end{equation}

</div>

where $S(E)$ is the so called "*astrophysical $S$ factor*" that contains the
intrinsic cross section that depends on the shape of the nuclear
potential well. This can be influenced strongly by nuclear resonances
(when $E$ &sim; energy of a metastable state of $C^{\star{}}$).

In practice, often one relies on laboratory measurements (at high $E\gg$
thermal energy in stars), and extrapolation to low energies to obtain
$S(E)$, which is a risky business precisely because of the resonances!
In absence of resonances though, one expects $S(E)$ to be only slowly
varying (unlike $\sigma(E)$ which depends on the Coulomb penetration
probability).

To obtain a *thermo*-nuclear reaction rate, the cross section above has
to be averaged over a Maxwell-Boltzmann distribution. The product
between the tunneling probability and the exponential factor of the
Maxwell-Boltzmann distribution produces the "Gamow peak" making
thermonuclear reaction rates strongly peaked functions of the
temperature whether there are resonances (included in the
astrophysical factor $S(E)$) or not.

We already know from the $B/A$ vs. $A$ curve that the most energy is
released by hydrogen burning into helium (because $\alpha$ particles have
such a high binding energy), and using conservation of charge and
electron leptonic number we have already written the overall reaction
as:

<div class="latex" id="org0120ad3">
\begin{equation}\label{eq:overall_reaction}
4^{1}\mathrm{H}\rightarrow^{4}\mathrm{He}+2e^{+} + 2\nu_{e} \ \ .
\end{equation}

</div>

And we know that a fraction $\phi=0.007$ of the rest mass of the 4
incoming protons (i.e., hydrogen positive ions) is converted into
energy, corresponding to a total energy released is $Q_\mathrm{H\ burn}= 26.5$
MeV.

From the overall reaction (\ref{eq:overall_reaction}) we know that the
conversion of hydrogen nuclei into helium requires two weak reactions
to explain the two $\nu_{e}$, necessary to conserve the electron leptonic
number. This is needed since we need to produce two positrons e<sup>+</sup> to
conserve the charge.

As you may expect from the name the weak interactions are weak,
meaning the coupling constant is small compared to the coupling
constant for the strong force and electromagnetic force: *weak
interactions are the bottleneck for nuclear burning in stars*.

Moreover, since the nucleus of helium (i.e., $\alpha$ particle) is made of
4 nucleons (2$p$ and 2$n$), the reaction (\ref{eq:overall_reaction})
seems to require the encounter of 4 protons (i.e., hydrogen ions) in
one point in space (within $r_\mathrm{nuc}\sim 10^{-13}$ cm) and with the
right relative energies. The statistical probability of this is
vanishingly small, and that *cannot* be how the process works in nature,
the rate would effectively be zero. [Hans Bethe](https://en.wikipedia.org/wiki/Hans_Bethe) was the person who
worked out the way this could actually happen.

The solution to the prohibitively small probability that nature finds
in stars is to go through intermediate steps instead of doing the
reaction (\ref{eq:overall_reaction}) in one single step, in other words,
to use *thermonuclear reaction chains*.This theorized solution has been
directly confirmed through solar neutrino observations (which also
lead to the development of new neutrino physics), and chemical
observations across astronomical sources.

**N.B.:** all the reactions we will write down today can be inferred using
the conservation law for baryonic number (=total number of baryons,
equivalent to the conservation of mass, but mass is *not* conserved
since part of the rest energy is released as heat by the reactions),
electron leptonic number ($\tau$ and $\mu$ leptons are unstable and not
usually present in the star), and four-momentum (i.e., energy and
momentum).


<a id="orgfa574d6"></a>

## Hydrogen burning


<a id="orgcab0bc7"></a>

### pp chain

The "pp chain" is the dominant hydrogen burning mode in low mass
stars, like the Sun:

![img](./images/pp_cycle.png "Schematic representation of the pp chain. Blue boxes highlight the weak reactions producing $\nu_{e}$. The right branch is the so called pp1, the rarer left branch is the so called pp2, which further has a rarer pp3 branch ending up with the formation and decay of a $^{8}\mathrm{Be}$ nucleus.")

Important thing to notice:

-   there are three branches (pp1, pp2 which further branches off into pp3)
    with different "branching ratios" (86% and 14% for pp1 and pp2,
    respectively, with 0.01% of pp2 ending in pp3) determined by the
    resonances in the daughter nuclei $C^{\star}$ which are $^{7}\mathrm{Be}$,
    $^{7}\mathrm{Li}$, and $^{8}\mathrm{B}$ respectively here.
-   the overall reaction produces two neutrinos $\nu_{e}$, as expected from the
    overall reaction (\ref{eq:overall_reaction}) (**N.B.**: the top two reactions
    have to happen twice in the pp1 chain to allow for two
    $^{3}\mathrm{He}$, thus two $\nu_{e}$ will be produced per each
    $^{4}\mathrm{He}$ as expected).
-   the first reaction, the weak reaction producing Deuterium ($D$) is the
    main bottleneck, which can also be understood in terms of the
    nuclear physics: it requires the interaction of two protons ($A=1 \Rightarrow
      r_\mathrm{nuc} = r_{0} = 1.\times10^{-13}$ cm) with a Coulomb barrier.
-   the $\gamma$ particle produced in certain reactions (i.e., photons needed
    for the conservation of the four-momentum, which are $\gamma$ rays
    because of the 1-10 MeV energy scale of nuclear interactions) will
    quickly scatter around off electrons and "thermalize" providing the
    energy to the star
-   viceversa, the $\nu_{e}$ leave directly the star. In fact the Earth is
    constantly bombarded by a flux of $\nu_{e}$ from (primarily) the Sun, with a
    flux of &sim;10<sup>9</sup> neutrinos per s<sup>-1</sup> cm<sup>-2</sup>.
-   the $^{3}\mathrm{He}+^{3}\mathrm{He}\rightarrow^{4}\mathrm{He}+p+p$ turns two nuclei into 3,
    this will impact the number of particles per unit baryonic mass (which
    remains $\sim 6m_{u}$ at zeroth-order, neglecting the small fraction $\phi$ going into
    energy): this will impact the mean molecular $\mu$ and thus the temperature
    gradient and the mixing!
-   note from the pp1 cycle we get two 2 protons out at the end as well
    (but 6 went in, 4 went into the $\alpha$ particle as expected in the overall
    reaction (\ref{eq:overall_reaction})).

Fitting the temperature dependence for the overall cycle one obtains
$\varepsilon_\mathrm{nuc} \propto \langle \sigma(v)v \rangle \propto T^{4}$. This is a fairly
steep powerlaw, therefore one should expect the nuclear burning to
be *very concentrated* inside the star in temperature coordinate.


<a id="org17573df"></a>

### CN-NO bi-cycle

When the luminosity of a star is high (recall for a fully radiative
star $L\propto M^{x}\mu^{4}$ with $x \equiv x(M)\ge0$), the bottleneck reaction
$p+p\rightarrow D+e^{+} +\nu_{e}$ prevents the stars from reaching the equilibrium
condition $L=L_\mathrm{nuc}$ through the pp chain: its rate is too
low. Another mechanism to achieve the overall reaction
(\ref{eq:overall_reaction}) is needed.

Therefore, for masses larger than a certain threshold, hydrogen core
burning occurs through the CN-NO bi-cycle, where the "trick" to bypass the
bottleneck of the weak reaction in the pp chain is to use metal ions as
catalysts for the reactions.

![img](./images/CN-NO.png "Schematic representation of the CN-NO bi cycle. The branches on the left of the figure are secondary channels less relevant for the energy release (smaller rates &rArr; smaller contribution to $\varepsilon_\mathrm{nuc}$).")

Important things to notice:

-   C, N, and O are not *destroyed* here, they just act as nuclear
    catalyst. Protons momentarily "stick" to them, and then $\alpha$ particles
    are produced re-making the original C, N, and O
-   the bottleneck of the weak reactions is now bypassed by forming an
    unstable isotope of a metal and having that decay: in a sense *massive
    stars hack nuclear physics* to make the weak reaction not happen in an
    isolated proton+proton reaction which is hard, but within nuclei.
-   There are really two main cycles, the CN cycle and the NO (the figure
    shows also minor branching out points). The second involves oxygen, which
    has a higher $Z$ and slightly higher Coulomb barriers, so it kicks in at
    slightly higher temperatures, but typically a star going through the CN
    cycle will also do the NO cycle, and they are often referred to jointly
    as CNO cycle.
-   $^{14}\mathrm{N}$ is a stable isotope ($N=Z=A/2$), and the
    $^{14}\mathrm{N}+p$ reaction is the bottleneck of the bi-cycle: since
    at equilibrium all these reactions occur at the same rate set by the
    slowest reaction, this means that C and O are converted into
    $^{14}\mathrm{N}$ in the core of massive stars with the sum of their
    mass fractions remaining constant
    $X(^{12}\mathrm{C})+X(^{14}\mathrm{N})+X(^{16}\mathrm{O})$ =  constant.

Because of the higher Coulomb barriers involved one can expect a
steeper temperature dependence of this hydrogen burning mode, and in
fact one finds for the CNO cycle $\varepsilon_\mathrm{nuc} \propto T^{16}$.

This very steep energy dependence produces a very large temperature
gradient in the core of massive stars (by releasing energy in a very
small region in mass): the cores of stars burning through the CNO
cycle are **convective**.

**N.B.:** This is also how hydrogen burns in a shell or at the surface of a
white dwarf during a nova explosion: in those cases the temperature of the
gas is set by the structure of the star independently of the requirement of
thermonuclear burning! For novae explosions, the burning is not even
hydrostatic: can have the "hot CNO" cycle, where reaction rates do *not* need
to wait for &beta;-decays to occur. This is a general feature of explosive
burning: in that case we don't need to wait for the slowest nuclear
reaction in the cycle, as the high temperatures can allow to bypass Coulomb
barriers more easily.

-   **Q**: How did population III stars do this? See also [honors project](./honors.md)


<a id="orgc488771"></a>

### pp &rarr; CNO transition

Because of the higher Coulomb barriers involved in the CNO cycle (i.e.
the higher charge of $^{12}\mathrm{C}$), it has a more sensitive
temperature dependence:

-   $\varepsilon_\mathrm{nuc, pp} \propto T^{4}$
-   $\varepsilon_\mathrm{nuc, CNO} \propto T^{16}$

However, the proportionality constant is larger for the pp cycle (see
figure), therefore, for stars with lower mass $M$, that is lower $\langle T
\rangle$ by the virial theorem, hydrogen burning through the pp-chain will
dominate. However, increasing $M$ (and thus $\langle T \rangle$), at some point
the CNO cycle takes over as dominant energy production mechanism.

![img](./images/pp_vs_CNO.png "$\varepsilon_\mathrm{nuc}/\rho$ as a function of temperature $T$ all calculated in the center of stellar models (bottom axis) or initial mass $M$ (top axis) for the pp chain (blue) and CNO cycle (orange) based on a grid of MESA models at the onset of hydrogen core burning once equilibrium ($L\simeq L_\mathrm{nuc}$) is established. Dashed lines are linear fits. Modified from a figure by R. Townsend.")

Because of the steepness of the $\varepsilon_\mathrm{_{nuc, CNO}}$ we expect that
at higher initial total mass $M$ the core will be *convective* (recall
that if $\nabla_\mathrm{rad} \propto \kappa L > \nabla_\mathrm{ad}$ we expect convection),
while if $M$ is sufficiently low that the pp chain dominates, the core
is stable against convection and remains radiative. This is something
that is *indirectly* confirmed by studying the eigenfrequencies of stars
that can be observed as pulsational frequencies (i.e.,
asteroseismology - see also guest lecture by Prof. Conny Aerts),
stellar lifetimes inferred from population analyses, etc.

The initial mass $M$ at which the transition happens needs to be
determined with stellar models and is around $M_{pp \rightarrow CNO} \sim
1.1-1.3M_{\odot}$, where the imprecision comes from the systematic
uncertainties in stellar models (in terms of input physics and
algorithmic representation of the processes in the code, that we will
discuss in more detail in the [next lecture](./notes-lecture-neutrinos.md)). To some extent, this is a
physically motivated threshold to *define* what a "massive" star is (for
example this is typical in asteroseismology context), though other
meaningful threshold exist: the term "massive star" is typically
context dependent.


<a id="orgc0fff53"></a>

## Helium burning

Once hydrogen fuel runs out in the core of a star (i.e., anywhere with
mass coordinate $m \le f_\mathrm{burn} M_\mathrm{tot}$ where all the
hydrogen has turned to helium, so the composition is $Y=1-Z$), the
next fuel to burn is going to be helium. First of all, this is always
available since it was produced in the Big Bang and also *locally
brewed* by the burning of hydrogen that just ended, and secondly, it's
the energetically second-best fuel in terms of energy release per
nucleon.

However, there is a nuclear physics problem: there are no stable
nuclei with $A=5$ and $A=8$ and the few $A=7$ produced during hydrogen
burning are very fragile and easy to break, so they don't survive the
hydrogen burning phase either. So how can one do thermonuclear
reactions of helium?

This was solved by [Fred Hoyle](https://en.wikipedia.org/wiki/Fred_Hoyle), who predicted that there would be a
metastable state of carbon (as a $C^{\star}$ compound nucleus in Bohr's
approximation) that would allow to consume helium, using astrophysics
to understand nuclear structure!


<a id="org9b61832"></a>

### "Triple &alpha;" reaction

The easiest way to consume helium is through the so called "triple $\alpha$
reaction", which is actually a *compound* reaction with a very short
lived intermediate state (**N.B.:** the probability of 3 $\alpha$ particles
to meet in the same place within their nuclear radii because of
thermal motion is negligibly small). The $3\alpha\rightarrow^{12}\mathrm{C}$ compound
reaction is actually:

<div class="latex" id="org7467699">
\begin{equation}
\alpha+\alpha\leftrightarrow^{8}\mathrm{Be}+\gamma \\
^{8}\mathrm{Be}+\alpha\rightarrow^{12}\mathrm{C^{\star\star}}\rightarrow^{12}\mathrm{C}+\gamma
\end{equation}

</div>

As mentioned above, the $A=8$ nucleus of Beryllium is unstable, and
decays with a half life of $\tau_\mathrm{Be}\sim8\times10^{-17}$ seconds (**N.B.:** this
is still much longer than the light crossing time $\sim10^{-23}$ sec, so
Bohr's approximation holds!). Therefore, the first reaction can go
both ways, with the beryllium decaying back in two $\alpha$ particles.
However, if the temperature is such that *before* it can decay, a third
$\alpha$ particle will interact with the beryllium, then one can consume
three nuclei of helium to make a carbon. This requires $T\sim10^{8} K \gg
T_\mathrm{center,\odot}\simeq10^{7} \sim T_\mathrm{H\ burn}$.

The insight of F. Hoyle was that this would happen, and for this to
happen there *needs* to be an excited (actually doubly-excited) state of
$^{12}\mathrm{C}$ with $\ell=0$ which was theoretically predicted from the
astrophysical evidence that carbon is the next most abundant element
after H and He: stellar observations were used to correctly predict
excited states of nuclei and thus nuclear resonances!

**N.B.**: In practice $^{8}\mathrm{Be}$ is so short lived that often it is
not included in stellar evolution simulation and what we use is a
reaction rate for the *compound* $3\alpha$ process with a temperature
dependence that makes the rate non-zero only for $T\geq10^{8}$ K allowing
for $\alpha+^{8}\mathrm{Be}$ to occur. This allows to not have to track the
isotope of $^{8}\mathrm{Be}$ saving computational time.


<a id="org321c282"></a>

### The nuclear astrophysics "holy grail": $^{12}\mathrm{C}(\alpha,\gamma)^{16}\mathrm{O}$

Once some carbon is produced, a new avenue for consuming $\alpha$ particles
opens up, the (in)famous $^{12}\mathrm{C}(\alpha,\gamma)^{16}\mathrm{O}$ reaction.
This still consumes &alpha;, but of course requires overcoming a higher
Coulomb barrier ($\propto Z_\mathrm{C}Z_\mathrm{He} >Z_\mathrm{He}^{2}$): it
becomes convenient for the star when $\alpha$ particles are getting scarse
towards the end of helium core burning.

This reaction regulates the C/O ratio in stars, and ultimately in the
Universe, clearly something of interest for biology (among other
things). However, its rate is notoriously uncertain, because of the
possible presence of unknown resonances in the compound nucleus.
In fact, here elements are getting sufficiently heavy that the energy
gap between laboratory experiments and the stellar conditions grows
and extrapolation of the astrophysical $S$ factor gets more and more
uncertain.

This reaction ultimately regulates the composition of the most common
white dwarfs, and also the masses of the most massive black holes, and
it is actively studied in laboratories *and* in stellar context (see for
example [Fields et al. 2016](https://iopscience.iop.org/article/10.3847/0004-637X/823/1/46) on the structure and composition of white
dwarfs, [Farmer et al. 2020](https://ui.adsabs.harvard.edu/abs/2020ApJ...902L..36F/abstract) on black hole masses, [Shen et al. 2023](https://ui.adsabs.harvard.edu/abs/2023ApJ...945...41S/abstract) for
the most recent lab measurements).


<a id="org8fe6f82"></a>

## Heavier burning

Once helium fuel is exhausted, helium core burning cannot provide the
energy to compensate for the losses, and the core of the star
contracts further, resulting in an increase in temperature until the
next fuel can ignite.

Because the end of helium core burning occurs through the
$^{12}\mathrm{C}(\alpha,\gamma)^{16}\mathrm{O}$ reaction, the composition of the core
is now a mixture of carbon and oxygen (plus some primordial metals
there since formation, which have so far been untouched by nuclear
processes, except maybe conversion of some primordial C and O into N
by the CNO cycle). The next fuel is thus carbon, because it has the
lowest Coulomb barrier.

**N.B.:** Recall that not all stars need to do all burning phases
possible: if electron degeneracy kicks in before $T_\mathrm{center}$
is high enough to start reactions, the gravothermal collapse imposed
by the virial theorem interrupts because of the EOS. Since we also
know from the virial theorem that $\langle T \rangle \propto M$, we know that lower mass
stars are on average cooler and will stop burning earlier.


<a id="org1f72d08"></a>

### Carbon burning

The carbon+carbon reaction can have several branching ratios with
positive $Q$ values (thus exo-energetic and of interest for the star
to sustain itself):

<div class="latex" id="org8699a46">
<p>
\(^{12}\mathrm{C}+^{12}\mathrm{C} \rightarrow^{24}\mathrm{Mg}+\gamma\) (Q&sim;13.93MeV)<br />
\(^{12}\mathrm{C}+^{12}\mathrm{C} \rightarrow^{20}\mathrm{Ne}+\alpha\) (Q&sim;4.616MeV)<br />
\(^{12}\mathrm{C}+^{12}\mathrm{C} \rightarrow^{23}\mathrm{Na}+p\) (Q&sim;2.238MeV)<br />
&ctdot;
</p>

</div>

These require $T\geq10^{8.5}$ K, and produce a mixture of Neon, Magnesium
(**N.B.:** an $\alpha$ nucleus that can be thought of as 6 $\alpha$ particles bound
together!) and Sodium.

**N.B.**: the $\alpha$ particle released by the second reaction listed, and the
 proton released by the third will immediately start reacting with the
 other particles present at the temperatures necessary for
 $^{12}\mathrm{C}+^{12}\mathrm{C}$ to be activated. Actually at these $T$,
 the reactions rates for reactions involving these light particles are
 going to be extremely high!


<a id="orge200852"></a>

### Neon ignition and nuclear "magic numbers"

Because of carbon burning, a significant amount of neon is produced.
Although neon has $A=20$ and $Z=10$ so it is heavier and more charged
than oxygen with $A=16$ and $Z=8$ (produced by the end of helium core
burning and still untouched by carbon burning at this point), it will
ignite before.

The reason has to do with a nuclear physics property: one can make a
direct analogy between nuclei and atoms, and like atoms of "noble
gases" which have electrons in all their shells are very stable and
don't like to do chemical interactions with other atoms/molecules,
nuclei with nucleons filling all their shells are also particularly
stable. This gives the nuclear "magic numbers" of nucleons that are
particularly stable: $Z$ or $N = 2, 8, 20, 28, 52$ (and there are
higher numbers theoretically predicted from nuclear structure
calculations).

$^{16}\mathrm{O}$ has $Z=8$ and $N=A-Z=8$, so it is a "double magic
nucleus", that from the nuclear interaction perspective is like a
noble gas from the chemical perspective: it is extremely stable and
does not want to interact.

**N.B.:** $\alpha$ particles have $Z=N=2$ and are also a "double magic"
nucleus, and in fact they have an extremely high binding energy per
nucleon! $^{16}\mathrm{O}$ is the second-lightest double magic nucleus.

Therefore, the gravothermal collapse reaches temperatures sufficient
to *photodisintegrate* the heavier (but not magic) nucleus of
$^{20}\mathrm{Ne}$ before oxygen burns: photodisintegration reactions are
in fact not affected by the Coulomb barriers. This photodisintegration
produce $\alpha$ particles and protons that stick to the existing nuclei
changing the composition typically increasing the mass fractions of
$\alpha$ nuclei ($^{16}\mathrm{O}$ and $^{24}\mathrm{Mg}$, primarily). While
unimportant for the energy generation, secondary reactions producing
$^{22}\mathrm{Ne}$ can be important for the synthesis of elements heavier
than iron through the s-process.

However, the fact that the photodisintegration of neon is easy
relative to oxygen ignition is a direct consequence that the nucleus
of neon is not very bound (compared to oxygen, or carbon) and its
burning does not release very much energy, resulting in a brief phase
of stellar evolution only (but numerically challenging to simulate!).


<a id="orga3d5c2d"></a>

### Oxygen

As T further increases because of the gravothermal collapse the oxygen
finally ignites. The dominant reaction has multiple branching ratios
with positive $Q$ value that produce sulfur and silicon primarily (two
other $\alpha$ nuclei!):

<div class="latex" id="org4448afc">
<p>
\(^{16}\mathrm{O}+^{16}\mathrm{O} \rightarrow^{32}\mathrm{S}+\gamma\) (Q&sim;16.53MeV)<br />
\(^{16}\mathrm{O}+^{16}\mathrm{O} \rightarrow^{28}\mathrm{Si}+\alpha\) (Q&sim;9.593MeV)<br />
\(^{16}\mathrm{O}+^{16}\mathrm{O} \rightarrow^{31}\mathrm{P}+p\) (Q&sim;7.676MeV)<br />
&ctdot;
</p>

</div>

**N.B.:** as before all the light produced will immediately react with the
present mixture at this temperature!


<a id="orgf050e48"></a>

### Silicon core burning

Finally, if a star has reached this point, gravity will compress its core
until it burns all the way to the most bound nucleus (iron/nickel):
stopping somehow the gravothermal collapse at this point would require
extreme fine-tuning, and by now the core density is so high that the
gravothermal collapse (of the core) is driven by neutrino emission (as we
will discuss in the [next lecture](./notes-lecture-neutrinos.md)) rather than photon losses at the surface.

Post core oxygen burning, the core is made of a mixture of silicon and
sulfur (**N.B.:** this is now very hard to probe directly observationally
because of the very short evolutionary timescales, but it matches well
the nuclear data and abundance patterns in the Universe!).

The next burning phase is typically referred to as "silicon burning",
although it physically proceeds in a slightly different fashion than
all the burning phases we have seen so far.

It typically requires $T\sim2-5\times10^{9}$ K and densities $\rho\sim10^{7}-10^{10}$ g cm<sup>-3</sup>
and only lasts order of $\tau_\mathrm{nuc, Si}$ &sim; days-weeks since the
energy release per nucleon is *only* $0.1$ MeV/nucleon (cf. &sim;
$Q<sub>\mathrm</sub>{H-burn}$/4&cong;6.6 MeV/nucleon for H burning!).

At such temperatures, we reach a "quasi statistical equilibrium"
between nuclei: the silicon, sulfur, and other elements (referred to
as "silicon group elements" with $A\sim28$ and $Z\sim14$) are
photodisintegrated and re-created at very high and nearly canceling
rates:

<div class="latex" id="orgca68c79">
\begin{equation}
\gamma + ^{A}Z \rightarrow ^{A'}Z' +{p,n,\alpha}
\end{equation}

</div>

This produces also a variety of light particles (protons, neutrons,
and $\alpha$ particles), which can be captured on the silicon group
elements to form heavier "iron group nuclei" (which are also
photodisintegrated and recreated constantly):

<div class="latex" id="org7ef9b93">
\begin{equation}
\{p, n,\alpha\} + \{ ^{A}Z,^{A'}Z' \} \rightarrow \{ \mathrm{Fe \ group \ nuclei} \} +
\dots
\end{equation}

</div>

Moreover, many $^{A'}Z'$ nuclei produced by photo-disintegrations and
particles captures are neutron or proton rich, therefore a lot of
weak reaction such as &beta;<sup>&plusmn;</sup>-decays and electron captures happen too (while
positron captures are always negligible for stars with M &le; 40 M<sub>o,</sub> and
positrons prefer to annihilate with an electron producing &gamma; rays that
quickly thermalize in the plasma see [Arnett et al. 1977](https://ui.adsabs.harvard.edu/abs/1977ApJS...35..145A/abstract)).

![img](./images/QSE.png "Schematic representation of quasi statistical equilibrium on the nuclear chart. The two filled circle represent the Si (red) and Fe (blue) groups. The abundance of nuclei within each group reach NSE. The links connecting specific isotopes within each group represent the few reactions out of equilibrium, which progressively result in the depletion of the number of isotopes in the Si group in favor of those in the Fe group.")

This process is computationally very challenging, since there are many
forward and reverse reactions happening at very high rates but
canceling each other out, resulting in a very *stiff* set of equations
to solve for the evolution of the chemical composition. In this
situation, the truncation errors in the floating point algebra of
computers can easily become problematic.

The rates are so high that the Quasi Statistical Equilibrium (QSE) regime
is achieved: two distinct groups of isotopes in equilibrium are formed
around silicon and iron and only few reactions linking the two groups are
out of balance with their reverse.

Within each "equilibrium group", the abundances of each isotope stay
roughly constant, because production and destruction reactions
involving only isotopes of that group cancel out almost exactly. This
means that within each group, Nuclear Statistical Equilibrium (NSE) is
reached, an assumption that can simplify the calculations that we will
use in atomic (rather than nuclear) context [later](./notes-lecture-radTrans.md).

Note however that *weak reaction are never balanced by their reverse
reaction*: the cross section for neutrino captures is too small at this
stage. Strong and electromagnetic mediated nuclear reactions need to
compensate also the weak reactions for the isotopes that can &beta;-decay
or capture electrons. Therefore this is not a true statistical
equilibrium regime, and the "principle of detailed balance" (meaning
each reaction is canceled out by the opposite corresponding reaction)
does not hold strictly. Some widely used stellar evolution codes
therefore do not rely on the approximation of "quasi equilibrium" and
instead calculate directly all the reactions.

This process ends with the formation of an Iron core, made of nuclei
at the maximum of the B/A vs. A curve that the star cannot burn to
sustain itself: at this point gravity wins, and we get a core-collapse
event resulting in (possibly) a supernova explosion and the formation
of a neutron star or a black hole, which we will discuss in a [future
lecture](./notes-lecture-end-massive-stars-and-SNe.md).


<a id="org360acb1"></a>

# Summary of energy scaling

![img](./images/Nuclear_energy_generation.png "$\varepsilon_\mathrm{nuc} \equiv \varepsilon_\mathrm{nuc}(T)$ dependence on a log-log plot for the burning cycles that cover &ge;99% of the stellar lifetime (H and He core burning). From [wikipedia](https://commons.wikimedia.org/wiki/File:Nuclear_energy_generation.svg).")

**N.B.:** The central temperature of the Sun correspond to the higher
range where the pp chain dominates the energy production. This means
that in the Sun we expect some CNO burning at a sub-dominant level,
and indeed $\nu_{e}$ from the decay of $^{13}N$ have been experimentally
detected (one can recognize them from their spectrum), see [Borexino
collaboration 2020](https://www.nature.com/articles/s41586-020-2934-0).

Because of the higher and higher Coulomb barriers, the temperature
dependence of $\varepsilon_\mathrm{nuc}$ gets steeper for heavier nuclear fuel,
so post-helium core burning $\varepsilon_\mathrm{nuc}$ is more and more
concentrated towards the center, leaving the outer layers unburned and
allowing for the so called "onion layer" structure of stars:

![img](./images/onion.png "Layer structure for an initially $15M_{\odot}$ star at the end of its nuclear burning lifetime in mass coordinate from [Renzo 2015](https://www.as.arizona.edu/\simmrenzo/materials/Thesis/Renzo_MSc_thesis.pdf). Note the final total mass is *not* 15M<sub>o</sub> because stars this massive lose mass through radiatively driven winds.")

How much burns, that is, how "thick" in mass coordinate is each layer
of the onion, depends on the mixing processes connecting the burning
layer with the fuel reservoir. At the outer edge of each shell of the
"onion" there can be (and typically there is) an off-center burning
region, so called "shell burning". The outer layer of the He
core/inner layer of the H envelope (the exact boundary depends on the
definition one adopts) is sufficiently hot to burn the remaining fuel
there, and this burning sustains the outer layer above it. Because of
the presence of burning shells, the core burning only needs to sustain
the matter inside the shell, which slightly complicates the
*gravothermal* argument we have used.

Each layer of heavier material requires a higher $T$ to burn (to have
a non-zero tunneling probability), so it is more centralized in mass
and radius. However, moving inward $\varepsilon_\mathrm{nuc}$ depends more
steeply on $T$, which implies the $dT/dr$ becomes steeper, and thus we
have convection, the extent of which determines where fuel is
depleted. At high masses ($M\geq20M_{\odot}$), the inner layers start
cooling through neutrinos, which may take away enough energy to
prevent convection from occurring (**N.B.:** convection kicks in only if
needed to transport the energy flux).

The interplay between convection, neutrino cooling, and nuclear
burning ultimately decides the core structure of massive stars at the
end of their life, and whether they form a neutron star or a black
hole, in ways that are still poorly understood (see for example
[Sukhbold & Woosley 2014](https://ui.adsabs.harvard.edu/abs/2014ApJ...783...10S/abstract), [Laplace et al. 2024](https://ui.adsabs.harvard.edu/abs/2024arXiv240902058L/abstract)).


<a id="orgf47a946"></a>

# Duration of each burning phase

As we have seen (cf. [virial theorem lecture](./notes-lecture-VirTheo.md)) stars shine as anything
with a finite temperature does. This consumes internal thermal energy,
which by the virial theorem is related to their gravitational
potential and drives a decrease in the radius. All this happens (by
definition) at the Kelvin-Helmholtz timescale if one assumes constant
luminosity.

However, since the virial theorem implies $\langle T \rangle \propto R^{-1}$ as the star
loses energy at the surface, it's average temperature must increase:
this is often phrased by saying that self-gravitating bodies have a
*negative heat capacity*. It is because of this temperature increase
that nuclear burning must kick in: *stars don't shine because they
burn, viceversa, they burn because they shine*.

Therefore, thermonuclear burning in stars exists only to compensate
the energy losses (to photons at the surface and to neutrinos
throughout the volume that can emit neutrinos), and at equilibrium
$L_\mathrm{nuc} \equiv L (+L_{\nu})$ making the nuclear burning a [self-regulating
process](./notes-lecture-nuclear-burning.md) where it is $L (+L_{\nu})$ (the energy loss rate) that determines
$L_\mathrm{nuc}$ (the energy generation rate), and *not* the other way
around.

Under the assumption that $L_\mathrm{nuc} = L$, we can ask how long does the
consumption of a given fuel take in a star, that is the nuclear
timescale for a given fuel:

<div class="latex" id="orgf368e54">
\begin{equation}
\tau_\mathrm{nuc} = \varphi f_\mathrm{burn} \frac{Mc^{2}}{L_{}} \ \ .
\end{equation}

</div>

As we saw in the [the previous lecture](./notes-lecture-nuclear-burning.md), $f_\mathrm{burn}$ is a quantity
that requires computing full stellar evolution models (we now have all
the equations to do so under typical assumptions, it's just a
matter to tell a computer how to solve them!), but clearly $0 <
f_\mathrm{burn}<1$. For a give star of mass $M$, the important factor
here is $\phi$, which we can estimate from the nuclear binding energy per
nucleon.

Hydrogen burning into helium releases a lot of energy (26.5MeV/4
protons &sim; 6.625 MeV/nucleon) because if forms one of the most bound
nuclei in nature, the $\alpha$ particle (which is also a double-magic
nucleus!). This large energy release, means a large $\phi$ and long
nuclear burning timescale. In fact, pretty much for any star, *hydrogen
core burning covers &sim;90% of the stellar lifetime*. This independently
on whether H burning happens through the pp chain or CNO cycle. For
this reason, while the "main sequence" is technically an
observationally defined feature on the color-magnitude diagram, it is
common to refer to hydrogen core burning models as "main sequence"
models: observed stars on the observed main sequence are so numerous
because they are in the by far longest phase of their evolution,
during which they are burning hydrogen in their core.

The  burning of  Helium into  a mixture  of carbon  and oxygen  is the
second most energetic burning: this is the reason why it occurs once a
star  runs out  of hydrogen  fuel.  Again, we  get a  high $\phi$  factor
because helium fusion climbs the $B/A$  vs. $A$ curve, and helium core
burning  usually   last  10%  of   the  hydrogen  core   burning  time
($\varphi_\mathrm{He}  \simeq 0.1 \varphi_\mathrm{H}$),  so *hydrogen  and helium  core
burning together cover 99% of the stellar lifetime*.

All the other burning phases *collectively* are only &le; 1% of a star
lifetime! Although they are *crucial* for the chemical evolution of the
Universe, they are only a "blip" in the lifetime of the stars, because
$B/A$ vs. $A$ roughly flattens (and $f_\mathrm{burn}$ also decreases
because of the steeper and steeper $T$ dependence of the nuclear rate
as the Coulomb barriers increase, cf. "onion structure"): each
subsequent fuel produces less and less energy per barion, thus the
burning must be faster and faster to compensate for the surface losses
(and $L$ also typically increases). This also makes these phases more
rare to observe and thus harder to study.

For instance, the timescale for the last possible burning phase in
massive stars, silicon &rarr; iron only lasts order of *days*.

![img](./images/durations.png "example of durations of burning phases for a few massive stars from [Renzo 2015](https://www.as.arizona.edu/\simmrenzo/materials/Thesis/Renzo_MSc_thesis.pdf).")


<a id="org94703c6"></a>

# Energetically unimportant but observationally puzzling Lithium

Lithium is a relatively rare element which has a low nuclear binding energy
and is thus easily broken without releasing much energy. Therefore, lithium
burning is never energetically important.

**N.B.:** similarly deuterium ($D$ = hydrogen with an extra neutron) is very
loosely bound and its burning is not energetically important, to the
point that both can happen in sub-stellar mass objects such as
brown-dwarfs (where the virial theorem imposes a collapse, but $\langle T \rangle$
is never high enough to generate enough energy through nuclear
reaction to sustain the structure and their collapse is interrupted by
degeneracy pressure).

Traces of Lithium are produced in the Big Bang nucleosynthesis, so some of
it exists in stars at the beginning of their evolution. Because of its
fragility, Lithium is a sensitive tracer of temperature in stars, and in
evolved stars it should not be found because of the
$^{7}\mathrm{Li}+p\rightarrow2^{4}\mathrm{He}$ reaction. However, lithium can be observed
in some stars atmospheres! This posed the problem of how lithium can be
produced again once the star evolves. Various mechanisms have been
proposed:

-   spallation of cosmic rays (but generally one expects the cosmic ray flux
    to be too low to explain the amount of lithium found)
-   "Cameron-Fowler mechanism" ([Cameron & Fowler 1971](https://ui.adsabs.harvard.edu/abs/1971ApJ...164..111C/abstract)): mixing at the bottom
    of the envelope can lead to $^{3}\mathrm{He}(\alpha, \gamma)^{7}\mathrm{Be}$ and the
    produced $^{7}\mathrm{Be}$ is then mixed outwards where it may decay into
    $^{7}\mathrm{Li}$ with an electron capture. For this mixing to happen one
    expects the star to be quite evolved (an AGB star), and we see more
    Lithium-rich giants than this can explain.


<a id="orgddcb4f8"></a>

# Homework

-   Calculate the Sun's mass loss rate due to the nuclear burning of 4
    protons into helium
-   Using `MESA-web`, which contains tabulated data for nuclear reactions from
    experiments, calculate the evolution until the end of iron core burning
    of a massive (M>15M<sub>o</sub>) star and use the `trimmed_history.data` output
    to:
    
    1.  determine the typical composition of the core at various
        evolutionary phases and explain it in terms of the experimentally
        derived properties of nuclei (**hint**: use the variables `center_*` to
        plot the mass fraction of abundances as a function of time)
    2.  estimate the duration of each core burning phase.
    
    **N.B.:** You can also use the "movie" of the evolution of the star
    produced by `MESA-web` for you.
    
     **N.B.:** The values you will find may differ from the table above:
    that's ok! The simulation output depends on many physics assumptions
    which are probably not the same in the models `MESA-web` runs and
    those I quoted, this actually gives you an idea of *systematic* errors
    in the numerical computations
    
    **N.B.:** Computing the evolution of massive stars through *all* the burning
    phases is numerically challenging (and the stiffness of the nuclear
    reactions rate dependence on T is a big part of the challenge), therefore
    it is possible that your `MESA-web` model may not finish the run. The file
    `input.txt` in the `*.zip` file you download from `MESA-web` has a string at
    the end telling you if the model was successful or not. If your model is
    not and you can't get a successful model by the deadline by fiddling with
    the input parameters, mention which input you used (listed in that file)
    and list the composition and typical duration up to where your model
    evolved.
    
    **Hint**: I have tried with the following settings and got a model to
    form an iron core, that is successfully burn through all the viable
    nuclear fuel:
    
    -   Initial Mass: 20M<sub>o</sub> (solar mass)
    -   Burning Modifiers: `none`
    -   Nuclear Reaction Network: `approx21`
    -   Sampled Nuclear Reaction: `none`
    -   Initial Metallicity: 0.02
    -   Mixing Length Alpha: 2.0
    -   Mixing Length Theory Implementation: Cox (this is an algorithmic
        formulation of MLT)
    -   Convective Overshoot f: 0.000
    -   Convective Overshoot f0: 0
    -   Semi-Convection Alpha: 0
    -   Thermohaline Alpha: 0
    -   Thermohaline Mixing Implementation: Kippenhahn
    -   Boundary Mixing: `pred` = `.false.` / `predms` = `.true.` / `cpm` =
        `.false.` (the default)
    -   Red Giant Branch Wind Scheme: Dutch (this specifies stellar winds)
    -   RGB Wind Scaling Factor: 0.8
    -   Asymptotic Giant Branch Wind Scheme: Dutch
    -   AGB Wind Scaling Factor: 0.8
    -   Initial Rotational Value: 0.0 (initial rotation)
    -   Variance Control Target: 1e-2
    -   Mesh Delta Coefficient: 2.0
    -   dX<sub>nuc</sub><sub>drop</sub><sub>min</sub><sub>X</sub><sub>limit</sub>: 1e-2
    -   MESA Release: `r12778`

