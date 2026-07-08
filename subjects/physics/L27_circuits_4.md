# Lesson 27: Circuits IV — EMF, Internal Resistance & Power

> **IB Data Booklet references:** $\varepsilon = V + Ir$, $P = IV = I^2 R = \frac{V^2}{R}$, $V = IR$

## What You'll Learn
- **EMF** vs. **terminal voltage**: $\varepsilon = V + Ir$
- **Internal resistance** of batteries and cells
- **Power** in circuits: $P = IV = I^2R = V^2/R$
- **Maximum power transfer** theorem
- **Energy dissipation** and circuit **efficiency**

---

## 1. EMF and Internal Resistance

### Electromotive Force (EMF)
The **EMF** $\varepsilon$ of a source is the **total energy supplied per unit charge** — the work done by the source to drive charge around a complete circuit. It is measured in **volts** (J/C).

> Despite its name, EMF is **not a force** — it's a potential difference (voltage). It represents the maximum voltage a source can provide when no current is drawn.

### Terminal Voltage
The **terminal voltage** $V$ is the actual voltage available across the terminals of the source when current is flowing. It is **always less than the EMF** because some energy is lost overcoming the **internal resistance** $r$ of the source.

$$\boxed{\varepsilon = V + Ir}$$

or equivalently:

$$\boxed{V = \varepsilon - Ir}$$

### What is internal resistance?
Inside every real battery or cell, the chemical reactions and physical construction create an unavoidable resistance to current flow. This $r$ behaves as if it's a small resistor **in series** with an ideal EMF source.

| Condition | Terminal voltage |
|-----------|-----------------|
| Open circuit ($I = 0$) | $V = \varepsilon$ |
| Normal operation | $V = \varepsilon - Ir$ |
| Short circuit ($R_{\text{ext}} = 0$) | $V = 0$, $I = \varepsilon/r$ (very large!) |

### Full Circuit Equation
For a source (EMF $\varepsilon$, internal resistance $r$) connected to an external load $R$:

$$\varepsilon = I(R + r)$$

$$I = \frac{\varepsilon}{R + r}$$

---

## 2. Finding Internal Resistance Experimentally

### Method: Vary Load, Measure V and I
Connect the cell to a variable resistor (rheostat). Measure terminal voltage $V$ and current $I$ for different load settings.

From $V = \varepsilon - Ir$, a graph of $V$ (y-axis) vs. $I$ (x-axis) gives:
- **y-intercept** = $\varepsilon$ (EMF, when $I = 0$)
- **gradient** = $-r$ (negative internal resistance)
- **x-intercept** = $\varepsilon/r$ (short-circuit current)

> **IB exam tip:** The gradient is **negative**, so $r = |\text{gradient}|$. Be explicit about this!

---

## 3. Electrical Power

**Power** is the rate at which energy is transferred or converted:

$$\boxed{P = IV}$$

Using Ohm's Law ($V = IR$), we get three equivalent forms:

$$\boxed{P = IV = I^2 R = \frac{V^2}{R}}$$

| Form | Best used when… |
|------|-----------------|
| $P = IV$ | You know current and voltage (general; always works) |
| $P = I^2R$ | You know current and resistance (power lost in a resistor) |
| $P = V^2/R$ | You know voltage and resistance (parallel circuits, fixed $V$) |

### Power in Series vs. Parallel
- **Series** (same $I$): $P \propto R$ — the largest resistor dissipates the most power
- **Parallel** (same $V$): $P \propto 1/R$ — the smallest resistor dissipates the most power

---

## 4. Power Transfer and Efficiency

### Total Power from a Source
The total power produced by a source: $P_{\text{total}} = \varepsilon I$

Power delivered to external circuit: $P_{\text{external}} = VI = I^2 R$

Power wasted in internal resistance: $P_{\text{internal}} = I^2 r$

### Efficiency
$$\eta = \frac{P_{\text{useful}}}{P_{\text{total}}} = \frac{I^2 R}{I^2(R + r)} = \frac{R}{R + r}$$

### Maximum Power Transfer
Maximum power is delivered to the load when:

$$\boxed{R = r}$$

(the load resistance equals the internal resistance). At this point, $\eta = 50\%$ — half the power is wasted internally.

> In practice, power systems operate with $R \gg r$ to maximize efficiency, even though this doesn't maximize power output.

---

## 5. Energy Dissipation

Electrical energy converted to heat in a resistor:

$$E = Pt = IVt = I^2Rt = \frac{V^2}{R}t$$

- $1\ \mathrm{J} = 1\ \mathrm{W} \times 1\ \mathrm{s}$
- For larger amounts: $\mathrm{kWh}$ (kilowatt-hour) = $3.6 \times 10^6\ \mathrm{J}$

---

## Worked Examples

### Worked Example 27.1 — Terminal Voltage
**Problem:** A battery has EMF $12.0\ \mathrm{V}$ and internal resistance $r = 0.500\ \Omega$. It is connected to an external resistor $R = 5.50\ \Omega$. Calculate:
(a) the circuit current
(b) the terminal voltage
(c) the power delivered to the external resistor
(d) the power wasted in the battery

**Solution:**
**(a)** $I = \frac{\varepsilon}{R + r} = \frac{12.0}{5.50 + 0.500} = \frac{12.0}{6.00} = 2.00\ \mathrm{A}$

**(b)** $V = \varepsilon - Ir = 12.0 - (2.00)(0.500) = 12.0 - 1.00 = 11.0\ \mathrm{V}$

**(c)** $P_{\text{ext}} = I^2 R = (2.00)^2 \times 5.50 = 22.0\ \mathrm{W}$
Or: $P_{\text{ext}} = V I = 11.0 \times 2.00 = 22.0\ \mathrm{W}$

**(d)** $P_{\text{int}} = I^2 r = (2.00)^2 \times 0.500 = 2.00\ \mathrm{W}$

Check: Total $P = \varepsilon I = 12.0 \times 2.00 = 24.0\ \mathrm{W} = 22.0 + 2.00$ ✓

---

### Worked Example 27.2 — Finding EMF and r from Data
**Problem:** A student measures the terminal voltage of a cell for different currents:

| $I$ (A) | 0.00 | 0.50 | 1.00 | 1.50 | 2.00 |
|---------|------|------|------|------|------|
| $V$ (V) | 1.58 | 1.45 | 1.32 | 1.18 | 1.05 |

Determine the EMF and internal resistance of the cell.

**Solution:**
EMF $\varepsilon$ = y-intercept = $V$ when $I = 0$ = **1.58 V**

Gradient = $\frac{\Delta V}{\Delta I} = \frac{1.05 - 1.58}{2.00 - 0.00} = \frac{-0.53}{2.00} = -0.265$

$r = |\text{gradient}| = 0.265\ \Omega$

Check: $V = \varepsilon - Ir \Rightarrow 1.45 \approx 1.58 - 0.50(0.265) = 1.58 - 0.133 = 1.447$ ✓

---

### Worked Example 27.3 — Power Comparison
**Problem:** A $12\ \mathrm{V}$ supply is connected to (a) a single $6.0\ \Omega$ resistor, (b) two $6.0\ \Omega$ resistors in series, (c) two $6.0\ \Omega$ resistors in parallel.
Calculate the total power dissipated in each case.

**Solution:**
**(a)** $P = \frac{V^2}{R} = \frac{12^2}{6.0} = 24\ \mathrm{W}$

**(b)** $R_{\text{total}} = 12\ \Omega$, $P = \frac{12^2}{12} = 12\ \mathrm{W}$
(Each gets 6 W — half the voltage, quarter the power individually)

**(c)** $R_{\text{total}} = 3.0\ \Omega$, $P = \frac{12^2}{3.0} = 48\ \mathrm{W}$
(Each gets 24 W — full voltage, double the current of single case)

---

### Worked Example 27.4 — Maximum Power Transfer
**Problem:** A source has EMF $9.0\ \mathrm{V}$ and internal resistance $r = 3.0\ \Omega$. What value of load resistance $R$ will receive maximum power, and what is that power?

**Solution:**
Maximum power when $R = r = 3.0\ \Omega$.

$I = \frac{\varepsilon}{R + r} = \frac{9.0}{6.0} = 1.5\ \mathrm{A}$

$P_{\text{max}} = I^2 R = (1.5)^2 \times 3.0 = 6.75\ \mathrm{W}$

Efficiency: $\eta = \frac{R}{R + r} = \frac{3.0}{6.0} = 50\%$

---

### Worked Example 27.5 — Battery Efficiency (IB-Style)
**Problem:** A $6.0\ \mathrm{V}$ battery with $r = 0.80\ \Omega$ powers a $4.0\ \Omega$ load.

(a) Calculate the current and terminal voltage. **[2 marks]**
(b) Calculate the power delivered to the load and the power dissipated in the battery. **[2 marks]**
(c) Calculate the efficiency of power transfer. **[1 mark]**
(d) The load is changed. For what load resistance would the efficiency be 90%? **[3 marks]**
(e) At this 90% efficiency load, what power is delivered to the load? How does this compare to the maximum possible power? **[3 marks]**

---

**Solution:**
**(a)** $I = \frac{6.0}{4.0 + 0.80} = 1.25\ \mathrm{A}$
$V = 6.0 - (1.25)(0.80) = 6.0 - 1.00 = 5.0\ \mathrm{V}$ ✓✓

**(b)** $P_{\text{load}} = I^2 R = (1.25)^2 \times 4.0 = 6.25\ \mathrm{W}$
$P_{\text{int}} = I^2 r = (1.25)^2 \times 0.80 = 1.25\ \mathrm{W}$ ✓✓

**(c)** $\eta = \frac{R}{R + r} = \frac{4.0}{4.0 + 0.80} = 0.833 = 83.3\%$ ✓

**(d)** $\eta = \frac{R}{R + r} = 0.90$
$R = 0.90(R + 0.80) \Rightarrow R = 0.90R + 0.72 \Rightarrow 0.10R = 0.72 \Rightarrow R = 7.2\ \Omega$ ✓✓✓

**(e)** $I = \frac{6.0}{7.2 + 0.80} = 0.75\ \mathrm{A}$
$P = I^2 R = (0.75)^2 \times 7.2 = 4.05\ \mathrm{W}$

Maximum power transfer occurs at $R = r = 0.80\ \Omega$:
$P_{\text{max}} = (\frac{6.0}{1.60})^2 \times 0.80 = (3.75)^2 \times 0.80 = 14.06 \times 0.80 = 11.25\ \mathrm{W}$

The 90% efficiency load delivers **much less power** (4.05 W vs. 11.25 W) but uses the battery's energy far more efficiently. This is the classic engineering trade-off: power vs. efficiency! ✓✓✓

---

## Practice Problems

### Problem 1 — Terminal Voltage
A cell has EMF $1.50\ \mathrm{V}$ and internal resistance $0.200\ \Omega$. It is connected to an external $2.80\ \Omega$ resistor. Calculate: (a) the current, (b) the terminal voltage. **[2 marks]**

### Problem 2 — Finding EMF and r
A student obtains these data for a battery: $V = 8.40\ \mathrm{V}$ at $I = 0.50\ \mathrm{A}$; $V = 7.80\ \mathrm{V}$ at $I = 1.00\ \mathrm{A}$. Find the EMF and internal resistance. **[3 marks]**

### Problem 3 — Power Dissipation
A $24\ \Omega$ resistor is connected to a $12\ \mathrm{V}$ supply with negligible internal resistance. Calculate the power dissipated. Then calculate the new power if a second $24\ \Omega$ resistor is added (a) in series, (b) in parallel. **[4 marks]**

### Problem 4 — Short Circuit Danger
Explain why short-circuiting a car battery (12 V, $r \approx 0.01\ \Omega$) is extremely dangerous, using calculations to support your answer. **[3 marks]**

### Problem 5 — IB-Style: EMF Experiment Analysis
A student investigates a solar cell by connecting it to a variable resistor and measuring $V$ and $I$. The data are:

| $V$ (V) | 0.00 | 0.20 | 0.40 | 0.50 | 0.55 | 0.60 |
|---------|------|------|------|------|------|------|
| $I$ (mA) | 50.0 | 48.0 | 42.0 | 32.0 | 20.0 | 0.0 |

(a) Plot a graph of $V$ vs. $I$ and determine the EMF of the solar cell. **[2 marks]**
(b) Determine the short-circuit current. **[1 mark]**
(c) Calculate the internal resistance near $I = 30\ \mathrm{mA}$. **[2 marks]**
(d) Calculate the maximum power output of the solar cell from the data. **[3 marks]**
(e) Explain why a solar cell's internal resistance is not constant, unlike a simple battery. **[2 marks]**

---

## Answers

### Answer 1
**(a)** $I = \frac{1.50}{2.80 + 0.200} = \frac{1.50}{3.00} = 0.500\ \mathrm{A}$
**(b)** $V = 1.50 - (0.500)(0.200) = 1.50 - 0.100 = 1.40\ \mathrm{V}$ ✓✓

### Answer 2
$V = \varepsilon - Ir$
$8.40 = \varepsilon - 0.50r$ …(1)
$7.80 = \varepsilon - 1.00r$ …(2)

(1) − (2): $0.60 = 0.50r \Rightarrow r = 1.20\ \Omega$
From (1): $\varepsilon = 8.40 + 0.50(1.20) = 8.40 + 0.60 = 9.00\ \mathrm{V}$

EMF = $9.00\ \mathrm{V}$, $r = 1.20\ \Omega$ ✓✓✓

### Answer 3
Single: $P = V^2/R = 12^2/24 = 6.0\ \mathrm{W}$
**(a)** Series: $R = 48\ \Omega$, $P = 12^2/48 = 3.0\ \mathrm{W}$ (half)
**(b)** Parallel: $R = 12\ \Omega$, $P = 12^2/12 = 12\ \mathrm{W}$ (double) ✓✓✓✓

### Answer 4
In a short circuit, $R_{\text{ext}} \approx 0$, so $I = \varepsilon/r = 12/0.01 = 1200\ \mathrm{A}$.
$P = I^2 r = (1200)^2 \times 0.01 = 14,400\ \mathrm{W} = 14.4\ \mathrm{kW}$ dissipated as heat in the battery.

This enormous current can cause the battery to overheat, explode, or melt the wires. Extremely dangerous! ✓✓✓

### Answer 5 — IB-Style Full Solution
**(a)** Plot $V$ (y-axis) vs $I$ (x-axis) in amps (convert mA: 0.050, 0.048, 0.042, 0.032, 0.020, 0.000).
EMF = $V$ when $I = 0$ = **0.60 V**. ✓✓

**(b)** Short-circuit current = $I$ when $V = 0$ = **50.0 mA** = 0.0500 A. ✓

**(c)** Near $I = 30\ \mathrm{mA} = 0.030\ \mathrm{A}$: From data, near $(0.032, 0.50)$ and $(0.020, 0.55)$.
$r = \left|\frac{\Delta V}{\Delta I}\right| = \frac{0.55 - 0.50}{0.020 - 0.032} = \frac{0.05}{-0.012} \approx 4.2\ \Omega$ ✓✓

**(d)** Power $P = VI$. Calculate for each data point:
$(0)(0.050) = 0$, $(0.20)(0.048) = 9.6\ \mathrm{mW}$, $(0.40)(0.042) = 16.8\ \mathrm{mW}$, 
$(0.50)(0.032) = 16.0\ \mathrm{mW}$, $(0.55)(0.020) = 11.0\ \mathrm{mW}$, $(0.60)(0) = 0$

Maximum power $\approx$ **16.8 mW** at $V = 0.40\ \mathrm{V}$, $I = 42\ \mathrm{mA}$. ✓✓✓

**(e)** A solar cell is a semiconductor device, not a simple chemical cell. Its internal resistance depends on the illumination level, the operating point on its I–V curve, and the semiconductor junction properties. It doesn't follow the simple linear $V = \varepsilon - Ir$ model of a chemical battery. ✓✓

---

## Key Takeaways
1. **EMF** $\varepsilon$ is the total energy per unit charge supplied. **Terminal voltage** $V = \varepsilon - Ir$ is always less when current flows.
2. **Internal resistance** $r$ acts like a resistor in series with the ideal source.
3. From a $V$ vs. $I$ graph: y-intercept = $\varepsilon$, gradient = $-r$.
4. **Power**: $P = IV = I^2R = V^2/R$. Use the form that matches what you know.
5. **Maximum power transfer** occurs when $R = r$, but efficiency is only 50%. For high efficiency, use $R \gg r$.
6. **Efficiency**: $\eta = R/(R + r) = V/\varepsilon$.

---

*Next: Lesson 28 — Circuits V: Capacitors & RC Circuits (HL)*
