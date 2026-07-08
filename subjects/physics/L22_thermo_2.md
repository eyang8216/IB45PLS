# Lesson 22: Thermodynamics II — pV Diagrams, Cycles and Heat Engines

## What You'll Learn
- Interpret and sketch processes on $p$–$V$ diagrams
- Calculate net work from a cyclic process as the enclosed area
- Determine the efficiency of a heat engine
- Distinguish between heat engines, refrigerators, and heat pumps conceptually

---

## 1. The $p$–$V$ Diagram — Your Most Powerful Tool

### 1.1 Why This Matters

In mechanics, motion graphs ($s$–$t$, $v$–$t$) give you instant visual understanding of what is happening. In thermodynamics, the $p$–$V$ diagram serves the same purpose. With one glance at a $p$–$V$ diagram, you can identify which processes are occurring, calculate work done, and determine whether heat is being added or removed. Every IB thermodynamics problem beyond the simplest will involve a $p$–$V$ diagram.

### 1.2 Reading a $p$–$V$ Diagram

The axes are pressure ($p$) on the vertical and volume ($V$) on the horizontal. A point on the diagram represents the state of the gas at an instant — its pressure and volume uniquely determine its temperature (via $pV = nRT$) for a fixed amount of gas.

A curve connecting two points represents a process — how the gas changed from the initial state to the final state. The shape of the curve tells you what kind of process occurred:

- **Horizontal line** = isobaric (constant pressure). The gas expanded or contracted while pressure remained the same.

- **Vertical line** = isochoric (constant volume). The pressure changed while volume remained fixed — a rigid container being heated or cooled.

- **Hyperbola ($p \propto 1/V$)** = isothermal (constant temperature). The gas expands while maintaining the same temperature by absorbing heat.

- **Steep curve (steeper than an isotherm)** = adiabatic. No heat exchange — the temperature changes, so the $p$–$V$ relationship is $pV^\gamma = \text{constant}$ (where $\gamma > 1$).

### 1.3 Work as Area

The single most important fact about $p$–$V$ diagrams: **the work done by the gas during any process equals the area under the $p$–$V$ curve between the initial and final volumes.** This is true for any process, not just constant-pressure ones.

Why? Work = force × distance. For a piston of area $A$, force = $pA$. Distance moved = $\Delta V/A$. So work = $(pA)(\Delta V/A) = p\Delta V$ — the area of a rectangle of height $p$ and width $\Delta V$. For varying pressure, we sum (integrate) $p\,dV$, which is exactly the area under the curve.

For **expansion** (moving right on the diagram), the area is positive — the gas does work on its surroundings. For **compression** (moving left), the area is negative — work is done ON the gas.

---

## 2. Cyclic Processes

### 2.1 What Goes Around Comes Around

A cyclic process is one where the gas returns to its initial state — same pressure, volume, and temperature. On a $p$–$V$ diagram, a cycle is a closed loop. After one complete cycle, $\Delta U = 0$ (because $U$ depends only on state, and the final state equals the initial state).

From the First Law, for a complete cycle:
$$\Delta U = 0 = Q_{\text{net}} - W_{\text{net}} \quad \Rightarrow \quad Q_{\text{net}} = W_{\text{net}}$$

**The net work done in a cycle equals the net heat added.** And the net work is equal to the **area enclosed by the loop** on the $p$–$V$ diagram.

### 2.2 Clockwise vs. Counterclockwise

When a cycle runs **clockwise** on the $p$–$V$ diagram, the net work is positive — the gas does more work expanding than is done on it during compression. This is a **heat engine**: it takes in heat, converts some to work, and rejects the rest.

When a cycle runs **counterclockwise**, the net work is negative — more work is done ON the gas than the gas does. This is a **refrigerator or heat pump**: work is used to move heat from a cold place to a hot place.

### 2.3 The Net Work — Area Inside the Loop

To find the net work from a $p$–$V$ cycle:
1. Find the area under the expansion path(s) — positive work done BY gas
2. Find the area under the compression path(s) — negative work done ON gas  
3. Subtract: net work = area enclosed = (area under expansion) − (area under compression)

For simple shapes (rectangles, triangles), calculate the geometric area directly. For a rectangular cycle on a $p$–$V$ diagram: $W_{\text{net}} = \Delta p \times \Delta V$.

---

## 3. Heat Engines

### 3.1 How They Work

A heat engine operates between a hot reservoir at temperature $T_h$ and a cold reservoir at temperature $T_c$. In each cycle:
1. The engine absorbs heat $Q_h$ from the hot reservoir
2. It converts part of this heat to useful work $W_{\text{net}}$
3. It rejects the remaining heat $Q_c$ to the cold reservoir

By energy conservation: $Q_h = W_{\text{net}} + Q_c$.

### 3.2 Efficiency

The efficiency of a heat engine is the fraction of the input heat that is converted to useful work:

$$\eta = \frac{W_{\text{net}}}{Q_h} = \frac{Q_h - Q_c}{Q_h} = 1 - \frac{Q_c}{Q_h}$$

Efficiency is always less than 1 (less than 100%). Some heat MUST be rejected to the cold reservoir — this is a consequence of the Second Law (Lesson 23). You cannot convert heat entirely to work in a cyclic process.

### 3.3 The Carnot Engine

The Carnot engine is a theoretical engine with the maximum possible efficiency between two given temperatures. It operates on a cycle of two isothermal and two adiabatic processes. Its efficiency is:

$$\eta_{\text{Carnot}} = 1 - \frac{T_c}{T_h}$$

where temperatures are in KELVIN. No real engine can exceed this efficiency when operating between the same two temperatures.

The Carnot efficiency tells us something profound: to increase efficiency, you must increase $T_h$ (make the hot reservoir hotter) or decrease $T_c$ (make the cold reservoir colder). Since $T_c$ cannot go below ambient temperature (without additional energy input), practical engines focus on increasing $T_h$ — which is why internal combustion engines run hot.

---

## Worked Examples

### Worked Example 22.1 — Work from a $p$–$V$ Diagram

**Problem:** A gas expands at constant pressure of $4.0 \times 10^5\text{ Pa}$ from $2.0 \times 10^{-3}\text{ m}^3$ to $6.0 \times 10^{-3}\text{ m}^3$. It is then cooled at constant volume back to its original pressure. Calculate the net work done and sketch the process on a $p$–$V$ diagram.

**Approach:** Work for isobaric expansion = $p\Delta V$. Isochoric cooling: $W = 0$. Net work = $p\Delta V$ (the area under the horizontal line).

**Solution:**
$$W_{\text{net}} = p\Delta V = (4.0 \times 10^5)(6.0 \times 10^{-3} - 2.0 \times 10^{-3}) = 1,600\text{ J}$$

The $p$–$V$ diagram shows a horizontal line right (expansion), then a vertical line down (cooling). The area under the path (a rectangle) is $1,600\text{ J}$.

---

### Worked Example 22.2 — Rectangular Cycle Net Work

**Problem:** A gas undergoes a clockwise rectangular cycle: A(2,2) → B(5,2) → C(5,4) → D(2,4) → A(2,2), where coordinates are $(V\text{ in }10^{-3}\text{ m}^3,\ p\text{ in }10^5\text{ Pa})$. Calculate the net work per cycle.

**Approach:** For a rectangular clockwise cycle, net work = $\Delta p \times \Delta V$.

**Solution:**
$$\Delta V = (5 - 2) \times 10^{-3} = 3.0 \times 10^{-3}\text{ m}^3$$
$$\Delta p = (4 - 2) \times 10^5 = 2.0 \times 10^5\text{ Pa}$$
$$W_{\text{net}} = (3.0 \times 10^{-3})(2.0 \times 10^5) = 600\text{ J}$$

---

### Worked Example 22.3 — Engine Efficiency

**Problem:** A heat engine absorbs $800\text{ J}$ of heat from a hot reservoir each cycle and rejects $500\text{ J}$ to a cold reservoir. Calculate: (a) the net work per cycle, and (b) the efficiency.

**Solution (a):**
$$W_{\text{net}} = Q_h - Q_c = 800 - 500 = 300\text{ J}$$

**(b):**
$$\eta = \frac{W_{\text{net}}}{Q_h} = \frac{300}{800} = 0.375 = 37.5\%$$

---

### Worked Example 22.4 — Carnot Efficiency

**Problem:** A Carnot engine operates between a hot reservoir at $500\text{ K}$ and a cold reservoir at $300\text{ K}$. Calculate its maximum possible efficiency. If the engine absorbs $1,000\text{ J}$ of heat per cycle, what is the maximum work it can do?

**Solution:**
$$\eta_{\text{Carnot}} = 1 - \frac{300}{500} = 1 - 0.60 = 0.40 = 40\%$$
$$W_{\text{max}} = \eta Q_h = 0.40 \times 1,000 = 400\text{ J}$$

---

### Worked Example 22.5 — IB-Style Cycle Analysis

**Problem:** $1.0\text{ mol}$ of an ideal monatomic gas undergoes the cycle: A → B isothermal expansion at $600\text{ K}$ from $V_A = 1.0 \times 10^{-2}\text{ m}^3$ to $V_B = 3.0 \times 10^{-2}\text{ m}^3$. B → C isochoric cooling to $300\text{ K}$. C → A isothermal compression at $300\text{ K}$ back to $V_A$.

(a) Calculate the work done during A → B. (2 marks)
(b) Calculate the heat removed during B → C. (2 marks)
(c) Determine the net work done in one complete cycle. (3 marks)
(d) Calculate the efficiency of this engine and compare it to the Carnot efficiency for the same temperature limits. (3 marks)

**Solution:**
**(a)** Isothermal: $W_{AB} = nRT\ln(V_B/V_A) = (1.0)(8.31)(600)\ln(3) = 4,986 \times 1.099 = 5,477\text{ J}$.

**(b)** Isochoric: $W = 0$, so $Q_{BC} = \Delta U_{BC} = \frac{3}{2}nR(T_C - T_B) = \frac{3}{2}(1.0)(8.31)(300-600) = -3,740\text{ J}$. Heat removed = $3,740\text{ J}$.

**(c)** C → A isothermal at $300\text{ K}$: $W_{CA} = nRT\ln(V_A/V_C) = (1.0)(8.31)(300)\ln(1/3) = 2,493 \times (-1.099) = -2,738\text{ J}$. (Note: $V_C = V_B = 3.0 \times 10^{-2}\text{ m}^3$.)

$W_{\text{net}} = 5,477 + 0 + (-2,738) = 2,739\text{ J}$.

**(d)** Heat added during A → B: $Q_{AB} = W_{AB} = 5,477\text{ J}$ (isothermal, $\Delta U = 0$). Efficiency: $\eta = W_{\text{net}}/Q_h = 2,739/5,477 = 0.50 = 50\%$.

Carnot efficiency: $\eta_{\text{Carnot}} = 1 - 300/600 = 1 - 0.50 = 0.50 = 50\%$.

This engine achieves the Carnot efficiency because it uses reversible processes (isothermal + isochoric is not a Carnot cycle, but with the right combination it can approach Carnot — actually the efficiency matches Carnot here because of the specific cycle chosen).

---

## Practice Problems

### Problem 1
A gas expands from $3.0 \times 10^{-3}\text{ m}^3$ to $8.0 \times 10^{-3}\text{ m}^3$. During this expansion, the pressure decreases linearly from $5.0 \times 10^5\text{ Pa}$ to $2.0 \times 10^5\text{ Pa}$. Calculate the work done by the gas. (Hint: the area under a straight line on a $p$–$V$ diagram is the area of a trapezoid.)

### Problem 2
A heat engine absorbs $1,200\text{ J}$ of heat and rejects $900\text{ J}$ per cycle. Calculate the net work and the efficiency. If the engine operates at 25 cycles per second, what is its power output?

### Problem 3
A Carnot engine operates between $800\text{ K}$ and $300\text{ K}$ and produces $400\text{ J}$ of work per cycle. Calculate the heat absorbed from the hot reservoir per cycle.

### Problem 4
A diesel engine has an efficiency of 30% and produces 45 kW of useful power. At what rate is heat rejected to the environment?

### Problem 5 — IB-Style Examination Question
A fixed mass of ideal gas undergoes the cycle KLMN. Process KL is isobaric expansion. Process LM is adiabatic expansion. Process MN is isobaric compression. Process NK is isochoric heating.

(a) Sketch this cycle on a $p$–$V$ diagram. (3 marks)

(b) During KL, the gas does $400\text{ J}$ of work and its temperature increases. Explain whether more than $400\text{ J}$, less than $400\text{ J}$, or exactly $400\text{ J}$ of heat is absorbed during this process. (2 marks)

(c) During LM, the gas does $250\text{ J}$ of work. Explain why the temperature of the gas decreases during this process and calculate the change in internal energy. (2 marks)

(d) The net work done in one cycle is $200\text{ J}$. The heat absorbed from the hot reservoir in one cycle is $600\text{ J}$. Calculate the efficiency. (1 mark)

(e) The hot reservoir is at $900\text{ K}$ and the cold reservoir at $300\text{ K}$. Compare the engine's efficiency to the Carnot efficiency and suggest a reason for any difference. (2 marks)

---

## Answers

### Answer 1
For a straight line, work = area of trapezoid = average pressure × $\Delta V$:
$$W = \frac{(5.0 + 2.0) \times 10^5}{2} \times (8.0 - 3.0) \times 10^{-3} = (3.5 \times 10^5)(5.0 \times 10^{-3}) = 1,750\text{ J}$$

### Answer 2
$W_{\text{net}} = 1,200 - 900 = 300\text{ J}$. $\eta = 300/1,200 = 0.25 = 25\%$.
Power = $W_{\text{net}} \times \text{cycles per second} = 300 \times 25 = 7,500\text{ W} = 7.5\text{ kW}$.

### Answer 3
$\eta = 1 - 300/800 = 0.625$. $\eta = W/Q_h$, so $Q_h = W/\eta = 400/0.625 = 640\text{ J}$.

### Answer 4
Power output = 45 kW. $\eta = P_{\text{out}}/P_{\text{in}}$, so $P_{\text{in}} = 45/0.30 = 150\text{ kW}$. Heat rejection rate = $P_{\text{in}} - P_{\text{out}} = 150 - 45 = 105\text{ kW}$.

### Answer 5 — IB-Style
**(a)** (3 marks) KL: horizontal line to the right (isobaric expansion). LM: steep curve down-right (adiabatic, steeper than isotherm). MN: horizontal line to the left (isobaric compression). NK: vertical line up (isochoric heating, returns to K). Clockwise cycle. (1 mark per two correct processes.)

**(b)** In isobaric expansion, $\Delta U > 0$ (temperature increases) AND $W > 0$ (expansion). First Law: $Q = \Delta U + W$. Since $\Delta U > 0$, $Q > W$. So MORE than $400\text{ J}$ of heat is absorbed — specifically, $Q = \Delta U + 400 > 400\text{ J}$. (2 marks)

**(c)** Adiabatic: $Q = 0$. First Law: $\Delta U = -W = -250\text{ J}$. Internal energy decreases by 250 J. Since $U \propto T$ for an ideal gas, the temperature must decrease. The gas does work by using its own internal energy, with no heat to replenish it. (2 marks)

**(d)** $\eta = W_{\text{net}}/Q_h = 200/600 = 0.333 = 33.3\%$. (1 mark)

**(e)** $\eta_{\text{Carnot}} = 1 - 300/900 = 1 - 0.333 = 0.667 = 66.7\%$. The engine's efficiency (33%) is half the Carnot efficiency. This is expected for a real engine — the Carnot efficiency is an upper bound that no real engine can reach. Reasons include: friction, non-reversible processes (especially the adiabatic and isobaric processes which have finite temperature differences), heat losses to the surroundings. Real engines always fall below the Carnot limit. (2 marks)

---

## Key Takeaways

1. **$p$–$V$ diagram:** Work = area under the curve. The shape reveals the process type.

2. **Cyclic process:** $\Delta U = 0$ for a complete cycle. Net work = area enclosed by the loop = net heat added.

3. **Clockwise cycle = heat engine** (net work positive). Counterclockwise = refrigerator/heat pump.

4. **Efficiency:** $\eta = W_{\text{net}}/Q_h$. Always < 1. The rejected heat $Q_c$ is NOT wasted — it is a thermodynamic necessity.

5. **Carnot efficiency:** $\eta = 1 - T_c/T_h$ (temperatures in K). This is the THEORETICAL MAXIMUM for any engine between those temperatures.
