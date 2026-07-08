# Lesson 32: Simple Harmonic Motion IV — Damping, Resonance and Q-Factor (HL)

## What You'll Learn
- Distinguish between light, heavy, and critical damping
- Explain resonance as the response of a system driven at its natural frequency
- Interpret resonance curves and understand the effect of damping on resonance width
- Define and calculate the Q-factor (quality factor) of an oscillator
- Apply resonance concepts to real-world examples including bridges, musical instruments, and MRI

---

## 1. What Happens When Friction Enters SHM?

### 1.1 Why This Matters

In Lessons 29–31, we studied ideal simple harmonic motion — a mass on a spring or a pendulum swinging forever with constant amplitude. This is a beautiful model, but it is not realistic. In the real world, every oscillator loses energy. A pendulum eventually stops. A guitar string's vibration fades. A car's suspension doesn't bounce forever after hitting a bump.

The loss of energy from an oscillating system is called **damping**. Understanding damping is essential because everything that oscillates in the real world is damped to some degree. Engineers design damping into systems deliberately — car shock absorbers, building earthquake dampers, and aircraft vibration controls all use controlled damping.

### 1.2 What Damping Does

Damping removes energy from an oscillating system, usually by converting kinetic energy to thermal energy through friction, air resistance, or internal material losses. The effect on the motion depends on how strong the damping is relative to the restoring force.

There are three regimes of damping, distinguished by how the system returns to equilibrium:

**Light damping (underdamping):** The system oscillates with a gradually decreasing amplitude. Each cycle is slightly smaller than the previous one. The frequency of the damped oscillation is very slightly less than the natural frequency $\omega_0$, but for light damping the difference is negligible. Most real oscillators operate in this regime — a pendulum in air, a tuning fork, a guitar string.

**Critical damping:** The system returns to equilibrium in the shortest possible time WITHOUT oscillating. It crosses the equilibrium position at most once. Critical damping represents the exact threshold between oscillatory and non-oscillatory behaviour. Car suspension systems are designed to be close to critically damped — you want the car to settle quickly after a bump without bouncing.

**Heavy damping (overdamping):** The system returns to equilibrium slowly without oscillating. The damping force is so large that it dominates the restoring force, and the system creeps back to equilibrium. A pendulum in thick oil or a door with a very stiff hydraulic closer exhibits heavy damping.

### 1.3 The Damping Force

For many systems, the damping force is proportional to velocity and opposes motion: $F_{\text{damping}} = -bv$, where $b$ is the damping coefficient. The larger $b$, the stronger the damping. This is called viscous damping and applies to objects moving slowly through fluids.

### 1.4 Common Misconception

Many students think that "damping changes the period." For light damping, the period is essentially unchanged — the oscillations still occur at very nearly the natural frequency. What changes is the amplitude. The system loses energy, so the amplitude decays (typically exponentially: $A = A_0 e^{-\gamma t}$), but the timing between zero-crossings stays nearly constant.

---

## 2. Resonance — When Pushing at the Right Time Multiplies the Motion

### 2.1 The Playground Swing Analogy

Think of pushing a child on a swing. If you push at random times, nothing much happens. If you push at exactly the right moment — just as the swing reaches its highest point and starts back down — each push adds a little energy, and the amplitude grows and grows. You are driving the swing at its natural frequency.

This is resonance: when a system is driven by an external periodic force at a frequency that matches (or is close to) its natural frequency, the amplitude of oscillation becomes very large.

### 2.2 The Physics of Resonance

Every oscillator has a **natural frequency** $f_0$ — the frequency at which it oscillates when displaced and released. When an external driving force oscillates at a frequency $f_d$, the response (amplitude) of the system depends on how close $f_d$ is to $f_0$.

- $f_d \ll f_0$: The system barely responds. The driving is too slow; the system can keep up easily.
- $f_d = f_0$: **Resonance.** The driving force is always in phase with the motion, adding energy at the optimal moment each cycle. Amplitude becomes very large.
- $f_d \gg f_0$: The system cannot keep up. The amplitude is small.

### 2.3 The Resonance Curve

A graph of amplitude against driving frequency shows a peak centred at $f_0$. The height and width of this peak depend on the amount of damping:

- **Light damping:** Very tall, narrow peak. The system responds strongly only to frequencies very close to $f_0$. The amplitude at resonance can be many times larger than the driving amplitude.
- **Heavy damping:** Short, wide peak. The system responds over a broader range of frequencies, but the maximum amplitude is much lower.
- **No damping (ideal):** The amplitude would theoretically go to infinity at resonance — the system would absorb energy indefinitely with no mechanism to lose it. In reality, some damping always exists.

### 2.4 Phase Relationship at Resonance

At resonance, the driven oscillator's displacement lags behind the driving force by exactly $90^\circ$ ($\pi/2$ radians). This means the velocity is exactly in phase with the driving force — the force pushes in the same direction as the motion at every instant, which is why energy transfer is maximised.

### 2.5 Resonance in the Real World — Helpful and Destructive

**Helpful resonance:**
- **Musical instruments:** The body of a violin resonates at the frequencies of the strings, amplifying the sound. The air column in a flute resonates at the frequency determined by the player's fingering.
- **MRI (Magnetic Resonance Imaging):** Radio waves at the resonant frequency of hydrogen nuclei in water molecules are used to create medical images.
- **Radio tuning:** Turning the dial changes the resonant frequency of an LC circuit to match the frequency of the desired station.

**Destructive resonance:**
- **Tacoma Narrows Bridge (1940):** Wind-driven oscillations at the bridge's resonant frequency caused it to twist and collapse. This is the most famous engineering failure due to resonance.
- **Soldiers marching on a bridge:** Soldiers are ordered to break step when crossing bridges to avoid driving the bridge at its resonant frequency.
- **Earthquakes:** Buildings have natural frequencies. If an earthquake's ground motion matches a building's natural frequency, the building can resonate and collapse even if the ground motion itself is modest.

---

## 3. The Q-Factor — Measuring the "Quality" of Resonance

### 3.1 What Q Measures

The quality factor $Q$ (or Q-factor) quantifies how underdamped an oscillator is — how "sharp" its resonance is. A high-Q oscillator rings for a long time after being struck; a low-Q oscillator dies out quickly.

$$Q = 2\pi \frac{\text{energy stored}}{\text{energy lost per cycle}}$$

A high Q means the oscillator loses a small fraction of its energy per cycle. A tuning fork might have $Q \sim 1,000$; a car suspension might have $Q \sim 1$.

### 3.2 Q from the Resonance Curve

Q can also be determined from the width of the resonance peak:

$$Q = \frac{f_0}{\Delta f}$$

where $f_0$ is the resonant frequency and $\Delta f$ is the **bandwidth** — the width of the resonance curve at an amplitude of $1/\sqrt{2}$ of the maximum (this is the "half-power" width, since power $\propto$ amplitude$^2$).

A narrow peak (small $\Delta f$) means high Q. A broad peak (large $\Delta f$) means low Q.

### 3.3 The Physical Meaning of Q

- $Q > 0.5$: Underdamped — oscillations occur
- $Q = 0.5$: Critically damped — fastest return to equilibrium without oscillation
- $Q < 0.5$: Overdamped — slow return, no oscillation
- High Q (hundreds or thousands): The oscillator rings for many cycles with little energy loss

---

## Worked Examples

### Worked Example 32.1 — Identifying Damping Type

**Problem:** A mass-spring system is set into oscillation. In medium A, the amplitude drops to half its initial value after 50 oscillations. In medium B, the system does not oscillate at all but returns slowly to equilibrium. In medium C, the system returns to equilibrium in the shortest possible time without oscillating. Identify the type of damping in each medium.

**Solution:**
Medium A: 50 oscillations with decaying amplitude = **light damping** (underdamped).
Medium B: No oscillation, slow return = **heavy damping** (overdamped).
Medium C: Fastest return, no oscillation = **critical damping**.

---

### Worked Example 32.2 — Q-Factor from Resonance Curve

**Problem:** A mechanical oscillator has a resonance curve centred at $f_0 = 500\text{ Hz}$. At an amplitude of $1/\sqrt{2}$ of the peak, the frequencies are $495\text{ Hz}$ and $505\text{ Hz}$. Calculate the Q-factor.

**Approach:** $Q = f_0/\Delta f$ where $\Delta f$ is the full width at $1/\sqrt{2}$ amplitude. $\Delta f = 505 - 495 = 10\text{ Hz}$.

**Solution:**
$$Q = \frac{500}{10} = 50$$

**Why this makes sense:** A Q of 50 means the oscillator is moderately high-Q — it would ring for roughly $Q/\pi \approx 16$ cycles to lose most of its energy after excitation stops. This is typical of a tuning fork or a good mechanical resonator.

---

### Worked Example 32.3 — Energy Lost per Cycle

**Problem:** An oscillator stores $0.20\text{ J}$ of energy and has a Q-factor of $200$. Calculate the energy lost per cycle.

**Approach:** Rearrange $Q = 2\pi E_{\text{stored}}/E_{\text{lost}}$ to find $E_{\text{lost}}$.

**Solution:**
$$E_{\text{lost}} = \frac{2\pi E_{\text{stored}}}{Q} = \frac{2\pi(0.20)}{200} = 6.28 \times 10^{-3}\text{ J}$$

---

### Worked Example 32.4 — IB-Style Damping and Resonance

**Problem:** A child on a swing (natural frequency 0.50 Hz) is being pushed by a parent.

(a) At what frequency should the parent push for maximum amplitude? (1 mark)

(b) The swing has light damping (Q ≈ 10). The parent pushes at exactly 0.50 Hz for 10 cycles, and the amplitude grows to 2.0 m. The parent then stops pushing. Approximately how many complete oscillations occur before the amplitude drops to about 0.1 m? Explain your reasoning. (3 marks)

**Solution (a):** The parent should push at the natural frequency, $0.50\text{ Hz}$, for maximum amplitude through resonance.

**(b):** With Q = 10, the energy decays by a factor of about $e^{-2\pi/Q} \approx e^{-0.628}$ per cycle — about half the energy per cycle. Amplitude is proportional to $\sqrt{E}$, so amplitude falls to $1/\sqrt{2} \approx 0.71$ per cycle. To fall from 2.0 m to 0.1 m (a factor of 20), roughly $\ln(20) \times Q/\pi \approx 3.0 \times 3.2 \approx 10$ cycles. More precisely: after $n$ cycles, amplitude $\approx 2.0 \times e^{-\pi n/Q}$. Set $0.1 = 2.0 e^{-\pi n/10}$, so $e^{-\pi n/10} = 0.05$, $-\pi n/10 = \ln(0.05) = -3.0$, $n = 30/\pi \approx 10$ oscillations.

---

## Practice Problems

### Problem 1
Describe and sketch the displacement-time graph for a lightly damped harmonic oscillator released from amplitude $A_0$. Label the envelope of the decay.

### Problem 2
A car suspension system is designed to be critically damped. Explain why this is desirable, referring to both underdamping and overdamping.

### Problem 3
A resonance curve for a driven oscillator peaks at 200 Hz with an amplitude of 5.0 cm. The frequencies at which the amplitude is $5.0/\sqrt{2} = 3.54\text{ cm}$ are 196 Hz and 204 Hz. Calculate the Q-factor.

### Problem 4
An oscillator stores $0.50\text{ J}$ and has $Q = 100$. Calculate the power dissipated (energy lost per second) when oscillating at 400 Hz.

### Problem 5 — IB-Style
A mechanical oscillator of mass 0.50 kg, spring constant $200\text{ N m}^{-1}$, and Q-factor 25 is driven by a variable-frequency motor.

(a) Calculate the natural frequency of the oscillator. (2 marks)

(b) Sketch a graph of oscillation amplitude against driving frequency for this oscillator, labelling the axes and the resonant frequency. (3 marks)

(c) On the same axes, sketch the curve for an oscillator with the same natural frequency but Q = 5. Explain the differences. (3 marks)

(d) The amplitude at resonance for the Q = 25 oscillator is 4.0 cm. The driving motor is switched off. Estimate the number of complete oscillations before the amplitude drops to 1.0 cm. (3 marks)

---

## Answers

### Answer 1
The graph shows oscillations with amplitude decreasing exponentially. The envelope consists of two curves: $+A_0 e^{-\gamma t}$ (upper) and $-A_0 e^{-\gamma t}$ (lower). The oscillations are contained within this shrinking envelope. The period remains essentially constant even as the amplitude decays.

### Answer 2
Underdamped suspension would oscillate (bounce) after hitting a bump, making the ride uncomfortable and reducing tyre contact with the road. Overdamped suspension would return too slowly — the car would not settle quickly after a bump, making handling sluggish. Critical damping provides the fastest return to equilibrium without oscillation, giving the best compromise between comfort and control.

### Answer 3
$\Delta f = 204 - 196 = 8.0\text{ Hz}$. $Q = 200/8.0 = 25$.

### Answer 4
Energy lost per cycle: $E_{\text{lost}} = 2\pi(0.50)/100 = 0.0314\text{ J}$. At 400 Hz, 400 cycles occur per second. Power = $0.0314 \times 400 = 12.6\text{ W}$.

### Answer 5 — IB-Style
**(a)** $f_0 = \frac{1}{2\pi}\sqrt{k/m} = \frac{1}{2\pi}\sqrt{200/0.50} = \frac{1}{2\pi}\sqrt{400} = 20/2\pi = 3.18\text{ Hz}$. (2 marks)

**(b)** (3 marks) Graph: amplitude (y-axis) vs. driving frequency (x-axis), with a peak at $f_0 = 3.18\text{ Hz}$. Axes labelled. Narrow, tall peak. (1 mark for axes, 1 for peak at correct frequency, 1 for tall narrow shape.)

**(c)** (3 marks) Q = 5 curve: shorter, wider peak centred at the same $f_0$. Lower maximum amplitude, broader width. The area under the curve is related to total energy absorption. (1 mark for same $f_0$, 1 for lower height, 1 for greater width with explanation.)

**(d)** (3 marks) $Q = 25$ means amplitude falls by factor $e^{-\pi n/25}$ over $n$ cycles. From 4.0 cm to 1.0 cm: factor of 4. $e^{-\pi n/25} = 0.25$. $-\pi n/25 = \ln(0.25) = -1.386$. $n = 1.386 \times 25/\pi = 11.0$ cycles. (1 mark for using $e^{-\pi n/Q}$ decay law, 1 mark for correct setup, 1 mark for $n \approx 11$.)

---

## Key Takeaways

1. **Three damping regimes:** Light (oscillations with decaying amplitude), critical (fastest return without oscillation), heavy (slow return, no oscillation).

2. **Resonance** occurs when driving frequency = natural frequency. The amplitude peaks because energy is transferred at the optimal phase.

3. **Damping controls resonance:** Light damping → tall, narrow resonance peak. Heavy damping → short, wide peak.

4. **Q-factor:** $Q = 2\pi E_{\text{stored}}/E_{\text{lost}} = f_0/\Delta f$. High Q = sharp resonance, long ringing.

5. **Resonance can be destructive** (Tacoma Narrows, earthquake-building interaction) or useful (musical instruments, MRI, radio tuning). Engineers design to either exploit or suppress it.
