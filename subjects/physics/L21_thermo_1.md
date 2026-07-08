# Lesson 21: Thermodynamics I — The First Law and Thermodynamic Processes

## What You'll Learn
- State the First Law of Thermodynamics and apply it to gas processes
- Distinguish between isothermal, isochoric, isobaric, and adiabatic processes
- Calculate work done by a gas using $W = p\Delta V$
- Relate changes in internal energy, heat, and work for each process type
- Understand the sign convention: $Q$ in = positive, $W$ done BY gas = positive

---

## 1. What Is Thermodynamics?

### 1.1 Why This Matters

In mechanics, we track energy as kinetic and potential. In thermal physics, we track energy as it flows between objects at different temperatures (heat) and as it is transferred by forces acting through distances (work). Thermodynamics is the framework that unifies these ideas — it tells us how the internal energy of a system changes when heat flows in or out and when work is done on or by the system.

Every engine, refrigerator, power plant, and living cell obeys the laws of thermodynamics. The First Law (this lesson) is about energy conservation. The Second Law (Lesson 23) is about why some processes happen and others do not. Together, they govern everything from car engines to the fate of the universe.

### 1.2 Internal Energy — What Is It?

The **internal energy** $U$ of a system is the sum of all the kinetic and potential energies of its constituent particles. For an ideal gas, there are no intermolecular forces, so the potential energy component is zero. The internal energy is purely the total random kinetic energy of all the molecules.

For a monatomic ideal gas, we showed in Lesson 20:
$$U = \frac{3}{2}nRT$$

For a diatomic gas at moderate temperatures, rotational degrees of freedom add energy: $U = \frac{5}{2}nRT$. For IB purposes, monatomic gases ($\frac{3}{2}nRT$) are most commonly tested.

The crucial point: **internal energy of an ideal gas depends ONLY on temperature.** If the temperature does not change, the internal energy does not change — regardless of what else happens to the gas.

---

## 2. The First Law of Thermodynamics

### 2.1 The Equation

The First Law is a statement of energy conservation applied to thermal systems:

$$\Delta U = Q - W$$

where:
- $\Delta U$ is the change in internal energy (J)
- $Q$ is the heat added TO the system (J). $Q > 0$ means heat enters the system; $Q < 0$ means heat leaves.
- $W$ is the work done BY the system (J). $W > 0$ means the system does work on its surroundings (expands); $W < 0$ means work is done ON the system (compressed).

### 2.2 The Sign Convention — Get This Right

The IB uses the sign convention where $W$ is work done BY the gas. This means:
- When a gas **expands**, it pushes against its surroundings → $W > 0$ → internal energy decreases (if no heat enters)
- When a gas is **compressed**, work is done ON it → $W < 0$ → internal energy increases (if no heat leaves)

Some textbooks write $\Delta U = Q + W$ and define $W$ as work done ON the system. The IB uses $\Delta U = Q - W$ with $W$ as work done BY the system. Both are valid if used consistently. For the exam, use the IB convention.

**A helpful memory device:** If the gas expands ($W > 0$), it is spending its internal energy to push outward. Its "bank account" of energy goes down unless heat deposits more energy ($Q > 0$).

---

## 3. Work Done by a Gas

### 3.1 Constant Pressure

When a gas expands against a constant external pressure, the work done is:

$$W = p\Delta V$$

where $\Delta V = V_f - V_i$ is the change in volume. For expansion ($\Delta V > 0$), work is positive. For compression ($\Delta V < 0$), work is negative.

### 3.2 Variable Pressure — The $p$–$V$ Diagram

When pressure is not constant, the work done is the **area under the $p$–$V$ curve** between the initial and final volumes. This is the most general way to calculate work in thermodynamics. We explore $p$–$V$ diagrams in detail in Lesson 22.

### 3.3 Units Check

$W = p\Delta V$ in pascals × cubic metres = N m⁻² × m³ = N m = J. The joule emerges naturally.

If pressure is given in atm or kPa and volume in L or cm³, convert to Pa and m³ before calculating work in joules. Alternatively: $1\text{ L·atm} = 101.3\text{ J}$. This conversion is sometimes useful but not in the Data Booklet.

---

## 4. The Four Fundamental Processes

For any process involving an ideal gas, we can hold one quantity constant while letting others change. This gives four named processes:

### 4.1 Isothermal (Constant Temperature, $\Delta T = 0$)

Since $U$ depends only on $T$ for an ideal gas, $\Delta U = 0$. The First Law becomes:
$$0 = Q - W \quad \Rightarrow \quad Q = W$$

All heat added to the gas is converted entirely to work done by the gas. If you compress a gas isothermally ($W < 0$), you must remove an equal amount of heat ($Q < 0$) to keep the temperature from rising.

On a $p$–$V$ diagram, an isotherm is a hyperbola: $p \propto 1/V$ (from Boyle's Law).

**Real-world example:** A very slow compression or expansion where the gas has time to exchange heat with its surroundings and maintain thermal equilibrium. Think of a syringe pushed so slowly that it stays at room temperature.

### 4.2 Isochoric (Constant Volume, $\Delta V = 0$)

No volume change means no work is done: $W = p\Delta V = 0$. The First Law becomes:
$$\Delta U = Q$$

All heat added goes directly into increasing the internal energy (and therefore the temperature). On a $p$–$V$ diagram, an isochoric process is a vertical line.

**Real-world example:** Heating a gas in a rigid sealed container. The gas cannot expand, so all the energy from heating raises the temperature and pressure. This is Gay-Lussac's Law.

### 4.3 Isobaric (Constant Pressure, $\Delta p = 0$)

The work done is simple: $W = p\Delta V$. The First Law has all three terms non-zero:
$$\Delta U = Q - p\Delta V$$

On a $p$–$V$ diagram, an isobaric process is a horizontal line.

**Real-world example:** Heating a gas in a cylinder with a frictionless piston that is free to move. The piston maintains constant pressure (equal to atmospheric pressure plus the piston's weight). The gas expands as it heats — this is Charles' Law in action.

### 4.4 Adiabatic ($Q = 0$, No Heat Exchange)

No heat enters or leaves the system. The First Law becomes:
$$\Delta U = -W$$

If the gas expands adiabatically ($W > 0$), its internal energy decreases ($\Delta U < 0$) and it cools. If it is compressed adiabatically ($W < 0$), its internal energy increases and it heats up.

On a $p$–$V$ diagram, an adiabat is steeper than an isotherm — pressure drops faster because the temperature is also dropping.

**Real-world examples:** A bicycle pump gets hot when you compress air quickly (adiabatic compression). A spray can feels cold after use because the remaining gas expanded adiabatically. Sound waves are approximately adiabatic because the oscillations are too fast for significant heat exchange.

### 4.5 Summary Table

| Process | Constant | $\Delta U$ | $Q$ | $W$ | $p$–$V$ shape |
|---------|----------|------------|-----|-----|---------------|
| Isothermal | $T$ | $0$ | $Q = W$ | $W = Q$ | Hyperbola |
| Isochoric | $V$ | $Q$ | $\Delta U$ | $0$ | Vertical line |
| Isobaric | $p$ | $Q - p\Delta V$ | $\Delta U + p\Delta V$ | $p\Delta V$ | Horizontal line |
| Adiabatic | $Q = 0$ | $-W$ | $0$ | $-\Delta U$ | Steep curve |

---

## Worked Examples

### Worked Example 21.1 — Isobaric Expansion

**Problem:** $0.50\text{ mol}$ of an ideal monatomic gas expands at constant pressure of $2.0 \times 10^5\text{ Pa}$ from $2.0 \times 10^{-3}\text{ m}^3$ to $5.0 \times 10^{-3}\text{ m}^3$. The initial temperature is $96\text{ K}$. Calculate: (a) the work done by the gas, (b) the change in internal energy, and (c) the heat added.

**Approach:** Work is $p\Delta V$. Find initial and final temperatures to get $\Delta U$. Then use the First Law for $Q$.

**Solution (a):**
$$W = p\Delta V = (2.0 \times 10^5)(5.0 \times 10^{-3} - 2.0 \times 10^{-3}) = (2.0 \times 10^5)(3.0 \times 10^{-3}) = 600\text{ J}$$

**(b):** Find $T_f$ from Charles' Law: $T_f/T_i = V_f/V_i = 5.0/2.0 = 2.5$. So $T_f = 96 \times 2.5 = 240\text{ K}$. $\Delta T = 240 - 96 = 144\text{ K}$.

$$\Delta U = \frac{3}{2}nR\Delta T = \frac{3}{2}(0.50)(8.31)(144) = 897\text{ J}$$

**(c):** From First Law: $Q = \Delta U + W = 897 + 600 = 1,497\text{ J} \approx 1,500\text{ J}$.

**Why this makes sense:** More heat enters the gas (1,500 J) than the work it does (600 J). The extra 900 J raises the internal energy. This is typical — in an isobaric expansion, the gas must absorb extra heat to both do work AND raise its temperature.

---

### Worked Example 21.2 — Adiabatic Compression

**Problem:** A gas is compressed adiabatically. $150\text{ J}$ of work is done ON the gas. Calculate the change in internal energy and state whether the gas temperature increases or decreases.

**Approach:** Adiabatic means $Q = 0$. Work done ON the gas is negative: $W = -150\text{ J}$.

**Solution:**
$$\Delta U = Q - W = 0 - (-150) = +150\text{ J}$$

The internal energy increases by 150 J. Since $U \propto T$ for an ideal gas, the temperature increases. This is why a bicycle pump gets hot.

---

### Worked Example 21.3 — Isochoric Heating

**Problem:** $2.0\text{ mol}$ of an ideal monatomic gas is heated at constant volume. The temperature rises from $300\text{ K}$ to $450\text{ K}$. Calculate the heat added and the final pressure as a fraction of the initial pressure.

**Approach:** Isochoric means $W = 0$ so $Q = \Delta U$. Pressure ratio comes from Gay-Lussac's Law.

**Solution:**
$$\Delta U = \frac{3}{2}nR\Delta T = \frac{3}{2}(2.0)(8.31)(150) = 3,740\text{ J}$$
Since $W = 0$, $Q = \Delta U = 3,740\text{ J}$.

Pressure ratio: $p_f/p_i = T_f/T_i = 450/300 = 1.5$. The pressure increases by 50%.

---

### Worked Example 21.4 — Complete Cycle (IB-Style)

**Problem:** A heat engine uses $0.25\text{ mol}$ of an ideal monatomic gas. The gas undergoes the following cycle starting at $p_1 = 1.0 \times 10^5\text{ Pa}$, $V_1 = 5.0 \times 10^{-3}\text{ m}^3$, $T_1 = 240\text{ K}$:

A → B: Isobaric expansion to $V_2 = 1.0 \times 10^{-2}\text{ m}^3$.  
B → C: Isochoric cooling to the original temperature $T_1$.  
C → A: Isothermal compression to the original state.

Calculate for process A → B: (a) the work done, (b) the heat added, and (c) the change in internal energy.

**Solution:**
**(a)** $W_{AB} = p\Delta V = (1.0 \times 10^5)(1.0 \times 10^{-2} - 5.0 \times 10^{-3}) = 500\text{ J}$

$T_B = T_A \times (V_B/V_A) = 240 \times 2 = 480\text{ K}$ (Charles' Law).

**(c)** $\Delta U_{AB} = \frac{3}{2}nR(T_B - T_A) = \frac{3}{2}(0.25)(8.31)(480-240) = \frac{3}{2}(0.25)(8.31)(240) = 748\text{ J}$

**(b)** $Q_{AB} = \Delta U_{AB} + W_{AB} = 748 + 500 = 1,248\text{ J}$

---

## Practice Problems

### Problem 1
A gas expands at constant pressure of $3.0 \times 10^5\text{ Pa}$ from $4.0 \times 10^{-3}\text{ m}^3$ to $9.0 \times 10^{-3}\text{ m}^3$. Calculate the work done by the gas. If the internal energy increases by $2,000\text{ J}$ during this process, how much heat was added?

### Problem 2
$300\text{ J}$ of heat is added to a gas while it is compressed. $150\text{ J}$ of work is done ON the gas during the compression. Calculate the change in internal energy. Does the temperature of the gas increase or decrease?

### Problem 3
A gas is compressed isothermally. Explain why heat must be removed from the gas during this process. If $400\text{ J}$ of work is done ON the gas, how much heat is removed?

### Problem 4
A sealed rigid container of gas is heated. Explain, using the First Law, why all the heat added goes into increasing the internal energy. If $500\text{ J}$ of heat is added to $1.0\text{ mol}$ of monatomic gas initially at $300\text{ K}$, calculate the final temperature.

### Problem 5 — IB-Style Examination Question
$0.40\text{ mol}$ of an ideal monatomic gas undergoes two processes in sequence:

Process 1: The gas is heated at constant volume from $300\text{ K}$ to $600\text{ K}$.

Process 2: The gas then expands isothermally at $600\text{ K}$ back to its original pressure.

(a) For Process 1, calculate: (i) the work done by the gas, (ii) the heat added to the gas. (2 marks)

(b) For Process 2, state the change in internal energy and explain your answer. (2 marks)

(c) During Process 2, the gas does $700\text{ J}$ of work. Calculate the heat added to the gas during Process 2. (1 mark)

(d) Sketch the two processes on a $p$–$V$ diagram, labelling the initial, intermediate, and final states. (3 marks)

(e) The gas is now returned to its initial state by an adiabatic compression. State whether heat enters or leaves the gas during this compression and explain what happens to the temperature. (2 marks)

---

## Answers

### Answer 1
$W = p\Delta V = (3.0 \times 10^5)(9.0 \times 10^{-3} - 4.0 \times 10^{-3}) = 1,500\text{ J}$.
$Q = \Delta U + W = 2,000 + 1,500 = 3,500\text{ J}$.

### Answer 2
Work done ON gas: $W = -150\text{ J}$. Heat added: $Q = +300\text{ J}$.
$\Delta U = Q - W = 300 - (-150) = 450\text{ J}$. Internal energy increases → temperature increases.

### Answer 3
In isothermal compression, $\Delta U = 0$ (ideal gas, $\Delta T = 0$). From First Law: $0 = Q - W$, so $Q = W$. Work is done ON the gas ($W = -400\text{ J}$), so $Q = -400\text{ J}$ — $400\text{ J}$ of heat must be REMOVED. If heat were not removed, the work done would increase the internal energy and temperature — the process would not be isothermal. Physically, the gas must be in contact with a cold reservoir to maintain constant temperature.

### Answer 4
$W = 0$ (rigid container, $\Delta V = 0$). First Law: $\Delta U = Q = 500\text{ J}$.
$\Delta U = \frac{3}{2}nR\Delta T$, so $\Delta T = \frac{2\Delta U}{3nR} = \frac{2(500)}{3(1.0)(8.31)} = 40.1\text{ K}$. $T_f = 300 + 40.1 = 340\text{ K}$.

### Answer 5 — IB-Style
**(a)(i)** Isochoric → $W = 0$. (1 mark)  
**(a)(ii)** $Q = \Delta U = \frac{3}{2}nR\Delta T = \frac{3}{2}(0.40)(8.31)(300) = 1,496\text{ J} \approx 1,500\text{ J}$. (1 mark)

**(b)** Isothermal → $\Delta U = 0$ because $U$ for an ideal gas depends only on $T$, and $T$ is constant. (2 marks)

**(c)** $\Delta U = 0$, so $Q = W = 700\text{ J}$. (1 mark)

**(d)** (3 marks) Initial state at $(p_1, V_1)$. Process 1: vertical line upward (isochoric, $V$ constant, $p$ increases to $2p_1$ at 600 K). Process 2: curved line downward-right (isothermal hyperbola, $p$ returns to $p_1$, $V$ doubles to $2V_1$). States clearly labelled. (1 mark per correct process representation.)

**(e)** (2 marks) Adiabatic: $Q = 0$ — no heat enters or leaves. Compression: $W < 0$ (work done ON gas). First Law: $\Delta U = -W > 0$ → internal energy increases → temperature RISES. The gas heats up during adiabatic compression.

---

## Key Takeaways

1. **First Law:** $\Delta U = Q - W$. Energy is conserved — internal energy changes by heat in minus work out.

2. **Sign convention (IB):** $W > 0$ = work done BY gas. $Q > 0$ = heat added TO gas.

3. **Internal energy of ideal gas depends only on $T$:** $U = \frac{3}{2}nRT$ (monatomic).

4. **Four processes:** Isothermal ($\Delta U=0$, $Q=W$). Isochoric ($W=0$, $Q=\Delta U$). Isobaric ($W=p\Delta V$). Adiabatic ($Q=0$, $\Delta U=-W$).

5. **Work on $p$–$V$ diagram** = area under the curve. This is the general method for non-constant pressure.
