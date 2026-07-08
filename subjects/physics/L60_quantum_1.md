# Lesson 60: Quantum 1 — The Photoelectric Effect

## What You'll Learn

Imagine you're at the beach, standing in ankle-deep water. The waves wash over your feet continuously. If you put a toy boat in the water, it bobs up and down — but it never gets knocked completely out of the water unless a wave is unusually big. The energy the boat gets depends on how big the wave is (its amplitude), not on how fast the waves arrive (their frequency).

This is how classical physics thought about light. Light is a wave. Its energy depends on its intensity (brightness). If you shine a dim light on a piece of metal long enough, the waves should eventually transfer enough energy to knock electrons out — just like gentle but persistent surf can erode a cliff.

But that's not what happens. Instead, the photoelectric effect revealed something shocking: below a certain frequency, NO electrons are emitted — even if you shine the brightest light imaginable on the metal for a million years. Above that frequency, electrons ARE emitted — instantly, even with the dimmest light. And their energy depends NOT on brightness, but on the light's COLOR (frequency).

This lesson explains the experiment that broke classical physics and launched the quantum revolution.

---

## 1. What Is the Photoelectric Effect?

### Why This Matters

The photoelectric effect is one of the three great "classical physics fails" experiments (along with blackbody radiation and atomic spectra). Understanding what was observed — and WHY classical wave theory couldn't explain it — gives you the motivation for every quantum concept that follows. Without understanding this crisis, quantum physics seems like arbitrary rules. With it, you see that quantum physics was FORCED upon us by experimental data.

### The Key Ideas

**The basic phenomenon.** When electromagnetic radiation (light, ultraviolet, X-rays) shines on a metal surface, electrons are sometimes emitted from the surface. These emitted electrons are called **photoelectrons**. The effect was first observed by Heinrich Hertz in 1887 (the same Hertz the frequency unit is named after) when he noticed that ultraviolet light made sparks jump more easily between two electrodes. He reported it as a curiosity. He didn't know he'd found the crack in classical physics.

**The experimental setup.** In its simplest form, a photoelectric experiment consists of:

1. A **photocathode** — a metal plate that emits electrons when light hits it.
2. An **anode** — a second plate that collects the emitted electrons.
3. These are sealed in an evacuated glass tube (air would stop the electrons).
4. A variable voltage source connected between the cathode and anode.
5. An ammeter to measure the resulting current (the **photocurrent**).
6. A light source that can be adjusted in both frequency (color) and intensity (brightness).

When light hits the cathode, electrons are emitted. If the anode is positive relative to the cathode, electrons are attracted to it, and current flows. The amount of current tells us how many photoelectrons are being emitted per second.

**The key observations.** Four experimental facts were discovered that classical wave theory COULD NOT EXPLAIN:

**Observation 1: Threshold frequency.** For each metal, there is a minimum frequency f₀ (called the **threshold frequency**) below which NO photoelectrons are emitted — regardless of how intense the light is. No matter how bright you make the light, if f < f₀, zero electrons come out. Zero. Above f₀, photoelectrons are emitted even with extremely dim light.

For example, sodium has a threshold frequency of about 5.5 × 10¹⁴ Hz (green light). Shine red light (f ≈ 4.3 × 10¹⁴ Hz) on sodium, and nothing happens — even if the red light is blindingly bright. Shine dim blue light (f ≈ 6.7 × 10¹⁴ Hz), and electrons are emitted immediately.

**Observation 2: Instantaneous emission.** When light with f > f₀ strikes the metal, photoelectrons are emitted IMMEDIATELY — with no measurable time delay. Not even a nanosecond. This is true even for extremely dim light where the total energy arriving per second is tiny.

**Observation 3: Maximum kinetic energy depends on frequency, not intensity.** The maximum kinetic energy of the emitted photoelectrons (KE_max) increases linearly with the frequency of the light. Doubling the intensity (brightness) of the light does NOT change KE_max — it only produces MORE photoelectrons (higher current).

**Observation 4: The linear relationship.** A graph of KE_max vs. frequency f is a straight line. The line has a slope equal to Planck's constant h. The x-intercept is the threshold frequency f₀. Different metals have different threshold frequencies but the SAME slope. This is incredibly important.

### Why Classical Wave Theory Fails — For Each Observation

Classical physics (Maxwell's electromagnetic wave theory) predicts something completely different. Let's go through each observation and see WHERE classical theory breaks:

**Classical prediction vs. Observation 1 (threshold frequency):** Classical theory says the energy in a wave depends on its amplitude (intensity) squared, not its frequency. A very intense low-frequency wave should carry plenty of energy and should eventually eject electrons, just like a gentle ocean wave can erode a cliff. But the experiment shows that below f₀, NOTHING works. A billion watts per square meter of red light ejects zero electrons from sodium; a milliwatt of blue light ejects them instantly. **Classical physics has no explanation for threshold frequency.**

**Classical prediction vs. Observation 2 (instantaneous emission):** In classical theory, the wave energy is spread continuously over the wavefront. A single electron is a tiny target — it can only absorb a tiny fraction of the wave's energy. For dim light, it should take seconds, minutes, or longer for one electron to accumulate enough energy to escape. But the experiment shows instantaneous emission — the electron is kicked out in less than 10⁻⁹ seconds. **Classical physics cannot explain why emission is instantaneous with dim light.**

**Classical prediction vs. Observation 3 (KE_max independent of intensity):** Classical theory says more intense light = bigger electric field = greater force on the electron = more kinetic energy when it escapes. But the experiment shows that intensity only affects the NUMBER of electrons, not their energy. **Classical physics cannot explain why intensity doesn't affect KE_max.**

**Classical prediction vs. Observation 4 (linear KE_max vs. f):** Classical theory predicts KE_max should depend on intensity, not frequency. It has no mechanism for the linear KE_max vs. f relationship with slope h. **Classical physics has no explanation for this graph at all.**

---

## 2. Einstein's Photon Model (1905)

### Why This Matters

Einstein's explanation of the photoelectric effect was the work specifically cited in his 1921 Nobel Prize (not relativity!). It introduced the **photon** — a quantum of light — and established that light energy comes in discrete packets. This was so radical that even Planck, who had introduced quantization for blackbody radiation, initially rejected it. The photon concept is the foundation of all quantum optics, lasers, and modern photonics.

### The Key Ideas

**The photon.** Einstein proposed that light consists of discrete packets of energy called **photons**. Each photon carries energy:

$$E = h f$$

where h = 6.63 × 10⁻³⁴ J·s (Planck's constant) and f is the frequency of the light. A photon is the smallest possible unit of light at that frequency — you can't have 0.37 of a photon. The energy of a photon depends ONLY on its frequency (color), not on the overall brightness of the beam.

**Intensity reinterpreted.** In the photon model, the intensity (brightness) of a beam of light is determined by the NUMBER of photons arriving per second per unit area. Bright light = many photons per second. Dim light = few photons per second. Each photon still has energy hf regardless of how many there are.

**The photoelectric equation.** When a photon hits the metal surface, it interacts with a SINGLE electron. All of the photon's energy (hf) is transferred to that one electron in a single interaction. The electron uses some of this energy to escape from the metal (overcoming the forces binding it to the surface) and the rest becomes its kinetic energy.

The minimum energy needed to free an electron from a particular metal is called the **work function**, denoted by ϕ (the Greek letter phi) or sometimes Φ. The work function is a property of the metal — different metals have different work functions.

Einstein's photoelectric equation:

$$K E_{\text{max}} = h f - \phi$$

where:
- KE_max is the maximum kinetic energy of the emitted photoelectron
- hf is the energy of the incident photon
- ϕ is the work function of the metal

**Why it's KE_max, not just KE.** Not every electron needs exactly ϕ to escape. Some electrons are more tightly bound (deeper in the metal), some lose energy in collisions on their way out. The electrons that emerge with maximum kinetic energy are those that were least tightly bound and lost no energy on their way out. For these electrons, KE_max = hf − ϕ. Other electrons have less kinetic energy.

**How this explains EVERY observation:**

1. **Threshold frequency:** If hf < ϕ, the photon doesn't have enough energy to free even the least tightly bound electron. The electron absorbs the photon, but can't escape. No photoelectrons, no matter how many such photons arrive. The threshold frequency is f₀ = ϕ/h. Below f₀, individual photons are too weak. More weak photons don't help — an electron can only absorb ONE photon at a time.

2. **Instantaneous emission:** The energy is delivered in a concentrated packet (one photon to one electron). As soon as a photon with hf > ϕ hits an electron, the electron is freed instantly. There's no "accumulation time" — the energy arrives all at once.

3. **KE_max independent of intensity:** Each photon-electron interaction is one-to-one. Doubling intensity means twice as many photons, twice as many electrons — but each individual photon still has energy hf, so each electron still gets the same maximum kinetic energy. Intensity affects the NUMBER of electrons (photocurrent), not their individual energy.

4. **Linear KE_max vs. f:** KE_max = hf − ϕ is the equation of a straight line with slope h and y-intercept −ϕ. Every metal has the same slope (Planck's constant is universal) but different intercepts (different work functions). This matches the data perfectly.

### Common Misconceptions

**"The photoelectric effect proves light is a particle."** This is an oversimplification. The photoelectric effect shows that light INTERACTS with matter in quantized packets (photons). It demonstrates the PARTICLE-LIKE aspect of light in this specific type of interaction. But light also shows wave behavior in interference and diffraction experiments. Light is not "a particle" or "a wave" — it's a quantum object that exhibits both types of behavior. The photoelectric effect explores the energy-exchange aspect, which is quantized.

**"A brighter light has photons with more energy."** No. A brighter light has MORE photons, not more energetic photons, at a given frequency. The energy per photon depends ONLY on frequency. A single gamma-ray photon can have more energy than a billion radio-wave photons combined.

**"If the photon energy is exactly equal to the work function, the electron is emitted with zero kinetic energy."** Yes, theoretically. In practice, these electrons would have essentially zero speed and wouldn't reach the collector, so they wouldn't contribute to measured current.

**"Electrons can absorb multiple photons to escape if one isn't enough."** This is called multi-photon absorption and it DOES happen, but only at extremely high intensities (like those produced by pulsed lasers). In the typical photoelectric effect with conventional light sources, the probability of an electron absorbing two photons simultaneously is negligible. The one-photon-per-electron model is the correct description for ordinary intensities.

**"The work function is the same as ionization energy."** They're related concepts but different contexts. Ionization energy is the energy to remove an electron from an isolated atom in the gas phase. The work function is the energy to remove an electron from a solid metal surface. The work function is typically lower than the ionization energy of the same element because the electron in a metal is shared among many atoms.

---

## 3. The Photoelectric Equation in Detail

### Why This Matters

The equation KE_max = hf − ϕ is one of the most important equations in physics. It appears repeatedly in IB exams, and understanding every term is essential.

### The Key Ideas

**The terms:**
- **hf**: The energy carried by one photon. This is the INPUT energy.
- **ϕ**: The work function — the minimum energy to extract one electron from the metal. Think of it as an "escape fee" the electron must pay.
- **KE_max**: The leftover energy after paying the escape fee. This is the electron's kinetic energy as it leaves the surface.

**Alternative forms:**

Using the threshold frequency f₀ = ϕ/h:
$$K E_{\text{max}} = h(f - f_0)$$

Using the stopping potential V_s (the voltage needed to stop the most energetic electrons — see Lesson 61):
$$e V_s = h f - \phi$$

**Units.** Work function is often given in electron-volts (eV). Recall: 1 eV = 1.60 × 10⁻¹⁹ J. A typical work function for a metal is 2-5 eV. For comparison, the ionization energy of hydrogen is 13.6 eV.

**Work functions of common metals (for reference):**
- Cesium: 2.1 eV (lowest of all stable elements — used in photomultiplier tubes)
- Sodium: 2.3 eV
- Calcium: 2.9 eV
- Zinc: 4.3 eV
- Iron: 4.5 eV
- Platinum: 6.4 eV

Notice that alkali metals (cesium, sodium) have low work functions. This is because they have only one loosely bound outer electron. These metals are most easily induced to emit photoelectrons.

---

## 4. The Stopping Potential (Preview)

### Why This Matters

How do you actually MEASURE KE_max? You can't put a speedometer on an electron. The clever technique, which we'll study in detail in Lesson 61, is the stopping potential. Here's a brief introduction.

### The Key Ideas

If you make the collector (anode) slightly NEGATIVE relative to the photocathode, the emitted electrons (which are negative) are repelled. Only electrons with enough kinetic energy can overcome this repulsion and reach the collector. By increasing the negative voltage until the photocurrent drops to exactly zero, you find the **stopping potential** V_s.

At the stopping potential, even the most energetic electrons just barely fail to reach the collector:

$$K E_{\text{max}} = e V_s$$

where e = 1.60 × 10⁻¹⁹ C is the elementary charge. Thus, measuring V_s for different frequencies of light allows you to plot KE_max vs. f and determine both h (from the slope) and ϕ (from the intercept).

This was Millikan's experiment (Lesson 61) — which, ironically, he performed trying to DISPROVE Einstein, and instead confirmed the photon model with exquisite precision.

---

### Photon Momentum and Radiation Pressure

Although photons have no mass, they carry momentum. From special relativity, E² = (pc)² + (mc²)², and with m = 0 for a photon, we get:

$$p = \frac{E}{c} = \frac{hf}{c} = \frac{h}{\lambda}$$

This momentum is real. When photons strike a surface and are absorbed or reflected, they transfer momentum to the surface, exerting **radiation pressure**. This is how solar sails could propel spacecraft — photons from the Sun transfer momentum to large, lightweight reflective sails.

For a perfectly absorbing surface: pressure = I/c, where I is the light intensity.
For a perfectly reflecting surface: pressure = 2I/c (twice as much, because the photons reverse direction).

Radiation pressure from the Sun at Earth's orbit is about 5 × 10⁻⁶ N/m² — tiny, but in the vacuum of space, constantly applied over large areas and long times, it's enough to accelerate a spacecraft. Radiation pressure also explains why comet tails always point AWAY from the Sun — the solar wind and radiation pressure push dust and gas away.

### The Photoelectric Effect and CCD Sensors

The photoelectric effect is the operating principle of CCD (charge-coupled device) sensors — the light detectors in digital cameras, smartphone cameras, and astronomical telescopes. When a photon strikes a silicon pixel in a CCD, it ejects an electron (if the photon energy exceeds silicon's work function/band gap of about 1.1 eV). The accumulated charge in each pixel is proportional to the number of photons that hit it, creating a digital image.

This connects the abstract physics of the photoelectric effect to the most ubiquitous imaging technology of the modern world. Every photo you take with your phone is made possible by Einstein's photon model.

### A Deeper Look at "Why Intensity Doesn't Affect KE_max"

Let's make this absolutely crystal-clear with a concrete numerical example.

Suppose sodium (ϕ = 2.28 eV) is illuminated with blue light of λ = 450 nm (f = 6.67 × 10¹⁴ Hz). Photon energy = hf = 4.14 × 10⁻¹⁵ × 6.67 × 10¹⁴ = 2.76 eV. KE_max = 2.76 − 2.28 = 0.48 eV.

Now double the intensity. The electric field amplitude of the light wave increases by √2 (since I ∝ E² in classical theory). But each photon still has exactly hf = 2.76 eV. An electron absorbs one photon, gets 2.76 eV, pays ϕ = 2.28 eV, and leaves with 0.48 eV. This doesn't change.

What DOES change: twice as many photons arrive per second. If each photon interaction has the same probability of ejecting an electron, twice as many electrons are emitted. The photocurrent doubles.

Classical prediction: doubled intensity → doubled energy flux → electrons should be ejected with up to ~twice the kinetic energy. This is NOT observed. The experiment decisively rules out classical wave theory.

This is why the independence of KE_max from intensity is considered the "smoking gun" that proves the photon model.

---

## Worked Examples

### Example 1: Photon Energy

Calculate the energy (in joules and eV) of a photon of: (a) red light, λ = 650 nm, (b) ultraviolet light, λ = 250 nm.

**Approach:** Use E = hf = hc/λ.

**(a) Red light:**
f = c/λ = 3.00 × 10⁸ / (650 × 10⁻⁹) = 4.62 × 10¹⁴ Hz.
E = hf = 6.63 × 10⁻³⁴ × 4.62 × 10¹⁴ = 3.06 × 10⁻¹⁹ J.
In eV: E = 3.06 × 10⁻¹⁹ / (1.60 × 10⁻¹⁹) = 1.91 eV.

**(b) UV light:**
f = 3.00 × 10⁸ / (250 × 10⁻⁹) = 1.20 × 10¹⁵ Hz.
E = 6.63 × 10⁻³⁴ × 1.20 × 10¹⁵ = 7.96 × 10⁻¹⁹ J = 4.97 eV.

**Why this makes sense:** UV photons are more energetic than red photons (shorter wavelength = higher frequency = higher energy). 1.91 eV is below most metal work functions; 4.97 eV is above many. This is why UV light causes the photoelectric effect more readily than visible light.

---

### Example 2: Threshold Frequency and Work Function

Sodium has a work function of 2.28 eV. Calculate: (a) the threshold frequency, (b) the threshold wavelength, (c) whether green light (λ = 530 nm) will cause photoemission.

**Approach:** f₀ = ϕ/h, λ₀ = c/f₀. Compare incident wavelength with λ₀.

**Step 1:** ϕ = 2.28 eV = 2.28 × 1.60 × 10⁻¹⁹ = 3.648 × 10⁻¹⁹ J.
f₀ = ϕ/h = 3.648 × 10⁻¹⁹ / (6.63 × 10⁻³⁴) = 5.50 × 10¹⁴ Hz.

**Step 2:** λ₀ = c/f₀ = 3.00 × 10⁸ / (5.50 × 10¹⁴) = 5.45 × 10⁻⁷ m = 545 nm.

**Step 3:** Green light at 530 nm has λ < λ₀ (530 nm < 545 nm), which means f > f₀. So green light WILL cause photoemission from sodium. (Red light at 650 nm would NOT, since 650 nm > 545 nm.)

**Why this makes sense:** The threshold wavelength of sodium (~545 nm) is in the green-yellow part of the spectrum. Light bluer/greener than this ejects electrons; redder light does not.

---

### Example 3: Maximum Kinetic Energy

Ultraviolet light of wavelength 200 nm shines on a zinc surface (ϕ = 4.30 eV). Calculate: (a) the energy of one photon in eV, (b) the maximum kinetic energy of the emitted photoelectrons in eV and joules, (c) the maximum speed of the photoelectrons.

**Approach:** E = hc/λ, then KE_max = hf − ϕ, then v = √(2KE/m_e).

**Step 1:** E = hc/λ = 1.989 × 10⁻²⁵ / (200 × 10⁻⁹) = 9.945 × 10⁻¹⁹ J = 6.22 eV.

**Step 2:** KE_max = 6.22 − 4.30 = 1.92 eV = 1.92 × 1.60 × 10⁻¹⁹ = 3.07 × 10⁻¹⁹ J.

**Step 3:** v = √(2 × 3.07 × 10⁻¹⁹ / 9.11 × 10⁻³¹) = √(6.74 × 10¹¹) = 8.21 × 10⁵ m/s.

**Why this makes sense:** The speed is about 0.3% of the speed of light — non-relativistic (so our classical KE formula is valid). This is a typical photoelectron speed.

---

### Example 4: Interpreting the Graph

The graph of KE_max vs. frequency for a particular metal is a straight line with slope 6.63 × 10⁻³⁴ J·s and x-intercept 4.40 × 10¹⁴ Hz. Determine: (a) Planck's constant from the slope, (b) the work function in eV, (c) the KE_max for light of frequency 8.00 × 10¹⁴ Hz.

**Approach:** The slope IS Planck's constant (confirms photon model). Work function from x-intercept. KE_max from equation.

**Step 1:** h = 6.63 × 10⁻³⁴ J·s (the slope). This matches the accepted value.

**Step 2:** f₀ = 4.40 × 10¹⁴ Hz. ϕ = h f₀ = 6.63 × 10⁻³⁴ × 4.40 × 10¹⁴ = 2.92 × 10⁻¹⁹ J = 1.82 eV.

**Step 3:** KE_max = hf − ϕ = 6.63 × 10⁻³⁴ × 8.00 × 10¹⁴ − 2.92 × 10⁻¹⁹
= 5.30 × 10⁻¹⁹ − 2.92 × 10⁻¹⁹ = 2.38 × 10⁻¹⁹ J = 1.49 eV.

**Why this makes sense:** The straight line with universal slope h is the signature of the photon model. Different metals shift the line left/right (different ϕ) but never change the slope.

---

### Example 5: Photocurrent vs. Intensity

A photocell is illuminated with light of frequency 7.00 × 10¹⁴ Hz (above threshold for the cathode material). The intensity is 2.0 W/m² and the photocathode area is 4.0 cm². If 5.0% of incident photons produce photoelectrons, calculate: (a) the number of photons arriving per second, (b) the photocurrent.

**Approach:** Power = intensity × area. Number of photons = total energy per second / energy per photon. Current = electrons per second × e.

**Step 1:** Power = 2.0 W/m² × 4.0 × 10⁻⁴ m² = 8.0 × 10⁻⁴ W = 8.0 × 10⁻⁴ J/s.
Photon energy = hf = 6.63 × 10⁻³⁴ × 7.00 × 10¹⁴ = 4.64 × 10⁻¹⁹ J.
Photons/s = Power / E_photon = 8.0 × 10⁻⁴ / (4.64 × 10⁻¹⁹) = 1.72 × 10¹⁵ photons/s.

**Step 2:** Electrons/s = 0.050 × 1.72 × 10¹⁵ = 8.62 × 10¹³ e⁻/s.
Current = 8.62 × 10¹³ × 1.60 × 10⁻¹⁹ = 1.38 × 10⁻⁵ A = 13.8 μA.

**Why this makes sense:** Photocurrents are typically microamps. The quantum efficiency (5%) is realistic — most photons don't produce photoelectrons because they hit atoms that aren't at the surface, or they transfer energy to electrons moving in the wrong direction.

---

## Practice Problems

### Problem 1
The work function for calcium is 2.90 eV. (a) Calculate the threshold frequency and threshold wavelength for calcium. (b) Determine whether light of wavelength 450 nm will cause photoemission from calcium. (c) If 450 nm light does cause emission, calculate the maximum kinetic energy of the photoelectrons. (d) What would happen if the intensity of the 450 nm light were doubled? Explain.

### Problem 2
A clean zinc plate has a work function of 4.30 eV. It is illuminated with ultraviolet light of wavelength 150 nm. (a) Calculate the maximum kinetic energy of the emitted photoelectrons in eV and joules. (b) Calculate the de Broglie wavelength of these photoelectrons (see Lesson 59). (c) Explain why visible light cannot eject electrons from zinc, even at high intensities.

### Problem 3
A photoelectric experiment is performed on an unknown metal. It is found that light of frequency 5.80 × 10¹⁴ Hz produces photoelectrons with maximum kinetic energy 0.45 eV. (a) Calculate the work function of the metal in eV. (b) Determine the threshold frequency. (c) If the light intensity is tripled, what happens to (i) the maximum kinetic energy, (ii) the number of photoelectrons emitted per second? Explain both answers.

### Problem 4
A student says: "The photoelectric effect shows that light is made of particles. So Young's double-slit experiment, which shows interference, must be wrong." Explain why this statement reflects a misunderstanding of wave-particle duality. Use specific experimental evidence to support your explanation.

### Problem 5
The graph shows KE_max vs. frequency for two different metals, A and B. Both graphs are parallel straight lines, but A has a larger threshold frequency than B. (a) Which metal has the larger work function? Explain. (b) Why are the lines parallel? (c) If light of frequency f = 1.0 × 10¹⁵ Hz is incident on both metals, which metal emits electrons with greater maximum kinetic energy? (d) Sketch what the graph would look like if the same experiment were performed on metal A but with light of twice the intensity.

### Problem 6 (IB Exam Style)
Monochromatic light of wavelength 435 nm is incident on a clean sodium surface in an evacuated tube. The work function of sodium is 2.28 eV.

(a) Define the term "work function." [1 mark]

(b) Show that the energy of a photon of this light is approximately 2.85 eV. [2 marks]

(c) (i) Calculate the maximum kinetic energy, in eV, of the electrons emitted from the sodium surface. [1 mark]
(ii) Determine the maximum speed of these electrons. [2 marks]

(d) The intensity of the light is doubled but its wavelength remains 435 nm. State and explain the effect, if any, on: (i) the maximum kinetic energy of the emitted electrons, (ii) the rate at which electrons are emitted from the surface. [4 marks]

(e) The light source is changed to one of wavelength 600 nm. Even at very high intensity, no electrons are detected. Explain this observation. [2 marks]

---

## Answers

### Answer 1
(a) ϕ = 2.90 × 1.60 × 10⁻¹⁹ = 4.64 × 10⁻¹⁹ J.
f₀ = ϕ/h = 4.64 × 10⁻¹⁹ / (6.63 × 10⁻³⁴) = 7.00 × 10¹⁴ Hz.
λ₀ = c/f₀ = 3.00 × 10⁸ / (7.00 × 10¹⁴) = 4.29 × 10⁻⁷ m = 429 nm.

(b) 450 nm > 429 nm, so the photon energy (hc/450nm = 2.76 eV) is less than ϕ = 2.90 eV. NO photoemission.

(c) Not applicable — no photoemission occurs.

(d) Doubling intensity still produces zero photoelectrons because each individual photon still has energy 2.76 eV < 2.90 eV. Below threshold, intensity is irrelevant. This is one of the key facts that classical wave theory cannot explain.

### Answer 2
(a) E = hc/λ = 1.989 × 10⁻²⁵ / (150 × 10⁻⁹) = 1.326 × 10⁻¹⁸ J = 8.29 eV.
KE_max = 8.29 − 4.30 = 3.99 eV = 6.38 × 10⁻¹⁹ J.

(b) p = √(2m_e KE) = √(2 × 9.11 × 10⁻³¹ × 6.38 × 10⁻¹⁹) = √(1.163 × 10⁻⁴⁸) = 1.078 × 10⁻²⁴ kg·m/s.
λ = h/p = 6.63 × 10⁻³⁴ / (1.078 × 10⁻²⁴) = 6.15 × 10⁻¹⁰ m = 0.615 nm.

(c) Visible light has photon energies up to about 3.1 eV (violet, 400 nm). Zinc's work function is 4.30 eV. Every visible photon, regardless of how many there are, individually has less energy than the work function. Since an electron can only absorb one photon at a time (at ordinary intensities), no single photon has enough energy to free an electron. Adding more photons doesn't help — one electron can't save up energy from multiple photons.

### Answer 3
(a) hf = 6.63 × 10⁻³⁴ × 5.80 × 10¹⁴ = 3.845 × 10⁻¹⁹ J = 2.40 eV.
KE_max = 0.45 eV.
ϕ = hf − KE_max = 2.40 − 0.45 = 1.95 eV.

(b) f₀ = ϕ/h = 1.95 × 1.60 × 10⁻¹⁹ / (6.63 × 10⁻³⁴) = 4.71 × 10¹⁴ Hz.

(c) (i) KE_max is unchanged. Each individual photon still has energy hf = 2.40 eV, and each electron still pays the same work function ϕ = 1.95 eV. The photon-electron interaction is one-to-one.
(ii) The number of photoelectrons per second triples. Three times the intensity means three times as many photons striking the surface per second, so (assuming constant quantum efficiency) three times as many photoelectrons are emitted per second. The current triples.

### Answer 4
The student's statement reflects a false dichotomy — that light must be EITHER a particle OR a wave. Both the photoelectric effect and Young's double-slit experiment are correct; they reveal DIFFERENT ASPECTS of light's behavior.

The photoelectric effect demonstrates that light exchanges energy with matter in discrete quanta (photons). The energy exchanges happen one photon at a time, and the photon energy is hf. This is the particle-like aspect of light in interactions.

Young's double-slit experiment demonstrates that light propagates as a wave, producing interference patterns that can only be explained by superposition of waves. This is the wave-like aspect of light in propagation.

Both experiments are correct, and both are reproducible. The resolution is wave-particle duality: light is a quantum entity that exhibits wave-like behavior (interference, diffraction) and particle-like behavior (quantized energy exchange) depending on how you measure it. Neither experiment invalidates the other — together, they give a more complete picture of what light is. Classical concepts of "pure wave" and "pure particle" are both inadequate.

### Answer 5
(a) Metal A has the larger work function. Threshold frequency f₀ = ϕ/h, so a larger f₀ means a larger ϕ. Metal A requires higher-frequency (more energetic) photons to initiate photoemission.

(b) The lines are parallel because the slope equals Planck's constant h, which is a universal constant — the same for all metals. KE_max = hf − ϕ; only the intercept (−ϕ) differs between metals.

(c) Metal B emits electrons with greater KE_max. At the same frequency, both metals give electrons the same photon energy hf, but metal B takes less of that energy as the "escape fee" (smaller ϕ), so more is left as kinetic energy.

(d) The graph for metal A would look EXACTLY the same. Intensity affects the number of photoelectrons (the photocurrent, which is a different graph) but does not affect KE_max. The KE_max vs. f graph depends only on the photon energy (hf) and the work function (ϕ), neither of which changes with intensity.

### Answer 6
(a) The work function ϕ is the minimum energy required to remove an electron from the surface of a material. It is the energy binding the least tightly bound electron to the metal.

(b) E = hc/λ = (6.63 × 10⁻³⁴ × 3.00 × 10⁸) / (435 × 10⁻⁹)
= 1.989 × 10⁻²⁵ / 4.35 × 10⁻⁷ = 4.572 × 10⁻¹⁹ J.
In eV: 4.572 × 10⁻¹⁹ / 1.60 × 10⁻¹⁹ = 2.858 eV ≈ 2.86 eV.
[The question says "approximately 2.85 eV" — close enough.]

(c) (i) KE_max = hf − ϕ = 2.86 − 2.28 = 0.58 eV.
(ii) KE_max = 0.58 × 1.60 × 10⁻¹⁹ = 9.28 × 10⁻²⁰ J.
v = √(2KE/m_e) = √(2 × 9.28 × 10⁻²⁰ / 9.11 × 10⁻³¹)
= √(2.037 × 10¹¹) = 4.51 × 10⁵ m/s.

(d) (i) No effect. The maximum kinetic energy depends only on the energy of individual photons (hf) minus the work function (ϕ). Doubling intensity increases the number of photons but each photon still has the same energy hf. Each electron still receives energy from one photon, so KE_max is unchanged.
(ii) The rate of electron emission doubles. Double intensity means double the number of photons per second. Since each photon (with sufficient energy) can liberate one electron, twice as many photoelectrons are emitted per second. The photocurrent would double.

(e) For λ = 600 nm: E = hc/λ = 1.989 × 10⁻²⁵ / (600 × 10⁻⁹) = 3.315 × 10⁻¹⁹ J = 2.07 eV. This is less than the work function of sodium (2.28 eV). Each individual photon lacks the energy to free an electron. An electron can absorb only one photon at a time (at these intensities), so no photon has sufficient energy, regardless of how many there are. Below the threshold frequency, photoemission is impossible.

---

## Key Takeaways

1. The photoelectric effect is the emission of electrons from a metal surface when illuminated by light of sufficiently high frequency.

2. Four key observations broke classical wave theory: (i) threshold frequency below which no emission occurs, (ii) instantaneous emission, (iii) KE_max depends on frequency not intensity, (iv) the linear KE_max vs. f graph with universal slope h.

3. Einstein explained the effect by proposing that light consists of photons, each with energy E = hf. A single photon transfers all its energy to a single electron.

4. The photoelectric equation: KE_max = hf − ϕ, where ϕ is the work function. The threshold frequency is f₀ = ϕ/h.

5. Intensity (brightness) determines the NUMBER of photons per second and thus the photocurrent. It does NOT affect the energy of individual photons or the KE_max of the electrons.

6. The work function ϕ is a material property. Alkali metals (cesium, sodium) have low work functions and are photosensitive to visible light; metals like zinc and platinum require ultraviolet.
