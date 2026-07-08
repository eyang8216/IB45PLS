# Lesson 17: The Greenhouse Effect 2 — Albedo, Emissivity, and the Enhanced Greenhouse Effect

## What You'll Learn

In the previous lesson, you learned that Earth's equilibrium temperature without an atmosphere would be about 255 K (−18°C), but the actual average is 288 K (15°C). This 33 K difference is caused by the greenhouse effect. In this lesson, you will explore how the greenhouse effect actually works at the molecular level, and you'll learn about two critical concepts that refine the energy balance model: **albedo** (reflectivity) and **emissivity** (efficiency of radiation). You will also examine the **enhanced greenhouse effect** — the additional warming caused by human activities that increase the concentration of greenhouse gases in the atmosphere. These concepts connect fundamental physics directly to one of the most important scientific and societal issues of our time.

---

## 1. Albedo: How Much Light Is Reflected

### Why This Matters

When sunlight strikes the Earth, not all of it is absorbed. Some fraction is reflected back into space by clouds, ice, oceans, deserts, and vegetation. This fraction is called the **albedo**, and it plays a crucial role in determining Earth's temperature. Changes in albedo — such as the melting of reflective ice sheets, exposing darker ocean water — can amplify climate change through what scientists call **feedback loops**. Understanding albedo helps us predict how Earth's climate will respond to changes in ice cover, cloud patterns, and land use.

### Key Ideas

The **albedo** (symbol: α, Greek letter "alpha") of a surface or a planet is defined as the fraction of incident electromagnetic radiation that is reflected:

**α = reflected power / incident power**

Albedo is a dimensionless number between 0 and 1 (often expressed as a percentage):
- α = 0: a perfectly absorbing surface (like a black body), reflecting nothing
- α = 1: a perfectly reflecting surface, absorbing nothing
- α = 0.30: reflects 30% of incident radiation, absorbs 70%

The Earth's average albedo is approximately **0.30**, but this varies dramatically across different surfaces:

| Surface | Approximate Albedo |
|---------|-------------------|
| Fresh snow | 0.80 – 0.90 |
| Old snow | 0.50 – 0.70 |
| Ice | 0.30 – 0.50 |
| Desert sand | 0.30 – 0.40 |
| Grassland | 0.15 – 0.25 |
| Forest | 0.05 – 0.15 |
| Ocean (calm) | 0.05 – 0.10 |
| Clouds (thick) | 0.60 – 0.80 |
| Asphalt | 0.05 – 0.10 |

When we calculated Earth's equilibrium temperature in Lesson 16, we used the factor (1 − α) in the absorption term: the fraction of solar radiation that is actually absorbed is (1 − α). For Earth, (1 − 0.30) = 0.70, meaning 70% of incoming solar radiation is absorbed.

**The Ice-Albedo Feedback:**
This is a critical climate concept. As global temperatures rise, ice and snow cover decrease. Since ice and snow have high albedo (they reflect a lot of sunlight), their loss means less sunlight is reflected and more is absorbed by the darker ocean or land beneath. This additional absorbed energy causes further warming, which melts more ice — a positive feedback loop (where "positive" means it amplifies the initial change, not that it is "good").

### Common Misconceptions

> **⚠️ MISCONCEPTION ALERT:** Students often confuse albedo with emissivity. Albedo describes how much incident radiation is **reflected** (primarily in the visible and near-infrared range for solar radiation). Emissivity describes how efficiently a surface **emits** its own thermal radiation (in the infrared for Earth-like temperatures). A surface can have high albedo and high emissivity simultaneously — for example, snow reflects visible sunlight well (high albedo) but also emits infrared radiation efficiently (high emissivity).

> **⚠️ MISCONCEPTION ALERT:** The albedo of Earth is not constant. It changes with seasons (more snow in winter), with cloud cover, and with long-term changes in ice extent. The value 0.30 is a long-term global average.

---

## 2. Emissivity: How Efficiently Objects Radiate

### Why This Matters

Real objects are not perfect black bodies. A polished silver teapot, a rough black rock, and a human body all at the same temperature radiate different amounts of thermal energy. The factor that accounts for this difference is **emissivity** (ε). Understanding emissivity is essential for thermal engineering (designing radiators, heat shields, and spacecraft thermal control) and for accurately modeling Earth's energy balance.

### Key Ideas

**Emissivity** (symbol: ε, Greek letter "epsilon") is defined as the ratio of the power radiated by a surface to the power that would be radiated by a black body at the same temperature:

**ε = power radiated by surface / power radiated by black body at same temperature**

Emissivity is a dimensionless number between 0 and 1:
- ε = 1: a perfect black body, radiating at the maximum possible rate
- ε = 0: a perfect reflector, radiating nothing (this is a theoretical limit)
- Most real surfaces have emissivities between 0.5 and 1.0

The Stefan-Boltzmann law for a real surface becomes:

**P = ε σ A T⁴**

Emissivity depends on the material, its surface finish, and the wavelength of radiation. For the same material at the same temperature, a rough, dark surface typically has higher emissivity than a smooth, shiny surface.

**Kirchhoff's law of thermal radiation** states that for a body in thermal equilibrium, the emissivity equals the absorptivity at each wavelength:
ε(λ) = a(λ)

This means a good absorber at a given wavelength is also a good emitter at that wavelength, and vice versa. A perfect reflector (like a polished metal mirror) has very low emissivity because it does not absorb radiation well — it reflects it instead.

**Important distinction:** Albedo (α) applies to the reflection of incoming radiation (primarily visible sunlight). Emissivity (ε) applies to the emission of the object's own thermal radiation (primarily infrared for objects at Earth-like temperatures). These involve different wavelength ranges, so α and ε can be quite different for the same surface.

### Common Misconceptions

> **⚠️ MISCONCEPTION ALERT:** Students sometimes think that a shiny metal surface, because it "looks reflective," must also be a good radiator in the infrared. In fact, polished metals have very low infrared emissivity (often 0.05 or less). This is why the shiny side of emergency blankets faces inward toward the body — it reflects the body's infrared radiation back, reducing heat loss.

> **⚠️ MISCONCEPTION ALERT:** Emissivity is a property of the **surface**, not the bulk material. A piece of aluminum has different emissivity depending on whether it is polished (ε ≈ 0.05), anodized (ε ≈ 0.80), or painted black (ε ≈ 0.95).

---

## 3. The Greenhouse Effect: How It Actually Works

### Why This Matters

The term "greenhouse effect" is a metaphor, and like many metaphors, it can be misleading. A real greenhouse works primarily by trapping warm air (preventing convection). The atmospheric greenhouse effect works by a completely different mechanism: **selective absorption of infrared radiation by greenhouse gases**. Understanding the actual physics is crucial for understanding climate change.

### Key Ideas

Here is the step-by-step mechanism of the greenhouse effect:

**Step 1:** The Sun emits radiation, primarily in the visible and near-infrared range. The Sun's surface temperature is about 5800 K, so by Wien's law, its peak emission is at visible wavelengths (around 500 nm).

**Step 2:** The Earth's atmosphere is largely transparent to visible light (this is why we can see the Sun). About 70% of the incoming solar radiation reaches the Earth's surface and is absorbed (the rest is reflected by albedo).

**Step 3:** The Earth's surface warms up and emits thermal radiation. Because Earth's surface temperature is about 288 K, this radiation peaks in the infrared (around 10,000 nm or 10 μm, by Wien's law).

**Step 4:** Certain gases in the atmosphere — called **greenhouse gases** — absorb infrared radiation at specific wavelengths. The key greenhouse gases are:
- **Water vapor (H₂O)**: the most abundant greenhouse gas, responsible for about 50% of the natural greenhouse effect
- **Carbon dioxide (CO₂)**: the second most important, responsible for about 20% of the natural effect
- **Methane (CH₄)**
- **Nitrous oxide (N₂O)**
- **Ozone (O₃)**

These gases are not greenhouse gases because of some special chemical property. They are greenhouse gases because their molecular structures allow them to vibrate in ways that match infrared frequencies. Molecules like N₂ and O₂ (which make up 99% of the atmosphere) are **not** greenhouse gases because they are diatomic homonuclear molecules (two identical atoms) — their vibrations do not create changing electric dipole moments, so they cannot absorb or emit infrared radiation efficiently.

**Step 5:** When greenhouse gas molecules absorb infrared photons, they gain vibrational energy. They then re-emit this energy in random directions — some goes upward into space, but some goes back downward toward the Earth's surface. This downward component is the "trapped" energy that warms the surface.

**Step 6:** The surface must now be warmer to radiate enough energy through this partially absorbing atmosphere to balance the incoming solar radiation. The surface temperature rises until the energy radiated to space (after passing through the atmosphere) equals the absorbed solar energy.

The key insight: greenhouse gases do not "trap heat" in the sense of creating a physical barrier. They absorb and re-radiate infrared radiation, with about half of the re-radiation directed back toward the surface. This effectively makes it harder for energy to escape to space, so the surface must heat up to push enough energy through.

### Common Misconceptions

> **⚠️ MISCONCEPTION ALERT:** "The greenhouse effect is like a real greenhouse." No. A real greenhouse works by preventing convection (hot air rising). The atmospheric greenhouse effect works by radiative absorption and re-emission. If you removed the glass from a greenhouse but left a roof that blocks convection, it would still work. If you replaced the Earth's greenhouse gases with a gas that blocks convection but not infrared, the greenhouse effect would vanish.

> **⚠️ MISCONCEPTION ALERT:** "The ozone hole causes global warming." These are separate problems. The ozone hole is about depletion of stratospheric ozone (O₃) by CFCs, which increases ultraviolet radiation reaching the surface. Global warming is about the enhanced greenhouse effect from CO₂ and other gases. While there are some indirect connections, they are fundamentally different issues.

> **⚠️ MISCONCEPTION ALERT:** "CO₂ is the only greenhouse gas" or "CO₂ is the most important greenhouse gas." Water vapor is actually the largest contributor to the natural greenhouse effect. However, human activities directly add CO₂ to the atmosphere, and its concentration is what we are changing. Water vapor acts as a feedback (warmer air holds more water vapor), amplifying the warming caused by CO₂.

---

## 4. The Enhanced Greenhouse Effect

### Why This Matters

The natural greenhouse effect is essential for life on Earth — without it, the planet would be a frozen wasteland at about −18°C. But human activities since the Industrial Revolution have significantly increased the concentration of greenhouse gases in the atmosphere, intensifying the greenhouse effect beyond its natural level. This **enhanced greenhouse effect** is the primary driver of modern climate change.

### Key Ideas

The enhanced greenhouse effect refers to the additional warming caused by increased concentrations of greenhouse gases from human activities:

- **Carbon dioxide (CO₂)**: Pre-industrial levels were about 280 parts per million (ppm). Current levels exceed 420 ppm — a more than 50% increase. Primary sources: burning of fossil fuels (coal, oil, natural gas), deforestation, and cement production.

- **Methane (CH₄)**: Concentrations have more than doubled since pre-industrial times. Primary sources: agriculture (especially livestock and rice paddies), landfills, and natural gas leakage.

- **Nitrous oxide (N₂O)**: Concentrations have increased about 20%. Primary sources: agricultural fertilizers and industrial processes.

The enhanced greenhouse effect shifts the energy balance. More greenhouse gases mean the atmosphere absorbs more outgoing infrared radiation, which means more is re-radiated back to the surface. The surface temperature rises until a new equilibrium is reached where outgoing radiation again balances incoming radiation.

**Quantifying the effect:**
The relationship between greenhouse gas concentration and temperature is complex because of feedback mechanisms. However, the fundamental physics is clear: increased greenhouse gas concentrations reduce the rate at which Earth can radiate energy to space. To restore balance, the Earth's surface must warm.

### Common Misconceptions

> **⚠️ MISCONCEPTION ALERT:** "If the greenhouse effect is natural, how can it be a problem?" The natural greenhouse effect keeps Earth habitable. The enhanced greenhouse effect from human emissions adds to this natural effect, pushing temperatures beyond the range in which human civilization developed. The problem is the rate and magnitude of the additional warming.

> **⚠️ MISCONCEPTION ALERT:** "Climate has always changed, so current warming is natural." While climate has changed naturally throughout Earth's history (due to orbital variations, volcanic activity, etc.), the current warming is occurring far more rapidly than natural cycles and correlates precisely with the industrial-era rise in greenhouse gas concentrations. The physics of greenhouse gas radiative forcing provides the causal mechanism.

---

## 5. Putting It All Together: The Refined Energy Balance Model

### Why This Matters

The simple black-body model from Lesson 16 gave T ≈ 255 K. Now we can refine it by incorporating albedo, emissivity, and the greenhouse effect to understand Earth's actual temperature. This refined model is the foundation of modern climate science.

### Key Ideas

The full energy balance equation for Earth:

**Power absorbed from Sun:**
P_absorbed = S × πR² × (1 − α)

where S ≈ 1360 W/m² and α ≈ 0.30.

**Power radiated by Earth:**
P_radiated = ε × σ × 4πR² × T⁴

where ε ≈ 0.61 is the average infrared emissivity of Earth (accounting for the greenhouse effect — the effective emissivity is less than 1 because greenhouse gases block some outgoing radiation).

At equilibrium:
S × (1 − α) = 4εσT⁴

T = [S(1 − α) / (4εσ)]^(1/4)

With ε = 1 (no greenhouse effect): T ≈ 255 K = −18°C
With ε ≈ 0.61 (including natural greenhouse effect): T ≈ 288 K = 15°C

The difference of 33 K is the natural greenhouse warming. Changes in ε (through changes in greenhouse gas concentrations) change the equilibrium temperature.

Note: In the IB syllabus, you may treat the greenhouse effect in terms of this effective emissivity model, or you may use a simpler layer model. Either approach captures the essential physics: greenhouse gases reduce the net rate at which energy escapes to space, requiring a higher surface temperature for balance.

---

## Worked Examples

### Example 1: Effect of Albedo on Temperature

Imagine Earth's albedo increased from 0.30 to 0.40 (for example, due to increased cloud cover). If all else remains the same, what would the new equilibrium temperature be? Use S = 1360 W/m², σ = 5.67 × 10⁻⁸ W/(m²·K⁴), and assume the greenhouse effect keeps the effective emissivity at ε = 0.61.

**Approach:** Use the refined energy balance equation with the new albedo value.

**Solution:**
T = [S(1 − α) / (4εσ)]^(1/4)

New absorption factor: (1 − α) = (1 − 0.40) = 0.60

T⁴ = 1360 × 0.60 / (4 × 0.61 × 5.67 × 10⁻⁸)
T⁴ = 816 / (1.383 × 10⁻⁷) = 5.90 × 10⁹
T = (5.90 × 10⁹)^(1/4) ≈ 277 K = 4°C

**Why this makes sense:** A 10 percentage point increase in albedo reduces the equilibrium temperature by about 11 K. This illustrates how sensitive climate is to albedo — and why ice-albedo feedback is so important.

---

### Example 2: Comparing Emissivities

Two metal plates of equal area are heated to 400 K. One is polished aluminum with ε = 0.05. The other is painted black with ε = 0.95. Calculate the power radiated per square meter by each plate. Use σ = 5.67 × 10⁻⁸ W/(m²·K⁴).

**Approach:** Use P/A = ε σ T⁴. Calculate separately for each plate.

**Solution:**
σ T⁴ = (5.67 × 10⁻⁸) × (400)⁴

400² = 160,000
400⁴ = 160,000² = 2.56 × 10¹⁰

σ T⁴ = 5.67 × 10⁻⁸ × 2.56 × 10¹⁰ = 5.67 × 2.56 × 10² = 14.52 × 100 = 1452 W/m²

Polished (ε = 0.05): P/A = 0.05 × 1452 = 72.6 W/m²
Black (ε = 0.95): P/A = 0.95 × 1452 = 1379 W/m²

**Why this makes sense:** The black surface radiates about 19 times more power than the polished surface, even though both are at exactly the same temperature. The emissivity makes an enormous difference in radiative heat transfer.

---

### Example 3: Energy Balance with Changing Greenhouse Effect

A simplified climate model treats Earth as having an effective emissivity ε. Currently, ε = 0.61 gives T = 288 K. If human activities increase greenhouse gas concentrations such that ε decreases to 0.58 (more trapping, lower effective emissivity), calculate the new equilibrium temperature. Use S = 1360 W/m², α = 0.30, σ = 5.67 × 10⁻⁸ W/(m²·K⁴).

**Approach:** Keep all parameters the same except ε.

**Solution:**
T_new = [S(1 − α) / (4ε_new σ)]^(1/4)
T_old = [S(1 − α) / (4ε_old σ)]^(1/4)

T_new / T_old = (ε_old / ε_new)^(1/4)
T_new / 288 = (0.61 / 0.58)^(1/4)
0.61 / 0.58 ≈ 1.0517
(1.0517)^(1/4) ≈ 1.0127

T_new ≈ 288 × 1.0127 ≈ 291.7 K ≈ 18.7°C

**Why this makes sense:** A 5% change in effective emissivity produces about a 3 K temperature rise — roughly the magnitude of warming observed over the 20th century. The T ∝ ε^(−1/4) relationship means small changes in ε produce noticeable but not catastrophic changes in T.

---

### Example 4: Albedo Change from Melting Ice

A region of the Arctic Ocean has an area of 1.0 × 10¹² m². Initially, it is covered by ice with an albedo of 0.60. If the ice melts, it becomes open water with an albedo of 0.07. The solar radiation incident on this region averages 200 W/m². Calculate the additional power absorbed due to the albedo change.

**Approach:** Calculate the power absorbed before and after melting. The difference is the additional absorbed power.

**Solution:**
Power absorbed = incident power × (1 − α) × area
Incident power on area = 200 W/m² × 1.0 × 10¹² m² = 2.0 × 10¹⁴ W

Before melting (α = 0.60):
Absorbed = 2.0 × 10¹⁴ × (1 − 0.60) = 2.0 × 10¹⁴ × 0.40 = 8.0 × 10¹³ W

After melting (α = 0.07):
Absorbed = 2.0 × 10¹⁴ × (1 − 0.07) = 2.0 × 10¹⁴ × 0.93 = 1.86 × 10¹⁴ W

Additional absorbed = 1.86 × 10¹⁴ − 8.0 × 10¹³ = 1.06 × 10¹⁴ W

**Why this makes sense:** This is over 100 TW (terawatts) of additional heating — comparable to the total power consumption of human civilization. Even a regional albedo change has enormous energy implications, which is why the ice-albedo feedback is a major concern in climate science.

---

## Practice Problems

### Problem 1
A roof is covered with two different materials. Half has an albedo of 0.80 (white coating) and half has an albedo of 0.10 (dark asphalt). The incident solar radiation is 800 W/m² on a sunny day. Calculate the power absorbed per square meter for each half, and find the overall average albedo of the entire roof.

### Problem 2
A tungsten filament in a light bulb operates at 2800 K. The filament has a surface area of 3.0 × 10⁻⁵ m² and an emissivity of 0.35. Calculate the total power radiated by the filament. Use σ = 5.67 × 10⁻⁸ W/(m²·K⁴).

### Problem 3
A spacecraft in deep space (far from any star) has a surface area of 20 m² and must radiate away 5000 W of internally generated heat to maintain a constant temperature. The spacecraft's surface has an average emissivity of 0.80. Calculate the equilibrium temperature of the spacecraft's surface. Use σ = 5.67 × 10⁻⁸ W/(m²·K⁴).

### Problem 4
Consider a planet identical to Earth in every way except that it has a thicker atmosphere, giving it an effective emissivity of 0.50 instead of Earth's 0.61. Use S = 1360 W/m², α = 0.30, and σ = 5.67 × 10⁻⁸ W/(m²·K⁴). Calculate the equilibrium surface temperature of this planet.

### Problem 5
A student claims: "If Earth's albedo increases due to more clouds, the planet will cool. But if more clouds also trap more infrared radiation, the planet might warm. The net effect depends on which process dominates." Answer the following:
(a) Explain how clouds increase planetary albedo.
(b) Explain how clouds trap infrared radiation.
(c) Describe why low, thick clouds tend to have a net cooling effect while high, thin cirrus clouds tend to have a net warming effect.

### Problem 6 (IB Exam-Style)
The Sun has a surface temperature of 5800 K and a radius of 7.0 × 10⁸ m. It radiates as a black body.

(a) Calculate the total power radiated by the Sun. Use σ = 5.67 × 10⁻⁸ W/(m²·K⁴). [2 marks]

(b) At Earth's orbital distance of 1.5 × 10¹¹ m from the Sun, calculate the intensity (power per unit area) of solar radiation arriving at the top of Earth's atmosphere. This is the solar constant S. [2 marks]

(c) Earth's average albedo is 0.30. Calculate the power absorbed by Earth from the Sun. Earth's radius is 6.4 × 10⁶ m. [3 marks]

(d) Calculate Earth's equilibrium surface temperature assuming: (i) no atmosphere and black-body emission (ε = 1, no greenhouse effect); (ii) an effective emissivity of ε = 0.61 that accounts for the natural greenhouse effect. [3 marks]
