# Lesson 46: Gravitational Fields II — Potential & Orbits

## What You'll Learn
- Gravitational potential V = −GM/r (scalar)
- Potential difference and work done: W = mΔV
- Equipotential surfaces in gravitational fields
- Field as potential gradient: g = −ΔV/Δr
- Orbital velocity and Kepler's Third Law

---

## 1. Gravitational Potential V

### Definition

Gravitational potential at a point is the **work done per unit mass** to bring a small test mass from **infinity** to that point.

$$V = -\frac{GM}{r}$$

where:
- **V** = gravitational potential (J/kg)
- **r** = distance from centre of mass M (m)
- The reference point is infinity: V(∞) = 0

### Why Negative?

- Gravity is **attractive** — you must do work AGAINST gravity to move a mass away
- As a mass falls toward Earth, gravity does positive work → potential decreases
- Since V(∞) = 0, all finite r values give V < 0
- The more negative V is, the more tightly bound you are

### Key Properties

| Property | Description |
|----------|-------------|
| Sign | Always negative (for point mass) |
| Scalar | Potential is a scalar, not a vector |
| Superposition | V_total = V₁ + V₂ + ... (simple addition!) |
| Reference | V = 0 at r = ∞ |

---

## 2. Gravitational Potential Difference and Work Done

### Work Done

To move a mass m from point A to point B:

$$W = m(V_B - V_A) = m\Delta V$$

- If ΔV > 0 (moving to higher potential): work must be done **on** the mass (against gravity)
- If ΔV < 0 (moving to lower potential): gravity does work, mass gains KE

### Lifting Mass from Earth's Surface

To move from r = R (surface) to r = R + h:

$$\Delta V = -\frac{GM}{R+h} - \left(-\frac{GM}{R}\right) = GM\left(\frac{1}{R} - \frac{1}{R+h}\right)$$

$$W = m\Delta V = GMm\left(\frac{1}{R} - \frac{1}{R+h}\right)$$

For small h (h ≪ R), this simplifies to W ≈ mgh as expected.

---

## 3. Equipotential Surfaces

Equipotential surfaces are surfaces where V is constant.

### Properties

- **Perpendicular to field lines** everywhere
- Moving along an equipotential requires **no work** (ΔV = 0)
- Closer spacing = stronger field
- For a point mass, equipotentials are concentric spheres

```
Field lines:   → → → → → (inward toward mass)
               ↓ ↓ ↓ ↓ ↓
Equipotentials: — — — — — (perpendicular to field lines)
```

### Field as Potential Gradient

The field strength is the negative gradient of the potential:

$$g = -\frac{\Delta V}{\Delta r}$$

In 1D: the steeper the V vs r graph, the stronger the g field.

```
V
|
|    ╲
|      ╲___  (V = −GM/r, getting less negative with r)
|          ╲___
|              ╲___
0├─────────────────────→ r
|         (V → 0 as r → ∞)
```

The slope of this curve = −g. Steeper slope → stronger field.

---

## 4. Orbital Motion

### Centripetal Force = Gravity

For a satellite in circular orbit:

$$\frac{GMm}{r^2} = \frac{mv^2}{r}$$

### Orbital Velocity

$$v = \sqrt{\frac{GM}{r}}$$

Key insights:
- Orbital speed depends only on r, not on satellite mass
- Lower orbit → faster speed
- Geostationary orbit requires a specific r (~42,000 km from Earth centre)

### Orbital Period — Kepler's Third Law

From v = 2πr/T and v = √(GM/r):

$$\frac{2\pi r}{T} = \sqrt{\frac{GM}{r}}$$

$$T^2 = \frac{4\pi^2}{GM} r^3$$

$$T^2 \propto r^3$$

This is **Kepler's Third Law**: the square of the period is proportional to the cube of the semi-major axis (radius for circular orbits).

---

## 5. Geostationary Orbits

A geostationary satellite:
- Orbits above Earth's equator
- Has period T = 24 hours = 86400 s
- Appears stationary from Earth's surface
- Used for communications, weather monitoring

### Finding r for Geostationary Orbit

$$r^3 = \frac{GMT^2}{4\pi^2} = \frac{6.67 \times 10^{-11} \times 5.97 \times 10^{24} \times (86400)^2}{4\pi^2}$$

$$r^3 = 7.54 \times 10^{22} \text{ m}^3$$

$$r \approx 4.22 \times 10^7 \text{ m}$$

Altitude = r − R_Earth ≈ 4.22×10⁷ − 6.37×10⁶ ≈ **3.58 × 10⁷ m ≈ 35,800 km**

---

## Worked Examples

### Worked Example 46.1 — Gravitational Potential at Height

**Problem:** Calculate the gravitational potential at the Earth's surface and at the altitude of the ISS (400 km). M_Earth = 5.97 × 10²⁴ kg, R = 6.37 × 10⁶ m.

**Solution:**

At surface:
$$V_{\text{surface}} = -\frac{GM}{R} = -\frac{6.67 \times 10^{-11} \times 5.97 \times 10^{24}}{6.37 \times 10^6}$$
$$V_{\text{surface}} = -\frac{3.98 \times 10^{14}}{6.37 \times 10^6} = -6.25 \times 10^7 \text{ J/kg}$$

At 400 km altitude (r = 6.77 × 10⁶ m):
$$V_{\text{ISS}} = -\frac{3.98 \times 10^{14}}{6.77 \times 10^6} = -5.88 \times 10^7 \text{ J/kg}$$

ΔV = (−5.88 − (−6.25)) × 10⁷ = **+3.7 × 10⁶ J/kg** (less negative = higher potential)

---

### Worked Example 46.2 — Work to Lift a Satellite

**Problem:** A 2000 kg satellite is launched from Earth's surface to an altitude of 300 km. How much work is done against gravity? M_Earth = 6.0 × 10²⁴ kg, R = 6.37 × 10⁶ m. Use G = 6.67 × 10⁻¹¹.

**Solution:**

$$W = m\Delta V = m \times \left[-\frac{GM}{R+h} - \left(-\frac{GM}{R}\right)\right]$$

$$W = GMm \left(\frac{1}{R} - \frac{1}{R+h}\right)$$

R + h = 6.37×10⁶ + 3.00×10⁵ = 6.67 × 10⁶ m

$$W = 6.67 \times 10^{-11} \times 6.0 \times 10^{24} \times 2000 \times \left(\frac{1}{6.37 \times 10^6} - \frac{1}{6.67 \times 10^6}\right)$$

$$\frac{1}{6.37 \times 10^6} - \frac{1}{6.67 \times 10^6} = 1.570 \times 10^{-7} - 1.499 \times 10^{-7} = 7.06 \times 10^{-9}$$

$$W = 8.00 \times 10^{17} \times 7.06 \times 10^{-9} = \mathbf{5.65 \times 10^9 \text{ J}}$$

Approximately: W ≈ mgh = 2000 × 10 × 3×10⁵ = 6.0 × 10⁹ J — close, validating mgh for small heights.

---

### Worked Example 46.3 — Orbital Speed and Period

**Problem:** A satellite orbits Earth at altitude 500 km. Find:
(a) its orbital speed
(b) its orbital period
M_Earth = 5.97 × 10²⁴ kg, R = 6.37 × 10⁶ m.

**Solution:**

r = R + h = 6.37×10⁶ + 5.00×10⁵ = 6.87 × 10⁶ m

**(a)**
$$v = \sqrt{\frac{GM}{r}} = \sqrt{\frac{6.67 \times 10^{-11} \times 5.97 \times 10^{24}}{6.87 \times 10^6}}$$
$$v = \sqrt{\frac{3.98 \times 10^{14}}{6.87 \times 10^6}} = \sqrt{5.79 \times 10^7} = \mathbf{7.61 \times 10^3 \text{ m/s} = 7.61 \text{ km/s}}$$

**(b)**
$$T = \frac{2\pi r}{v} = \frac{2\pi \times 6.87 \times 10^6}{7.61 \times 10^3} = \frac{4.32 \times 10^7}{7.61 \times 10^3} = \mathbf{5670 \text{ s} \approx 94.5 \text{ minutes}}$$

---

### Worked Example 46.4 — Geostationary Orbit

**Problem:** Verify that a satellite at r = 4.22 × 10⁷ m from Earth's centre is geostationary. M_Earth = 5.97 × 10²⁴ kg.

**Solution:**

Using Kepler's Third Law:
$$T = \sqrt{\frac{4\pi^2 r^3}{GM}} = \sqrt{\frac{4\pi^2 \times (4.22 \times 10^7)^3}{6.67 \times 10^{-11} \times 5.97 \times 10^{24}}}$$

$$T = \sqrt{\frac{4\pi^2 \times 7.52 \times 10^{22}}{3.98 \times 10^{14}}} = \sqrt{\frac{2.97 \times 10^{24}}{3.98 \times 10^{14}}}$$

$$T = \sqrt{7.46 \times 10^9} = 8.64 \times 10^4 \text{ s} = \mathbf{86400 \text{ s} = 24 \text{ hours}}$$

✓ Confirmed!

---

## Practice Problems

### Problem 1
(a) Calculate the gravitational potential at a point 8.0 × 10⁷ m from the centre of Earth. (M = 6.0 × 10²⁴ kg)
(b) A 500 kg spacecraft moves from this point to r = 1.0 × 10⁸ m. Calculate the work done.
(c) Does gravity do this work or must the spacecraft's engines provide it? Explain.

### Problem 2
A satellite is in a circular orbit of radius 7.0 × 10⁶ m around Earth (M = 6.0 × 10²⁴ kg). Calculate:
(a) the orbital speed
(b) the period
(c) the gravitational potential at the orbit

### Problem 3
Two satellites orbit Earth at radii r₁ and r₂ where r₂ = 4r₁. Find the ratio:
(a) v₁ : v₂ (orbital speeds)
(b) T₁ : T₂ (periods)

### Problem 4
The Moon orbits Earth at mean distance 3.84 × 10⁸ m with period 27.3 days.
(a) Use this data to calculate the mass of Earth. (G = 6.67 × 10⁻¹¹)
(b) The Moon's orbital speed is about 1.02 km/s. Verify this using your calculated mass.

### Problem 5 (IB-Style — Satellite Energy)
A 1500 kg satellite is in a circular orbit at altitude 2000 km above Earth. M_Earth = 5.97 × 10²⁴ kg, R_Earth = 6.37 × 10⁶ m, G = 6.67 × 10⁻¹¹.

**(a)** Calculate the gravitational potential V at the satellite's orbit.
**(b)** Determine the satellite's orbital speed and kinetic energy.
**(c)** The satellite fires its thrusters briefly, increasing its speed by 10% while still at the same radius. Explain what happens to the orbit shape.
**(d)** Calculate the minimum additional energy required for the satellite to escape Earth's gravity entirely from its original orbit. (This is the escape energy from the orbit, not from the surface.)

---

## Answers

### Answer 1
**(a)** V = −GM/r = −(6.67×10⁻¹¹)(6.0×10²⁴)/(8.0×10⁷) = −4.0×10¹⁴/8.0×10⁷ = **−5.0 × 10⁶ J/kg**

**(b)** ΔV = V_final − V_initial = [−GM/(1.0×10⁸)] − [−GM/(8.0×10⁷)]
= (−4.0×10¹⁴/1.0×10⁸) − (−5.0×10⁶) = −4.0×10⁶ + 5.0×10⁶ = +1.0×10⁶ J/kg
W = mΔV = 500 × 1.0×10⁶ = **5.0 × 10⁸ J**

**(c)** ΔV is positive (moving to higher potential, farther from Earth), so work must be done **against** gravity. The spacecraft's engines must provide this energy.

---

### Answer 2
**(a)** v = √(GM/r) = √(6.67×10⁻¹¹ × 6.0×10²⁴ / 7.0×10⁶) = √(4.0×10¹⁴/7.0×10⁶) = √(5.71×10⁷) = **7.56 × 10³ m/s**

**(b)** T = 2πr/v = 2π(7.0×10⁶)/7.56×10³ = 4.40×10⁷/7.56×10³ = **5810 s ≈ 97 min**

**(c)** V = −GM/r = −4.0×10¹⁴/7.0×10⁶ = **−5.71 × 10⁷ J/kg**

---

### Answer 3
**(a)** v ∝ 1/√r. v₁/v₂ = √(r₂/r₁) = √(4r₁/r₁) = √4 = **2 : 1** (inner satellite is twice as fast)

**(b)** T ∝ r^(3/2). T₁/T₂ = (r₁/r₂)^(3/2) = (1/4)^(3/2) = 1/8 = **1 : 8** (inner satellite period is 8× shorter)

---

### Answer 4
**(a)** T = 27.3 × 86400 = 2.36 × 10⁶ s
M = 4π²r³/(GT²) = 4π²(3.84×10⁸)³/[6.67×10⁻¹¹(2.36×10⁶)²]
= 4π²(5.66×10²⁵)/(6.67×10⁻¹¹ × 5.57×10¹²) = 2.23×10²⁷/371 = **6.02 × 10²⁴ kg** ✓

**(b)** v = 2πr/T = 2π(3.84×10⁸)/2.36×10⁶ = 2.41×10⁹/2.36×10⁶ = 1.02 × 10³ m/s = **1.02 km/s** ✓

---

### Answer 5 (IB-Style)
**(a)** r = 6.37×10⁶ + 2.00×10⁶ = 8.37×10⁶ m
V = −GM/r = −(6.67×10⁻¹¹)(5.97×10²⁴)/8.37×10⁶ = −3.98×10¹⁴/8.37×10⁶ = **−4.76 × 10⁷ J/kg**

**(b)** v = √(GM/r) = √(3.98×10¹⁴/8.37×10⁶) = √(4.76×10⁷) = 6.90 × 10³ m/s
KE = ½mv² = ½ × 1500 × (6.90×10³)² = 750 × 4.76×10⁷ = **3.57 × 10¹⁰ J**

**(c)** The speed increase at constant radius means the satellite now has excess speed for a circular orbit at that r. The orbit becomes **elliptical**, with the firing point becoming the **perigee** (closest approach), and the satellite will rise to a higher apogee on the opposite side. If it fired retro-rockets (slowing down), the firing point would become the apogee.

**(d)** Escape from this orbit requires total energy E ≥ 0.
Total orbital energy E = −GMm/(2r) = ½ × m × V = ½ × 1500 × (−4.76×10⁷) = −3.57×10¹⁰ J
To escape, energy must go from −3.57×10¹⁰ to 0, so **ΔE = +3.57 × 10¹⁰ J** needed.

---

## Key Takeaways

| Concept | Equation | Notes |
|---------|----------|-------|
| Gravitational potential | V = −GM/r | Scalar, negative, V(∞) = 0 |
| Work done | W = mΔV | Positive work to lift mass |
| Equipotentials | Perpendicular to g | No work along equipotential |
| Field from potential | g = −ΔV/Δr | Steeper V curve = stronger g |
| Orbital velocity | v = √(GM/r) | Independent of satellite mass |
| Kepler's 3rd Law | T² ∝ r³ | T² = 4π²r³/(GM) |
| Geostationary orbit | r ≈ 4.22×10⁷ m | T = 24 hours, above equator |

> **IB Data Booklet:** V = −GM/r, g = −ΔV/Δr, and orbital equations are in Sub-topic 6.2 and 6.1 (HL). The relationship T² ∝ r³ is fundamental. Remember that potential is a scalar (adds directly for multiple masses) while field is a vector.
