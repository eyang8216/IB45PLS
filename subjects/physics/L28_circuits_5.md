# Lesson 28: Circuits V — Capacitors & RC Circuits (HL)

> **IB Data Booklet references:** $C = \frac{Q}{V}$, $C = \varepsilon_0 \frac{A}{d}$, $C = \kappa \varepsilon_0 \frac{A}{d}$, $E = \frac{1}{2}QV = \frac{1}{2}CV^2$, $\tau = RC$, $Q = Q_0(1 - e^{-t/RC})$, $I = I_0 e^{-t/RC}$

## What You'll Learn
- **Capacitance**: $C = Q/V$, energy stored, parallel-plate capacitor
- **Dielectrics**: how they increase capacitance; dielectric constant $\kappa$
- **RC circuits**: the time constant $\tau = RC$
- **Charging and discharging**: exponential growth and decay equations
- How to analyze RC graphs and extract $\tau$

---

## 1. Capacitance

A **capacitor** is a device that stores electrical charge and energy. Two conducting plates separated by an insulator (dielectric) or vacuum.

### Definition of Capacitance

$$\boxed{C = \frac{Q}{V}}$$

| Symbol | Meaning | SI Unit |
|--------|---------|---------|
| $C$ | Capacitance | Farad (F) = C/V |
| $Q$ | Charge stored (on one plate) | Coulomb (C) |
| $V$ | Potential difference across plates | Volt (V) |

> $1\ \mathrm{F}$ is enormous! Most practical capacitors are in $\mathrm{\mu F}$ ($10^{-6}$), $\mathrm{nF}$ ($10^{-9}$), or $\mathrm{pF}$ ($10^{-12}$).

### Capacitance depends on geometry, not charge
For a given capacitor, $C$ is constant (like resistance). Doubling the voltage doubles the charge stored: $Q = CV$.

---

## 2. The Parallel-Plate Capacitor

For two parallel plates of area $A$, separated by distance $d$, with vacuum between:

$$\boxed{C = \varepsilon_0 \frac{A}{d}}$$

where $\varepsilon_0 = 8.85 \times 10^{-12}\ \mathrm{F/m}$ is the **permittivity of free space**.

### Intuition
- **Larger plates** ($A \uparrow$): More "room" for charge → $C \uparrow$
- **Closer plates** ($d \downarrow$): Stronger electric field for given $V$ → more charge for same $V$ → $C \uparrow$
- **Capacitance does NOT depend on $Q$ or $V$** — it's purely geometric (for vacuum)

---

## 3. Dielectric Materials

A **dielectric** is an insulating material placed between capacitor plates. It becomes **polarized** in the electric field, reducing the net field between the plates for a given charge.

### Effect on Capacitance
With a dielectric of **dielectric constant** $\kappa$ (also called relative permittivity $\varepsilon_r$):

$$\boxed{C = \kappa \varepsilon_0 \frac{A}{d} = \kappa C_0}$$

where $C_0$ is the vacuum capacitance.

| Material | $\kappa$ (approx.) |
|----------|-------------------|
| Vacuum | 1 (by definition) |
| Air | 1.0006 |
| Paper | 3.5 |
| Glass | 5–10 |
| Mica | 6–7 |
| Water | 80 |
| Ceramic | 100–1000+ |

### Why dielectrics help
1. **Increased capacitance** — same size, more charge storage for same voltage
2. **Increased maximum voltage** — dielectric prevents sparking/breakdown between plates
3. **Mechanical support** — holds thin plates at fixed separation

### Permittivity
The general formula is $C = \varepsilon_0 \varepsilon_r \frac{A}{d} = \varepsilon \frac{A}{d}$, where $\varepsilon = \kappa \varepsilon_0$ is the absolute permittivity.

---

## 4. Energy Stored in a Capacitor

The energy stored in a charged capacitor is the work done to charge it:

$$\boxed{E = \frac{1}{2}QV = \frac{1}{2}CV^2 = \frac{Q^2}{2C}}$$

### Derivation (qualitative)
Charging is not "all at once" — as charge builds up, the voltage rises ($V = Q/C$), making it progressively harder to add more charge. The average voltage during charging is $V/2$, so work = average voltage × total charge = $\frac{1}{2}QV$.

### Energy density
The energy per unit volume in the electric field between plates:

$$u = \frac{E}{\text{volume}} = \frac{1}{2}\varepsilon_0 E^2$$

---

## 5. RC Circuits — The Time Constant

When a capacitor charges or discharges through a resistor, the voltage and current change **exponentially** (not instantly).

### The Time Constant

$$\boxed{\tau = RC}$$

| Quantity | Unit check |
|----------|-----------|
| $R \times C$ | $\Omega \times \mathrm{F} = (\mathrm{V/A}) \times (\mathrm{C/V}) = \mathrm{C/A} = \mathrm{s}$ |

**$\tau$ is the time for:**
- Voltage to reach **63.2%** of its final value during charging
- Voltage to fall to **36.8%** ($e^{-1}$) of its initial value during discharging
- Current to fall to **36.8%** of its initial value in either case

### Charging Equations

Voltage across capacitor:
$$\boxed{V_C = V_0\left(1 - e^{-t/RC}\right)}$$

Current in circuit:
$$I = I_0 e^{-t/RC}$$

where $V_0$ is the supply voltage and $I_0 = V_0/R$ is the initial current.

### Discharging Equations

Voltage across capacitor:
$$\boxed{V_C = V_0 e^{-t/RC}}$$

Current in circuit:
$$I = I_0 e^{-t/RC}$$

where $V_0$ is the initial capacitor voltage and $I_0 = V_0/R$.

### Behavior at Key Times

| Time | Charging $V_C/V_0$ | Discharging $V_C/V_0$ |
|------|-------------------|----------------------|
| $t = 0$ | 0 (0%) | 1 (100%) |
| $t = \tau$ | $1 - e^{-1} \approx 0.632$ (63.2%) | $e^{-1} \approx 0.368$ (36.8%) |
| $t = 2\tau$ | $1 - e^{-2} \approx 0.865$ (86.5%) | $e^{-2} \approx 0.135$ (13.5%) |
| $t = 3\tau$ | $1 - e^{-3} \approx 0.950$ (95.0%) | $e^{-3} \approx 0.050$ (5.0%) |
| $t = 5\tau$ | $1 - e^{-5} \approx 0.993$ (99.3%) | $e^{-5} \approx 0.007$ (0.7%) |

> **Rule of thumb:** After $5\tau$, the capacitor is "fully" charged or discharged (>99%).

---

## 6. Finding $\tau$ from Graphs

### From a discharging $V$ vs. $t$ graph
- $\tau$ is the time at which $V = 0.368 V_0$
- Alternatively, $\tau$ = time for voltage to halve divided by $\ln 2$ ($t_{1/2} / \ln 2$)

### From a $\ln V$ vs. $t$ graph (linearization)
Taking $\ln$ of the discharge equation: $V = V_0 e^{-t/RC}$

$$\ln V = \ln V_0 - \frac{t}{RC}$$

Plot $\ln V$ (y-axis) vs. $t$ (x-axis):
- **Slope** = $-1/RC$ → $\tau = -1/\text{slope}$
- **y-intercept** = $\ln V_0$

---

## Worked Examples

### Worked Example 28.1 — Energy Stored in a Capacitor
**Problem:** A $470\ \mathrm{\mu F}$ capacitor is charged to $12.0\ \mathrm{V}$. Calculate:
(a) the charge stored
(b) the energy stored

**Solution:**
**(a)** $Q = CV = (470 \times 10^{-6}) \times 12.0 = 5.64 \times 10^{-3}\ \mathrm{C} = 5.64\ \mathrm{mC}$

**(b)** $E = \frac{1}{2}CV^2 = 0.5 \times (470 \times 10^{-6}) \times (12.0)^2 = 0.5 \times 470\times10^{-6} \times 144 = 3.38 \times 10^{-2}\ \mathrm{J} = 33.8\ \mathrm{mJ}$

---

### Worked Example 28.2 — Parallel-Plate Capacitor
**Problem:** A parallel-plate capacitor has plates of area $0.0500\ \mathrm{m^2}$ separated by $0.200\ \mathrm{mm}$. Calculate the capacitance (a) with vacuum, (b) with mica ($\kappa = 6.0$).

**Solution:**
$d = 0.200\ \mathrm{mm} = 2.00 \times 10^{-4}\ \mathrm{m}$

**(a)** $C_0 = \varepsilon_0 \frac{A}{d} = \frac{(8.85 \times 10^{-12})(0.0500)}{2.00 \times 10^{-4}} = 2.21 \times 10^{-9}\ \mathrm{F} = 2.21\ \mathrm{nF}$

**(b)** $C = \kappa C_0 = 6.0 \times 2.21 = 13.3\ \mathrm{nF}$

---

### Worked Example 28.3 — Time Constant and Charging
**Problem:** A $100\ \mathrm{\mu F}$ capacitor is charged through a $50.0\ \mathrm{k\Omega}$ resistor from a $9.00\ \mathrm{V}$ supply.
(a) Calculate the time constant.
(b) Find the capacitor voltage after $3.00\ \mathrm{s}$.
(c) How long until the capacitor voltage reaches $8.00\ \mathrm{V}$?

**Solution:**
**(a)** $\tau = RC = (50.0 \times 10^3) \times (100 \times 10^{-6}) = 50,000 \times 0.000100 = 5.00\ \mathrm{s}$

**(b)** $t = 3.00\ \mathrm{s}$, $t/\tau = 3.00/5.00 = 0.600$
$V_C = 9.00(1 - e^{-0.600}) = 9.00(1 - 0.549) = 9.00 \times 0.451 = 4.06\ \mathrm{V}$

**(c)** $8.00 = 9.00(1 - e^{-t/5.00})$
$1 - e^{-t/5.00} = 8.00/9.00 = 0.889$
$e^{-t/5.00} = 0.111$
$-t/5.00 = \ln(0.111) = -2.20$
$t = 5.00 \times 2.20 = 11.0\ \mathrm{s}$

---

### Worked Example 28.4 — Discharging and Half-life
**Problem:** A $220\ \mathrm{\mu F}$ capacitor charged to $15.0\ \mathrm{V}$ discharges through a $10.0\ \mathrm{k\Omega}$ resistor.
(a) Calculate $\tau$ and the half-life $t_{1/2}$.
(b) What is the capacitor voltage after $4.40\ \mathrm{s}$?

**Solution:**
**(a)** $\tau = RC = (10.0 \times 10^3)(220 \times 10^{-6}) = 2.20\ \mathrm{s}$
$t_{1/2} = \tau \ln 2 = 2.20 \times 0.693 = 1.52\ \mathrm{s}$

**(b)** $t = 4.40\ \mathrm{s} = 2\tau$
$V = V_0 e^{-t/\tau} = 15.0 \times e^{-2} = 15.0 \times 0.135 = 2.03\ \mathrm{V}$

---

### Worked Example 28.5 — RC Graph Analysis (IB-Style)
**Problem:** A student discharges a capacitor through a resistor and records the voltage:

| $t$ (s) | 0 | 10 | 20 | 30 | 40 | 50 | 60 |
|---------|---|---|----|----|----|----|----|
| $V$ (V) | 6.00 | 3.64 | 2.21 | 1.34 | 0.81 | 0.49 | 0.30 |

(a) Plot $\ln V$ vs. $t$ and use the graph to determine the time constant $\tau$. **[4 marks]**
(b) If $C = 470\ \mathrm{\mu F}$, calculate the resistance $R$. **[2 marks]**
(c) Calculate the initial energy stored in the capacitor. **[2 marks]**
(d) Calculate how much energy remains after one time constant. **[3 marks]**

**Solution:**
**(a)** Calculate $\ln V$:

| $t$ (s) | 0 | 10 | 20 | 30 | 40 | 50 | 60 |
|---------|---|---|----|----|----|----|----|
| $\ln V$ | 1.79 | 1.29 | 0.793 | 0.293 | -0.211 | -0.713 | -1.20 |

Plot $\ln V$ (y) vs. $t$ (x). This should be a straight line.

Gradient: Using endpoints $\frac{-1.20 - 1.79}{60 - 0} = \frac{-2.99}{60} = -0.0498\ \mathrm{s^{-1}}$

$\tau = -1/\text{gradient} = -1/(-0.0498) = 20.1\ \mathrm{s}$

(Or read from original: $V = 0.368 \times 6.00 = 2.21\ \mathrm{V}$, which occurs at $t = 20\ \mathrm{s}$ → $\tau \approx 20\ \mathrm{s}$) ✓✓✓✓

**(b)** $\tau = RC$
$R = \frac{\tau}{C} = \frac{20.1}{470 \times 10^{-6}} = 4.28 \times 10^4\ \Omega = 42.8\ \mathrm{k\Omega}$ ✓✓

**(c)** $E_0 = \frac{1}{2}CV_0^2 = 0.5 \times (470 \times 10^{-6}) \times 6.00^2 = 0.5 \times 470\times10^{-6} \times 36 = 8.46 \times 10^{-3}\ \mathrm{J} = 8.46\ \mathrm{mJ}$ ✓✓

**(d)** After one time constant, $V = V_0 e^{-1} = 6.00 \times 0.368 = 2.21\ \mathrm{V}$
$E = \frac{1}{2}CV^2 = 0.5 \times (470\times10^{-6}) \times (2.21)^2 = 0.5 \times 470\times10^{-6} \times 4.88 = 1.15 \times 10^{-3}\ \mathrm{J} = 1.15\ \mathrm{mJ}$

Alternatively: $E = E_0(e^{-1})^2 = E_0 e^{-2} = 8.46 \times 0.135 = 1.14\ \mathrm{mJ}$ ✓✓✓

---

## Practice Problems

### Problem 1 — Capacitance Basics
A $220\ \mathrm{\mu F}$ capacitor stores $1.10 \times 10^{-3}\ \mathrm{C}$ of charge. Calculate: (a) the voltage across it, (b) the energy stored. **[2 marks]**

### Problem 2 — Dielectric Effect
A parallel-plate capacitor with vacuum has capacitance $50.0\ \mathrm{pF}$. A dielectric of $\kappa = 4.0$ is inserted, completely filling the space. Calculate: (a) the new capacitance, (b) the factor by which the energy stored changes if the capacitor remains connected to a battery. **[3 marks]**

### Problem 3 — RC Charging
A $100\ \mathrm{\mu F}$ capacitor is charged through a $20.0\ \mathrm{k\Omega}$ resistor from a $6.00\ \mathrm{V}$ supply. (a) Calculate the time constant. (b) At what time will the capacitor voltage be $4.00\ \mathrm{V}$? **[3 marks]**

### Problem 4 — RC Discharging Half-life
A capacitor discharges through a resistor. Its voltage falls from $12.0\ \mathrm{V}$ to $6.0\ \mathrm{V}$ in $3.50\ \mathrm{s}$. (a) Calculate the half-life and the time constant. (b) What will the voltage be after $10.0\ \mathrm{s}$? **[4 marks]**

### Problem 5 — IB-Style: Comprehensive RC Analysis
A student investigates an RC circuit using a $9.00\ \mathrm{V}$ battery, a switch, a $47.0\ \mathrm{k\Omega}$ resistor, and an unknown capacitor $C$. She charges the capacitor fully, then flips the switch to discharge mode and records:

| $t$ (s) | 0 | 5.0 | 10.0 | 15.0 | 20.0 | 25.0 |
|---------|---|-----|------|------|------|------|
| $V$ (V) | 9.00 | 6.32 | 4.44 | 3.11 | 2.19 | 1.54 |

(a) Explain why the voltage decreases exponentially rather than linearly. **[2 marks]**
(b) Use the data to determine the time constant $\tau$ by two methods. **[4 marks]**
(c) Calculate the capacitance $C$. **[2 marks]**
(d) Calculate the initial current when the discharge begins. **[1 mark]**
(e) The student repeats with a $94.0\ \mathrm{k\Omega}$ resistor instead. Sketch (on the same axes) how the discharge curve would differ. Explain the difference. **[3 marks]**

---

## Answers

### Answer 1
**(a)** $V = Q/C = 1.10\times10^{-3} / (220\times10^{-6}) = 5.00\ \mathrm{V}$
**(b)** $E = \frac{1}{2}QV = 0.5 \times 1.10\times10^{-3} \times 5.00 = 2.75 \times 10^{-3}\ \mathrm{J} = 2.75\ \mathrm{mJ}$ ✓✓

### Answer 2
**(a)** $C = \kappa C_0 = 4.0 \times 50.0 = 200\ \mathrm{pF}$
**(b)** Connected to battery → $V$ is constant. $E = \frac{1}{2}CV^2$, so $E \propto C$.
Energy increases by factor $\kappa = 4.0$. (The battery supplies additional charge.) ✓✓✓

### Answer 3
**(a)** $\tau = RC = (20.0 \times 10^3)(100 \times 10^{-6}) = 2.00\ \mathrm{s}$
**(b)** $V = V_0(1 - e^{-t/\tau})$, so $4.00 = 6.00(1 - e^{-t/2.00})$
$1 - e^{-t/2.00} = 0.667$, $e^{-t/2.00} = 0.333$
$-t/2.00 = \ln(0.333) = -1.10$
$t = 2.20\ \mathrm{s}$ ✓✓✓

### Answer 4
**(a)** Voltage halves in $3.50\ \mathrm{s}$ → $t_{1/2} = 3.50\ \mathrm{s}$
$\tau = t_{1/2} / \ln 2 = 3.50 / 0.693 = 5.05\ \mathrm{s}$
**(b)** $V = V_0 e^{-t/\tau} = 12.0 \times e^{-10.0/5.05} = 12.0 \times e^{-1.98} = 12.0 \times 0.138 = 1.66\ \mathrm{V}$ ✓✓✓✓

### Answer 5 — IB-Style Full Solution
**(a)** During discharge, the current $I = V/R$. But $V$ is also related to $Q$ by $V = Q/C$. As charge leaves, $V$ decreases, reducing the current, which reduces the rate of charge loss. This self-limiting feedback produces an exponential, not linear, decay: $\frac{dQ}{dt} = -\frac{Q}{RC}$ → $Q = Q_0 e^{-t/RC}$. ✓✓

**(b)** **Method 1 — $36.8\%$ point:** $0.368 \times 9.00 = 3.31\ \mathrm{V}$. From data, this is between $t = 10\ \mathrm{s}$ ($4.44\ \mathrm{V}$) and $t = 15\ \mathrm{s}$ ($3.11\ \mathrm{V}$). Interpolation: $\tau \approx 14\ \mathrm{s}$.

**Method 2 — $\ln V$ graph:**
| $t$ | 0 | 5 | 10 | 15 | 20 | 25 |
|-----|---|---|----|----|----|----|
| $\ln V$ | 2.20 | 1.84 | 1.49 | 1.13 | 0.784 | 0.432 |

Gradient $\approx (0.432 - 2.20)/(25 - 0) = -1.768/25 = -0.0707$
$\tau = -1/(-0.0707) = 14.1\ \mathrm{s}$

Also check: $t_{1/2}$ is when $V = 4.5\ \mathrm{V}$ → about $9.8\ \mathrm{s}$. $\tau = 9.8/\ln 2 = 14.1\ \mathrm{s}$.

$\tau \approx 14.0\ \mathrm{s}$ ✓✓✓✓

**(c)** $C = \tau/R = 14.0 / (47.0 \times 10^3) = 2.98 \times 10^{-4}\ \mathrm{F} = 298\ \mathrm{\mu F} \approx 300\ \mathrm{\mu F}$ ✓✓

**(d)** $I_0 = V_0/R = 9.00 / (47.0 \times 10^3) = 1.91 \times 10^{-4}\ \mathrm{A} = 191\ \mathrm{\mu A}$ ✓

**(e)** With $R = 94.0\ \mathrm{k\Omega}$ (doubled), $\tau = 28.0\ \mathrm{s}$ (doubled). The new discharge curve would:
- Start at the same $V_0 = 9.00\ \mathrm{V}$
- Decay **more slowly** — the curve is less steep
- The initial current is halved ($I_0 = 95.5\ \mathrm{\mu A}$)

Sketch: both curves start at $(0, 9.00)$. The $94\ \mathrm{k\Omega}$ curve always lies **above** the $47\ \mathrm{k\Omega}$ curve at any $t > 0$, because the larger resistance allows slower discharge. ✓✓✓

---

## Key Takeaways
1. **Capacitance** $C = Q/V$ measures charge storage per volt. For a parallel-plate: $C = \kappa \varepsilon_0 A/d$.
2. **Dielectrics** increase capacitance by factor $\kappa$: they polarize, reducing the net electric field.
3. **Energy stored**: $E = \frac{1}{2}CV^2 = \frac{1}{2}QV = Q^2/(2C)$.
4. **RC time constant**: $\tau = RC$. After $\tau$, a charging capacitor reaches 63.2% of final voltage; a discharging one falls to 36.8%.
5. **Charging**: $V = V_0(1 - e^{-t/RC})$. **Discharging**: $V = V_0 e^{-t/RC}$.
6. Use $\ln V$ vs. $t$ graphs to find $\tau$ from the gradient = $-1/RC$. After $5\tau$, charging/discharging is ~99% complete.

---

*This concludes the Circuits series and the full set of Gas Laws, Thermodynamics, and Circuits lessons for IB Physics HL.*
