# Lesson 58: Atom 2 — Energy Levels, Spectra, and the Bohr Model

## What You'll Learn

Rutherford's nuclear model solved one problem (what's inside the atom) but created another, much more serious one. According to classical physics, an electron orbiting a nucleus should continuously radiate electromagnetic energy, spiral into the nucleus in about a nanosecond, and atoms should not exist. But atoms DO exist. They're stable. And when they do emit light, they don't emit a continuous rainbow — they emit only specific, sharply defined colors.

This lesson explains how Niels Bohr solved this crisis in 1913 with a model that, while ultimately incomplete, introduced the revolutionary idea that energy at the atomic scale is **quantized** — it comes in discrete packets, not as a continuous flow. You'll learn about emission and absorption spectra, how they serve as fingerprints for identifying elements, and why the light from a neon sign is fundamentally different from the light from a hot piece of metal.

---

## 1. The Crisis of the Nuclear Atom

### Why This Matters

Before Bohr, physics had a paradox: Rutherford's experimental evidence for the nuclear atom was irrefutable, but classical electromagnetic theory said such an atom couldn't exist for more than a billionth of a second. The resolution of this paradox required abandoning one of the most deeply held assumptions in physics: that energy can vary continuously.

### The Key Ideas

**The classical problem.** In Rutherford's model, electrons orbit the nucleus. But an orbiting electron is accelerating (centripetal acceleration toward the nucleus — acceleration doesn't just mean "speeding up"; changing direction is acceleration too). According to classical electromagnetism, any accelerating charged particle radiates electromagnetic waves — it loses energy. An electron losing energy would spiral into the nucleus in about 10⁻⁹ seconds. Atoms would collapse instantly. They don't. Therefore, something is fundamentally wrong with applying classical physics to the atom.

**The spectral problem.** When you heat a solid object (like the filament of an incandescent bulb), it glows with a continuous spectrum — all wavelengths from red to blue are present. But when you pass an electric current through a gas at low pressure (like a neon sign), the gas emits only specific, discrete wavelengths — a **line spectrum**. Each element has its own unique set of spectral lines. Classical physics had no explanation for why atoms only emit certain colors.

**The stability problem and the spectral problem are the same problem.** They both point to the same thing: energy at the atomic scale cannot vary continuously. There must be something that prevents the electron from spiraling in — some rule that says certain orbits are allowed and others are forbidden. That "something" is quantization.

---

## 2. Emission and Absorption Spectra

### Why This Matters

Spectra are the primary way we know what stars are made of, what elements exist in distant galaxies, and even what the atmospheres of exoplanets contain. Understanding how spectra form gives you the key to reading the chemical composition of the entire universe.

### The Key Ideas

**Continuous spectrum.** A hot, dense object (like the Sun's interior or an incandescent bulb filament) produces a continuous spectrum — a smooth rainbow of colors with no gaps. The spectrum looks like a continuous band of colors. This is called **blackbody radiation** and is purely thermal in origin.

**Emission line spectrum.** A hot gas at low pressure, excited by an electric discharge or heat, emits light only at specific, sharply defined wavelengths. When this light is passed through a prism or diffraction grating, you see bright colored lines on a dark background. Each element has its own unique pattern of lines — like a fingerprint.

For example, hydrogen's visible spectrum (the **Balmer series**) shows four prominent lines: red (656 nm), blue-green (486 nm), violet (434 nm), and deep violet (410 nm). Sodium's spectrum shows a brilliant yellow doublet at 589.0 and 589.6 nm — this is the yellow glow of sodium streetlights.

**Absorption line spectrum.** When white light (all wavelengths) passes through a cool gas, the gas absorbs light at exactly the same wavelengths it would emit if it were hot. The resulting spectrum shows dark lines (absorption lines) against a bright continuous background. The dark lines appear at exactly the same wavelengths as the bright lines in the emission spectrum of the same element.

This is how we discovered helium: in 1868, astronomers observed a yellow spectral line in the Sun's absorption spectrum that didn't match any known element on Earth. They named the new element "helium" after *helios*, the Greek word for Sun. It was found on Earth 27 years later.

**The connection.** The wavelengths absorbed by a cold gas are EXACTLY the wavelengths emitted by a hot gas of the same element. This tells us something profound: atoms can only absorb or emit energy in specific, fixed amounts. They cannot absorb or emit just any amount. This is the essence of quantization.

### Common Misconceptions

**"Emission spectra and absorption spectra are different things."** They're two manifestations of the same atomic process. An atom absorbs a photon when an electron jumps UP to a higher energy level; it emits a photon when an electron falls DOWN. The energy (and thus wavelength) of the photon is the same in both directions.

**"Stars produce emission spectra."** The Sun's photosphere produces an absorption spectrum. The dense interior emits a continuous spectrum; the cooler outer atmosphere absorbs specific wavelengths, creating dark Fraunhofer lines. This absorption spectrum reveals the chemical composition of the Sun's atmosphere.

---

## 3. The Bohr Model of the Atom (1913)

### Why This Matters

Bohr's model was the first to successfully explain the hydrogen spectrum and introduce quantization to atomic physics. Although it was superseded by quantum mechanics, it's still taught because: (1) it gives the correct energy levels for hydrogen, (2) it introduces the quantum concept in a concrete, visualizable way, and (3) it explains the origin of spectral lines.

### The Key Ideas

**Bohr's postulates.** Bohr made three radical assumptions that broke with classical physics:

**Postulate 1: Stationary states.** Electrons can only exist in certain specific orbits, called **stationary states**, without radiating energy. While in these orbits, the electron does NOT emit electromagnetic radiation, despite being in accelerated motion. This directly contradicts classical electromagnetism but is necessary to explain atomic stability.

**Postulate 2: Quantized angular momentum.** The allowed orbits are those in which the electron's angular momentum is an integer multiple of h/(2π):

$$m_e v r = n \frac{h}{2\pi} = n\hbar$$

where n = 1, 2, 3, ... is the **principal quantum number** and ℏ (h-bar) = h/(2π) = 1.055 × 10⁻³⁴ J·s.

**Postulate 3: Energy transitions.** An electron can jump from one stationary state to another. When it jumps from a higher energy level to a lower one, it emits a photon whose energy equals the difference between the two levels:

$$h f = |E_{\text{high}} - E_{\text{low}}|$$

When it absorbs a photon, it jumps from a lower level to a higher one. The photon energy must EXACTLY match the energy difference — no more, no less.

**Deriving the energy levels.** From Coulomb's law and centripetal force for an electron in a circular orbit:

$$\frac{1}{4\pi\varepsilon_0} \frac{e^2}{r^2} = \frac{m_e v^2}{r}$$

Combined with the angular momentum condition m_e v r = nℏ, we can solve for the radius and energy of each orbit.

The result for the radius of the nth orbit:

$$r_n = n^2 \frac{4\pi\varepsilon_0 \hbar^2}{m_e e^2} = n^2 r_B$$

where r_B = 5.29 × 10⁻¹¹ m is the **Bohr radius** — the radius of the ground state of hydrogen.

The total energy (kinetic + potential) of the nth level:

$$E_n = -\frac{m_e e^4}{8\varepsilon_0^2 h^2} \frac{1}{n^2} = -\frac{13.6 \text{ eV}}{n^2}$$

This is the famous formula: $E_n = -13.6 / n^2$ eV.

**What the negative sign means.** The energy is negative because the electron is bound to the nucleus. You would have to ADD 13.6 eV of energy to remove the electron from the ground state (n = 1). This energy, 13.6 eV, is the **ionization energy** of hydrogen. An electron with positive total energy is no longer bound — it's free.

### The Energy Level Diagram

The energy levels of hydrogen:
- n = 1: E = −13.60 eV (ground state)
- n = 2: E = −3.40 eV
- n = 3: E = −1.51 eV
- n = 4: E = −0.85 eV
- n = 5: E = −0.54 eV
- ...
- n = ∞: E = 0 eV (ionization — electron is free)

Notice that the levels get closer together as n increases. The energy difference between n = 1 and n = 2 is 10.2 eV. Between n = 4 and n = 5, it's only 0.31 eV.

---

## 4. Explaining the Hydrogen Spectrum

### Why This Matters

Bohr's model predicted the wavelengths of hydrogen's spectral lines with remarkable accuracy. This was the first time anyone had derived the Balmer formula from fundamental principles. It was a stunning success that launched quantum physics.

### The Key Ideas

**Calculating spectral lines.** When an electron falls from level n_i to n_f (where n_i > n_f), the photon emitted has energy:

$$\Delta E = E_{n_i} - E_{n_f} = 13.6 \left(\frac{1}{n_f^2} - \frac{1}{n_i^2}\right) \text{ eV}$$

The wavelength of the photon is:

$$\lambda = \frac{hc}{\Delta E}$$

Putting it together (and using the Rydberg constant R = 1.097 × 10⁷ m⁻¹):

$$\frac{1}{\lambda} = R\left(\frac{1}{n_f^2} - \frac{1}{n_i^2}\right)$$

**Spectral series.** Transitions ending at the same lower level form a spectral series:

- **Lyman series**: n_f = 1, n_i = 2, 3, 4, ... → ultraviolet
- **Balmer series**: n_f = 2, n_i = 3, 4, 5, ... → visible
- **Paschen series**: n_f = 3, n_i = 4, 5, 6, ... → infrared
- **Brackett series**: n_f = 4, n_i = 5, 6, 7, ... → infrared
- **Pfund series**: n_f = 5, n_i = 6, 7, 8, ... → infrared

**Why the Balmer series is visible.** The Balmer series (n_f = 2) spans wavelengths from 656 nm (red, n_i = 3) to 365 nm (ultraviolet, n_i = ∞). The first four lines fall in the visible range, which is why they were the first to be discovered.

**Absorption spectrum of hydrogen.** When white light passes through cold hydrogen gas, the gas can only absorb photons that have EXACTLY the right energy to raise an electron from n = 1 (where most hydrogen atoms are) to a higher level. This means only the Lyman series appears in absorption — because hydrogen atoms are almost all in the ground state at room temperature. (The Balmer series in absorption requires atoms already in n = 2, which is rare at low temperatures unless the gas is very hot.)

### Common Misconceptions

**"The electron physically jumps between orbits."** In Bohr's model, yes — it's a "quantum jump." In the more accurate quantum mechanical picture, the electron doesn't have a definite position and doesn't "jump" in the classical sense. The transition is a change in the electron's quantum state. The Bohr model uses classical orbits as a stepping stone to the quantum idea.

**"All atoms have the same energy level structure as hydrogen."** No. Hydrogen has one electron and one proton. The Bohr model works perfectly for hydrogen (and other one-electron ions like He⁺, Li²⁺) but fails for atoms with more than one electron because electron-electron repulsion changes the energy levels. Multi-electron atoms require quantum mechanics.

**"The energy levels are equally spaced."** No. They get closer together as n increases. The spacing between levels decreases as 1/n². This is why hydrogen's spectral lines get closer together at shorter wavelengths — the Balmer series limit at 365 nm represents the transition from n = ∞ to n = 2.

---

## 5. Limitations of the Bohr Model

### Why This Matters

Every physics model has limits. Understanding what the Bohr model CAN'T explain is just as important as understanding what it can. The model's failures pointed the way to full quantum mechanics.

### The Key Ideas

**What Bohr got right:**
1. Energy is quantized in atoms.
2. The hydrogen energy levels: E_n = −13.6/n² eV.
3. The Rydberg formula for hydrogen's spectral lines.
4. The concept of stationary states.

**What Bohr got wrong or couldn't explain:**
1. **Multi-electron atoms.** The model gives wrong predictions for helium (2 electrons), lithium (3 electrons), etc. The single-electron assumption is the problem.

2. **Relative intensities.** Why are some spectral lines brighter than others? The Bohr model has no mechanism for predicting transition probabilities.

3. **Fine structure.** High-resolution spectra show that many "single" lines are actually closely spaced doublets or triplets. The Bohr model predicts single lines.

4. **The Zeeman effect.** Spectral lines split into multiple components in a magnetic field. Bohr's circular orbits can't account for this.

5. **Why angular momentum is quantized.** Bohr simply asserted it. Quantum mechanics derives it from the wave nature of electrons.

6. **No explanation for why electrons don't radiate in stationary states.** This was just a postulate — an assumption that made the model work, not a physical explanation.

---

## Worked Examples

### Example 1: Energy of a Photon from a Transition

An electron in a hydrogen atom falls from the n = 4 level to the n = 2 level. Calculate: (a) the energy released, in eV and in joules, (b) the frequency and wavelength of the emitted photon, (c) the series this transition belongs to.

**Approach:** Use E_n = −13.6/n². Then use E = hf and c = fλ.

**Step 1:** Energy difference.
E₄ = −13.6/16 = −0.850 eV
E₂ = −13.6/4 = −3.40 eV
ΔE = E₄ − E₂ = −0.850 − (−3.40) = 2.55 eV

In joules: ΔE = 2.55 × 1.60 × 10⁻¹⁹ = 4.08 × 10⁻¹⁹ J.

**Step 2:** Frequency and wavelength.
f = ΔE / h = 4.08 × 10⁻¹⁹ / (6.63 × 10⁻³⁴) = 6.15 × 10¹⁴ Hz.
λ = c / f = 3.00 × 10⁸ / (6.15 × 10¹⁴) = 4.88 × 10⁻⁷ m = 488 nm.

**Step 3:** This drops to n = 2, so it's part of the Balmer series (visible). 488 nm is blue-green light.

**Why this makes sense:** The wavelength falls in the visible spectrum, consistent with the Balmer series. The blue-green line at 486 nm (n = 4 → 2) is the second line of the Balmer series.

---

### Example 2: Ionization Energy

Calculate the minimum energy required to ionize a hydrogen atom that is initially in the n = 3 state.

**Approach:** Ionization means the electron is completely removed (n = ∞, E = 0). The energy needed is the difference between n = 3 and n = ∞.

**Step 1:** E₃ = −13.6/9 = −1.51 eV. E_∞ = 0.
ΔE = 0 − (−1.51) = 1.51 eV.

**Step 2:** In joules: 1.51 × 1.60 × 10⁻¹⁹ = 2.42 × 10⁻¹⁹ J.

**Why this makes sense:** It takes less energy to ionize an electron from n = 3 (1.51 eV) than from the ground state (13.6 eV). The electron is already partially "up the ladder" and needs less of a boost to escape.

---

### Example 3: Identifying the Transition

A photon of wavelength 102.6 nm is emitted by a hydrogen atom. Determine the initial and final energy levels.

**Approach:** Calculate the photon energy. Then identify which transition between known levels matches this energy.

**Step 1:** Photon energy.
f = c/λ = 3.00 × 10⁸ / (102.6 × 10⁻⁹) = 2.924 × 10¹⁵ Hz.
E = hf = 6.63 × 10⁻³⁴ × 2.924 × 10¹⁵ = 1.939 × 10⁻¹⁸ J = 12.12 eV.

**Step 2:** This is a large energy, suggesting a transition to the ground state. Try n_f = 1:
ΔE = 13.6(1/1² − 1/n_i²) = 12.12
1 − 1/n_i² = 12.12/13.6 = 0.8912
1/n_i² = 0.1088
n_i² = 9.19 → n_i = 3 (or close to it; the discrepancy is small).

Let's check: n_i = 3, n_f = 1: ΔE = 13.6(1 − 1/9) = 13.6 × 8/9 = 12.09 eV. Close match.

**Why this makes sense:** 102.6 nm is in the ultraviolet — the Lyman series (n_f = 1). The Lyman-beta line (n = 3 → 1) is at 102.6 nm. The small difference between 12.12 and 12.09 eV is within rounding.

---

### Example 4: Absorption

A beam of white light passes through cold hydrogen gas. (a) What is the longest wavelength that can be absorbed? (b) What series does this absorption line belong to?

**Approach:** Most atoms are in the ground state (n = 1). The longest absorbed wavelength corresponds to the smallest energy jump from n = 1, which is to n = 2.

**Step 1:** Energy for n = 1 → n = 2:
ΔE = 13.6(1/1² − 1/2²) = 13.6 × (1 − 0.25) = 13.6 × 0.75 = 10.2 eV.

**Step 2:** Wavelength:
λ = hc/ΔE = (6.63 × 10⁻³⁴ × 3.00 × 10⁸) / (10.2 × 1.60 × 10⁻¹⁹)
= 1.989 × 10⁻²⁵ / 1.632 × 10⁻¹⁸ = 1.219 × 10⁻⁷ m = 121.9 nm.

**Step 3:** This is the Lyman-alpha line, in the ultraviolet. The Lyman series is the absorption spectrum of cold hydrogen.

**Why this makes sense:** Cold hydrogen absorbs only in the UV because the gaps from n = 1 are large. This is why the Sun's Lyman lines are in the UV — they form in the relatively cool upper atmosphere.

---

### Example 5: Bohr Radius

Using the Bohr model, calculate the radius of the electron orbit for a hydrogen atom in: (a) the ground state (n = 1), (b) the n = 3 state.

**Approach:** Use r_n = n² × r_B where r_B = 5.29 × 10⁻¹¹ m (Bohr radius).

**Step 1:** n = 1: r₁ = 1² × 5.29 × 10⁻¹¹ = 5.29 × 10⁻¹¹ m.

**Step 2:** n = 3: r₃ = 3² × 5.29 × 10⁻¹¹ = 9 × 5.29 × 10⁻¹¹ = 4.76 × 10⁻¹⁰ m.

**Why this makes sense:** The radius increases with n². An electron in n = 3 is 9 times farther from the nucleus than in n = 1. In Bohr's picture, higher energy states correspond to larger orbits.

---

## Practice Problems

### Problem 1
(a) Calculate the energy in eV of a photon emitted when an electron in hydrogen falls from n = 5 to n = 2. (b) What is the wavelength of this photon? (c) What color is this light, and is it visible to the human eye?

### Problem 2
A hydrogen atom absorbs a photon of wavelength 97.3 nm. (a) Calculate the energy of this photon in eV. (b) If the atom was initially in the ground state (n = 1), to which energy level was the electron excited? (c) Explain why the atom can absorb this photon but not one with energy 11.0 eV.

### Problem 3
A student claims that the longest wavelength in the Balmer series is 656 nm (the red line). Verify this claim by: (a) identifying the transition that produces this line, (b) calculating the wavelength, (c) explaining why no longer wavelength is possible in the Balmer series.

### Problem 4
Calculate the minimum speed an electron must have to ionize a hydrogen atom from its ground state by collision. Assume the electron transfers all its kinetic energy to the atomic electron.

### Problem 5
The Lyman-alpha line of hydrogen is at 121.6 nm. (a) Calculate the energy of this photon in eV. (b) What transition produces this line? (c) Calculate the wavelength of the equivalent line for singly ionized helium (He⁺). The energy levels for one-electron ions are E_n = −13.6 Z²/n² eV. (d) Explain why the He⁺ line is at a shorter wavelength.

### Problem 6 (IB Exam Style)
The diagram shows some energy levels of the hydrogen atom. (Not shown, but use E_n = −13.6/n² eV.)

(a) State what is meant by the "ground state" of an atom. [1 mark]

(b) Explain why the energy levels are negative. [2 marks]

(c) An electron in the n = 3 level makes a transition to the n = 2 level. (i) Calculate the energy of the emitted photon in eV. (ii) Determine the wavelength of the emitted photon. (iii) Identify the region of the electromagnetic spectrum in which this photon lies. [5 marks]

(d) A photon of energy 12.1 eV is incident on a hydrogen atom in the ground state. (i) Determine whether this photon can be absorbed. (ii) If it can, identify the final energy level of the electron. [3 marks]

(e) The Bohr model successfully predicts the energy levels of hydrogen but fails for helium. Outline one reason for this failure. [1 mark]

---

## Answers

### Answer 1
(a) E₅ = −13.6/25 = −0.544 eV; E₂ = −3.40 eV. ΔE = −0.544 − (−3.40) = 2.856 eV ≈ 2.86 eV.

(b) λ = hc/ΔE = (6.63 × 10⁻³⁴ × 3.00 × 10⁸) / (2.856 × 1.60 × 10⁻¹⁹) = 1.989 × 10⁻²⁵ / 4.570 × 10⁻¹⁹ = 4.35 × 10⁻⁷ m = 435 nm.

(c) 435 nm is violet/blue light, at the edge of human visibility (we see roughly 380-750 nm). It is visible and is in fact the violet line of the Balmer series (n = 5 → 2).

### Answer 2
(a) E = hc/λ = 1.989 × 10⁻²⁵ / (97.3 × 10⁻⁹) = 2.044 × 10⁻¹⁸ J = 12.78 eV.

(b) For n = 1 → n_i: ΔE = 13.6(1 − 1/n_i²) = 12.78.
1 − 1/n_i² = 12.78/13.6 = 0.9397.
1/n_i² = 0.0603 → n_i² = 16.58 → n_i ≈ 4.
Check: n = 4: E = −13.6/16 = −0.85 eV. ΔE = −0.85 − (−13.6) = 12.75 eV. Close match.

(c) Atoms can only absorb photons with energy exactly equal to the difference between two energy levels. The hydrogen atom has a transition at 10.2 eV (n = 1 → 2) and 12.09 eV (n = 1 → 3), but no transition at 11.0 eV. The photon must match an available energy gap EXACTLY. A photon of 11.0 eV would simply pass through without being absorbed. This is the essence of quantized energy levels.

**Common pitfall:** Students sometimes think the atom can absorb any photon above the ionization energy (13.6 eV). Above ionization, the electron is freed with kinetic energy = photon energy − 13.6 eV. But BELOW ionization, absorption only happens at exact energy matches.

### Answer 3
(a) The longest wavelength in any series corresponds to the smallest energy transition. For the Balmer series (n_f = 2), the smallest transition is from n_i = 3 to n_f = 2.

(b) ΔE = 13.6(1/4 − 1/9) = 13.6 × (0.25 − 0.1111) = 13.6 × 0.1389 = 1.889 eV.
λ = hc/ΔE = 1.989 × 10⁻²⁵ / (1.889 × 1.60 × 10⁻¹⁹) = 1.989 × 10⁻²⁵ / 3.022 × 10⁻¹⁹ = 6.58 × 10⁻⁷ m = 658 nm ≈ 656 nm (allowing for rounding and using more precise constants).

(c) The longest wavelength corresponds to the smallest ΔE, which is from the nearest higher level (n_i = 3) to n_f = 2. Any higher n_i (4, 5, ...) would jump a larger energy gap to n = 2, producing a shorter wavelength. So 656 nm is indeed the longest wavelength of the Balmer series.

### Answer 4
Ionization energy from ground state of hydrogen = 13.6 eV = 2.176 × 10⁻¹⁸ J.
Kinetic energy needed: ½ m_e v² = 2.176 × 10⁻¹⁸ J.
v² = 2 × 2.176 × 10⁻¹⁸ / (9.11 × 10⁻³¹) = 4.778 × 10¹².
v = √(4.778 × 10¹²) = 2.186 × 10⁶ m/s ≈ 2.19 × 10⁶ m/s.

This is about 0.7% of the speed of light — fast, but non-relativistic.

### Answer 5
(a) E = hc/λ = 1.989 × 10⁻²⁵ / (1.216 × 10⁻⁷) = 1.636 × 10⁻¹⁸ J = 10.23 eV. (More precisely 10.2 eV — the small difference is rounding.)

(b) Lyman-alpha = n = 2 → n = 1. This is the first line of the Lyman series.

(c) For He⁺ (Z = 2): E_n = −13.6 × 4 / n² = −54.4/n² eV.
For n = 2 → 1: ΔE = 54.4(1/1² − 1/2²) = 54.4 × 0.75 = 40.8 eV.
λ = hc/ΔE = 1.989 × 10⁻²⁵ / (40.8 × 1.60 × 10⁻¹⁹) = 1.989 × 10⁻²⁵ / 6.528 × 10⁻¹⁸ = 3.05 × 10⁻⁸ m = 30.5 nm.

(d) The He⁺ line is at a much shorter wavelength because the nuclear charge is doubled (Z = 2 vs Z = 1). The stronger electrostatic attraction makes energy gaps larger by a factor of Z² = 4. Larger energy gaps mean higher photon energies and thus shorter wavelengths.

### Answer 6
(a) The ground state is the lowest energy state of an atom (n = 1 for hydrogen). It is the most stable state; an atom in the ground state cannot emit radiation because there is no lower energy level to fall to.

(b) The energy of a bound electron is defined as negative. The zero of energy is taken as the state where the electron is infinitely far from the nucleus and at rest (completely free). Since energy must be added to remove the electron (to reach E = 0), the bound states have negative energy. The magnitude of the negative energy is the binding energy — the energy required to free the electron.

(c) (i) E₃ = −13.6/9 = −1.511 eV; E₂ = −13.6/4 = −3.40 eV. ΔE = 1.889 eV.
(ii) λ = hc/ΔE = (6.63 × 10⁻³⁴ × 3.00 × 10⁸) / (1.889 × 1.60 × 10⁻¹⁹) = 6.58 × 10⁻⁷ m = 658 nm.
(iii) This lies in the visible region (red light). Specifically, it is the H-alpha line of the Balmer series.

(d) (i) Yes, it can. The energy difference between n = 1 and n = 3 is 13.6 − 1.51 = 12.09 eV. The photon has 12.1 eV, which is approximately equal to this gap (the small difference is within experimental uncertainty for the value given).
(ii) The electron would be excited to n = 3.

(e) The Bohr model treats the atom as having a single electron orbiting the nucleus. Helium has two electrons, and the electron-electron repulsion significantly modifies the energy levels. The Bohr model does not account for electron-electron interactions, so it cannot correctly predict the spectrum of helium or any other multi-electron atom.

---

## Key Takeaways

1. Classical physics predicts that accelerating electrons should radiate and spiral into the nucleus in ~10⁻⁹ s. Atoms are stable, so classical physics fails at the atomic scale.

2. Atoms emit and absorb light only at specific wavelengths (line spectra). Each element has a unique spectral "fingerprint."

3. Bohr's model postulates: (i) electrons exist in stationary states without radiating, (ii) angular momentum is quantized (mvr = nℏ), (iii) photons are emitted/absorbed when electrons jump between levels (hf = ΔE).

4. Hydrogen energy levels: E_n = −13.6/n² eV. Transitions between levels produce the Lyman (n_f = 1, UV), Balmer (n_f = 2, visible), Paschen (n_f = 3, IR), and other series.

5. The Bohr model works for one-electron atoms (H, He⁺, Li²⁺) but fails for multi-electron atoms because it ignores electron-electron repulsion.

6. Energy at the atomic scale is quantized — an atom can only absorb photons with EXACTLY the right energy, explaining the discrete nature of spectral lines.
