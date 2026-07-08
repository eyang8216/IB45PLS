# Lesson 40: Standing Waves I — Nodes, Antinodes & Strings

## What You'll Learn
- How standing waves form from incident + reflected waves
- Nodes (zero displacement) and antinodes (maximum displacement)
- Boundary conditions and harmonics on strings
- The harmonic series: λₙ = 2L/n and fₙ = nf₁
- Wave speed on a stretched string: v = √(T/μ)

---

## 1. Formation of Standing Waves

A **standing wave** is not a travelling wave — it is a pattern of oscillation that appears to stand still. It forms when two identical waves travelling in **opposite directions** superpose.

### The Key Mechanism

Consider a wave pulse sent down a string fixed at one end. Upon reaching the fixed end, it reflects and travels back. If you continuously send waves (incident waves), they meet the reflected waves and interfere.

At certain frequencies, the interference produces a **stable, stationary pattern** — a standing wave.

**Incident wave:** `y₁ = A sin(kx − ωt)`
**Reflected wave:** `y₂ = A sin(kx + ωt)` *(phase change of π at fixed end)*

**Superposition:** `y = y₁ + y₂ = 2A cos(kx) sin(ωt)`

This is the standing wave equation. Note:
- `2A cos(kx)` is the **amplitude envelope** — varies with position x
- `sin(ωt)` is the **time oscillation** — all points oscillate in phase or antiphase

---

## 2. Nodes and Antinodes

### Definitions

| Feature | Definition | Displacement | Spacing |
|---------|-----------|-------------|---------|
| **Node (N)** | Point of **zero** displacement at all times | Always 0 | λ/2 apart |
| **Antinode (A)** | Point of **maximum** displacement | Varies between ±2A | λ/2 apart |

In the standing wave equation `y = 2A cos(kx) sin(ωt)`:
- **Nodes** occur where `cos(kx) = 0` → `kx = π/2, 3π/2, 5π/2, ...` → `x = λ/4, 3λ/4, 5λ/4, ...`
- **Antinodes** occur where `cos(kx) = ±1` → `kx = 0, π, 2π, ...` → `x = 0, λ/2, λ, ...`

### Phase Relationship
- Points between two consecutive nodes oscillate **in phase** (move up and down together)
- Points separated by one node oscillate **in antiphase** (180° out of phase)
- **No energy is transmitted** along a standing wave — energy is trapped between nodes

---

## 3. Boundary Conditions on Strings

### Fixed End → Node
When a string is fixed (tied down), the end cannot move → **node at a fixed end**.

### Free End → Antinode
If the end is free to move (unusual for strings, common for pipes), maximum displacement occurs → **antinode at a free end**.

### Both Ends Fixed (Most Common String Case)
- Both ends are nodes
- Standing waves can only form when an integer number of half-wavelengths fit into the string length

---

## 4. Harmonics on Strings

For a string of length L, fixed at both ends:

$$L = n \cdot \frac{\lambda_n}{2} \quad \text{where } n = 1, 2, 3, ...$$

$$\lambda_n = \frac{2L}{n}$$

### Fundamental Frequency (n = 1)

The fundamental (first harmonic) has one antinode in the middle:

$$\lambda_1 = 2L$$

$$f_1 = \frac{v}{\lambda_1} = \frac{v}{2L}$$

where v is the wave speed on the string.

### Harmonic Frequencies

$$f_n = n \cdot f_1 = \frac{nv}{2L}$$

### Wave Speed on a Stretched String

$$v = \sqrt{\frac{T}{\mu}}$$

where:
- **T** = tension in the string (N)
- **μ** = mass per unit length = m/L (kg/m)

### Full String Equation

$$f_n = \frac{n}{2L}\sqrt{\frac{T}{\mu}}$$

### Harmonic Series Summary

| Harmonic | n | λ | f | Pattern |
|----------|---|---|---|---------|
| 1st (fundamental) | 1 | 2L | f₁ | N–A–N |
| 2nd | 2 | L | 2f₁ | N–A–N–A–N |
| 3rd | 3 | 2L/3 | 3f₁ | N–A–N–A–N–A–N |
| nth | n | 2L/n | n·f₁ | n antinodes |

---

## Worked Examples

### Worked Example 40.1 — Frequency of Third Harmonic

**Problem:** A guitar string is 0.65 m long with mass 2.6 g. It is under tension of 80 N. Find:
(a) the wave speed on the string
(b) the fundamental frequency
(c) the frequency of the third harmonic

**Solution:**

**(a) Wave speed:**
$$\mu = \frac{m}{L} = \frac{2.6 \times 10^{-3}}{0.65} = 4.0 \times 10^{-3} \text{ kg/m}$$

$$v = \sqrt{\frac{T}{\mu}} = \sqrt{\frac{80}{4.0 \times 10^{-3}}} = \sqrt{20000} = 141 \text{ m/s}$$

**(b) Fundamental frequency:**
$$f_1 = \frac{v}{2L} = \frac{141}{2 \times 0.65} = \frac{141}{1.30} = 108 \text{ Hz}$$

**(c) Third harmonic:**
$$f_3 = 3f_1 = 3 \times 108 = 325 \text{ Hz}$$

*(Alternatively: λ₃ = 2L/3 = 0.433 m, f₃ = v/λ₃ = 141/0.433 = 326 Hz — same result)*

---

### Worked Example 40.2 — Finding Tension for a Given Frequency

**Problem:** A violin string of length 0.33 m and linear density 4.0 × 10⁻⁴ kg/m produces a fundamental frequency of 440 Hz (concert A). What tension is required?

**Solution:**

Use the fundamental frequency equation:
$$f_1 = \frac{1}{2L}\sqrt{\frac{T}{\mu}}$$

Rearrange for T:
$$\sqrt{\frac{T}{\mu}} = 2L f_1$$
$$\frac{T}{\mu} = (2L f_1)^2$$
$$T = \mu (2L f_1)^2$$

Substitute:
$$T = (4.0 \times 10^{-4}) \times (2 \times 0.33 \times 440)^2$$
$$T = (4.0 \times 10^{-4}) \times (290.4)^2$$
$$T = (4.0 \times 10^{-4}) \times 84332$$
$$T = 33.7 \text{ N}$$

---

### Worked Example 40.3 — Identifying Harmonic from Pattern

**Problem:** A string 1.20 m long oscillates with 5 nodes (including the fixed ends) and 4 antinodes. Determine:
(a) the harmonic number
(b) the wavelength
(c) the frequency if the wave speed is 240 m/s

**Solution:**

**(a)** For a string fixed at both ends, n = number of antinodes = 4. This is the **4th harmonic**.

Alternatively: number of nodes = n + 1 = 5, so n = 4.

**(b)**
$$\lambda_4 = \frac{2L}{n} = \frac{2 \times 1.20}{4} = 0.60 \text{ m}$$

**(c)**
$$f_4 = \frac{v}{\lambda_4} = \frac{240}{0.60} = 400 \text{ Hz}$$

Or: f₁ = v/(2L) = 240/(2×1.20) = 100 Hz, f₄ = 4 × 100 = 400 Hz.

---

### Worked Example 40.4 — Changing Tension and Its Effect

**Problem:** A guitar string tuned to 196 Hz (G note) has its tension increased by 21%. What is the new frequency?

**Solution:**

Since f ∝ √T, when tension changes:
$$\frac{f_{\text{new}}}{f_{\text{old}}} = \sqrt{\frac{T_{\text{new}}}{T_{\text{old}}}}$$

If T increases by 21%, then T_new/T_old = 1.21:
$$\frac{f_{\text{new}}}{f_{\text{old}}} = \sqrt{1.21} = 1.10$$

$$f_{\text{new}} = 1.10 \times 196 = 216 \text{ Hz}$$

The pitch rises — this is how guitarists tune by tightening pegs.

---

## Practice Problems

### Problem 1
A nylon guitar string is 0.70 m long and has a mass of 2.8 g. It vibrates in its fundamental mode at 125 Hz.
(a) Calculate the linear density of the string.
(b) Find the wave speed on the string.
(c) Determine the tension in the string.

### Problem 2
A string fixed at both ends is 2.40 m long. Standing waves are observed at frequencies of 60 Hz, 90 Hz, 120 Hz, and 150 Hz. No standing waves are seen between these values.
(a) What is the fundamental frequency?
(b) What is the wave speed on the string?
(c) What harmonic is the 150 Hz wave?

### Problem 3
A 0.50 m string vibrates in its 3rd harmonic at 450 Hz. Find:
(a) the wavelength of this standing wave
(b) the wave speed
(c) the fundamental frequency

### Problem 4
A steel wire of length 1.50 m and diameter 0.50 mm (density of steel = 7800 kg/m³) is under tension of 200 N. Find:
(a) the linear density μ
(b) the fundamental frequency
(c) the frequency of the 5th harmonic

### Problem 5 (IB-Style — Challenging)
A student investigates standing waves on a string. One end is attached to a vibration generator set at frequency f, and the string passes over a pulley with a hanging mass M to provide tension. The string has linear density μ.

When f = 50.0 Hz and M = 1.00 kg, a standing wave with 3 antinodes is observed between the vibrator and the pulley (distance L = 1.50 m).

(a) Show that the hanging mass is 1.00 kg, calculate the tension. (g = 10 m/s²)
(b) Determine the wave speed and hence μ.
(c) The student increases f to 75.0 Hz while keeping everything else the same. Explain why no clear standing wave pattern is observed initially, and state what change must be made to M to restore a 3-antinode pattern.

---

## Answers

### Answer 1
**(a)** μ = m/L = 2.8×10⁻³ / 0.70 = **4.0 × 10⁻³ kg/m**

**(b)** For fundamental: v = f₁ × 2L = 125 × 2 × 0.70 = **175 m/s**

**(c)** T = μ v² = 4.0×10⁻³ × (175)² = **123 N**

---

### Answer 2
**(a)** The frequencies are multiples: 60, 90, 120, 150. This is 2f₁, 3f₁, 4f₁, 5f₁ (the fundamental 30 Hz is missing from observations but implied since 60 = 2×30, etc.).
**f₁ = 30 Hz**

**(b)** f₁ = v/(2L) → v = 2L f₁ = 2 × 2.40 × 30 = **144 m/s**

**(c)** 150/30 = 5 → **5th harmonic**

---

### Answer 3
**(a)** λ₃ = 2L/3 = 2 × 0.50 / 3 = **0.333 m**

**(b)** v = f₃ × λ₃ = 450 × 0.333 = **150 m/s** (or: v = f₃ × 2L/3)

**(c)** f₁ = f₃/3 = 450/3 = **150 Hz**

---

### Answer 4
**(a)** Cross-sectional area: A = π(d/2)² = π(0.25×10⁻³)² = 1.96×10⁻⁷ m²
μ = ρA = 7800 × 1.96×10⁻⁷ = **1.53 × 10⁻³ kg/m**

**(b)** v = √(T/μ) = √(200 / 1.53×10⁻³) = 361 m/s
f₁ = v/(2L) = 361/(2 × 1.50) = **120 Hz**

**(c)** f₅ = 5f₁ = 5 × 120 = **600 Hz**

---

### Answer 5 (IB-Style)
**(a)** T = Mg = 1.00 × 10 = **10.0 N**

**(b)** With 3 antinodes: n = 3, λ = 2L/3 = 2×1.50/3 = 1.00 m
v = fλ = 50.0 × 1.00 = 50.0 m/s

v = √(T/μ) → μ = T/v² = 10.0/(50.0)² = **4.0 × 10⁻³ kg/m**

**(c)** At f = 75.0 Hz, the wave speed hasn't changed (T and μ unchanged), so v = 50.0 m/s. 
Wavelength for 3 antinodes would be: λ = v/f = 50.0/75.0 = 0.667 m. 
But for n = 3, we need λ = 2L/3 = 1.00 m. These don't match, so no standing wave forms.

To restore the 3-antinode pattern at 75.0 Hz, we need v = fλ = 75.0 × 1.00 = 75.0 m/s.
Since v ∝ √T and T ∝ M, we need v² ∝ M:
M_new / M_old = (75.0/50.0)² = 2.25
**M_new = 2.25 kg** — the mass must be increased to 2.25 kg.

---

## Key Takeaways

| Concept | Key Equation | Notes |
|---------|-------------|-------|
| Standing wave formation | Superposition of incident + reflected waves | Frequencies must match |
| Nodes | cos(kx) = 0 | λ/2 spacing |
| Antinodes | cos(kx) = ±1 | λ/2 spacing |
| String harmonics | fₙ = nf₁ = (n/2L)√(T/μ) | n = 1,2,3,... |
| Wave speed on string | v = √(T/μ) | Depends on tension and linear density |
| Boundary: fixed end | Node | Displacement = 0 |
| Harmonic number | n = number of antinodes | n = nodes − 1 (strings) |

> **IB Data Booklet references:** v = fλ, f = 1/T (Sub-topic 4.2). The string harmonic formula fₙ = nv/(2L) and v = √(T/μ) must be memorized — they are not in the formula booklet but are directly tested.
