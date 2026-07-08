# Lesson 29: Simple Harmonic Motion I — Introducing Oscillations

> **IB Data Booklet references:** $a = -\omega^2 x$, $T = \frac{1}{f}$, $\omega = \frac{2\pi}{T} = 2\pi f$

## What You'll Learn
- What an **oscillation** is and what makes motion **periodic**
- The meaning of **equilibrium position**, **amplitude**, **period**, **frequency**, and **angular frequency**
- The definition of **Simple Harmonic Motion (SHM)** and its defining equation: $a = -\omega^2 x$
- How SHM connects to uniform circular motion

---

## 1. What Is an Oscillation?

### What an Oscillation Is — Starting from Nothing

An **oscillation** is a motion that repeats itself over and over, going back and forth through a central position. Imagine a child on a playground swing. You give her one push, and she swings forward, slows down, stops for an instant at the highest point, then swings backward, passes through the bottom, slows down on the other side, stops, and then swings forward again. That entire back-and-forth journey — and the fact that she repeats it over and over — is an **oscillation**.

Here are some oscillations you have experienced:

- A **guitar string** after you pluck it: it vibrates back and forth rapidly, producing sound.
- Your **heartbeat**: it contracts and relaxes in a repeating rhythm.
- A **cork bobbing on water** after a ripple passes: it moves up and down around its original floating level.
- The **piston in a car engine**: it moves up and down inside the cylinder thousands of times per minute.
- A **tuning fork** when struck: its prongs move inward and outward at a specific frequency.

All of these have one thing in common: something moves away from a central position, returns, overshoots to the other side, and keeps repeating. That central position is called the **equilibrium position**.

### The Equilibrium Position — Your "Home Base"

The **equilibrium position** is where the object would sit if it were not moving at all — the position where all forces on it cancel out. For the swing, equilibrium is hanging straight down. For the cork on water, equilibrium is where the cork naturally floats. For a mass hanging on a spring, equilibrium is where the spring's upward force exactly balances the weight.

When an oscillating object passes through equilibrium, it is moving at its fastest. When it is farthest from equilibrium (at the extreme ends of its motion), it momentarily stops before turning around.

### Restoring Force — What Brings You Back

For any oscillation to happen, there must be a **restoring force** — a force that always points back toward the equilibrium position. The further you are from equilibrium, the larger this force becomes (at least for SHM).

Think about a swing. When the swing is displaced to the side, gravity pulls it back toward the bottom. The larger the angle, the stronger the component of gravity that pushes it back. This is the restoring force. Without it, the swing would never come back — it would just keep going.

### Why This Matters

Oscillations are everywhere in physics. Sound is oscillating air pressure. Light is oscillating electric and magnetic fields. Radio signals carry information on oscillating electromagnetic waves. The atoms in a solid vibrate around their lattice positions. Planets orbit stars, and while that's not SHM, the mathematics of periodic motion you learn here becomes the foundation for understanding waves, alternating current electricity, quantum mechanics, and more.

---

## 2. Describing Oscillations — The Basic Vocabulary

Before we can write equations, we need words to describe what we see. Imagine watching that child on the swing. How would you describe her motion to someone who cannot see it?

### Displacement $x$

**Displacement** is how far the oscillating object is from the equilibrium position at any instant. We use the letter $x$ (in meters, m). Displacement can be positive or negative, depending on which side of equilibrium the object is on.

- $x = 0$ means the object is exactly at equilibrium.
- $x = +A$ means it is at the maximum displacement on the side we call positive.
- $x = -A$ means it is at the maximum displacement on the negative side.

### Amplitude $A$

The **amplitude** is the maximum displacement from equilibrium. It is always a positive number. If the swing goes 1.5 meters to the right and 1.5 meters to the left, the amplitude is 1.5 m. The amplitude tells you how "big" the oscillation is — how far from center the motion reaches.

The symbol is $A$ (or sometimes $x_0$), and it is measured in meters (m).

Amplitude does not change over time in an ideal (undamped) oscillator. In real life, friction slowly reduces the amplitude, which is why a swing eventually stops if you don't keep pumping it.

### Period $T$

The **period** is the time it takes to complete one full oscillation — one complete back-and-forth cycle. Start the stopwatch when the swing is at its rightmost point. Stop it when the swing returns to the rightmost point, having gone all the way to the left and back. That time is the period.

The symbol is $T$, and it is measured in seconds (s).

A pendulum clock uses a pendulum with a period of exactly 2 seconds (1 second each way). The second hand ticks once per swing.

$$\boxed{T = \frac{1}{f}}$$

### Frequency $f$

The **frequency** is the number of complete oscillations per second. If a guitar string vibrates 440 times per second, its frequency is 440 Hz (Hertz). The symbol is $f$, and it is measured in Hertz (Hz), where $1\ \mathrm{Hz} = 1\ \mathrm{s}^{-1}$.

$$\boxed{f = \frac{1}{T}}$$

Period and frequency are inverses. A long period means low frequency (slow oscillation). A short period means high frequency (fast oscillation).

### Angular Frequency $\omega$

There is a third way to describe how fast something oscillates: **angular frequency**, symbol $\omega$ (the Greek letter omega). It is measured in radians per second ($\mathrm{rad\ s^{-1}}$).

Why radians? Because SHM is deeply connected to circular motion (we will explore this shortly). One full oscillation corresponds to the object going through $2\pi$ radians of the reference circle.

$$\boxed{\omega = \frac{2\pi}{T} = 2\pi f}$$

| Quantity | Symbol | SI Unit | Relationship |
|----------|--------|---------|--------------|
| Period | $T$ | seconds (s) | $T = 1/f = 2\pi/\omega$ |
| Frequency | $f$ | Hertz (Hz) | $f = 1/T = \omega/(2\pi)$ |
| Angular frequency | $\omega$ | rad/s | $\omega = 2\pi f = 2\pi/T$ |

### Common Misconception

**Many students confuse frequency $f$ with angular frequency $\omega$.** Frequency $f$ tells you cycles per second; angular frequency $\omega$ tells you radians per second. They differ by a factor of $2\pi$. For a 1 Hz oscillation (one cycle per second), $\omega = 2\pi \approx 6.28\ \mathrm{rad/s}$. Always check which one a problem is asking for. If you see $\omega$ in a formula like $\sin(\omega t)$, you need angular frequency, not plain frequency.

---

## 3. What Is Simple Harmonic Motion (SHM)?

### The Defining Equation

Not all oscillations are SHM. **Simple Harmonic Motion** is a special kind of oscillation where the acceleration is directly proportional to the displacement from equilibrium and always directed toward equilibrium.

Mathematically:

$$\boxed{a = -\omega^2 x}$$

Let's break this down piece by piece:

- $a$ is the acceleration at any instant (in $\mathrm{m/s^2}$).
- $x$ is the displacement at that instant (in m).
- $\omega^2$ is a positive constant (the square of the angular frequency).
- The **minus sign** is the most important part. It means: when $x$ is positive (object to the right), $a$ is negative (acceleration points left, toward equilibrium). When $x$ is negative (object to the left), $a$ is positive (acceleration points right, toward equilibrium). The acceleration always points toward $x = 0$.

### What This Equation Tells Us Physically

1. **At the extremes**: When $x = +A$ (maximum positive displacement), $a = -\omega^2 A$, the maximum acceleration toward equilibrium. The object is momentarily at rest but being pulled hardest.

2. **At equilibrium**: When $x = 0$, $a = 0$. There is no net force (for the mass-spring system, this is where the spring is at its natural length minus the static extension due to weight). The object passes through equilibrium at maximum speed.

3. **In between**: Acceleration grows linearly with displacement. Double the displacement, double the acceleration (in magnitude).

### The SHM Test — How to Recognize SHM

If you encounter a system and want to know whether it undergoes SHM, ask one question:

> Is the net force (or acceleration) proportional to displacement and directed toward equilibrium?

If the answer is yes, and you can write it in the form $a = -\omega^2 x$, then the motion is SHM. The value of $\omega^2$ tells you the angular frequency, and from that you can find the period: $T = 2\pi/\omega$.

For a **mass on a spring**, the force is $F = -kx$ (Hooke's Law), so $a = -(k/m)x$, giving $\omega^2 = k/m$ and $T = 2\pi\sqrt{m/k}$.

For a **simple pendulum** with small angles, the tangential acceleration is $a = -(g/L)x$ (where $x$ is arc length), giving $\omega^2 = g/L$ and $T = 2\pi\sqrt{L/g}$.

More on both of these in Lesson 32.

### Common Misconception

**Many students think any repeating motion is SHM.** A bouncing basketball is not SHM. A heartbeat is not SHM. SHM requires that the restoring force be proportional to displacement, not just that the motion repeats. Only a few idealized systems (mass-spring, simple pendulum at small angles, LC circuits) truly exhibit SHM.

**Many students think the minus sign in $a = -\omega^2 x$ is just a mathematical formality.** It is not. The minus sign is what makes the motion oscillatory. If the sign were positive ($a = +\omega^2 x$), the object would accelerate away from equilibrium faster and faster and never return. The minus sign encodes the restoring nature of the force.

---

## 4. SHM as a Projection of Circular Motion

### The Connection to the Circle

This is one of the most powerful ideas in SHM: **SHM is exactly the same as the projection of uniform circular motion onto a straight line.**

Imagine a point P moving around a circle of radius $A$ at a constant angular speed $\omega$. Now imagine shining a light from the side so that the shadow of P falls onto a screen. The shadow moves back and forth in a straight line. That back-and-forth motion of the shadow is precisely SHM.

Why does this help? Because everything you know about uniform circular motion can be translated into SHM:

- The radius of the circle becomes the **amplitude** $A$ of the SHM.
- The angular speed $\omega$ of the circular motion is exactly the **angular frequency** of the SHM.
- One full revolution ($2\pi$ radians) corresponds to one complete oscillation, so $T = 2\pi/\omega$, exactly as we wrote before.

### Deriving $x(t)$ from the Circle

At any time $t$, the point P has swept out an angle $\theta = \omega t$ (starting from the positive x-axis). The x-coordinate (or y-coordinate, depending on your projection direction) of the shadow is:

$$x(t) = A\cos(\omega t) \quad \text{or} \quad x(t) = A\sin(\omega t)$$

Both describe SHM. The choice between sine and cosine just depends on where you define $t = 0$:

- If the oscillator starts at maximum displacement ($x = +A$ at $t = 0$), use $x = A\cos(\omega t)$.
- If the oscillator starts at equilibrium moving in the positive direction ($x = 0$ at $t = 0$), use $x = A\sin(\omega t)$.

### Deriving $a = -\omega^2 x$ from the Circle

In uniform circular motion, the acceleration of the point P always points toward the center of the circle (centripetal acceleration) with magnitude $a_c = \omega^2 A$.

When we project this acceleration onto the line of SHM, the component along the direction of motion has magnitude $\omega^2 A \cos(\omega t) = \omega^2 x$, and it always points toward the center — which, in the projection, corresponds to pointing toward $x = 0$. This gives us:

$$a = -\omega^2 x$$

The minus sign falls out naturally from the geometry.

### Why This Matters

The circular motion analogy gives you intuition for everything:

- At the ends ($x = \pm A$), the circular point is moving tangentially (all velocity is perpendicular to the projection line), so the shadow appears momentarily stationary. Speed = 0.
- At the center ($x = 0$), the circular point is moving purely along the projection line, so the shadow moves at maximum speed. Speed = $\omega A$.
- The period comes from the time for one full circle: $T = 2\pi/\omega$.

---

## Worked Examples

### Example 1: Identifying SHM

**Problem:** A particle moves such that its acceleration is given by $a = -25x$, where $x$ is in meters and $a$ in $\mathrm{m/s^2}$. Determine whether the motion is SHM, and if so, find the angular frequency and period.

**Approach:** Compare the given equation to the SHM defining equation $a = -\omega^2 x$.

**Solution:**

The equation is $a = -25x$, which has the form $a = -(\text{constant}) \times x$. Since the acceleration is proportional to displacement and the minus sign ensures it points toward equilibrium, the motion is SHM.

Comparing $a = -25x$ to $a = -\omega^2 x$ gives $\omega^2 = 25$, so:

$$\omega = \sqrt{25} = 5.0\ \mathrm{rad/s}$$

The period is:

$$T = \frac{2\pi}{\omega} = \frac{2\pi}{5} = 0.4\pi \approx 1.26\ \mathrm{s}$$

**Why this makes sense:** The period of about 1.26 seconds means the particle completes roughly 0.8 oscillations per second. The angular frequency of 5 rad/s is less than $2\pi$, which means it takes more than 1 second for one cycle — consistent.

---

### Example 2: From Circular Motion to SHM

**Problem:** A point moves around a circle of radius 0.30 m at a constant speed, completing one revolution every 2.0 seconds. The shadow of the point projected onto a screen moves along a line. Find: (a) the amplitude of the SHM, (b) the angular frequency, (c) the maximum speed of the shadow.

**Approach:** The amplitude is the circle's radius. Angular frequency comes from the period. Maximum speed comes from $v_{\max} = \omega A$.

**Solution:**

(a) Amplitude = radius of the circle = $A = 0.30\ \mathrm{m}$.

(b) $T = 2.0\ \mathrm{s}$, so:
$$\omega = \frac{2\pi}{T} = \frac{2\pi}{2.0} = \pi \approx 3.14\ \mathrm{rad/s}$$

(c) The speed of the point on the circle is $v = \omega A$. This is the tangential speed. The shadow's speed ranges from $0$ at the extremes to $v_{\max} = \omega A$ at equilibrium:
$$v_{\max} = \omega A = \pi \times 0.30 = 0.30\pi \approx 0.94\ \mathrm{m/s}$$

**Why this makes sense:** The point on the circle moves at constant speed $0.94\ \mathrm{m/s}$, but its shadow only has this full speed when moving parallel to the projection line (at equilibrium). At the turning points, the shadow is momentarily still.

---

### Example 3: Reading SHM from an Equation

**Problem:** An oscillator has displacement $x = 0.050\sin(4.0t)$, with $x$ in meters and $t$ in seconds. Find: (a) the amplitude, (b) the angular frequency, (c) the frequency, (d) the period, (e) the maximum acceleration.

**Approach:** Match the given equation to the standard form $x = A\sin(\omega t)$.

**Solution:**

(a) Amplitude: $A = 0.050\ \mathrm{m} = 5.0\ \mathrm{cm}$.

(b) Angular frequency: $\omega = 4.0\ \mathrm{rad/s}$.

(c) Frequency: $f = \frac{\omega}{2\pi} = \frac{4.0}{2\pi} = \frac{2}{\pi} \approx 0.637\ \mathrm{Hz}$.

(d) Period: $T = \frac{1}{f} = \frac{\pi}{2} \approx 1.57\ \mathrm{s}$.

(e) Maximum acceleration: $a_{\max} = \omega^2 A = (4.0)^2 \times 0.050 = 16 \times 0.050 = 0.80\ \mathrm{m/s^2}$.

**Why this makes sense:** The acceleration magnitude at the extremes is $\omega^2 A$, which is the centripetal acceleration of the equivalent circular motion. Here, the equivalent circle has radius 5 cm and angular speed 4 rad/s.

---

### Example 4: Finding $\omega$ from Mass-Spring Data

**Problem:** A 0.200 kg mass attached to a spring oscillates horizontally on a frictionless surface. Measurements show that when the mass is displaced 0.10 m from equilibrium, the acceleration is $3.0\ \mathrm{m/s^2}$ toward equilibrium. Find: (a) the angular frequency, (b) the spring constant, (c) the period.

**Approach:** Use $a = -\omega^2 x$ to find $\omega$, then $k = m\omega^2$.

**Solution:**

(a) At $|x| = 0.10\ \mathrm{m}$, $|a| = 3.0\ \mathrm{m/s^2}$. From $|a| = \omega^2 |x|$:
$$\omega^2 = \frac{|a|}{|x|} = \frac{3.0}{0.10} = 30$$
$$\omega = \sqrt{30} \approx 5.48\ \mathrm{rad/s}$$

(b) For a mass-spring system, $\omega^2 = k/m$, so:
$$k = m\omega^2 = 0.200 \times 30 = 6.0\ \mathrm{N/m}$$

(c) $T = \frac{2\pi}{\omega} = \frac{2\pi}{\sqrt{30}} \approx 1.15\ \mathrm{s}$

**Why this makes sense:** A spring constant of 6.0 N/m is modest — it stretches about 3.3 cm under the weight of a 200 g mass. The period just over 1 second feels reasonable for a soft spring with a medium mass.

---

### Example 5: Comparing Two Oscillators

**Problem:** Oscillator A has twice the amplitude of oscillator B, but the same period. Both are SHM. At the instant when A is at $x = +A/2$, where is B if both started at $x = 0$ at $t = 0$ and move in the positive direction?

**Approach:** Both have equation $x = A\sin(\omega t)$. Find the time when A is at $A/2$, then evaluate B's position at that same time.

**Solution:**

For oscillator A: $x_A = A\sin(\omega t)$. At $x_A = A/2$, we have:
$$\sin(\omega t) = \frac{1}{2}$$
$$\omega t = \frac{\pi}{6} \text{ (taking the first occurrence, since it starts moving positive)}$$

At this same time, oscillator B (amplitude $A/2$):
$$x_B = \frac{A}{2}\sin(\omega t) = \frac{A}{2} \times \frac{1}{2} = \frac{A}{4}$$

**Why this makes sense:** At the moment A is halfway to its peak, B is also "halfway" to its (smaller) peak, so B's absolute displacement is one-quarter of A's amplitude.

---

## Practice Problems

### Problem 1
A particle undergoes SHM with an amplitude of 0.12 m and a frequency of 2.5 Hz. At $t = 0$, the particle is at $x = +0.12\ \mathrm{m}$.
(a) Find the angular frequency, period, and maximum acceleration.
(b) Write the equation for displacement as a function of time.
(c) At what displacement is the acceleration half of its maximum value?

### Problem 2
A mass on a spring oscillates with angular frequency $8.0\ \mathrm{rad/s}$. When the mass is at $x = 0.040\ \mathrm{m}$, its acceleration is measured to be $2.56\ \mathrm{m/s^2}$ toward equilibrium. Verify that this is consistent with SHM and calculate the amplitude if the maximum speed is $0.64\ \mathrm{m/s}$.

### Problem 3
A point moves on a circle of radius 0.25 m with a period of 3.0 s. A light projects its shadow onto a line.
(a) Find the angular frequency of the resulting SHM.
(b) What is the maximum speed of the shadow?
(c) At what displacement(s) is the shadow's speed equal to half its maximum speed?

### Problem 4
An object in SHM has a period of 0.50 s and an amplitude of 8.0 cm. Starting from equilibrium moving in the positive direction:
(a) How long does it take to reach $x = 4.0\ \mathrm{cm}$?
(b) What is the acceleration at this position?
(c) What is the displacement 0.10 s after starting?

### Problem 5
A student measures the acceleration of an oscillator at various displacements and obtains the following data:

| $x$ (cm) | 0 | 2.0 | 4.0 | 6.0 | 8.0 |
|----------|---|-----|-----|-----|-----|
| $a$ (m/s²) | 0 | 0.80 | 1.60 | 2.40 | 3.20 |

(a) Plot $a$ against $x$. Does this represent SHM? Explain.
(b) Determine the angular frequency.
(c) If the mass is 0.50 kg, find the effective spring constant.

### Problem 6 *(IB Exam Style)*
A particle moves in SHM along a straight line. Its maximum speed is $4.0\ \mathrm{m/s}$ and its maximum acceleration is $16\ \mathrm{m/s^2}$. 

(a) Calculate the angular frequency of the motion. [2 marks]
(b) Determine the amplitude of the motion. [2 marks]
(c) The particle has mass 0.25 kg. Calculate the maximum kinetic energy of the particle. [2 marks]
(d) On a single set of axes, sketch the variation with displacement $x$ of (i) the kinetic energy and (ii) the potential energy of the particle over one full oscillation from $x = -A$ to $x = +A$. Label key values. [3 marks]

---

## Answers

### Answer 1
(a) $\omega = 2\pi f = 2\pi(2.5) = 5\pi \approx 15.7\ \mathrm{rad/s}$.
$T = 1/f = 1/2.5 = 0.40\ \mathrm{s}$.
$a_{\max} = \omega^2 A = (5\pi)^2 \times 0.12 = 25\pi^2 \times 0.12 = 3\pi^2 \approx 29.6\ \mathrm{m/s^2}$.

(b) Starting at $x = +A$ at $t = 0$ means we use cosine: $x(t) = 0.12\cos(5\pi t)$.

(c) $a = -\omega^2 x$. Half of maximum: $|a| = \frac{1}{2}\omega^2 A = \omega^2 |x|$. So $|x| = \frac{1}{2}A = 0.060\ \mathrm{m}$. At $x = \pm 0.060\ \mathrm{m}$, the acceleration has half its maximum magnitude. 

**Common pitfall:** Some students think "half maximum acceleration" means "half the distance." That's only true for SHM because $a \propto x$. In general, check the proportionality.

---

### Answer 2
Given $a = -2.56\ \mathrm{m/s^2}$ when $x = 0.040\ \mathrm{m}$. The ratio $|a|/|x| = 2.56/0.040 = 64$. This equals $\omega^2$, and indeed $8.0^2 = 64$. The motion is consistent with SHM because $a \propto x$ with the correct constant and direction.

$v_{\max} = \omega A$, so $A = v_{\max}/\omega = 0.64/8.0 = 0.080\ \mathrm{m} = 8.0\ \mathrm{cm}$.

---

### Answer 3
(a) $\omega = 2\pi/T = 2\pi/3.0 = 2\pi/3 \approx 2.09\ \mathrm{rad/s}$.

(b) $v_{\max} = \omega A = (2\pi/3) \times 0.25 = \pi/6 \approx 0.524\ \mathrm{m/s}$.

(c) When $v = \frac{1}{2}v_{\max} = \frac{1}{2}\omega A$. In SHM, $v = \omega\sqrt{A^2 - x^2}$. Setting $\omega\sqrt{A^2 - x^2} = \frac{1}{2}\omega A$, we get $\sqrt{A^2 - x^2} = A/2$, so $A^2 - x^2 = A^2/4$, giving $x^2 = \frac{3}{4}A^2$, so $x = \pm \frac{\sqrt{3}}{2}A = \pm \frac{\sqrt{3}}{2} \times 0.25 \approx \pm 0.217\ \mathrm{m}$.

---

### Answer 4
(a) $\omega = 2\pi/T = 2\pi/0.50 = 4\pi\ \mathrm{rad/s}$. Starting from $x = 0$ moving positive: $x = A\sin(\omega t) = 0.080\sin(4\pi t)$. Set $x = 0.040$:
$0.040 = 0.080\sin(4\pi t)$ → $\sin(4\pi t) = 0.5$ → $4\pi t = \pi/6$ (first positive crossing) → $t = 1/24 \approx 0.0417\ \mathrm{s}$.

(b) At $x = 0.040\ \mathrm{m}$: $a = -\omega^2 x = -(4\pi)^2 \times 0.040 = -16\pi^2 \times 0.040 = -0.64\pi^2 \approx -6.32\ \mathrm{m/s^2}$.

(c) At $t = 0.10\ \mathrm{s}$: $x = 0.080\sin(4\pi \times 0.10) = 0.080\sin(0.4\pi) = 0.080 \times \sin(72^\circ) = 0.080 \times 0.951 \approx 0.076\ \mathrm{m}$. 

**Common pitfall:** Make sure your calculator is in radian mode. $4\pi \times 0.10 = 0.4\pi$ radians, not degrees.

---

### Answer 5
(a) Plotting $a$ vs $x$ yields a straight line through the origin with a negative slope (since acceleration points opposite to displacement). This is exactly the signature of SHM: $a = -(\text{constant}) \times x$. The data confirms SHM.

(b) Slope = $\Delta a / \Delta x$. From $x = 0.020\ \mathrm{m}$ to $x = 0.080\ \mathrm{m}$, $\Delta a = 3.20 - 0.80 = 2.40\ \mathrm{m/s^2}$, $\Delta x = 0.060\ \mathrm{m}$. Slope = $2.40/0.060 = 40$. But note: $a = -\omega^2 x$, so the magnitude of the slope is $\omega^2$. Thus $\omega^2 = 40$, $\omega = \sqrt{40} = 2\sqrt{10} \approx 6.32\ \mathrm{rad/s}$.

(c) $k = m\omega^2 = 0.50 \times 40 = 20\ \mathrm{N/m}$.

---

### Answer 6 (IB Exam Style)

(a) $v_{\max} = \omega A$ and $a_{\max} = \omega^2 A$. Dividing: $a_{\max}/v_{\max} = \omega^2 A / (\omega A) = \omega$. So $\omega = 16/4.0 = 4.0\ \mathrm{rad/s}$. 
**[2 marks — 1 for equation, 1 for correct answer]**

(b) $A = v_{\max}/\omega = 4.0/4.0 = 1.0\ \mathrm{m}$.
**[2 marks — 1 for equation, 1 for correct answer]**

(c) $E_{k,\max} = \frac{1}{2}mv_{\max}^2 = \frac{1}{2} \times 0.25 \times (4.0)^2 = 0.125 \times 16 = 2.0\ \mathrm{J}$.
**[2 marks — 1 for formula, 1 for correct answer]**

(d) Sketch: The $x$-axis runs from $-1.0$ to $+1.0$ m. Kinetic energy is a downward-opening parabola with maximum $2.0\ \mathrm{J}$ at $x = 0$ and zero at $x = \pm 1.0$ m. Potential energy is an upward-opening parabola with maximum $2.0\ \mathrm{J}$ at $x = \pm 1.0$ m and zero at $x = 0$. The two curves are mirror images, and their sum at every $x$ is $2.0\ \mathrm{J}$ (total mechanical energy, a horizontal line).
**[3 marks — 1 for correct shape of each curve, 1 for correct key values, 1 for showing constant total energy]**

---

## Key Takeaways

1. **An oscillation** is a repeating back-and-forth motion through an equilibrium position. The **restoring force** always pulls the object back toward equilibrium.

2. **Amplitude** $A$ is the maximum displacement. **Period** $T$ is the time for one full cycle. **Frequency** $f = 1/T$ is cycles per second. **Angular frequency** $\omega = 2\pi f = 2\pi/T$.

3. **SHM** is defined by $a = -\omega^2 x$: acceleration is proportional to displacement and directed toward equilibrium. The minus sign is what makes it oscillatory, not just linear.

4. **SHM is the projection of uniform circular motion.** The radius becomes the amplitude, the angular speed becomes $\omega$, and all SHM formulas can be derived from this geometry.

5. The **connection to the IB Data Booklet** is direct: $a = -\omega^2 x$, $T = 1/f$, $\omega = 2\pi/T = 2\pi f$. You are expected to use these relationships fluently.
