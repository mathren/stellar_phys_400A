
# Table of Contents

1.  [Virial theorem](#org2fc383e)
    1.  [(Almost fully) General derivation](#org454e624)
    2.  [Derivation for binary orbits](#org56ee5db)
    3.  [Derivation for stars](#org49aa6bc)
        1.  [Stability criterion](#orgaf0797d)
        2.  [Use of gravitational energy in a star: negative heat capacity](#orgeb11170)
    4.  [Kelvin-Helmholtz timescale](#orgacb56d8)
2.  [Homework](#org0a81841)
    1.  [The Sun with no energy sources](#orgba6b3ce)

**Materials**: Chapter 2 of Onno Pols' lecture notes, Chapter 3 of
Kippenhahn's book, Sec. 1.5 of "Tapestry of Modern Astrophysics" by S.
N. Shore, pages 134-139 Clayton's book.


<a id="org2fc383e"></a>

# Virial theorem

In the [previous lecture](./notes-lecture-EOS1.md), we have discussed that it is appropriate to
use thermodynamics to describe the *local* properties of the stellar
gas. We had already established that (self-)gravity determines the
pressure gradient in the star through the hydrostatic equilibrium
equation (which is just the particular form that momentum conservation
takes in a stellar context). Therefore, in this lecture we will
explore the relation there may be between gravitational physics and
thermodynamics which will allow us to get some crucial facts about
stars.

The virial theorem relates the kinetic and potential energy of system
of point masses interacting through long-range forces, and thus allows
one to **connect thermodynamics and gravitational physics**. It is a
statistical statement on mutually interacting particles (e.g., because
of their mutual gravity!), and thus it is very general. The etymology
of the name comes from "vir" which is latin for "forces".


<a id="org454e624"></a>

## (Almost fully) General derivation

Let's start with a very general derivation (see for example
Goldstein's classical mechanics book or Shore's Tapesty of Modern
Astrophysics Sec. 1.5). For a collection of particles with (constant)
mass $m_{i}$, Netwon's second law states that the change in their
momentum is equal to the total force they are subject to:

<div class="latex" id="orgb4c1837">
\begin{equation}
 m_{i} \ddot{\mathbf{r_{}}_{i}} = \mathbf{F}_{i} \ \, .
\end{equation}

</div>

Note that here $\mathbf{r}_{i}$ and $\mathbf{F}_{i}$ are vector quantities.
We take the *first-order spatial moment of this distribution*, which
means we take the dot product of each term by the position of the
particles and sum over all the particles. Why? The reason is to make
*something like the work done by forces (and thus the potential energy)
appear in the second term*:

<div class="latex" id="org11feabb">
\begin{equation}\label{eq:first_moment_second_law}
\sum_{i} m_{i}\ddot{\mathbf{r}_{i}} \cdot \mathbf{r}_{i} = \sum_{i} \mathbf{F}_{i} \cdot \mathbf{r}_{i} \ \ .
\end{equation}

</div>

The r.h.s. looks like a sum of work done by the total foce on each
particle: $\sum_{i} \mathbf{F}_{i} \cdot \mathbf{r}_{i} \equiv W$. This is the so
called "virial", which contains only long-range forces between the
particles (collisions cancel out in the sum because of Netwon's 3<sup>rd</sup>
law). This by conservation of energy has to be equal to the net
potential energy available $E_\mathrm{pot}$.

The l.h.s. can be re-written using the chain rule for the second
time-derivative:

<div class="latex" id="orgb260970">
\begin{equation}
\sum_{i} m_{i}\ddot{\mathbf{r}_{i}} \cdot \mathbf{r}_{i}  = \sum_{i} \frac{1}{2} m_{i} \frac{d^{2}}{dt^{2}}r_{i}^{2} - \sum_{i} m_{i} \cdot \dot{r_{i}}^{2}
\end{equation}

</div>

And now we have on the right hand side (assuming the mass of the
particles to be constant) twice the second time derivative of the
moment of inertia $I = \sum_{i} m_{i} r_{i}^{2}$ and twice the kinetic energy
$E_\mathrm{kin} = \sum_{i }m_{i} v_{i}^{2}/2$ (because of course $v_{i} = \dot{r_{i}}$).
So putting the r.h.s. of this last equation in the first spatial
moment of Newton's second law (Eq. \ref{eq:first_moment_second_law})
we obtain:

<div class="latex" id="org0968b55">
\begin{equation}
 2\mathrm{E}_\mathrm{kin}+\mathrm{E}_\mathrm{pot} = \frac{1}{2}\ddot{I}
\end{equation}

</div>

This is the general form of the Virial theorem derived by Clausius. In
general, in the virial theorem there is a second derivative of the
moment of inertia on the r.h.s., which is often forgotten. We did not
specify almost anything about the system (see Goldstein for a
momentum-based derivation where the assumption of constant masses m<sub>i</sub>
of the particles implicit in the way we wrote Newton's second law is
not even needed).

The virial theorem effectively says that *for a bound system of
self-interacting particles*, *there is a limited amount of potential
energy that can be extracted*, because part of the potential will need
to go into the kinetic terms and the acceleration of the moment of
inertia.

So far, this general form doesn't give us much intuition on its
meaning. We have a relation between the kinetic energy of a collection
of particles, its potential energy, and the second time-derivative of
its moment of inertia. But in the frame of the center of mass of such
collection, the kinetic energy of the particles is a measure of their
thermal energy, and this is non-trivial: why would the thermal energy
know about the potential energy! This statement is however very
general and its implication for stellar structure and evolution are
profound.


<a id="org56ee5db"></a>

## Derivation for binary orbits

As a demonstration for the generality of the virial theorem, we can
apply it to a collection of particle with only 2 particles subject
only to the gravitational force, that is a binary system of two
point-mass stars on a Keplerian orbit!

One can write the total energy of the binary as:

<div class="latex" id="org6a7927d">
\begin{equation}
E_\mathrm{tot} = \mathrm{E_\mathrm{kin}}_{1} + \mathrm{E_\mathrm{kin}}_{2} + \mathrm{E}_\mathrm{pot} \equiv \mathrm{E_\mathrm{kin}} + \mathrm{E}_\mathrm{pot}  \equiv -\frac{GM_{1}M_{2}}{2a}  \ \ ,
\end{equation}

</div>

where in the last term we are using Kepler's laws. The gravitational
potential energy is $E_\mathrm{pot} = -GM_{1}M_{2}/a$, thus making it
explicit we obtain: $E_{kin} = |E_{pot}|/2$. Since Keplerian orbits in
Newtonian gravity are stable (energy losses through gravitational
waves make this statement not physically true, but this is only
relevant for close binaries of compact objects), this implies that the
second (and first) time-derivative of the moment of inertia of the
orbit is zero, and thus this *is* the virial theorem! *Keplerian binary
orbits are "virialized"*.

**N.B.:** Here we considered the case of just 2 particles, but nothing
stops us to consider $i=2...N$ with $N$ that can reach &sim; 10<sup>6</sup> and apply
the virial theorem to *clusters* of stars. Indeed, the virial theorem is
useful to initialize the positions and velocities of stars in a
simulated self-gravitating cluster such as globular clusters (the
question usually is whether the second-time derivative of the
cluster's moment of inertia can or cannot be approximated with zero).


<a id="org49aa6bc"></a>

## Derivation for stars

Let's now re-derive the Virial theorem for a star. Let's assume a
continuous description of the stellar gas, hydrostatic equilibrium and
spherical symmetry, and write explicitly the forces acting on each
shell $dr$ of gas (cf. hydrostatic momentum balance [seen before](notes-lecture-HSE.md)):

<div class="latex" id="org81d4f19">
\begin{equation}\label{eq:HSE}
\frac{dP}{dm} = -\frac{Gm}{4\pi r^{4}}
\end{equation}

</div>

By analogy with what is done in the general derivation above, we want
to make the gravitational potential appear on the r.h.s., which can be
done by multiplying by $4\pi r^{3}$ and integrating in $dm$ over the entire
mass of the star (from $0$ to $M$).

<div class="latex" id="org53f8d11">
\begin{equation}\label{eq:pot}
\int_{0}^{M} -\frac{Gm}{4\pi r^{4}} \times 4\pi r^{3} dm  = \int_{0}^{M} -\frac{Gm}{r}dm \equiv - \mathrm{E}_\mathrm{pot} \ \ .
\end{equation}

</div>

(so that $E_{_\mathrm{pot}}=|\int_{0}^{M} -Gm/r dm| >0$). The l.h.s. becomes integrating per parts

<div class="latex" id="org2657991">
\begin{equation}
\int_{0}^{M} \frac{dP}{dm} 4\pi r^{3} dm = \left[ 4\pi r^{3}P \right]^{M}_{0}- 3\int_{0}^{M}4\pi r^{2} \frac{\partial r}{\partial m} Pdm \ \ ,
\end{equation}

</div>

where the first term is zero: $P(M)=0$ at the outer surface of the star,
and in the center $r=0$ by definition. For the second term, we can use
the mass continuity equation and obtain $-3\int_{0}^{M} P/\rho dm$, thus, putting
back the pieces together:

<div class="latex" id="orgc2e8d6c">
\begin{equation}\label{eq:vir}
\int_{0}^{M }\frac{Gmdm}{r} = 3\int_{0}^{M} \frac{P}{\rho} dm \ \ .
\end{equation}

</div>

Note that if we had kept a non-zero $\rho \ddot{\mathbf{r}}$ term in Eq.
\ref{eq:HSE}, we would again obtain a term depending on the moment of
inertia and the bulk kinetic energy of the stellar gas (see for
example sec. 4.2.1 in Shore's "Tapestry of modern astrophysics"). From
Eq. \ref{eq:pot}, we have already interpreted the l.h.s. of Eq.
\ref{eq:vir} as the gravitational potential energy normalized to zero
at infinity.

Let's interpret the r.h.s., which in the general derivation would be
part of the $\sum_{i} \mathbf{F}_{}\cdot \mathbf{r}_{i}$ term. By dimensional
analysis we know it has to have the dimension of an energy. In fact,
still by dimensional analysis we can infer that [P/&rho;] = [E]/[L<sup>3</sup>] /
[M]/[L<sup>3</sup>] = [E]/[M] has the units of a specific energy (i.e., energy
per unit mass), and thus $P/\rho \propto u$ with $u \equiv u_\mathrm{int}$ specific
internal energy. Let's rewrite this as $u = \Phi P/\rho$ with $\Phi$ unknown
dimensionless constant.

To specify &Phi;, let's consider the second law of thermodynamics per unit
mass: *the heat exchanged by a gas* ($dq$) *is equal to the change in
internal energy* ($du$) *plus the work done* ($Pdv$, with $v$ the specific
volume, i.e. the volume per unit mass). We can use this to *define* the
specific entropy $s$, and also re-write this in terms of density instead
of specific volume $v$=(1 mass unit)/&rho; &rArr; $dv = -d\rho/\rho^{2}$:

<div class="latex" id="org2c74544">
\begin{equation}\label{eq:second_thermodynamics_law}
dq = Tds = du + Pdv = du -\frac{P}{\rho^{2}}d\rho \ \ ,
\end{equation}

</div>

We want to derive a relation between $u$, $P$, and &rho;. We are
considering the momentum conservation (Eq. \ref{eq:HSE}), so something
related to dynamics (which acts fast compared to thermal processes &#x2013;
you can verify this comparing timescales after the end of this
lecture!), therefore let's consider an adiabatic process where by
definition there is no heat exchange. Thus, $dq=0$ and $du = P/\rho^{2}
d\rho$.

Now by differentiating $u = \Phi P/\rho$ we get $du = \Phi (dP/\rho - P/\rho^{2} d\rho)
\equiv P/\rho^{2} d\rho$ (where we use Eq. \ref{eq:second_thermodynamics_law} with
$dq=0$ in the last step), that can be re-arranged into $\Phi/(1+\Phi) dP/P =
d\rho/\rho$, or in other words $(1+\Phi)/\Phi = d \log(P)/d \log(\rho) \equiv \Gamma_{1}$ because the
derivative has to be taken assuming no heat exchange, that is at
constant entropy, so that is by definition the first adiabatic index
$\Gamma_{1}$. Ultimately, we can put all this together and write

<div class="latex" id="orgff098e5">
\begin{equation}
\frac{P}{\rho} = (\Gamma-1)u \ \ ,
\end{equation}

</div>

where $\Gamma\equiv\Gamma_{1}$ is the first adiabatic index.

Finally, substituting in the first-order moment of the hydrostatic
equilibrium Eq. \ref{eq:vir} equation we have:

<div class="latex" id="org132e788">
\begin{equation}
3\int_{0}^{M} \frac{P}{\rho} dm = 3\int_{0}^{M} (\Gamma-1)u dm \ \ .
\end{equation}

</div>

Assuming that $\Gamma$ is constant throughout the star, we can take the
parenthesis out of the integral. We can define $E_\mathrm{int} = \int_{0}^{M} u dm$
and rewrite the above as $3(\Gamma-1)E-\mathrm{int}$, and thus

<div class="latex" id="orge6f5842">
\begin{equation}\label{eq:virial_star}
- E_\mathrm{pot} = 3(\Gamma-1)E_\mathrm{int}
\end{equation}

</div>

For a monoatomic gas where each particle has 3 degrees of freedom
(motion in 3 direction, no internal degrees of freedom for
point-particles), $\Gamma = 5/3$, and we obtain $|E_\mathrm{pot}| = 2
E_\mathrm{int}$ where the internal energy is due to the thermal motion
of gas, in agreement with the general form assuming hydro-*static*
equilibrium (&rArr; $d^{2} I/dt^{2} =0$).

Now lets define the total energy of the gas: $E_\mathrm{tot} =
E_\mathrm{pot} + E_\mathrm{int}$. For a star to be bound,
$E_\mathrm{tot}<0$. Because of the virial theorem in Eq.
\ref{eq:virial_star}, we can rewrite this as

<div class="latex" id="orga84fad8">
\begin{equation}
\mathrm{E}_\mathrm{tot} = \mathrm{E}_\mathrm{pot}\frac{3\Gamma-4}{3(\Gamma-1)} \equiv -(3\Gamma-4)\mathrm{E}_\mathrm{int}\ \ .
\end{equation}

</div>

Again, for a monoatomic gas with $\Gamma=5/3$ we recover $E_\mathrm{tot} =
E_\mathrm{pot}/2$, the total energy is half of the gravitational
binding energy!


<a id="orgaf0797d"></a>

### Stability criterion

From the form of $E_\mathrm{tot}\equiv E_\mathrm{tot}(E_\mathrm{int})$,
since $E_\mathrm{int}$ is a quantity that is always non-negative by
definition (think thermal energy!), we see that for the star to be
bound, that is $E_\mathrm{tot}<0$, then a necessary condition is
$\Gamma>4/3$. One can immediately see that if $\Gamma <4/3$, then
$E_\mathrm{tot}$ changes sign. If $E_\mathrm{tot}>0$ the stellar gas
is unbound: the kinetic energy due to thermal motion is sufficient to
overcome the gravitational potential and the gas will fly out.

One can encounter cases in stellar evolution where $\Gamma\le 4/3$ (e.g.,
because of recombination that changes the mean molecular weight or
pair-production). In general though $\Gamma$ is *not* constant throughout the
star as we assumed to pull the $\Gamma-1$ factor out of the integral. In
physical situations where $\Gamma\leq 4/3$ this typically occurs first *locally*
somewhere in the star, and there can be a *local* rearrangement of the
stellar gas that prevents catastrophic consequences. However, this
local rearrangements are not always sufficient or even possible, and
sometimes *global* consequences of the impossibility of stability occur:
for example the theorized (pulsational) pair instability supernovae
where a (very) massive star is completely obliterated and leaves
behind no black hole.

-   **Q**: for a star made only of photons, what is $\Gamma$? **Hint**: think of the
    $P\equiv P(u_{})$ relation!


<a id="orgeb11170"></a>

### Use of gravitational energy in a star: negative heat capacity

Let's consider a star made of a perfect mono-atomic gas with $\Gamma=5/3$.
Let's say that for some reason this star is contracting (e.g., because
it is in its formation process). Let's assume this contraction is
quasi-static, meaning that at any point in time the hydrostatic
equilibrium assumption holds, and all the bulk motion of the gas is
very slow compared to thermal velocities, that is $v\ll v_{th} = (2k_{B}T/m)^{1/2}$,
and thus also highly sub-sonic, $v\ll c_\mathrm{sound}$.

The contraction increases the gravitational potential energy
$E_\mathrm{pot} \propto GM^{2}/R$ since $M$ is by assumption constant and $R$
decreases. The total energy $E_\mathrm{tot}$ also increases, but only
by half the amount that the gravitational potential increases. The
other half goes into internal thermal energy of the gas because of the
Virial theorem! This is the limit in the amount of work that can be
extracted set by the virial theorem mentioned above.

For an ideal  gas, the internal energy is related to the
mean temperature by

<div class="latex" id="org5e803ad">
\begin{equation}
E_\mathrm{int} = \frac{\# \mathrm{degrees\ of\ freedom}}{2}Nk_{B}\langle T \rangle
\end{equation}

</div>

where $N = \int \rho/(\mu m_{u})dV = M/(\mu m_{u})$ is the number of particles, with
$\mu$ mean molecular weight assumed to be constant, $\langle T \rangle$ is the
average temperature in the star, and the number of degrees of freedom
is 3 for a monoatomic gas. From the Virial theorem it follows that:

<div class="latex" id="org38ecd17">
\begin{equation}
E_\mathrm{int} = - \frac{E_\mathrm{pot}}{2} \Rightarrow \frac{3}{2} \frac{M}{\mu m_{u}} k_{B}\langle T \rangle = C \frac{GM^{2}}{R} \ \ ,
\end{equation}

</div>

where $C = \{\int_{0}^{M} Gmdm/r\}/\{GM^{2}/R\}$ is a constant of $\mathcal{O}(1)$
that depends on the mass distribution in the star. Thus:

<div class="latex" id="org6806bfb">
\begin{equation}
\langle T \rangle = \frac{2\mu m_{u}}{3 k_{B}} C \frac{GM^{}}{R} \propto \frac{\mu M}{R} \ \ .
\end{equation}

</div>

From this equation, several important facts follow for any
self-gravitating star in hydrostatic equilibrium:

-   the mean temperature of a star depends only on its mass $M$ and radius $R$
    (and chemical composition through &mu;);
-   *as a star contracts* ($R$ decreases at constant mass $M$), *the
    temperature must rise*! This, as we will see, governs the evolution
    of stars.
-   A self-gravitating collection of particle with finite temperature
    must radiate away energy, thus it will lose energy. This energy
    loss, since $E_\mathrm{tot} = |E_\mathrm{pot}|/2 = - CGM^{2}/2R <0$ implies that $R$ must
    decrease. But then, $\langle T \rangle$ must increase! This is the "gravothermal"
    collapse of a cloud/star. As thermal energy is lost to radiation at
    the surface, the (average) temperature raises! This is why stars can
    be thought of objects with *negative* heat capacity: it heats up as it
    loses energy! This is a property typical of self-gravitating systems
    only (stars and gravitationally bound stellar clusters) and because
    of the virial theorem it does not violate energy conservation.
-   The gravothermal collapse must go on until either:
    
    1.  an internal energy source, compensating for the surface energy loss kicks in, or
    2.  the ideal gas approximation does not hold anymore.
    
    As we will see, both 1. and 2. occur in nature: 1. is the typical option for
    stars using nuclear fusion as internal energy source to delay the
    collapse, and 2. is what occurs for white dwarfs, where quantum
    mechanical effects stop the collapse.

Thus, *gravity determines not only the structure (through the
hydrostatic equilibrium equation) but also the evolution of a star*. It
dictates that as the star loses energy, it must heat up. Because of
this, at some point nuclear fusion can occur (as we will discuss
later): *stars don't shine because they burn, stars burn because they
shine*. Without the loss of (internal/thermal) energy by radiation they
would not contract, without contracting they would not reach
temperatures high enough to do nuclear fusion. **The nuclear fusion is a
consequence of the fact that stars shine, and not the cause**. Stars
shine as any object with finite temperature must do.

Internal energy sources such as nuclear fusion ultimately only delay
the gravothermal collapse of the stars until either the ideal gas
approximation does not hold (for white dwarfs) or even nuclear fusion
cannot stop the collapse, and gravity wins, leading to a supernova
explosion and/or the formation of a black hole.


<a id="orgacb56d8"></a>

## Kelvin-Helmholtz timescale

This is by definition the timescale it takes a star to radiate away
all its internal energy at a constant rate in absence of any other
energy sources. Note that this is a *global* timescale for the whole
star!

Let's call L the "luminosity of the star", that is the rate at which
is loses energy from radiating away photons at its surface. Note that
L has the units of power [L] = [E]/[t].

Then by definition:

<div class="latex" id="org54b7230">
\begin{equation}\label{eq:tau_KH}
\tau_\mathrm{KH} = \frac{\mathrm{E}_\mathrm{int}}{L} \equiv
\frac{\mathrm{E}_\mathrm{pot}}{2L} \simeq \frac{GM^{2}}{2RL} \ \ ,
\end{equation}

</div>

where we have used the virial theorem and set $C\simeq1$. We can scale all
the quantities to Solar values and obtain:

<div class="latex" id="orgb3df4dc">
\begin{equation}\label{eq:KH_timescale_scaling}
\tau_{KH} \simeq 1.57 \times 10^{7} \mathrm{years} \times \left(\frac{M}{M_{\odot}}\right)^{2} \left(\frac{R}{R_{\odot}}\right)^{-1 }\left(\frac{L}{L_{\odot}}\right)^{-1} \ \ .
\end{equation}

</div>

Clearly $\tau_{KH} \gg \tau_{ff}$, and also $\gg$ {human timescales}: it is hard to
get direct observational evidence that stars are in thermal
equilibrium. In fact, the name of this timescale comes from proposals
in the late 19<sup>th</sup> century by Kelvin and Helmholtz that the Sun may be
out of thermal equilibrium and contracting, meaning it would have a
lifetime of the order of &sim; 10 million years &#x2013; this was in contrast
with geological evidence (and with the timescale necessary for
Darwinian evolution), leading to a great debate that was ultimately
settled with the discovery of nuclear energy as a potential source of
energy in the 1930s (by primarily [Hans Bethe](https://en.wikipedia.org/wiki/Hans_Bethe) and collaborators), see G.
Shaviv "Life of stars" for a detailed discussion.

-   **Q**: A star may lose energy also by means other than photons,
    especially neutrinos. If such energy losses are important, how can
    we modify Eq. \ref{eq:tau_KH}?


<a id="org0a81841"></a>

# Homework

Using the virial theorem:

-   Estimate the average temperature of the Sun and compare it with its
    surface temperature. Is the Sun in global thermal equilibrium? (you
    can assume C&sim;1 in the notation used in class/in my notes, or use the
    mass and radius profile from the `MESA-web` model you already computed
    to calculate a more precise value for C)
-   Find an order of magnitude (&sim;) relation between the average sound
    speed in the star and the escape velocity (assume the star is made
    of ideal gas of temperature &lang; T &rang;).
-   Demonstrate that if a binary loses instantaneously an amount of mass
    greater than half the total mass of the binary, &Delta; M &ge; (M<sub>1</sub>+M<sub>2</sub>)/2,
    then the orbit is unbound. This can happen when a supernova goes off
    in a binary (cf. [Blaauw 1961](https://ui.adsabs.harvard.edu/abs/1961BAN....15..265B/abstract))!
-   determine a condition for the minimum mass of a gas cloud to
    collapse as a function of its temperature and density (**Hint**:
    collapse &hArr; d<sup>2</sup> I/dt<sup>2</sup><0)

Using the model of the 1M<sub>o</sub> star computed earlier with `MESA-web`:

-   use one profile file to plot &Gamma;<sub>1</sub>&equiv;&Gamma;<sub>1</sub>(m) for a Sun-like star
    of roughly the same age as the Sun. Label the age of the star for
    the corresponding profile.


<a id="orgba6b3ce"></a>

## The Sun with no energy sources

Let's use `MESA-web` to revisit the late 19<sup>th</sup> century/early 20<sup>th</sup> century
debate on the age of the Earth/Sun. (Astro)physicists calculated the
Kelvin-Helmholtz timescale and assumed that this was the age of the
Sun (from Eq. \ref{eq:KH_timescale_scaling}). Geologists and
biologists instead argued for a much longer age.

Let's assume we know the age of the Earth to be 4.5&times;10<sup>9</sup> years (this is
what the geologist and biologists argued!), but let's assume, like
physicists had to before knowing nuclear physics, that there is no
internal energy source in the Sun. In `MESA-web`, there is a `Burning
Modifiers` option where you can disable energy release and chemical
evolution. Make a model of a 1M<sub>o</sub> star without energy release
and/or chemical evolution, until 4.5&times;10<sup>9</sup> years, and plot an HR
diagram. Plot also the 1M<sub>o</sub> star you ran previously (which should
have included the nuclear energy release and chemical evolution).

**N.B.:** we can make a computer code do whatever we want! *Never* take
computer simulations as ground truth, they are *at best* only as good as
the input!

Write a short paragraph answering the following:

-   Which agrees better with the observation of the real Sun at the
    Earth's age?
-   What is its radius and how does it compare to the measured R<sub>o</sub>?
    (**hint**: you can plot the lines at constant radius on the HRD, or read
    the outermost radius from the last `profile*.data` file you saved)
-   What is the average density of the model without energy generation?
    (an order of magnitude estimate is sufficient for the purpose).

