# Lesson 7: Rigid Body Mechanics II — Moment of Inertia (HL)

## What You'll Learn
- Define moment of inertia and understand why it depends on mass distribution
- Recall moments of inertia for common shapes from the Data Booklet
- Apply $\tau = I\alpha$ to calculate angular acceleration
- Use the parallel axis theorem for off-centre rotation

---

## 1. Moment of Inertia — Rotational "Mass"

### 1.1 Why Mass Isn't Enough for Rotation

In linear motion, mass tells you how hard it is to accelerate an object: $F = ma$. A 10 kg mass resists acceleration ten times as much as a 1 kg mass. But in rotation, it's not just how MUCH mass you have — it's WHERE that mass is located relative to the axis of rotation.

Imagine two wheels of equal mass. One has all its mass concentrated at the hub. The other has all its mass at the rim. Which is harder to spin up? The rim-heavy wheel — because the mass is further from the axis. The mass at the rim moves faster for a given angular speed, so it has more kinetic energy and requires more work to accelerate.

This resistance to rotational acceleration is **moment of inertia**, symbol $I$.

### 1.2 Definition

For a system of point masses:
$$I = \Sigma m_i r_i^2$$

where $m_i$ is each mass and $r_i$ is its perpendicular distance from the axis of rotation. For continuous objects, this sum becomes an integral, but at IB level you are given the results for common shapes in the Data Booklet.

The unit of moment of inertia is $\text{kg m}^2$.

### 1.3 Why the $r^2$ Dependence?

Mass twice as far from the axis contributes FOUR times as much to $I$. This is because:
- The mass moves twice as fast (for the same $\omega$, $v = \omega r$), so it has four times the kinetic energy ($\frac{1}{2}mv^2$)
- The torque needed to produce a given angular acceleration is larger because the force must act over a larger radius

This $r^2$ dependence is why flywheels store energy in heavy rims, why ice skaters spin faster by pulling their arms in, and why a solid cylinder rolls down an incline faster than a hollow cylinder of the same mass and radius.

---

## 2. Moments of Inertia — Data Booklet Values

These are in the IB Data Booklet. You need to recognise the shape and know which axis the formula applies to:

| Object | Axis | Moment of Inertia $I$ |
|--------|------|----------------------|
| Point mass $m$ | Distance $r$ from axis | $mr^2$ |
| Thin hoop / cylindrical shell | Through centre, perpendicular to plane | $mr^2$ |
| Solid cylinder / disk | Through centre, perpendicular to plane | $\frac{1}{2}mr^2$ |
| Thin spherical shell | Through centre | $\frac{2}{3}mr^2$ |
| Solid sphere | Through centre | $\frac{2}{5}mr^2$ |
| Thin rod, length $L$ | Through centre, perpendicular | $\frac{1}{12}mL^2$ |
| Thin rod, length $L$ | Through end, perpendicular | $\frac{1}{3}mL^2$ |

Notice: $I$ always has the form (constant) × $mr^2$ or $mL^2$. The constant tells you how the mass is distributed:
- Hoop: all mass at the rim → constant = 1 (maximum for a given radius)
- Solid disk: mass distributed from centre to rim → constant = $\frac{1}{2}$
- Solid sphere: mass concentrated toward centre → constant = $\frac{2}{5}$ (least for a given radius)

---

## 3. The Rotational Second Law — $\tau = I\alpha$

### 3.1 The Analogy

Newton's Second Law for rotation:
$$\tau = I\alpha$$

where $\tau$ is net torque (N m), $I$ is moment of inertia (kg m²), and $\alpha$ is angular acceleration (rad s⁻²). This is the exact rotational analogue of $F = ma$, with torque replacing force, moment of inertia replacing mass, and angular acceleration replacing linear acceleration.

### 3.2 The Complete Analogy

| Linear | Rotational | Relationship |
|--------|------------|--------------|
| Force $F$ | Torque $\tau$ | $\tau = Fr\sin\theta$ |
| Mass $m$ | Moment of inertia $I$ | $I = \Sigma mr^2$ |
| Acceleration $a$ | Angular acceleration $\alpha$ | $a = \alpha r$ |
| $F = ma$ | $\tau = I\alpha$ | — |

---

## 4. The Parallel Axis Theorem

### 4.1 When the Axis Isn't Through the Centre

The Data Booklet gives $I$ for axes through the centre of mass. What if the rotation axis is somewhere else? The parallel axis theorem:

$$I = I_{\text{CM}} + Md^2$$

where $I_{\text{CM}}$ is the moment of inertia about an axis through the centre of mass parallel to the desired axis, $M$ is the total mass, and $d$ is the perpendicular distance between the two axes.

**Example:** A rod rotating about its end. $I_{\text{CM}} = \frac{1}{12}ML^2$ (centre). Shift by $d = L/2$. $I = \frac{1}{12}ML^2 + M(L/2)^2 = \frac{1}{12}ML^2 + \frac{1}{4}ML^2 = \frac{1}{3}ML^2$ — matching the Data Booklet value.

---

## Worked Examples

### Worked Example 7.1 — System of Point Masses

**Problem:** Two 2.0 kg masses are fixed to the ends of a light rod 1.0 m long. Find $I$ about (a) the centre, and (b) one end.

**Solution (a):** Each mass is 0.50 m from centre. $I = 2 \times (2.0)(0.50)^2 = 1.0\text{ kg m}^2$.
**(b):** One mass at $r = 0$, other at $r = 1.0\text{ m}$. $I = (2.0)(1.0)^2 = 2.0\text{ kg m}^2$.

---

### Worked Example 7.2 — Angular Acceleration from Torque

**Problem:** A torque of $6.0\text{ N m}$ is applied to a solid disk of mass $4.0\text{ kg}$ and radius $0.50\text{ m}$. Find the angular acceleration.

**Solution:**
$I = \frac{1}{2}mr^2 = \frac{1}{2}(4.0)(0.50)^2 = 0.50\text{ kg m}^2$. $\alpha = \tau/I = 6.0/0.50 = 12\text{ rad s}^{-2}$.

---

### Worked Example 7.3 — Rolling vs. Sliding

**Problem:** A solid sphere and a hollow sphere of equal mass and radius roll down an incline. Which reaches the bottom first?

**Approach:** Compare $I$ values. Solid sphere: $\frac{2}{5}mr^2$. Hollow sphere: $\frac{2}{3}mr^2$. Less $I$ means less energy stored in rotation, more in translation, so faster linear speed.

**Solution:** The solid sphere ($I = \frac{2}{5}mr^2$) has less moment of inertia, so more of its gravitational potential energy converts to translational KE rather than rotational KE. It reaches the bottom first. The hollow sphere stores more energy in rotation.

---

### Worked Example 7.4 — Parallel Axis Theorem (IB-Style)

**Problem:** A thin uniform rod of mass $0.60\text{ kg}$ and length $1.2\text{ m}$ rotates about an axis perpendicular to the rod, passing through a point $0.30\text{ m}$ from one end. Calculate the moment of inertia.

**Solution:**
$I_{\text{CM}} = \frac{1}{12}ML^2 = \frac{1}{12}(0.60)(1.2)^2 = 0.072\text{ kg m}^2$. Distance from CM (at 0.60 m from either end) to axis (0.30 m from one end): $d = 0.60 - 0.30 = 0.30\text{ m}$. $I = 0.072 + (0.60)(0.30)^2 = 0.072 + 0.054 = 0.126\text{ kg m}^2$.

---

## Practice Problems

### Problem 1
Three 1.0 kg masses are placed at $(0, 0)$, $(2.0, 0)$, and $(0, 1.5)$ metres. Find the moment of inertia about the origin.

### Problem 2
A solid disk of mass 5.0 kg and radius 0.40 m experiences a net torque of 8.0 N m. Find the angular acceleration and the tangential acceleration of a point on the rim.

### Problem 3
A torque of 12 N m accelerates a hoop from rest to 30 rad s⁻¹ in 5.0 s. Find the mass of the hoop if its radius is 0.60 m.

### Problem 4
Explain why a tightrope walker carries a long pole. Use the concept of moment of inertia.

### Problem 5 — IB-Style
A solid cylinder ($m = 2.0\text{ kg}$, $r = 0.10\text{ m}$) rolls without slipping down an incline from rest. The vertical height descended is $1.5\text{ m}$. Use $g = 10\text{ m s}^{-2}$.

(a) Write expressions for the translational and rotational kinetic energy in terms of $v$ and the cylinder parameters. (2 marks)
(b) Using energy conservation, calculate the final linear speed $v$ at the bottom. (3 marks)
(c) A hollow cylinder with equal mass and radius rolls down the same incline. Without calculation, state whether it will reach the bottom at a higher or lower speed, and explain why. (2 marks)
(d) Calculate the angular speed of the solid cylinder at the bottom. (1 mark)

---

## Answers

### Answer 1
$I = (1.0)(0)^2 + (1.0)(2.0)^2 + (1.0)(1.5)^2 = 0 + 4.0 + 2.25 = 6.25\text{ kg m}^2$.

### Answer 2
$I = \frac{1}{2}(5.0)(0.40)^2 = 0.40\text{ kg m}^2$. $\alpha = 8.0/0.40 = 20\text{ rad s}^{-2}$. $a_t = \alpha r = 20 \times 0.40 = 8.0\text{ m s}^{-2}$.

### Answer 3
$\alpha = \Delta\omega/t = 30/5.0 = 6.0\text{ rad s}^{-2}$. $I = \tau/\alpha = 12/6.0 = 2.0\text{ kg m}^2$. For hoop: $I = mr^2$, so $m = 2.0/0.36 = 5.56\text{ kg}$.

### Answer 4
The pole has a large moment of inertia about the walker's centre of mass (mass is far from the axis). $\tau = I\alpha$ — for a given disturbing torque (from wind or imbalance), a large $I$ produces a small $\alpha$, giving the walker more time to correct their balance. The pole resists angular acceleration, making tipping motions slower and more controllable.

### Answer 5 — IB-Style
**(a)** (2 marks) Translation: $\frac{1}{2}mv^2$. Rotation: $\frac{1}{2}I\omega^2$. For solid cylinder, $I = \frac{1}{2}mr^2$, and rolling without slipping: $\omega = v/r$, so rotational KE $= \frac{1}{2}(\frac{1}{2}mr^2)(v/r)^2 = \frac{1}{4}mv^2$. Total KE $= \frac{1}{2}mv^2 + \frac{1}{4}mv^2 = \frac{3}{4}mv^2$.

**(b)** (3 marks) $mgh = \frac{3}{4}mv^2$. $v = \sqrt{4gh/3} = \sqrt{4(10)(1.5)/3} = \sqrt{20} = 4.47\text{ m s}^{-1}$. (1 for energy conservation, 1 for total KE expression, 1 for answer.)

**(c)** (2 marks) Lower speed. Hollow cylinder has $I = mr^2$ (all mass at rim), so rotational KE $= \frac{1}{2}mv^2$ and total KE $= mv^2$. More energy goes into rotation, leaving less for translation. $v_{\text{hollow}} = \sqrt{gh}$ vs. $v_{\text{solid}} = \sqrt{4gh/3}$ — hollow is slower.

**(d)** $\omega = v/r = 4.47/0.10 = 44.7\text{ rad s}^{-1}$. (1 mark)

---

## Key Takeaways

1. **Moment of inertia** $I = \Sigma mr^2$ is the rotational analogue of mass. It depends on mass AND distribution.

2. **Data Booklet** gives $I$ for common shapes about their centres. Know which constant goes with which shape.

3. **$\tau = I\alpha$** — torque causes angular acceleration in exact analogy to $F = ma$.

4. **Parallel axis theorem:** $I = I_{\text{CM}} + Md^2$. For off-centre axes, add $Md^2$ to the centre-of-mass value.

5. **Rolling without slipping:** $v = \omega r$, and KE splits between translation and rotation. More $I$ → more energy in rotation → slower linear speed.
