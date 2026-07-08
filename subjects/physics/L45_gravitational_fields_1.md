# Lesson 45: Gravitational Fields I — Newton's Law & Field Strength

## What You'll Learn
- Newton's Law of Universal Gravitation: F = GMm/r²
- Gravitational field strength g = F/m = GM/r²
- Field lines for gravitational fields
- How g varies with distance from a planet
- Calculating g on different planets and at altitude

---

## 1. Newton's Law of Universal Gravitation

Every particle in the universe attracts every other particle with a force that is:
- Proportional to the product of their masses
- Inversely proportional to the square of the distance between their centers

$$F = \frac{GMm}{r^2}$$

where:
- **F** = gravitational force (N)
- **G** = universal gravitational constant = 6.67 × 10⁻¹¹ N·m²/kg²
- **M** = mass of first body (kg)
- **m** = mass of second body (kg)
- **r** = distance between centres of mass (m)

> **G** is given in the IB Data Booklet (Sub-topic 6.1).

### Key Properties

- **Always attractive** — gravity never repels
- **Inverse square law** — double the distance → force becomes ¼
- **Acts along the line joining centres**
- **Applies to point masses and spherically symmetric bodies**

### Vector Form

$$\vec{F} = -\frac{GMm}{r^2} \hat{r}$$

The negative sign indicates the force is attractive (toward the source mass).

---

## 2. Gravitational Field Strength g

### Definition

The gravitational field strength **g** at a point is the force per unit mass experienced by a small test mass placed at that point:

$$g = \frac{F}{m}$$

### Field Due to a Point Mass (or Spherical Body)

For a body of mass M at distance r from its centre:

$$g = \frac{GM}{r^2}$$

**Units:** N/kg (which is equivalent to m/s² — this is why g is also called "acceleration due to gravity")

### Direction

g is a vector pointing **toward** the centre of the mass creating the field.

---

## 3. Gravitational Field Lines

Field lines show the direction of the gravitational force on a test mass.

### Properties

| Property | Description |
|----------|-------------|
| Direction | Point toward the mass (inward, radial) |
| Spacing | Closer lines = stronger field |
| Origin | Start at infinity, end on the mass |
| Never cross | Field is single-valued at each point |

```
Field around a point mass (2D cross-section):

        ↘ ↓ ↙
    → → → ● ← ← ←
        ↗ ↑ ↖

(All arrows point INWARD toward the mass)
```

### Near Earth's Surface

Close to Earth's surface, the field is approximately **uniform**:
- g ≈ 9.81 N/kg (we use g = 10 m/s² in problems)
- Field lines are parallel and equally spaced
- Direction: downward

---

## 4. g at the Surface of Planets

For a planet of mass M and radius R:

$$g_{\text{surface}} = \frac{GM}{R^2}$$

### g on Different Planets

| Body | Mass (kg) | Radius (m) | g_surface (m/s²) |
|------|-----------|------------|-----------------|
| Earth | 5.97 × 10²⁴ | 6.37 × 10⁶ | ~9.8 |
| Moon | 7.35 × 10²² | 1.74 × 10⁶ | ~1.6 |
| Mars | 6.42 × 10²³ | 3.39 × 10⁶ | ~3.7 |
| Jupiter | 1.90 × 10²⁷ | 6.99 × 10⁷ | ~24.8 |

---

## 5. Variation of g with Distance

### g vs r Graph

```
g
↑
| ╲
|   ╲    g ∝ 1/r²  (above surface)
|     ╲
|       ╲________
|       /        ╲
|      /           ╲
|     /  g ∝ r       ╲
|    / (inside Earth)  ╲
|   /                    ╲
0──┼──────────────────────────→ r
   0    R                  distance from centre
```

**Key regions:**
- **r ≥ R** (on or above surface): g = GM/r², decreases as 1/r²
- **r < R** (inside, assuming uniform density): g ∝ r (field decreases linearly to zero at the centre)

### g at Altitude

At height h above Earth's surface (r = R + h):

$$g_h = \frac{GM}{(R + h)^2}$$

Alternatively, relating to surface g:

$$\frac{g_h}{g_{\text{surface}}} = \frac{R^2}{(R + h)^2}$$

---

## Worked Examples

### Worked Example 45.1 — g at Altitude

**Problem:** Calculate the gravitational field strength at the orbit of the International Space Station (h = 400 km above Earth's surface). 
Given: M_Earth = 5.97 × 10²⁴ kg, R_Earth = 6.37 × 10⁶ m, G = 6.67 × 10⁻¹¹.

**Solution:**

r = R + h = 6.37×10⁶ + 4.00×10⁵ = 6.77 × 10⁶ m

$$g = \frac{GM}{r^2} = \frac{6.67 \times 10^{-11} \times 5.97 \times 10^{24}}{(6.77 \times 10^6)^2}$$

$$g = \frac{3.98 \times 10^{14}}{4.58 \times 10^{13}} = 8.69 \text{ N/kg}$$

Note: g at 400 km is still 89% of surface g. Astronauts feel weightless not because g is small, but because they're in free fall!

---

### Worked Example 45.2 — Mass of Earth from g

**Problem:** Given g = 10 N/kg at Earth's surface and R = 6.37 × 10⁶ m, calculate the mass of Earth. (Use G = 6.67 × 10⁻¹¹.)

**Solution:**

From g = GM/R²:
$$M = \frac{g R^2}{G} = \frac{10 \times (6.37 \times 10^6)^2}{6.67 \times 10^{-11}}$$

$$M = \frac{10 \times 4.06 \times 10^{13}}{6.67 \times 10^{-11}} = \frac{4.06 \times 10^{14}}{6.67 \times 10^{-11}} = 6.09 \times 10^{24} \text{ kg}$$

Close to the accepted value of 5.97 × 10²⁴ kg (the difference is from using g = 10 instead of 9.81).

---

### Worked Example 45.3 — Force Between Two Masses

**Problem:** Two identical spherical masses, each 100 kg, have their centres 2.0 m apart. Calculate:
(a) the gravitational force between them
(b) Compare this to the weight of a 100 kg mass on Earth (g = 10 m/s²)

**Solution:**

**(a)**
$$F = \frac{GMm}{r^2} = \frac{6.67 \times 10^{-11} \times 100 \times 100}{2.0^2}$$
$$F = \frac{6.67 \times 10^{-7}}{4.0} = 1.67 \times 10^{-7} \text{ N}$$

**(b)** Weight = mg = 100 × 10 = 1000 N.
Ratio = 1000 / (1.67×10⁻⁷) ≈ **6 × 10⁹** — gravity is extremely weak compared to other forces! The only reason we feel it strongly is because Earth is so massive.

---

### Worked Example 45.4 — g on Mars Surface

**Problem:** Calculate g on the surface of Mars.
M_Mars = 6.42 × 10²³ kg, R_Mars = 3.39 × 10⁶ m.

**Solution:**

$$g_{\text{Mars}} = \frac{GM}{R^2} = \frac{6.67 \times 10^{-11} \times 6.42 \times 10^{23}}{(3.39 \times 10^6)^2}$$

$$g_{\text{Mars}} = \frac{4.28 \times 10^{13}}{1.15 \times 10^{13}} = 3.72 \text{ N/kg}$$

An astronaut weighing 700 N on Earth would weigh only 700 × (3.72/10) = 260 N on Mars.

---

## Practice Problems

### Problem 1
Calculate the gravitational force between Earth (M = 5.97 × 10²⁴ kg) and the Moon (m = 7.35 × 10²² kg) if their centres are 3.84 × 10⁸ m apart.

### Problem 2
A satellite of mass 500 kg orbits Earth at an altitude where g = 5.0 N/kg.
(a) What is the gravitational force on the satellite?
(b) How far from Earth's centre is the satellite? (M_Earth = 6.0 × 10²⁴ kg, G = 6.67 × 10⁻¹¹)

### Problem 3
Planet X has twice the mass and twice the radius of Earth. Earth's surface g = 10 N/kg.
(a) Calculate the surface gravity of Planet X.
(b) Explain why doubling both M and R doesn't give the same g.

### Problem 4
At what altitude above Earth's surface does g become 2.5 N/kg (one quarter of surface value)? R_Earth = 6.37 × 10⁶ m.

### Problem 5 (IB-Style — g vs r Graph)
A planet has a solid core of uniform density. The planet's radius is R.

**(a)** Sketch and label a graph of g vs distance r from the planet's centre, for r = 0 to r = 3R.

**(b)** On the same axes, sketch the g vs r graph for a second planet with the same mass but half the radius. Explain the key differences.

**(c)** The escape velocity from the first planet is v_esc. For the second planet (same mass, half radius), state whether the escape velocity is greater than, less than, or equal to v_esc. Justify your answer.

---

## Answers

### Answer 1
F = GMm/r² = (6.67×10⁻¹¹)(5.97×10²⁴)(7.35×10²²)/(3.84×10⁸)²
= (2.93×10³⁷)/(1.47×10¹⁷) = **1.99 × 10²⁰ N**

(This enormous force keeps the Moon in orbit!)

---

### Answer 2
**(a)** F = mg = 500 × 5.0 = **2500 N**

**(b)** g = GM/r² → r = √(GM/g) = √[(6.67×10⁻¹¹ × 6.0×10²⁴)/5.0]
= √(4.0×10¹⁴ / 5.0) = √(8.0×10¹³) = **8.94 × 10⁶ m**

Altitude = r − R = 8.94×10⁶ − 6.37×10⁶ = 2.57 × 10⁶ m = **2570 km**

---

### Answer 3
**(a)** g ∝ M/R². If M → 2M and R → 2R:
g_new = G(2M)/(2R)² = 2GM/4R² = (1/2)(GM/R²) = g_earth/2 = **5.0 N/kg**

**(b)** Mass scales linearly (×2), but radius squared scales quadratically (×4). The inverse square dependence on radius dominates — gravity is halved even though mass doubled. Surface gravity depends on both M and R², with R² in the denominator being more "powerful."

---

### Answer 4
g ∝ 1/r², so g/g₀ = (R/r)²
2.5/10 = (R/r)² → (R/r)² = 0.25 → R/r = 0.5 → r = 2R
r = 2 × 6.37×10⁶ = 1.274×10⁷ m
Altitude = r − R = **6.37 × 10⁶ m** (one Earth radius up)

At h = R, g = g_surface/4.

---

### Answer 5 (IB-Style)
**(a)** The graph should show:
- r = 0 to R: g ∝ r (linear increase from 0 to g_surface)
- r ≥ R: g ∝ 1/r² (hyperbolic decrease)
- Sharp peak at r = R

**(b)** Planet 2 (same M, half R):
- Surface g is 4× larger (g ∝ 1/R²)
- Inside: g ∝ r but reaches a higher peak at R/2
- Outside: Same g at same r (since same M, g = GM/r²)
- So the graph for r < R/2 is steeper, peaks at R/2 at 4× the height, then drops as 1/r² but shifted left.

**(c)** Escape velocity v_esc = √(2GM/R). With same M and half R, v_esc_new = √(2GM/(R/2)) = √(4GM/R) = √2 × √(2GM/R) = √2 × v_esc.

**Greater.** The smaller radius means you're deeper in the gravitational well, starting closer to the centre where the potential is more negative.

---

## Key Takeaways

| Concept | Equation | Notes |
|---------|----------|-------|
| Newton's law | F = GMm/r² | Always attractive, inverse square |
| Field strength | g = F/m = GM/r² | Vector pointing toward mass |
| Surface g | g = GM/R² | Depends on M and R |
| g at altitude | g_h = g₀ × R²/(R + h)² | Decreases with height |
| Inside planet | g ∝ r (uniform density) | Zero at centre |
| G value | 6.67 × 10⁻¹¹ N·m²/kg² | Very small — gravity is weak |

> **IB Data Booklet:** F = GMm/r² and g = F/m are given in Sub-topic 6.1. The Data Booklet also provides values for G, Earth mass, and Earth radius. Always use consistent SI units: force in N, mass in kg, distance in m.
