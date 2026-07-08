# Lesson 44: The Doppler Effect II — Light, Redshift, and Applications

## What You'll Learn
- Why the Doppler effect for light is fundamentally different from sound
- The relativistic Doppler formula for electromagnetic waves
- Redshift and blueshift: what they tell us about the universe
- The redshift parameter z and how astronomers use it
- Applications: Hubble's law, expanding universe, radar speed guns
- How to distinguish between Doppler shift and cosmological redshift

---

## 1. Light vs. Sound: A Fundamental Difference

In Lesson 43, we studied the Doppler effect for sound waves. Sound requires a medium (air, water, solid) and the speeds v_o and v_s are measured relative to that medium.

Light is different. Light does **not** require a medium. There is no "ether" that light travels through. Because of special relativity, all observers measure the same speed of light (c = 3.00 × 10⁸ m/s) regardless of their own motion. This changes the Doppler formula completely.

### What Stays the Same

- If source and observer approach each other, the observed frequency **increases** (blueshift).
- If source and observer recede from each other, the observed frequency **decreases** (redshift).

### What Changes

- There is only **relative velocity** between source and observer — no separate "source speed" and "observer speed" relative to a medium.
- The formula is different because of relativistic time dilation and length contraction.
- The shift depends only on the relative speed, not on who is moving.

---

## 2. The Relativistic Doppler Formula

For electromagnetic waves (light, radio, X-rays, etc.):

$$f' = f \sqrt{\frac{c \pm v}{c \mp v}}$$

where:
- **f** = frequency emitted by the source in its rest frame (Hz)
- **f'** = frequency observed (Hz)
- **v** = relative speed of source and observer (m/s) — the magnitude of the relative velocity
- **c** = speed of light = 3.00 × 10⁸ m/s

### Sign Convention for Light

The sign convention is simpler than for sound because only the relative motion matters:

- **Approaching (blueshift, f' > f):** Use the upper signs — f' = f √((c+v)/(c−v))
- **Receding (redshift, f' < f):** Use the lower signs — f' = f √((c−v)/(c+v))

Equivalently, in terms of wavelength λ = c/f:

$$\lambda' = \lambda \sqrt{\frac{c \mp v}{c \pm v}}$$

where the upper signs are for approaching (λ' < λ, blueshift) and the lower signs for receding (λ' > λ, redshift).

### Low-Speed Approximation

For speeds much less than c (v ≪ c), which covers nearly all everyday situations, we can use an approximation:

$$\frac{\Delta f}{f} \approx \pm \frac{v}{c}$$

or equivalently:

$$\frac{\Delta \lambda}{\lambda} \approx \mp \frac{v}{c}$$

where Δf = f' − f and Δλ = λ' − λ. The minus sign in the wavelength version means: if v is the speed of recession (positive), Δλ is positive (redshift). If v is the speed of approach, Δλ is negative (blueshift).

### Common Misconception #1

> "Light from a moving source travels at c + v or c − v."

No. All observers measure light travelling at exactly c = 3.00 × 10⁸ m/s. The wavelength and frequency change, but the speed is invariant. This is a fundamental postulate of special relativity. The Doppler effect for light is a consequence of the invariance of c combined with time dilation.

### Common Misconception #2

> "Redshift means the light is actually red in colour."

Redshift means the wavelength has **increased** (shifted toward the red end of the spectrum). If ultraviolet light from a distant galaxy is redshifted, it might become visible blue light — still not red. The term "redshift" refers to the direction of the shift, not the final colour. Similarly, "blueshift" means the wavelength has decreased.

---

## 3. The Redshift Parameter z

Astronomers define a dimensionless quantity called **redshift**, denoted by z:

$$z = \frac{\lambda_{\text{observed}} - \lambda_{\text{emitted}}}{\lambda_{\text{emitted}}} = \frac{\Delta \lambda}{\lambda}$$

Equivalently:

$$z = \frac{f_{\text{emitted}} - f_{\text{observed}}}{f_{\text{observed}}}$$

**Important:** Some textbooks define z using the observed frequency in the denominator. The IB Data Booklet uses the wavelength formula above, which is equivalent for small shifts.

For the relativistic Doppler effect:

$$1 + z = \sqrt{\frac{1 + v/c}{1 - v/c}}$$

Solving for v/c:

$$\frac{v}{c} = \frac{(1+z)^2 - 1}{(1+z)^2 + 1}$$

For small z (v ≪ c), v/c ≈ z.

### What z Values Mean

| z | Meaning |
|---|---------|
| z > 0 | Redshift — object moving away |
| z < 0 | Blueshift — object moving toward us |
| z = 0.1 | v ≈ 0.1c = 30,000 km/s |
| z = 1 | v ≈ 0.6c |
| z = 10 | v ≈ 0.98c (very distant galaxies) |

The highest confirmed redshifts for galaxies are around z ≈ 11, corresponding to light that has been travelling for over 13 billion years.

---

## 4. Applications of the Doppler Effect for Light

### 4.1 Radar Speed Guns

Police radar guns emit a microwave beam that reflects off a moving car. The reflected wave is Doppler-shifted. By measuring Δf, the gun calculates the car's speed.

This is a **double Doppler shift**: the car "receives" a shifted frequency from the gun (like a moving observer), then reflects it as a moving source. For v ≪ c:

$$\Delta f \approx \frac{2v f}{c}$$

The factor of 2 comes from the double shift.

### 4.2 Measuring the Rotation of the Sun

By measuring the Doppler shift of light from the east and west limbs (edges) of the Sun, astronomers can measure the Sun's rotation speed. One limb approaches us (blueshift), the other recedes (redshift). The Sun rotates once approximately every 25 days at its equator.

### 4.3 Binary Stars

When two stars orbit each other, one star periodically moves toward Earth and then away. The spectral lines from that star oscillate between blueshift and redshift with the orbital period. This allows astronomers to measure orbital speeds and periods, and from those, calculate the masses of the stars using Kepler's laws.

### 4.4 Exoplanet Detection

When a planet orbits a star, the star wobbles slightly around the common centre of mass. This wobble creates a tiny periodic Doppler shift in the star's light. By measuring this wobble (the **radial velocity method**), astronomers have discovered thousands of exoplanets. The effect is tiny — shifts of a few metres per second in a star's motion — requiring extremely precise spectroscopy.

---

## 5. Hubble's Law and the Expanding Universe

In 1929, Edwin Hubble discovered that distant galaxies are moving away from us, and the farther away they are, the faster they recede:

$$v = H_0 d$$

where:
- **v** = recessional velocity of the galaxy (km/s)
- **d** = distance to the galaxy (Mpc, megaparsecs)
- **H₀** = Hubble constant ≈ 70 km/s per Mpc

This is **Hubble's Law**. It tells us the universe is expanding. Every galaxy (except a few very nearby ones bound by gravity) is moving away from every other galaxy. The space between galaxies is stretching.

### Cosmological Redshift vs. Doppler Redshift

This is a subtle but important distinction. The redshift of distant galaxies is NOT primarily a Doppler shift. Galaxies are not "flying through space" away from us. Instead, the **space itself is expanding**, and the light waves are stretched as they travel through expanding space. The redshift of distant galaxies is a **cosmological redshift**, caused by the expansion of the universe.

However, for IB purposes, you can use the Doppler formula and z to calculate recessional velocities, as this gives a reasonable approximation for moderate redshifts.

### The Big Bang Implication

If galaxies are moving apart now, then in the past they must have been closer together. Extrapolating backwards, about 13.8 billion years ago, all matter and energy was concentrated in an extremely hot, dense state — the Big Bang. The cosmic microwave background radiation (CMB), with a temperature of 2.7 K, is the redshifted remnant of the radiation from this early universe.

---

## 6. Comparing Doppler Effect for Sound vs. Light

| Property | Sound | Light |
|----------|-------|-------|
| Medium required | Yes (air, water, etc.) | No |
| Speed measurement | Relative to medium | All observers measure c |
| Moving source vs. observer | Different effects | Only relative velocity matters |
| Formula | f' = f(v ± v_o)/(v ∓ v_s) | f' = f √((c ± v)/(c ∓ v)) |
| Applications | Sirens, echolocation | Astronomy, radar, cosmology |

---

## Worked Examples

### Example 1: Hydrogen Spectrum Redshift

The hydrogen-alpha spectral line has a rest wavelength of 656.3 nm. In a distant galaxy's spectrum, this line is observed at 662.9 nm.
(a) Calculate the redshift z.
(b) Estimate the recessional velocity of the galaxy.
(c) Estimate the distance to the galaxy using H₀ = 70 km/s/Mpc.

**Approach:** (a) Use the definition of z. (b) For small z, use v = cz. (c) Use Hubble's law.

(a) $z = \frac{\lambda' - \lambda}{\lambda} = \frac{662.9 - 656.3}{656.3} = \frac{6.6}{656.3} = 0.01006$

(b) Since z ≪ 1, we can use v ≈ zc = 0.01006 × 3.00 × 10⁸ = 3.02 × 10⁶ m/s = 3020 km/s.

Let's verify with the full relativistic formula: z = 0.01006 → v/c = ((1.01006)² − 1)/((1.01006)² + 1) = 0.0202/2.0202 = 0.0100. So v = 0.0100c = 3000 km/s. The approximation is excellent.

(c) d = v/H₀ = 3020 / 70 = 43.1 Mpc ≈ 140 million light-years.

**Why this makes sense:** A shift of about 6.6 nm on 656 nm is about 1%, so z ≈ 0.01 and v ≈ 3000 km/s, which is 1% of c. This is a moderately nearby galaxy (43 Mpc) that would be part of the general Hubble flow.

---

### Example 2: Radar Speed Gun

A police radar gun operates at 10.525 GHz (X-band). It detects a reflected signal shifted by 1.50 kHz from a car.
(a) Is the car approaching or receding?
(b) Calculate the speed of the car.

**Approach:** (a) Determine the sign of Δf. (b) Use Δf ≈ 2vf/c for radar double-shift.

(a) The reflected frequency is higher than the emitted frequency. A higher frequency means the car is approaching the radar gun (blueshift/double blueshift).

(b) $\Delta f = \frac{2v f}{c}$ → $v = \frac{\Delta f \cdot c}{2f}$

$v = \frac{1.50 \times 10^3 \times 3.00 \times 10^8}{2 \times 10.525 \times 10^9} = \frac{4.50 \times 10^{11}}{2.105 \times 10^{10}} = 21.4 \text{ m/s}$

v = 21.4 m/s = 77.0 km/h.

**Why this makes sense:** A 1.5 kHz shift on 10.525 GHz is about 1.4 × 10⁻⁷ fractional shift. This corresponds to v/c ≈ 7 × 10⁻⁸, giving v ≈ 21 m/s. The factor of 2 in the formula accounts for the double Doppler shift.

---

### Example 3: Receding Galaxy Using Relativistic Formula

A galaxy is measured to have z = 0.50. Calculate its recessional velocity using:
(a) The low-speed approximation v = zc.
(b) The full relativistic formula.
(c) Explain why the answers differ.

**Approach:** Compare the two formulas.

(a) $v_{\text{approx}} = 0.50 \times c = 1.50 \times 10^8 \text{ m/s}$

(b) $\frac{v}{c} = \frac{(1+z)^2 - 1}{(1+z)^2 + 1} = \frac{2.25 - 1}{2.25 + 1} = \frac{1.25}{3.25} = 0.3846$

$v = 0.3846c = 1.154 \times 10^8 \text{ m/s}$ = 115,400 km/s.

(c) The approximation v = zc fails at large z because it ignores relativistic effects. The approximation gives 0.50c, while the correct value is 0.38c. The error is about 30%. For z < 0.1, the error is less than 5%, so the approximation is acceptable. For z ≥ 0.1, always use the relativistic formula.

---

### Example 4: Blueshift of Andromeda

The Andromeda Galaxy (M31) shows a blueshift with z = −0.0010 (negative z means blueshift).
(a) What does a negative z tell us about Andromeda's motion?
(b) Calculate Andromeda's radial velocity.
(c) Why is Andromeda blueshifted when most galaxies are redshifted?

**Approach:** (a) Interpret the sign. (b) Use v ≈ zc. (c) Gravitational binding.

(a) Negative z means the observed wavelength is shorter than the emitted wavelength. Andromeda is moving toward us.

(b) Since z is very small: v ≈ zc = (−0.0010) × (3.00 × 10⁸) = −3.0 × 10⁵ m/s = −300 km/s. The negative sign indicates approaching motion.

(c) Most galaxies are redshifted because the expansion of the universe carries them away from us. However, Andromeda is only 2.5 million light-years away — close enough that the gravitational attraction between Andromeda and the Milky Way overcomes the cosmic expansion. Andromeda is on a collision course with the Milky Way, expected to merge in about 4.5 billion years.

---

### Example 5: Stellar Rotation

The hydrogen-alpha line (656.3 nm) from opposite edges of the Sun shows a wavelength difference of 0.0082 nm between the approaching and receding limbs. Calculate the rotational speed of the Sun's equator.

**Approach:** The wavelength shift on each limb is Δλ = 0.0041 nm (half the total difference). Use Δλ/λ = v/c.

$\frac{\Delta \lambda}{\lambda} = \frac{v}{c}$

$v = c \times \frac{\Delta \lambda}{\lambda} = 3.00 \times 10^8 \times \frac{0.0041}{656.3} = 3.00 \times 10^8 \times 6.25 \times 10^{-6} = 1875 \text{ m/s} \approx 1.9 \text{ km/s}$

**Why this makes sense:** The Sun's equatorial rotation speed is about 2 km/s. The wavelength shift is tiny — about 6 parts per million — which is why precise spectroscopy is needed.

---

## Practice Problems

### Problem 1
A star's spectrum shows the hydrogen-alpha line at 656.5 nm instead of its rest wavelength of 656.3 nm.
(a) Is the star moving toward or away from Earth? Explain.
(b) Calculate the redshift z.
(c) Estimate the radial velocity of the star using the approximation v = zc.
(d) Calculate the exact velocity using the relativistic formula and compare.

### Problem 2
A distant quasar has a measured redshift of z = 3.0.
(a) Explain what z = 3.0 means in terms of the wavelength shift.
(b) Calculate the recessional velocity using the relativistic formula.
(c) The light we see from this quasar was emitted when the universe was much younger. If the current age is 13.8 billion years, and the quasar's light has been travelling for about 11.5 billion years, how old was the universe when the light was emitted?

### Problem 3
A police radar operates at 24.125 GHz (K-band). It measures a frequency shift of 2.8 kHz from a receding car.
(a) Calculate the speed of the car.
(b) Convert your answer to km/h.
(c) Why is the frequency shift negative for a receding car, but radar guns display positive speed? Explain what the gun actually measures.

### Problem 4
The calcium K-line has a rest wavelength of 393.4 nm. In the spectrum of a binary star system, this line oscillates between 393.1 nm and 393.7 nm with a period of 8.0 days.
(a) Calculate the maximum approach and recession speeds of the star.
(b) If the orbit is circular, what is the orbital speed?
(c) Why does the spectral line oscillate? Draw a simple diagram showing the positions of the star and Earth when the line is at each extreme.

### Problem 5
A galaxy cluster is measured to be at a distance of 200 Mpc. The Hubble constant is 70 km/s/Mpc.
(a) Use Hubble's law to calculate the expected recessional velocity of the cluster.
(b) Calculate the expected redshift z of this cluster.
(c) If the measured z is different from your answer in (b), what might that indicate about the cluster?

### Problem 6 (IB Exam-Style)
The Andromeda Galaxy is approaching the Milky Way at approximately 110 km/s. It is 2.5 × 10⁶ light-years away.
(a) Calculate the blueshift z for Andromeda. [2 marks]
(b) The hydrogen-alpha line from Andromeda is measured in a laboratory at 656.3 nm. Calculate the observed wavelength from Andromeda. [2 marks]
(c) Most galaxies are redshifted. Explain why Andromeda is blueshifted and discuss why this does not contradict the Big Bang theory. [3 marks]

---

## Answers

### Answer 1
(a) The observed wavelength (656.5 nm) is longer than the rest wavelength (656.3 nm). Longer wavelength = redshift = the star is moving away from Earth.

(b) $z = \frac{656.5 - 656.3}{656.3} = \frac{0.2}{656.3} = 3.05 \times 10^{-4}$

(c) $v \approx zc = 3.05 \times 10^{-4} \times 3.00 \times 10^8 = 9.15 \times 10^4 \text{ m/s} = 91.5 \text{ km/s}$

(d) Using the relativistic formula: $v/c = \frac{1.000305^2 - 1}{1.000305^2 + 1} = 3.05 \times 10^{-4}$. The answers are essentially identical because z is very small.

### Answer 2
(a) z = 3.0 means the observed wavelength is 4 times the emitted wavelength: λ' = (1 + 3.0)λ = 4λ. Every spectral line is stretched by a factor of 4.

(b) $\frac{v}{c} = \frac{(1+3)^2 - 1}{(1+3)^2 + 1} = \frac{16-1}{16+1} = \frac{15}{17} = 0.8824$. $v = 0.8824c = 2.65 \times 10^8 \text{ m/s}$.

(c) Universe age at emission = 13.8 − 11.5 = 2.3 billion years. The quasar's light was emitted when the universe was only about 2.3 billion years old.

### Answer 3
(a) $\Delta f = \frac{2vf}{c}$, and for a receding car Δf = −2.8 kHz. $v = \frac{2.8 \times 10^3 \times 3.00 \times 10^8}{2 \times 24.125 \times 10^9} = \frac{8.4 \times 10^{11}}{4.825 \times 10^{10}} = 17.4 \text{ m/s}$.

(b) 17.4 m/s × 3.6 = 62.6 km/h.

(c) The radar gun measures the absolute value of Δf and converts it to speed. The sign tells whether the car approaches or recedes, but the gun displays speed regardless. Modern guns use the phase shift between transmitted and received signals rather than the frequency shift, but the principle is the same.

### Answer 4
(a) At 393.1 nm (blueshift): Δλ = −0.3 nm. v = (0.3/393.4) × 3.00×10⁸ = 2.29×10⁵ m/s = 229 km/s. At 393.7 nm (redshift): Δλ = +0.3 nm. v = 229 km/s away. Maximum speeds are ±229 km/s.

(b) For a circular orbit, the orbital speed is the constant magnitude: 229 km/s. The radial velocity varies sinusoidally between −229 and +229 km/s.

(c) As the star orbits, its velocity component along our line of sight changes. When the star moves directly toward us, we see maximum blueshift. A quarter orbit later, it moves perpendicular to our line of sight (zero radial velocity, λ = rest wavelength). A quarter orbit after that, it moves directly away (maximum redshift). This is why the spectral line oscillates.

### Answer 5
(a) $v = H_0 d = 70 \times 200 = 14,000 \text{ km/s}$.

(b) $z \approx v/c = 14,000 / 3.00 \times 10^5 = 0.0467$.

(c) A different measured z could indicate that the cluster has a **peculiar velocity** — motion relative to the Hubble flow caused by local gravitational interactions (with nearby clusters, superclusters, or large-scale structures). The Hubble flow describes the average expansion; individual galaxies and clusters can deviate from it.

### Answer 6
(a) $z = v/c = −110 / (3.00 × 10^5) = −3.67 × 10^{−4}$. The negative sign indicates blueshift. [2 marks]

(b) $\lambda' = \lambda (1 + z) = 656.3 \times (1 − 3.67 × 10^{−4}) = 656.3 \times 0.999633 = 656.06 \text{ nm}$. [2 marks]

(c) Andromeda is close enough that its gravitational attraction to the Milky Way dominates over cosmic expansion. On small scales, gravity can overcome the Hubble flow. This does not contradict the Big Bang because Hubble's law describes the large-scale average expansion. On local scales (a few Mpc), peculiar velocities from gravitational interactions between galaxies can exceed the Hubble velocity. The Big Bang theory predicts expansion on the largest scales, not that every object moves away from every other. [3 marks]

---

## Key Takeaways

1. **The Doppler effect for light is fundamentally relativistic.** There is no medium, so only the relative velocity matters. All observers measure the speed of light as c.

2. **Redshift (z > 0) means a source is receding; blueshift (z < 0) means a source is approaching.** The parameter z = Δλ/λ quantifies the shift.

3. **The relativistic Doppler formula** is $f' = f \sqrt{(c \pm v)/(c \mp v)}$. For v ≪ c, use Δf/f ≈ ±v/c.

4. **Radar speed guns use the double Doppler shift** — Δf ≈ 2vf/c, with the factor of 2 from the round trip.

5. **Hubble's Law (v = H₀d)** tells us the universe is expanding. The redshift of distant galaxies is cosmological — due to the expansion of space itself, not simple Doppler shift.

6. **Redshift is one of the most powerful tools in astronomy.** It lets us measure velocities, distances, stellar rotation, binary orbits, and detect exoplanets.
