# Lesson 1: Kinematics — Describing Motion

## What You'll Learn

By the end of this lesson, you will be able to:
- Describe motion using displacement, velocity, and acceleration
- Use all four SUVAT equations to solve problems involving constant acceleration
- Read and sketch displacement–time, velocity–time, and acceleration–time graphs
- Solve projectile motion problems by treating horizontal and vertical motion independently

---

## 1. Why Kinematics Matters

Before we can understand forces, energy, or any other part of physics, we need a language for describing motion itself. Kinematics is that language. It answers questions like: *How far did the object go? How fast is it moving? Is it speeding up or slowing down?* Notice what kinematics does NOT ask: it does not ask *why* the object moved. That question belongs to dynamics, which comes later. Kinematics is purely about description — the "what" of motion, not the "why."

Every IB Physics Paper 1 and Paper 2 will include kinematics problems. They appear on their own and also embedded inside larger problems about forces, energy, fields, and waves. If you cannot solve a SUVAT problem cold, you will lose marks across the entire exam, not just in the mechanics section.

---

## 2. The Three Quantities That Describe Motion

### 2.1 Displacement — Where Is It?

**Displacement** is a vector quantity: it tells you how far an object is from its starting point AND in which direction. The symbol is $s$ and the SI unit is the metre (m).

A student walks 3 metres east, then 4 metres west. The total *distance* travelled is 7 metres, but the *displacement* is 1 metre west. Distance is a scalar (magnitude only); displacement is a vector (magnitude and direction). This distinction matters every time an object changes direction.

When we write $s = 25\text{ m}$, the sign of $s$ tells us the direction relative to a chosen coordinate system. If we define "right" as positive, then $s = +25\text{ m}$ means 25 metres to the right, and $s = -25\text{ m}$ means 25 metres to the left.

### 2.2 Velocity — How Fast and Which Way?

**Velocity** is the rate of change of displacement with respect to time. It is also a vector.

$$v = \frac{\Delta s}{\Delta t}$$

The symbol is $v$ and the SI unit is metres per second (m s⁻¹).

**Speed** is different from velocity. Speed is a scalar: it tells you how fast something is going but not in which direction. If a car drives in a circle at a constant 30 m s⁻¹, its *speed* never changes, but its *velocity* changes continuously because the direction changes.

**Instantaneous velocity** is the velocity at a single moment in time. **Average velocity** is the total displacement divided by the total time. These are only equal when velocity is constant.

### 2.3 Acceleration — Is It Speeding Up or Slowing Down?

**Acceleration** is the rate of change of velocity with respect to time. It is also a vector.

$$a = \frac{\Delta v}{\Delta t}$$

The symbol is $a$ and the SI unit is metres per second squared (m s⁻²).

An acceleration of $3\text{ m s}^{-2}$ means the velocity increases by 3 m s⁻¹ every second.

**A common misconception:** Many students think "acceleration" always means "speeding up." It does not. If an object is slowing down, it is still accelerating — the acceleration is simply in the opposite direction to its velocity. We sometimes call this "deceleration," but the physics is the same: the velocity is changing. A car braking from 20 m s⁻¹ to 0 m s⁻¹ in 4 seconds has an acceleration of $-5\text{ m s}^{-2}$. The negative sign tells us the acceleration opposes the motion.

---

## 3. The SUVAT Equations

When acceleration is **constant** (and only when it is constant), there are four equations that relate the five quantities: $s$, $u$, $v$, $a$, and $t$. These are called the SUVAT equations.

| Quantity | Symbol | Meaning | SI Unit |
|----------|--------|---------|---------|
| Displacement | $s$ | How far from the start | m |
| Initial velocity | $u$ | Velocity at $t = 0$ | m s⁻¹ |
| Final velocity | $v$ | Velocity at time $t$ | m s⁻¹ |
| Acceleration | $a$ | Rate of change of velocity | m s⁻² |
| Time | $t$ | Duration of motion | s |

The four equations, each missing one quantity:

| Equation | Missing |
|----------|---------|
| $v = u + at$ | $s$ |
| $s = ut + \frac{1}{2}at^2$ | $v$ |
| $v^2 = u^2 + 2as$ | $t$ |
| $s = \frac{(u+v)}{2}t$ | $a$ |

**How to choose the right equation:** Every SUVAT problem gives you three quantities and asks for a fourth. Identify which quantity is NOT mentioned in the problem (neither given nor asked for), then pick the equation that does not contain that quantity. This method works every time.

All four equations appear in the IB Data Booklet. You do not need to memorise them, but you DO need to know which one to use. Practise identifying the missing quantity until it becomes automatic.

---

## 4. Motion Graphs

Graphs are a second language for kinematics. The IB exam will ask you to interpret them and sketch them.

### 4.1 Displacement–Time Graphs ($s$–$t$)

- The **gradient** (slope) of an $s$–$t$ graph at any point gives the instantaneous velocity
- A straight line means constant velocity
- A curved line means the velocity is changing (acceleration is present)
- A horizontal line means the object is stationary (zero velocity)

### 4.2 Velocity–Time Graphs ($v$–$t$)

- The **gradient** of a $v$–$t$ graph at any point gives the instantaneous acceleration
- The **area under the curve** between two times gives the displacement during that interval
- A horizontal line means constant velocity (zero acceleration)
- A straight sloping line means constant acceleration

This graph type is the most powerful because it gives you three quantities at once: velocity (read directly from the vertical axis), acceleration (from the gradient), and displacement (from the area).

### 4.3 Acceleration–Time Graphs ($a$–$t$)

- The **area under the curve** gives the change in velocity
- A horizontal line means constant acceleration
- A horizontal line at zero means constant velocity

### 4.4 How the Three Graphs Relate

If you have a $v$–$t$ graph, you can construct the other two:
- The $s$–$t$ graph is found by calculating the area under the $v$–$t$ curve at each point (this gives cumulative displacement)
- The $a$–$t$ graph is found by calculating the gradient of the $v$–$t$ curve at each point

---

## 5. Free Fall

An object falling under gravity alone (no air resistance) experiences constant downward acceleration. Near Earth's surface, the magnitude of this acceleration is approximately $9.81\text{ m s}^{-2}$. In IB problems, you may be told to use $g = 10\text{ m s}^{-2}$ for simplicity — always check the instructions.

The key insight for free fall: the equations are exactly the same SUVAT equations, with $a = -g$ if we define upward as positive. The negative sign is because gravity pulls downward, opposite to our chosen positive direction.

**A common misconception:** Some students think heavier objects fall faster. In the absence of air resistance, all objects fall with the same acceleration regardless of mass. A feather and a hammer dropped on the Moon (no atmosphere) hit the ground at the same time — this was famously demonstrated during the Apollo 15 mission.

---

## 6. Projectile Motion

A projectile is any object launched into the air and moving under gravity alone (we ignore air resistance in IB problems). The key to solving projectile problems is to realise that **horizontal and vertical motions are independent**.

### 6.1 Why Independence Works

Gravity acts only in the vertical direction. There is no horizontal force (we neglect air resistance), so there is no horizontal acceleration. This means:
- **Horizontal velocity is constant** throughout the flight: $v_x = u\cos\theta$ (constant)
- **Vertical motion** follows the SUVAT equations with $a = -g$: $v_y = u\sin\theta - gt$

The two motions share only one thing: **time**. The time of flight is determined by the vertical motion. Once you know the time, you can find the horizontal range.

### 6.2 Horizontal Launch (Launched Horizontally from a Height)

When an object is launched horizontally from a height $H$:

- Initial vertical velocity $u_y = 0$
- Time to hit the ground comes from vertical motion alone: $H = \frac{1}{2}gt^2$, so $t = \sqrt{\frac{2H}{g}}$
- Horizontal range: $R = u_x \times t = u_x\sqrt{\frac{2H}{g}}$

The object follows a parabolic path. Its vertical speed increases as it falls; its horizontal speed never changes.

### 6.3 Angled Launch (Launched from Ground Level at Angle $\theta$)

When an object is launched from ground level at speed $u$ and angle $\theta$ above the horizontal:

The initial velocity splits into components:
- $u_x = u\cos\theta$ (horizontal — constant throughout flight)
- $u_y = u\sin\theta$ (vertical — changes due to gravity)

Three key results (derived from SUVAT with $s_y = 0$ at landing):

- **Time of flight:** $T = \frac{2u\sin\theta}{g}$
- **Maximum height:** $H_{\text{max}} = \frac{u^2\sin^2\theta}{2g}$
- **Range:** $R = \frac{u^2\sin(2\theta)}{g}$

The maximum range for a given launch speed occurs when $\theta = 45^\circ$, because $\sin(90^\circ) = 1$, which maximises $R$.

**A common misconception:** Doubling the launch speed does NOT double the range. Since $R \propto u^2$, doubling $u$ quadruples the range. This counterintuitive result appears regularly in IB multiple-choice questions.

---

## Worked Examples

### Worked Example 1.1 — Choosing the Right SUVAT Equation

**Problem:** A car accelerates uniformly from rest at $3.0\text{ m s}^{-2}$ for $6.0$ seconds. How far does it travel during this time?

**Approach:** We are given $u = 0$, $a = 3.0$, $t = 6.0$, and asked for $s$. The quantity NOT mentioned is $v$ (final velocity). We need the equation without $v$, which is $s = ut + \frac{1}{2}at^2$.

**Solution:**
$$s = ut + \frac{1}{2}at^2$$
$$s = (0)(6.0) + \frac{1}{2}(3.0)(6.0)^2$$
$$s = 0 + \frac{1}{2}(3.0)(36)$$
$$s = 0 + 54$$
$$s = 54\text{ m}$$

**Why this makes sense:** Starting from rest at a modest acceleration for 6 seconds, 54 metres is a reasonable distance — about half a football pitch.

---

### Worked Example 1.2 — Free Fall

**Problem:** A stone is dropped from a cliff $80\text{ m}$ high. Using $g = 10\text{ m s}^{-2}$, calculate: (a) the time taken to reach the ground, and (b) the speed at which it hits the ground.

**Approach:** This is vertical motion under gravity. Define downward as positive so $a = +g = +10\text{ m s}^{-2}$. We know $u = 0$ (dropped, not thrown), $s = 80\text{ m}$, $a = 10\text{ m s}^{-2}$.

For part (a), we need $t$. The missing quantity is $v$, so use $s = ut + \frac{1}{2}at^2$.

For part (b), we now know $t = 4.0\text{ s}$, so use $v = u + at$.

**Solution (a):**
$$s = ut + \frac{1}{2}at^2$$
$$80 = 0 \times t + \frac{1}{2}(10)t^2$$
$$80 = 5t^2$$
$$t^2 = 16$$
$$t = 4.0\text{ s}$$

**Solution (b):**
$$v = u + at$$
$$v = 0 + (10)(4.0)$$
$$v = 40\text{ m s}^{-1}$$

**Why this makes sense:** After 4 seconds of free fall, the speed is 40 m s⁻¹. At $g = 10$, the speed increases by 10 m s⁻¹ each second: after 1 s it is 10 m s⁻¹, after 2 s it is 20 m s⁻¹, after 3 s it is 30 m s⁻¹, after 4 s it is 40 m s⁻¹. The numbers are consistent.

---

### Worked Example 1.3 — Velocity–Time Graph Interpretation

**Problem:** A car's velocity–time graph shows: from $t = 0$ to $t = 4\text{ s}$, velocity increases linearly from $0$ to $20\text{ m s}^{-1}$; from $t = 4$ to $t = 10\text{ s}$, velocity stays constant at $20\text{ m s}^{-1}$; from $t = 10$ to $t = 14\text{ s}$, velocity decreases linearly from $20\text{ m s}^{-1}$ to $0$. Find the total displacement.

**Approach:** The displacement equals the area under the velocity–time graph. The graph consists of three regions: a triangle (0–4 s), a rectangle (4–10 s), and another triangle (10–14 s). Find each area separately and sum them.

**Solution:**

Region 1 (0–4 s, triangle):
$$\text{Area} = \frac{1}{2} \times \text{base} \times \text{height} = \frac{1}{2} \times 4 \times 20 = 40\text{ m}$$

Region 2 (4–10 s, rectangle):
$$\text{Area} = \text{base} \times \text{height} = 6 \times 20 = 120\text{ m}$$

Region 3 (10–14 s, triangle):
$$\text{Area} = \frac{1}{2} \times 4 \times 20 = 40\text{ m}$$

Total displacement:
$$s_{\text{total}} = 40 + 120 + 40 = 200\text{ m}$$

**Why this makes sense:** The car accelerates, cruises at constant speed, then decelerates. The displacement from the acceleration and deceleration phases are equal (both triangles have the same base and height), which is expected for symmetric acceleration and deceleration.

---

### Worked Example 1.4 — Projectile Motion (Horizontal Launch)

**Problem:** A ball rolls off a horizontal table $1.8\text{ m}$ high with a speed of $4.0\text{ m s}^{-1}$. Using $g = 10\text{ m s}^{-2}$, calculate: (a) the time the ball takes to hit the floor, and (b) the horizontal distance the ball travels before hitting the floor.

**Approach:** This is a horizontally-launched projectile. The vertical motion determines the time of flight because the initial vertical velocity is zero. The horizontal motion is at constant speed because there is no horizontal force. We treat the vertical and horizontal motions separately, connected only by the time $t$.

**Solution (a) — Vertical motion:**
$$s_y = u_y t + \frac{1}{2}a_y t^2$$
$$1.8 = 0 \times t + \frac{1}{2}(10)t^2$$
$$1.8 = 5t^2$$
$$t^2 = 0.36$$
$$t = 0.60\text{ s}$$

**Solution (b) — Horizontal motion:**
The horizontal velocity is constant at $4.0\text{ m s}^{-1}$.
$$R = v_x \times t = 4.0 \times 0.60 = 2.4\text{ m}$$

**Why this makes sense:** The table is relatively low (1.8 m), so the ball doesn't have much time to fall — only 0.6 seconds. In that time, at 4 m s⁻¹ horizontally, it travels about 2.4 metres. A higher table or a faster launch speed would give a longer range.

---

### Worked Example 1.5 — Projectile Motion (Angled Launch) — IB Style

**Problem:** A footballer kicks a ball from ground level with a speed of $25\text{ m s}^{-1}$ at an angle of $30^\circ$ above the horizontal. Using $g = 10\text{ m s}^{-2}$, calculate: (a) the time of flight, (b) the maximum height reached, and (c) the horizontal range.

**Approach:** First resolve the initial velocity into horizontal and vertical components. Then apply the projectile formulas for time of flight, maximum height, and range. The vertical motion determines the time; the horizontal motion uses that time to find range.

**Solution:**

Resolve initial velocity:
$$u_x = 25\cos 30^\circ = 25 \times \frac{\sqrt{3}}{2} = 21.7\text{ m s}^{-1}$$
$$u_y = 25\sin 30^\circ = 25 \times \frac{1}{2} = 12.5\text{ m s}^{-1}$$

**(a) Time of flight:**
At the highest point, the vertical velocity is momentarily zero. The time to reach the peak is found from $v_y = u_y - gt$, with $v_y = 0$ at the peak:
$$0 = 12.5 - 10t_{\text{up}}$$
$$t_{\text{up}} = 1.25\text{ s}$$

By symmetry (launch and landing at the same height), the total time of flight is twice the time to the peak:
$$T = 2 \times 1.25 = 2.50\text{ s}$$

Alternatively, using the formula: $T = \frac{2u\sin\theta}{g} = \frac{2(25)(0.5)}{10} = 2.50\text{ s}$.

**(b) Maximum height:**
Using $v_y^2 = u_y^2 - 2gH$ with $v_y = 0$ at the peak:
$$0 = (12.5)^2 - 2(10)H$$
$$20H = 156.25$$
$$H = 7.81\text{ m} \approx 7.8\text{ m}$$

**(c) Horizontal range:**
$$R = u_x \times T = 21.7 \times 2.50 = 54.3\text{ m}$$

Or using the formula: $R = \frac{u^2\sin(2\theta)}{g} = \frac{25^2\sin 60^\circ}{10} = \frac{625 \times 0.866}{10} = 54.1\text{ m}$.

(The small difference is due to rounding in $u_x$.)

**Why this makes sense:** At 25 m s⁻¹ (90 km/h, a strong kick), the ball stays in the air for 2.5 seconds and travels about 54 metres — roughly half a football pitch. The maximum height of about 8 metres is plausible for a lofted kick.

---

## Practice Problems

### Problem 1
A train starts from rest and accelerates uniformly at $2.0\text{ m s}^{-2}$ for $10$ seconds. It then continues at constant velocity for a further $20$ seconds. Calculate the total distance travelled by the train during the entire 30-second period.

### Problem 2
A cyclist is travelling at $8.0\text{ m s}^{-1}$ when she applies the brakes, producing a constant deceleration of $2.0\text{ m s}^{-2}$. (a) How long does it take for the cyclist to come to a complete stop? (b) How far does she travel during the braking period?

### Problem 3
A velocity–time graph for an object consists of three straight-line segments. From $t = 0$ to $t = 5\text{ s}$, the velocity increases uniformly from $0$ to $15\text{ m s}^{-1}$. From $t = 5\text{ s}$ to $t = 12\text{ s}$, the velocity remains constant at $15\text{ m s}^{-1}$. From $t = 12\text{ s}$ to $t = 15\text{ s}$, the velocity decreases uniformly from $15\text{ m s}^{-1}$ to $0$. (a) Sketch the velocity–time graph. (b) Calculate the acceleration during each of the three time intervals. (c) Calculate the total displacement of the object.

### Problem 4
A stone is thrown vertically upward from ground level with a speed of $30\text{ m s}^{-1}$. Using $g = 10\text{ m s}^{-2}$, calculate: (a) the maximum height reached by the stone, (b) the time taken to reach the maximum height, and (c) the total time before the stone returns to ground level. (d) Explain why the time to go up equals the time to come down, assuming no air resistance.

### Problem 5 — IB-Style Examination Question
A projectile is launched from ground level with an initial speed of $20\text{ m s}^{-1}$ at an angle of $60^\circ$ above the horizontal. The ground is level, and air resistance is negligible. The acceleration due to gravity is $g = 10\text{ m s}^{-2}$.

(a) Resolve the initial velocity into its horizontal and vertical components. (2 marks)

(b) Determine the time taken for the projectile to reach its maximum height. (2 marks)

(c) Calculate the maximum height reached by the projectile above the ground. (2 marks)

(d) Determine the total horizontal distance travelled by the projectile before it strikes the ground. (2 marks)

(e) On the same set of axes, sketch graphs of the horizontal velocity and the vertical velocity of the projectile from launch until it returns to the ground. Label each graph clearly. (3 marks)

---

## Answers

### Answer 1
The motion has two phases: acceleration and constant velocity.

**Phase 1 (0–10 s):** The train accelerates from rest. We know $u = 0$, $a = 2.0\text{ m s}^{-2}$, $t = 10\text{ s}$, and we need $s_1$. The missing quantity is $v$, so we use $s = ut + \frac{1}{2}at^2$.

$$s_1 = 0 \times 10 + \frac{1}{2}(2.0)(10)^2 = 0 + \frac{1}{2}(2.0)(100) = 100\text{ m}$$

At the end of phase 1, the train's velocity is $v = u + at = 0 + 2.0 \times 10 = 20\text{ m s}^{-1}$.

**Phase 2 (10–30 s):** The train moves at constant velocity $v = 20\text{ m s}^{-1}$ for $20$ seconds.

$$s_2 = v \times t = 20 \times 20 = 400\text{ m}$$

**Total distance:** $s_{\text{total}} = s_1 + s_2 = 100 + 400 = 500\text{ m}$.

A common mistake is to apply the SUVAT equation for the whole 30 seconds as if acceleration were constant throughout. It is not. You must treat the two phases separately because the acceleration changes at $t = 10\text{ s}$.

---

### Answer 2
The cyclist is decelerating, so $a = -2.0\text{ m s}^{-2}$ (negative because the acceleration opposes the direction of motion).

**(a) Time to stop:** We know $u = 8.0\text{ m s}^{-1}$, $v = 0$ (stopped), $a = -2.0\text{ m s}^{-2}$, and we need $t$. The missing quantity is $s$, so we use $v = u + at$.

$$0 = 8.0 + (-2.0)t$$
$$2.0t = 8.0$$
$$t = 4.0\text{ s}$$

**(b) Distance travelled during braking:** Now we know $t = 4.0\text{ s}$, so we can use $s = \frac{(u+v)}{2}t$.

$$s = \frac{(8.0 + 0)}{2} \times 4.0 = \frac{8.0}{2} \times 4.0 = 4.0 \times 4.0 = 16\text{ m}$$

We could also use $s = ut + \frac{1}{2}at^2$:
$$s = 8.0 \times 4.0 + \frac{1}{2}(-2.0)(4.0)^2 = 32 - 16 = 16\text{ m}$$

Both methods give the same answer, which is a good check. The cyclist travels 16 metres while braking to a stop.

A common mistake is to forget the negative sign for deceleration and write $a = +2.0$, which would give $t = -4.0\text{ s}$ — a negative time, which is physically impossible and should alert you that the sign is wrong.

---

### Answer 3
**(a)** The velocity–time graph has three segments: a straight line rising from $(0, 0)$ to $(5, 15)$; a horizontal line from $(5, 15)$ to $(12, 15)$; and a straight line falling from $(12, 15)$ to $(15, 0)$.

**(b) Acceleration (gradient of each segment):**

Segment 1 (0–5 s): $a_1 = \frac{\Delta v}{\Delta t} = \frac{15 - 0}{5 - 0} = 3.0\text{ m s}^{-2}$

Segment 2 (5–12 s): $a_2 = \frac{15 - 15}{12 - 5} = 0\text{ m s}^{-2}$ (constant velocity)

Segment 3 (12–15 s): $a_3 = \frac{0 - 15}{15 - 12} = -5.0\text{ m s}^{-2}$ (deceleration)

**(c) Total displacement (area under the graph):**

Area of first triangle: $\frac{1}{2} \times 5 \times 15 = 37.5\text{ m}$

Area of rectangle: $7 \times 15 = 105\text{ m}$

Area of second triangle: $\frac{1}{2} \times 3 \times 15 = 22.5\text{ m}$

Total displacement: $37.5 + 105 + 22.5 = 165\text{ m}$

---

### Answer 4
**(a)** At maximum height, the vertical velocity is momentarily zero. Using $v^2 = u^2 + 2as$ with $v = 0$, $u = 30\text{ m s}^{-1}$, $a = -10\text{ m s}^{-2}$ (gravity opposes the upward motion):

$$0 = 30^2 + 2(-10)H$$
$$0 = 900 - 20H$$
$$20H = 900$$
$$H = 45\text{ m}$$

**(b)** Using $v = u + at$ with $v = 0$ at the peak:

$$0 = 30 + (-10)t_{\text{up}}$$
$$10t_{\text{up}} = 30$$
$$t_{\text{up}} = 3.0\text{ s}$$

**(c)** By symmetry, the time to come down equals the time to go up, so total time is $6.0\text{ s}$.

We can verify this independently. For the downward journey from height 45 m: $s = ut + \frac{1}{2}at^2$ with $u = 0$ (starting from rest at the peak), $s = 45\text{ m}$, $a = +10\text{ m s}^{-2}$ (now downward is positive):

$$45 = 0 \times t + \frac{1}{2}(10)t_{\text{down}}^2$$
$$45 = 5t_{\text{down}}^2$$
$$t_{\text{down}}^2 = 9$$
$$t_{\text{down}} = 3.0\text{ s}$$

Total time: $t_{\text{up}} + t_{\text{down}} = 3.0 + 3.0 = 6.0\text{ s}$.

**(d)** Without air resistance, the only force acting on the stone throughout its flight is gravity, which is constant and downward. The upward journey and downward journey are mirror images: the stone leaves the ground at $+30\text{ m s}^{-1}$ and returns at $-30\text{ m s}^{-1}$, with the speed at any given height being the same on the way up and the way down. Since the acceleration is the same ($-10\text{ m s}^{-2}$ throughout), the time to lose $30\text{ m s}^{-1}$ going up equals the time to gain $30\text{ m s}^{-1}$ coming down.

---

### Answer 5 — IB-Style Full Solution with Mark Scheme

**(a) Resolve initial velocity into components (2 marks)**

Horizontal component: $u_x = u\cos\theta = 20\cos 60^\circ = 20 \times 0.50 = 10\text{ m s}^{-1}$. (1 mark for correct calculation)

Vertical component: $u_y = u\sin\theta = 20\sin 60^\circ = 20 \times \frac{\sqrt{3}}{2} = 20 \times 0.866 = 17.3\text{ m s}^{-1}$. (1 mark for correct calculation)

Award 1 mark for each correct component. Accept $17\text{ m s}^{-1}$ or $17.3\text{ m s}^{-1}$ for the vertical component.

**(b) Time to maximum height (2 marks)**

At maximum height, the vertical component of velocity is zero. Using $v_y = u_y - gt$ with $v_y = 0$:
$$0 = 17.3 - 10t$$
$$t = 1.73\text{ s} \approx 1.7\text{ s}$$

1 mark for recognising that $v_y = 0$ at maximum height. 1 mark for correct substitution and answer. Accept answers between $1.7$ and $1.73$ seconds.

**(c) Maximum height (2 marks)**

Using $v_y^2 = u_y^2 - 2gH$ with $v_y = 0$ at the peak:
$$0 = (17.3)^2 - 2(10)H$$
$$20H = 299.3$$
$$H = 15.0\text{ m}$$

1 mark for correct equation selection. 1 mark for correct answer with unit. Accept $15.0\text{ m}$ or $15\text{ m}$.

Alternatively, using $H = u_y t - \frac{1}{2}gt^2$ with $t = 1.73\text{ s}$: $H = 17.3(1.73) - 5(1.73)^2 = 29.9 - 15.0 = 14.9\text{ m}$. Accept either method.

**(d) Horizontal range (2 marks)**

The total time of flight is twice the time to maximum height: $T = 2 \times 1.73 = 3.46\text{ s}$.

Horizontal range: $R = u_x \times T = 10 \times 3.46 = 34.6\text{ m} \approx 35\text{ m}$.

1 mark for recognising that total time is twice the time to peak (or for using the range formula $R = u^2\sin(2\theta)/g$). 1 mark for correct answer with unit.

Using the range formula: $R = \frac{20^2\sin(120^\circ)}{10} = \frac{400 \times 0.866}{10} = 34.6\text{ m}$. This also receives full credit.

**(e) Velocity–time graphs (3 marks)**

The horizontal velocity graph is a horizontal straight line at $v_x = 10\text{ m s}^{-1}$ from $t = 0$ to $t = 3.46\text{ s}$. (1 mark for correct constant value)

The vertical velocity graph is a straight line starting at $v_y = +17.3\text{ m s}^{-1}$ at $t = 0$, crossing through zero at $t = 1.73\text{ s}$, and ending at $v_y = -17.3\text{ m s}^{-1}$ at $t = 3.46\text{ s}$. (1 mark for correct intercepts and zero-crossing, 1 mark for straight line showing constant gradient)

The gradient of the vertical velocity graph should be $-10\text{ m s}^{-2}$. Both graphs should be clearly labelled to distinguish them.

---

## Key Takeaways

1. **SUVAT equations only work for constant acceleration.** If acceleration changes during the motion, split the problem into phases, each with constant acceleration.

2. **Choose the SUVAT equation by identifying the missing quantity.** Write down what you know ($s$, $u$, $v$, $a$, $t$) and what you need. The quantity that appears nowhere in the problem tells you which equation to use.

3. **Velocity–time graphs are the most powerful motion graph.** The gradient gives acceleration, the area gives displacement, and the y-value gives instantaneous velocity — three quantities from one graph.

4. **Projectile motion = independent horizontal and vertical motions.** Horizontal velocity is constant. Vertical motion follows SUVAT with $a = -g$. Time is the only link between them.

5. **Sign conventions matter.** Choose a direction as positive at the start of every problem and stick to it. Velocities and accelerations in the opposite direction get negative signs.
