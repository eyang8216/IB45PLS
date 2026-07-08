# Lesson 4: Atomic Emission Spectra — Hydrogen Spectrum & Convergence

## What You'll Learn
- Distinguish between continuous spectra and line spectra, and explain why line spectra are evidence that electron energy levels are quantised
- Describe the three stages of producing a line spectrum: excitation, relaxation (emission), and detection
- Name the three main series in the hydrogen emission spectrum and identify the final energy level (n₁) for each series
- Explain what the convergence limit of a spectral series represents and how it is related to the ionisation energy of the atom
- Calculate the energy of a photon from its wavelength or frequency using ΔE = hν and c = λν
- Use the Rydberg formula to calculate the wavelength of any line in the hydrogen spectrum and to explain trends within and between series

---

## 1. Continuous Spectra and Line Spectra — Two Very Different Kinds of Light

### What a continuous spectrum is

If you pass ordinary white light — the kind that comes from the sun or a light bulb — through a glass prism, the light spreads out into a rainbow of colours: red, orange, yellow, green, blue, indigo, and violet. This is a **continuous spectrum**. In a continuous spectrum, every possible wavelength of visible light is present, and the colours blend smoothly into one another without any gaps. A continuous spectrum is produced by hot, dense objects like the filament of an incandescent light bulb or the surface of a star. In these sources, atoms are so crowded together that they emit light across all wavelengths.

### What a line spectrum is and why it is so important

A **line spectrum** looks completely different. If you pass the light from a glowing gas (such as the gas inside a neon sign or a hydrogen discharge tube) through a prism, you do not see a continuous rainbow. Instead, you see a dark background with a few isolated, brightly coloured lines at specific positions. Each line corresponds to light of one very precise wavelength. There is no light at all at the wavelengths between these lines.

Line spectra were a puzzle when they were first discovered in the nineteenth century. Classical physics could not explain why atoms would only emit light at certain wavelengths and not others. The explanation only came with the development of quantum mechanics in the early twentieth century. The existence of line spectra is one of the most important pieces of evidence that **electron energy levels in atoms are quantised**, meaning that electrons can only have certain specific energies and cannot have any energy value in between. We will explore what "quantised" means and why it produces line spectra in the next section.

A common misconception is that line spectra are only produced in special laboratory conditions. In fact, line spectra are everywhere. The colours of neon signs, the yellow glow of sodium street lamps, and the characteristic colours seen in fireworks are all examples of line spectra produced by excited atoms in gases.

---

## 2. How a Line Spectrum Is Produced — Excitation, Relaxation, and Detection

### What happens step by step

The production of a line spectrum can be understood as a three-stage process. Every step is a direct consequence of the fact that electrons in atoms can only occupy specific, discrete energy levels.

**Stage 1: Excitation.** An atom in its normal, lowest-energy state (called the **ground state**) is supplied with energy. This energy can come from heating, from an electrical discharge, or from absorbing a photon of light. An electron in the atom absorbs a precise amount of this energy — exactly the amount needed to jump from its current energy level to a higher, empty energy level. The atom is now in an **excited state**. The electron cannot absorb just any amount of energy; it can only absorb the exact amount that matches the energy gap between two allowed levels. This is what "quantised" means: only certain energy values are permitted.

**Stage 2: Relaxation (Emission).** An excited atom is unstable. After a very short time (typically about 10⁻⁸ seconds), the excited electron falls back down to a lower energy level. When it does so, it must release the energy it previously absorbed. This energy is released as a single particle (a quantum) of light, called a **photon**. The energy of this photon is exactly equal to the energy difference between the higher level and the lower level:

\[
\Delta E = E_{\text{higher}} - E_{\text{lower}} = h\nu
\]

In this equation, h is Planck's constant (6.63 × 10⁻³⁴ J s) and ν (the Greek letter "nu") is the frequency of the light in hertz (Hz). Since the energy levels are fixed, the energy difference ΔE can only take certain specific values, so the frequency (and therefore the colour) of the emitted photon can also only take certain specific values. This is why we see discrete lines rather than a continuous smear of colour.

**Stage 3: Detection.** The emitted photons travel to a detector (which could be a prism and a photographic plate, or a modern electronic detector). Because each photon has a specific wavelength, photons from different transitions are separated. The result is a **line emission spectrum**: a pattern of bright lines at distinct wavelengths against a dark background.

### Worked Example 1: Calculating the Energy of a Photon from Its Wavelength

**Problem:** An electron in a hydrogen atom falls from the n = 3 energy level to the n = 2 energy level, emitting a photon of red light with a wavelength of 656 nanometres (nm). Calculate the energy of this photon in joules (J). Use h = 6.63 × 10⁻³⁴ J s and c = 3.00 × 10⁸ m s⁻¹.

**Approach:** We are given the wavelength and need the energy. The two equations that connect wavelength to energy are c = λν (which relates wavelength λ and frequency ν) and E = hν (which relates frequency ν and energy E). We will first find the frequency from the wavelength, then use the frequency to find the energy.

**Step 1:** Convert the wavelength from nanometres to metres, because the speed of light c is in metres per second.

\[
\lambda = 656\text{ nm} = 656 \times 10^{-9}\text{ m} = 6.56 \times 10^{-7}\text{ m}
\]

**Step 2:** Calculate the frequency using c = λν, rearranged to ν = c / λ.

\[
\nu = \frac{c}{\lambda} = \frac{3.00 \times 10^8\text{ m s}^{-1}}{6.56 \times 10^{-7}\text{ m}} = 4.57 \times 10^{14}\text{ Hz}
\]

**Step 3:** Calculate the energy using E = hν.

\[
E = h\nu = (6.63 \times 10^{-34}\text{ J s}) \times (4.57 \times 10^{14}\text{ Hz}) = 3.03 \times 10^{-19}\text{ J}
\]

**Why this makes sense:** Photon energies for visible light are typically in the range of 10⁻¹⁹ J. The red photon has a longer wavelength and lower frequency than blue light, so its energy should be at the lower end of the visible range. About 3 × 10⁻¹⁹ J is reasonable. For context, if you multiply this energy by Avogadro's number (6.02 × 10²³), you get about 182 kJ mol⁻¹ — the energy per mole of these photons.

---

## 3. The Hydrogen Emission Spectrum — Three Series of Lines

### Why hydrogen is the simplest and most important spectrum

Hydrogen is the simplest atom in the universe: it has only one proton and one electron. Because there is only one electron, the hydrogen emission spectrum is the simplest and cleanest line spectrum of any element. It became the testing ground for the quantum mechanical model of the atom, and understanding the hydrogen spectrum is essential for understanding atomic structure in general.

### What a spectral series is

In the hydrogen spectrum, the many possible electron transitions are grouped into **series**. Each series corresponds to electrons falling to a specific lower energy level, designated as n₁. Different values of n₁ produce series in different regions of the electromagnetic spectrum:

| Series Name | Final Energy Level (n₁) | Region of the Electromagnetic Spectrum | Example Transition |
|-------------|------------------------|---------------------------------------|-------------------|
| Lyman series | n₁ = 1 | Ultraviolet (UV) | n = 2 → n = 1 |
| Balmer series | n₁ = 2 | Visible light | n = 3 → n = 2 |
| Paschen series | n₁ = 3 | Infrared (IR) | n = 4 → n = 3 |

The **Balmer series** is the one you can see with your own eyes. It consists of four visible lines: a red line at 656 nm (from n = 3 to n = 2), a blue-green line at 486 nm (from n = 4 to n = 2), a blue line at 434 nm (from n = 5 to n = 2), and a violet line at 410 nm (from n = 6 to n = 2).

The **Lyman series** lies entirely in the ultraviolet region. Because the electron is falling all the way to the ground state (n = 1), these transitions release more energy than Balmer transitions. Higher energy means higher frequency and shorter wavelength — all beyond what the human eye can see.

The **Paschen series** lies in the infrared region. Because the electron only falls to n = 3, these transitions release less energy, producing photons with frequencies below the visible range.

### A key pattern: the lines get closer together

Within any series, as you look at transitions from higher and higher starting levels, the lines get closer and closer together. For example, in the Balmer series, the gap between the n = 3 → 2 line (656 nm) and the n = 4 → 2 line (486 nm) is about 170 nm. The gap between n = 4 → 2 and n = 5 → 2 (434 nm) is only about 52 nm. As n gets larger, the energy levels themselves get closer together near the top, so the differences between successive transitions become smaller and smaller.

### Worked Example 2: Identifying a Transition from Its Wavelength

**Problem:** A line in the emission spectrum of hydrogen is observed at a wavelength of 486 nm. This line belongs to the Balmer series. Determine the values of n₁ and n₂ for this transition.

**Approach:** The Balmer series is defined by n₁ = 2 (the electron always falls to the n = 2 level). The wavelength of 486 nm corresponds to one of the four visible Balmer lines. We need to identify which starting level n₂ produces this wavelength.

**Solution:** The four visible Balmer lines and their starting levels are: 656 nm (n₂ = 3), 486 nm (n₂ = 4), 434 nm (n₂ = 5), and 410 nm (n₂ = 6). Therefore, the line at 486 nm corresponds to the transition from n₂ = 4 to n₁ = 2.

**Why this makes sense:** It is useful to memorise the correspondence between the visible Balmer lines and their n₂ values, as IB exam questions often require you to identify transitions. The 486 nm line is the blue-green line, which is the second line in the series.

---

## 4. The Convergence Limit — Where Lines Become a Continuum

### What the convergence limit is and what it physically represents

As we look at transitions from higher and higher starting levels within a series, the lines crowd closer and closer together. Eventually, at very high values of n, the lines are so close that they cannot be distinguished from one another. They appear to merge into a continuous band of light. The point at which this merging occurs is called the **convergence limit**.

The convergence limit corresponds to a transition from n = ∞ (infinity) to the final level n₁ of that series. An electron at n = ∞ is completely free — it is no longer bound to the nucleus at all. The atom has been ionised. Therefore, the convergence limit represents the point at which the electron has just enough energy to escape the atom entirely.

### How the convergence limit gives us the ionisation energy

For the Lyman series (n₁ = 1), the convergence limit corresponds to an electron falling from n = ∞ all the way to n = 1. The energy of a photon at the convergence limit is exactly the energy that would be required to do the reverse process: remove an electron from n = 1 and send it to n = ∞. In other words, the energy of the Lyman series convergence limit photon is equal to the **first ionisation energy** of hydrogen.

We can calculate this energy using the frequency at convergence:

\[
\text{Ionisation energy (per atom)} = h \times \nu_{\text{convergence}}
\]

To convert from joules per atom to kilojoules per mole, multiply by Avogadro's number (6.02 × 10²³ mol⁻¹) and divide by 1000.

### Worked Example 3: Calculating Ionisation Energy from the Convergence Limit

**Problem:** The convergence limit of the Lyman series for hydrogen occurs at a frequency of 3.28 × 10¹⁵ Hz. Calculate the first ionisation energy of hydrogen in kilojoules per mole (kJ mol⁻¹). Use h = 6.63 × 10⁻³⁴ J s.

**Approach:** First calculate the energy per photon (per atom) using E = hν. Then convert to energy per mole using Avogadro's number. Finally convert from joules to kilojoules.

**Step 1:** Energy per atom.

\[
E_{\text{atom}} = h\nu = (6.63 \times 10^{-34}\text{ J s}) \times (3.28 \times 10^{15}\text{ Hz}) = 2.17 \times 10^{-18}\text{ J}
\]

**Step 2:** Energy per mole.

\[
E_{\text{mole}} = (2.17 \times 10^{-18}\text{ J}) \times (6.02 \times 10^{23}\text{ mol}^{-1}) = 1.31 \times 10^{6}\text{ J mol}^{-1}
\]

**Step 3:** Convert to kilojoules.

\[
E = 1.31 \times 10^{6}\text{ J mol}^{-1} \div 1000 = 1310\text{ kJ mol}^{-1}
\]

**Why this makes sense:** The literature value for the ionisation energy of hydrogen is 1312 kJ mol⁻¹. Our calculated value of 1310 kJ mol⁻¹ agrees to three significant figures. The small difference arises from rounding of constants.

---

## 5. The Rydberg Formula — Predicting Any Line in the Hydrogen Spectrum

### What the Rydberg formula is and what it tells us

The **Rydberg formula** is a mathematical equation that can predict the wavelength of any line in the hydrogen emission spectrum, given the two energy levels involved in the transition. It is written as:

\[
\frac{1}{\lambda} = R_H \left( \frac{1}{n_1^2} - \frac{1}{n_2^2} \right)
\]

In this formula:
- λ (lambda) is the wavelength of the emitted photon, in metres (m).
- R_H is the Rydberg constant, which has a value of 1.097 × 10⁷ m⁻¹.
- n₁ is the lower energy level (the level the electron falls to). This must be a positive integer: 1, 2, 3, and so on.
- n₂ is the higher energy level (the level the electron falls from). This must be larger than n₁, so n₂ > n₁.

The formula shows us that the energy of a photon (which is proportional to 1/λ) depends on the difference between 1/n₁² and 1/n₂². As n₂ gets larger and larger, the term 1/n₂² gets smaller and smaller, approaching zero. This explains why the lines in a series crowd together — the differences between successive transitions shrink as n₂ increases.

### Using the Rydberg formula to compare series

The Rydberg formula also explains why the Lyman series (n₁ = 1) produces photons with much higher energy (shorter wavelength) than the Balmer series (n₁ = 2). When n₁ = 1, the term 1/n₁² = 1/1 = 1. When n₁ = 2, the term 1/n₁² = 1/4 = 0.25. Since 1/λ = R_H × (1/n₁² − 1/n₂²), a larger value of 1/n₁² leads to a larger value of 1/λ, which means a smaller wavelength λ and therefore a higher energy photon. The Lyman series photons are ultraviolet; the Balmer series photons are visible — exactly as the formula predicts.

### Worked Example 4: Using the Rydberg Formula to Calculate a Wavelength

**Problem:** Use the Rydberg formula to calculate the wavelength of the first line in the Lyman series, which corresponds to the transition from n = 2 to n = 1. The Rydberg constant R_H = 1.097 × 10⁷ m⁻¹.

**Approach:** Substitute n₁ = 1 and n₂ = 2 into the Rydberg formula and solve for λ.

\[
\frac{1}{\lambda} = R_H \left( \frac{1}{n_1^2} - \frac{1}{n_2^2} \right) = 1.097 \times 10^7 \times \left( \frac{1}{1^2} - \frac{1}{2^2} \right)
\]

\[
\frac{1}{\lambda} = 1.097 \times 10^7 \times \left( 1 - \frac{1}{4} \right) = 1.097 \times 10^7 \times 0.75
\]

\[
\frac{1}{\lambda} = 8.23 \times 10^6\text{ m}^{-1}
\]

\[
\lambda = \frac{1}{8.23 \times 10^6} = 1.22 \times 10^{-7}\text{ m} = 122\text{ nm}
\]

**Why this makes sense:** The wavelength of 122 nm is in the ultraviolet region of the electromagnetic spectrum, which is exactly where we expect the Lyman series to be. The first line of the Lyman series is indeed the longest-wavelength (lowest-energy) line in that series, and 122 nm is just beyond the violet end of the visible spectrum.

---

## Practice Problems

**Problem 1:** A photon of green light has a wavelength of 500 nanometres. Calculate the energy of this photon in joules. Use Planck's constant h = 6.63 × 10⁻³⁴ J s and the speed of light c = 3.00 × 10⁸ m s⁻¹.

**Problem 2:** A line in the Balmer series of the hydrogen emission spectrum has a frequency of 6.17 × 10¹⁴ Hz. (a) Calculate the wavelength of this line in nanometres. (b) Identify the transition by giving the values of n₁ and n₂. (c) State what colour this line appears to the human eye. (The visible spectrum spans roughly 400 nm to 700 nm.)

**Problem 3:** (a) The lines in the Balmer series get closer and closer together as the wavelength decreases. Explain why this happens, making reference to the energy levels in the hydrogen atom. (b) Name the series of the hydrogen spectrum that would be observed in the infrared region of the electromagnetic spectrum, and state the value of n₁ for this series.

**Problem 4:** The convergence limit of the Lyman series for atomic hydrogen occurs at a frequency of 3.28 × 10¹⁵ Hz. (a) Calculate the wavelength of the photon at the convergence limit. (b) Use this frequency to calculate the first ionisation energy of hydrogen in kilojoules per mole. Use h = 6.63 × 10⁻³⁴ J s and Avogadro's number = 6.02 × 10²³ mol⁻¹.

**Problem 5 (IB-Style):** The emission spectrum of atomic hydrogen contains a prominent red line at a wavelength of 656 nm in the visible region. (a) State the name of the series to which this line belongs, and give the values of n₁ and n₂ for the transition that produces it. (b) Calculate the energy, in joules, of one photon of this red light. Use c = 3.00 × 10⁸ m s⁻¹ and h = 6.63 × 10⁻³⁴ J s. (c) Another line in the same series appears at a wavelength of 365 nm, which is in the ultraviolet. Explain, by comparing the energy levels involved, why this line has a shorter wavelength (and therefore higher energy) than the 656 nm line. (d) The line at 365 nm happens to be the convergence limit of the Balmer series. Describe what would be observed in the spectrum at wavelengths shorter than 365 nm, and explain why.

---

## Answers

**Answer 1:** Convert wavelength to metres: λ = 500 nm = 5.00 × 10⁻⁷ m.

Calculate frequency: ν = c / λ = (3.00 × 10⁸) / (5.00 × 10⁻⁷) = 6.00 × 10¹⁴ Hz.

Calculate energy: E = hν = (6.63 × 10⁻³⁴) × (6.00 × 10¹⁴) = 3.98 × 10⁻¹⁹ J.

---

**Answer 2:** (a) λ = c / ν = (3.00 × 10⁸) / (6.17 × 10¹⁴) = 4.86 × 10⁻⁷ m = 486 nm.

(b) The line at 486 nm is the second line of the Balmer series, corresponding to the transition from n₂ = 4 to n₁ = 2.

(c) A wavelength of 486 nm falls in the blue-green region of the visible spectrum. The line appears as a blue-green (or cyan) colour.

---

**Answer 3:** (a) The lines get closer together because the energy levels in hydrogen converge as n increases. The energy difference between two adjacent levels, n and n + 1, is large at small values of n (for example, between n = 1 and n = 2) but becomes very small at large values of n (for example, between n = 10 and n = 11). Since the energy of the photon equals the energy difference between the two levels, transitions from high n values produce photons with very similar energies, and the corresponding spectral lines are crowded together. As n approaches infinity, the energy levels are so close together that the lines merge into a continuum.

(b) The Paschen series appears in the infrared region. For this series, the electron always falls to n₁ = 3.

---

**Answer 4:** (a) λ = c / ν = (3.00 × 10⁸) / (3.28 × 10¹⁵) = 9.15 × 10⁻⁸ m = 91.5 nm. This is in the ultraviolet region.

(b) Energy per atom: E = hν = (6.63 × 10⁻³⁴) × (3.28 × 10¹⁵) = 2.17 × 10⁻¹⁸ J.

Energy per mole: E = (2.17 × 10⁻¹⁸) × (6.02 × 10²³) = 1.31 × 10⁶ J mol⁻¹.

Convert to kJ: 1.31 × 10⁶ ÷ 1000 = 1310 kJ mol⁻¹. This is the first ionisation energy of hydrogen.

---

**Answer 5:** (a) The 656 nm line is in the visible region, so it belongs to the Balmer series, for which n₁ = 2. This particular line comes from the transition n₂ = 3 → n₁ = 2.

(b) First, convert the wavelength: λ = 656 nm = 6.56 × 10⁻⁷ m.

ν = c / λ = (3.00 × 10⁸) / (6.56 × 10⁻⁷) = 4.57 × 10¹⁴ Hz.

E = hν = (6.63 × 10⁻³⁴) × (4.57 × 10¹⁴) = 3.03 × 10⁻¹⁹ J.

(c) The 365 nm line involves a transition from a much higher starting level (for example, n₂ = 6 or higher) to n₁ = 2. The energy gap between a very high n level and n = 2 is larger than the energy gap between n = 3 and n = 2. A larger energy gap means the emitted photon carries more energy. Since energy and wavelength are inversely related (E = hc/λ), a higher energy photon has a shorter wavelength. Therefore, the transition from a higher n level produces a line at the shorter wavelength of 365 nm.

(d) At wavelengths shorter than 365 nm (which is the convergence limit of the Balmer series), the spectrum would show a continuous range of light rather than discrete lines. The convergence limit represents the transition from n = ∞ to n = 2. At wavelengths shorter than this limit, the electron is no longer falling to n = 2 but is instead being completely removed from the atom (ionised). The ejected electron can carry away any amount of kinetic energy, allowing a continuous range of photon energies and therefore a continuous spectrum rather than discrete lines. This continuous region is sometimes called the Balmer continuum.
