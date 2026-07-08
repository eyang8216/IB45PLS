# Lesson 26: Circuits III — Kirchhoff's Laws & Potential Dividers

> **IB Data Booklet references:** $\sum I_{\text{in}} = \sum I_{\text{out}}$ (Junction Rule), $\sum V = 0$ (Loop Rule), $V_{\text{out}} = V_{\text{in}} \frac{R_2}{R_1 + R_2}$ (potential divider)

## What You'll Learn
- **Kirchhoff's Junction Rule**: $\sum I_{\text{in}} = \sum I_{\text{out}}$ (charge conservation)
- **Kirchhoff's Loop Rule**: $\sum V = 0$ around any closed loop (energy conservation)
- How to solve **multi-loop circuits** using Kirchhoff's Laws
- The **potential divider** formula: $V_{\text{out}} = V_{\text{in}} \times \frac{R_2}{R_1 + R_2}$
- Applications of potential dividers with **sensors** (LDR, thermistor)

---

## 1. Kirchhoff's Junction Rule (First Law)

**Statement:** At any junction in a circuit, the sum of currents entering equals the sum of currents leaving.

$$\boxed{\sum I_{\text{in}} = \sum I_{\text{out}}}$$

### Why it works
This is a direct consequence of **conservation of charge**. Charge cannot accumulate at a junction — whatever flows in must flow out.

### Sign convention
- Currents **entering** the junction: positive
- Currents **leaving** the junction: negative
- Algebraic sum: $\sum I = 0$

### Example
At a junction with three wires:
$$I_1 = I_2 + I_3$$

If $I_1 = 5.0\ \mathrm{A}$ and $I_2 = 3.0\ \mathrm{A}$, then $I_3 = 2.0\ \mathrm{A}$.

---

## 2. Kirchhoff's Loop Rule (Second Law)

**Statement:** Around any closed loop in a circuit, the algebraic sum of potential differences is zero.

$$\boxed{\sum V = 0}$$

### Why it works
This is a consequence of **conservation of energy**. The electrical potential energy gained by a charge going through the battery must exactly equal the energy lost going through the resistors in a complete loop.

### Sign Convention for Loop Rule

Going around a loop in your chosen direction:

| Component | Direction | Sign of $V$ |
|-----------|-----------|-------------|
| Battery | From − to + | $+\varepsilon$ (gain) |
| Battery | From + to − | $-\varepsilon$ (loss) |
| Resistor | Same direction as current | $-IR$ (voltage drop) |
| Resistor | Opposite direction to current | $+IR$ (voltage rise) |

### Practical strategy for applying loop rule
1. **Assign currents** to each branch (label $I_1$, $I_2$, $I_3$, etc.) with assumed directions
2. **Write junction equations** for each node
3. **Write loop equations** for each independent loop (number of loops = branches − junctions + 1)
4. **Solve the system** of equations simultaneously
5. If any current comes out negative, it means the actual direction is opposite to your assumption

---

## 3. Solving Multi-Loop Circuits Step by Step

### Systematic Method

1. **Label all junctions** (nodes) — usually with letters A, B, C, etc.
2. **Assign a current** and direction to each branch. Use $I_1$, $I_2$, $I_3$, etc. (Direction is arbitrary; a negative result means opposite direction.)
3. **Apply Junction Rule** at $(n-1)$ junctions, where $n$ is the total number of junctions
4. **Apply Loop Rule** to independent loops (choose loops that don't just repeat information)
5. **Solve the simultaneous equations**
6. **Check** with unused loops or by verifying power balance: $P_{\text{supplied}} = P_{\text{dissipated}}$

---

## 4. The Potential Divider

A **potential divider** (voltage divider) is two resistors in series across a voltage source. The output voltage is taken across one of the resistors:

$$\boxed{V_{\text{out}} = V_{\text{in}} \times \frac{R_2}{R_1 + R_2}}$$

where $V_{\text{out}}$ is the voltage across $R_2$.

### How it works
The same current $I = \frac{V_{\text{in}}}{R_1 + R_2}$ flows through both resistors.

$V_{\text{out}} = I R_2 = \frac{V_{\text{in}}}{R_1 + R_2} \times R_2 = V_{\text{in}} \frac{R_2}{R_1 + R_2}$

### Key Insight
- If $R_2 = 0$: $V_{\text{out}} = 0$ (short circuit)
- If $R_2 \to \infty$: $V_{\text{out}} = V_{\text{in}}$ (open circuit)
- If $R_1 = R_2$: $V_{\text{out}} = V_{\text{in}}/2$
- The output voltage can be continuously varied between 0 and $V_{\text{in}}$

### The Potentiometer
A **potentiometer** is a variable potential divider — a single resistive track with a sliding contact (wiper). Moving the wiper changes the ratio $R_1 : R_2$, giving a continuously variable $V_{\text{out}}$.

---

## 5. Sensor Applications

Potential dividers are widely used with sensors whose resistance changes with the environment.

### Light-Dependent Resistor (LDR)
- Resistance **decreases** as light intensity **increases**
- In bright light: $R_{\text{LDR}}$ is low (typically few hundred $\Omega$)
- In darkness: $R_{\text{LDR}}$ is high (typically M$\Omega$)

### Thermistor (NTC — Negative Temperature Coefficient)
- Resistance **decreases** as temperature **increases**
- At low temperatures: $R$ is high
- At high temperatures: $R$ is low

### Sensor Circuit Design
Place the sensor in the appropriate position:

- **To get $V_{\text{out}} \uparrow$ when sensor $R \downarrow$**: Put the sensor as $R_1$ (top), fixed resistor as $R_2$ (bottom)
  - $V_{\text{out}} = V_{\text{in}} \frac{R_{\text{fixed}}}{R_{\text{sensor}} + R_{\text{fixed}}}$
  - When sensor $R \downarrow$, denominator $\downarrow$, $V_{\text{out}} \uparrow$

- **To get $V_{\text{out}} \downarrow$ when sensor $R \downarrow$**: Put the sensor as $R_2$ (bottom), fixed resistor as $R_1$ (top)
  - $V_{\text{out}} = V_{\text{in}} \frac{R_{\text{sensor}}}{R_{\text{fixed}} + R_{\text{sensor}}}$
  - When sensor $R \downarrow$, numerator $\downarrow$, $V_{\text{out}} \downarrow$

> ⚠️ **Exam tip:** Be explicit about which resistor is in which position and explain how $V_{\text{out}}$ changes.

---

## 6. The Wheatstone Bridge (Balanced Condition)

A Wheatstone bridge consists of four resistors in a diamond configuration. A galvanometer (sensitive ammeter) connects the two midpoints.

### Balanced Condition
The bridge is **balanced** when no current flows through the galvanometer:

$$\boxed{\frac{R_1}{R_2} = \frac{R_3}{R_4}}$$

At balance, the potentials at the two midpoints are equal. This is used for precise resistance measurement.

---

## Worked Examples

### Worked Example 26.1 — Junction Rule
**Problem:** At a junction, $I_1 = 4.0\ \mathrm{A}$ enters, $I_2 = 1.5\ \mathrm{A}$ leaves, and $I_3 = 1.0\ \mathrm{A}$ leaves. What is the magnitude and direction of $I_4$?

**Solution:**
Junction rule: $I_1 - I_2 - I_3 - I_4 = 0$ (entering positive)
$4.0 - 1.5 - 1.0 - I_4 = 0$
$I_4 = 1.5\ \mathrm{A}$ **leaving** the junction. ✓

---

### Worked Example 26.2 — Two-Loop Kirchhoff Problem
**Problem:** Circuit: $12\ \mathrm{V}$ battery, then node A. Branch 1: $R_1 = 4\ \Omega$ to node B. Branch 2: $R_2 = 6\ \Omega$ to node B. From B back to battery through $R_3 = 2\ \Omega$.

Find all three branch currents.

**Solution:**
Let $I_1$ through $R_1$, $I_2$ through $R_2$, $I_3$ through $R_3$.

At junction A: $I_3 = I_1 + I_2$ (total from battery splits)

Loop 1 (battery → $R_1$ → $R_3$ → battery): $12 - 4I_1 - 2I_3 = 0$
Loop 2 (battery → $R_2$ → $R_3$ → battery): $12 - 6I_2 - 2I_3 = 0$

Substitute $I_3 = I_1 + I_2$:
Loop 1: $12 - 4I_1 - 2(I_1 + I_2) = 0 \Rightarrow 12 - 6I_1 - 2I_2 = 0$ … (1)
Loop 2: $12 - 6I_2 - 2(I_1 + I_2) = 0 \Rightarrow 12 - 2I_1 - 8I_2 = 0$ … (2)

From (1): $6I_1 + 2I_2 = 12 \Rightarrow 3I_1 + I_2 = 6$
From (2): $2I_1 + 8I_2 = 12 \Rightarrow I_1 + 4I_2 = 6$

Solve: From first: $I_2 = 6 - 3I_1$. Substitute: $I_1 + 4(6 - 3I_1) = 6$
$I_1 + 24 - 12I_1 = 6 \Rightarrow -11I_1 = -18 \Rightarrow I_1 = 1.636\ \mathrm{A}$

$I_2 = 6 - 3(1.636) = 1.092\ \mathrm{A}$
$I_3 = I_1 + I_2 = 2.728\ \mathrm{A}$

Check: Loop 1: $12 - 4(1.636) - 2(2.728) = 12 - 6.544 - 5.456 = 0$ ✓

---

### Worked Example 26.3 — Potential Divider (Fixed Resistors)
**Problem:** A $9.0\ \mathrm{V}$ battery is connected across a potential divider with $R_1 = 200\ \Omega$ and $R_2 = 300\ \Omega$. Calculate $V_{\text{out}}$ across $R_2$.

**Solution:**
$V_{\text{out}} = 9.0 \times \frac{300}{200 + 300} = 9.0 \times \frac{300}{500} = 9.0 \times 0.600 = 5.4\ \mathrm{V}$ ✓

---

### Worked Example 26.4 — Potential Divider with LDR
**Problem:** An LDR is placed as $R_1$ in a potential divider with a fixed $R_2 = 10\ \mathrm{k\Omega}$ and $V_{\text{in}} = 6.0\ \mathrm{V}$. In bright light, $R_{\text{LDR}} = 1.0\ \mathrm{k\Omega}$. In darkness, $R_{\text{LDR}} = 100\ \mathrm{k\Omega}$.
(a) Calculate $V_{\text{out}}$ in bright light and in darkness. **[4 marks]**
(b) This $V_{\text{out}}$ is connected to a circuit that switches on a lamp when $V_{\text{out}} > 4.0\ \mathrm{V}$. Does the lamp turn on in bright light or darkness? Explain. **[2 marks]**

**Solution:**
**(a)** $V_{\text{out}}$ is across $R_2$ (the fixed resistor):
$V_{\text{out}} = V_{\text{in}} \times \frac{R_2}{R_1 + R_2} = 6.0 \times \frac{10}{R_1 + 10}$

Bright light ($R_1 = 1.0$): $V_{\text{out}} = 6.0 \times \frac{10}{1.0 + 10} = 6.0 \times \frac{10}{11} = 5.45\ \mathrm{V}$
Darkness ($R_1 = 100$): $V_{\text{out}} = 6.0 \times \frac{10}{100 + 10} = 6.0 \times \frac{10}{110} = 0.545\ \mathrm{V}$ ✓✓

**(b)** $V_{\text{out}}$ exceeds $4.0\ \mathrm{V}$ in **bright light** ($5.45\ \mathrm{V} > 4.0\ \mathrm{V}$), not in darkness ($0.545\ \mathrm{V}$). So the lamp turns on in **bright light**. This is counterintuitive (you might want a lamp to come on when it's dark). To reverse, swap the LDR and fixed resistor positions. ✓✓

---

### Worked Example 26.5 — Wheatstone Bridge
**Problem:** In a Wheatstone bridge, $R_1 = 100\ \Omega$, $R_2 = 200\ \Omega$, and $R_3 = 150\ \Omega$. The bridge is balanced.
(a) Calculate $R_4$. **[2 marks]**
(b) Explain what "balanced" means and how you would detect it experimentally. **[2 marks]**

**Solution:**
**(a)** Balanced: $\frac{R_1}{R_2} = \frac{R_3}{R_4}$
$\frac{100}{200} = \frac{150}{R_4} \Rightarrow R_4 = 150 \times \frac{200}{100} = 300\ \Omega$ ✓✓

**(b)** "Balanced" means the potentials at the two midpoints are equal, so **no current flows** through the galvanometer connecting them. Experimentally, you vary one of the known resistors until the galvanometer reads zero. ✓✓

---

## Practice Problems

### Problem 1 — Junction Rule
Currents of $2.0\ \mathrm{A}$ and $3.0\ \mathrm{A}$ enter a junction, and a current of $1.0\ \mathrm{A}$ leaves. What is the magnitude and direction of the fourth current? **[2 marks]**

### Problem 2 — Simple Potential Divider
A $12\ \mathrm{V}$ supply is connected across $R_1 = 40\ \Omega$ and $R_2 = 60\ \Omega$ in series. Calculate $V_{\text{out}}$ across $R_2$. **[1 mark]**

### Problem 3 — Kirchhoff Two-Loop Circuit
In a circuit: a $9.0\ \mathrm{V}$ battery connects to a junction. One branch has $R_1 = 3.0\ \Omega$; the other has $R_2 = 6.0\ \Omega$. Both rejoin, then pass through $R_3 = 2.0\ \Omega$ back to the battery. Calculate all three branch currents using Kirchhoff's Laws. **[6 marks]**

### Problem 4 — Sensor Circuit Design
You need a circuit where $V_{\text{out}}$ **increases** when the temperature **decreases**. You have an NTC thermistor and a fixed resistor.
(a) Draw the circuit showing whether the thermistor is $R_1$ or $R_2$. **[2 marks]**
(b) Explain your choice. **[2 marks]**
(c) If $V_{\text{in}} = 5.0\ \mathrm{V}$, $R_{\text{fixed}} = 10\ \mathrm{k\Omega}$, and the thermistor has $R = 5.0\ \mathrm{k\Omega}$ at $30\mathrm{°C}$ and $R = 20\ \mathrm{k\Omega}$ at $10\mathrm{°C}$, calculate $V_{\text{out}}$ at each temperature. **[3 marks]**

### Problem 5 — IB-Style: Kirchhoff + Potential Divider Combined
Consider this circuit: A $6.0\ \mathrm{V}$ battery with negligible internal resistance. From positive terminal, the circuit splits into two parallel branches:
- **Branch A:** $R_1 = 12\ \Omega$ in series with a parallel pair ($R_2 = 6.0\ \Omega$, $R_3 = 3.0\ \Omega$)
- **Branch B:** $R_4 = 4.0\ \Omega$

Both branches rejoin and return to the battery.

(a) Using circuit reduction, calculate the total equivalent resistance. **[3 marks]**
(b) Calculate the current supplied by the battery. **[1 mark]**
(c) Calculate the current through $R_4$. **[2 marks]**
(d) Using potential divider principles, calculate the voltage across $R_2$. **[4 marks]**
(e) Verify your answer to (d) using Kirchhoff's Laws. **[3 marks]**

---

## Answers

### Answer 1
Entering positive: $+2.0 + 3.0 - 1.0 - I_4 = 0$
$I_4 = 4.0\ \mathrm{A}$ **leaving** the junction. ✓✓

### Answer 2
$V_{\text{out}} = 12 \times \frac{60}{40 + 60} = 12 \times 0.60 = 7.2\ \mathrm{V}$ ✓

### Answer 3
Let $I_1$ through $3\ \Omega$, $I_2$ through $6\ \Omega$, $I_3$ through $2\ \Omega$ (from battery).

Junction: $I_3 = I_1 + I_2$
Loop via $R_1$: $9 - 3I_1 - 2I_3 = 0$
Loop via $R_2$: $9 - 6I_2 - 2I_3 = 0$

Substitute: $9 - 3I_1 - 2(I_1 + I_2) = 0 \Rightarrow 9 - 5I_1 - 2I_2 = 0$ …(1)
$9 - 6I_2 - 2(I_1 + I_2) = 0 \Rightarrow 9 - 2I_1 - 8I_2 = 0$ …(2)

From (1): $5I_1 + 2I_2 = 9$
From (2): $2I_1 + 8I_2 = 9 \Rightarrow I_1 + 4I_2 = 4.5$

$I_1 = 4.5 - 4I_2$. Substitute into (1): $5(4.5 - 4I_2) + 2I_2 = 9$
$22.5 - 20I_2 + 2I_2 = 9 \Rightarrow -18I_2 = -13.5 \Rightarrow I_2 = 0.75\ \mathrm{A}$

$I_1 = 4.5 - 4(0.75) = 1.5\ \mathrm{A}$
$I_3 = 1.5 + 0.75 = 2.25\ \mathrm{A}$ ✓✓✓✓✓✓

### Answer 4
**(a)** Place the thermistor as $R_2$ (bottom) and the fixed resistor as $R_1$ (top). $V_{\text{out}}$ is taken across the thermistor. ✓✓

**(b)** $V_{\text{out}} = V_{\text{in}} \frac{R_{\text{thermistor}}}{R_{\text{fixed}} + R_{\text{thermistor}}}$. When temperature decreases, $R_{\text{thermistor}}$ increases (NTC), so the fraction increases → $V_{\text{out}}$ increases. ✓✓

**(c)** At $30\mathrm{°C}$: $V_{\text{out}} = 5.0 \times \frac{5.0}{10 + 5.0} = 5.0 \times \frac{5}{15} = 1.67\ \mathrm{V}$
At $10\mathrm{°C}$: $V_{\text{out}} = 5.0 \times \frac{20}{10 + 20} = 5.0 \times \frac{20}{30} = 3.33\ \mathrm{V}$ ✓✓✓

### Answer 5 — IB-Style Full Solution
**(a)** $R_{23} = \frac{6.0 \times 3.0}{6.0 + 3.0} = 2.0\ \Omega$
$R_A = R_1 + R_{23} = 12 + 2.0 = 14\ \Omega$
$R_B = R_4 = 4.0\ \Omega$
$R_{\text{total}} = \frac{R_A \times R_B}{R_A + R_B} = \frac{14 \times 4.0}{14 + 4.0} = \frac{56}{18} = 3.11\ \Omega$ ✓✓✓

**(b)** $I_{\text{total}} = 6.0/3.11 = 1.93\ \mathrm{A}$ ✓

**(c)** $R_4$ is directly across $6.0\ \mathrm{V}$: $I_4 = 6.0/4.0 = 1.5\ \mathrm{A}$ ✓✓

**(d)** Current in Branch A: $I_A = 1.93 - 1.5 = 0.43\ \mathrm{A}$
Voltage across $R_1$: $V_1 = 0.43 \times 12 = 5.16\ \mathrm{V}$
Voltage across parallel pair: $V_{23} = 6.0 - 5.16 = 0.84\ \mathrm{V}$

Both $R_2$ and $R_3$ have $0.84\ \mathrm{V}$ across them.
$I_2 = 0.84/6.0 = 0.14\ \mathrm{A}$, $I_3 = 0.84/3.0 = 0.28\ \mathrm{A}$
Check: $0.14 + 0.28 = 0.42 \approx 0.43$ ✓ ✓✓✓

**(e)** Using Kirchhoff for Branch A: $6.0 - 12I_A - 6I_2 = 0$ and $I_A = I_2 + I_3$ and $6I_2 = 3I_3$ (same voltage). $I_3 = 2I_2$, so $I_A = 3I_2$. Then $6.0 - 12(3I_2) - 6I_2 = 0 \Rightarrow 6.0 - 42I_2 = 0 \Rightarrow I_2 = 0.143\ \mathrm{A}$. Then $V_2 = 0.143 \times 6 = 0.86\ \mathrm{V}$. Matches! ✓✓✓

---

## Key Takeaways
1. **Kirchhoff's Junction Rule** ($\sum I_{\text{in}} = \sum I_{\text{out}}$): Charge is conserved at every junction.
2. **Kirchhoff's Loop Rule** ($\sum V = 0$): Energy is conserved around any closed loop. Going through a battery from − to + gives +$\varepsilon$; going through a resistor in the direction of current gives −$IR$.
3. For multi-loop circuits, write junction equations first, then loop equations. Solve the system.
4. **Potential divider**: $V_{\text{out}} = V_{\text{in}} \frac{R_2}{R_1 + R_2}$. The output voltage depends on the resistance ratio.
5. For **sensor circuits** (LDR, thermistor), place the sensor carefully — its position determines whether $V_{\text{out}}$ increases or decreases with the environmental change.

---

*Next: Lesson 27 — Circuits IV: EMF, Internal Resistance & Power*
