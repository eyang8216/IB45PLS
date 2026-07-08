# Lesson 61: Quantum 2 — Millikan's Experiment, Stopping Potential, and KE_max vs. f

## What You'll Learn

In Lesson 60, you learned that Einstein's photon model explains the photoelectric effect with the equation KE_max = hf − ϕ. But how do we actually MEASURE KE_max? You can't attach a speedometer to an individual electron. The answer is an elegant experimental technique called the stopping potential, perfected by Robert Millikan.

Millikan is one of the great ironies of physics history. He set out to DISPROVE Einstein's photon model — he thought the whole "quantum" idea was nonsense. He spent ten years building the most precise photoelectric experiment ever constructed. And when the data came in, it confirmed Einstein's equation with such precision that Millikan won the 1923 Nobel Prize. Einstein won it in 1921 for the same equation.

This lesson walks you through Millikan's experiment step by step, explains how the stopping potential reveals KE_max, and shows you how to analyze and interpret KE_max vs. f graphs — one of the most commonly tested skills in IB Physics HL.

---

## 1. How Do You Measure the Kinetic Energy of an Electron?

### Why This Matters

The photoelectric equation KE_max = hf − ϕ is central to quantum physics, but without a way to measure KE_max, it's just a theory. The stopping potential technique transforms this equation from speculation into experimentally verifiable science. Understanding this measurement is also essential for interpreting KE_max vs. f graphs, which appear frequently in IB exams.

### The Key Ideas

**The problem.** When light hits a metal and ejects electrons, those electrons fly off in all directions with a range of kinetic energies — from near zero up to KE_max. You can't directly measure the speed or energy of individual electrons in a simple tabletop experiment.

**The solution: an electric brake.** The idea is beautifully simple. Since electrons are negatively charged, they can be slowed down or stopped entirely by an electric field that repels them. If you make the collector slightly negative relative to the emitter, the electrons have to fight against this repulsive voltage. Only electrons with enough kinetic energy can overcome the voltage and reach the collector.

**The stopping potential, defined.** The **stopping potential** (V_s, also written as V₀) is the minimum reverse voltage that reduces the photocurrent to exactly zero. At this voltage, even the MOST energetic electrons — those with KE_max — are just barely stopped before reaching the collector.

The relationship between KE_max and V_s is:

$$K E_{\text{max}} = e V_s$$

where e = 1.60 × 10⁻¹⁹ C is the elementary charge.

**Why this works.** An electron with kinetic energy KE_max is trying to move through a retarding potential V_s. The work done against the electric field is eV_s (the potential energy the electron must overcome). When eV_s = KE_max, the electron comes to rest exactly at the collector surface. When eV_s > KE_max, no electrons reach the collector, and the current is zero.

**The experimental procedure.** For a given frequency of light:
1. Set the voltage to zero and measure the photocurrent (all emitted electrons reach the collector).
2. Gradually increase the reverse (negative) voltage.
3. The photocurrent decreases as fewer electrons have enough energy to overcome the retarding voltage.
4. Record the voltage V_s at which the current just reaches zero.
5. Calculate KE_max = eV_s.
6. Repeat for different frequencies of light.

---

## 2. Millikan's Experiment (1916)

### Why This Matters

Millikan's experiment is a masterpiece of experimental physics. He measured h with an accuracy of about 0.5% — a remarkable achievement for 1916. More importantly, his data showed conclusively that KE_max is a linear function of frequency with a universal slope h, exactly as Einstein predicted. This experiment is often called the definitive confirmation of the photon model.

### The Key Ideas

**The apparatus.** Millikan built an elaborate vacuum chamber containing a rotating wheel with different metal samples (sodium, potassium, lithium) that could be scraped clean under vacuum. Why scrape them? Because the work function of a metal surface is extremely sensitive to contamination — even a monolayer of oxygen or water molecules changes ϕ. By scraping the surface in vacuum, Millikan ensured he was measuring the true work function of the clean metal.

**The light source.** Millikan used a mercury arc lamp combined with a prism monochromator to select individual spectral lines (specific frequencies) of light. He used a range of frequencies from infrared through visible to ultraviolet.

**The measurement.** For each frequency, he measured the photocurrent vs. voltage curve and determined V_s. The key observation: V_s was linearly related to frequency, with the same slope for all metals tested.

**The data.** Plotting KE_max (= eV_s) vs. frequency f for each metal gave a family of parallel straight lines. The slope of each line was experimentally determined as approximately 6.57 × 10⁻³⁴ J·s (Millikan's value; the modern value is 6.63 × 10⁻³⁴ J·s). The x-intercept gave the threshold frequency for each metal.

**The significance of the parallel lines.** The fact that ALL metals gave the SAME slope was crucial. It meant that the slope was a universal constant — Planck's constant h. Different metals had different intercepts (different work functions), but the relationship between photon energy and frequency was the same everywhere. This universality is a hallmark of fundamental physics.

**Millikan's reluctant conclusion.** In his own words, Millikan said he spent ten years testing Einstein's equation "contrary to my own expectation" and found it correct. He still didn't quite believe in photons as a physical reality, but he couldn't deny that the equation KE_max = hf − ϕ fit his data perfectly.

### Common Misconceptions

**"Millikan discovered the value of h."** Max Planck first introduced h in 1900 to explain blackbody radiation. Millikan's contribution was measuring h through an entirely DIFFERENT phenomenon (the photoelectric effect) and obtaining a value consistent with Planck's. This cross-confirmation between blackbody radiation and the photoelectric effect was powerful evidence that h was a real constant of nature, not just a mathematical trick for fitting one type of data.

**"The stopping potential directly measures the work function."** No. The stopping potential measures KE_max = hf − ϕ. To find ϕ, you need to measure V_s at multiple frequencies, plot KE_max vs. f, and extrapolate to f = 0. The y-intercept gives −ϕ (or equivalently, the x-intercept gives f₀ = ϕ/h).

---

## 3. The KE_max vs. f Graph — Deep Analysis

### Why This Matters

The KE_max vs. f graph is one of the most information-rich graphs in IB Physics. IB exam questions frequently ask you to interpret this graph, extract h and ϕ from it, or explain what happens to the graph under various changes. Mastering this graph is essential for exam success.

### The Key Ideas

**The basic graph.** KE_max (y-axis) plotted against frequency f (x-axis) is a straight line:

$$K E_{\text{max}} = h f - \phi$$

This is the equation of a straight line y = mx + c, where:
- y = KE_max
- m = h (slope = Planck's constant)
- x = f (frequency)
- c = −ϕ (y-intercept = negative of the work function)

**Features of the graph:**
- **Slope = h**: Approximately 6.63 × 10⁻³⁴ J·s or 4.14 × 10⁻¹⁵ eV·s (if KE_max is in eV).
- **y-intercept = −ϕ**: Extending the line back to f = 0 gives a negative value equal to −ϕ. (Physically, this is below the x-axis because at f = 0, no photons exist, and the concept of photoelectric emission is meaningless — but mathematically, the line extends there.)
- **x-intercept = f₀**: Where KE_max = 0, we have hf₀ − ϕ = 0, so f₀ = ϕ/h. This is the threshold frequency.

**Multiple metals on the same graph.** When you plot KE_max vs. f for different metals:
- All lines have the SAME slope (same h).
- Different metals have different x-intercepts (different f₀).
- Different metals have different y-intercepts (different −ϕ).
- The lines are PARALLEL — they never cross.

**What the graph tells us:**
1. The relationship is linear — this confirms the photon model.
2. The slope is universal — this confirms Planck's constant is fundamental.
3. Different metals need different minimum frequencies — each has its own work function.
4. Below f₀, KE_max is negative on the graph — physically, this means NO photoemission (the equation doesn't apply below threshold).

**What happens when you change things:**
- **Change metal (different ϕ):** The line shifts parallel to itself. Larger ϕ → line shifts right (larger f₀). Smaller ϕ → line shifts left (smaller f₀).
- **Change intensity:** The graph does NOT change at all. The KE_max vs. f graph does not depend on intensity. Intensity affects photocurrent, which is plotted on a different graph.
- **Change photon model to wave model:** If classical wave theory were correct, KE_max would increase with intensity, not frequency. The graph would be a horizontal line (KE_max constant for a given intensity) — completely different from the experimental result.

### Common Misconceptions

**"The graph passes through the origin."** No. The line crosses the f-axis at f₀, not at f = 0. There is no photoemission (no KE_max) below f₀.

**"The y-intercept represents the work function."** Actually, the y-intercept is NEGATIVE of the work function (−ϕ in joules or eV). Some students incorrectly read the intercept as ϕ. Be careful: the work function ϕ is the MAGNITUDE of the negative intercept.

**"Steeper slope means larger h."** No. The slope IS h, period. You can't change h. If you see a steeper slope on a data plot, it's due to experimental error — h is constant.

---

## 4. Photocurrent vs. Voltage Characteristics

### Why This Matters

While KE_max vs. f tells us about energy, the photocurrent vs. voltage (I-V) characteristic tells us about the number and energy distribution of photoelectrons. Understanding both types of graphs is essential.

### The Key Ideas

**The I-V curve.** Plot photocurrent I (y-axis) against applied voltage V (x-axis) for a fixed frequency and intensity of light.

- At large positive V (anode strongly positive), all emitted electrons are collected. The current saturates at a maximum value (I_sat).
- At V = 0, some electrons still reach the anode (those emitted with enough kinetic energy and in the right direction).
- As V becomes negative, the current decreases.
- At V = −V_s, the current drops to zero.

**What intensity changes.** Increasing intensity (more photons per second) increases I_sat proportionally — more electrons are emitted per second. But V_s is UNCHANGED. The I-V curve shifts upward (higher saturation current) but dies at the SAME stopping potential.

**What frequency changes.** Increasing frequency (more energetic photons) increases V_s — electrons have higher KE_max so a larger reverse voltage is needed to stop them. But I_sat changes only if the intensity (photon flux) also changes.

**This is a key experimental test.** If you change only the intensity and observe that V_s doesn't change, and change only the frequency and observe that V_s does change, you've demonstrated the photon model and ruled out classical wave theory. Classical theory predicts V_s should depend on intensity (wave amplitude), not frequency.

---

## 5. Quantum Efficiency

### Why This Matters

Not every photon that hits a metal surface ejects an electron. Understanding why — and what determines the efficiency — connects the microscopic photon-electron interaction to the macroscopic photocurrent you measure.

### The Key Ideas

**Quantum efficiency (QE)** is the ratio of emitted electrons to incident photons:

$$\text{QE} = \frac{\text{number of photoelectrons emitted}}{\text{number of photons incident}}$$

Typical quantum efficiencies for metal photocathodes range from 0.1% to 10%. Most photons don't produce photoelectrons because:
1. The photon may be absorbed deep inside the metal, and the excited electron loses its energy in collisions before reaching the surface.
2. The electron may be emitted in a direction away from the surface (into the metal).
3. A photon may hit an atom and transfer its energy to an electron that is too tightly bound for even the entire photon energy to free it.

**Why quantum efficiency matters.** Photomultiplier tubes and other photodetectors are designed to maximize QE. Using materials like cesium antimonide (QE up to 25%), these devices can detect single photons — essential for night vision, particle physics detectors, and medical imaging.

---

## Worked Examples

### Example 1: Finding Stopping Potential

Light of frequency 1.20 × 10¹⁵ Hz is incident on a metal with work function 3.20 eV. Calculate the stopping potential.

**Approach:** KE_max = hf − ϕ, then V_s = KE_max/e.

**Step 1:** hf = 6.63 × 10⁻³⁴ × 1.20 × 10¹⁵ = 7.956 × 10⁻¹⁹ J = 4.97 eV.

**Step 2:** KE_max = 4.97 − 3.20 = 1.77 eV.

**Step 3:** V_s = 1.77 V (since KE_max in eV = eV_s in volts).

**Why this makes sense:** The stopping potential is just KE_max expressed in electron-volts, and the numerical value in volts equals the energy in eV. This is by definition: 1 eV is the energy gained by an electron accelerated through 1 V.

---

### Example 2: Extracting h and ϕ from a Graph

A graph of KE_max (in eV) vs. frequency (in 10¹⁴ Hz) for a certain metal shows: slope = 4.14 × 10⁻¹⁵ eV·s, x-intercept = 4.60 × 10¹⁴ Hz. Determine: (a) Planck's constant in eV·s and J·s, (b) the work function in eV, (c) the stopping potential for light of frequency 8.00 × 10¹⁴ Hz.

**Step 1:** h = slope = 4.14 × 10⁻¹⁵ eV·s.
In J·s: h = 4.14 × 10⁻¹⁵ × 1.60 × 10⁻¹⁹ = 6.62 × 10⁻³⁴ J·s. (Close to 6.63 × 10⁻³⁴.)

**Step 2:** ϕ = h × f₀ = 4.14 × 10⁻¹⁵ × 4.60 × 10¹⁴ = 1.904 eV ≈ 1.90 eV.

**Step 3:** KE_max = 4.14 × 10⁻¹⁵ × 8.00 × 10¹⁴ − 1.904 = 3.312 − 1.904 = 1.408 eV.
V_s = 1.41 V.

**Why this makes sense:** The slope in eV·s (4.14 × 10⁻¹⁵) is h/e, which is convenient for plots where KE_max is in eV. The x-intercept gives f₀ directly.

---

### Example 3: Millikan's Data Analysis

In a photoelectric experiment, the following stopping potentials were measured for different frequencies of light incident on potassium:

| f / 10¹⁴ Hz | V_s / V |
|---|---|
| 5.50 | 0.00 |
| 6.50 | 0.41 |
| 8.00 | 1.03 |
| 10.0 | 1.86 |

Determine: (a) Planck's constant in eV·s, (b) the work function of potassium in eV, (c) the threshold wavelength.

**Approach:** KE_max = eV_s. Plot KE_max vs. f (or calculate slope from pairs). Use KE_max = hf − ϕ.

**Step 1:** Let's use the first and last points.
At f = 5.50 × 10¹⁴: KE_max = 0.
At f = 10.0 × 10¹⁴: KE_max = 1.86 eV.
Slope h (in eV·s) = ΔKE/Δf = 1.86 / ((10.0 − 5.50) × 10¹⁴) = 1.86 / (4.50 × 10¹⁴) = 4.133 × 10⁻¹⁵ eV·s.

In J·s: h = 4.133 × 10⁻¹⁵ × 1.60 × 10⁻¹⁹ = 6.61 × 10⁻³⁴ J·s. (Within 0.3% of the accepted value.)

Let's verify with another pair: (6.50, 0.41) and (8.00, 1.03):
ΔKE = 1.03 − 0.41 = 0.62 eV.
Δf = (8.00 − 6.50) × 10¹⁴ = 1.50 × 10¹⁴ Hz.
h = 0.62 / (1.50 × 10¹⁴) = 4.13 × 10⁻¹⁵ eV·s. Consistent.

**Step 2:** ϕ = hf₀ = 4.133 × 10⁻¹⁵ × 5.50 × 10¹⁴ = 2.27 eV.
Check: at f = 6.50 × 10¹⁴: KE_max = 4.133 × 10⁻¹⁵ × 6.50 × 10¹⁴ − 2.27 = 2.686 − 2.27 = 0.416 eV ≈ 0.41 eV. ✓

**Step 3:** λ₀ = c/f₀ = 3.00 × 10⁸ / (5.50 × 10¹⁴) = 5.45 × 10⁻⁷ m = 545 nm (green-yellow).

**Why this makes sense:** Potassium has a low work function and a threshold in the visible range, which is why it (and sodium, and cesium) were used by Millikan — their thresholds are accessible with visible light and don't require ultraviolet.

---

### Example 4: Effect of Intensity on I-V Curve

Light of frequency 8.00 × 10¹⁴ Hz and intensity I₀ shines on a photocell, producing a saturation current of 2.0 μA and stopping potential of 1.0 V. (a) Sketch the I-V curve. (b) On the same axes, sketch the I-V curve if intensity is doubled to 2I₀ but frequency is unchanged. (c) Sketch the I-V curve if intensity stays at I₀ but frequency is increased to 1.00 × 10¹⁵ Hz.

**Approach:** (b) Double intensity → double saturation current, same V_s. (c) Higher frequency → higher V_s, same saturation current (assuming same photon flux).

**(a)** The curve starts at V_s = −1.0 V (I = 0), rises, and saturates at 2.0 μA for large positive V.

**(b)** The new curve has the same V_s = −1.0 V but saturates at 4.0 μA. The curve is vertically stretched but stops at the same negative voltage.

**(c)** For the new frequency: hf = 6.63 × 10⁻³⁴ × 1.00 × 10¹⁵ = 6.63 × 10⁻¹⁹ J = 4.14 eV. KE_max = 4.14 − ϕ. We need ϕ: from part (a), at f = 8.00 × 10¹⁴: hf = 3.31 eV, KE_max = 1.0 eV, so ϕ = 3.31 − 1.0 = 2.31 eV. For new f: KE_max = 4.14 − 2.31 = 1.83 eV, so V_s = 1.83 V. The curve saturates at 2.0 μA (same photon flux assumed) but V_s shifts to −1.83 V.

**Why this makes sense:** Intensity affects the vertical scale (how many electrons), frequency affects the horizontal position of the cutoff (how energetic the electrons are).

---

### Example 5: Checking for Relativistic Effects

An X-ray photon of energy 50.0 keV ejects a photoelectron from a metal. Should relativistic kinematics be used to compute the electron speed?

**Approach:** Calculate the classical speed. If v/c > 0.1, relativistic effects are significant.

**Step 1:** For rough estimate, assume ϕ ≪ 50 keV, so KE_max ≈ 50 keV.
v_classical = √(2KE/m_e) = √(2 × 50 × 10³ × 1.60 × 10⁻¹⁹ / 9.11 × 10⁻³¹)
= √(1.60 × 10⁻¹⁴ / 9.11 × 10⁻³¹) = √(1.756 × 10¹⁶) = 1.33 × 10⁸ m/s.

**Step 2:** v/c = 1.33 × 10⁸ / 3.00 × 10⁸ = 0.44. This is > 0.1, so relativistic effects ARE significant. The actual speed would be less than the classical calculation (because relativistic KE grows faster than v² near c).

**Why this makes sense:** For typical photoelectric experiments with visible or UV light (photon energies 2-6 eV), electron speeds are below 1% of c, and classical kinematics is fine. For X-rays or gamma rays, relativistic corrections are needed.

---

## Practice Problems

### Problem 1
In a photoelectric experiment using calcium, the stopping potential is measured as a function of frequency:

| f / 10¹⁴ Hz | 7.00 | 8.50 | 10.00 | 11.50 |
|---|---|---|---|---|
| V_s / V | 0.24 | 0.86 | 1.48 | 2.10 |

(a) Using these data, determine a value for Planck's constant in J·s. (b) Determine the work function of calcium in eV. (c) Calculate the threshold frequency and threshold wavelength. (d) Predict the stopping potential for light of frequency 9.00 × 10¹⁴ Hz.

### Problem 2
A photocell has a cesium cathode (ϕ = 2.10 eV). It is illuminated with blue light of wavelength 450 nm. (a) Calculate the stopping potential. (b) If the incident power is 5.0 mW and the photocathode area is 2.0 cm², calculate the number of photons arriving per second. (c) If 3.0% of these photons produce photoelectrons, calculate the saturation current. (d) Explain what happens to the stopping potential and saturation current if the wavelength is changed to 380 nm with the same power.

### Problem 3
A graph of KE_max vs. frequency for two metals X and Y shows parallel lines. Metal X has a threshold frequency of 5.0 × 10¹⁴ Hz; metal Y has a threshold frequency of 7.5 × 10¹⁴ Hz. (a) Which metal has the larger work function? Calculate both work functions in eV. (b) If light of frequency 9.0 × 10¹⁴ Hz illuminates both metals, calculate KE_max for each. (c) If the experiment is repeated with the same two metals but using light of twice the intensity, explain how (if at all) the graph would change.

### Problem 4
A student makes the following statement: "The stopping potential depends on the intensity of the light because brighter light has more energy, so it should give electrons more kinetic energy." Identify the error in this statement and explain the correct physics. Reference specific experimental evidence.

### Problem 5
In a Millikan-type experiment, light of wavelength 400 nm produces a stopping potential of 0.80 V for an unknown metal. (a) Calculate the work function of the metal in eV. (b) Light of wavelength 300 nm is then used. Calculate the new stopping potential. (c) Explain, using the photon model, why reducing the wavelength from 400 nm to 300 nm changes the stopping potential, but reducing the intensity of the 400 nm light by half would not.

### Problem 6 (IB Exam Style)
A student investigates the photoelectric effect using a photocell. Monochromatic light of variable frequency f is incident on a metal cathode. The stopping potential V_s is measured for each frequency.

The data is plotted on a graph of V_s against f:

(a) State what is meant by the "stopping potential." [1 mark]

(b) The graph is a straight line. (i) State what the gradient of this line represents. (ii) State what the intercept on the f-axis represents. [2 marks]

(c) The gradient of the line is 4.14 × 10⁻¹⁵ V·s. Show that this value is consistent with Planck's constant h = 6.63 × 10⁻³⁴ J·s. [2 marks]

(d) The intercept on the f-axis is 5.20 × 10¹⁴ Hz. Calculate the work function of the metal in eV. [2 marks]

(e) The experiment is repeated with a different metal that has a larger work function. On a copy of the axes, sketch the expected graph for this second metal alongside the original graph. [2 marks]

(f) The intensity of the light is doubled at one particular frequency. State and explain the effect, if any, on the stopping potential at that frequency. [3 marks]

---

## Answers

### Answer 1
(a) KE_max = eV_s. Use two well-separated points, e.g., f = 7.00 × 10¹⁴ Hz and 11.50 × 10¹⁴ Hz:
ΔKE = e(2.10 − 0.24) = 1.60 × 10⁻¹⁹ × 1.86 = 2.976 × 10⁻¹⁹ J.
Δf = (11.50 − 7.00) × 10¹⁴ = 4.50 × 10¹⁴ Hz.
h = ΔKE/Δf = 2.976 × 10⁻¹⁹ / (4.50 × 10¹⁴) = 6.61 × 10⁻³⁴ J·s.
(Close to 6.63 × 10⁻³⁴; the small difference is from rounding in the data.)

(b) ϕ = hf₀. Find f₀ from interpolation: at V_s = 0, KE_max = 0. Using f = 7.00 at V_s = 0.24, slope = 0.24/0.24 part of the way from f₀ to 7.00. Let's use the equation: V_s = (h/e)f − ϕ/e.
Slope = h/e = 6.63 × 10⁻³⁴ / 1.60 × 10⁻¹⁹ = 4.144 × 10⁻¹⁵ V·s.
At f = 7.00 × 10¹⁴: 0.24 = 4.144 × 10⁻¹⁵ × 7.00 × 10¹⁴ − ϕ/e
ϕ/e = 2.901 − 0.24 = 2.661 V → ϕ = 2.66 eV.

(c) f₀ = ϕ/h = 2.66 × 1.60 × 10⁻¹⁹ / (6.63 × 10⁻³⁴) = 6.42 × 10¹⁴ Hz.
λ₀ = c/f₀ = 3.00 × 10⁸ / (6.42 × 10¹⁴) = 4.67 × 10⁻⁷ m = 467 nm.

(d) V_s = (h/e)f − ϕ/e = 4.144 × 10⁻¹⁵ × 9.00 × 10¹⁴ − 2.661 = 3.730 − 2.661 = 1.069 V ≈ 1.07 V.

### Answer 2
(a) E_photon = hc/λ = 1.989 × 10⁻²⁵ / (450 × 10⁻⁹) = 4.42 × 10⁻¹⁹ J = 2.76 eV.
KE_max = 2.76 − 2.10 = 0.66 eV.
V_s = 0.66 V.

(b) Power per area = 5.0 × 10⁻³ W / (2.0 × 10⁻⁴ m²) = 25 W/m² — but the total power on the cathode is still 5.0 mW.
Power = 5.0 × 10⁻³ J/s.
Photons/s = Power / E_photon = 5.0 × 10⁻³ / (4.42 × 10⁻¹⁹) = 1.13 × 10¹⁶ photons/s.

(c) Electrons/s = 0.030 × 1.13 × 10¹⁶ = 3.39 × 10¹⁴ e⁻/s.
Current = 3.39 × 10¹⁴ × 1.60 × 10⁻¹⁹ = 5.43 × 10⁻⁵ A = 54.3 μA.

(d) At 380 nm: E_photon = hc/λ = 1.989 × 10⁻²⁵ / (380 × 10⁻⁹) = 5.23 × 10⁻¹⁹ J = 3.27 eV.
KE_max = 3.27 − 2.10 = 1.17 eV → V_s = 1.17 V (INCREASES because photons are more energetic).
Number of photons/s: same power 5.0 mW but each photon has more energy, so FEWER photons arrive per second: 5.0 × 10⁻³ / (5.23 × 10⁻¹⁹) = 9.56 × 10¹⁵ photons/s.
Saturation current DECREASES slightly (from 54.3 μA) because fewer photons/s × same QE = fewer electrons/s. But the current might not decrease proportionally because UV typically has higher QE than blue.

**Key point:** Stopping potential increase and saturation current change are independent effects — one depends on photon energy (frequency), the other on photon flux (intensity).

### Answer 3
(a) Y has the larger work function because it has the larger threshold frequency.
ϕ_X = h f₀,X = 6.63 × 10⁻³⁴ × 5.0 × 10¹⁴ = 3.315 × 10⁻¹⁹ J = 2.07 eV.
ϕ_Y = 6.63 × 10⁻³⁴ × 7.5 × 10¹⁴ = 4.973 × 10⁻¹⁹ J = 3.11 eV.

(b) hf = 6.63 × 10⁻³⁴ × 9.0 × 10¹⁴ = 5.967 × 10⁻¹⁹ J = 3.73 eV.
KE_max,X = 3.73 − 2.07 = 1.66 eV.
KE_max,Y = 3.73 − 3.11 = 0.62 eV.

(c) The KE_max vs. f graph would not change at all. Intensity does NOT affect KE_max — it affects the photocurrent (a different graph). The KE_max vs. f relationship depends only on the photon energy (hf) and work function (ϕ), neither of which changes with intensity. The graph for each metal would remain identical.

### Answer 4
The student's statement reflects the classical wave model, not the photon model. The error is in thinking that light energy transfers to electrons continuously — that "brighter" light means more energy available to each electron.

In the photon model:
- Light energy arrives in discrete packets (photons). Each photon has energy hf.
- One photon interacts with one electron, transferring all its energy at once.
- Brighter light means MORE photons per second, not more energetic photons.
- Doubling intensity doubles the NUMBER of photoelectrons (doubles the photocurrent) but does not change the energy of individual photons.
- Each electron still receives hf from a single photon, and KE_max = hf − ϕ is unchanged.

Experimental evidence: Millikan's data shows that V_s depends on frequency, not intensity. For a fixed frequency, changing intensity by a factor of 100 changes the photocurrent by a factor of 100 but leaves V_s unchanged. This is impossible to explain with classical wave theory but is a natural consequence of the photon model.

### Answer 5
(a) E_photon = hc/λ = 1.989 × 10⁻²⁵ / (400 × 10⁻⁹) = 4.973 × 10⁻¹⁹ J = 3.11 eV.
KE_max = eV_s = 0.80 eV.
ϕ = hf − KE_max = 3.11 − 0.80 = 2.31 eV.

(b) E_photon(300nm) = hc/λ = 1.989 × 10⁻²⁵ / (300 × 10⁻⁹) = 6.63 × 10⁻¹⁹ J = 4.14 eV.
KE_max = 4.14 − 2.31 = 1.83 eV.
V_s = 1.83 V.

(c) Reducing wavelength means increasing frequency, which means each photon carries MORE energy (hf increases). Each electron therefore receives more energy from its photon, leaving more as KE_max after paying the work function. The stopping potential must increase.

Reducing intensity means FEWER photons arrive per second, but each photon still has the same energy (same frequency). Each electron that is ejected still gets the same hf from its photon, so KE_max is unchanged. V_s stays the same. Only the photocurrent decreases (fewer electrons per second).

### Answer 6
(a) The stopping potential V_s is the minimum reverse (negative) voltage that must be applied between the cathode and anode to reduce the photocurrent to zero. At this voltage, even the most energetic photoelectrons are just prevented from reaching the collector.

(b) (i) The gradient of the V_s vs. f graph represents h/e, the ratio of Planck's constant to the elementary charge. (Since eV_s = hf − ϕ, dividing by e gives V_s = (h/e)f − ϕ/e.)
(ii) The intercept on the f-axis represents the threshold frequency f₀, below which no photoemission occurs.

(c) Gradient = h/e, so h = gradient × e = 4.14 × 10⁻¹⁵ × 1.60 × 10⁻¹⁹ = 6.624 × 10⁻³⁴ J·s ≈ 6.63 × 10⁻³⁴ J·s. The values are consistent.

(d) ϕ = h f₀ = 6.63 × 10⁻³⁴ × 5.20 × 10¹⁴ = 3.448 × 10⁻¹⁹ J = 2.155 eV ≈ 2.16 eV.
Alternatively: using the gradient, ϕ/e = gradient × f₀ = 4.14 × 10⁻¹⁵ × 5.20 × 10¹⁴ = 2.153 V, so ϕ = 2.15 eV.

(e) The graph would be a straight line PARALLEL to the original (same gradient = h/e, same for all metals) but shifted right — the f-axis intercept would be at a larger frequency (the new metal's higher threshold frequency). The V_s-axis intercept would be more negative (larger −ϕ/e).

(f) Doubling the intensity has NO effect on the stopping potential. The stopping potential measures KE_max, which depends on the photon energy hf (unchanged, since frequency is the same) and the work function ϕ (unchanged, since the metal is the same). KE_max = hf − ϕ is independent of intensity. Intensity affects the number of photons per second, which changes the photocurrent (saturation current) but not the stopping potential. This is a key experimental distinction between the photon model and classical wave theory.

---

## Key Takeaways

1. The stopping potential V_s is the reverse voltage that reduces photocurrent to zero. KE_max = eV_s. This is how we measure the maximum kinetic energy of photoelectrons.

2. Millikan's experiment (1916) measured V_s for multiple frequencies and metals, confirming the linear relationship KE_max = hf − ϕ with universal slope h. This was the definitive experimental validation of Einstein's photon model.

3. The KE_max vs. f graph is a straight line: slope = h (universal), y-intercept = −ϕ, x-intercept = f₀ (threshold frequency). Different metals give parallel lines with different x-intercepts.

4. The photocurrent vs. voltage (I-V) characteristic shows: saturation current proportional to intensity, stopping potential dependent on frequency but NOT intensity.

5. Quantum efficiency is the fraction of incident photons that produce photoelectrons. Typical values are 0.1-10% for metals. Most photons do not eject electrons because energy is lost to collisions or the electron is emitted in the wrong direction.

6. The independence of V_s from intensity is a direct experimental refutation of classical wave theory and a confirmation of the photon model.
