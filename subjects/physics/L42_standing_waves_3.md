# Lesson 42: Standing Waves III — Advanced & Energy (HL)

## What You'll Learn
- The standing wave equation: y = 2A cos(kx) sin(ωt)
- Energy in standing waves — no net energy transfer
- Standing waves in 2D: Chladni plates
- Acoustic resonance and Helmholtz resonators
- Physics of musical instruments

---

## 1. The Standing Wave Equation

### Derivation (Recap)

A standing wave is the superposition of two identical travelling waves moving in opposite directions:

**Wave travelling right:** y₁ = A sin(kx − ωt)
**Wave travelling left:** y₂ = A sin(kx + ωt) _(reflected with π phase change, equivalent to −A sin(kx + ωt) at a fixed end)_

For a string fixed at x = 0, the reflected wave is inverted: y₂ = −A sin(−kx − ωt)... but the general result is:

$$y = y_1 + y_2 = 2A \cos(kx) \sin(\omega t)$$

### Interpretation

- **2A cos(kx)** — the **spatial amplitude envelope**. At any position x, the maximum displacement (over time) is |2A cos(kx)|.
- **sin(ωt)** — the **temporal oscillation**. All positions oscillate at the same angular frequency ω (but possibly with different amplitudes and sign).

### Key Features

| Feature | Mathematical Condition | Physical Meaning |
|---------|----------------------|------------------|
| Node | cos(kx) = 0 | Zero displacement at all t |
| Antinode | |cos(kx)| = 1 | Maximum displacement ±2A |
| Node positions | x = (2m+1)λ/4, m = 0,1,2... | Nodes spaced λ/2 apart |
| Antinode positions | x = mλ/2, m = 0,1,2... | Antinodes spaced λ/2 apart |

### Phase

Within one "loop" (between consecutive nodes), cos(kx) has the same sign — all points move **in phase**. Across a node, cos(kx) flips sign — points move **in antiphase**.

---

## 2. Energy in Standing Waves

### The Critical Insight

In a **travelling wave**, energy propagates — each particle transfers energy to the next, and energy moves through the medium.

In a **standing wave**, **no net energy is transferred!** Energy is trapped between nodes.

### Why?

- At a **node**, the string never moves (v = 0 always), so no energy passes through a node.
- Energy oscillates between kinetic (when string is moving fast through equilibrium) and elastic potential (when string is maximally stretched at the extremes).
- This is analogous to energy oscillating between KE and PE in a mass-spring system.

### Energy Distribution

- **Antinodes:** Both KE and elastic PE are maximum (alternately, not simultaneously). At equilibrium position, KE is max; at extremes, PE is max.
- **Nodes:** KE is always zero (no displacement → no velocity). PE is zero because adjacent segments don't stretch the string at a node.
- **Between nodes:** Energy sloshes back and forth but never crosses a node.

### Comparison

| | Travelling Wave | Standing Wave |
|---|---|---|
| Energy flow | Energy propagates at wave speed | No net energy transfer |
| Energy at nodes | Energy passes through | Energy never passes through |
| Medium behaviour | Each particle slightly delayed from neighbour | Particles in same loop move in phase |

---

## 3. Standing Waves in Two Dimensions — Chladni Plates

When a flat plate is vibrated (e.g., by a violin bow or speaker), 2D standing wave patterns appear. Sand sprinkled on the plate collects along **nodal lines** (where there is no vibration), creating beautiful geometric patterns.

### Characteristics

- Nodal **lines** (instead of nodal points in 1D)
- Patterns depend on:
  - Plate shape (square, circular, etc.)
  - Frequency of vibration
  - Where the plate is held/clamped
- Higher frequencies → more complex patterns → more nodal lines

### IB Connection

Chladni plates demonstrate that standing waves are not limited to 1D — the same principles of nodes (zero displacement) and antinodes (maximum displacement) extend to 2D and 3D.

---

## 4. Acoustic Resonance

### What is Acoustic Resonance?

When a sound wave encounters a cavity or object with a natural frequency matching the sound frequency, the amplitude builds dramatically. This is the same resonance principle as pushing a swing at the right moment.

### Examples

| System | Description |
|--------|-------------|
| **Organ pipe** | Air column resonates at harmonic frequencies |
| **Guitar body** | Hollow body resonates, amplifying string vibrations |
| **Room modes** | Rooms have resonant frequencies based on dimensions |
| **Helmholtz resonator** | A cavity with a neck — resonates at a single frequency |

---

## 5. The Helmholtz Resonator

A **Helmholtz resonator** is a rigid cavity with a narrow neck. When you blow across the neck (like a bottle), the air in the neck acts as a mass, and the air in the cavity acts as a spring.

### Resonant Frequency

$$f = \frac{v}{2\pi}\sqrt{\frac{A}{V L_{\text{neck}}}}$$

where:
- v = speed of sound in air
- A = cross-sectional area of the neck
- V = volume of the cavity
- L_neck = length of the neck (including end correction, L_eff ≈ L_neck + 1.7r for flanged end)

### Simplified Bottle Formula

For a bottle with neck area A, neck length L_n, and cavity volume V:

$$f = \frac{v}{2\pi}\sqrt{\frac{A}{V L_{\text{eff}}}}$$

### Real-World Examples

- Blowing across a bottle top
- Bass-reflex speaker ports
- Car exhaust mufflers
- Some musical instruments (ocarina)

---

## 6. Musical Instruments Physics

### String Instruments (Guitar, Violin, Piano)

- **Source:** Vibrating string
- **Harmonics:** Full series (n = 1,2,3...)
- **Frequency control:** f ∝ 1/L (finger position), f ∝ √T (tuning pegs), f ∝ 1/√μ (string thickness)
- **Amplification:** Soundboard/body resonance
- **Timbre:** Mix of harmonics (not just fundamental)

### Wind Instruments — Open Pipes (Flute, Recorder)

- **Source:** Vibrating air column
- **Harmonics:** Full series
- **Frequency control:** Opening/closing holes changes effective L
- **Overblowing:** Excites higher harmonics

### Wind Instruments — Closed Pipes (Clarinet)

- **Source:** Vibrating air column
- **Harmonics:** Odd only! (n = 1,3,5...)
- **Frequency control:** Keys change effective L
- **Register key:** Opens a small hole near the mouthpiece, forcing the pipe to behave as open → jumps to 3rd harmonic (a 12th higher, not just an octave!)

### Brass Instruments (Trumpet, Trombone)

- **Source:** Lips buzzing (drives mouthpiece)
- **Harmonics:** Closed-pipe-like behaviour (odd) modified by bell flare
- **Frequency control:** Valves/slide change L; lip tension selects harmonic

### Percussion (Drums, Xylophone)

- **Source:** Membrane or bar vibration
- **Harmonics:** Usually **non-harmonic** — frequencies are not simple multiples
- **Pitch clarity:** Varies; xylophone bars are undercut for harmonic tuning

---

## Worked Examples

### Worked Example 42.1 — Standing Wave Equation Analysis

**Problem:** The standing wave on a string is described by:
y = 0.050 cos(4.0x) sin(120t)  *(SI units)*

Find:
(a) the amplitude of each original travelling wave
(b) the wavelength
(c) the frequency
(d) the positions of the first three nodes from x = 0

**Solution:**

Comparing to y = 2A cos(kx) sin(ωt):

**(a)** 2A = 0.050 → **A = 0.025 m** (each travelling wave amplitude is 2.5 cm)

**(b)** k = 4.0 rad/m. λ = 2π/k = 2π/4.0 = **1.57 m**

**(c)** ω = 120 rad/s. f = ω/(2π) = 120/(2π) = **19.1 Hz**

**(d)** Nodes: cos(kx) = 0 → kx = π/2, 3π/2, 5π/2...
- x₁ = (π/2)/4.0 = **0.393 m**
- x₂ = (3π/2)/4.0 = **1.18 m**
- x₃ = (5π/2)/4.0 = **1.96 m**

---

### Worked Example 42.2 — Bottle Resonant Frequency

**Problem:** A glass bottle has a cavity volume of 500 cm³ and a neck of length 5.0 cm with diameter 2.0 cm. The speed of sound is 340 m/s. Estimate the resonant frequency (blowing across the top).

**Solution:**

Convert to SI:
- V = 500 cm³ = 5.0 × 10⁻⁴ m³
- r = 1.0 cm = 0.010 m, A = πr² = π × (0.010)² = 3.14 × 10⁻⁴ m²
- L_neck = 0.050 m
- End correction for flanged end: L_eff ≈ L_neck + 1.7r = 0.050 + 1.7(0.010) = 0.067 m

$$f = \frac{v}{2\pi}\sqrt{\frac{A}{V L_{\text{eff}}}} = \frac{340}{2\pi}\sqrt{\frac{3.14 \times 10^{-4}}{5.0 \times 10^{-4} \times 0.067}}$$

$$f = \frac{340}{6.28}\sqrt{\frac{3.14 \times 10^{-4}}{3.35 \times 10^{-5}}} = 54.1 \times \sqrt{9.37}$$

$$f = 54.1 \times 3.06 = \mathbf{166 \text{ Hz}}$$

This is near E₃ on a piano — a typical bottle note.

---

### Worked Example 42.3 — Energy in Standing Waves (Conceptual)

**Problem:** A standing wave is established on a string. Explain:
(a) Why no net energy is transferred along the string.
(b) What happens to the energy that was put in to create the wave.
(c) How this differs from a travelling wave pulse.

**Solution:**

**(a)** At nodes, the string is always stationary, so no displacement or velocity ever occurs there. Energy cannot be transferred through a point that never moves — the nodes act as energy barriers. Energy is confined to each segment between nodes.

**(b)** The energy continuously interconverts between kinetic energy (when the string segments pass through equilibrium at maximum speed) and elastic potential energy (when the segments are maximally displaced and stretched). This is analogous to a mass on a spring — continuous oscillation without dissipation (in the ideal case). In reality, some energy is lost to internal friction and air resistance.

**(c)** In a travelling pulse, energy moves with the pulse — each particle transfers its energy to the next particle. The pulse carries energy from one end to the other. In a standing wave, energy stays in place, oscillating between KE and PE but never migrating.

---

### Worked Example 42.4 — Helmholtz Resonator Applied

**Problem:** A 1-litre bottle (V = 1.0 × 10⁻³ m³) with neck length 8 cm and neck radius 1.2 cm produces a resonant frequency of 120 Hz when blown. Use this to estimate the speed of sound. (Use end correction L_eff = L + 1.7r.)

**Solution:**

A = πr² = π × (0.012)² = 4.52 × 10⁻⁴ m²
L_eff = 0.080 + 1.7(0.012) = 0.1004 m

Rearrange Helmholtz formula:
$$f = \frac{v}{2\pi}\sqrt{\frac{A}{V L_{\text{eff}}}}$$
$$v = 2\pi f \sqrt{\frac{V L_{\text{eff}}}{A}}$$
$$v = 2\pi \times 120 \times \sqrt{\frac{1.0 \times 10^{-3} \times 0.1004}{4.52 \times 10^{-4}}}$$
$$v = 754 \times \sqrt{0.222} = 754 \times 0.471 = \mathbf{355 \text{ m/s}}$$

Reasonable for warm air (~30°C).

---

## Practice Problems

### Problem 1
A standing wave on a string is given by: y = 0.080 cos(5.0x) sin(200t) (SI units).
(a) What is the amplitude of each travelling wave component?
(b) Determine the frequency and wavelength.
(c) At t = 0.010 s, what is the displacement at x = 0.30 m?

### Problem 2
A Helmholtz resonator (bottle) has cavity volume 750 cm³, neck radius 1.5 cm, and neck length 6.0 cm. Speed of sound = 345 m/s.
(a) Calculate the resonant frequency.
(b) If the bottle is half-filled with water (reducing V to 375 cm³), what happens to the frequency?
(c) Explain this trend physically.

### Problem 3
A standing wave on a string fixed at both ends has total length 1.20 m and carries its 3rd harmonic. At one instant, the antinode displacement is +3.0 cm and all points between the first two nodes are moving downward.
(a) Sketch the wave at this instant.
(b) Describe the motion of the middle antinode.
(c) A quarter-period later, what is the displacement of the middle antinode?

### Problem 4 (IB-Style — Conceptual + Calculation)
A student investigates standing waves on a string and in pipes.

**(a)** On a stretched string, standing waves are observed at 60 Hz, 120 Hz, and 180 Hz but NOT at 90 Hz or 150 Hz. Explain this pattern. If the string length is 0.80 m, find the wave speed.

**(b)** In an organ pipe closed at one end, standing waves are observed at 150 Hz, 450 Hz, and 750 Hz. The pipe length is 0.57 m. Using this data, determine the speed of sound and identify which harmonics these are.

**(c)** The student notices that when the pipe in (b) is played loudly, additional higher frequencies are faintly audible. Two of these are measured at approximately 300 Hz and 600 Hz. Suggest a physical explanation. *(Hint: real pipes are not perfectly closed/open.)*

---

## Answers

### Answer 1
**(a)** 2A = 0.080 → **A = 0.040 m**

**(b)** k = 5.0 → λ = 2π/5.0 = **1.26 m**
ω = 200 → f = 200/(2π) = **31.8 Hz**

**(c)** y = 0.080 cos(5.0 × 0.30) sin(200 × 0.010)
= 0.080 cos(1.5) sin(2.0)
cos(1.5) = 0.0707, sin(2.0) = 0.909
y = 0.080 × 0.0707 × 0.909 = **0.00514 m ≈ 5.1 mm**

---

### Answer 2
**(a)** A = π(0.015)² = 7.07×10⁻⁴ m², L_eff = 0.060 + 1.7(0.015) = 0.0855 m
f = (345/2π) × √(7.07×10⁻⁴ / (7.5×10⁻⁴ × 0.0855))
= 54.9 × √(11.04) = 54.9 × 3.32 = **182 Hz**

**(b)** V halves → (1/V) doubles → f_new = f_old × √2 = 182 × 1.414 = **257 Hz**

**(c)** Less air in the cavity → stiffer "spring" → higher resonant frequency. This is why adding water to a bottle raises the pitch when you blow across it.

---

### Answer 3
**(a)** 3rd harmonic: N–A–N–A–N–A–N. Antinodes at x = L/6, L/2, 5L/6 = 0.20 m, 0.60 m, 1.00 m. At this instant, positive displacement at antinodes.

**(b)** The middle antinode is at maximum positive displacement (+3.0 cm) right now. It will move downward, pass through equilibrium, reach −3.0 cm, then move back up — simple harmonic motion at frequency f₃.

**(c)** A quarter-period later (t = T/4), sin(ωt + π/2) means displacement = 0 for all points since the time-dependent part is sin(ωt) and at T/4 from max, sin = 0. **Displacement = 0 everywhere** (the string is momentarily straight).

---

### Answer 4 (IB-Style)

**(a)** The pattern 60, 120, 180 Hz corresponds to f₁, 2f₁, 3f₁ with f₁ = 60 Hz. The missing 90 Hz and 150 Hz are 1.5f₁ and 2.5f₁ — these are not integer multiples, so they don't form standing waves on a string fixed at both ends (which requires integer n).

v = 2L f₁ = 2 × 0.80 × 60 = **96 m/s**

**(b)** 150, 450, 750 Hz: these are in ratio 1:3:5, so f₁ = 150 Hz, and these are the 1st, 3rd, and 5th harmonics of a closed pipe.

For closed pipe: f₁ = v/(4L) → v = 4L f₁ = 4 × 0.57 × 150 = **342 m/s**

**(c)** The frequencies 300 Hz and 600 Hz are 2f₁ and 4f₁ — the even harmonics that should not exist in an ideal closed pipe. Their faint presence suggests the pipe is not perfectly closed: perhaps the stopper is slightly loose, or the pipe has a small leak, partially allowing even harmonics. Alternatively, the pipe may be exciting some open-pipe-like modes if the end isn't perfectly rigid. In real instruments, boundary conditions are never perfectly ideal.

---

## Key Takeaways

| Concept | Key Points |
|---------|-----------|
| Standing wave equation | y = 2A cos(kx) sin(ωt) — spatial envelope × temporal oscillation |
| Nodes & antinodes | cos(kx) = 0 → nodes; |cos(kx)| = 1 → antinodes |
| Energy in standing waves | No net transfer — energy trapped between nodes |
| Chladni plates | 2D standing waves, nodal lines visible with sand |
| Helmholtz resonator | f = (v/2π)√(A/(V·L_eff)) — neck air = mass, cavity air = spring |
| Musical instruments | Strings: all harmonics. Closed pipes: odd only. Percussion: often non-harmonic. |

> **IB Data Booklet:** y = A sin(kx − ωt) and v = fλ. The standing wave equation and Helmholtz resonator formula should be understood conceptually; calculations require correct interpretation. The energy analysis (no net transfer) is a key HL conceptual point frequently tested in Paper 2.
