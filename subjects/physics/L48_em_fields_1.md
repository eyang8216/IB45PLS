# Lesson 48: Electric & Magnetic Fields I — Coulomb's Law & E-Fields

## What You'll Learn
- Electric charge conservation, conductors vs insulators
- Coulomb's Law: F = kq₁q₂/r²
- Electric field strength E = F/q
- Field due to a point charge: E = kQ/r²
- Uniform E-field between parallel plates: E = V/d

---

## 1. Electric Charge — Fundamental Properties

### Charge Conservation

Electric charge cannot be created or destroyed — it can only be transferred. The net charge of an isolated system is constant.

### Quantization of Charge

Charge comes in discrete units:
$$e = 1.60 \times 10^{-19} \text{ C}$$

All charges are integer multiples of e: q = ne, n = ±1, ±2, ±3, ...

### Conductors vs Insulators

| Property | Conductors | Insulators |
|----------|-----------|------------|
| Charge movement | Free electrons can flow | Electrons tightly bound |
| Examples | Metals (copper, silver), graphite | Rubber, glass, plastic |
| Charging | Charge distributes over surface | Charge stays where deposited |
| Electric field inside | Zero (in electrostatic equilibrium) | Can be non-zero |

### Charging Methods

- **Friction:** Rubbing transfers electrons (triboelectric effect)
- **Conduction:** Contact with charged object
- **Induction:** Bringing a charged object near (without contact) causes charge separation, then grounding fixes the charge

---

## 2. Coulomb's Law

The force between two point charges is proportional to the product of the charges and inversely proportional to the square of the separation:

$$F = \frac{k q_1 q_2}{r^2}$$

where:
- **k** = Coulomb constant = 8.99 × 10⁹ N·m²/C²
- **q₁, q₂** = charges (C) — signs matter!
- **r** = separation (m)

In terms of permittivity of free space ε₀:
$$k = \frac{1}{4\pi\varepsilon_0}$$

$$\varepsilon_0 = 8.85 \times 10^{-12} \text{ C}^2\text{/N·m}^2$$

### Sign and Direction

- Like charges (both + or both −): **repel** → F positive (away from each other)
- Unlike charges (+ and −): **attract** → F negative (toward each other)
- Force acts along the line joining the charges

### Comparison with Gravity

| | Electrostatic | Gravitational |
|---|---|---|
| Formula | F = kq₁q₂/r² | F = Gm₁m₂/r² |
| Constant | k ≈ 9×10⁹ | G ≈ 6.67×10⁻¹¹ |
| Force can be | Attractive or repulsive | Only attractive |
| Relative strength | ~10³⁶× stronger | Extremely weak |

---

## 3. Electric Field Strength E

### Definition

The electric field at a point is the force per unit charge experienced by a small positive test charge placed at that point:

$$E = \frac{F}{q}$$

**Units:** N/C (equivalent to V/m)

### Field Due to a Point Charge

$$E = \frac{kQ}{r^2} = \frac{Q}{4\pi\varepsilon_0 r^2}$$

### Direction

- Away from positive charges (+Q → E points outward)
- Toward negative charges (−Q → E points inward)

```
+Q                    −Q
 ↑ → · ← ↓           ↓ → · ← ↑
(E outward)          (E inward)
```

---

## 4. Electric Field Lines

### Rules

| Rule | Description |
|------|-------------|
| Start/End | Start on + charges, end on − charges |
| Density | More lines = stronger field |
| Direction | Tangent to line = direction of E |
| Never cross | Field is single-valued at each point |
| Perpendicular | Perpendicular to conductor surfaces |

### Common Configurations

**Single positive charge:** Radial lines outward
**Single negative charge:** Radial lines inward
**Dipole (+ and −):** Curved lines from + to −
**Two like charges:** Lines repel between them, null point in between

---

## 5. Uniform Electric Field — Parallel Plates

When two parallel conducting plates are connected to a potential difference (battery), a **uniform** E-field is established between them (ignoring edge effects).

$$E = \frac{V}{d}$$

where:
- **V** = potential difference between plates (volts)
- **d** = plate separation (m)

```
    + + + + + + + + + + +
    |                     |
    ↓  ↓  ↓  ↓  ↓  ↓  ↓   ← Uniform E-field (everywhere same strength & direction)
    |                     |
    − − − − − − − − − − −
```

### Force on a Charge in Uniform Field

$$F = qE = \frac{qV}{d}$$

- Positive charge: force **in direction of E** (toward negative plate)
- Negative charge: force **opposite to E** (toward positive plate)

### Acceleration

$$a = \frac{F}{m} = \frac{qE}{m} = \frac{qV}{md}$$

---

## Worked Examples

### Worked Example 48.1 — Force Between Charges

**Problem:** Two point charges, +3.0 μC and −5.0 μC, are placed 0.20 m apart. Find the magnitude and direction of the force on each charge.

**Solution:**

$$F = \frac{k q_1 q_2}{r^2} = \frac{8.99 \times 10^9 \times (3.0 \times 10^{-6}) \times (5.0 \times 10^{-6})}{(0.20)^2}$$

$$F = \frac{8.99 \times 10^9 \times 1.5 \times 10^{-11}}{0.040} = \frac{0.1349}{0.040} = 3.37 \text{ N}$$

Force is **attractive** (unlike charges). The +3.0 μC charge is pulled toward the −5.0 μC charge, and vice versa. Magnitude: **3.37 N** on each.

---

### Worked Example 48.2 — E-field at a Point

**Problem:** Find the electric field at a point 0.15 m from a +4.0 μC point charge.

**Solution:**

$$E = \frac{kQ}{r^2} = \frac{8.99 \times 10^9 \times 4.0 \times 10^{-6}}{(0.15)^2}$$

$$E = \frac{3.596 \times 10^4}{0.0225} = \mathbf{1.60 \times 10^6 \text{ N/C}}$$

Direction: radially **outward** from the charge (away from +).

---

### Worked Example 48.3 — Electron in Uniform Field

**Problem:** An electron enters a uniform electric field between two parallel plates separated by 0.020 m with a potential difference of 100 V. Find:
(a) the electric field strength between the plates
(b) the force on the electron
(c) the acceleration of the electron (e = 1.60 × 10⁻¹⁹ C, mₑ = 9.11 × 10⁻³¹ kg)

**Solution:**

**(a)**
$$E = \frac{V}{d} = \frac{100}{0.020} = \mathbf{5.0 \times 10^3 \text{ V/m}}$$

**(b)**
$$F = qE = 1.60 \times 10^{-19} \times 5.0 \times 10^3 = \mathbf{8.0 \times 10^{-16} \text{ N}}$$

Direction: opposite to E (electron is negative → force toward positive plate).

**(c)**
$$a = \frac{F}{m} = \frac{8.0 \times 10^{-16}}{9.11 \times 10^{-31}} = \mathbf{8.78 \times 10^{14} \text{ m/s}^2}$$

This enormous acceleration shows how strongly electric fields affect electrons!

---

### Worked Example 48.4 — Null Point Between Charges

**Problem:** Two charges +9.0 μC and +4.0 μC are placed 1.0 m apart. Find the point on the line between them where the net electric field is zero.

**Solution:**

Let the null point be at distance x from the 9.0 μC charge. The fields must be equal in magnitude and opposite in direction:

$$\frac{k \times 9.0 \times 10^{-6}}{x^2} = \frac{k \times 4.0 \times 10^{-6}}{(1.0 - x)^2}$$

Cancel k and 10⁻⁶:
$$\frac{9.0}{x^2} = \frac{4.0}{(1.0 - x)^2}$$

Take square root of both sides:
$$\frac{3.0}{x} = \frac{2.0}{1.0 - x}$$

Cross multiply: 3.0(1.0 − x) = 2.0x
3.0 − 3.0x = 2.0x
3.0 = 5.0x
**x = 0.60 m** from the 9.0 μC charge.

Check: at 0.60 m from 9 μC → E₁ = k×9/(0.36) = 25k. At 0.40 m from 4 μC → E₂ = k×4/(0.16) = 25k. Equal magnitude, opposite direction ✓

---

## Practice Problems

### Problem 1
Two point charges of +2.0 μC and +8.0 μC are 0.30 m apart. Calculate:
(a) the force between them (magnitude and type)
(b) the electric field at the midpoint between them

### Problem 2
A proton (q = +1.60 × 10⁻¹⁹ C, m = 1.67 × 10⁻²⁷ kg) is placed in a uniform electric field of 2.0 × 10⁴ N/C.
(a) Find the force on the proton.
(b) Calculate its acceleration.
(c) If it starts from rest, how fast is it moving after 1.0 μs?

### Problem 3
Two parallel plates are separated by 5.0 mm and connected to a 200 V battery.
(a) What is the E-field between the plates?
(b) An electron enters this field. What is the magnitude of the force on it?
(c) If the electron enters at 3.0 × 10⁶ m/s parallel to the plates, sketch its path and explain.

### Problem 4
Three point charges form an equilateral triangle of side 0.10 m: q₁ = +3.0 μC, q₂ = +3.0 μC, q₃ = −3.0 μC. Find the net electric field at the midpoint of the side connecting q₁ and q₂.

### Problem 5 (IB-Style — Charge Configuration)
Two identical small conducting spheres, A and B, carry charges of +6.0 nC and −2.0 nC respectively. They are touched together briefly and then separated to a distance of 12 cm.

**(a)** State the charge on each sphere after separation. Justify your answer.
**(b)** Calculate the electrostatic force between them after separation.
**(c)** A third identical sphere C, initially uncharged, is now brought into contact with sphere A, then removed. Sphere C is then brought into contact with sphere B, then removed. Calculate the final charge on each sphere.
**(d)** Sphere A (with its charge from part c) is placed at the origin (0,0). Sphere B (with its charge from part c) is placed at (0.12 m, 0). Calculate the net electric field at the point (0.06 m, 0.08 m) — directly above the midpoint.

---

## Answers

### Answer 1
**(a)** F = kq₁q₂/r² = 8.99×10⁹ × 2.0×10⁻⁶ × 8.0×10⁻⁶/(0.30)² = 143.8×10⁻³/0.09 = **1.60 N repulsive** (both positive)

**(b)** At midpoint (0.15 m from each): 
E₁ = k×2.0×10⁻⁶/(0.15)² = 8.99×10⁹×2.0×10⁻⁶/0.0225 = 7.99×10⁵ N/C (away from q₁)
E₂ = k×8.0×10⁻⁶/(0.15)² = 3.20×10⁶ N/C (away from q₂)
E_net = 3.20×10⁶ − 7.99×10⁵ = **2.40 × 10⁶ N/C** toward the smaller charge.

---

### Answer 2
**(a)** F = qE = 1.60×10⁻¹⁹ × 2.0×10⁴ = **3.20 × 10⁻¹⁵ N** in direction of E

**(b)** a = F/m = 3.20×10⁻¹⁵/1.67×10⁻²⁷ = **1.92 × 10¹² m/s²**

**(c)** v = u + at = 0 + 1.92×10¹² × 1.0×10⁻⁶ = **1.92 × 10⁶ m/s**

---

### Answer 3
**(a)** E = V/d = 200/(5.0×10⁻³) = **4.0 × 10⁴ V/m**

**(b)** F = eE = 1.60×10⁻¹⁹ × 4.0×10⁴ = **6.4 × 10⁻¹⁵ N**

**(c)** The electron enters parallel to plates with horizontal speed 3.0×10⁶ m/s. The E-field exerts a force toward the positive plate (electron is negative, so opposite to E direction). This causes parabolic motion — constant horizontal velocity, constant vertical acceleration — just like projectile motion. Path: parabola curving toward the positive plate.

---

### Answer 4
The midpoint of q₁−q₂: fields from q₁ and q₂ cancel (equal magnitude, opposite direction — both positive, so both point away, toward the midpoint from opposite sides → cancel).

Only q₃ contributes. Distance from q₃ to midpoint: the altitude of the equilateral triangle = 0.10 × √3/2 = 0.0866 m.

E = k|q₃|/r² = 8.99×10⁹ × 3.0×10⁻⁶/(0.0866)² = 2.697×10⁴/0.0075 = **3.60 × 10⁶ N/C**

Direction: toward q₃ (since q₃ is negative, field points toward it).

---

### Answer 5 (IB-Style)
**(a)** When conducting spheres touch, charge distributes equally (they're identical). Total charge = +6.0 + (−2.0) = +4.0 nC. Each gets +2.0 nC.

**(b)** F = k(2.0×10⁻⁹)²/(0.12)² = 8.99×10⁹ × 4.0×10⁻¹⁸/0.0144 = **2.50 × 10⁻⁶ N repulsive**

**(c)** Step 1: C touches A (A has +2.0 nC, C has 0). Total = +2.0 nC → each gets +1.0 nC. A = +1.0 nC, C = +1.0 nC.
Step 2: C (now +1.0 nC) touches B (+2.0 nC). Total = +3.0 nC → each gets +1.5 nC.
Final: **A = +1.0 nC, B = +1.5 nC, C = +1.5 nC**

**(d)** At (0.06, 0.08): distance to A = distance to B = √(0.06² + 0.08²) = 0.10 m.
E_A = k(1.0×10⁻⁹)/(0.10)² = 8.99×10⁹×1.0×10⁻⁹/0.01 = 899 N/C, direction: away from A at angle.
E_B = k(1.5×10⁻⁹)/(0.10)² = 1349 N/C, direction: away from B at angle.

Components: E_A_x = 899 × (0.06/0.10) = 539 N/C right
E_A_y = 899 × (0.08/0.10) = 719 N/C up
E_B_x = 1349 × (−0.06/0.10) = −809 N/C (left)
E_B_y = 1349 × (0.08/0.10) = 1079 N/C up

E_net_x = 539 − 809 = −270 N/C
E_net_y = 719 + 1079 = 1798 N/C

Magnitude: √(270² + 1798²) = **1818 N/C**
Direction: θ = tan⁻¹(1798/270) ≈ **81.5° above the negative x-axis** (pointing up and mostly left).

---

## Key Takeaways

| Concept | Equation | Notes |
|---------|----------|-------|
| Coulomb's Law | F = kq₁q₂/r² | k = 8.99×10⁹ N·m²/C² |
| E-field definition | E = F/q | N/C or V/m |
| Point charge E-field | E = kQ/r² | Direction: away from +, toward − |
| Parallel plate E-field | E = V/d | Uniform between plates |
| Charge of electron | e = 1.60 × 10⁻¹⁹ C | Quantized! |
| ε₀ | 8.85 × 10⁻¹² C²/N·m² | k = 1/(4πε₀) |

> **IB Data Booklet:** F = kq₁q₂/r², E = F/q, E = kQ/r², and E = V/d are given in Sub-topic 5.1. The Data Booklet provides k, ε₀, and e values. Electric field is a vector — always consider direction when adding fields from multiple charges.
