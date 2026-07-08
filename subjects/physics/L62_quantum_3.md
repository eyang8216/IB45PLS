# Lesson 62: Quantum 3 — Matter Waves, Heisenberg Uncertainty, and Wavefunctions

## What You'll Learn

In Lessons 59-61, you learned that light has a dual nature (wave and particle), that electrons have de Broglie wavelengths, and that the photoelectric effect demonstrates quantization. But these discoveries created a deeper problem: if electrons are BOTH particles and waves, what exactly IS an electron? Where is it? How does it move?

Classical physics assumes you can know both the position and velocity of a particle with arbitrary precision. This assumption underlies everything from Newton's laws to Maxwell's equations. But at the quantum scale, this assumption is WRONG — not because our instruments aren't good enough, but because nature itself doesn't allow it. The Heisenberg uncertainty principle says there is a fundamental limit to how precisely position and momentum can be known simultaneously.

This lesson introduces three interconnected ideas that form the core of quantum mechanics: the uncertainty principle, the wavefunction, and the probabilistic interpretation of nature. These are not just abstract philosophy — they explain why atoms don't collapse, why electrons occupy probability clouds instead of orbits, and why the world at the atomic scale is fundamentally different from the world we see.

---

## 1. The End of Certainty: Heisenberg's Uncertainty Principle

### Why This Matters

The uncertainty principle is not a statement about the limitations of measurement technology. It's a statement about the nature of reality. It says that certain pairs of physical properties — position and momentum, energy and time — cannot both be precisely defined at the same instant. This is not because our instruments are clumsy. It's because a particle simply doesn't HAVE a precise position and a precise momentum at the same time. The very concepts are incompatible at the quantum scale.

### The Key Ideas

**What the principle says.** For position (x) and momentum (p), the uncertainty principle states:

$$\Delta x \cdot \Delta p \geq \frac{h}{4\pi} = \frac{\hbar}{2}$$

where:
- Δx is the uncertainty in position (the range within which the particle might be found)
- Δp is the uncertainty in momentum (the range of possible momentum values)
- ℏ = h/(2π) = 1.055 × 10⁻³⁴ J·s

The product of these uncertainties must be at least ℏ/2. You can make Δx very small (know position precisely), but then Δp must be large (momentum becomes uncertain). Conversely, you can know momentum precisely, but then position becomes fuzzy.

**What the principle does NOT say.** Many popular accounts get this wrong. The uncertainty principle does NOT say:
- "We disturb the particle when we measure it" — this is true but it's not what the principle is fundamentally about.
- "We can't measure both position and momentum accurately" — the principle says they can't both BE accurate simultaneously; it's a property of nature, not a measurement limitation.
- "Everything is uncertain so science is meaningless" — the uncertainties are extremely small for macroscopic objects and well-defined mathematically.

**Why electrons don't crash into the nucleus.** Here's a beautiful application. If an electron were confined to a nuclear-sized volume (Δx ≈ 10⁻¹⁵ m), the uncertainty principle says:

Δp ≥ ℏ/(2Δx) ≈ 1.055 × 10⁻³⁴ / (2 × 10⁻¹⁵) ≈ 5 × 10⁻²⁰ kg·m/s

This corresponds to a kinetic energy of roughly:

KE = p²/2m ≥ (5 × 10⁻²⁰)² / (2 × 9.11 × 10⁻³¹) ≈ 10⁻⁹ J ≈ 10¹⁰ eV = 10 GeV!

This is enormous — far more than the binding energy from the Coulomb attraction (which is on the order of MeV). An electron confined to the nucleus would have so much kinetic energy it would immediately fly out. The electron's ground state in hydrogen (r ≈ 5 × 10⁻¹¹ m) represents the optimal compromise between the uncertainty principle (which favors delocalization to keep momentum uncertainty low) and electrostatic attraction (which favors localization near the nucleus). The size of the atom is determined by this balance.

**Energy-time uncertainty.** A second form of the uncertainty principle relates energy and time:

$$\Delta E \cdot \Delta t \geq \frac{\hbar}{2}$$

This means that a quantum state that exists for only a very short time Δt has a correspondingly large uncertainty in its energy ΔE. This explains why spectral lines have a natural width — excited states have finite lifetimes, so their energy is slightly uncertain. This is also why virtual particles in quantum field theory can "borrow" energy for short periods.

### Common Misconceptions

**"The uncertainty principle is just about measurement disturbance."** This is a half-truth taught in some introductory courses. While measurement does disturb quantum systems, the uncertainty principle is deeper: it describes an intrinsic limitation. Even if you could measure without disturbing, the uncertainty would remain. A particle confined to a small region simply doesn't have a well-defined momentum, regardless of measurement.

**"Heisenberg uncertainty applies to everything, including macroscopic objects."** In principle, yes. For a 1 kg object, Δx·Δp ≥ 5.27 × 10⁻³⁵ m·kg·m/s. If we know its position to 1 mm (10⁻³ m), the momentum uncertainty is about 5 × 10⁻³² kg·m/s, corresponding to a velocity uncertainty of about 5 × 10⁻³² m/s. This is utterly negligible — about the distance of a proton diameter per year. The uncertainty principle is always present but only matters when ℏ is not negligible compared to the relevant position and momentum scales.

---

## 2. The Wavefunction: What an Electron "Is"

### Why This Matters

If electrons aren't tiny billiard balls and they aren't classical waves either, then what ARE they? The answer, developed by Erwin Schrödinger in 1926, is that every particle is described by a **wavefunction** — a mathematical function that contains all possible information about the particle. The wavefunction is the central concept of quantum mechanics.

### The Key Ideas

**What is a wavefunction?** The wavefunction, usually denoted by the Greek letter ψ (psi), is a mathematical function of position and time: ψ(x, t). It is generally complex-valued (contains imaginary numbers). The wavefunction itself is not directly observable — you can't "see" a wavefunction. But the wavefunction determines everything you CAN observe about a particle.

**Schrödinger's equation.** The wavefunction evolves in time according to the Schrödinger equation. We won't solve it in IB Physics (that's university-level), but the key idea is: given the forces acting on a particle (potential energy V(x)), Schrödinger's equation tells you how ψ(x, t) changes. It's the quantum equivalent of Newton's F = ma.

**Born's probabilistic interpretation.** Max Born proposed (and won the Nobel Prize for) the interpretation that changed everything: the square of the absolute value of the wavefunction, |ψ(x)|², gives the probability density of finding the particle at position x.

Formally: the probability of finding the particle in a small region dx around position x is:

$$P(x) \, dx = |\psi(x)|^2 \, dx$$

This means:
- Where |ψ|² is large, the electron is likely to be found.
- Where |ψ|² is small, the electron is unlikely to be found.
- The total probability of finding the electron SOMEWHERE is 1 (normalization): ∫|ψ|² dx = 1.

**What this means: probability clouds, not orbits.** An electron in an atom does NOT follow a well-defined orbit like a planet. Instead, it exists as a "cloud" of probability — regions where it's more likely or less likely to be detected. A hydrogen atom in its ground state has a spherically symmetric probability distribution with maximum probability at the Bohr radius (5.29 × 10⁻¹¹ m). But the electron can sometimes be found closer to or farther from the nucleus — just with lower probability.

**The standing wave picture from Lesson 59 now makes more sense.** In Lesson 59, we said the electron's de Broglie wave must form a standing wave around the nucleus. That was a semi-classical picture. The full quantum mechanical picture is: the wavefunction ψ(x) is a standing wave in three dimensions. The boundary conditions (ψ must be finite, continuous, and single-valued) lead to quantization — only certain "shapes" of ψ are allowed. Each allowed shape corresponds to an energy level.

### Common Misconceptions

**"The electron is smeared out into a cloud."** This is sloppy language. The electron is still a particle (it's always detected as a single point). The "cloud" describes our KNOWLEDGE of where the electron might be. Before measurement, the electron doesn't have a definite position — it's in a superposition of possible positions. Upon measurement, it's found at one specific location. The probability cloud describes the likelihood of each possible outcome.

**"The wavefunction is a physical wave, like a water wave."** No. The wavefunction is a mathematical construct — a complex-valued function that encodes probabilities. It propagates and interferes like a wave, but it's not a physical vibration of any medium. It's a "probability wave." This is why de Broglie's matter waves are not physical vibrations but probability amplitudes.

---

## 3. Quantum Tunneling (Introduction)

### Why This Matters

Quantum tunneling is one of the most dramatic consequences of the wave nature of matter. It's the reason the Sun shines (protons tunnel through their mutual electrostatic repulsion to start fusion), the reason some radioactive decays occur, and the operating principle behind scanning tunneling microscopes. A full treatment comes in Lesson 63, but the basic idea belongs here because it follows directly from the wavefunction.

### The Key Ideas

**The classical picture.** Imagine a ball rolling toward a hill. If the ball doesn't have enough kinetic energy to reach the top, it rolls back down. It can never appear on the other side of the hill. This is classical physics: a particle cannot cross a barrier higher than its total energy.

**The quantum picture.** A quantum particle is described by a wavefunction that extends slightly INTO the barrier and, if the barrier is thin enough, emerges on the other side. Even if the particle's energy is less than the barrier height, there is a non-zero probability of finding it on the far side. This is **quantum tunneling**.

**Why tunneling happens.** The wavefunction doesn't abruptly go to zero at the barrier. In classical physics, the particle would have "negative kinetic energy" inside the barrier (since E < V), which is impossible. In quantum mechanics, the wavefunction decays exponentially inside the barrier — it gets smaller but doesn't vanish. If the barrier is thin enough, the wavefunction still has non-zero amplitude at the far side, meaning there's a probability the particle "tunneled through."

**The tunneling probability** depends on:
- Barrier height: higher barriers → less tunneling
- Barrier width: wider barriers → exponentially less tunneling
- Particle mass: heavier particles → less tunneling (the de Broglie wavelength is shorter)

---

## 4. The Quantum-Mechanical Atom (Beyond Bohr)

### Why This Matters

Bohr's model gave correct energy levels for hydrogen but couldn't explain multi-electron atoms, chemical bonding, or the shapes of molecules. The quantum mechanical model, based on Schrödinger's equation and the wavefunction, explains all of these. It's the foundation of all modern chemistry and materials science.

### The Key Ideas

**Quantum numbers.** Solving Schrödinger's equation for the hydrogen atom yields wavefunctions characterized by three **quantum numbers** (plus a fourth for spin, which we won't cover in detail):

- **n — principal quantum number**: n = 1, 2, 3, ... Determines the energy (same as Bohr). Larger n → larger average distance from the nucleus, higher energy.
- **ℓ — orbital angular momentum quantum number**: ℓ = 0, 1, 2, ..., n−1. Determines the shape of the orbital. ℓ = 0 is spherical (s-orbital), ℓ = 1 is dumbbell-shaped (p-orbital), ℓ = 2 is cloverleaf (d-orbital).
- **m_ℓ — magnetic quantum number**: m_ℓ = −ℓ, −ℓ+1, ..., 0, ..., ℓ−1, ℓ. Determines the orientation of the orbital in space.

**Electron clouds, not orbits.** The probability distributions |ψ|² for different quantum numbers give the familiar orbital shapes: spherical s-orbitals, dumbbell-shaped p-orbitals, etc. These are the regions where the electron is most likely to be found. This is completely different from Bohr's circular orbits.

**Why this matters for chemistry.** The shapes of electron orbitals determine how atoms bond. A covalent bond forms when orbitals from two atoms overlap, creating a region of high electron probability between the nuclei. The geometry of molecules (linear, bent, tetrahedral, etc.) follows from the shapes and orientations of the orbitals involved. All of chemistry emerges from the quantum mechanical description of electrons.

### Common Misconceptions

**"Electrons orbit the nucleus like planets around the Sun."** This is the Bohr model, and it's WRONG in the details. Electrons do not have well-defined trajectories. They exist in orbitals — regions of space where the probability of finding the electron is high. The "orbit" is a probability cloud. The planetary model is a useful stepping stone for learning but should be abandoned once you understand wavefunctions.

**"The quantum numbers are just labels."** They are labels, but they correspond to physical properties: n determines energy, ℓ determines angular momentum magnitude, and m_ℓ determines angular momentum orientation. These are measurable physical quantities — ℏ√(ℓ(ℓ+1)) is the actual angular momentum of the state — not just arbitrary numbers.

---

### The Double-Slit Experiment with Single Particles

The double-slit experiment is the most profound demonstration of wave-particle duality. When you fire electrons one at a time through a double slit and record where they hit a screen, individual electrons arrive as localized dots — like particles. But as thousands of electrons accumulate, the dots form an INTERFERENCE PATTERN — like waves.

This experiment forces us to abandon any hope of a simple classical picture:

1. **Each electron goes through ONE slit?** Then why does it "know" about the other slit? The interference pattern requires both slits to be open. If you close one slit, the pattern disappears.
2. **Each electron goes through BOTH slits?** But we always detect electrons as single, localized particles — never "half an electron" from each slit.
3. **If we watch which slit it goes through?** Any attempt to detect which slit the electron passes through destroys the interference pattern. The wavefunction "collapses" to a definite position when measured.

The resolution: The electron's wavefunction — its probability amplitude — goes through BOTH slits and interferes with itself. The interference pattern in the wavefunction determines where individual electrons are likely to be detected. Each electron is still detected as a single particle, but the probability distribution is shaped by wave interference.

This experiment was first performed with electrons by Claus Jönsson in 1961 and has since been repeated with neutrons, atoms, and even molecules containing over 800 atoms (buckyballs — C₆₀ molecules). All show the same behavior: individual particles producing wave-like interference patterns when accumulated.

### The Observer Effect vs. the Uncertainty Principle

Students often confuse two related but distinct concepts:

- **The uncertainty principle** (Δx·Δp ≥ ℏ/2): A fundamental limit on the simultaneous precision of position and momentum. This is intrinsic — the particle doesn't HAVE precise values for both simultaneously.
- **The observer effect**: The act of measurement unavoidably disturbs the system. To measure an electron's position (with photons, for instance), you must interact with it, changing its momentum.

The uncertainty principle is more fundamental than the observer effect. Even if you could measure without disturbing (which is impossible), the uncertainty would remain because it's a property of the quantum state itself — not a measurement artifact.

### Why Zero-Point Energy Matters

The uncertainty principle implies that even at absolute zero temperature (0 K, −273.15°C), particles cannot be at rest. If a particle had zero momentum (p = 0 exactly), then Δp = 0, which would require Δx = ∞ (infinite position uncertainty). But bound particles (like atoms in a crystal or electrons in an atom) are confined — they have finite Δx. Therefore, Δp must be non-zero. The particle must have some kinetic energy. This minimum energy is called **zero-point energy**.

For helium, zero-point energy is so large relative to the interatomic forces that helium remains liquid at atmospheric pressure even at absolute zero — it never freezes! Helium is the only substance that exhibits this behavior, and it's a direct macroscopic consequence of the uncertainty principle.

---

### Quantum Numbers and the Periodic Table

The quantum mechanical model explains the structure of the periodic table — a triumph that the Bohr model could never achieve. The four quantum numbers and the Pauli exclusion principle (no two electrons in an atom can have the same set of four quantum numbers) determine how electrons fill orbitals and why the periodic table has the structure it does.

- **n = 1:** 1s orbital, holds 2 electrons → H and He (first row)
- **n = 2:** 2s + 2p orbitals, hold 2 + 6 = 8 electrons → Li through Ne (second row)
- **n = 3:** 3s + 3p, hold 8 electrons → Na through Ar (third row, though 3d exists and fills later)
- The filling order (Aufbau principle) explains why the fourth row has 18 elements (4s fills before 3d)

The periodicity of chemical properties — why lithium, sodium, and potassium are all reactive alkali metals — arises because they all have one electron in their outermost s-orbital, regardless of the energy level. The chemical behavior is determined by the electron configuration, and the electron configuration is determined by the quantum numbers allowed by Schrödinger's equation.

This connection — from Schrödinger's equation to the periodic table to all of chemistry — is one of the greatest intellectual achievements in science.

### Spin: The Fourth Quantum Number

The electron has an intrinsic angular momentum called **spin**, described by the spin quantum number m_s = ±½. Spin is not literally the electron spinning like a top — it's a fundamentally quantum mechanical property with no classical analog. But it behaves like angular momentum and produces a magnetic moment.

The Pauli exclusion principle states that no two electrons in an atom can share the same four quantum numbers (n, ℓ, m_ℓ, m_s). Since m_s can only take two values (±½), each spatial orbital (defined by n, ℓ, m_ℓ) can hold at most two electrons, with opposite spins.

Spin is essential for understanding:
- Why each orbital holds exactly 2 electrons
- The splitting of spectral lines in magnetic fields (anomalous Zeeman effect)
- Ferromagnetism (alignment of electron spins in iron, nickel, cobalt)
- The periodic table's structure

### The Correspondence Principle

Niels Bohr proposed the **correspondence principle**: quantum mechanics must reduce to classical mechanics in the limit of large quantum numbers. For very large n (n → ∞), the spacing between energy levels becomes vanishingly small, and the quantum behavior approaches classical behavior.

For hydrogen: E_n = −13.6/n². The difference between adjacent levels: ΔE ≈ 27.2/n³ eV. As n → ∞, ΔE → 0. The energy spectrum becomes effectively continuous, and the electron behaves classically.

This principle bridges the quantum and classical worlds. It explains why we don't observe quantum behavior in everyday life — everyday objects correspond to astronomically large quantum numbers, where quantum effects are immeasurably small. The correspondence principle is not just a curiosity; it's a requirement for any quantum theory to be consistent with the classical world we observe.


## Worked Examples

### Example 1: Uncertainty Principle — Electron

An electron is known to be within a region of width 1.0 × 10⁻¹⁰ m (about the size of an atom). Estimate the minimum uncertainty in its speed.

**Approach:** Use Δx·Δp ≥ ℏ/2. Δp = m_e Δv. Solve for Δv.

**Step 1:** ℏ = h/(2π) = 1.055 × 10⁻³⁴ J·s.
Δp_min = ℏ/(2Δx) = 1.055 × 10⁻³⁴ / (2 × 1.0 × 10⁻¹⁰) = 5.27 × 10⁻²⁵ kg·m/s.

**Step 2:** Δv_min = Δp_min / m_e = 5.27 × 10⁻²⁵ / (9.11 × 10⁻³¹) = 5.79 × 10⁵ m/s.

**Why this makes sense:** If the electron is confined to an atomic-sized region (~0.1 nm), the uncertainty in its speed is about 600 km/s. This is a significant fraction of the typical electron speed in hydrogen (≈2.2 × 10⁶ m/s). The uncertainty principle is a major effect at the atomic scale.

---

### Example 2: Uncertainty Principle — Macroscopic Object

A 50.0 g golf ball has its position measured to within 1.0 μm. Estimate the minimum uncertainty in its velocity.

**Approach:** Same formula, macroscopic mass.

**Step 1:** Δp_min = 1.055 × 10⁻³⁴ / (2 × 1.0 × 10⁻⁶) = 5.27 × 10⁻²⁹ kg·m/s.

**Step 2:** Δv_min = 5.27 × 10⁻²⁹ / 0.0500 = 1.05 × 10⁻²⁷ m/s.

**Why this makes sense:** This velocity uncertainty is unimaginably small — roughly one atomic diameter per year. For any practical purpose, the uncertainty principle imposes no meaningful limit on macroscopic measurements. Quantum effects are negligible at this scale.

---

### Example 3: Energy-Time Uncertainty

An atom in an excited state has a lifetime of 1.0 × 10⁻⁸ s before emitting a photon and decaying. Estimate the minimum uncertainty in the energy of this state, and the resulting uncertainty in the wavelength of the emitted photon.

**Approach:** ΔE·Δt ≥ ℏ/2. Then Δλ from E = hc/λ.

**Step 1:** ΔE_min = ℏ/(2Δt) = 1.055 × 10⁻³⁴ / (2 × 1.0 × 10⁻⁸) = 5.27 × 10⁻²⁷ J = 3.30 × 10⁻⁸ eV.

**Step 2:** For a typical visible transition (~2 eV, λ ≈ 600 nm):
E = hc/λ → |dE/dλ| = hc/λ².
Δλ ≈ (λ²/hc) × ΔE.
For λ = 600 × 10⁻⁹ m: Δλ ≈ (3.60 × 10⁻¹³ × 5.27 × 10⁻²⁷) / (1.989 × 10⁻²⁵) ≈ 9.5 × 10⁻¹⁵ m = 9.5 × 10⁻⁶ nm.

**Why this makes sense:** The uncertainty in wavelength is extremely small (~10⁻⁵ nm), which is why spectral lines appear sharp. However, this "natural line width" is measurable with high-resolution spectroscopy and provides information about excited state lifetimes.

---

### Example 4: Position Probability from Wavefunction

For an electron in the ground state of hydrogen, the probability density at the Bohr radius (r = a₀ = 5.29 × 10⁻¹¹ m) is proportional to e⁻² = 0.135. At r = 2a₀, it is proportional to e⁻⁴ = 0.0183. By what factor is the electron more likely to be found at the Bohr radius than at twice the Bohr radius?

**Approach:** Ratio of probability densities.

**Step 1:** Ratio = |ψ(a₀)|² / |ψ(2a₀)|² = e⁻²/e⁻⁴ = e² = 7.39.

**Why this makes sense:** The electron is more than 7 times as likely (per unit volume) to be found at the Bohr radius as at twice that distance. The probability drops off exponentially with distance, but there is a non-zero probability of finding the electron at any distance — it just becomes vanishingly small far from the nucleus.

---

### Example 5: Tunneling Probability Estimate

A simplified tunneling calculation: an electron with energy 1.0 eV encounters a potential barrier of height 3.0 eV and width 0.50 nm. The tunneling probability is approximately T ≈ exp(−2κL), where κ = √(2m(V−E))/ℏ. Estimate the tunneling probability.

**Approach:** Calculate κ, then T.

**Step 1:** V − E = 2.0 eV = 3.20 × 10⁻¹⁹ J.
κ = √(2 × 9.11 × 10⁻³¹ × 3.20 × 10⁻¹⁹) / (1.055 × 10⁻³⁴)
= √(5.830 × 10⁻⁴⁹) / (1.055 × 10⁻³⁴)
= 7.636 × 10⁻²⁵ / 1.055 × 10⁻³⁴ = 7.24 × 10⁹ m⁻¹.

**Step 2:** L = 0.50 × 10⁻⁹ m.
2κL = 2 × 7.24 × 10⁹ × 0.50 × 10⁻⁹ = 7.24.
T ≈ e⁻⁷·²⁴ ≈ 7.2 × 10⁻⁴ ≈ 0.07%.

**Why this makes sense:** The tunneling probability is small but non-zero. About 1 in 1400 electrons would tunnel through this barrier. Wider or taller barriers give exponentially smaller probabilities.

---

## Practice Problems

### Problem 1
(a) An electron is confined to a region of width 0.10 nm. Using the Heisenberg uncertainty principle, estimate the minimum uncertainty in its momentum. (b) Estimate the minimum kinetic energy this electron can have. (c) Explain why this "confinement energy" prevents electrons from being localized within the nucleus.

### Problem 2
A proton is confined within a uranium nucleus of radius 7.4 × 10⁻¹⁵ m. (a) Estimate the minimum uncertainty in the proton's momentum. (b) Estimate the minimum kinetic energy in MeV. (c) Compare this with the typical binding energy per nucleon (~7 MeV). What does this tell you about protons in nuclei?

### Problem 3
An excited atomic state has an energy uncertainty of 6.6 × 10⁻⁸ eV. (a) Estimate the lifetime of this state using the energy-time uncertainty principle. (b) Is this a "long-lived" or "short-lived" excited state? (c) If the transition to the ground state emits a photon of 2.0 eV, estimate the spread in wavelengths of the emitted light (the natural line width).

### Problem 4
A student says: "The Heisenberg uncertainty principle means we can never really know anything for sure, so quantum mechanics proves that objective reality doesn't exist." Critically evaluate this claim, addressing what the uncertainty principle actually says and what it implies (and doesn't imply) about reality.

### Problem 5
In a quantum mechanical model, an electron is described by a wavefunction where the probability density is |ψ(x)|² = A² sin²(πx/L) for 0 ≤ x ≤ L and zero elsewhere. (a) Normalize this wavefunction to find A. (b) Where is the electron most likely to be found? (c) Calculate the probability of finding the electron in the left half of the region (0 ≤ x ≤ L/2).

### Problem 6 (IB Exam Style)
The Heisenberg uncertainty principle is a fundamental concept in quantum mechanics.

(a) State the Heisenberg uncertainty principle for position and momentum, giving a mathematical expression. [2 marks]

(b) An electron is confined within a one-dimensional region of length 1.0 × 10⁻¹⁰ m. (i) Use the uncertainty principle to estimate the minimum uncertainty in the electron's momentum. (ii) Hence, estimate the minimum kinetic energy of the electron. [4 marks]

(c) State and explain one consequence of the uncertainty principle for the structure of the atom. [2 marks]

(d) Describe what is meant by the "wavefunction" of a particle and explain how it relates to the probability of finding the particle at a given position. [3 marks]

(e) Explain why the Bohr model, while successful for hydrogen, was replaced by the quantum mechanical model. [1 mark]

---

## Answers

### Answer 1
(a) Δp_min = ℏ/(2Δx) = 1.055 × 10⁻³⁴ / (2 × 0.10 × 10⁻⁹) = 1.055 × 10⁻³⁴ / (2.0 × 10⁻¹¹) = 5.27 × 10⁻²⁴ kg·m/s.

(b) KE_min ≈ (Δp)²/(2m_e) = (5.27 × 10⁻²⁴)² / (2 × 9.11 × 10⁻³¹) = 2.78 × 10⁻⁴⁷ / (1.822 × 10⁻³⁰) = 1.53 × 10⁻¹⁷ J ≈ 95 eV.

(c) If an electron were confined to a nuclear-sized region (~10⁻¹⁴ m), the kinetic energy would be enormous — roughly 10 GeV (from the calculation in the main text). This energy is far greater than the binding energy from the nucleus, so the electron would immediately escape. The uncertainty principle thus explains why electrons CANNOT be part of the nucleus and why atoms have radii of ~10⁻¹⁰ m — this is the optimal balance between confinement energy (favoring large size) and electrostatic attraction (favoring small size).

### Answer 2
(a) Δp_min = ℏ/(2Δx) = 1.055 × 10⁻³⁴ / (2 × 7.4 × 10⁻¹⁵) = 7.13 × 10⁻²¹ kg·m/s.

(b) m_p = 1.673 × 10⁻²⁷ kg.
KE_min = (7.13 × 10⁻²¹)² / (2 × 1.673 × 10⁻²⁷) = 5.08 × 10⁻⁴¹ / (3.346 × 10⁻²⁷) = 1.52 × 10⁻¹⁴ J.
In MeV: 1.52 × 10⁻¹⁴ / (1.60 × 10⁻¹³) = 0.095 MeV. (1 MeV = 10⁶ eV = 1.60 × 10⁻¹³ J.)

Wait, let me recalculate more carefully:
1.52 × 10⁻¹⁴ J / 1.60 × 10⁻¹³ J/MeV = 0.095 MeV.

Hmm, that seems low. Let me double-check:
Δp = 1.055 × 10⁻³⁴ / (1.48 × 10⁻¹⁴) = 7.13 × 10⁻²¹.
(Δp)² = 5.08 × 10⁻⁴¹.
2m = 3.346 × 10⁻²⁷.
KE = 5.08 × 10⁻⁴¹ / 3.346 × 10⁻²⁷ = 1.52 × 10⁻¹⁴ J.
1 eV = 1.60 × 10⁻¹⁹ J, so 1 MeV = 1.60 × 10⁻¹³ J.
KE = 1.52 × 10⁻¹⁴ / 1.60 × 10⁻¹³ = 0.095 MeV ≈ 0.1 MeV.

(c) The confinement energy (~0.1 MeV) is much LESS than typical nuclear binding energy (~7 MeV). This tells us that protons CAN be confined within nuclei — unlike electrons, for which confinement to nuclear dimensions would require ~10 GeV. This is consistent with protons being nuclear constituents. The strong nuclear force provides more than enough binding to overcome the zero-point kinetic energy from the uncertainty principle.

### Answer 3
(a) Δt ≥ ℏ/(2ΔE) = 1.055 × 10⁻³⁴ / (2 × 6.6 × 10⁻⁸ × 1.60 × 10⁻¹⁹) = 1.055 × 10⁻³⁴ / (2.112 × 10⁻²⁶) = 5.0 × 10⁻⁹ s.

(b) 5 ns is a relatively short lifetime for atomic excited states. Typical allowed transitions have lifetimes of 1-100 ns. Forbidden transitions can be much longer (ms to seconds). This state would produce a measurable natural line width.

(c) E = 2.0 eV, λ = hc/E = 1.989 × 10⁻²⁵ / (3.20 × 10⁻¹⁹) = 6.22 × 10⁻⁷ m = 622 nm.
Δλ ≈ (λ²/hc) × ΔE = λ × (ΔE/E) = 622 nm × (6.6 × 10⁻⁸ / 2.0) = 622 × 3.3 × 10⁻⁸ = 2.1 × 10⁻⁵ nm.
This is a very narrow line — about 0.00002 nm spread in wavelength. This is measurable with high-resolution spectroscopy (like Fabry-Perot interferometry).

### Answer 4
The student's claim is an overinterpretation and a misunderstanding of the uncertainty principle. Here's why:

The uncertainty principle places mathematical limits on the simultaneous precision of certain pairs of properties (position/momentum, energy/time). It does NOT say "we can never know anything for sure." It says: if we know position precisely, momentum is fundamentally uncertain, and vice versa. This is a quantitative relationship, not a statement of complete ignorance.

Furthermore, the uncertainty principle does NOT imply that objective reality doesn't exist. It implies that the classical description of reality (particles with definite positions and momenta at all times) is incomplete at the quantum scale. In quantum mechanics, the wavefunction ψ provides a complete and objective description of the system — it just describes probabilities rather than certainties. The evolution of the wavefunction via Schrödinger's equation is perfectly deterministic. Only the outcome of a specific measurement is probabilistic.

So quantum mechanics doesn't say "nothing is real." It says "reality at the quantum scale is described by probability amplitudes, not by trajectories through space." This is a different KIND of reality, not an absence of reality. There are different philosophical interpretations (Copenhagen, many-worlds, etc.) but none of them claim that "objective reality doesn't exist."

### Answer 5
(a) Normalization: ∫₀^L A² sin²(πx/L) dx = 1.
sin²(θ) = (1 − cos(2θ))/2.
∫₀^L sin²(πx/L) dx = ∫₀^L (1 − cos(2πx/L))/2 dx = [x/2 − (L/(4π))sin(2πx/L)]₀^L = L/2.
So A² × L/2 = 1 → A = √(2/L).

(b) The probability density is A² sin²(πx/L). sin² is maximum when sin(πx/L) = ±1, which occurs when πx/L = π/2, i.e., x = L/2. The electron is most likely to be found at the center of the region.

(c) P = ∫₀^(L/2) A² sin²(πx/L) dx.
∫₀^(L/2) sin²(πx/L) dx = [x/2 − (L/(4π))sin(2πx/L)]₀^(L/2)
= (L/4 − 0) − (0 − 0) = L/4.
P = (2/L) × (L/4) = 0.50 = 50%.

This makes sense: the probability distribution is symmetric about x = L/2, so the probability of being in the left half equals the probability of being in the right half = 50%.

### Answer 6
(a) The Heisenberg uncertainty principle states that the product of the uncertainties in position (Δx) and momentum (Δp) cannot be less than ℏ/2: Δx·Δp ≥ ℏ/2, where ℏ = h/(2π). This is a fundamental limit, not a limitation of measurement technology.

(b) (i) Δp_min = ℏ/(2Δx) = 1.055 × 10⁻³⁴ / (2 × 1.0 × 10⁻¹⁰) = 5.27 × 10⁻²⁵ kg·m/s.
(ii) KE_min ≈ (Δp)²/(2m_e) = (5.27 × 10⁻²⁵)² / (2 × 9.11 × 10⁻³¹)
= 2.78 × 10⁻⁴⁹ / (1.822 × 10⁻³⁰) = 1.53 × 10⁻¹⁹ J = 0.954 eV.

(c) The uncertainty principle explains why electrons do not spiral into the nucleus. If an electron were confined to the tiny nuclear volume (~10⁻¹⁵ m), the uncertainty principle would require it to have enormous momentum (and thus kinetic energy, ~10 GeV), far exceeding the electrostatic binding energy. The electron would immediately escape. Instead, the electron settles at a distance (~10⁻¹⁰ m) where the confinement energy from the uncertainty principle balances the electrostatic attraction. This determines the size of the atom. Additionally, the uncertainty principle is the root cause of the zero-point energy — even at absolute zero temperature, quantum particles have non-zero kinetic energy because they cannot be perfectly at rest (zero momentum would require infinite position uncertainty, which is impossible for a bound electron).

(d) The wavefunction ψ(x, t) is a complex-valued mathematical function that contains all information about a quantum particle. The wavefunction itself is not directly observable. According to Born's interpretation, the square of the absolute value of the wavefunction, |ψ(x, t)|², gives the probability density of finding the particle at position x at time t. Specifically, the probability of finding the particle in a small interval dx around x is P(x) dx = |ψ(x, t)|² dx. The wavefunction must be normalized so that the total probability of finding the particle somewhere is 1: ∫|ψ|² dx = 1.

(e) The Bohr model successfully predicted hydrogen's energy levels but failed for multi-electron atoms, could not explain spectral line intensities, and provided no explanation for why stationary states don't radiate. The quantum mechanical model (based on Schrödinger's equation and wavefunctions) provides a consistent description of all atoms, explains chemical bonding, predicts orbital shapes, and naturally accounts for quantization through boundary conditions on the wavefunction. The Bohr model was a crucial stepping stone but was replaced because it was an ad-hoc mixture of classical and quantum ideas rather than a consistent theory.

---

## Key Takeaways

1. The Heisenberg uncertainty principle (Δx·Δp ≥ ℏ/2) states that position and momentum cannot both be precisely known simultaneously. This is a fundamental property of nature, not a measurement limitation.

2. The energy-time uncertainty (ΔE·Δt ≥ ℏ/2) explains the finite lifetime of excited states and the natural line width of spectral emissions.

3. A particle is described by a wavefunction ψ(x, t). The probability density of finding the particle at position x is |ψ|² (Born's interpretation).

4. Electrons in atoms do not follow orbits — they exist as probability clouds (orbitals) characterized by quantum numbers n, ℓ, m_ℓ.

5. The uncertainty principle explains why electrons don't collapse into the nucleus and why atoms have the size they do.

6. Quantum tunneling occurs when a particle's wavefunction extends through a potential barrier, allowing the particle to appear on the far side even when classically it lacks the energy to cross.
