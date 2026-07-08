# Lesson 11: Special Relativity II — Time Dilation and Length Contraction

## What You'll Learn
- Calculate the Lorentz factor $\gamma = 1/\sqrt{1 - v^2/c^2}$
- Apply time dilation: moving clocks run slow by factor $\gamma$
- Apply length contraction: moving objects are shortened by factor $1/\gamma$
- Distinguish between proper time and proper length vs. measured values

---

## 1. The Lorentz Factor — How "Relativistic" Are You?

### 1.1 The Magic Number $\gamma$

All relativistic effects depend on a single number: the Lorentz factor:

$$\gamma = \frac{1}{\sqrt{1 - \frac{v^2}{c^2}}}$$

- At $v = 0$: $\gamma = 1$ (no effect — Newtonian physics)
- At $v = 0.6c$: $\gamma = 1.25$ (25% time dilation)
- At $v = 0.866c$: $\gamma = 2$ (time runs at half speed)
- At $v = 0.99c$: $\gamma \approx 7$ (time runs at 1/7 speed)
- As $v \to c$: $\gamma \to \infty$

For everyday speeds ($v \ll c$), $\gamma \approx 1$ and relativistic effects are negligible. This is why we never notice them — the fastest human-made object (Parker Solar Probe, ~$2 \times 10^5\text{ m s}^{-1}$) has $\gamma = 1.0000002$.

### 1.2 The Speed Limit

As $v$ approaches $c$, $\gamma$ approaches infinity. It would take infinite energy to accelerate a massive object to exactly $c$. The speed of light is a universal speed limit for anything with mass.

---

## 2. Time Dilation — Moving Clocks Run Slow

### 2.1 Proper Time vs. Dilated Time

**Proper time** $\Delta t_0$ is the time interval measured by an observer who is at rest relative to the events — someone for whom the two events occur at the same position. Think of a clock on a spaceship: the astronaut measures the time between two ticks of her own clock as $\Delta t_0$.

**Dilated time** $\Delta t$ is what a stationary observer measures:

$$\Delta t = \gamma \Delta t_0$$

Since $\gamma \geq 1$, $\Delta t \geq \Delta t_0$ — the stationary observer sees the moving clock running SLOWER. A clock moving at $0.866c$ ($\gamma = 2$) ticks once every 2 seconds according to the stationary observer, while the astronaut sees it tick every 1 second.

### 2.2 The Muon Evidence

Cosmic rays create muons in the upper atmosphere (~10 km up). Muons have a half-life of only $2.2\text{ μs}$ (in their own rest frame). At nearly $c$, they "should" travel only about $660\text{ m}$ before decaying — yet we detect them at sea level. Why?

From Earth's frame: the muon's internal clock is time-dilated by $\gamma \approx 22$ (since $v \approx 0.999c$). Its effective half-life becomes $22 \times 2.2 = 48.4\text{ μs}$, enough to travel ~$14\text{ km}$ and reach the ground.

From the muon's frame: the atmosphere is length-contracted (see Section 3) to about $450\text{ m}$, easily traversed in its brief lifetime.

Both perspectives give the same result — the muon reaches the ground. This is experimental confirmation of both time dilation AND length contraction.

### 2.3 The Twin Paradox

One twin stays on Earth. The other travels to a distant star at relativistic speed and returns. The travelling twin ages LESS. This seems paradoxical because motion is relative — each twin sees the other moving. The resolution: the travelling twin experiences acceleration (turning around), which breaks the symmetry. The travelling twin IS younger upon return. This has been confirmed with atomic clocks on aeroplanes.

---

## 3. Length Contraction — Moving Objects Shrink

### 3.1 Proper Length vs. Contracted Length

**Proper length** $L_0$ is the length of an object measured in its own rest frame — the frame where the object is stationary. An astronaut measures her spaceship to be $100\text{ m}$ long. That's $L_0$.

**Contracted length** $L$ is what a stationary observer measures when the object moves past at speed $v$:

$$L = \frac{L_0}{\gamma}$$

Since $\gamma \geq 1$, $L \leq L_0$ — moving objects are SHORTER in the direction of motion. The contraction only affects the dimension parallel to motion; perpendicular dimensions are unchanged.

At $0.866c$ ($\gamma = 2$), a $100\text{ m}$ spaceship appears to be $50\text{ m}$ long to a stationary observer.

### 3.2 It's Real, Not an Illusion

Length contraction is not an optical illusion caused by the finite travel time of light (though that also affects appearance). It is a genuine consequence of the geometry of spacetime. A moving object really IS shorter in the stationary frame.

---

## Worked Examples

### Worked Example 11.1 — Time Dilation Calculation

**Problem:** A spacecraft travels at $0.80c$ relative to Earth. The journey takes $5.0$ years as measured by the astronauts on board. How long does the journey take as measured by mission control on Earth?

**Approach:** The astronauts measure proper time $\Delta t_0 = 5.0$ years. Earth measures dilated time $\Delta t = \gamma\Delta t_0$. Calculate $\gamma$.

**Solution:**
$$\gamma = \frac{1}{\sqrt{1 - 0.80^2}} = \frac{1}{\sqrt{1 - 0.64}} = \frac{1}{\sqrt{0.36}} = \frac{1}{0.60} = 1.667$$
$$\Delta t = 1.667 \times 5.0 = 8.33\text{ years}$$

**Why this makes sense:** At $0.80c$, $\gamma \approx 1.67$, so Earth sees the journey take about 67% longer than the astronauts experience.

---

### Worked Example 11.2 — Length Contraction

**Problem:** A spaceship has a proper length of $120\text{ m}$. It flies past Earth at $0.60c$. What length does an Earth-based observer measure?

**Approach:** $L_0 = 120\text{ m}$ is the proper length. $L = L_0/\gamma$.

**Solution:**
$$\gamma = \frac{1}{\sqrt{1-0.36}} = \frac{1}{0.80} = 1.25$$
$$L = \frac{120}{1.25} = 96\text{ m}$$

---

### Worked Example 11.3 — Muon Problem

**Problem:** A muon is created $10\text{ km}$ above Earth's surface and travels straight down at $0.995c$. Its proper half-life is $2.2\text{ μs}$. Using time dilation, determine whether it reaches the surface.

**Solution:**
$$\gamma = \frac{1}{\sqrt{1-0.995^2}} = \frac{1}{\sqrt{0.009975}} \approx 10.0$$
Dilated half-life: $\gamma \times 2.2 = 22\text{ μs}$. In $22\text{ μs}$ at $0.995c$, distance $= (0.995)(3.0\times 10^8)(22\times 10^{-6}) = 6,570\text{ m}$. After one half-life, half remain. After several half-lives, a significant fraction survives to $10\text{ km}$. Yes, many reach the surface.

---

## Practice Problems

### Problem 1
A spacecraft travels at $0.90c$. Find $\gamma$ and state the time dilation factor.

### Problem 2
An astronaut ages $3.0$ years during a journey at $0.95c$ relative to Earth. How much time passes on Earth?

### Problem 3
A rod has proper length $5.0\text{ m}$. At what speed must it move for its length to be measured as $3.0\text{ m}$ by a stationary observer?

### Problem 4
Explain how both time dilation (from Earth's frame) and length contraction (from the muon's frame) give consistent predictions for the muon reaching sea level.

### Problem 5 — IB-Style
A star is $40$ light-years from Earth as measured in Earth's frame. A spaceship travels to the star at $0.80c$.

(a) Calculate $\gamma$ for this speed. (1 mark)
(b) How long does the journey take as measured by an observer on Earth? (1 mark)
(c) How long does the journey take as measured by the astronauts on the spaceship? (2 marks)
(d) From the astronauts' perspective, the distance to the star is contracted. Calculate this distance. (2 marks)
(e) Verify that the time in (c) and distance in (d) are consistent with the ship's speed being $0.80c$. (1 mark)

---

## Answers

### Answer 1
$\gamma = 1/\sqrt{1-0.81} = 1/\sqrt{0.19} = 1/0.436 = 2.29$. Time runs $2.29\times$ slower for the moving clock as observed from the stationary frame.

### Answer 2
$\gamma = 1/\sqrt{1-0.9025} = 1/\sqrt{0.0975} = 3.20$. $\Delta t = 3.20 \times 3.0 = 9.6$ years.

### Answer 3
$L = L_0/\gamma$, so $\gamma = L_0/L = 5.0/3.0 = 1.667$. $1/\sqrt{1-v^2/c^2} = 1.667$, so $1-v^2/c^2 = 0.36$, $v/c = 0.80$. $v = 0.80c$.

### Answer 4
Earth frame: muon lifetime dilated by $\gamma$ → lives longer, travels further. Muon frame: atmosphere length-contracted by $1/\gamma$ → distance to travel is shorter. Both frames predict the muon survives to the ground. The results are consistent because $\Delta t_{\text{Earth}} = \gamma\Delta t_0$ and $L_{\text{muon}} = L_0/\gamma$ — both give $v = L_0/\Delta t_{\text{Earth}} = (L_0/\gamma)/\Delta t_0$, which is the same speed.

### Answer 5 — IB-Style
**(a)** $\gamma = 1/\sqrt{1-0.64} = 1/0.60 = 1.667$. (1 mark)
**(b)** Time = distance/speed = $40/0.80 = 50$ years. (1 mark)
**(c)** Proper time for astronauts: $\Delta t_0 = \Delta t/\gamma = 50/1.667 = 30$ years. (2 marks — 1 for identifying proper time, 1 for calculation.)
**(d)** $L = L_0/\gamma = 40/1.667 = 24$ light-years. (2 marks)
**(e)** Speed = contracted distance/proper time = $24/30 = 0.80c$ ✓. (1 mark)

---

## Key Takeaways

1. **Lorentz factor:** $\gamma = 1/\sqrt{1-v^2/c^2}$. At everyday speeds $\gamma \approx 1$. Approaches $\infty$ as $v \to c$.

2. **Time dilation:** $\Delta t = \gamma\Delta t_0$. Moving clocks run slow. Proper time $\Delta t_0$ is measured in the rest frame.

3. **Length contraction:** $L = L_0/\gamma$. Moving objects are shortened along the direction of motion. Proper length $L_0$ is measured in the rest frame.

4. **Muons prove both effects.** They reach sea level because of time dilation (Earth frame) or length contraction (muon frame).

5. **$c$ is the universal speed limit.** Nothing with mass can reach it — $\gamma$ would be infinite.
