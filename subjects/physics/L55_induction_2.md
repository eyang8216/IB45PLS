# Lesson 55: Induction II — AC Generators, RMS Values and Power

## What You'll Learn
- Explain how a rotating coil in a magnetic field generates sinusoidal EMF
- Calculate peak EMF using $\varepsilon_0 = NBA\omega$
- Define and use RMS (root-mean-square) values for AC voltage and current
- Distinguish between AC generators (slip rings) and DC generators (commutator)

---

## 1. The AC Generator — Turning Motion into Electricity

### 1.1 Why This Matters

Nearly all the electricity on Earth is produced by generators that spin coils in magnetic fields. Whether the turbine is turned by steam (coal, gas, nuclear), falling water (hydroelectric), or wind, the physics at the generator is the same: a coil rotates in a magnetic field, the flux through it changes continuously, and an alternating EMF is induced. Understanding the AC generator is understanding where electricity comes from.

### 1.2 The Rotating Coil

Consider a rectangular coil of $N$ turns, each of area $A$, rotating at constant angular velocity $\omega$ in a uniform magnetic field $B$. At time $t$, the angle between the field and the normal to the coil is $\theta = \omega t$ (if $\theta = 0$ at $t = 0$).

The flux through one turn is:
$$\Phi = BA\cos\theta = BA\cos(\omega t)$$

By Faraday's Law, the induced EMF is:
$$\varepsilon = -N\frac{d\Phi}{dt} = -N(-BA\omega\sin(\omega t)) = NBA\omega\sin(\omega t)$$

### 1.3 The Generator Equation

$$\varepsilon = \varepsilon_0\sin(\omega t) \quad \text{where} \quad \varepsilon_0 = NBA\omega$$

- $\varepsilon_0$ is the **peak EMF** (maximum value)
- $N$ = number of turns
- $B$ = magnetic field strength
- $A$ = area of each turn
- $\omega = 2\pi f$ = angular frequency

The output is a sinusoidal voltage. The EMF is zero when the coil is perpendicular to the field ($\theta = 0^\circ$, flux maximum but not changing) and maximum in magnitude when the coil is parallel to the field ($\theta = 90^\circ$, flux zero but changing fastest).

### 1.4 Slip Rings

To connect the rotating coil to the external circuit without twisting the wires, the coil ends are connected to **slip rings** — continuous circular contacts that rotate with the coil. Carbon brushes press against the rings, conducting current to the external circuit. Because the connections never reverse, the output alternates between positive and negative — true AC.

---

## 2. RMS Values — What "230 Volts" Really Means

### 2.1 Why Not Just Use Peak?

Mains electricity in Europe is described as "230 V AC." But the voltage is constantly changing from $+325\text{ V}$ to $-325\text{ V}$ and back, 50 times per second. What does "230 V" mean?

The power delivered to a resistor depends on $V^2$. The average of $\sin^2(\omega t)$ over a complete cycle is $\frac{1}{2}$. So the average power is half the peak power:

$$P_{\text{avg}} = \frac{V_0^2}{2R}$$

The **RMS (root-mean-square) voltage** is the DC voltage that would deliver the same average power:

$$V_{\text{rms}} = \frac{V_0}{\sqrt{2}} \qquad I_{\text{rms}} = \frac{I_0}{\sqrt{2}}$$

For sinusoidal AC:
$$V_{\text{rms}} \approx 0.707\,V_0$$

For UK mains ($V_{\text{rms}} = 230\text{ V}$): $V_0 = 230 \times \sqrt{2} = 325\text{ V}$. The peak-to-peak voltage is $650\text{ V}$.

### 2.2 Why RMS Matters

Almost all AC meters display RMS values. When you see "230 V" on a multimeter, it's $V_{\text{rms}}$. Power calculations with RMS values work exactly like DC formulas:
$$P_{\text{avg}} = I_{\text{rms}}V_{\text{rms}} = I_{\text{rms}}^2R = \frac{V_{\text{rms}}^2}{R}$$

---

## 3. The DC Generator — The Commutator

### 3.1 Converting AC to Pulsating DC

Replace the slip rings with a **split-ring commutator**. The commutator reverses the coil's connection to the external circuit every half-turn, exactly when the EMF would reverse. The output never goes negative — it is a rectified sine wave:

$$\varepsilon = |\varepsilon_0\sin(\omega t)|$$

This is pulsating DC — it always pushes current in the same direction, but the magnitude still varies. For smoother DC, multiple coils at different angles are used, each contributing overlapping pulses.

---

## Worked Examples

### Worked Example 55.1 — Generator Peak EMF

**Problem:** A generator coil has 250 turns, each of area $0.015\text{ m}^2$, rotating at 3,600 rpm in a $0.20\text{ T}$ field. Find the peak EMF and output frequency.

**Solution:**
$f = 3,600/60 = 60\text{ Hz}$. $\omega = 2\pi(60) = 377\text{ rad s}^{-1}$. $\varepsilon_0 = (250)(0.20)(0.015)(377) = 283\text{ V}$. Frequency = 60 Hz.

---

### Worked Example 55.2 — RMS Values

**Problem:** UK mains is $230\text{ V}$ RMS at $50\text{ Hz}$. Find the peak voltage and peak-to-peak voltage.

**Solution:**
$V_0 = 230 \times \sqrt{2} = 325\text{ V}$. $V_{\text{pp}} = 2 \times 325 = 650\text{ V}$.

---

### Worked Example 55.3 — AC Power

**Problem:** A $60\text{ W}$, $120\text{ V}$ (RMS) light bulb operates on AC mains. Find its resistance and the peak current.

**Solution:**
$R = V_{\text{rms}}^2/P = 120^2/60 = 240\text{ Ω}$. $I_{\text{rms}} = P/V_{\text{rms}} = 60/120 = 0.50\text{ A}$. $I_0 = 0.50 \times \sqrt{2} = 0.707\text{ A}$.

---

### Worked Example 55.4 — IB-Style Generator Problem

**Problem:** A simple AC generator has a rectangular coil of 500 turns, dimensions 5.0 cm × 10 cm, rotating at 50 revolutions per second in a 0.15 T field.

(a) Calculate the peak EMF. (2 marks)
(b) Calculate the RMS voltage. (1 mark)
(c) The coil is connected to a 100 Ω resistor. Calculate the average power dissipated. (2 marks)
(d) If the rotation speed doubles, state how this affects: (i) the peak EMF, (ii) the frequency, and (iii) the average power. (3 marks)

**Solution:**
**(a)** $A = 0.050 \times 0.10 = 5.0 \times 10^{-3}\text{ m}^2$. $f = 50\text{ Hz}$, $\omega = 2\pi(50) = 314\text{ rad s}^{-1}$. $\varepsilon_0 = (500)(0.15)(5.0 \times 10^{-3})(314) = 118\text{ V}$.

**(b)** $V_{\text{rms}} = 118/\sqrt{2} = 83.4\text{ V}$.

**(c)** $P = V_{\text{rms}}^2/R = 83.4^2/100 = 69.5\text{ W}$.

**(d)** (i) $\varepsilon_0 \propto \omega$, so peak EMF doubles. (ii) Frequency doubles (from 50 to 100 Hz). (iii) $P \propto \varepsilon_0^2$, so power quadruples — double the EMF gives four times the power at the same resistance.

---

## Practice Problems

### Problem 1
A generator coil has 400 turns of area $0.010\text{ m}^2$ in a $0.25\text{ T}$ field, rotating at 1,800 rpm. Find the peak EMF.

### Problem 2
An AC source has a peak voltage of $170\text{ V}$. Calculate the RMS voltage. A $50\text{ Ω}$ resistor is connected. Find the RMS current and average power.

### Problem 3
Sketch the output waveform of an AC generator (slip rings) and a DC generator (commutator) for two complete rotations, starting at $\theta = 0$.

### Problem 4
Explain why the EMF from a rotating coil is sinusoidal. What determines when the EMF is maximum and when it is zero?

### Problem 5 — IB-Style
A generator consists of a 250-turn coil of area $0.020\text{ m}^2$ rotating at frequency $f$ in a $0.12\text{ T}$ field. The output is connected to a data logger.

(a) When $f = 25\text{ Hz}$, the peak EMF is measured as $94\text{ V}$. Determine whether this is consistent with the theoretical value. (2 marks)
(b) The rotation frequency is increased to $50\text{ Hz}$. Calculate the new peak EMF and RMS voltage. (2 marks)
(c) A $200\text{ Ω}$ resistor is connected. Calculate the power dissipated at $f = 50\text{ Hz}$. (2 marks)
(d) The generator is converted to DC output by replacing slip rings with a commutator. Sketch the new waveform for one rotation and explain qualitatively how the average power delivered compares to the AC case. (3 marks)

---

## Answers

### Answer 1
$f = 1,800/60 = 30\text{ Hz}$. $\omega = 2\pi(30) = 188.5\text{ rad s}^{-1}$. $\varepsilon_0 = (400)(0.25)(0.010)(188.5) = 189\text{ V}$.

### Answer 2
$V_{\text{rms}} = 170/\sqrt{2} = 120\text{ V}$. $I_{\text{rms}} = 120/50 = 2.4\text{ A}$. $P = (2.4)(120) = 288\text{ W}$, or $P = 120^2/50 = 288\text{ W}$.

### Answer 3
AC (slip rings): sine wave crossing zero twice per cycle. DC (commutator): $|\sin|$ shape, always positive, touches zero twice per cycle. Both have the same peak value.

### Answer 4
$\Phi = BA\cos(\omega t)$. $\varepsilon = -d\Phi/dt = BA\omega\sin(\omega t)$. EMF is sinusoidal because the derivative of a cosine is a sine. EMF is zero when $\sin(\omega t) = 0$ — when the coil is perpendicular to the field (flux at maximum). EMF peaks when $\sin(\omega t) = \pm 1$ — when the coil is parallel to the field (flux zero, changing fastest).

### Answer 5 — IB-Style
**(a)** $\omega = 2\pi(25) = 157\text{ rad s}^{-1}$. $\varepsilon_0 = (250)(0.12)(0.020)(157) = 94.2\text{ V}$. Measured value is 94 V — excellent agreement. (2 marks)

**(b)** Doubling $f$ doubles $\omega$, so $\varepsilon_0 = 188\text{ V}$. $V_{\text{rms}} = 188/\sqrt{2} = 133\text{ V}$. (2 marks)

**(c)** $P = V_{\text{rms}}^2/R = 133^2/200 = 88.4\text{ W}$. (2 marks)

**(d)** (3 marks) DC waveform is $|\varepsilon_0\sin(\omega t)|$ — always positive. The average power with a resistive load is the same as AC for the same peak voltage because $P \propto V^2$ and $|V|^2 = V^2$ — squaring removes the negative signs. However, practical DC generators use multiple coils to reduce pulsation. (1 mark for correct sketch, 1 mark for noting power is the same, 1 mark for explaining why.)

---

## Key Takeaways

1. **AC generator:** $\varepsilon = \varepsilon_0\sin(\omega t)$ where $\varepsilon_0 = NBA\omega$. Sinusoidal because $\Phi = BA\cos(\omega t)$.

2. **RMS values:** $V_{\text{rms}} = V_0/\sqrt{2}$. This is what meters display. Power calculations use RMS: $P = I_{\text{rms}}V_{\text{rms}}$.

3. **Slip rings = AC.** **Commutator = pulsating DC** (always same polarity).

4. **Peak EMF** depends on $N$, $B$, $A$, and $\omega$. Double the rotation speed → double the frequency AND quadruple the power.
