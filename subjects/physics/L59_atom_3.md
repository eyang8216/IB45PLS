# Lesson 59: Atom 3 — Wave-Particle Duality, de Broglie, and Electron Diffraction

## What You'll Learn

By the 1920s, physics had a crisis: light sometimes behaved like a wave (interference, diffraction) and sometimes like a particle (photoelectric effect). Einstein had shown that light comes in quantized packets of energy — photons. But if light, which everyone "knew" was a wave, could also behave as a particle, could the reverse be true? Could electrons, which everyone "knew" were particles, also behave as waves?

The answer was yes — and it changed everything. Louis de Broglie proposed that ALL matter has wave-like properties. This idea was so strange that even Einstein was initially skeptical. But within a few years, experiments proved de Broglie right: electrons really do diffract, just like light waves. This discovery was the key that unlocked quantum mechanics.

In this lesson, you'll learn about wave-particle duality — the idea that every object in the universe has both particle-like and wave-like properties — and how this concept explains the "why" behind Bohr's quantized orbits.

---

## 1. The Double Personality of Light

### Why This Matters

Before you can understand why electrons have wavelengths, you need to appreciate the evidence that light has a dual nature. The fact that light is both wave and particle is no longer controversial — it's the foundation of modern physics. But in 1905-1923, it was deeply unsettling.

### The Key Ideas

**Light as a wave: the evidence.** For over a century, the evidence for light's wave nature had been overwhelming:

1. **Diffraction:** Light bends around corners and spreads out after passing through narrow slits. A diffraction grating produces a pattern of bright and dark fringes — the bright spots are where waves arrive in phase and constructively interfere; dark spots are where they arrive out of phase and destructively interfere. Particles cannot produce interference patterns.

2. **Interference:** Thomas Young's double-slit experiment (1801) showed two overlapping beams of light producing alternating bright and dark bands. This is a definitive wave signature.

3. **Maxwell's equations (1865):** James Clerk Maxwell showed that light is an electromagnetic wave — oscillating electric and magnetic fields propagating through space at speed c = 1/√(ε₀μ₀).

**Light as a particle: the evidence.** Then came Einstein:

1. **The photoelectric effect:** When light shines on a metal surface, electrons are emitted. But below a certain threshold frequency, NO electrons are emitted — no matter how intense the light. Above the threshold, electrons are emitted instantly with kinetic energy proportional to the frequency. Classical wave theory predicts that any frequency should eventually release electrons if the intensity is high enough (build up energy over time). It doesn't happen. (We'll study this in detail in Lessons 60-61.)

2. **Einstein's explanation (1905):** Light energy comes in quantized packets called **photons**. Each photon has energy E = hf, where h = 6.63 × 10⁻³⁴ J·s is Planck's constant and f is the frequency. A photon is the smallest possible packet of light at that frequency — you cannot have "half a photon."

**The uncomfortable truth.** Light is not a wave OR a particle. It is something more fundamental that exhibits wave-like behavior in some experiments and particle-like behavior in others. We have no everyday analogy for this. The best we can say is: light propagates like a wave but exchanges energy like a particle.

### Common Misconceptions

**"Light is sometimes a wave and sometimes a particle."** This phrasing suggests light switches between two identities. A better statement: light has both wave and particle properties simultaneously. Which aspect we observe depends on the experiment we perform. In interference, we probe the wave aspect. In the photoelectric effect, we probe the particle aspect.

**"Photons are tiny billiard balls of light."** No. A photon is not a tiny localized object whizzing through space. It's a quantum of the electromagnetic field. It doesn't have a well-defined position or trajectory. Photons are detected as localized energy deposits (like a "click" on a detector), but between emission and absorption, they are described by a wave function.

---

## 2. De Broglie's Bold Hypothesis (1924)

### Why This Matters

Louis de Broglie, a French prince-turned-physicist, made one of the most audacious proposals in the history of science: if waves can behave as particles (photons), then particles should behave as waves. This idea was the key that finally explained why Bohr's orbits are quantized — and it pointed the way to Schrödinger's wave mechanics.

### The Key Ideas

**The symmetry argument.** De Broglie's reasoning was elegant in its simplicity. For light:

- E = hf (photon energy from wave frequency)
- p = h/λ (photon momentum from wavelength, derived from E = pc for massless particles)

Since photons (traditionally "waves") have momentum (traditionally a particle property), perhaps electrons (traditionally "particles") have a wavelength (traditionally a wave property).

**The de Broglie wavelength.** Every particle with momentum p has an associated wavelength:

$$\lambda = \frac{h}{p}$$

where h = 6.63 × 10⁻³⁴ J·s. This is called the **de Broglie wavelength**.

For a particle with mass m moving at speed v:

$$\lambda = \frac{h}{mv}$$

**Order of magnitude.** Let's see how big de Broglie wavelengths are:

- **Electron** with kinetic energy 100 eV: v = √(2K/m_e) = √(2 × 100 × 1.60 × 10⁻¹⁹ / 9.11 × 10⁻³¹) ≈ 5.93 × 10⁶ m/s. λ = h/(m_e v) = 6.63 × 10⁻³⁴ / (9.11 × 10⁻³¹ × 5.93 × 10⁶) ≈ 1.23 × 10⁻¹⁰ m = 0.123 nm. This is comparable to atomic spacing in crystals (typically 0.1-0.5 nm) — which means electrons should diffract from crystals!

- **Baseball** (0.15 kg, 40 m/s): λ = 6.63 × 10⁻³⁴ / (0.15 × 40) ≈ 1.1 × 10⁻³⁴ m. This is 10²⁴ times smaller than a nucleus. No conceivable experiment could detect this wavelength. The wave nature of macroscopic objects exists in principle but is completely unobservable in practice.

- **You** walking (70 kg, 1 m/s): λ ≈ 10⁻³⁵ m. Wave nature is negligible.

**Why we don't see everyday objects diffracting.** The de Broglie wavelength is inversely proportional to momentum. Macroscopic objects have enormous momentum compared to h, so their wavelengths are impossibly small. Only particles with very small mass (electrons, neutrons, atoms) have measurable de Broglie wavelengths. This is why quantum effects are only apparent at the atomic scale.

### Common Misconceptions

**"Everything is a wave."** This is an oversimplification. Everything has a de Broglie wavelength, but for macroscopic objects, the wavelength is so small that wave effects are undetectable. In practice, we can treat baseballs and people as purely classical particles. Wave-particle duality is ALWAYS present but only OBSERVABLE for particles with wavelengths comparable to the relevant length scales.

**"De Broglie waves are physical vibrations."** No. A de Broglie wave is not a physical vibration of a medium. It's a **probability amplitude** — a mathematical wave that, when squared, gives the probability of finding the particle at a given location. This interpretation was developed by Max Born and is central to quantum mechanics (see Lesson 62).

---

## 3. Electron Diffraction: Proof That Matter Waves Exist

### Why This Matters

A scientific hypothesis is only as good as its experimental tests. De Broglie's idea was beautiful, but physics requires evidence. Two experiments — one accidental, one deliberate — proved that electrons really do diffract, confirming the wave nature of matter.

### The Key Ideas

**Davisson and Germer (1927).** Clinton Davisson and Lester Germer at Bell Labs were studying how electrons scatter from a nickel crystal. Their apparatus accidentally broke, exposing the nickel to air and oxidizing it. To clean the crystal, they heated it to high temperature, which caused the nickel to recrystallize into large, uniform crystals. When they resumed their experiment, the electron scattering pattern changed dramatically — the electrons were now emerging at specific angles, forming a pattern of peaks and valleys.

They had accidentally created a diffraction grating for electrons. The regularly spaced atoms in the nickel crystal were acting like a diffraction grating for the electron waves, producing interference maxima at angles that satisfied the Bragg condition (the same equation used for X-ray diffraction):

$$n\lambda = 2d\sin\theta$$

where d is the atomic spacing and θ is the scattering angle.

Using the known spacing of nickel atoms and the measured scattering angles, they calculated the electron wavelength. It matched de Broglie's prediction λ = h/p perfectly. Electrons really do diffract. They really do have wavelengths.

**G.P. Thomson (1927).** George Paget Thomson (J.J. Thomson's son!) independently confirmed electron diffraction by passing electrons through thin metal films and observing diffraction rings on a photographic plate. The irony is beautiful: J.J. Thomson won the Nobel Prize for proving electrons are particles; his son G.P. Thomson won the Nobel Prize for proving electrons are waves. Both were right.

**The modern version.** In many physics labs, students perform electron diffraction using a tube where electrons are accelerated through a known voltage, then pass through a thin graphite film. The resulting diffraction pattern — concentric rings on a fluorescent screen — provides a direct visual confirmation of matter waves.

**Calculating the wavelength from accelerating voltage.** In an electron diffraction tube, electrons are accelerated through a potential difference V. Their kinetic energy is:

$$K = eV$$

Their momentum is:

$$p = \sqrt{2m_e K} = \sqrt{2m_e eV}$$

And their de Broglie wavelength is:

$$\lambda = \frac{h}{\sqrt{2m_e eV}}$$

For V = 4000 V: λ = h/√(2 × 9.11 × 10⁻³¹ × 1.60 × 10⁻¹⁹ × 4000) ≈ 1.94 × 10⁻¹¹ m = 0.0194 nm. This is comparable to interatomic spacing, making crystal diffraction possible.

---

## 4. De Broglie Explains Bohr's Quantization

### Why This Matters

Bohr's model worked, but nobody knew WHY angular momentum was quantized. Bohr just declared it as a postulate. De Broglie's idea provided the physical reason: electron orbits are quantized because an integer number of electron wavelengths must fit around the orbit circumference. Standing waves, in other words.

### The Key Ideas

**The standing wave analogy.** Imagine a vibrating string fixed at both ends. Only certain wavelengths "fit" — the string can only support standing waves where the length L equals an integer number of half-wavelengths: L = n λ/2. Other wavelengths produce destructive interference and quickly die out.

De Broglie applied the same idea to the electron orbit. For a circular orbit of radius r:

$$2\pi r = n\lambda = n\frac{h}{p} = n\frac{h}{mv}$$

where n = 1, 2, 3, ...

Rearrange: $$mvr = n\frac{h}{2\pi} = n\hbar$$

This is exactly Bohr's quantization condition! The electron's orbit circumference must contain an integer number of de Broglie wavelengths. If it doesn't, the electron wave would destructively interfere with itself and the orbit would not be stable.

**The physical picture.** The electron is not a tiny ball whizzing around the nucleus. It's a standing wave wrapped around the nucleus. The allowed orbits correspond to the resonant modes of this wave — the states where the wave constructively interferes with itself after one complete circuit. The ground state (n = 1) has one wavelength fitted around the circumference. The first excited state (n = 2) has two wavelengths, and so on.

**Why this is profound.** Bohr's postulate — which seemed like an arbitrary rule — emerges naturally from the wave nature of the electron. Quantization is not a mysterious decree; it's the consequence of fitting standing waves into a confined space. In Lesson 62, you'll see how Schrödinger generalized this idea into a complete wave equation for matter.

### Common Misconceptions

**"The electron IS a standing wave."** The electron is a particle that is described by a wave function. The standing wave is the wave FUNCTION, not the electron itself. This is a subtle but crucial distinction. The wave function determines the probability of finding the electron at each point.

**"The orbit is a physical circle."** In the full quantum mechanical picture (Lesson 62), the electron does not follow a well-defined orbit. The circular orbit is a simplification from the Bohr model. The standing-wave picture is a bridge between the Bohr model and full quantum mechanics — it explains WHY Bohr's rule works, but the true picture is more complex.

---

## 5. Applications and Extensions

### Why This Matters

Wave-particle duality is not just a philosophical curiosity — it's the working principle behind some of the most important scientific instruments ever built.

### The Key Ideas

**The electron microscope.** Optical microscopes are limited by the wavelength of visible light (λ ≈ 400-700 nm). The smallest resolvable detail is about half the wavelength, so optical microscopes cannot resolve objects smaller than about 200 nm. But electrons accelerated through 100 kV have a de Broglie wavelength of about 0.0037 nm — 100,000 times smaller than visible light. This allows electron microscopes to resolve individual atoms.

**Neutron diffraction.** Neutrons also have de Broglie wavelengths. "Thermal" neutrons (those in thermal equilibrium with room-temperature matter) have λ ≈ 0.1 nm — ideal for crystal structure determination. Unlike X-rays, neutrons are scattered by atomic nuclei, not electrons. This makes neutron diffraction especially useful for locating light atoms (like hydrogen) in crystal structures, and for studying magnetic structures.

**Scanning tunneling microscope (STM).** The STM (covered in detail in Lesson 63) uses quantum tunneling — a direct consequence of the wave nature of electrons. When a sharp metal tip is brought extremely close to a conducting surface, electrons can "tunnel" across the gap even though classical physics says they lack the energy to cross. The tunneling current depends exponentially on the gap distance, allowing the STM to map surfaces with atomic resolution.

**The double-slit experiment with electrons.** If you fire electrons one at a time through a double slit and record where they hit a screen, you get... an interference pattern. Even though only ONE electron goes through at a time, and it presumably goes through one slit or the other, the accumulated pattern of many electrons shows interference fringes. Each electron somehow "interferes with itself." This experiment is one of the most profound demonstrations of quantum mechanics and will be discussed further in Lesson 62.

---

## Worked Examples

### Example 1: De Broglie Wavelength of an Electron

Calculate the de Broglie wavelength of an electron moving at 2.50 × 10⁶ m/s.

**Approach:** Use λ = h/(mv).

**Step 1:** λ = 6.63 × 10⁻³⁴ / (9.11 × 10⁻³¹ × 2.50 × 10⁶)
= 6.63 × 10⁻³⁴ / (2.278 × 10⁻²⁴)
= 2.91 × 10⁻¹⁰ m = 0.291 nm.

**Why this makes sense:** This is about 0.3 nm, which is on the order of atomic spacing in crystals. Electrons at this speed (typical of those in an electron microscope) can be diffracted by crystals.

---

### Example 2: De Broglie Wavelength from Accelerating Voltage

Electrons are accelerated from rest through a potential difference of 2500 V. Calculate their de Broglie wavelength.

**Approach:** Kinetic energy K = eV. Then momentum from K = p²/2m. Then λ = h/p.

**Step 1:** K = 1.60 × 10⁻¹⁹ × 2500 = 4.00 × 10⁻¹⁶ J.

**Step 2:** p = √(2m_eK) = √(2 × 9.11 × 10⁻³¹ × 4.00 × 10⁻¹⁶)
= √(7.288 × 10⁻⁴⁶) = 2.70 × 10⁻²³ kg·m/s.

**Step 3:** λ = 6.63 × 10⁻³⁴ / (2.70 × 10⁻²³) = 2.46 × 10⁻¹¹ m = 0.0246 nm.

**Why this makes sense:** This wavelength is in the X-ray range and is ideal for crystal diffraction. Electron diffraction tubes typically operate at a few thousand volts.

---

### Example 3: Wavelength of a Moving Object

Calculate the de Broglie wavelength of: (a) a proton moving at 5.00 × 10⁵ m/s, (b) a 50.0 g golf ball traveling at 30.0 m/s.

**Approach:** λ = h/(mv). Use m_proton = 1.67 × 10⁻²⁷ kg.

**(a) Proton:**
λ = 6.63 × 10⁻³⁴ / (1.67 × 10⁻²⁷ × 5.00 × 10⁵)
= 6.63 × 10⁻³⁴ / (8.35 × 10⁻²²)
= 7.94 × 10⁻¹³ m = 0.000794 nm.

This is about the size of a nucleus. Neutrons at thermal speeds have similar wavelengths, which is why neutron diffraction works.

**(b) Golf ball:**
λ = 6.63 × 10⁻³⁴ / (0.0500 × 30.0)
= 6.63 × 10⁻³⁴ / 1.50
= 4.42 × 10⁻³⁴ m.

**Why this makes sense:** The golf ball's wavelength is unimaginably small — about 10³⁴ times smaller than a proton. No experiment could ever detect wave-like behavior from a golf ball. This is why we don't see quantum effects in everyday life.

---

### Example 4: Electron Diffraction Pattern

In an electron diffraction experiment, electrons accelerated through 4000 V produce a first-order diffraction ring at an angle of 2.50° from a crystal with atomic spacing d = 0.215 nm. Verify that this is consistent with the de Broglie relationship.

**Approach:** Use Bragg's law nλ = 2d sinθ to find λ from the experiment. Then compare with λ = h/√(2meV) from de Broglie.

**Step 1:** Experimental λ from Bragg's law (n = 1):
λ = 2d sinθ = 2 × 2.15 × 10⁻¹⁰ × sin(2.50°)
= 4.30 × 10⁻¹⁰ × 0.04362 = 1.876 × 10⁻¹¹ m = 0.01876 nm.

**Step 2:** De Broglie prediction:
K = eV = 1.60 × 10⁻¹⁹ × 4000 = 6.40 × 10⁻¹⁶ J.
p = √(2 × 9.11 × 10⁻³¹ × 6.40 × 10⁻¹⁶) = √(1.166 × 10⁻⁴⁵) = 3.415 × 10⁻²³ kg·m/s.
λ = 6.63 × 10⁻³⁴ / (3.415 × 10⁻²³) = 1.941 × 10⁻¹¹ m = 0.01941 nm.

**Step 3:** Comparison: 0.01876 nm vs 0.01941 nm. The difference is about 3%, which is within experimental uncertainty (the crystal spacing might not be exactly 0.215 nm, and the angle measurement has uncertainty).

**Why this makes sense:** The agreement confirms de Broglie's hypothesis. Electron diffraction is a real phenomenon that follows the same mathematics as X-ray diffraction.

---

### Example 5: Bohr Quantization via De Broglie

Use the de Broglie standing-wave condition to derive the radius of the n = 2 orbit in hydrogen.

**Approach:** For a circular orbit, the circumference must equal nλ. Use the Coulomb force to relate v and r. Solve for r.

**Step 1:** Standing-wave condition: 2πr = nλ = nh/(m_e v). So m_e v r = nℏ.

**Step 2:** Centripetal force = Coulomb force: m_e v²/r = (1/4πε₀) × e²/r².

**Step 3:** From step 1, v = nℏ/(m_e r). Substitute into step 2:
m_e (n²ℏ²)/(m_e² r²) × (1/r) = (1/4πε₀) × e²/r²
n²ℏ²/(m_e r³) = (1/4πε₀) × e²/r²
n²ℏ²/(m_e r) = (1/4πε₀) × e²
r = (4πε₀ n²ℏ²) / (m_e e²) = n² × (4πε₀ ℏ²)/(m_e e²)

**Step 4:** The Bohr radius is a₀ = (4πε₀ ℏ²)/(m_e e²) = 5.29 × 10⁻¹¹ m.
For n = 2: r = 4 × 5.29 × 10⁻¹¹ = 2.12 × 10⁻¹⁰ m.

**Why this makes sense:** This matches the n² r_B result from the Bohr model. De Broglie's hypothesis reproduces Bohr's quantization condition from a physical argument about standing waves, rather than an arbitrary postulate.

---

## Practice Problems

### Problem 1
Calculate the de Broglie wavelength of: (a) an electron with kinetic energy 50.0 eV, (b) a neutron with kinetic energy 0.025 eV (typical thermal neutron), (c) an alpha particle with kinetic energy 5.00 MeV. Use m_n = 1.675 × 10⁻²⁷ kg, m_α = 6.64 × 10⁻²⁷ kg.

### Problem 2
In an electron diffraction experiment, electrons are accelerated through a potential difference of 3500 V before striking a thin graphite film. (a) Calculate the de Broglie wavelength of these electrons. (b) The graphite film has a dominant atomic spacing of 0.123 nm. At what angle would the first-order diffraction ring appear? (c) Explain why higher accelerating voltages would produce smaller diffraction rings.

### Problem 3
A student says: "The de Broglie wavelength of a moving car is so small that quantum effects are negligible. Therefore, cars are purely classical objects and do not obey quantum mechanics." Critically evaluate this statement.

### Problem 4
In the Bohr model of hydrogen, the electron in the ground state (n = 1) has a speed of 2.19 × 10⁶ m/s. (a) Calculate the de Broglie wavelength of this electron. (b) Calculate the circumference of the n = 1 orbit (radius = 5.29 × 10⁻¹¹ m). (c) Show that the circumference equals exactly one de Broglie wavelength. (d) Explain the physical significance of this result.

### Problem 5
An electron and a proton are both accelerated through the same potential difference of 100 V from rest. (a) Calculate the de Broglie wavelength of each. (b) Explain why the electron's wavelength is larger. (c) Which would be more suitable for probing the structure of a crystal with atomic spacing 0.25 nm? Justify your answer.

### Problem 6 (IB Exam Style)
In 1927, Davisson and Germer demonstrated the wave nature of electrons by observing diffraction from a nickel crystal.

(a) State the de Broglie hypothesis. [1 mark]

(b) Explain why the wave nature of electrons is not observed in everyday situations. [2 marks]

(c) In their experiment, electrons were accelerated through a potential difference V. Show that the de Broglie wavelength λ is given by:
$$\lambda = \frac{h}{\sqrt{2m_e e V}}$$
[2 marks]

(d) For V = 54.0 V, the electrons were found to produce a strong diffraction peak at a scattering angle of 50.0°. The atomic spacing in nickel is 0.215 nm. Using the Bragg equation nλ = 2d sinθ, calculate: (i) the wavelength that would produce a first-order (n = 1) peak at this angle, (ii) the de Broglie wavelength for 54.0 V electrons. (iii) Comment on whether the results confirm de Broglie's hypothesis. [5 marks]

(e) Outline how G.P. Thomson's experiment provided additional independent evidence for electron diffraction. [2 marks]

---

## Answers

### Answer 1
(a) K = 50.0 eV = 8.00 × 10⁻¹⁸ J.
p = √(2 × 9.11 × 10⁻³¹ × 8.00 × 10⁻¹⁸) = √(1.4576 × 10⁻⁴⁷) = 3.818 × 10⁻²⁴ kg·m/s.
λ = 6.63 × 10⁻³⁴ / (3.818 × 10⁻²⁴) = 1.737 × 10⁻¹⁰ m = 0.174 nm.

(b) K = 0.025 eV = 4.00 × 10⁻²¹ J.
p = √(2 × 1.675 × 10⁻²⁷ × 4.00 × 10⁻²¹) = √(1.34 × 10⁻⁴⁷) = 3.66 × 10⁻²⁴ kg·m/s.
λ = 6.63 × 10⁻³⁴ / (3.66 × 10⁻²⁴) = 1.81 × 10⁻¹⁰ m = 0.181 nm.

(c) K = 5.00 MeV = 8.00 × 10⁻¹³ J.
p = √(2 × 6.64 × 10⁻²⁷ × 8.00 × 10⁻¹³) = √(1.062 × 10⁻³⁸) = 1.031 × 10⁻¹⁹ kg·m/s.
λ = 6.63 × 10⁻³⁴ / (1.031 × 10⁻¹⁹) = 6.43 × 10⁻¹⁵ m = 6.43 × 10⁻⁶ nm.

The alpha particle's wavelength is in the femtometer range — comparable to nuclear dimensions. This is why alpha particles were used to probe the nucleus in Rutherford's experiment; their short wavelength gives them good spatial resolution.

### Answer 2
(a) λ = h/√(2m_e eV) = 6.63 × 10⁻³⁴ / √(2 × 9.11 × 10⁻³¹ × 1.60 × 10⁻¹⁹ × 3500)
= 6.63 × 10⁻³⁴ / √(1.020 × 10⁻⁴⁵)
= 6.63 × 10⁻³⁴ / 3.194 × 10⁻²³ = 2.08 × 10⁻¹¹ m = 0.0208 nm.

(b) Bragg: λ = 2d sinθ → sinθ = λ/(2d) = 2.08 × 10⁻¹¹ / (2 × 1.23 × 10⁻¹⁰) = 2.08 × 10⁻¹¹ / 2.46 × 10⁻¹⁰ = 0.0846.
θ = sin⁻¹(0.0846) = 4.85°.

(c) Higher voltage → higher electron kinetic energy → higher momentum → shorter de Broglie wavelength. From Bragg's law, shorter λ gives smaller sinθ, hence smaller θ. The diffraction rings shrink. Physically: the electron waves have shorter wavelength, so they diffract less.

### Answer 3
The student is partially correct but conceptually wrong. The de Broglie wavelength of a car (say 1000 kg moving at 20 m/s) is λ ≈ 3 × 10⁻³⁸ m. This is indeed too small for any conceivable experiment to detect wave behavior. In practice, we treat the car as a classical object because quantum effects are negligible. However, the car STILL obeys quantum mechanics in principle — quantum mechanics reduces to classical mechanics when de Broglie wavelengths are much smaller than all relevant length scales. This is called the **correspondence principle**. The car is not "purely classical"; it's a quantum object whose wave nature is simply too subtle to detect. The classical description is an excellent approximation, not a fundamental truth.

### Answer 4
(a) λ = h/(m_e v) = 6.63 × 10⁻³⁴ / (9.11 × 10⁻³¹ × 2.19 × 10⁶)
= 6.63 × 10⁻³⁴ / (1.995 × 10⁻²⁴) = 3.32 × 10⁻¹⁰ m = 0.332 nm.

(b) Circumference = 2πr = 2π × 5.29 × 10⁻¹¹ = 3.32 × 10⁻¹⁰ m = 0.332 nm.

(c) The circumference (0.332 nm) equals exactly one de Broglie wavelength (0.332 nm). n = 1.

(d) This means the ground state orbit in hydrogen corresponds to a standing electron wave with exactly one wavelength wrapped around the circumference. The electron wave constructively interferes with itself after one circuit. Orbits with non-integer numbers of wavelengths would destructively interfere, making them unstable. This provides a physical explanation for Bohr's quantization condition: only orbits where nλ = 2πr are allowed.

### Answer 5
(a) K_same = eV = 1.60 × 10⁻¹⁹ × 100 = 1.60 × 10⁻¹⁷ J.

Electron: p = √(2 × 9.11 × 10⁻³¹ × 1.60 × 10⁻¹⁷) = √(2.915 × 10⁻⁴⁷) = 5.40 × 10⁻²⁴ kg·m/s.
λ_e = 6.63 × 10⁻³⁴ / (5.40 × 10⁻²⁴) = 1.23 × 10⁻¹⁰ m = 0.123 nm.

Proton: p = √(2 × 1.67 × 10⁻²⁷ × 1.60 × 10⁻¹⁷) = √(5.344 × 10⁻⁴⁴) = 2.31 × 10⁻²² kg·m/s.
λ_p = 6.63 × 10⁻³⁴ / (2.31 × 10⁻²²) = 2.87 × 10⁻¹² m = 0.00287 nm.

(b) Same kinetic energy means the heavier proton has more momentum (p = √(2mK)). Since λ ∝ 1/p, the lighter electron has a larger de Broglie wavelength.

(c) The electron (λ = 0.123 nm) is more suitable. Its wavelength is comparable to the atomic spacing (0.25 nm), so it will produce clear diffraction patterns. The proton's wavelength (0.00287 nm) is about 100 times smaller than the spacing, so diffraction angles would be extremely small and hard to measure. For effective crystal diffraction, the wavelength should be similar to the spacing being probed.

### Answer 6
(a) The de Broglie hypothesis states that all particles with momentum p have an associated wavelength λ = h/p, where h is Planck's constant. This endows matter with wave-like properties.

(b) The de Broglie wavelength λ = h/(mv) is inversely proportional to mass. For macroscopic objects (large m), the wavelength is many orders of magnitude smaller than any physical dimension we can measure. For example, a 1 kg object moving at 1 m/s has λ ≈ 10⁻³⁴ m, which is completely undetectable. Wave effects like diffraction and interference are only observable when the wavelength is comparable to the size of apertures or obstacles.

(c) K = eV. For non-relativistic electrons, K = p²/(2m_e), so p² = 2m_e eV.
p = √(2m_e eV).
λ = h/p = h/√(2m_e eV). This is the required result.

(d) (i) Using Bragg's law with n = 1, d = 0.215 nm = 2.15 × 10⁻¹⁰ m, θ = 50.0°:
λ = 2d sinθ = 2 × 2.15 × 10⁻¹⁰ × sin(50.0°) = 4.30 × 10⁻¹⁰ × 0.7660 = 3.294 × 10⁻¹⁰ m = 0.329 nm.

(ii) De Broglie wavelength for V = 54.0 V:
λ = h/√(2m_e eV) = 6.63 × 10⁻³⁴ / √(2 × 9.11 × 10⁻³¹ × 1.60 × 10⁻¹⁹ × 54.0)
= 6.63 × 10⁻³⁴ / √(1.574 × 10⁻⁴⁷)
= 6.63 × 10⁻³⁴ / 3.967 × 10⁻²⁴ = 1.671 × 10⁻¹⁰ m = 0.167 nm.

(iii) The wavelengths differ by almost a factor of 2 (0.167 nm vs 0.329 nm). At first glance this seems to contradict de Broglie. However, in the actual Davisson-Germer experiment, the 50° peak was not the first-order diffraction. The strong peak at 50° came from a particular set of crystal planes, and the effective spacing was different from the bulk atomic spacing. When the correct crystal geometry is accounted for, the measured wavelength matches de Broglie's prediction. The student should note that this apparent discrepancy highlights the importance of using the correct d-spacing for the specific crystal planes involved.

(e) G.P. Thomson passed high-energy electrons through thin metal films (rather than reflecting them from a crystal surface). The electrons produced concentric diffraction rings on a photographic plate — analogous to the Debye-Scherrer rings in X-ray diffraction. This was an independent method because it used transmission geometry (electrons passing through the sample) rather than reflection geometry (Davisson-Germer). Both methods gave wavelengths consistent with λ = h/p, providing strong, complementary evidence for electron diffraction.

---

## Key Takeaways

1. Light exhibits wave-particle duality: it shows wave behavior (interference, diffraction) and particle behavior (photoelectric effect, photon momentum).

2. Louis de Broglie (1924) proposed that all matter has an associated wavelength λ = h/p = h/(mv). This was a bold symmetry argument: if waves can be particles, particles can be waves.

3. Electron diffraction experiments (Davisson-Germer, G.P. Thomson, 1927) confirmed de Broglie's hypothesis experimentally. Electrons produce diffraction patterns just like X-rays.

4. The de Broglie wavelength of macroscopic objects is far too small to observe. Only particles with very small mass (electrons, neutrons, atoms) have measurable wavelengths.

5. De Broglie's hypothesis explains Bohr's quantization: electron orbits are stable only when an integer number of wavelengths fit around the circumference (2πr = nλ). This gives mvr = nℏ — Bohr's postulate derived from wave physics.

6. Applications include electron microscopes (λ ≈ 0.004 nm, 100,000× better resolution than visible light) and neutron diffraction (probing crystal and magnetic structure).
