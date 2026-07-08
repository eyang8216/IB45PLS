# Lesson 49: Electric & Magnetic Fields II — Electric Potential

## What You'll Learn
- Electric potential V = kQ/r (scalar!)
- Potential due to multiple charges: simple scalar addition
- Equipotential surfaces in electric fields
- The electronvolt (eV): energy unit for atomic physics
- Relationship between E-field and potential: E = −ΔV/Δr

---

## 1. Electric Potential V

### Definition

Electric potential at a point is the **work done per unit charge** to bring a small positive test charge from **infinity** to that point.

$$V = \frac{kQ}{r} = \frac{Q}{4\pi\varepsilon_0 r}$$

where:
- **V** = electric potential (volts, V = J/C)
- **r** = distance from point charge Q (m)
- Reference: V(∞) = 0

### Sign of Potential

- **Positive charge** (+Q): V is **positive** (work done AGAINST repulsion to bring + test charge in)
- **Negative charge** (−Q): V is **negative** (work done BY attraction as + test charge comes in)

### Why Scalar Matters

Unlike the electric field (vector), potential is a **scalar**. For multiple charges, you just add the potentials algebraically:

$$V_{\text{total}} = V_1 + V_2 + V_3 + ... = \frac{kq_1}{r_1} + \frac{kq_2}{r_2} + \frac{kq_3}{r_3} + ...$$

No vector components needed! This makes potential calculations much simpler than field calculations.

---

## 2. Potential Difference and Work Done

### Potential Difference (Voltage)

$$\Delta V = V_B - V_A$$

### Work Done to Move a Charge

$$W = q \Delta V$$

- If ΔV > 0 (moving to higher potential): work done **on** charge by external agent
- If ΔV < 0 (moving to lower potential): work done **by** field on charge

### Energy Gained by Accelerated Charge

When a charge q moves freely through a potential difference ΔV:

$$\Delta KE = q\Delta V$$

$$v = \sqrt{\frac{2q\Delta V}{m}} \quad (\text{starting from rest})$$

---

## 3. The Electronvolt (eV)

### Definition

One electronvolt is the energy gained (or lost) by one electron when it moves through a potential difference of 1 volt.

$$1 \text{ eV} = 1.60 \times 10^{-19} \text{ J}$$

### Why eV?

Atomic and subatomic energies are tiny in joules. An electron accelerated through 100 V gains:

$$KE = 100 \text{ eV} = 100 \times 1.60 \times 10^{-19} = 1.60 \times 10^{-17} \text{ J}$$

Much more convenient to say "100 eV" than "1.60 × 10⁻¹⁷ J"!

### Conversion

| To convert... | Multiply by... |
|--------------|----------------|
| eV → J | 1.60 × 10⁻¹⁹ |
| J → eV | 6.25 × 10¹⁸ |
| MeV → J | 1.60 × 10⁻¹³ |
| GeV → J | 1.60 × 10⁻¹⁰ |

---

## 4. Equipotential Surfaces

### Definition

An equipotential surface is a surface on which the potential is constant everywhere.

### Properties

| Property | Description |
|----------|-------------|
| Orientation | **Perpendicular** to E-field lines everywhere |
| Work | No work is done moving a charge along an equipotential (ΔV = 0) |
| Spacing | Closer equipotentials = stronger E-field |
| Shape for point charge | Concentric spheres centred on the charge |

### Visualizing Equipotentials

```
Point charge (+Q):

   E-field lines (radial outward)
        → → →
       ←—·—→     ← equipotential circles (spheres in 3D)
        → → →
```

---

## 5. Relationship Between E and V

### Field as Potential Gradient

$$E = -\frac{\Delta V}{\Delta r}$$

In words: the electric field strength is the **negative gradient** of the potential.

- The steeper the V-vs-r graph, the stronger the E-field
- E points in the direction of **decreasing** V

### For Parallel Plates

$$E = \frac{V}{d}$$

This is the uniform field case. The potential drops linearly from the positive plate to the negative plate.

### For a Point Charge

$$E = \frac{kQ}{r^2}, \quad V = \frac{kQ}{r}$$

Check: E = −dV/dr = −d(kQ/r)/dr = −(−kQ/r²) = kQ/r² ✓

---

## 6. Electron Accelerated Through a p.d.

This is one of the most common IB problems. An electron (or proton) is accelerated from rest through a potential difference V:

### Electron Speed

$$\frac{1}{2}mv^2 = eV$$

$$v = \sqrt{\frac{2eV}{m}}$$

### Example Values

| ΔV | Electron speed | Proton speed |
|----|----------------|--------------|
| 100 V | 5.93 × 10⁶ m/s | 1.38 × 10⁵ m/s |
| 1000 V | 1.87 × 10⁷ m/s | 4.38 × 10⁵ m/s |
| 10 kV | 5.93 × 10⁷ m/s | 1.38 × 10⁶ m/s |

Note: For V ≥ ~10 kV, relativistic corrections become significant for electrons (v approaches c).

---

## Worked Examples

### Worked Example 49.1 — Potential at Midpoint

**Problem:** Charges of +4.0 μC and −2.0 μC are 0.60 m apart. Find the electric potential at the midpoint.

**Solution:**

Midpoint: r = 0.30 m from each charge.

$$V = \frac{kq_1}{r} + \frac{kq_2}{r} = \frac{k}{r}(q_1 + q_2) = \frac{8.99 \times 10^9}{0.30} \times (4.0 \times 10^{-6} + (-2.0) \times 10^{-6})$$

$$V = 3.00 \times 10^{10} \times 2.0 \times 10^{-6} = \mathbf{6.0 \times 10^4 \text{ V}}$$

Note: even though one charge is negative, potential is positive here because the +4.0 μC contribution is larger.

---

### Worked Example 49.2 — Work to Move a Charge

**Problem:** A +3.0 nC charge is moved from a point where V = 500 V to a point where V = −200 V. Find:
(a) the potential difference
(b) the work done

**Solution:**

**(a)** ΔV = V_final − V_initial = −200 − 500 = **−700 V**

**(b)** W = qΔV = 3.0×10⁻⁹ × (−700) = **−2.1 × 10⁻⁶ J**

Negative work means the field does the work — the charge naturally moves to lower potential (positive charge moves toward negative charges).

---

### Worked Example 49.3 — eV Conversion and Electron Speed

**Problem:** An electron is accelerated from rest through 5000 V.
(a) Find its kinetic energy in eV and joules.
(b) Calculate its final speed. (e = 1.60×10⁻¹⁹ C, mₑ = 9.11×10⁻³¹ kg)
(c) A proton accelerated through the same p.d. — how does its speed compare?

**Solution:**

**(a)** KE = 5000 eV = 5000 × 1.60×10⁻¹⁹ = **8.00 × 10⁻¹⁶ J**

**(b)**
$$v = \sqrt{\frac{2eV}{m}} = \sqrt{\frac{2 \times 1.60 \times 10^{-19} \times 5000}{9.11 \times 10^{-31}}}$$
$$v = \sqrt{\frac{1.60 \times 10^{-15}}{9.11 \times 10^{-31}}} = \sqrt{1.756 \times 10^{15}} = \mathbf{4.19 \times 10^7 \text{ m/s}}$$

(About 14% of the speed of light — relativistic effects are becoming noticeable.)

**(c)** Proton mass = 1.67×10⁻²⁷ kg (1836× heavier). 
v_p = √(2eV/m_p). Since m_p/mₑ = 1836, v_p/vₑ = √(mₑ/m_p) = 1/√1836 ≈ 1/42.8.
v_p ≈ 4.19×10⁷/42.8 = **9.79 × 10⁵ m/s** — much slower!

---

### Worked Example 49.4 — Potential Due to Multiple Charges

**Problem:** Three charges lie on a line: q₁ = +2.0 μC at x = 0, q₂ = −3.0 μC at x = 0.20 m, q₃ = +4.0 μC at x = 0.50 m. Find the potential at x = 0.35 m (between q₂ and q₃).

**Solution:**

Distances: r₁ = 0.35 m, r₂ = 0.15 m, r₃ = 0.15 m.

$$V = k\left(\frac{q_1}{r_1} + \frac{q_2}{r_2} + \frac{q_3}{r_3}\right)$$

$$V = 8.99 \times 10^9 \left(\frac{2.0 \times 10^{-6}}{0.35} + \frac{-3.0 \times 10^{-6}}{0.15} + \frac{4.0 \times 10^{-6}}{0.15}\right)$$

$$V = 8.99 \times 10^9 \left(5.71 \times 10^{-6} - 2.00 \times 10^{-5} + 2.67 \times 10^{-5}\right)$$

$$V = 8.99 \times 10^9 \times 1.24 \times 10^{-5} = \mathbf{1.11 \times 10^5 \text{ V}}$$

---

## Practice Problems

### Problem 1
Calculate the electric potential at a distance of 0.50 m from a +6.0 μC point charge. How much work is required to bring a +2.0 μC charge from infinity to this point?

### Problem 2
Two parallel plates are 2.0 cm apart with a 500 V potential difference.
(a) Find the E-field between the plates.
(b) An electron starts from rest at the negative plate. What is its speed when it reaches the positive plate?
(c) Express the electron's final kinetic energy in eV.

### Problem 3
Charges +5.0 μC and −5.0 μC are placed at opposite corners of a square of side 0.40 m. Find the potential at the other two corners (the "empty" corners).

### Problem 4
An alpha particle (q = +2e, m = 6.64 × 10⁻²⁷ kg) is accelerated from rest through 2000 V. Find:
(a) its kinetic energy in eV and joules
(b) its final speed

### Problem 5 (IB-Style — Potential Graph)
Charges q₁ = +4.0 nC and q₂ = −2.0 nC are fixed on the x-axis at x = −0.20 m and x = +0.20 m respectively.

**(a)** Calculate the potential at x = 0 (the origin).
**(b)** Calculate the potential at x = 0.50 m.
**(c)** A positive test charge of +1.0 nC is released from rest at x = 0.50 m. Describe its subsequent motion qualitatively.
**(d)** There is a point on the x-axis to the right of q₂ where V = 0. Find this point.

---

## Answers

### Answer 1
V = kQ/r = 8.99×10⁹ × 6.0×10⁻⁶ / 0.50 = **1.08 × 10⁵ V**
W = qV = 2.0×10⁻⁶ × 1.08×10⁵ = **0.216 J**

---

### Answer 2
**(a)** E = V/d = 500/0.020 = **2.5 × 10⁴ V/m**

**(b)** ½mv² = eV → v = √(2eV/m) = √(2 × 1.60×10⁻¹⁹ × 500 / 9.11×10⁻³¹)
= √(1.60×10⁻¹⁶/9.11×10⁻³¹) = √(1.756×10¹⁴) = **1.33 × 10⁷ m/s**

**(c)** KE = **500 eV** (the potential difference in volts = the KE in eV for an electron!)

---

### Answer 3
At an empty corner: distance to +5.0 μC is 0.40 m, distance to −5.0 μC is diagonal = √(0.40² + 0.40²) = 0.566 m.

V = k(5.0×10⁻⁶/0.40 + (−5.0×10⁻⁶)/0.566)
= 8.99×10⁹(1.25×10⁻⁵ − 8.83×10⁻⁶)
= 8.99×10⁹ × 3.67×10⁻⁶ = **3.30 × 10⁴ V**

By symmetry, both empty corners have the same potential.

---

### Answer 4
**(a)** KE = qV = 2e × 2000 = **4000 eV** (= 4 keV)
In joules: 4000 × 1.60×10⁻¹⁹ = **6.40 × 10⁻¹⁶ J**

**(b)** v = √(2KE/m) = √(2 × 6.40×10⁻¹⁶ / 6.64×10⁻²⁷) = √(1.28×10⁻¹⁵/6.64×10⁻²⁷) = √(1.93×10¹¹) = **4.39 × 10⁵ m/s**

---

### Answer 5 (IB-Style)
**(a)** At x = 0: r₁ = 0.20 m, r₂ = 0.20 m.
V = k[4.0×10⁻⁹/0.20 + (−2.0×10⁻⁹)/0.20] = (8.99×10⁹/0.20)(2.0×10⁻⁹)
= 4.495×10¹⁰ × 2.0×10⁻⁹ = **89.9 V**

**(b)** At x = 0.50 m: r₁ = 0.70 m (to q₁ at −0.20), r₂ = 0.30 m (to q₂ at +0.20).
V = 8.99×10⁹[4.0×10⁻⁹/0.70 + (−2.0×10⁻⁹)/0.30]
= 8.99×10⁹[5.71×10⁻⁹ − 6.67×10⁻⁹]
= 8.99×10⁹ × (−9.52×10⁻¹⁰) = **−8.56 V**

**(c)** The test charge (+1.0 nC) at x = 0.50 m is in a region of slightly negative potential. Positive charges are repelled from + charges and attracted to − charges. Since q₂ = −2.0 nC at x = +0.20 m, the test charge will be attracted leftward toward q₂. As it moves left, it gains KE as potential decreases (becomes more negative near q₂). It will accelerate toward and past q₂ (assuming it can pass through), then decelerate as it approaches q₁ = +4.0 nC. The motion is oscillatory if it's trapped between the charges.

**(d)** For V = 0 to the right of q₂ (at x = d > 0.20):
k×4.0×10⁻⁹/(d + 0.20) + k×(−2.0×10⁻⁹)/(d − 0.20) = 0
4.0/(d + 0.20) = 2.0/(d − 0.20)
4.0(d − 0.20) = 2.0(d + 0.20)
4.0d − 0.80 = 2.0d + 0.40
2.0d = 1.20
**d = 0.60 m** (from origin), or 0.40 m to the right of q₂.

---

## Key Takeaways

| Concept | Equation | Notes |
|---------|----------|-------|
| Electric potential (point charge) | V = kQ/r | Scalar, sign matters |
| Multiple charges | V = Σ(kqᵢ/rᵢ) | Simple algebraic addition |
| Work done | W = qΔV | W > 0: against field; W < 0: by field |
| Electronvolt | 1 eV = 1.60 × 10⁻¹⁹ J | Energy unit for atomic scales |
| E from V (uniform) | E = V/d | For parallel plates |
| E from V (general) | E = −ΔV/Δr | E points toward decreasing V |
| Electron through p.d. | v = √(2eV/m) | Very common IB problem |

> **IB Data Booklet:** V = kQ/r, W = qV, and E = V/d are given in Sub-topic 5.1. The electronvolt conversion 1 eV = 1.60 × 10⁻¹⁹ J is explicitly provided. Remember: potential is a scalar (simple addition), field is a vector (directional addition). This is a key difference frequently tested.
