# Lesson 50: Electric & Magnetic Fields III — Magnetic Fields & Forces

## What You'll Learn
- Magnetic field patterns (bar magnet, straight wire, solenoid)
- Magnetic force on a moving charge: F = qvB sin θ
- Magnetic force on a current-carrying wire: F = BIL sin θ
- Fleming's Left-Hand Rule for direction
- Definition of the tesla

---

## 1. Magnetic Fields — Sources and Patterns

### What Creates a Magnetic Field?

- **Permanent magnets** (aligned electron spins in iron, nickel, cobalt)
- **Moving charges** (electric currents)
- **Changing electric fields** (beyond IB scope)

### Magnetic Field Lines

| Rule | Description |
|------|-------------|
| Direction | North → South (outside the magnet) |
| Closed loops | Field lines form complete loops |
| Density | More lines = stronger field |
| Never cross | Field is single-valued |

### Key Magnetic Field Patterns

**Bar Magnet:**
```
    → → → → → → → →
  N ●—————→——————→● S
    → → → → → → → →
```
Lines emerge from N, curve around, enter at S.

**Straight Current-Carrying Wire:**
Concentric circles around the wire. Right-Hand Grip Rule: thumb points in current direction, fingers curl in B-field direction.

```
Current ↑     B-field (from above):
   │          ↺ ↺ ↺
   │          →·←
   │          ↻ ↻ ↻
```

**Solenoid (Coil):**
Inside: uniform field parallel to axis (like a bar magnet).
Right-Hand Grip Rule: fingers curl in current direction, thumb points to N pole.

```
   ═══════════════
   → → → → → → → →     Inside: uniform B
   ═══════════════
   S              N
```

---

## 2. Magnetic Force on a Moving Charge

### The Lorentz Force

A charge q moving with velocity v in a magnetic field B experiences a force:

$$F = qvB\sin\theta$$

where:
- **F** = magnetic force (N)
- **q** = charge (C) — sign matters!
- **v** = speed (m/s)
- **B** = magnetic field strength (T, tesla)
- **θ** = angle between v and B

### Important Properties

| Property | Description |
|----------|-------------|
| Direction | **Perpendicular** to BOTH v and B |
| Work | Magnetic force does **NO WORK** (F ⊥ v always) |
| Speed | Magnetic force changes direction, NEVER speed |
| θ = 0° or 180° | No force if moving parallel to field |
| θ = 90° | Maximum force F = qvB |

### Fleming's Left-Hand Rule

```
     F (Force)
     ↑
     |
  B ←—·—→ I (Current / v for + charge)
     |
```

- **ThuMb** = Motion/Force (F)
- **First finger** = Field (B, N→S)
- **SeCond finger** = Current (I, or v for positive charge)

For negative charges, reverse the current/velocity direction!

---

## 3. Magnetic Force on a Current-Carrying Wire

A current I in a wire of length L in a magnetic field B:

$$F = BIL\sin\theta$$

where:
- **F** = force on wire (N)
- **I** = current (A)
- **L** = length of wire in the field (m)
- **θ** = angle between wire (current direction) and B-field

### Derivation

In time t, charge q = It passes through the wire. The force on this charge:
F = qvB sin θ = (It)(L/t)(B sin θ) = BIL sin θ

*(since v = L/t for charge moving through wire length L)*

### Direction

Same Fleming's Left-Hand Rule: middle finger points in **conventional current** direction (+ to −).

---

## 4. Definition of the Tesla

The tesla (T) is defined from F = BIL:

$$1 \text{ T} = 1 \frac{\text{N}}{\text{A} \cdot \text{m}}$$

A magnetic field of 1 tesla exerts a force of 1 newton on a 1-metre wire carrying 1 ampere perpendicular to the field.

### Typical B-Field Values

| Source | B-field |
|--------|---------|
| Earth's magnetic field | ~5 × 10⁻⁵ T |
| Refrigerator magnet | ~0.01 T |
| MRI machine | 1.5 − 3 T |
| Strongest lab magnets | ~45 T |
| Neutron star surface | ~10⁸ T |

---

## 5. Right-Hand Slap Rule (Alternative to Fleming's)

An alternative to Fleming's Left-Hand Rule:

- **Fingers** point in B-field direction (N→S)
- **Thumb** points in current direction (or v for + charge)
- **Palm faces** direction of force ("slap")

Good for checking: if you "slap" the wire, the force pushes in the direction of your palm.

---

## Worked Examples

### Worked Example 50.1 — Force on an Electron in a B-Field

**Problem:** An electron moves at 5.0 × 10⁶ m/s perpendicular to a magnetic field of 0.20 T. Find:
(a) the magnitude of the magnetic force
(b) the acceleration of the electron
(e = 1.60 × 10⁻¹⁹ C, mₑ = 9.11 × 10⁻³¹ kg)

**Solution:**

**(a)**
$$F = qvB\sin\theta = 1.60 \times 10^{-19} \times 5.0 \times 10^6 \times 0.20 \times \sin 90°$$
$$F = 1.60 \times 10^{-19} \times 5.0 \times 10^6 \times 0.20 = \mathbf{1.60 \times 10^{-13} \text{ N}}$$

**(b)**
$$a = \frac{F}{m} = \frac{1.60 \times 10^{-13}}{9.11 \times 10^{-31}} = \mathbf{1.76 \times 10^{17} \text{ m/s}^2}$$

Direction: perpendicular to both v and B (use Fleming's Left-Hand Rule, reversing for negative charge).

---

### Worked Example 50.2 — Force on a Current-Carrying Wire

**Problem:** A straight wire of length 0.50 m carries a current of 3.0 A and is placed in a uniform magnetic field of 0.40 T. The wire makes an angle of 30° with the field. Find the force on the wire.

**Solution:**

$$F = BIL\sin\theta = 0.40 \times 3.0 \times 0.50 \times \sin 30°$$
$$F = 0.40 \times 3.0 \times 0.50 \times 0.50 = \mathbf{0.30 \text{ N}}$$

---

### Worked Example 50.3 — Direction Practice

**Problem:** A wire carries current eastward. The magnetic field points northward. Find the direction of the force on the wire.

**Solution:**

Using Fleming's Left-Hand Rule:
- First finger (Field): North
- Second finger (Current): East
- ThuMb (Force): **Upward** (vertically out of the page)

Verify with Right-Hand Slap: fingers North, thumb East → palm faces upward ✓

---

### Worked Example 50.4 — Solenoid Field

**Problem:** A solenoid has 500 turns over a length of 0.25 m and carries 2.0 A. Calculate the magnetic field inside the solenoid. (μ₀ = 4π × 10⁻⁷ T·m/A)

**Solution:**

For an ideal solenoid:
$$B = \mu_0 n I$$

where n = turns per unit length = N/L = 500/0.25 = 2000 turns/m.

$$B = 4\pi \times 10^{-7} \times 2000 \times 2.0 = 4\pi \times 10^{-7} \times 4000$$
$$B = 1.60\pi \times 10^{-3} = \mathbf{5.03 \times 10^{-3} \text{ T}}$$

---

## Practice Problems

### Problem 1
A proton (q = +1.60 × 10⁻¹⁹ C) moves at 3.0 × 10⁶ m/s northward in a magnetic field of 0.50 T directed eastward.
(a) Find the magnitude of the magnetic force.
(b) State the direction of the force.
(c) Explain why the proton's speed doesn't change.

### Problem 2
A 0.80 m wire carries 5.0 A perpendicular to a uniform magnetic field and experiences a force of 0.60 N.
(a) Calculate the magnetic field strength.
(b) If the wire is rotated so it makes 60° with the field, what is the new force?

### Problem 3
An electron enters a region where the magnetic field is directed into the page and the electron's velocity is to the right.
(a) Sketch the electron's path (qualitatively).
(b) Use Fleming's Left-Hand Rule to verify the initial direction of deflection.
(c) Why does the electron follow a circular path?

### Problem 4
A power line carries 200 A horizontally east-west. Earth's magnetic field at this location is 5.0 × 10⁻⁵ T directed northward, dipping at 60° below the horizontal.
(a) Which component of Earth's field affects the wire? (The wire is horizontal.)
(b) Calculate the force per metre on the wire.
(c) Determine the direction of the force.

### Problem 5 (IB-Style — Direction + Magnitude)
Two long parallel wires are separated by 0.10 m. Wire 1 carries 4.0 A northward, wire 2 carries 3.0 A southward.

**(a)** State the direction of the magnetic field created by wire 1 at the location of wire 2.
**(b)** Calculate the magnitude of this magnetic field. (μ₀ = 4π × 10⁻⁷ T·m/A)
**(c)** Determine the magnitude and direction of the force on wire 2 (length 2.0 m) due to wire 1's magnetic field.
**(d)** State whether the wires attract or repel each other. Explain using field line concepts.

---

## Answers

### Answer 1
**(a)** v ⊥ B (north ⊥ east): F = qvB = 1.60×10⁻¹⁹ × 3.0×10⁶ × 0.50 = **2.40 × 10⁻¹³ N**

**(b)** Fleming's LHR: First finger East (B), Second finger North (v for + charge). Thumb points **upward** (out of the page/skyward).

**(c)** Magnetic force is always perpendicular to velocity. F ⊥ v → no work done → KE unchanged → speed constant. Only direction changes.

---

### Answer 2
**(a)** F = BIL → B = F/(IL) = 0.60/(5.0 × 0.80) = **0.15 T**

**(b)** F = BIL sin θ = 0.15 × 5.0 × 0.80 × sin 60° = 0.60 × 0.866 = **0.52 N**

---

### Answer 3
**(a)** Electron enters from left, moving right. B into page. Force initially downward (negative charge reverses direction). Path curves downward in a circular arc.

**(b)** For − charge: reverse the current direction in Fleming's LHR. The electron moving right = current to the LEFT. First finger into page (B), Second finger LEFT, Thumb points DOWNWARD ✓

**(c)** F is always ⊥ v, providing centripetal force. The electron undergoes uniform circular motion in the plane perpendicular to B (in this case, the plane of the page). Radius r = mv/(qB).

---

### Answer 4
**(a)** Only the vertical component of B affects a horizontal wire (component ⊥ to wire and ⊥ to current direction). B_vertical = B × sin 60° = 5.0×10⁻⁵ × 0.866 = 4.33×10⁻⁵ T.

**(b)** F/L = IB⊥ = 200 × 4.33×10⁻⁵ = **8.66 × 10⁻³ N/m**

**(c)** Current eastward. B vertical component downward. Fleming's LHR: First finger downward, Second finger east → Thumb SOUTH. Force is southward.

---

### Answer 5 (IB-Style)
**(a)** Wire 1 (current north). Using Right-Hand Grip Rule: thumb north, fingers curl. At the position of wire 2 (to the east of wire 1), the field points **downward** (into the page if the wires are in the horizontal plane).

**(b)** B = μ₀I/(2πr) = (4π×10⁻⁷ × 4.0)/(2π × 0.10) = (1.6π×10⁻⁶)/(0.20π) = **8.0 × 10⁻⁶ T**

**(c)** Wire 2 carries 3.0 A southward (opposite direction to wire 1). Using F = BIL sin θ with B from wire 1 at wire 2:
F = 8.0×10⁻⁶ × 3.0 × 2.0 × sin 90° = **4.8 × 10⁻⁵ N**

Direction: B downward, I southward. Fleming's LHR: First finger down, Second finger south → Thumb WEST. So wire 2 is pushed **away** from wire 1 (westward).

**(d)** The wires carry currents in **opposite** directions → they **repel**. 

Field line explanation: Between the wires, the B-fields from the two currents point in the same direction (both up or both down, depending on position), creating a stronger field between them. The wires are pushed toward regions of weaker field → pushed apart. (For parallel currents, fields cancel between wires → wires are pushed together → attract.)

Mnemonic: "Parallel currents attract, anti-parallel currents repel."

---

## Key Takeaways

| Concept | Equation | Notes |
|---------|----------|-------|
| Force on moving charge | F = qvB sin θ | Direction: Fleming's LHR |
| Force on current wire | F = BIL sin θ | I = conventional current (+ to −) |
| No work | F ⊥ v | Speed unchanged, only direction |
| Tesla definition | 1 T = 1 N/(A·m) | Unit of B-field |
| Solenoid field | B = μ₀nI | Uniform inside, similar to bar magnet |
| Parallel wires | F/L = μ₀I₁I₂/(2πr) | Attract if currents parallel |

> **IB Data Booklet:** F = qvB sin θ and F = BIL sin θ are in Sub-topic 5.4. μ₀ = 4π × 10⁻⁷ T·m/A is provided. Magnetic force direction uses Fleming's Left-Hand Rule (motor rule) — you must know this for Paper 1 and 2. Remember: magnetic force does zero work!
