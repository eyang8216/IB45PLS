# Lesson 30: Simple Harmonic Motion II — Kinematics: Displacement, Velocity, Acceleration, and Phase

> **IB Data Booklet references:** $x = x_0 \sin(\omega t)$, $x = x_0 \cos(\omega t)$, $v = \omega\sqrt{x_0^2 - x^2}$, $a = -\omega^2 x$, $\omega = \frac{2\pi}{T}$

## What You'll Learn
- The **displacement equation** for SHM: $x = x_0\sin(\omega t)$ and $x = x_0\cos(\omega t)$ — when to use which
- The **velocity equation**: $v = \omega\sqrt{x_0^2 - x^2}$ and $v = \omega x_0\cos(\omega t)$
- How $x$, $v$, and $a$ graphs relate to each other and to the circular motion picture
- What **phase** and **phase difference** mean, and how to calculate them
- How to extract all kinematic information from a given SHM equation

---

## 1. Displacement as a Function of Time: $x(t)$

### Where We Left Off

In Lesson 29, we established that SHM is the projection of uniform circular motion onto a straight line. A point P moves around a circle of radius $x_0$ (the amplitude) at constant angular speed $\omega$. The shadow of P on a line shows SHM.

Now we write the equation that tells us exactly where the shadow is at any time $t$.

### The General Displacement Equations

$$\boxed{x(t) = x_0 \sin(\omega t)} \quad \text{or} \quad \boxed{x(t) = x_0 \cos(\omega t)}$$

Both equations describe SHM. The only difference is **where the object is at $t = 0$**.

| Equation | Position at $t = 0$ | Initial motion |
|----------|-------------------|----------------|
| $x = x_0 \sin(\omega t)$ | $x = 0$ (equilibrium) | Moving toward positive $x$ |
| $x = x_0 \cos(\omega t)$ | $x = +x_0$ (maximum positive) | Momentarily at rest |

Think of it this way: you can start your stopwatch at any moment during the oscillation. Where you start the stopwatch determines which function describes the motion.

### The Most General Form: Phase Constant $\phi$

In the most general case, the oscillator could be anywhere when you start the clock:

$$\boxed{x(t) = x_0 \sin(\omega t + \phi)}$$

The quantity $\phi$ (Greek letter phi) is called the **phase constant** or **initial phase**. It tells you the position at $t = 0$:

- If $\phi = 0$: $x(0) = x_0\sin(0) = 0$, starting at equilibrium, moving positive.
- If $\phi = \pi/2$: $x(0) = x_0\sin(\pi/2) = x_0$, starting at max positive (same as cosine).
- If $\phi = \pi$: $x(0) = x_0\sin(\pi) = 0$, starting at equilibrium, moving negative.
- If $\phi = 3\pi/2$: $x(0) = x_0\sin(3\pi/2) = -x_0$, starting at max negative.

The argument of the sine (or cosine) — the whole thing inside the parentheses, $\omega t + \phi$ — is called the **phase** of the motion at time $t$.

---

## 2. Velocity in SHM

### Two Forms of the Velocity Equation

The velocity at any instant can be written in two ways. The first relates velocity to **displacement**:

$$\boxed{v = \pm\,\omega\sqrt{x_0^2 - x^2}}$$

The $\pm$ sign means: velocity can be positive (moving in the $+x$ direction) or negative (moving in the $-x$ direction). The magnitude of the velocity depends only on how far the object is from equilibrium.

The second form relates velocity to **time** (assuming $x = x_0\sin(\omega t)$):

$$\boxed{v = \omega x_0 \cos(\omega t)}$$

Key observations:

- **At equilibrium** ($x = 0$): $v = \pm\,\omega x_0$, the maximum speed. All energy is kinetic.
- **At the extremes** ($x = \pm x_0$): $v = 0$. The object turns around.
- **The speed is symmetric**: the object has the same speed at $x = +d$ and $x = -d$.

### Where Does $v = \omega\sqrt{x_0^2 - x^2}$ Come From?

From the circular motion picture: the point on the circle has constant tangential speed $v_{\text{tan}} = \omega x_0$. The shadow's speed is the component of this velocity along the projection line. At an angle $\theta = \omega t$, the tangential velocity makes an angle $\theta$ with the vertical (depending on your projection). The component along the projection line is $v_{\text{tan}}\cos(\omega t) = \omega x_0\cos(\omega t)$.

Meanwhile, the position of the shadow is $x = x_0\sin(\omega t)$. Using $\sin^2\theta + \cos^2\theta = 1$:

$$\cos(\omega t) = \sqrt{1 - \sin^2(\omega t)} = \sqrt{1 - (x/x_0)^2}$$

Substituting into $v$:

$$v = \omega x_0\sqrt{1 - (x/x_0)^2} = \omega\sqrt{x_0^2 - x^2}$$

### Maximum Speed

$$\boxed{v_{\max} = \omega x_0}$$

This is the speed at equilibrium. It's also the tangential speed of the equivalent circular motion.

---

## 3. Acceleration in SHM

The acceleration is always:

$$\boxed{a = -\omega^2 x}$$

This is the **defining equation** of SHM. We discussed it in Lesson 29, but now let's integrate it with our understanding of $x(t)$ and $v(t)$.

If $x = x_0\sin(\omega t)$, then differentiating twice (or using the circular motion picture):

$$\boxed{a = -\omega^2 x_0 \sin(\omega t)}$$

Key observations:
- **At equilibrium** ($x = 0$): $a = 0$. No net force.
- **At the extremes** ($x = \pm x_0$): $a = \mp\,\omega^2 x_0$, maximum magnitude.
- **Maximum acceleration**: $a_{\max} = \omega^2 x_0$.

### The Direction of Acceleration

The acceleration always points toward equilibrium. If the object is on the right side ($x > 0$), it accelerates left. If on the left ($x < 0$), it accelerates right. This is why $a$ is negative when $x$ is positive, and positive when $x$ is negative.

---

## 4. The Graphs of SHM — Seeing the Relationships

### Displacement vs. Time: $x(t)$

The $x$–$t$ graph for SHM starting at $x = 0$ (using sine) is a smooth wave that oscillates between $+x_0$ and $-x_0$. One complete cycle ($0$ to $T$) corresponds to the phase going from $0$ to $2\pi$.

The slope of the $x$–$t$ graph at any point IS the velocity at that instant. Steepest slope = fastest speed (at equilibrium). Zero slope = zero speed (at extremes).

### Velocity vs. Time: $v(t)$

The $v$–$t$ graph is also sinusoidal, but it is **shifted** relative to $x(t)$. When $x$ is at a maximum, $v$ is at zero. When $x$ crosses zero, $v$ is at its maximum (positive or negative).

Specifically, if $x = x_0\sin(\omega t)$, then $v = \omega x_0\cos(\omega t)$. The velocity graph leads the displacement graph by a quarter cycle ($T/4$, or $\pi/2$ radians).

### Acceleration vs. Time: $a(t)$

The $a$–$t$ graph is the **negative** of the $x$–$t$ graph, scaled by $\omega^2$. If $x = x_0\sin(\omega t)$, then $a = -\omega^2 x_0\sin(\omega t) = -\omega^2 x$.

The acceleration is always opposite in sign to the displacement. When $x$ is most positive, $a$ is most negative.

### The Three Graphs Side by Side

| Time $t$ | $x$ (displacement) | $v$ (velocity) | $a$ (acceleration) |
|----------|-------------------|----------------|-------------------|
| 0 | 0 | $+\omega x_0$ (max) | 0 |
| $T/4$ | $+x_0$ (max) | 0 | $-\omega^2 x_0$ (max negative) |
| $T/2$ | 0 | $-\omega x_0$ (max negative) | 0 |
| $3T/4$ | $-x_0$ (max negative) | 0 | $+\omega^2 x_0$ (max) |
| $T$ | 0 | $+\omega x_0$ (max) | 0 |

### How to Read the Graphs

If you are given one graph, you can construct the others:
- $v$ is the slope (gradient) of $x$.
- $a$ is the slope (gradient) of $v$.
- $a$ is proportional to $-x$.

**Common Misconception:** Many students look at the $x$–$t$ graph and think the velocity is zero wherever the displacement is zero. That is backwards. Velocity is the slope of the $x$–$t$ graph. Where $x$ crosses zero, the slope is steepest → velocity is maximum.

---

## 5. Phase and Phase Difference

### What Is Phase?

The **phase** of an oscillator at any moment is the quantity $\omega t + \phi$ — the argument of the sine or cosine. It is measured in radians. The phase tells you exactly where in the cycle the oscillator is.

Think of phase as an angle on the reference circle. A phase of $0$ means the reference point is at angle $0$. A phase of $\pi/2$ means it's at $90^\circ$. A phase of $2\pi$ means one full cycle is complete.

### What Is Phase Difference?

When you have **two oscillators** (or two points on a wave), the **phase difference** tells you how much one lags behind or leads the other in its cycle.

$$\boxed{\Delta\phi = \phi_2 - \phi_1}$$

Phase difference is measured in radians (or degrees). Key values:

| $\Delta\phi$ | Meaning |
|-------------|---------|
| 0 | **In phase** — both reach max at the same time, both cross equilibrium together |
| $\pi/2$ ($90^\circ$) | One reaches max a quarter-cycle after the other |
| $\pi$ ($180^\circ$) | **Out of phase / antiphase** — one is at $+x_0$ when the other is at $-x_0$ |
| $2\pi$ ($360^\circ$) | Back in phase — equivalent to zero |

### Relating Phase Difference to Time Difference

If two oscillators have the same period $T$ and a phase difference of $\Delta\phi$, the time difference between corresponding events (e.g., both passing through equilibrium in the same direction) is:

$$\Delta t = \frac{\Delta\phi}{2\pi}\,T = \frac{\Delta\phi}{\omega}$$

For example, if oscillator B lags oscillator A by $\pi/2$ radians (a quarter cycle), then B does everything a time $T/4$ later than A does.

### Common Misconception

**Many students think "in phase" and "out of phase" are the only two options.** There is a continuous range of phase differences. Two oscillators can be $\pi/3$ out of phase, or any other value. "In phase" just means $\Delta\phi = 0, 2\pi, 4\pi, \ldots$ and "antiphase" means $\Delta\phi = \pi, 3\pi, 5\pi, \ldots$.

**Many students confuse phase difference with path difference.** Phase difference describes timing; path difference describes spatial separation. They are related for waves (we will see this later), but for simple oscillators, phase is purely about timing.

---

## Worked Examples

### Example 1: Reading an SHM Equation

**Problem:** An oscillator's displacement is given by $x = 0.15\cos(3t + \pi/4)$, with $x$ in meters and $t$ in seconds. Find: (a) the amplitude, (b) the angular frequency, (c) the period, (d) the phase constant, (e) the displacement at $t = 0$.

**Approach:** Match to standard form $x = x_0\cos(\omega t + \phi)$.

**Solution:**

(a) Amplitude: $x_0 = 0.15\ \mathrm{m}$.

(b) Angular frequency: $\omega = 3.0\ \mathrm{rad/s}$.

(c) Period: $T = 2\pi/\omega = 2\pi/3 \approx 2.09\ \mathrm{s}$.

(d) Phase constant: $\phi = \pi/4$ rad ($45^\circ$).

(e) At $t = 0$: $x = 0.15\cos(\pi/4) = 0.15 \times \frac{\sqrt{2}}{2} \approx 0.106\ \mathrm{m}$.

**Why this makes sense:** The oscillator starts partway out from equilibrium (not at max and not at zero), which is what a non-zero phase constant does.

---

### Example 2: Finding Velocity at a Given Position

**Problem:** An oscillator has amplitude 0.200 m and period 0.500 s. Find its speed when it is 0.100 m from equilibrium.

**Approach:** Use $v = \omega\sqrt{x_0^2 - x^2}$.

**Solution:**

First find $\omega$: $\omega = 2\pi/T = 2\pi/0.500 = 4\pi\ \mathrm{rad/s}$.

Now $|v| = \omega\sqrt{x_0^2 - x^2} = 4\pi\sqrt{(0.200)^2 - (0.100)^2}$
$= 4\pi\sqrt{0.0400 - 0.0100} = 4\pi\sqrt{0.0300}$
$= 4\pi\sqrt{3/100} = (4\pi/10)\sqrt{3} = 0.4\pi\sqrt{3} \approx 2.18\ \mathrm{m/s}$.

**Why this makes sense:** At half the amplitude, the speed is not half the maximum — it's higher. $v_{\max} = \omega x_0 = 4\pi \times 0.200 = 0.8\pi \approx 2.51\ \mathrm{m/s}$. Our answer of $2.18\ \mathrm{m/s}$ is about $87\%$ of max, which is correct — at half amplitude, $v/v_{\max} = \sqrt{1 - (1/2)^2} = \sqrt{3/4} \approx 86.6\%$.

**Common pitfall:** Many students assume speed varies linearly with displacement (half the displacement = half the speed). It does not. The relationship is $v = \omega\sqrt{x_0^2 - x^2}$, which is a quarter-circle in the $x$–$v$ plane.

---

### Example 3: Maximum Values from Graphs

**Problem:** The displacement–time graph for an oscillator shows that it takes 0.40 s to go from equilibrium to maximum displacement (0.080 m). Find: (a) the period, (b) the frequency, (c) the angular frequency, (d) the maximum speed, (e) the maximum acceleration.

**Approach:** Going from equilibrium to max is one-quarter of a cycle. Amplitude is read directly.

**Solution:**

(a) $T/4 = 0.40\ \mathrm{s}$, so $T = 1.60\ \mathrm{s}$.

(b) $f = 1/T = 1/1.60 = 0.625\ \mathrm{Hz}$.

(c) $\omega = 2\pi f = 2\pi \times 0.625 = 1.25\pi \approx 3.93\ \mathrm{rad/s}$.

(d) $v_{\max} = \omega x_0 = 1.25\pi \times 0.080 = 0.10\pi \approx 0.314\ \mathrm{m/s}$.

(e) $a_{\max} = \omega^2 x_0 = (1.25\pi)^2 \times 0.080 = 1.5625\pi^2 \times 0.080 = 0.125\pi^2 \approx 1.23\ \mathrm{m/s^2}$.

---

### Example 4: Phase Difference

**Problem:** Two identical pendulums oscillate with the same period but are started at different times. Pendulum A is at maximum positive displacement when $t = 0$. Pendulum B is at equilibrium moving positive when $t = 0$. Find the phase difference between them, and state whether B leads or lags A.

**Approach:** Write the equations for both and compare the phase constants.

**Solution:**

Pendulum A: $x_A = x_0\cos(\omega t)$ (max positive at $t = 0$). Phase = $\omega t$.
Pendulum B: $x_B = x_0\sin(\omega t)$ (equilibrium, moving positive at $t = 0$). Phase = $\omega t$.

But wait — $\sin(\omega t) = \cos(\omega t - \pi/2)$. So we can write $x_B = x_0\cos(\omega t - \pi/2)$.

Comparing: $\phi_A = 0$, $\phi_B = -\pi/2$ (or equivalently $\phi_B = 3\pi/2$).

Phase difference: $\Delta\phi = \phi_A - \phi_B = 0 - (-\pi/2) = +\pi/2$.

A leads B by $\pi/2$ radians. Equivalently, B lags A by $\pi/2$ radians. B reaches any given point a quarter-cycle after A does.

**Why this makes sense:** At $t = 0$, A is already at the top, while B is just starting upward from the bottom. A is ahead.

---

### Example 5: Extracting $\omega$ and $x_0$ from $v_{\max}$ and $a_{\max}$

**Problem:** An object in SHM has a maximum speed of 3.0 m/s and a maximum acceleration of 18 m/s². Determine the amplitude and the period.

**Approach:** Use $v_{\max} = \omega x_0$ and $a_{\max} = \omega^2 x_0$. Divide to get $\omega$, then solve for $x_0$.

**Solution:**

Dividing: $a_{\max} / v_{\max} = \omega^2 x_0 / (\omega x_0) = \omega$.

$\omega = 18 / 3.0 = 6.0\ \mathrm{rad/s}$.

$T = 2\pi/\omega = 2\pi/6.0 = \pi/3 \approx 1.05\ \mathrm{s}$.

$x_0 = v_{\max} / \omega = 3.0 / 6.0 = 0.50\ \mathrm{m}$.

**Why this makes sense:** A half-meter amplitude with a period of about 1 second means the object moves at an average speed of roughly $4x_0/T = 2.0/1.05 \approx 1.9\ \mathrm{m/s}$, and a peak speed of $3.0\ \mathrm{m/s}$ — reasonable for this size of oscillation.

---

## Practice Problems

### Problem 1
A particle in SHM has an amplitude of 6.0 cm and a frequency of 4.0 Hz. At $t = 0$, the particle is at $x = 0$ and moving in the positive direction.
(a) Write the equation for displacement as a function of time.
(b) Find the velocity at $t = 0.10$ s.
(c) Find the acceleration when the displacement is $-3.0$ cm.
(d) How long does it take for the particle to go from $x = 0$ to $x = 3.0$ cm?

### Problem 2
An oscillator has the velocity–time equation $v = 2.0\cos(5.0t)$, with $v$ in m/s and $t$ in s. Assuming $x = 0$ when $t = 0$, find:
(a) The amplitude.
(b) The displacement as a function of time $x(t)$.
(c) The maximum acceleration.
(d) The acceleration at $t = \pi/15$ s.

### Problem 3
The acceleration of a particle in SHM is given by $a = -36x$, with $x$ in meters. If the particle has a speed of $1.20\ \mathrm{m/s}$ when it passes through equilibrium, find:
(a) The angular frequency.
(b) The amplitude.
(c) The speed when $x = 10.0$ cm.
(d) The acceleration at the same position.

### Problem 4
Two identical mass-spring systems oscillate with the same amplitude of 5.0 cm and period of 0.80 s. System A is at $x = +5.0$ cm at $t = 0$. System B is at $x = 0$ moving negative at $t = 0$.
(a) Write $x(t)$ for each system.
(b) What is the phase difference between them?
(c) At what time after $t = 0$ do they both have the same displacement for the first time?

### Problem 5
Below is a description of an oscillator's motion at four instants during one cycle. For each instant, state the displacement $x$ (in terms of $x_0$), velocity $v$ (in terms of $v_{\max}$), and acceleration $a$ (in terms of $a_{\max}$):
(a) $\omega t = \pi/3$
(b) $\omega t = 2\pi/3$
(c) $\omega t = \pi$
(d) $\omega t = 5\pi/3$

Assume $x = x_0\sin(\omega t)$.

### Problem 6 *(IB Exam Style)*
A particle undergoes SHM with displacement given by $x = 0.080\sin(2.5\pi t)$, where $x$ is in meters and $t$ is in seconds.

(a) Determine the amplitude and period of the motion. [2 marks]
(b) Calculate the maximum speed of the particle. [2 marks]
(c) On graph paper, sketch the variation with time $t$ (from $t = 0$ to $t = 0.80$ s) of:
 (i) the displacement $x$
 (ii) the velocity $v$
Label the axes with appropriate values. [4 marks]
(d) Using your graphs or otherwise, determine the phase difference between the displacement and the velocity. [1 mark]

---

## Answers

### Answer 1
(a) $x_0 = 0.060\ \mathrm{m}$, $\omega = 2\pi f = 8\pi\ \mathrm{rad/s}$. Starting at equilibrium moving positive: $x = 0.060\sin(8\pi t)$.

(b) $v = \omega x_0\cos(\omega t) = 8\pi \times 0.060 \times \cos(8\pi \times 0.10) = 0.48\pi\cos(0.8\pi)$.
$\cos(0.8\pi) = \cos(144^\circ) = -\cos(36^\circ) \approx -0.809$.
$v \approx 0.48\pi \times (-0.809) \approx -1.22\ \mathrm{m/s}$.

(c) $a = -\omega^2 x = -(8\pi)^2 \times (-0.030) = 64\pi^2 \times 0.030 = 1.92\pi^2 \approx 18.9\ \mathrm{m/s^2}$ (positive, toward equilibrium since $x$ is negative).

(d) $x = 0.060\sin(8\pi t) = 0.030$ → $\sin(8\pi t) = 0.5$ → $8\pi t = \pi/6$ → $t = 1/48 \approx 0.0208\ \mathrm{s}$.

---

### Answer 2
(a) $v = \omega x_0\cos(\omega t)$. Given $v = 2.0\cos(5.0t)$, so $\omega = 5.0\ \mathrm{rad/s}$, and $\omega x_0 = 2.0$, so $x_0 = 2.0/5.0 = 0.40\ \mathrm{m}$.

(b) Since $x = 0$ at $t = 0$ and $v$ is positive ($\cos(0) = +1$), use sine: $x = 0.40\sin(5.0t)$.

(c) $a_{\max} = \omega^2 x_0 = 25 \times 0.40 = 10\ \mathrm{m/s^2}$.

(d) $t = \pi/15$, so $\omega t = 5.0 \times \pi/15 = \pi/3$. $x = 0.40\sin(\pi/3) = 0.40 \times \sqrt{3}/2 = 0.20\sqrt{3}$.
$a = -\omega^2 x = -25 \times 0.20\sqrt{3} = -5.0\sqrt{3} \approx -8.66\ \mathrm{m/s^2}$.

---

### Answer 3
(a) $a = -36x$, so $\omega^2 = 36$, $\omega = 6.0\ \mathrm{rad/s}$.

(b) At equilibrium, $v = v_{\max} = \omega x_0$, so $x_0 = 1.20/6.0 = 0.20\ \mathrm{m} = 20\ \mathrm{cm}$.

(c) $|v| = \omega\sqrt{x_0^2 - x^2} = 6.0\sqrt{(0.20)^2 - (0.10)^2} = 6.0\sqrt{0.04 - 0.01} = 6.0\sqrt{0.03} = 6.0 \times 0.1732 \approx 1.04\ \mathrm{m/s}$.

(d) $a = -\omega^2 x = -36 \times 0.10 = -3.6\ \mathrm{m/s^2}$.

---

### Answer 4
$\omega = 2\pi/T = 2\pi/0.80 = 2.5\pi\ \mathrm{rad/s}$.

(a) A: starts at $+x_0$ → $x_A = 0.050\cos(2.5\pi t)$.
B: starts at $0$ moving negative → $x_B = -0.050\sin(2.5\pi t) = 0.050\sin(2.5\pi t + \pi)$.

(b) $x_A = 0.050\cos(2.5\pi t) = 0.050\sin(2.5\pi t + \pi/2)$.
$x_B = 0.050\sin(2.5\pi t + \pi) = -0.050\sin(2.5\pi t)$.
Phase difference: $\Delta\phi = (\pi/2) - \pi = -\pi/2$. B lags A by $\pi/2$ rad, or A leads B by $\pi/2$.

(c) Set $x_A = x_B$: $0.050\cos(2.5\pi t) = -0.050\sin(2.5\pi t)$ → $\cos(2.5\pi t) = -\sin(2.5\pi t)$→ $\tan(2.5\pi t) = -1$ → $2.5\pi t = 3\pi/4$ (first positive solution in second quadrant) → $t = (3\pi/4)/(2.5\pi) = 3/10 = 0.30\ \mathrm{s}$.

---

### Answer 5
(a) $\omega t = \pi/3$: $x = x_0\sin(\pi/3) = x_0\sqrt{3}/2 \approx 0.866x_0$.
$v = v_{\max}\cos(\pi/3) = v_{\max}/2$.
$a = -a_{\max}\sin(\pi/3) = -a_{\max}\sqrt{3}/2 \approx -0.866a_{\max}$.

(b) $\omega t = 2\pi/3$: $x = x_0\sin(2\pi/3) = x_0\sqrt{3}/2 \approx 0.866x_0$.
$v = v_{\max}\cos(2\pi/3) = -v_{\max}/2$.
$a = -a_{\max}\sin(2\pi/3) = -0.866a_{\max}$.

(c) $\omega t = \pi$: $x = x_0\sin(\pi) = 0$.
$v = v_{\max}\cos(\pi) = -v_{\max}$.
$a = -a_{\max}\sin(\pi) = 0$.

(d) $\omega t = 5\pi/3$: $x = x_0\sin(5\pi/3) = -x_0\sqrt{3}/2$.
$v = v_{\max}\cos(5\pi/3) = v_{\max}/2$.
$a = -a_{\max}\sin(5\pi/3) = a_{\max}\sqrt{3}/2$.

---

### Answer 6 (IB Exam Style)

(a) $x_0 = 0.080\ \mathrm{m}$, $\omega = 2.5\pi\ \mathrm{rad/s}$, $T = 2\pi/\omega = 2\pi/(2.5\pi) = 0.80\ \mathrm{s}$.
**[2 marks — 1 for amplitude, 1 for period]**

(b) $v_{\max} = \omega x_0 = 2.5\pi \times 0.080 = 0.20\pi \approx 0.628\ \mathrm{m/s}$.
**[2 marks — 1 for formula, 1 for correct answer]**

(c) The $x$–$t$ graph is a sine wave from $0$ to $0.80$ s (one full period), amplitude $0.080$ m. It crosses zero at $0, 0.40, 0.80$ s, peaks at $+0.080$ m at $0.20$ s, and troughs at $-0.080$ m at $0.60$ s.

The $v$–$t$ graph is a cosine wave, amplitude $0.20\pi \approx 0.628$ m/s. It peaks at $+0.628$ m/s at $t = 0$, crosses zero at $t = 0.20$ s, troughs at $-0.628$ m/s at $t = 0.40$ s, crosses zero at $t = 0.60$ s, peaks again at $t = 0.80$ s.
**[4 marks — 1 for correct shape of x, 1 for correct values on x, 1 for correct shape of v, 1 for correct values on v]**

(d) Phase difference: The velocity leads the displacement by $\pi/2$ radians (quarter cycle). This is visible from the graphs: $v$ reaches its maximum a quarter-cycle before $x$ reaches its maximum.
**[1 mark]**

---

## Key Takeaways

1. **Displacement**: $x = x_0\sin(\omega t)$ (start at equilibrium) or $x = x_0\cos(\omega t)$ (start at max). The most general form includes a phase constant: $x = x_0\sin(\omega t + \phi)$.

2. **Velocity**: $v = \omega\sqrt{x_0^2 - x^2}$ relates $v$ to $x$; $v_{\max} = \omega x_0$ at equilibrium. The velocity graph leads the displacement graph by $\pi/2$ rad.

3. **Acceleration**: $a = -\omega^2 x$ always. $a_{\max} = \omega^2 x_0$ at the extremes. $a = 0$ at equilibrium. The acceleration is always opposite to displacement.

4. **Phase** describes where an oscillator is in its cycle. **Phase difference** compares two oscillators. In phase: $\Delta\phi = 0, 2\pi,\ldots$ Antiphase: $\Delta\phi = \pi, 3\pi,\ldots$

5. The **three graphs** ($x$ vs $t$, $v$ vs $t$, $a$ vs $t$) tell the same story from different perspectives. $v$ is the slope of $x$; $a$ is the slope of $v$; $a \propto -x$.
