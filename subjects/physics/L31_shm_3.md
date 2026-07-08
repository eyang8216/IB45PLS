# Lesson 31: Simple Harmonic Motion III — Energy in SHM

> **IB Data Booklet references:** $E_K = \frac{1}{2}m\omega^2(x_0^2 - x^2)$, $E_T = \frac{1}{2}m\omega^2 x_0^2$, $E_p = \frac{1}{2}kx^2$ (mass-spring), $T = 2\pi\sqrt{\frac{m}{k}}$

## What You'll Learn
- How energy transforms between **kinetic** and **potential** during SHM
- The formulas for kinetic energy $E_K$, potential energy $E_P$, and total mechanical energy $E_T$
- Why total energy is proportional to amplitude squared: $E_T \propto A^2$
- Energy graphs: $E_K$ vs $x$, $E_P$ vs $x$, $E_T$ vs $x$
- Energy for the mass-spring system

---

## 1. The Energy Story of SHM

### A Concrete Starting Point: The Mass-Spring System

Imagine a block of mass $m$ attached to a horizontal spring on a frictionless surface. You pull the block to the right, stretching the spring, and then release it. What happens?

The block accelerates leftward toward equilibrium. As it moves, the spring's stretch decreases, so the spring force decreases. The block moves faster and faster until it reaches $x = 0$, where the spring is neither stretched nor compressed. At that instant, the spring exerts zero force, but the block is moving at its maximum speed. It overshoots equilibrium and starts compressing the spring. Now the spring pushes rightward, slowing the block down. Eventually the block stops at $x = -x_0$ (maximum compression), then reverses direction.

This story is really a story about **energy**. At the extremes, all the energy is stored as elastic potential energy in the spring. At equilibrium, all that stored energy has been converted to kinetic energy of the block. In between, the energy is shared.

### Why This Matters

Understanding energy in SHM gives you a powerful alternative to the kinematic approach. Sometimes it is much easier to use energy to find speeds or displacements than to manipulate trigonometric functions. Energy also connects SHM to the broader conservation laws of physics.

---

## 2. Kinetic Energy in SHM

### The Formula

Kinetic energy is always $\frac{1}{2}mv^2$. For SHM, we substitute $v = \omega\sqrt{x_0^2 - x^2}$:

$$\boxed{E_K = \frac{1}{2}m\omega^2(x_0^2 - x^2)}$$

This tells us:

- **At equilibrium** ($x = 0$): $E_K = \frac{1}{2}m\omega^2 x_0^2$, which is the maximum possible kinetic energy.
- **At the extremes** ($x = \pm x_0$): $E_K = 0$, because $v = 0$.
- Kinetic energy depends on $x^2$ — it decreases parabolically as you move away from equilibrium.

### Graph of $E_K$ vs $x$

The $E_K$ vs $x$ graph is a downward-opening parabola, with its peak at $x = 0$ and zeros at $x = \pm x_0$. It is symmetric: $E_K$ at $x = +d$ is exactly the same as $E_K$ at $x = -d$.

---

## 3. Potential Energy in SHM

### Where Does Potential Energy Come From?

Potential energy is stored in the "spring" of the system — whatever provides the restoring force. For a mass on a spring, this is literally elastic potential energy: $E_P = \frac{1}{2}kx^2$.

For a general SHM system, the potential energy function can be written in terms of $\omega$ and $m$. Since $\omega^2 = k/m$ for the mass-spring system, we have $k = m\omega^2$, so:

$$\boxed{E_P = \frac{1}{2}m\omega^2 x^2}$$

This is the potential energy for **any** system undergoing SHM, not just a mass on a spring. It is the energy stored in whatever mechanism provides the restoring force.

Key points:

- **At equilibrium** ($x = 0$): $E_P = 0$. The spring is relaxed (or, for a pendulum, the bob is at its lowest point).
- **At the extremes** ($x = \pm x_0$): $E_P = \frac{1}{2}m\omega^2 x_0^2$, the maximum potential energy.
- Potential energy depends on $x^2$. It does not matter which side of equilibrium you are on; the stored energy is the same at $x = +d$ and $x = -d$.

### For the Simple Pendulum

For a simple pendulum at small angles, the potential energy is gravitational: $E_P = mgh$, where $h$ is the vertical height above the lowest point. For small oscillations, $h \approx x^2/(2L)$, giving $E_P \approx (mg/2L)x^2$, which has the same $x^2$ form with an effective "spring constant" $k_{\text{eff}} = mg/L$. This is why the pendulum approximates SHM for small angles.

---

## 4. Total Mechanical Energy

### The Conservation Statement

In an ideal SHM system with no friction or air resistance, the total mechanical energy $E_T$ is constant:

$$\boxed{E_T = E_K + E_P = \frac{1}{2}m\omega^2(x_0^2 - x^2) + \frac{1}{2}m\omega^2 x^2 = \frac{1}{2}m\omega^2 x_0^2}$$

The $x^2$ terms cancel! This is remarkable: no matter where the object is, the sum of kinetic and potential energy is always the same.

$$\boxed{E_T = \frac{1}{2}m\omega^2 x_0^2}$$

### The Critical Result: $E_T \propto x_0^2$

The total energy is proportional to the **square of the amplitude**. Double the amplitude and the energy quadruples. Triple the amplitude and the energy increases by a factor of nine.

This has profound consequences:
- A pendulum pulled back twice as far carries four times the energy.
- In waves (which we will study soon), intensity is proportional to energy, which is proportional to amplitude squared: $I \propto A^2$.
- In quantum mechanics, the energy of a photon is proportional to the square of the electric field amplitude — this is why bright light has more photons, not larger-amplitude photons.

### Alternative Form

Since $v_{\max} = \omega x_0$, we can also write:

$$E_T = \frac{1}{2}mv_{\max}^2$$

which is simply: the total energy equals the kinetic energy at equilibrium (where all energy is kinetic).

---

## 5. Energy Graphs — The Complete Picture

### $E$ vs $x$ Graph

If you plot $E_K$, $E_P$, and $E_T$ on the same axes with $x$ on the horizontal axis (from $-x_0$ to $+x_0$) and energy on the vertical:

- $E_T$ is a **horizontal line** at height $\frac{1}{2}m\omega^2 x_0^2$. It does not change with $x$.
- $E_P = \frac{1}{2}m\omega^2 x^2$ is an **upward-opening parabola** through the origin. At $x = 0$, $E_P = 0$. At $x = \pm x_0$, $E_P = E_T$.
- $E_K = E_T - E_P$ is a **downward-opening parabola**. At $x = 0$, $E_K = E_T$. At $x = \pm x_0$, $E_K = 0$.

At every $x$, the vertical gap between $E_T$ and $E_P$ is $E_K$. The three graphs together tell the complete energy story.

### $E$ vs $t$ Graph

If you plot the same energies against time:
- $E_P$ oscillates between $0$ and $E_T$ at twice the frequency of the displacement. Why? Because $E_P \propto x^2$, and $x^2$ goes from zero to max twice per cycle (once at $+x_0$, once at $-x_0$).
- $E_K$ oscillates the same way, exactly out of phase with $E_P$: when $E_P$ is max, $E_K = 0$, and vice versa.
- $E_T$ is a constant horizontal line.

### Common Misconception

**Many students think potential energy is maximum at equilibrium because "the speed is highest."** Speed is highest at equilibrium, which means KINETIC energy is maximum there. Potential energy is stored in the deformation of the spring (or the height of the pendulum bob), which is greatest at the extremes. At equilibrium, the spring is relaxed → zero potential energy. Think: if you stop the oscillator and hold it at equilibrium, is there any stored energy? No.

**Many students think energy is "used up" during oscillation.** In an ideal SHM system, energy is conserved — it just changes form between kinetic and potential. No energy is lost. In real systems, friction gradually converts mechanical energy to thermal energy, reducing amplitude over time (this is damping, covered in Lesson 32).

---

## 6. Energy Transfer in One Cycle — A Frame-by-Frame Story

Let's follow the mass-spring system through one full cycle:

| Position | $x$ | $v$ | $E_K$ | $E_P$ | $E_T$ |
|----------|-----|-----|-------|-------|-------|
| Release (max stretch) | $+x_0$ | 0 | 0 | $E_T$ | $E_T$ |
| 1/4 cycle: pass equilibrium | 0 | $-v_{\max}$ | $E_T$ | 0 | $E_T$ |
| 1/2 cycle: max compression | $-x_0$ | 0 | 0 | $E_T$ | $E_T$ |
| 3/4 cycle: pass equilibrium | 0 | $+v_{\max}$ | $E_T$ | 0 | $E_T$ |
| Full cycle: max stretch again | $+x_0$ | 0 | 0 | $E_T$ | $E_T$ |

The total energy never changes. Energy just shifts back and forth between kinetic and potential, twice per cycle.

---

## 7. Two Specific Systems

### Mass-Spring System (Horizontal)

For a horizontal mass-spring on a frictionless surface:

- Restoring force: $F = -kx$ (Hooke's Law)
- $\omega^2 = k/m$, so $\omega = \sqrt{k/m}$
- $T = 2\pi\sqrt{m/k}$
- $E_P = \frac{1}{2}kx^2$ (elastic potential energy)
- $E_T = \frac{1}{2}kA^2$ (using $A$ for amplitude, same as $x_0$)

### Simple Pendulum (Small Angles)

For a simple pendulum (point mass on a massless string of length $L$):

- Restoring force: $F = -mg\sin\theta \approx -mg\theta$ (for small $\theta$)
- Using arc length $s = L\theta$: $F \approx -(mg/L)s$, so "effective spring constant" is $mg/L$
- $\omega^2 = g/L$, so $\omega = \sqrt{g/L}$
- $T = 2\pi\sqrt{L/g}$
- $E_P = mgh$ (gravitational), where $h$ is the vertical displacement

For both systems, the energy formulas $E_K = \frac{1}{2}m\omega^2(A^2 - x^2)$ and $E_T = \frac{1}{2}m\omega^2 A^2$ apply, even though the physical origin of the potential energy is different.

---

## Worked Examples

### Example 1: Energy from Amplitude and Frequency

**Problem:** A 0.500 kg mass oscillates on a spring with amplitude 0.120 m and frequency 2.00 Hz. Find: (a) the total mechanical energy, (b) the maximum speed, (c) the kinetic energy when $x = 0.060$ m.

**Approach:** Find $\omega$ from $f$, then use energy formulas.

**Solution:**

(a) $\omega = 2\pi f = 4\pi\ \mathrm{rad/s}$.
$E_T = \frac{1}{2}m\omega^2 A^2 = \frac{1}{2}(0.500)(4\pi)^2(0.120)^2$
$= 0.250 \times 16\pi^2 \times 0.0144 = 0.250 \times 16 \times \pi^2 \times 0.0144$
$= 4.0 \times 9.87 \times 0.0144 = 0.568\ \mathrm{J}$.

(b) $v_{\max} = \omega A = 4\pi \times 0.120 = 0.48\pi \approx 1.51\ \mathrm{m/s}$.
Check: $E_K = \frac{1}{2}mv_{\max}^2 = \frac{1}{2}(0.500)(0.48\pi)^2 = 0.250 \times 0.2304\pi^2 \approx 0.568\ \mathrm{J}$. ✓

(c) $E_K = E_T - E_P = \frac{1}{2}m\omega^2(A^2 - x^2)$
$= \frac{1}{2}(0.500)(16\pi^2)[(0.120)^2 - (0.060)^2]$
$= (4\pi^2)[0.0144 - 0.0036] = 4\pi^2 \times 0.0108 \approx 0.427\ \mathrm{J}$.

**Why this makes sense:** At half the amplitude, the object has $\frac{3}{4}$ of the total energy as kinetic. This matches the ratio $(A^2 - (A/2)^2)/A^2 = 3/4$.

---

### Example 2: Finding Amplitude from Energy

**Problem:** A 0.200 kg mass on a spring (spring constant $k = 50\ \mathrm{N/m}$) oscillates with a maximum speed of $2.0\ \mathrm{m/s}$. Find: (a) the total energy, (b) the amplitude, (c) the position where the kinetic and potential energies are equal.

**Approach:** Use $v_{\max}$ to get $E_T$, then $E_T = \frac{1}{2}kA^2$ for amplitude.

**Solution:**

(a) $E_T = \frac{1}{2}mv_{\max}^2 = \frac{1}{2}(0.200)(2.0)^2 = 0.100 \times 4.0 = 0.40\ \mathrm{J}$.

(b) $E_T = \frac{1}{2}kA^2$, so $A = \sqrt{2E_T/k} = \sqrt{2 \times 0.40 / 50} = \sqrt{0.80/50} = \sqrt{0.016} = \sqrt{16/1000} = 4/\sqrt{1000} = 4/(10\sqrt{10}) \approx 0.126\ \mathrm{m}$.

Alternatively: $\omega = \sqrt{k/m} = \sqrt{50/0.200} = \sqrt{250} = 5\sqrt{10} \approx 15.8\ \mathrm{rad/s}$. $A = v_{\max}/\omega = 2.0/(5\sqrt{10}) = 2/(5\sqrt{10}) \approx 0.126\ \mathrm{m}$. ✓

(c) $E_K = E_P$ means $E_K = E_P = E_T/2 = 0.20\ \mathrm{J}$.
$E_P = \frac{1}{2}kx^2 = 0.20$ → $x^2 = 2 \times 0.20 / 50 = 0.40/50 = 0.008$ → $x = \sqrt{0.008} \approx 0.0894\ \mathrm{m}$.

As a fraction of amplitude: $x/A = 0.0894/0.126 \approx 0.707 = 1/\sqrt{2}$. This is a general result: $E_K = E_P$ at $x = \pm A/\sqrt{2}$.

**Why this makes sense:** At $A/\sqrt{2}$, $x^2 = A^2/2$, so $E_P = \frac{1}{2}k(A^2/2) = \frac{1}{4}kA^2 = E_T/2$. Then $E_K = E_T - E_T/2 = E_T/2$. Equal.

---

### Example 3: Energy Graphs

**Problem:** A 0.400 kg mass oscillates on a spring with $\omega = 10\ \mathrm{rad/s}$ and amplitude $0.150\ \mathrm{m}$. (a) Calculate and sketch the $E_P$ vs $x$ and $E_K$ vs $x$ graphs on the same axes. (b) From the graph, determine $x$ when $E_K = 3E_P$.

**Approach:** Calculate $E_T$, then use energy relationships.

**Solution:**

(a) $E_T = \frac{1}{2}m\omega^2 A^2 = \frac{1}{2}(0.400)(100)(0.0225) = 20 \times 0.0225 = 0.450\ \mathrm{J}$.

$E_P = \frac{1}{2}m\omega^2 x^2 = 20x^2$.
At $x = A$: $E_P = 20(0.0225) = 0.450\ \mathrm{J} = E_T$.
At $x = 0$: $E_P = 0$.

$E_K = E_T - E_P = 0.450 - 20x^2$.
The graph: $E_P$ is a parabola opening upward from $(0,0)$ to $(\pm A, E_T)$. $E_K$ is an inverted parabola from $(0, E_T)$ to $(\pm A, 0)$.

(b) $E_K = 3E_P$ → $E_T - E_P = 3E_P$ → $E_T = 4E_P$ → $E_P = E_T/4$.
$20x^2 = 0.450/4 = 0.1125$ → $x^2 = 0.005625$ → $x = 0.075\ \mathrm{m} = A/2$.

**Why this makes sense:** $E_P \propto x^2$, so $E_P = E_T/4$ means $x = A/2$. Then $E_K = 3E_T/4$.

---

### Example 4: Pendulum Energy

**Problem:** A simple pendulum of length 2.50 m has a bob of mass 0.300 kg. It is pulled sideways so the string makes an angle of $8.0^\circ$ with the vertical and released. Find: (a) the vertical height the bob rises, (b) the total mechanical energy (relative to the lowest point), (c) the maximum speed of the bob. Use $g = 10\ \mathrm{m/s^2}$.

**Approach:** Geometry for height; then energy conservation.

**Solution:**

(a) $h = L - L\cos\theta = L(1 - \cos\theta)$.
$\cos 8.0^\circ \approx 0.9903$.
$h = 2.50(1 - 0.9903) = 2.50 \times 0.0097 = 0.02425\ \mathrm{m} \approx 2.43\ \mathrm{cm}$.

(b) $E_T = mgh = 0.300 \times 10 \times 0.02425 = 0.07275 \approx 0.0728\ \mathrm{J}$.

(c) $v_{\max} = \sqrt{2E_T/m} = \sqrt{2 \times 0.07275 / 0.300} = \sqrt{0.485} \approx 0.696\ \mathrm{m/s}$.

**Why this makes sense:** For small angles, the pendulum approximates SHM with $\omega = \sqrt{g/L} = \sqrt{10/2.5} = 2.0\ \mathrm{rad/s}$. The amplitude in arc length is $s = L\theta = 2.50 \times (8.0\pi/180) \approx 0.349\ \mathrm{m}$. Then $v_{\max} = \omega s \approx 2.0 \times 0.349 \approx 0.698\ \mathrm{m/s}$, which matches our energy result.

---

### Example 5: Energy Ratio Problem

**Problem:** An object in SHM has total energy $E$. At a certain instant, its kinetic energy is $E/3$. What fraction of the amplitude is its displacement at this instant?

**Approach:** Use $E_K = E_T - E_P$ and express in terms of $x/A$.

**Solution:**

$E_K = E/3$ means $E_P = E_T - E_K = E - E/3 = 2E/3$.

$E_P/E_T = (x/A)^2$ (since both are proportional to $x^2$ and $A^2$).

$(x/A)^2 = 2/3$, so $x/A = \sqrt{2/3} \approx 0.816$.

The displacement is about $81.6\%$ of the amplitude.

---

## Practice Problems

### Problem 1
A 0.250 kg mass attached to a spring oscillates with amplitude 0.080 m and period 0.40 s.
(a) Find the spring constant $k$ and the total mechanical energy.
(b) What is the kinetic energy of the mass when $x = 0.040$ m?
(c) At what displacement is the speed of the mass equal to half its maximum speed?

### Problem 2
A simple pendulum of length 1.60 m has a bob of mass 0.150 kg. It is set swinging with an angular amplitude of $5.0^\circ$.
(a) Calculate the maximum height of the bob above its lowest point.
(b) Use energy conservation to find the maximum speed of the bob.
(c) Find the speed when the bob is at an angle of $2.5^\circ$ from the vertical. (Hint: calculate the height at $2.5^\circ$ first.)
(d) Determine the period of this pendulum and verify that $v_{\max} = \omega x_0$ gives the same result (using arc length as $x_0$).

### Problem 3
A 0.600 kg mass oscillates on a spring. Measurements show that its maximum speed is 1.50 m/s and its maximum acceleration is 7.50 m/s².
(a) Find the angular frequency, the amplitude, and the spring constant.
(b) Calculate the total mechanical energy in two different ways and verify they match.
(c) When the displacement is 0.150 m, what fraction of the total energy is kinetic?

### Problem 4
The total energy of a mass-spring oscillator is 0.320 J. When the displacement is one-third of the amplitude, calculate:
(a) The potential energy.
(b) The kinetic energy.
(c) The ratio $v/v_{\max}$ at this position.

### Problem 5
An oscillator has the displacement equation $x = 0.12\sin(8.0t)$, with $x$ in meters and $t$ in seconds. The mass of the oscillator is 0.400 kg.
(a) Find the total mechanical energy.
(b) On the same set of axes, sketch $E_K(t)$ and $E_P(t)$ over one period. Label all maxima, minima, and the period of the energy oscillation.
(c) At what times during one period is $E_K = E_P$? List all values from $t = 0$ to $t = T$.

### Problem 6 *(IB Exam Style)*
A mass-spring system oscillates with SHM on a frictionless horizontal surface. The mass is 0.350 kg and the spring constant is 56.0 N/m.

(a) Show that the angular frequency of oscillation is $12.6\ \mathrm{rad/s}$. [2 marks]
(b) The amplitude of oscillation is 0.120 m. Calculate the total energy of the system. [2 marks]
(c) Determine the speed of the mass when it is 0.060 m from the equilibrium position. [3 marks]
(d) On a graph of energy against displacement, sketch and label lines to show:
 (i) the total energy
 (ii) the potential energy
 (iii) the kinetic energy
for one full oscillation. Label the maxima on both axes. [3 marks]

---

## Answers

### Answer 1
(a) $\omega = 2\pi/T = 2\pi/0.40 = 5\pi \approx 15.7\ \mathrm{rad/s}$.
$k = m\omega^2 = 0.250 \times (5\pi)^2 = 0.250 \times 25\pi^2 = 6.25\pi^2 \approx 61.7\ \mathrm{N/m}$.
$E_T = \frac{1}{2}kA^2 = \frac{1}{2} \times 6.25\pi^2 \times (0.080)^2 = 3.125\pi^2 \times 0.0064 \approx 0.197\ \mathrm{J}$.

(b) $E_K = E_T - \frac{1}{2}kx^2 = \frac{1}{2}k(A^2 - x^2) = \frac{1}{2} \times 6.25\pi^2 \times (0.0064 - 0.0016) = 3.125\pi^2 \times 0.0048 \approx 0.148\ \mathrm{J}$.
Fraction: $E_K/E_T = (A^2 - x^2)/A^2 = (64 - 16)/64 = 48/64 = 3/4 = 0.75$. ✓

(c) $v = \frac{1}{2}v_{\max}$ → $v = \frac{1}{2}\omega A$.
$v = \omega\sqrt{A^2 - x^2}$ → $\omega\sqrt{A^2 - x^2} = \frac{1}{2}\omega A$ → $A^2 - x^2 = A^2/4$ → $x^2 = \frac{3}{4}A^2$ → $x = \pm\frac{\sqrt{3}}{2}A = \pm 0.0693\ \mathrm{m}$.

---

### Answer 2
(a) $h_{\max} = L(1 - \cos 5.0^\circ) = 1.60(1 - 0.9962) = 1.60 \times 0.0038 = 0.00608\ \mathrm{m} \approx 6.1\ \mathrm{mm}$.

(b) $v_{\max} = \sqrt{2gh_{\max}} = \sqrt{2 \times 10 \times 0.00608} = \sqrt{0.1216} \approx 0.349\ \mathrm{m/s}$.

(c) At $2.5^\circ$: $h = L(1 - \cos 2.5^\circ) = 1.60(1 - 0.99905) = 1.60 \times 0.00095 = 0.00152\ \mathrm{m}$.
Speed from energy: $\frac{1}{2}mv^2 = mg(h_{\max} - h)$ → $v = \sqrt{2g(h_{\max} - h)} = \sqrt{2 \times 10 \times (0.00608 - 0.00152)} = \sqrt{20 \times 0.00456} = \sqrt{0.0912} \approx 0.302\ \mathrm{m/s}$.

(d) $T = 2\pi\sqrt{L/g} = 2\pi\sqrt{1.60/10} = 2\pi\sqrt{0.16} = 2\pi \times 0.40 = 0.80\pi \approx 2.51\ \mathrm{s}$.
$\omega = 2\pi/T = 2.50\ \mathrm{rad/s}$.
Arc length amplitude: $s_0 = L\theta = 1.60 \times (5.0\pi/180) = 0.1396\ \mathrm{m}$.
$v_{\max} = \omega s_0 = 2.50 \times 0.1396 \approx 0.349\ \mathrm{m/s}$. Matches part (b). ✓

---

### Answer 3
(a) $\omega = a_{\max}/v_{\max} = 7.50/1.50 = 5.00\ \mathrm{rad/s}$.
$A = v_{\max}/\omega = 1.50/5.00 = 0.300\ \mathrm{m}$.
$k = m\omega^2 = 0.600 \times 25.0 = 15.0\ \mathrm{N/m}$.

(b) Method 1: $E_T = \frac{1}{2}mv_{\max}^2 = \frac{1}{2}(0.600)(1.50)^2 = 0.300 \times 2.25 = 0.675\ \mathrm{J}$.
Method 2: $E_T = \frac{1}{2}kA^2 = \frac{1}{2}(15.0)(0.300)^2 = 7.50 \times 0.0900 = 0.675\ \mathrm{J}$. ✓

(c) $x = 0.150 = A/2$. $E_K/E_T = (A^2 - x^2)/A^2 = (A^2 - A^2/4)/A^2 = 3/4$.
So $E_K = 0.75 \times 0.675 = 0.506\ \mathrm{J}$.

---

### Answer 4
(a) $x = A/3$, so $(x/A)^2 = 1/9$. $E_P/E_T = 1/9$.
$E_P = 0.320/9 \approx 0.0356\ \mathrm{J}$.

(b) $E_K = E_T - E_P = 0.320 - 0.0356 = 0.2844\ \mathrm{J} = \frac{8}{9}E_T$.

(c) $v/v_{\max} = \sqrt{E_K/E_T} = \sqrt{8/9} = \frac{2\sqrt{2}}{3} \approx 0.943$.

---

### Answer 5
(a) $\omega = 8.0\ \mathrm{rad/s}$, $A = 0.12\ \mathrm{m}$, $m = 0.400\ \mathrm{kg}$.
$E_T = \frac{1}{2}m\omega^2 A^2 = \frac{1}{2}(0.400)(64)(0.0144) = 0.200 \times 64 \times 0.0144 = 12.8 \times 0.0144 = 0.1843\ \mathrm{J}$.

(b) $T = 2\pi/\omega = \pi/4 \approx 0.785\ \mathrm{s}$. The energy period is $T/2 \approx 0.393\ \mathrm{s}$ (since $E_K$ and $E_P$ go through two cycles per oscillation cycle).
$E_K(t) = E_T\cos^2(8.0t)$, $E_P(t) = E_T\sin^2(8.0t)$.
$E_K$ starts at max ($E_T$ at $t = 0$), $E_P$ starts at zero. They oscillate between $0$ and $E_T$ at frequency $16.0\ \mathrm{rad/s}$.
The graph shows two sinusoidal curves, $180^\circ$ out of phase, each peaking at $E_T$ and bottoming at $0$.

(c) $E_K = E_P$ when $\cos^2(8.0t) = \sin^2(8.0t)$ → $\tan^2(8.0t) = 1$ → $8.0t = \pi/4, 3\pi/4, 5\pi/4, 7\pi/4$.
$t = \pi/32, 3\pi/32, 5\pi/32, 7\pi/32$ seconds.
That is $t \approx 0.098, 0.295, 0.491, 0.687$ s.

---

### Answer 6 (IB Exam Style)

(a) $\omega = \sqrt{k/m} = \sqrt{56.0/0.350} = \sqrt{160} = 4\sqrt{10} \approx 12.65 \approx 12.6\ \mathrm{rad/s}$.
**[2 marks — 1 for formula, 1 for correct value with units]**

(b) $E_T = \frac{1}{2}kA^2 = \frac{1}{2}(56.0)(0.120)^2 = 28.0 \times 0.0144 = 0.4032 \approx 0.403\ \mathrm{J}$.
**[2 marks — 1 for formula, 1 for correct answer]**

(c) $v = \omega\sqrt{A^2 - x^2} = 12.65\sqrt{0.0144 - 0.0036} = 12.65\sqrt{0.0108} = 12.65 \times 0.1039 \approx 1.31\ \mathrm{m/s}$.
Alternative energy method: $E_K = \frac{1}{2}k(A^2 - x^2) = \frac{1}{2}(56.0)(0.0108) = 0.3024\ \mathrm{J}$.
$v = \sqrt{2E_K/m} = \sqrt{2 \times 0.3024/0.350} = \sqrt{1.728} \approx 1.31\ \mathrm{m/s}$.
**[3 marks — 1 for correct relationship, 1 for substitution, 1 for answer]**

(d) $E_T$ is a horizontal line at $0.403\ \mathrm{J}$. $E_P$ is an upward parabola from $(0, 0)$ to $(\pm 0.120, 0.403)$. $E_K$ is a downward parabola from $(0, 0.403)$ to $(\pm 0.120, 0)$. x-axis labeled "displacement / m" from $-0.12$ to $+0.12$. y-axis labeled "energy / J" from $0$ to $0.403$.
**[3 marks — 1 for correct shape of each curve, 1 for correct values, 1 for labels]**

---

## Key Takeaways

1. **Total mechanical energy** in SHM is constant: $E_T = \frac{1}{2}m\omega^2 A^2 = \frac{1}{2}kA^2$. It is proportional to $A^2$.

2. **Kinetic energy**: $E_K = \frac{1}{2}m\omega^2(A^2 - x^2)$. Maximum at equilibrium, zero at extremes.

3. **Potential energy**: $E_P = \frac{1}{2}m\omega^2 x^2 = \frac{1}{2}kx^2$ (mass-spring). Maximum at extremes, zero at equilibrium.

4. **Energy graphs**: $E_T$ is a horizontal line. $E_P$ and $E_K$ are parabolas, mirror images. The sum is always $E_T$.

5. **Key ratio**: $E_K = E_P$ when $x = A/\sqrt{2}$. In general, $(E_P/E_T) = (x/A)^2$.
