# Unit D: Fields — Solutions

---

## Solution 1

**Answer: C** — $\dfrac{g_0}{4}$

The gravitational field strength at distance $r$ from the centre of a planet is $g = \dfrac{GM}{r^2}$.

At the surface ($r = R$): $g_0 = \dfrac{GM}{R^2}$.

At height $R$ above the surface, the distance from the centre is $r = 2R$:

$$g = \frac{GM}{(2R)^2} = \frac{GM}{4R^2} = \frac{g_0}{4}$$

- **A** is incorrect: this would require $r = R$, i.e. at the surface.
- **B** is incorrect: $g \propto 1/r^2$, not $1/r$.
- **D** is incorrect: this would correspond to $r = 2\sqrt{2}R$, not $2R$.

---

## Solution 2

**Answer: C** — $V_g$ is always negative and its magnitude decreases with distance.

Gravitational potential is defined as $V_g = -\dfrac{GM}{r}$, with the zero of potential at infinity. Since $r > 0$ for all finite points, $V_g$ is always **negative**. As $r$ increases, the magnitude $|V_g| = GM/r$ decreases (becomes less negative, approaching zero).

- **A** is incorrect: potential at the surface is $-GM/R$, not zero. The zero is at infinity.
- **B** is incorrect: $V_g$ is negative (except at $r \to \infty$, where it approaches zero from below).
- **D** is incorrect: $V_g$ is a scalar quantity (though measured in J kg$^{-1}$, which is correct, the "vector" claim makes this wrong).

---

## Solution 3

**(a) Orbital radius** [1 mark]

$$r = R + h = 6.37 \times 10^6 + 3.58 \times 10^7 = 4.22 \times 10^7\ \mathrm{m}$$

✓ Correct addition and units.

---

**(b) Orbital speed** [1 mark]

For a circular orbit, gravitational force provides centripetal force:

$$\frac{GMm}{r^2} = \frac{mv^2}{r} \quad \Rightarrow \quad v = \sqrt{\frac{GM}{r}}$$

$$v = \sqrt{\frac{(6.67 \times 10^{-11})(5.97 \times 10^{24})}{4.22 \times 10^7}}$$

$$v = \sqrt{\frac{3.98 \times 10^{14}}{4.22 \times 10^7}} = \sqrt{9.44 \times 10^6}$$

$$v = 3.07 \times 10^3\ \mathrm{m\,s^{-1}}$$

✓ Uses correct formula; value matches the "show that".

---

**(c) Orbital period** [1 mark]

$$T = \frac{2\pi r}{v} = \frac{2\pi \times 4.22 \times 10^7}{3.07 \times 10^3} = \frac{2.65 \times 10^8}{3.07 \times 10^3}$$

$$T = 8.63 \times 10^4\ \mathrm{s} \approx 24\ \text{hours}$$

✓ This confirms the satellite is geostationary.

**Total: 3 marks**

---

## Solution 4

**Answer: B** — $\displaystyle \sqrt{\frac{2GM}{R}}$

Escape speed is derived by equating kinetic energy to the magnitude of gravitational potential energy:

$$\frac{1}{2}mv_{\text{esc}}^2 = \frac{GMm}{R} \quad \Rightarrow \quad v_{\text{esc}} = \sqrt{\frac{2GM}{R}}$$

- **A** is the **orbital** speed for a circular orbit at the surface, not escape speed.
- **C** is the gravitational field strength $g$ at the surface — dimensionally incorrect (m s$^{-2}$, not m s$^{-1}$).
- **D** is missing the square root; dimensionally incorrect.

---

## Solution 5

**(a)** [1 mark]

For a circular orbit, Kepler's third law is:

$$T^2 = \frac{4\pi^2}{GM}\,r^3$$

where $T$ is the orbital period, $r$ is the orbital radius, $M$ is the mass of the central body, and $G$ is the gravitational constant. This form applies when $M \gg m$ (the satellite mass is negligible compared to Earth).

---

**(b)** [1 mark]

Rearranging: $r^3 = \dfrac{GMT^2}{4\pi^2}$

$$r^3 = \frac{(6.67 \times 10^{-11})(5.97 \times 10^{24})(4.00 \times 10^4)^2}{4\pi^2}$$

$$r^3 = \frac{(3.98 \times 10^{14})(1.60 \times 10^9)}{39.48} = \frac{6.37 \times 10^{23}}{39.48}$$

$$r^3 = 1.61 \times 10^{22}$$

$$r = \sqrt[3]{1.61 \times 10^{22}} = 2.53 \times 10^7\ \mathrm{m}$$

---

**(c)** [1 mark]

$$v = \frac{2\pi r}{T} = \frac{2\pi \times 2.53 \times 10^7}{4.00 \times 10^4}$$

$$v = \frac{1.59 \times 10^8}{4.00 \times 10^4} = 3.97 \times 10^3\ \mathrm{m\,s^{-1}}$$

**Total: 3 marks**

---

## Solution 6

**Answer: D** — $16F$

Coulomb's law: $F = \dfrac{k|q_1q_2|}{r^2}$.

Original: $F = \dfrac{kQ^2}{r^2}$.

New charges: $+2Q$ and $-2Q$. New separation: $r/2$.

$$F' = \frac{k(2Q)(2Q)}{(r/2)^2} = \frac{4kQ^2}{r^2/4} = 16 \times \frac{kQ^2}{r^2} = 16F$$

- **A**: ignores all changes.
- **B**: only accounts for doubling both charges ($\times 4$) but forgets the separation change.
- **C**: $\times 8$ has no clear physical basis.

---

## Solution 7

**Answer: C** — $4000\ \mathrm{V\,m^{-1}}$

For parallel plates: $E = \dfrac{V}{d}$.

$$E = \frac{200}{0.050} = 4000\ \mathrm{V\,m^{-1}}$$

- **A** ($10$): erroneously multiplies $V$ and $d$, or uses $0.05 \times 200$.
- **B** ($100$): uses $V/2$, no physical basis.
- **D** ($10\,000$): divides by $0.020$ instead of $0.050$, or uses $V^2/d$.

---

## Solution 8

**(a) Net electric potential at the midpoint** [2 marks]

The midpoint is $r = 0.20\ \mathrm{m}$ from each charge.

Potential due to a point charge: $V = \dfrac{kq}{r}$. Potential is a scalar — signs are included.

$$V_1 = \frac{(8.99 \times 10^9)(+2.0 \times 10^{-6})}{0.20} = \frac{1.798 \times 10^4}{0.20} = 8.99 \times 10^4\ \mathrm{V}$$

$$V_2 = \frac{(8.99 \times 10^9)(-3.0 \times 10^{-6})}{0.20} = \frac{-2.697 \times 10^4}{0.20} = -1.35 \times 10^5\ \mathrm{V}$$

$$V_{\text{net}} = V_1 + V_2 = 8.99 \times 10^4 + (-1.35 \times 10^5) = -4.5 \times 10^4\ \mathrm{V}$$

✓ [1] for each potential, [1] for correct sum — **2 marks**

---

**(b) Work done** [2 marks]

The work done **by the electric field** when a charge $q$ moves from infinity (where $V = 0$) to a point with potential $V$ is:

$$W = -q\Delta V = -q(V_{\text{final}} - V_{\text{initial}}) = -qV_{\text{midpoint}}$$

$$W = -(1.0 \times 10^{-6})(-4.5 \times 10^4) = +4.5 \times 10^{-2}\ \mathrm{J}$$

The positive sign means work is done **by the field** (the charge is attracted to the net negative potential region).

Alternatively, if the question is interpreted as work done **on** the charge **by an external agent** to bring it from infinity, that work is $W_{\text{ext}} = qV = -4.5 \times 10^{-2}\ \mathrm{J}$ (negative, meaning the field does the work).

✓ [1] for using $W = qV$ or $W = -q\Delta V$; [1] for correct numerical answer with sign — **2 marks**

**Total: 4 marks**

---

## Solution 9

**Answer: A** — concentric spheres centred on the charge

For an isolated point charge, $V = kq/r$. All points at the same distance $r$ have the same potential, forming spherical surfaces.

- **B** describes electric field lines, not equipotential surfaces.
- **C** describes equipotentials for a uniform electric field (parallel plates).
- **D** describes equipotentials for a line charge, not a point charge.

---

## Solution 10

**Answer: B** — $eE$ to the left

The force on a charge in an electric field is $\vec{F} = q\vec{E}$. The electron has charge $q = -e$, so $\vec{F} = -e\vec{E}$. If $\vec{E}$ points to the right, $\vec{F}$ points to the left with magnitude $eE$.

- **A**: would be correct for a **positive** charge.
- **C**: an electron in an electric field always experiences a force unless $E = 0$.
- **D**: the force is parallel (or antiparallel) to the field, not perpendicular. Perpendicular force is characteristic of magnetic fields.

---

## Solution 11

**Answer: B** — zero

Magnetic force: $F = qvB\sin\theta$, where $\theta$ is the angle between $\vec{v}$ and $\vec{B}$.

When $\vec{v} \parallel \vec{B}$, $\theta = 0^\circ$ (or $180^\circ$), so $\sin\theta = 0$ and $F = 0$.

- **A**: gives force when $\theta = 90^\circ$.
- **C**, **D**: have no physical basis.

---

## Solution 12

**(a) Magnitude of magnetic force** [2 marks]

$$F = BIL\sin\theta$$

$$F = (0.20)(3.0)(0.50)(\sin 30^\circ)$$

$$F = 0.20 \times 3.0 \times 0.50 \times 0.50$$

$$F = 0.15\ \mathrm{N}$$

✓ [1] for correct formula; [1] for correct substitution and answer — **2 marks**

---

**(b) Maximum force** [1 mark]

The force is maximum when $\sin\theta = 1$, i.e. $\theta = 90^\circ$. The wire should be **perpendicular** to the magnetic field.

✓ **1 mark**

**Total: 3 marks**

---

## Solution 13

**(a) Circular path** [1 mark]

The magnetic force is always perpendicular to the velocity: $\vec{F} = q(\vec{v} \times \vec{B})$. Since the force is perpendicular to the motion, it acts as a centripetal force, changing the direction but not the speed. This produces uniform circular motion.

✓ **1 mark**

---

**(b) Radius** [1 mark]

Centripetal force = magnetic force:

$$\frac{mv^2}{r} = qvB \quad \Rightarrow \quad r = \frac{mv}{qB}$$

$$r = \frac{(1.67 \times 10^{-27})(2.0 \times 10^6)}{(1.60 \times 10^{-19})(0.50)}$$

$$r = \frac{3.34 \times 10^{-21}}{8.0 \times 10^{-20}} = 4.18 \times 10^{-2}\ \mathrm{m} = 4.2\ \mathrm{cm}$$

✓ **1 mark**

---

**(c) Period** [1 mark]

$$T = \frac{2\pi r}{v} = \frac{2\pi m}{qB}$$

$$T = \frac{2\pi \times 1.67 \times 10^{-27}}{(1.60 \times 10^{-19})(0.50)} = \frac{1.049 \times 10^{-26}}{8.0 \times 10^{-20}}$$

$$T = 1.31 \times 10^{-7}\ \mathrm{s}$$

✓ **1 mark**

**Total: 3 marks**

---

## Solution 14

**Answer: B** — doubles

The radius of a charged particle's circular path in a magnetic field is $r = \dfrac{mv}{qB}$.

Since $r \propto v$ (with $m$, $q$, $B$ constant), doubling $v$ doubles $r$.

- **A**: would be true only if $v$ too were unchanged.
- **C**: is the inverse relationship, confused with $r \propto 1/v$.
- **D**: would require $r \propto v^2$, which is not the case.

---

## Solution 15

**Answer: A** — upward (out of the page)

Using the right-hand rule for $\vec{F} = q(\vec{v} \times \vec{B})$:

- $\vec{v}$: east (point fingers east)
- $\vec{B}$: north (curl fingers toward north)
- $\vec{F}$: thumb points **upward** (out of the page)

- **B** (downward): would be the direction for a **negative** charge.
- **C** (west): confuses the cross product direction.
- **D** (south): opposite to the field direction, no physical basis.

---

## Solution 16

**Answer: C** — $\sqrt{V}$

Work–energy: the work done by the electric field equals the kinetic energy gained.

$$eV = \frac{1}{2}mv^2 \quad \Rightarrow \quad v = \sqrt{\frac{2eV}{m}}$$

Thus $v \propto \sqrt{V}$.

- **A**: would be true if $eV = mv$ (incorrect: energy, not momentum).
- **B**: would require $eV \propto v^2 \Rightarrow V \propto v^2$, so $v \propto \sqrt{V}$, not $V^2$.
- **D**: inverse relationship, physically incorrect.

---

## Solution 17 [HL]

**(a) Speed of undeflected ions** [1 mark]

In a velocity selector, electric force equals magnetic force:

$$qE = qvB \quad \Rightarrow \quad v = \frac{E}{B}$$

$$v = \frac{2.0 \times 10^4}{0.10} = 2.0 \times 10^5\ \mathrm{m\,s^{-1}}$$

✓ **1 mark**

---

**(b) Mass of ions** [2 marks]

In the magnetic field only, circular motion: $\dfrac{mv^2}{r} = qvB \;\Rightarrow\; m = \dfrac{qBr}{v}$

$$m = \frac{(1.60 \times 10^{-19})(0.10)(0.25)}{2.0 \times 10^5}$$

$$m = \frac{4.0 \times 10^{-21}}{2.0 \times 10^5} = 2.0 \times 10^{-26}\ \mathrm{kg}$$

✓ [1] for formula; [1] for correct substitution and answer — **2 marks**

---

**(c) Mass in atomic mass units** [1 mark]

$$m = \frac{2.0 \times 10^{-26}}{1.66 \times 10^{-27}} \approx 12.0\ \mathrm{u}$$

This corresponds to a **carbon-12** ion ($^{12}\mathrm{C}^+$).

✓ **1 mark**

---

**(d) Application** [1 mark]

Mass spectrometers are used for:
- Determining the isotopic composition of elements
- Identifying unknown compounds by their mass spectrum
- Radiocarbon dating
- Pharmaceutical analysis

✓ **1 mark** for any valid application.

**Total: 5 marks**

---

## Solution 18

**Answer: B** — $T = \dfrac{2\pi m}{qB}$ has no dependence on $v$

The cyclotron period is $T = \dfrac{2\pi m}{qB}$. Although the radius increases as the particle gains speed ($r = mv/qB$), and $T = 2\pi r/v$, the ratio $r/v = m/qB$ is constant, so $T$ is independent of $v$.

- **A** is true (magnetic force does no work) but does not directly explain why $T$ is constant.
- **C** is a feature of cyclotron operation but not the reason $T$ is independent of speed.
- **D** contains the correct physics but is essentially a restatement; **B** is the fundamental reason.

---

## Solution 19

**(a) Electron speed** [1 mark]

$$\frac{1}{2}m_ev^2 = eV \quad \Rightarrow \quad v = \sqrt{\frac{2eV}{m_e}}$$

$$v = \sqrt{\frac{2 \times 1.60 \times 10^{-19} \times 2000}{9.11 \times 10^{-31}}}$$

$$v = \sqrt{\frac{6.40 \times 10^{-16}}{9.11 \times 10^{-31}}} = \sqrt{7.03 \times 10^{14}}$$

$$v = 2.65 \times 10^7\ \mathrm{m\,s^{-1}}$$

✓ **1 mark**

---

**(b) Radius of circular path** [1 mark]

$$r = \frac{m_ev}{eB} = \frac{(9.11 \times 10^{-31})(2.65 \times 10^7)}{(1.60 \times 10^{-19})(5.0 \times 10^{-3})}$$

$$r = \frac{2.41 \times 10^{-23}}{8.0 \times 10^{-22}} = 3.02 \times 10^{-2}\ \mathrm{m} = 3.0\ \mathrm{cm}$$

✓ **1 mark**

---

**(c) Period of revolution** [1 mark]

$$T = \frac{2\pi m_e}{eB} = \frac{2\pi \times 9.11 \times 10^{-31}}{(1.60 \times 10^{-19})(5.0 \times 10^{-3})}$$

$$T = \frac{5.72 \times 10^{-30}}{8.0 \times 10^{-22}} = 7.15 \times 10^{-9}\ \mathrm{s}$$

(Note: $T$ is independent of speed, so the same result follows from $T = 2\pi r/v$.)

✓ **1 mark**

**Total: 3 marks**

---

## Solution 20 [HL]

**(a) Electric field strength** [1 mark]

$$E = \frac{V}{d} = \frac{30}{0.020} = 1.50 \times 10^3\ \mathrm{V\,m^{-1}}$$

✓ Field direction: downward (from + upper plate to − lower plate). **1 mark**

---

**(b) Vertical acceleration** [1 mark]

$$a = \frac{F}{m_e} = \frac{eE}{m_e}$$

$$a = \frac{(1.60 \times 10^{-19})(1.50 \times 10^3)}{9.11 \times 10^{-31}} = \frac{2.40 \times 10^{-16}}{9.11 \times 10^{-31}}$$

$$a = 2.63 \times 10^{14}\ \mathrm{m\,s^{-2}}\ \text{(downward)}$$

✓ Electron is negative, so force is upward (opposite to field), toward the positive upper plate. Acceleration direction: upward. **1 mark**

---

**(c) Time between plates** [1 mark]

Horizontal motion is at constant velocity (no horizontal force):

$$t = \frac{L}{v_x} = \frac{0.040}{5.0 \times 10^6} = 8.0 \times 10^{-9}\ \mathrm{s}$$

✓ **1 mark**

---

**(d) Vertical deflection** [1 mark]

Vertical displacement (constant acceleration, zero initial vertical velocity):

$$y = \frac{1}{2}at^2$$

$$y = \frac{1}{2} \times (2.63 \times 10^{14}) \times (8.0 \times 10^{-9})^2$$

$$y = \frac{1}{2} \times (2.63 \times 10^{14}) \times (6.40 \times 10^{-17})$$

$$y = \frac{1}{2} \times 1.68 \times 10^{-2} = 8.42 \times 10^{-3}\ \mathrm{m} = 8.4\ \mathrm{mm}$$

The electron enters midway between plates, so the distance to the upper plate is $\dfrac{0.020}{2} = 0.010\ \mathrm{m} = 10\ \mathrm{mm}$. Since $8.4\ \mathrm{mm} < 10\ \mathrm{mm}$, the electron **does not hit the plate** and exits the field region.

✓ **1 mark**

**Total: 4 marks**

---

## Solution 21

**Answer: B** — $25\ \mathrm{V}$

Faraday's law: $\varepsilon = N\dfrac{\Delta\Phi}{\Delta t}$.

$$\varepsilon = 100 \times \frac{0.050}{0.20} = 100 \times 0.25 = 25\ \mathrm{V}$$

- **A** ($10$): forgets the factor of $N$, using $\varepsilon = \Delta\Phi/\Delta t = 0.25\ \mathrm{V}$ → hmm wait, $0.050/0.20 = 0.25$ V, not $10$. Actually $10$ would be using $\Phi/t = 0.05/0.005 = 10$ — no. $10$ could come from $0.050 \times 0.20 = 0.01$, then $\times 1000$ error. Or more likely, using $N\Phi/t$ wrong: $100 \times 0.05 / 0.5 = 10$.
- **C** ($50$): uses $\varepsilon = 2N\Delta\Phi/\Delta t$ or doubles incorrectly.
- **D** ($250$): uses $\varepsilon = N\Delta\Phi \times \Delta t = 100 \times 0.050 \times 0.20 \times 25$... no clear basis.

---

## Solution 22

**Answer: A** — conservation of energy

Lenz's law states that the direction of induced current is such that it opposes the change in magnetic flux that produced it. If the induced current reinforced the change instead, a small change would produce a larger change, which would produce an even larger induced current — violating conservation of energy (a "runaway" process).

- **B**: conservation of charge relates to Kirchhoff's current law.
- **C**: Newton's third law concerns action–reaction force pairs.
- **D**: conservation of momentum is unrelated to induction.

---

## Solution 23 [HL]

**(a) Angular frequency** [1 mark]

$$\omega = 300\ \text{rpm} \times \frac{2\pi\ \text{rad}}{1\ \text{rev}} \times \frac{1\ \text{min}}{60\ \text{s}}$$

$$\omega = 300 \times \frac{2\pi}{60} = 10\pi\ \mathrm{rad\,s^{-1}} = 31.4\ \mathrm{rad\,s^{-1}}$$

✓ **1 mark**

---

**(b) Magnetic flux** [1 mark]

At $t = 0$, the plane of the coil is perpendicular to $\vec{B}$, so the area vector $\vec{A}$ is parallel to $\vec{B}$. The flux is maximum:

$$\Phi(t) = BA\cos(\omega t)$$

$$\Phi(t) = (0.40)(0.020)\cos(10\pi t)$$

$$\Phi(t) = 8.0 \times 10^{-3}\cos(10\pi t)\ \mathrm{Wb}$$

✓ **1 mark**

---

**(c) Induced emf** [2 marks]

Faraday's law: $\varepsilon = -N\dfrac{d\Phi}{dt}$

$$\varepsilon(t) = -N\frac{d}{dt}\bigl[BA\cos(\omega t)\bigr]$$

$$\varepsilon(t) = -N\bigl[-BA\omega\sin(\omega t)\bigr]$$

$$\varepsilon(t) = NBA\omega\sin(\omega t)$$

Substituting values:

$$\varepsilon(t) = (50)(0.40)(0.020)(10\pi)\sin(10\pi t)$$

$$\varepsilon(t) = 50 \times 0.0080 \times 10\pi \times \sin(10\pi t)$$

$$\varepsilon(t) = 12.6\sin(10\pi t)\ \mathrm{V}$$

✓ [1] for correct differentiation; [1] for correct substitution — **2 marks**

---

**(d) Peak emf** [1 mark]

$$\varepsilon_0 = NBA\omega = 12.6\ \mathrm{V}$$

(Since $\sin(10\pi t)$ has a maximum value of 1.)

✓ **1 mark**

**Total: 5 marks**

---

## Solution 24

**Answer: B** — parallel to the magnetic field

The induced emf is $\varepsilon = NBA\omega\sin(\omega t)$. The emf is maximum when $|\sin(\omega t)| = 1$, which occurs at $\omega t = 90^\circ, 270^\circ, \ldots$ — i.e. when the plane of the coil is **parallel** to $\vec{B}$. At this orientation, the rate of change of flux through the coil is greatest.

- **A**: when perpendicular to the field ($\omega t = 0$), $\Phi$ is maximum but $d\Phi/dt = 0$, so $\varepsilon = 0$.
- **C**, **D**: intermediate angles give $\varepsilon < \varepsilon_{\text{max}}$.

---

## Solution 25 [HL]

**(a) Secondary voltage** [1 mark]

For an ideal transformer: $\dfrac{V_s}{V_p} = \dfrac{N_s}{N_p}$

$$V_s = V_p \times \frac{N_s}{N_p} = 240 \times \frac{50}{500} = 240 \times 0.10 = 24\ \mathrm{V}\ \text{(rms)}$$

✓ **1 mark**

---

**(b) Primary current** [1 mark]

For $100\%$ efficiency: $P_p = P_s \;\Rightarrow\; V_pI_p = V_sI_s$

$$I_p = \frac{V_sI_s}{V_p} = \frac{24 \times 2.0}{240} = \frac{48}{240} = 0.20\ \mathrm{A}\ \text{(rms)}$$

✓ **1 mark**

---

**(c) Damage at lower frequency** [2 marks]

The primary coil of a transformer has inductance, and the **back emf** induced in it opposes the applied voltage. The magnitude of the back emf is proportional to the **rate of change of current**, which depends on the frequency of the AC supply.

At a significantly lower frequency:
- The **rate of change of magnetic flux** in the core decreases.
- The **back emf** in the primary coil is reduced.
- The net voltage driving current through the primary coil's resistance increases, causing the **primary current to rise substantially**.
- This results in excessive **$I^2R$ (Joule) heating** in the primary windings, which can melt insulation or burn out the coil.

This is why transformers are designed for a specific operating frequency and can be damaged if operated at much lower frequencies.

✓ [1] for identifying increased primary current; [1] for linking to overheating/energy dissipation — **2 marks**

**Total: 4 marks**

---

# Mark Scheme Summary

| Q | Topic | Type | Marks | Answer / Key |
|---|---|---|---|---|
| 1 | Gravitational field strength | MCQ | 1 | **C**: $g_0/4$ |
| 2 | Gravitational potential | MCQ | 1 | **C**: always negative, magnitude decreases with $r$ |
| 3 | Geostationary orbit | Paper 2 | 3 | $r = 4.22 \times 10^7$ m; $v = 3.07 \times 10^3$ m/s; $T = 8.63 \times 10^4$ s |
| 4 | Escape velocity | MCQ | 1 | **B**: $\sqrt{2GM/R}$ |
| 5 | Kepler's 3rd Law | Paper 2 | 3 | $r = 2.53 \times 10^7$ m; $v = 3.97 \times 10^3$ m/s |
| 6 | Coulomb's Law | MCQ | 1 | **D**: $16F$ |
| 7 | Parallel plates | MCQ | 1 | **C**: $4000$ V/m |
| 8 | Electric potential | Paper 2 | 4 | $V = -4.5 \times 10^4$ V; $W = +4.5 \times 10^{-2}$ J |
| 9 | Equipotentials | MCQ | 1 | **A**: concentric spheres |
| 10 | Force on charge in $\vec{E}$ | MCQ | 1 | **B**: $eE$ to the left |
| 11 | Force on charge in $\vec{B}$, $\theta = 0$ | MCQ | 1 | **B**: zero |
| 12 | Force on current-carrying wire | Paper 2 | 3 | $F = 0.15$ N; perpendicular to $\vec{B}$ |
| 13 | Circular motion in $\vec{B}$ | Paper 2 | 3 | $r = 4.2$ cm; $T = 1.31 \times 10^{-7}$ s |
| 14 | Radius dependence on $v$ | MCQ | 1 | **B**: doubles |
| 15 | Right-hand rule | MCQ | 1 | **A**: upward |
| 16 | Electron gun: $v \propto \sqrt{V}$ | MCQ | 1 | **C** |
| 17 | Mass spectrometer **[HL]** | Paper 2 | 5 | $v = 2.0 \times 10^5$ m/s; $m = 2.0 \times 10^{-26}$ kg = 12 u ($^{12}$C$^+$) |
| 18 | Cyclotron period | MCQ | 1 | **B**: $T = 2\pi m/qB$, no $v$ dependence |
| 19 | Electron in $\vec{B}$ field | Paper 2 | 3 | $v = 2.65 \times 10^7$ m/s; $r = 3.0$ cm; $T = 7.15 \times 10^{-9}$ s |
| 20 | Electron deflection in $\vec{E}$ **[HL]** | Paper 2 | 4 | $E = 1500$ V/m; $a = 2.63 \times 10^{14}$ m/s²; $y = 8.4$ mm (exits safely) |
| 21 | Faraday's Law (average emf) | MCQ | 1 | **B**: $25$ V |
| 22 | Lenz's Law | MCQ | 1 | **A**: conservation of energy |
| 23 | AC generator / rotating coil **[HL]** | Paper 2 | 5 | $\omega = 10\pi$ rad/s; $\Phi = 0.008\cos(10\pi t)$ Wb; $\varepsilon_0 = 12.6$ V |
| 24 | AC generator peak emf | MCQ | 1 | **B**: parallel to field |
| 25 | Transformer + frequency **[HL]** | Paper 2 | 4 | $V_s = 24$ V; $I_p = 0.20$ A; low $f$ → high $I_p$ → overheating |

| | | **Total** | **50 marks** | |
| **Paper 1 subtotal** | | | **15 marks** | |
| **Paper 2 subtotal** | | | **35 marks** | |

---

> **HL Extension problems: Q17, Q20, Q23, Q25**
