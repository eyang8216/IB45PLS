# Lesson 16: The Greenhouse Effect 1 — Energy Balance and Black-Body Radiation

## What You'll Learn

Every object in the universe emits electromagnetic radiation simply because it has a temperature above absolute zero. The Sun emits visible light that warms the Earth, and the Earth emits infrared radiation back into space. The balance between incoming solar radiation and outgoing terrestrial radiation determines our planet's average temperature. In this lesson, you'll learn about **black-body radiation**, the **Stefan-Boltzmann law**, and how these concepts form the foundation for understanding the greenhouse effect. These ideas are not just physics — they are central to climate science, astrophysics, and the design of thermal imaging systems.

---

## 1. Black-Body Radiation

### Why This Matters

Have you ever seen an electric stove element glow red when hot? That red glow is thermal radiation — electromagnetic waves emitted by the hot metal. Even objects at room temperature emit radiation; you just can't see it because it's in the infrared part of the spectrum, which human eyes cannot detect. This universal property of matter — that all objects with temperature above absolute zero emit electromagnetic radiation — is called **thermal radiation**. Understanding thermal radiation is the first step toward understanding how the Earth maintains its temperature and how the greenhouse effect works.

### Key Ideas

A **black body** is a theoretical object that perfectly absorbs all electromagnetic radiation that falls on it, regardless of wavelength or angle of incidence. The word "black" here does not mean the object looks black to human eyes — a black body at high temperatures glows brightly (like the Sun). It means that the body absorbs all incoming radiation.

Because a black body is a perfect absorber, it is also a perfect emitter. If it absorbed radiation without emitting equally well, its temperature would rise without limit. In thermal equilibrium, the rate of energy absorption equals the rate of energy emission. A black body emits the maximum possible amount of thermal radiation for a given temperature.

**Real objects are not perfect black bodies.** They have an **emissivity** (symbol: ε, Greek letter "epsilon") that ranges from 0 (a perfect reflector that emits nothing) to 1 (a perfect black body). We will explore emissivity in detail in the next lesson. For now, we focus on the ideal black-body case.

The **black-body radiation spectrum** has three crucial properties:

1. **A black body emits radiation at all wavelengths**, but the intensity varies with wavelength in a characteristic curve called the Planck distribution.

2. **The peak wavelength** (the wavelength at which the radiation intensity is maximum) shifts to shorter wavelengths as temperature increases. A warm object (like a human body at ~310 K) peaks in the infrared. A hot object (like the Sun at ~5800 K) peaks in the visible range. This is described by **Wien's displacement law**.

3. **The total power radiated** (summed over all wavelengths) increases dramatically with temperature. This is described by the **Stefan-Boltzmann law**.

### Common Misconceptions

> **⚠️ MISCONCEPTION ALERT:** Many students think a black body is an object that looks black. This is wrong. A black body is a perfect absorber of all radiation. At room temperature, a black body would indeed appear black because it absorbs all visible light and emits mainly infrared (which we cannot see). But a black body at 5800 K glows brilliantly — the Sun is approximately a black body.

> **⚠️ MISCONCEPTION ALERT:** Students sometimes confuse thermal radiation with other forms of heat transfer (conduction and convection). Thermal radiation does not require a medium — it can travel through the vacuum of space. This is how the Sun's energy reaches Earth. Conduction and convection both require matter.

---

## 2. The Stefan-Boltzmann Law

### Why This Matters

How much energy does the Sun radiate each second? How much energy does the Earth radiate back into space? The answers determine our planet's temperature. The Stefan-Boltzmann law quantifies the total power radiated by a black body as a function of its temperature, and it is one of the most important equations in astrophysics and climate science.

### Key Ideas

The **Stefan-Boltzmann law** states that the total power radiated per unit area by a black body is proportional to the fourth power of its absolute temperature:

**P/A = σ T⁴**

where:
- **P** is the radiated power (in watts, W, where 1 W = 1 J/s)
- **A** is the surface area of the radiating body (in m²)
- **σ** (Greek letter "sigma") is the Stefan-Boltzmann constant: **σ = 5.67 × 10⁻⁸ W/(m²·K⁴)**
- **T** is the absolute temperature (in kelvin, K)

You can find σ in your IB Data Booklet.

Multiplying both sides by A gives the total power:

**P = σ A T⁴**

For a real object that is not a perfect black body, we multiply by the emissivity ε:

**P = ε σ A T⁴**

The T⁴ dependence is extremely strong. If you double the absolute temperature, the radiated power increases by a factor of 2⁴ = 16. A small temperature increase produces a large increase in radiated power. This has profound implications for climate: a small rise in Earth's average temperature produces a much larger increase in the rate at which Earth radiates energy to space.

**Important note about the Stefan-Boltzmann constant:** The value 5.67 × 10⁻⁸ has been chosen so that when T is in kelvin and A is in m², P comes out in watts. The units W/(m²·K⁴) look unusual, but they make the equation dimensionally consistent.

### Common Misconceptions

> **⚠️ MISCONCEPTION ALERT:** Students often plug temperatures in °C into the Stefan-Boltzmann law. The T in T⁴ must be in **kelvin**. Using °C gives nonsensical results (and negative values raised to the fourth power for temperatures below 0°C).

> **⚠️ MISCONCEPTION ALERT:** The area A in the Stefan-Boltzmann law is the **surface area** of the radiating object, not its cross-sectional area. For a sphere of radius R, A = 4πR². We'll see later that when calculating the power absorbed from the Sun, the relevant area is the cross-sectional area πR² — this distinction is a common source of confusion.

---

## 3. Energy Balance: Why the Earth Has Its Temperature

### Why This Matters

The Earth absorbs energy from the Sun and radiates energy back into space. The Earth's average temperature is the temperature at which these two rates balance — energy in equals energy out. This is the fundamental principle of planetary energy balance. Without this balance, the Earth would either heat up indefinitely (if absorption exceeded emission) or cool to near absolute zero (if emission exceeded absorption).

### Key Ideas

To calculate the Earth's equilibrium temperature, we need two expressions:

**Power absorbed from the Sun:**
The Sun radiates power P_sun = σ × (surface area of Sun) × T_sun⁴. This power spreads uniformly in all directions. By the time it reaches Earth (at distance d, the Earth-Sun distance), it is spread over the surface area of a sphere of radius d: 4πd².

The **solar constant** S is the solar power per unit area arriving at Earth's orbital distance:
S = P_sun / (4πd²)

At Earth's distance, S ≈ 1360 W/m². This is the power that would strike a 1 m² surface held perpendicular to the Sun's rays at Earth's distance (above the atmosphere).

The Earth intercepts solar radiation over its cross-sectional area πR² (the area of the circular shadow it casts), not its full surface area. This is because the Earth is a sphere and only one side faces the Sun at any moment.

Power absorbed = S × πR² × (1 − α)

where α (Greek letter "alpha") is the **albedo**, the fraction of incoming radiation that is reflected back into space without being absorbed. Earth's average albedo is about 0.30 (30%).

**Power radiated by the Earth:**
If the Earth behaved as a black body at temperature T, it would radiate from its entire surface area (4πR²):

Power radiated = σ × 4πR² × T⁴

**At equilibrium:**
Power absorbed = Power radiated
S × πR² × (1 − α) = σ × 4πR² × T⁴

The πR² cancels (it appears on both sides), and we can solve for T:

S × (1 − α) = 4σ T⁴
T⁴ = S(1 − α) / (4σ)
T = [S(1 − α) / (4σ)]^(1/4)

Let's plug in approximate values (for conceptual understanding; you would use exact values on an exam):

S ≈ 1360 W/m², α = 0.30, σ = 5.67 × 10⁻⁸ W/(m²·K⁴)

T⁴ = 1360 × 0.70 / (4 × 5.67 × 10⁻⁸)
T⁴ = 952 / (2.268 × 10⁻⁷)
T⁴ ≈ 4.20 × 10⁹
T ≈ (4.20 × 10⁹)^(1/4) ≈ 255 K

The calculated temperature is about 255 K, which is −18°C. But the Earth's actual average surface temperature is about 288 K (15°C). The difference — about 33 K — is due to the **greenhouse effect**. The Earth's atmosphere traps some of the outgoing infrared radiation, so the surface must be warmer to radiate enough energy through the atmosphere to balance the incoming solar radiation.

### Common Misconceptions

> **⚠️ MISCONCEPTION ALERT:** Students sometimes think the Earth's cross-sectional area for absorbing sunlight is half the surface area (2πR²) because "only half the Earth faces the Sun." But the Sun's rays arrive as parallel beams (the Sun is very far away), so the Earth intercepts radiation over a circle of radius R, giving area πR². Think of the Earth's shadow on a screen behind it — it's a circle, not a hemisphere.

> **⚠️ MISCONCEPTION ALERT:** Many students ask why we use 4πR² for emission but πR² for absorption. The Earth absorbs over the side facing the Sun (effectively a disk), but radiates from its entire surface in all directions (a sphere).

---

## 4. Wien's Displacement Law

### Why This Matters

Why does a hot star look blue-white while a cooler star looks red? Why do infrared cameras "see" warm objects in the dark? The answer is Wien's displacement law, which relates the peak wavelength of thermal radiation to the temperature of the emitting body. This law is used in astronomy to determine the surface temperature of stars, in thermal imaging to map temperature distributions, and in the design of light bulbs.

### Key Ideas

**Wien's displacement law** states that the wavelength at which a black body's radiation spectrum peaks is inversely proportional to its absolute temperature:

**λ_max × T = 2.90 × 10⁻³ m·K**

where:
- **λ_max** (lambda-max) is the peak wavelength (in meters)
- **T** is the absolute temperature (in kelvin)
- **2.90 × 10⁻³ m·K** is Wien's displacement constant (found in the IB Data Booklet)

This law means: the hotter the object, the shorter the peak wavelength. The "displacement" in the name refers to how the peak of the spectrum shifts (displaces) as temperature changes.

**Examples:**
- The Sun (T ≈ 5800 K): λ_max = (2.90 × 10⁻³) / 5800 ≈ 5.0 × 10⁻⁷ m = 500 nm. This is green-yellow light, near the peak sensitivity of human vision (not a coincidence — our eyes evolved to use the most abundant wavelengths).
- A human body (T ≈ 310 K): λ_max = (2.90 × 10⁻³) / 310 ≈ 9.4 × 10⁻⁶ m = 9400 nm. This is deep in the infrared, which is why thermal cameras detect us in complete darkness.
- The cosmic microwave background (T ≈ 2.73 K): λ_max ≈ 1.06 × 10⁻³ m = 1.06 mm. This is in the microwave region, which is why it was discovered by radio astronomers.

### Common Misconceptions

> **⚠️ MISCONCEPTION ALERT:** Students often think Wien's law gives the only wavelength emitted. It gives the **peak** wavelength. A black body emits at ALL wavelengths, just less intensely away from the peak. The Sun emits infrared and ultraviolet as well as visible light.

> **⚠️ MISCONCEPTION ALERT:** λ_max × T = constant means λ_max ∝ 1/T. If T is halved, λ_max doubles. Students sometimes invert this relationship.

---

## Worked Examples

### Example 1: Power Radiated by the Sun

The Sun has a surface temperature of approximately 5800 K and a radius of 7.0 × 10⁸ m. Estimate the total power radiated by the Sun, treating it as a black body. Use σ = 5.67 × 10⁻⁸ W/(m²·K⁴).

**Approach:** Use the Stefan-Boltzmann law P = σ A T⁴. A is the Sun's surface area: A = 4πR².

**Solution:**
A = 4π(7.0 × 10⁸)² = 4π × 4.9 × 10¹⁷ ≈ 6.16 × 10¹⁸ m²
T⁴ = (5800)⁴ = 5800² × 5800² = 3.364 × 10⁷ × 3.364 × 10⁷ ≈ 1.13 × 10¹⁵ K⁴

P = σ A T⁴ = (5.67 × 10⁻⁸) × (6.16 × 10¹⁸) × (1.13 × 10¹⁵)
P ≈ 3.95 × 10²⁶ W

**Why this makes sense:** The accepted value for the Sun's luminosity is about 3.83 × 10²⁶ W. Our approximate calculation gives a value very close to this, confirming that the Sun approximates a black body quite well.

---

### Example 2: Peak Wavelength of a Star

The star Betelgeuse (in the constellation Orion) has a surface temperature of approximately 3500 K. Calculate the peak wavelength of its radiation. In what part of the electromagnetic spectrum does this peak lie? Use the Wien constant = 2.90 × 10⁻³ m·K.

**Approach:** Apply Wien's displacement law: λ_max = (2.90 × 10⁻³) / T.

**Solution:**
λ_max = (2.90 × 10⁻³) / 3500 = 8.29 × 10⁻⁷ m = 829 nm

This is in the infrared region (visible light ranges from about 400 nm to 700 nm). However, the spectrum is broad, so Betelgeuse emits significantly in the red part of the visible spectrum, which is why it appears as a distinctly red star in the night sky.

**Why this makes sense:** Cooler stars peak at longer wavelengths, appearing red. Hotter stars peak at shorter wavelengths, appearing blue-white. Our Sun (5800 K) peaks in the green-yellow, appearing white to our eyes.

---

### Example 3: Comparing Radiated Power at Different Temperatures

A metal sphere is heated from 300 K to 600 K. By what factor does the total radiated power increase? Assume the sphere behaves as a black body.

**Approach:** The power is proportional to T⁴. Calculate the ratio P₂/P₁ = (T₂/T₁)⁴.

**Solution:**
P₂/P₁ = (T₂/T₁)⁴ = (600/300)⁴ = 2⁴ = 16

The radiated power increases by a factor of 16 when the temperature in kelvin is doubled.

**Why this makes sense:** The T⁴ dependence is extremely steep. Even modest temperature increases dramatically increase radiative output. This is why hot objects glow visibly while warm objects only emit infrared — the power at visible wavelengths increases enormously with temperature.

---

### Example 4: Earth's Equilibrium Temperature Without Atmosphere

Calculate the equilibrium temperature of Earth assuming no atmosphere (i.e., no greenhouse effect) and an albedo of 0.30. Use S = 1360 W/m² and σ = 5.67 × 10⁻⁸ W/(m²·K⁴). Express your answer in both kelvin and °C.

**Approach:** Use the energy balance equation T = [S(1 − α) / (4σ)]^(1/4).

**Solution:**
S(1 − α) = 1360 × (1 − 0.30) = 1360 × 0.70 = 952 W/m²
4σ = 4 × 5.67 × 10⁻⁸ = 2.268 × 10⁻⁷ W/(m²·K⁴)

T⁴ = 952 / (2.268 × 10⁻⁷) = 4.197 × 10⁹ K⁴
T = (4.197 × 10⁹)^(1/4)

To evaluate the fourth root: 10⁹ = (10²·²⁵)⁴ ≈ (177.8)⁴, so (10⁹)^(1/4) = 10^(9/4) = 10^2.25 ≈ 177.8

T ≈ 177.8 × (4.197)^(1/4) ≈ 177.8 × 1.43 ≈ 254 K

In °C: T = 254 − 273 = −19°C

**Why this makes sense:** This temperature is well below freezing, confirming that Earth would be a frozen planet without the greenhouse effect. The actual average surface temperature is about 288 K (15°C), showing a 34 K greenhouse warming. (Note: the exact answer using more precise arithmetic is about 255 K or −18°C.)

---

### Example 5: Temperature from Peak Wavelength

In a laboratory, a heated filament is observed to emit thermal radiation that peaks at a wavelength of 1.45 × 10⁻⁶ m. Calculate the temperature of the filament. Use Wien's constant = 2.90 × 10⁻³ m·K.

**Approach:** Rearrange Wien's law: T = (2.90 × 10⁻³) / λ_max.

**Solution:**
T = (2.90 × 10⁻³) / (1.45 × 10⁻⁶) = 2000 K

**Why this makes sense:** A filament at 2000 K glows with a warm yellow-orange color. The peak is in the infrared (1450 nm), but the visible portion of the spectrum is strong enough to produce visible light. Traditional incandescent light bulbs operate at similar temperatures.

---

## Practice Problems

### Problem 1
A spherical piece of charcoal of radius 0.050 m is heated to 1000 K in a furnace. Treating the charcoal as a black body, calculate the total power it radiates. Use σ = 5.67 × 10⁻⁸ W/(m²·K⁴). Give your answer in watts.

### Problem 2
The star Sirius has a surface temperature of approximately 9900 K. Calculate the peak wavelength of its radiation using Wien's displacement law (constant = 2.90 × 10⁻³ m·K). In what part of the spectrum does this peak lie? Explain why Sirius appears bluish-white to the naked eye.

### Problem 3
A black-body radiator emits a total power of 100 W at a temperature of 500 K. The temperature is then increased to 1000 K while all other conditions remain the same. Calculate the new total radiated power.

### Problem 4
A planet orbits a star at a distance where the stellar radiation intensity (the "solar constant" for that planet) is 2000 W/m². The planet has an albedo of 0.40 and no atmosphere. Calculate the equilibrium surface temperature of the planet. Use σ = 5.67 × 10⁻⁸ W/(m²·K⁴).

### Problem 5
The human body has a skin temperature of approximately 34°C and an emissivity of about 0.97. The surface area of an average adult human is about 1.8 m². Calculate the net power radiated by the body when the surroundings are at 20°C. Give your answer in watts. Use σ = 5.67 × 10⁻⁸ W/(m²·K⁴).

### Problem 6 (IB Exam-Style)
The star Rigel has a surface temperature of 12,000 K and a luminosity (total radiated power) of 5.1 × 10³¹ W. It is approximately spherical.

(a) Using Wien's displacement law (constant = 2.90 × 10⁻³ m·K), calculate the peak wavelength of Rigel's radiation. State the region of the electromagnetic spectrum in which this peak is found. [2 marks]

(b) Assuming Rigel radiates as a black body, calculate the radius of Rigel. Use σ = 5.67 × 10⁻⁸ W/(m²·K⁴). [3 marks]

(c) The radius of the Sun is 7.0 × 10⁸ m. Express the radius of Rigel in terms of solar radii. [1 mark]

(d) A planet orbits Rigel at a distance of 2.5 × 10¹² m. Calculate the intensity of Rigel's radiation at this distance (the "solar constant" for this planet). [2 marks]

(e) This planet has an albedo of 0.25 and no greenhouse effect. Calculate its equilibrium temperature. [2 marks]

---

## Answers

### Answer 1
Surface area of sphere: A = 4πr² = 4π(0.050)² = 4π × 0.0025 = 0.0314 m²
P = σ A T⁴ = (5.67 × 10⁻⁸) × 0.0314 × (1000)⁴
(1000)⁴ = 10¹²
P = (5.67 × 10⁻⁸) × 0.0314 × 10¹² = 5.67 × 0.0314 × 10⁴ = 5.67 × 314 = 1780 W

The charcoal radiates approximately 1800 W. This is a significant amount of power — comparable to a space heater — from a sphere only 10 cm across, illustrating the dramatic T⁴ dependence.

---

### Answer 2
λ_max = (2.90 × 10⁻³) / 9900 = 2.93 × 10⁻⁷ m = 293 nm.

This is in the ultraviolet region (UV ranges from about 10 nm to 400 nm). Sirius appears bluish-white because even though the peak is in the UV, the spectrum is very broad. The star emits intensely across the visible range, but more intensely at the blue end (short wavelengths) than at the red end (long wavelengths). This gives it a characteristic blue-white color.

---

### Answer 3
P ∝ T⁴, so P_new / P_old = (T_new / T_old)⁴ = (1000 / 500)⁴ = 2⁴ = 16.
P_new = 16 × 100 = 1600 W.

The power increases by a factor of 16 when the absolute temperature doubles.

---

### Answer 4
T = [S(1 − α) / (4σ)]^(1/4)
S(1 − α) = 2000 × 0.60 = 1200 W/m²
T⁴ = 1200 / (4 × 5.67 × 10⁻⁸) = 1200 / (2.268 × 10⁻⁷) = 5.29 × 10⁹
T = (5.29 × 10⁹)^(1/4)

(10⁹)^(1/4) = 10^(9/4) ≈ 177.8
(5.29)^(1/4) ≈ 1.52
T ≈ 177.8 × 1.52 ≈ 270 K

The equilibrium temperature is about 270 K (or −3°C). This is warmer than Earth's no-atmosphere temperature because the star provides more intense radiation.

---

### Answer 5
Body temperature: T_body = 34 + 273 = 307 K
Surroundings: T_surr = 20 + 273 = 293 K

The net power radiated is the difference between power emitted and power absorbed:
P_net = εσA(T_body⁴ − T_surr⁴)

T_body⁴ = (307)⁴ ≈ 8.88 × 10⁹ K⁴
T_surr⁴ = (293)⁴ ≈ 7.37 × 10⁹ K⁴
Difference = 1.51 × 10⁹ K⁴

P_net = 0.97 × (5.67 × 10⁻⁸) × 1.8 × 1.51 × 10⁹
P_net = 0.97 × 5.67 × 1.8 × 1.51 × 10¹
P_net ≈ 149 W

The body radiates a net power of about 150 W. This is similar to the metabolic heat generated by a resting adult, which is why rooms at 20°C feel comfortable — they allow us to dissipate our metabolic heat at the right rate.

---

### Answer 6

**(a)** λ_max = (2.90 × 10⁻³) / 12,000 = 2.42 × 10⁻⁷ m = 242 nm. This is in the ultraviolet region. [2 marks]

**(b)** P = σ A T⁴, so A = P / (σT⁴)
T⁴ = (12,000)⁴ = (1.2 × 10⁴)⁴ = 2.0736 × 10¹⁶ K⁴
A = 5.1 × 10³¹ / (5.67 × 10⁻⁸ × 2.0736 × 10¹⁶)
A = 5.1 × 10³¹ / (1.176 × 10⁹) = 4.34 × 10²² m²

For a sphere, A = 4πR², so R = √(A / 4π) = √(4.34 × 10²² / 12.57) = √(3.45 × 10²¹) ≈ 5.87 × 10¹⁰ m [3 marks]

**(c)** R_Rigel / R_Sun = 5.87 × 10¹⁰ / 7.0 × 10⁸ ≈ 84 solar radii. Rigel is a supergiant star, about 84 times wider than the Sun. [1 mark]

**(d)** At distance d, power is spread over area 4πd²:
I = P / (4πd²) = 5.1 × 10³¹ / (4π × (2.5 × 10¹²)²)
= 5.1 × 10³¹ / (4π × 6.25 × 10²⁴)
= 5.1 × 10³¹ / (7.85 × 10²⁵) ≈ 6.5 × 10⁵ W/m²

The intensity is about 650,000 W/m² — nearly 500 times Earth's solar constant. [2 marks]

**(e)** T = [I(1 − α) / (4σ)]^(1/4)
I(1 − α) = 6.5 × 10⁵ × 0.75 = 4.875 × 10⁵ W/m²
T⁴ = 4.875 × 10⁵ / (2.268 × 10⁻⁷) = 2.15 × 10¹²
T = (2.15 × 10¹²)^(1/4) ≈ 1210 K

The planet is extremely hot — about 940°C. This is far too hot for liquid water, illustrating why habitable planets must orbit at the right distance from their stars. [2 marks]

---

## Key Takeaways

1. **Thermal radiation** is electromagnetic radiation emitted by all objects with temperature above absolute zero. It does not require a medium to travel.

2. A **black body** is a perfect absorber and perfect emitter of radiation. The Sun and other stars are approximately black bodies.

3. The **Stefan-Boltzmann law** (P = σAT⁴) relates the total power radiated to the absolute temperature. The T⁴ dependence means a small temperature change produces a large change in radiative output.

4. **Wien's displacement law** (λ_max T = 2.90 × 10⁻³ m·K) relates the peak wavelength to temperature. Hotter objects peak at shorter wavelengths.

5. The Earth's **energy balance** — absorbed solar radiation equals emitted terrestrial radiation — determines the planet's average temperature. The calculation yields about 255 K without greenhouse effect.

6. The difference between the calculated 255 K and the actual 288 K (about 33 K) is due to the **greenhouse effect**, which traps some outgoing infrared radiation.
