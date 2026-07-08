# Lesson 8: Rigid Body Mechanics III — Angular Momentum (HL)

## What You'll Learn
- Define angular momentum $L = I\omega$ and understand conservation of angular momentum
- Calculate rotational kinetic energy $E_k = \frac{1}{2}I\omega^2$
- Apply $v = \omega r$ for rolling without slipping
- Analyse collisions and interactions using angular momentum conservation

---

## 1. Angular Momentum — The Spinning Twin of Linear Momentum

### 1.1 What Is Angular Momentum?

Just as linear momentum $p = mv$ measures "how much motion" an object has in a straight line, angular momentum $L$ measures "how much rotational motion" an object has about an axis:

$$L = I\omega$$

where $I$ is moment of inertia and $\omega$ is angular velocity (rad s⁻¹). Units: $\text{kg m}^2\text{ s}^{-1}$.

### 1.2 Conservation of Angular Momentum

If no external torque acts on a system, its total angular momentum is conserved:

$$I_1\omega_1 = I_2\omega_2$$

This is an exact analogue of conservation of linear momentum ($m_1u_1 + m_2u_2 = m_1v_1 + m_2v_2$). It holds whenever the net external torque is zero.

### 1.3 The Ice Skater Effect

An ice skater spinning with arms extended has a large $I$ (arms far from axis). When she pulls her arms in, $I$ decreases dramatically. Since $L = I\omega$ must stay constant, $\omega$ increases — she spins faster. The product $I\omega$ before equals $I\omega$ after. No external torque is applied; she does internal work to pull her arms in, which increases her rotational kinetic energy.

This effect is everywhere in physics: neutron stars spinning faster as they collapse, divers tucking to increase rotation speed, cats twisting to land on their feet.

---

## 2. Rotational Kinetic Energy

### 2.1 The Formula

A rotating object has kinetic energy because its mass is in motion:

$$E_{k,\text{rot}} = \frac{1}{2}I\omega^2$$

This is the rotational analogue of $\frac{1}{2}mv^2$, with $I$ replacing $m$ and $\omega$ replacing $v$.

### 2.2 Rolling Without Slipping — Total Kinetic Energy

When an object rolls without slipping, it has BOTH translational and rotational kinetic energy. The condition $v = \omega r$ (or more precisely, $v_{\text{CM}} = \omega r$) links the two:

$$E_{k,\text{total}} = \frac{1}{2}mv^2 + \frac{1}{2}I\omega^2$$

Substituting $\omega = v/r$:
$$E_{k,\text{total}} = \frac{1}{2}mv^2 + \frac{1}{2}I\frac{v^2}{r^2} = \frac{1}{2}v^2\left(m + \frac{I}{r^2}\right)$$

This is why objects with different $I$ roll at different speeds — the effective inertia for acceleration includes both translational and rotational terms.

---

## 3. The Second Rotational Law — Torque as Rate of Change of Angular Momentum

In its most general form, Newton's Second Law for rotation is:

$$\tau = \frac{\Delta L}{\Delta t}$$

This is exactly analogous to $F = \Delta p/\Delta t$. Torque is the rate of change of angular momentum, just as force is the rate of change of linear momentum. When $I$ is constant, $\tau = I\alpha$ is a special case of this more general law.

---

## 4. Collisions Involving Rotation

When objects collide and one or both are rotating, both linear AND angular momentum may be conserved:
- $\Sigma p$ before = $\Sigma p$ after (if no external forces)
- $\Sigma L$ before = $\Sigma L$ after (if no external torques)

These are independent conservation laws and must be applied separately.

---

## Worked Examples

### Worked Example 8.1 — Ice Skater

**Problem:** An ice skater spins at $3.0\text{ rad s}^{-1}$ with arms extended, giving $I = 4.0\text{ kg m}^2$. She pulls her arms in, reducing $I$ to $1.5\text{ kg m}^2$. Find her new angular speed and the ratio of her final to initial rotational KE.

**Solution:**
$I_1\omega_1 = I_2\omega_2$, so $\omega_2 = (4.0)(3.0)/(1.5) = 8.0\text{ rad s}^{-1}$.

$E_{k1} = \frac{1}{2}(4.0)(3.0)^2 = 18\text{ J}$. $E_{k2} = \frac{1}{2}(1.5)(8.0)^2 = 48\text{ J}$. Ratio = $48/18 = 2.67$.

**Why the increase in KE?** The skater does work pulling her arms inward against centrifugal forces. That work becomes additional rotational kinetic energy. Angular momentum is conserved; energy is not (because internal work was done).

---

### Worked Example 8.2 — Disk Dropped onto Rotating Disk

**Problem:** A disk ($I_1 = 0.20\text{ kg m}^2$) rotates at $12\text{ rad s}^{-1}$. A second identical disk, initially not rotating, is dropped onto it and they stick together. Find the final angular speed.

**Approach:** Angular momentum is conserved (no external torque about the axis). Final $I = I_1 + I_2 = 0.40\text{ kg m}^2$.

**Solution:**
$I_1\omega_1 = (I_1 + I_2)\omega_f$, so $\omega_f = (0.20)(12)/(0.40) = 6.0\text{ rad s}^{-1}$.

**Note:** Kinetic energy is NOT conserved — the final KE ($\frac{1}{2}(0.40)(6.0)^2 = 7.2\text{ J}$) is half the initial KE ($\frac{1}{2}(0.20)(12)^2 = 14.4\text{ J}$). Energy is lost as heat during the sticking collision. This is the rotational analogue of a perfectly inelastic collision.

---

### Worked Example 8.3 — Rolling Down an Incline (Energy Method)

**Problem:** A solid sphere ($m = 3.0\text{ kg}$, $r = 0.20\text{ m}$) rolls without slipping from rest down an incline of vertical height $2.0\text{ m}$. Find its speed at the bottom using $g = 10\text{ m s}^{-2}$.

**Approach:** Energy conservation. Initial GPE converts to translational + rotational KE. For a solid sphere, $I = \frac{2}{5}mr^2$, and $\omega = v/r$.

**Solution:**
$$mgh = \frac{1}{2}mv^2 + \frac{1}{2}I\omega^2 = \frac{1}{2}mv^2 + \frac{1}{2}\left(\frac{2}{5}mr^2\right)\left(\frac{v}{r}\right)^2 = \frac{1}{2}mv^2 + \frac{1}{5}mv^2 = \frac{7}{10}mv^2$$

$$(3.0)(10)(2.0) = \frac{7}{10}(3.0)v^2$$
$$60 = 2.1v^2$$
$$v = \sqrt{28.6} = 5.35\text{ m s}^{-1}$$

**Compare:** If the sphere slid without friction (no rotation), $v = \sqrt{2gh} = \sqrt{40} = 6.32\text{ m s}^{-1}$. The rolling sphere is slower because some energy goes into rotation.

---

## Practice Problems

### Problem 1
A diver can change her moment of inertia from $12\text{ kg m}^2$ to $3.0\text{ kg m}^2$ by tucking. If she leaves the board spinning at $1.5\text{ rad s}^{-1}$, what is her angular speed in the tuck position?

### Problem 2
A solid disk ($m = 2.0\text{ kg}$, $r = 0.30\text{ m}$) rotates at $20\text{ rad s}^{-1}$ on a frictionless axle. A second disk ($m = 1.0\text{ kg}$, $r = 0.20\text{ m}$) initially at rest is dropped on top and they stick. Find the final angular speed.

### Problem 3
A hollow sphere ($I = \frac{2}{3}mr^2$) and a solid sphere ($I = \frac{2}{5}mr^2$) of equal mass and radius roll down the same incline from rest. Calculate the ratio of their final speeds.

### Problem 4
Explain why Earth's rotation is gradually slowing down (the day is getting longer by about 1.7 milliseconds per century). Use conservation of angular momentum.

### Problem 5 — IB-Style
A playground roundabout (solid disk, $m = 150\text{ kg}$, $r = 1.5\text{ m}$) is initially rotating at $2.0\text{ rad s}^{-1}$. A child of mass $40\text{ kg}$ jumps onto the edge of the roundabout.

(a) Calculate the moment of inertia of the roundabout. (1 mark)
(b) Determine the total angular momentum before the child jumps on. (2 marks)
(c) Calculate the new angular speed after the child lands. Treat the child as a point mass. (3 marks)
(d) Determine the ratio (final rotational KE)/(initial rotational KE) and account for any energy change. (2 marks)

---

## Answers

### Answer 1
$I_1\omega_1 = I_2\omega_2$. $\omega_2 = (12)(1.5)/(3.0) = 6.0\text{ rad s}^{-1}$.

### Answer 2
$I_1 = \frac{1}{2}(2.0)(0.30)^2 = 0.090\text{ kg m}^2$. $I_2 = \frac{1}{2}(1.0)(0.20)^2 = 0.020\text{ kg m}^2$. $\omega_f = (0.090)(20)/(0.110) = 16.4\text{ rad s}^{-1}$.

### Answer 3
$mgh = \frac{1}{2}mv^2 + \frac{1}{2}I\omega^2$. Solid: $\frac{7}{10}mv^2$, $v_s = \sqrt{10gh/7}$. Hollow: $\frac{1}{2}mv^2 + \frac{1}{3}mv^2 = \frac{5}{6}mv^2$, $v_h = \sqrt{6gh/5}$. Ratio $v_s/v_h = \sqrt{10gh/7} / \sqrt{6gh/5} = \sqrt{50/42} = 1.09$. Solid sphere is 9% faster.

### Answer 4
Tidal friction between Earth and Moon transfers angular momentum from Earth's rotation to the Moon's orbit. Earth's $I\omega$ decreases → $\omega$ decreases → day lengthens. The Moon gains orbital angular momentum and recedes from Earth (~3.8 cm/year). Total angular momentum of Earth-Moon system is conserved.

### Answer 5 — IB-Style
**(a)** $I = \frac{1}{2}mr^2 = \frac{1}{2}(150)(1.5)^2 = 169\text{ kg m}^2$. (1 mark)

**(b)** $L = I\omega = (169)(2.0) = 338\text{ kg m}^2\text{ s}^{-1}$. (2 marks — 1 for L formula, 1 for value.)

**(c)** (3 marks) Child as point mass: $I_{\text{child}} = mr^2 = (40)(1.5)^2 = 90\text{ kg m}^2$. Total $I_f = 169 + 90 = 259\text{ kg m}^2$. $L$ conserved: $\omega_f = L/I_f = 338/259 = 1.31\text{ rad s}^{-1}$. (1 for child's I, 1 for total I, 1 for final ω.)

**(d)** (2 marks) Initial KE $= \frac{1}{2}(169)(2.0)^2 = 338\text{ J}$. Final KE $= \frac{1}{2}(259)(1.31)^2 = 222\text{ J}$. Ratio $= 222/338 = 0.66$. Energy decreased — this is an inelastic "collision" where the child and roundabout come to a common angular speed. Energy is dissipated as thermal energy in the child's muscles and the impact.

---

## Key Takeaways

1. **Angular momentum:** $L = I\omega$. Conserved when net external torque is zero.

2. **Rotational KE:** $E_k = \frac{1}{2}I\omega^2$. Total KE for rolling = translational + rotational.

3. **Ice skater principle:** Decreasing $I$ increases $\omega$ to conserve $L$. Internal work increases KE.

4. **Rolling without slipping:** $v_{\text{CM}} = \omega r$. The link between translation and rotation.

5. **In collisions with sticking:** $L$ is conserved, KE is NOT (some converted to thermal energy).
