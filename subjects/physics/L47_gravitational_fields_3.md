# Lesson 47: Gravitational Fields III — Kepler's Laws & Advanced Orbits

## What You'll Learn
- Kepler's Three Laws of planetary motion
- Escape velocity: v_esc = √(2GM/r)
- Total orbital energy: E = −GMm/(2r)
- Binary star systems and centre of mass orbits
- Gravitational slingshot and Roche limit

---

## 1. Kepler's Three Laws

### Kepler's First Law — Law of Ellipses

Planets move in **elliptical** orbits with the Sun at one focus.

```
        Planet
       ○
     ·     ·
    ·         ·
    ·     ☉    ·    ← Sun at one focus
    ·         ·
     ·     ·
       ○
```

- The semi-major axis **a** is half the longest diameter
- For a circle (special case), a = r and both foci coincide

### Kepler's Second Law — Law of Equal Areas

A line from the planet to the Sun sweeps out **equal areas in equal times**.

```
   t₂
    ○
   ·  ·        Planet moves FASTER near Sun
  ·    ○       (perihelion) and SLOWER far away
  ·   ·  ·     (aphelion)
   · ·              t₁
    ○ → Sun
```

**Consequence:** Orbital speed is NOT constant — faster when closer to the Sun.

### Kepler's Third Law — The Harmonic Law

$$T^2 \propto a^3$$

For orbits around the same central body, the square of the period is proportional to the cube of the semi-major axis.

$$\frac{T^2}{a^3} = \frac{4\pi^2}{GM}$$

This is the same as the circular orbit formula, with a replacing r.

### Using Kepler's Third Law

If you know the period and semi-major axis of one planet, you can find another:

$$\frac{T_1^2}{T_2^2} = \frac{a_1^3}{a_2^3}$$

---

## 2. Escape Velocity

### Definition

Escape velocity is the minimum speed an object needs at a distance r from a mass M to escape its gravitational field and coast to infinity.

### Derivation

For escape: total energy E = KE + PE ≥ 0 at infinity. At the starting point:

$$\frac{1}{2}mv_{\text{esc}}^2 + \left(-\frac{GMm}{r}\right) = 0$$

$$\frac{1}{2}mv_{\text{esc}}^2 = \frac{GMm}{r}$$

$$v_{\text{esc}} = \sqrt{\frac{2GM}{r}}$$

### Key Points

| Property | Value |
|----------|-------|
| From Earth's surface | ~11.2 km/s |
| From Moon's surface | ~2.4 km/s |
| From Mars surface | ~5.0 km/s |
| Depends on | M and r only — NOT on the escaping object's mass! |
| Relationship to orbital v | v_esc = √2 × v_orbital (at same r) |

---

## 3. Total Orbital Energy

For a satellite in circular orbit:

$$E_{\text{total}} = KE + PE = \frac{1}{2}mv^2 + \left(-\frac{GMm}{r}\right)$$

Substituting v = √(GM/r):

$$\frac{1}{2}m \cdot \frac{GM}{r} - \frac{GMm}{r} = -\frac{GMm}{2r}$$

### Important Result

$$E_{\text{total}} = -\frac{GMm}{2r} = \frac{PE}{2}$$

For circular orbits:
- Total energy is **negative** (bound orbit)
- KE = −E_total (KE = GMm/(2r))
- PE = 2E_total (PE = −GMm/r)
- |KE| = |E_total| and |PE| = 2|KE|

### Energy Level Interpretation

```
E
↑
0 ├─────────────────────── Escape (E = 0)
  |   ╲
  |     ╲  Higher orbit (less negative E)
  |       ╲
  |         ╲  Lower orbit (more negative E)
──┼───────────╲────────→ r
  |  More bound   Less bound
```

- More negative total energy = more tightly bound
- To move to a higher orbit, you must ADD energy
- To escape: add enough energy to make E ≥ 0

---

## 4. Binary Star Systems

In a binary star system, two stars orbit their **common centre of mass (CM)**.

### Centre of Mass

$$r_1 = \frac{m_2}{m_1 + m_2} d, \quad r_2 = \frac{m_1}{m_1 + m_2} d$$

where d is the distance between their centres.

### Period

Both stars have the SAME orbital period T. Using Newton's form of Kepler's Third Law:

$$T^2 = \frac{4\pi^2 d^3}{G(m_1 + m_2)}$$

Note: the denominator uses (m₁ + m₂) not just the central mass — both masses matter!

---

## 5. Gravitational Slingshot (Gravity Assist)

Spacecraft use planetary flybys to gain speed without using fuel.

### How It Works

1. Spacecraft approaches a planet from behind (relative to planet's orbital motion)
2. Spacecraft falls into the planet's gravity well, gaining speed
3. Spacecraft swings around and leaves in a different direction
4. The planet loses a tiny amount of orbital energy (negligible due to huge mass difference)
5. **Net result:** Spacecraft gains significant speed relative to the Sun

### Key Physics

- In the planet's reference frame: elastic "collision" — speed in/out is same, direction changes
- In the Sun's frame: speed can increase dramatically
- Used by Voyager, Cassini, New Horizons, and many other missions

---

## 6. Roche Limit (Qualitative)

The **Roche limit** is the distance from a planet within which a satellite (moon) will be torn apart by tidal forces — the planet's gravity pulling more strongly on the near side than the far side.

### Approximate Roche Limit

$$d \approx 2.44 R_{\text{planet}} \left(\frac{\rho_{\text{planet}}}{\rho_{\text{moon}}}\right)^{1/3}$$

- Saturn's rings lie within Saturn's Roche limit — a moon that strayed too close was torn apart
- This is why rings form and why moons don't exist very close to planets

---

## Worked Examples

### Worked Example 47.1 — Escape Velocity from Earth

**Problem:** Calculate the escape velocity from Earth's surface.
M_Earth = 5.97 × 10²⁴ kg, R = 6.37 × 10⁶ m.

**Solution:**

$$v_{\text{esc}} = \sqrt{\frac{2GM}{R}} = \sqrt{\frac{2 \times 6.67 \times 10^{-11} \times 5.97 \times 10^{24}}{6.37 \times 10^6}}$$

$$v_{\text{esc}} = \sqrt{\frac{7.96 \times 10^{14}}{6.37 \times 10^6}} = \sqrt{1.25 \times 10^8} = \mathbf{1.12 \times 10^4 \text{ m/s} = 11.2 \text{ km/s}}$$

---

### Worked Example 47.2 — Orbital Energy Change

**Problem:** A 1000 kg satellite moves from a circular orbit at r = 7000 km to one at r = 14000 km (measured from Earth's centre). M_Earth = 6.0 × 10²⁴ kg.
(a) Calculate the total energy in each orbit.
(b) How much energy must be added?

**Solution:**

**(a)** Lower orbit:
$$E_1 = -\frac{GMm}{2r_1} = -\frac{6.67 \times 10^{-11} \times 6.0 \times 10^{24} \times 1000}{2 \times 7.0 \times 10^6}$$
$$E_1 = -\frac{4.0 \times 10^{17}}{1.4 \times 10^7} = -2.86 \times 10^{10} \text{ J}$$

Higher orbit:
$$E_2 = -\frac{4.0 \times 10^{17}}{2 \times 1.4 \times 10^7} = -1.43 \times 10^{10} \text{ J}$$

**(b)** Energy to add = E₂ − E₁ = −1.43×10¹⁰ − (−2.86×10¹⁰) = **+1.43 × 10¹⁰ J**

Note: E₁ is more negative (more tightly bound) than E₂. Moving to a higher orbit requires positive energy input.

---

### Worked Example 47.3 — Kepler's Third Law with Two Planets

**Problem:** Earth orbits the Sun at r = 1.50 × 10¹¹ m (1 AU) with T = 365 days. Mars orbits at 2.28 × 10¹¹ m (1.52 AU). Use Kepler's Third Law to find Mars's orbital period.

**Solution:**

$$\frac{T_{\text{Mars}}^2}{T_{\text{Earth}}^2} = \frac{a_{\text{Mars}}^3}{a_{\text{Earth}}^3}$$

$$T_{\text{Mars}} = T_{\text{Earth}} \left(\frac{a_{\text{Mars}}}{a_{\text{Earth}}}\right)^{3/2} = 365 \times (1.52)^{3/2}$$

(1.52)^(3/2) = (1.52)^(1.5) = 1.87

$$T_{\text{Mars}} = 365 \times 1.87 = \mathbf{684 \text{ days}}$$

(The actual value is about 687 days — close!)

---

### Worked Example 47.4 — Binary Star Period

**Problem:** Two stars of masses 2.0 × 10³⁰ kg and 3.0 × 10³⁰ kg orbit their common CM separated by distance 4.0 × 10¹¹ m. Find:
(a) the orbital period
(b) the orbital speed of each star

**Solution:**

**(a)** Using Kepler's Third Law for binaries:
$$T^2 = \frac{4\pi^2 d^3}{G(m_1 + m_2)} = \frac{4\pi^2 (4.0 \times 10^{11})^3}{6.67 \times 10^{-11} (5.0 \times 10^{30})}$$

$$T^2 = \frac{4\pi^2 \times 6.4 \times 10^{34}}{3.335 \times 10^{20}} = \frac{2.53 \times 10^{36}}{3.335 \times 10^{20}} = 7.58 \times 10^{15}$$

$$T = \mathbf{8.71 \times 10^7 \text{ s} \approx 2.76 \text{ years}}$$

**(b)** Distance from CM:
- r₁ = d × m₂/(m₁+m₂) = 4.0×10¹¹ × 3.0/5.0 = 2.4 × 10¹¹ m
- r₂ = d × m₁/(m₁+m₂) = 4.0×10¹¹ × 2.0/5.0 = 1.6 × 10¹¹ m

Speeds:
- v₁ = 2πr₁/T = 2π(2.4×10¹¹)/8.71×10⁷ = **1.73 × 10⁴ m/s**
- v₂ = 2πr₂/T = 2π(1.6×10¹¹)/8.71×10⁷ = **1.15 × 10⁴ m/s**

---

## Practice Problems

### Problem 1
Calculate the escape velocity from:
(a) The Moon's surface (M = 7.35 × 10²² kg, R = 1.74 × 10⁶ m)
(b) A point 3.0 × 10⁷ m from Earth's centre (M = 6.0 × 10²⁴ kg)

### Problem 2
A 500 kg satellite has total energy E = −1.0 × 10¹⁰ J in circular orbit around Earth (M = 6.0 × 10²⁴ kg).
(a) What is its orbital radius?
(b) Find its kinetic energy and orbital speed.
(c) How much additional energy is needed to escape?

### Problem 3
Jupiter orbits the Sun at 5.2 AU with period 11.9 years. Saturn orbits at 9.5 AU. Use Kepler's Third Law to find Saturn's orbital period.

### Problem 4
A comet has a highly elliptical orbit with semi-major axis 18 AU. Using Earth's orbit (a = 1 AU, T = 1 year), find the comet's period. This is Halley's Comet — verify the period is about 76 years.

### Problem 5 (IB-Style — Escape + Orbit Combined)
A probe of mass 2000 kg is launched from Earth's surface.

**(a)** Calculate the escape velocity from Earth's surface. (M_E = 5.97 × 10²⁴ kg, R_E = 6.37 × 10⁶ m)

**(b)** The probe is instead placed into a circular orbit at altitude 500 km.
    (i) Find its orbital speed.
    (ii) Calculate the total energy of the probe in this orbit.
    (iii) Determine the minimum additional impulse (change in velocity) needed for the probe to escape from this orbit, assuming the engines fire instantaneously.

**(c)** The probe uses a gravitational slingshot around Mars to gain speed. Explain qualitatively:
    (i) Why the probe gains energy relative to the Sun.
    (ii) What happens to Mars's orbital energy as a result.

---

## Answers

### Answer 1
**(a)** v_esc = √(2GM/R) = √(2 × 6.67×10⁻¹¹ × 7.35×10²² / 1.74×10⁶)
= √(9.81×10¹² / 1.74×10⁶) = √(5.64×10⁶) = **2.37 × 10³ m/s = 2.37 km/s**

**(b)** v_esc = √(2GM/r) = √(2 × 6.67×10⁻¹¹ × 6.0×10²⁴ / 3.0×10⁷)
= √(8.0×10¹⁴ / 3.0×10⁷) = √(2.67×10⁷) = **5.16 × 10³ m/s = 5.16 km/s**

---

### Answer 2
**(a)** E = −GMm/(2r) → r = −GMm/(2E) = −4.0×10¹⁷/(2 × (−1.0×10¹⁰)) = 4.0×10¹⁷ / 2.0×10¹⁰ = **2.0 × 10⁷ m**

**(b)** KE = −E_total = **1.0 × 10¹⁰ J**
v = √(2KE/m) = √(2.0×10¹⁰/500) = √(4.0×10⁷) = **6.32 × 10³ m/s**

**(c)** To escape: E must go from −1.0×10¹⁰ to 0, so **ΔE = +1.0 × 10¹⁰ J**

---

### Answer 3
T_Saturn = T_Jupiter × (a_Saturn/a_Jupiter)^(3/2) = 11.9 × (9.5/5.2)^(3/2)
(9.5/5.2) = 1.827, (1.827)^(3/2) = 1.827^(1.5) = 2.47
T_Saturn = 11.9 × 2.47 = **29.4 years** (actual: ~29.5 years)

---

### Answer 4
T_comet = T_Earth × (a_comet/a_Earth)^(3/2) = 1 × (18/1)^(3/2)
18^(3/2) = 18^(1.5) = 76.4
**T ≈ 76.4 years** ✓ Halley's Comet period is ~76 years.

---

### Answer 5 (IB-Style)
**(a)** v_esc = √(2GM/R) = √(2 × 6.67×10⁻¹¹ × 5.97×10²⁴ / 6.37×10⁶)
= √(7.96×10¹⁴ / 6.37×10⁶) = √(1.25×10⁸) = **11.2 km/s**

**(b)(i)** r = R + h = 6.37×10⁶ + 5.00×10⁵ = 6.87×10⁶ m
v_orb = √(GM/r) = √(3.98×10¹⁴/6.87×10⁶) = √(5.79×10⁷) = **7.61 km/s**

**(b)(ii)** E_total = −GMm/(2r) = −3.98×10¹⁴ × 2000/(2 × 6.87×10⁶) = −7.96×10¹⁷/(1.374×10⁷)
= **−5.79 × 10¹⁰ J**

**(b)(iii)** Escape from orbit requires v_esc_orbit = √(2GM/r) = √2 × v_orb = 1.414 × 7.61 = 10.76 km/s.
Δv = 10.76 − 7.61 = **3.15 km/s**

**(c)(i)** In the Sun's reference frame: the probe approaches Mars from behind (relative to Mars's orbital motion). It falls into Mars's gravity well, swings around, and leaves. The planet's orbital motion effectively "drags" the probe, adding to its heliocentric speed — like a tennis ball bouncing off a moving racquet.

**(c)(ii)** By conservation of energy and momentum, Mars loses a tiny amount of orbital energy. However, because Mars is ~10²³ kg and the probe is ~10³ kg, the change in Mars's orbit is utterly negligible — Mars slows down by less than a nanometer per year. The slingshot is effectively "free" energy from the probe's perspective.

---

## Key Takeaways

| Concept | Equation | Notes |
|---------|----------|-------|
| Kepler's 1st | Elliptical orbits, Sun at focus | Planets: e is small (nearly circular) |
| Kepler's 2nd | Equal areas in equal times | Faster near Sun, slower far away |
| Kepler's 3rd | T² ∝ a³ | T² = 4π²a³/(GM) |
| Escape velocity | v_esc = √(2GM/r) | √2 × orbital speed |
| Total orbital E | E = −GMm/(2r) | Negative for bound orbits |
| Binary period | T² = 4π²d³/[G(m₁+m₂)] | Both masses in denominator |
| Slingshot | Gravity assist from planets | Planet effectively "lends" energy |

> **IB Data Booklet:** Kepler's Third Law (T² ∝ r³) and escape velocity are referenced in Sub-topic 6.2 (HL). The orbital energy equation E = −GMm/(2r) is implied but should be understood. Binary systems, slingshot effects, and Roche limit are conceptual HL topics that may appear in Paper 2 or Paper 3.
