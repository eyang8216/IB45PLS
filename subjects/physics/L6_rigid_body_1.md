# Lesson 6: Rigid Body Mechanics I — Torque and Static Equilibrium (HL)

## What You'll Learn
- Define torque and understand why it depends on both force and lever arm
- Calculate torque using $\tau = Fr\sin\theta$
- Apply the two conditions for static equilibrium: $\Sigma F = 0$ and $\Sigma\tau = 0$
- Solve equilibrium problems involving beams, ladders, and seesaws

---

## 1. What Is Torque?

### 1.1 Why Forces Aren't Enough

In Lessons 2–4, we treated every object as a point particle. A force applied to a point particle causes it to accelerate in a straight line. But real objects are extended — they have size and shape. Apply a force to an extended object, and it might not just translate; it might also **rotate**.

Torque is the rotational analogue of force. Just as a net force causes linear acceleration ($F = ma$), a net torque causes angular acceleration ($\tau = I\alpha$). And just as forces can balance to produce equilibrium ($\Sigma F = 0$), torques can balance to prevent rotation ($\Sigma\tau = 0$).

Understanding torque is essential for everything from tightening a bolt (why a longer wrench works better) to designing bridges (why forces must be placed carefully to prevent collapse).

### 1.2 The Definition

Torque is the ability of a force to cause rotation about a pivot point:

$$\tau = Fr\sin\theta$$

where:
- $F$ is the magnitude of the applied force (N)
- $r$ is the distance from the pivot to the point where the force is applied (m) — called the **lever arm** or **moment arm**
- $\theta$ is the angle between the force vector and the line from the pivot to the point of application

The unit of torque is the newton-metre (N m). Do not confuse this with joules — torque is not energy. They share the same base units but measure fundamentally different things.

### 1.3 Understanding the Sine Factor

The factor $\sin\theta$ accounts for the fact that only the **perpendicular component** of the force produces rotation. A force applied parallel to the lever arm ($\theta = 0^\circ$ or $180^\circ$) produces zero torque — it pulls directly toward or away from the pivot and cannot cause rotation. A force applied perpendicular to the lever arm ($\theta = 90^\circ$) produces maximum torque — every newton of force goes into causing rotation.

You can think of torque in two equivalent ways, which is useful for problem-solving:
- $\tau = F(r\sin\theta)$ — the force $F$ times the perpendicular distance from the pivot to the line of action of the force
- $\tau = r(F\sin\theta)$ — the distance $r$ times the perpendicular component of the force

### 1.4 Sign Convention

Torque can be clockwise or counterclockwise. Choose one direction as positive and be consistent throughout the problem. If you define counterclockwise as positive, then a force that tends to rotate the object counterclockwise produces a positive torque.

---

## 2. Static Equilibrium — When Nothing Moves

### 2.1 The Two Conditions

For an extended object to be in **static equilibrium** (completely at rest, no translation, no rotation), two conditions must be satisfied simultaneously:

**Condition 1 — No net force (translational equilibrium):**
$$\Sigma F_x = 0 \quad \text{and} \quad \Sigma F_y = 0$$

The vector sum of all forces acting on the object must be zero. If this were not true, the object would accelerate in a straight line.

**Condition 2 — No net torque (rotational equilibrium):**
$$\Sigma\tau = 0$$

The sum of all torques about ANY axis must be zero. If this were not true, the object would undergo angular acceleration (start spinning).

### 2.2 Why "About Any Axis"?

A remarkable property of static equilibrium: if the net torque is zero about one axis, it is zero about ALL axes. This means you can choose whichever pivot point makes the problem easiest. The standard strategy is to choose the pivot at a point where an unknown force acts — that way, the unknown force produces zero torque about that point (since $r = 0$) and disappears from the torque equation.

### 2.3 The Centre of Mass and Centre of Gravity

The weight of an extended object acts as if it is concentrated at a single point called the **centre of gravity**. For uniform objects in a uniform gravitational field, the centre of gravity is at the geometric centre. For a uniform rod, it's at the midpoint. For a uniform rectangular block, it's at the intersection of the diagonals.

When calculating torques due to weight, treat the entire weight $mg$ as acting at the centre of gravity, with the lever arm being the horizontal distance from the pivot to that point.

---

## 3. Couples — Pure Rotation

A **couple** is a pair of equal and opposite forces whose lines of action do not coincide. Because the net force is zero, a couple produces no translation. But because the forces are separated by a perpendicular distance $d$, they produce a net torque:

$$\tau = Fd$$

A couple produces pure rotation — a steering wheel being turned, a tap being opened, a compass needle aligning with a magnetic field.

---

## Worked Examples

### Worked Example 6.1 — Torque on a Wrench

**Problem:** A mechanic applies a force of $80\text{ N}$ to the end of a $0.30\text{ m}$ wrench at an angle of $60^\circ$ to the wrench handle. Calculate the torque about the bolt.

**Approach:** Use $\tau = Fr\sin\theta$ with $r = 0.30\text{ m}$, $F = 80\text{ N}$, $\theta = 60^\circ$.

**Solution:**
$$\tau = (80)(0.30)\sin 60^\circ = 24 \times 0.866 = 20.8\text{ N m}$$

**Why this makes sense:** If the force were perpendicular ($90^\circ$), $\tau = 24\text{ N m}$. At $60^\circ$, we get $87\%$ of the maximum — typical for someone pulling at a comfortable angle.

---

### Worked Example 6.2 — Beam Supported at Both Ends

**Problem:** A uniform beam of length $4.0\text{ m}$ and weight $300\text{ N}$ rests on two supports, one at each end. A $200\text{ N}$ weight is placed $1.0\text{ m}$ from the left end. Calculate the upward forces from the two supports.

**Approach:** The beam is in static equilibrium. Two unknown support forces: $F_L$ (left) and $F_R$ (right). Use $\Sigma F_y = 0$ and $\Sigma\tau = 0$. Choose the pivot at the left support to eliminate $F_L$ from the torque equation.

**Solution:**

$\Sigma F_y = 0$: $F_L + F_R - 300 - 200 = 0$, so $F_L + F_R = 500\text{ N}$. (Equation 1)

$\Sigma\tau = 0$ about left support (counterclockwise positive):
- $F_L$: torque = $0$ (at pivot)
- Beam weight ($300\text{ N}$ at $2.0\text{ m}$ from left): torque = $-(300)(2.0) = -600\text{ N m}$ (clockwise)
- Placed weight ($200\text{ N}$ at $1.0\text{ m}$): torque = $-(200)(1.0) = -200\text{ N m}$
- $F_R$ at $4.0\text{ m}$: torque = $+F_R(4.0) = 4.0F_R$ (counterclockwise)

Sum: $-600 - 200 + 4.0F_R = 0$, so $4.0F_R = 800$, $F_R = 200\text{ N}$.

From Equation 1: $F_L = 500 - 200 = 300\text{ N}$.

**Why this makes sense:** The beam's weight (300 N) is centred, so half goes to each support (150 N each from the beam). The 200 N weight is closer to the left, so the left support bears more of it. Total left: $150 + 150 = 300\text{ N}$. Total right: $150 + 50 = 200\text{ N}$. Checks out.

---

### Worked Example 6.3 — Ladder Against a Wall

**Problem:** A uniform ladder of length $5.0\text{ m}$ and weight $400\text{ N}$ leans against a smooth vertical wall at an angle such that its base is $3.0\text{ m}$ from the wall. There is no friction at the wall; the ground provides both normal force and friction. Calculate: (a) the reaction force from the wall, and (b) the friction force at the ground.

**Approach:** The wall has no friction, so its force is purely horizontal ($R_w$). The ground has normal force $N$ (vertical) and friction $f$ (horizontal). Four unknowns. Use both force conditions and a torque condition. Choose pivot at the base.

**Solution:**

Geometry: height of ladder top = $\sqrt{5.0^2 - 3.0^2} = 4.0\text{ m}$.

$\Sigma F_x = 0$: $R_w - f = 0$, so $f = R_w$. (Equation 1)
$\Sigma F_y = 0$: $N - 400 = 0$, so $N = 400\text{ N}$. (Equation 2)

$\Sigma\tau = 0$ about base (counterclockwise positive):
- $N$, $f$: torque = 0 (at pivot)
- Weight at $1.5\text{ m}$ horizontal from base (half of $3.0\text{ m}$): torque = $-(400)(1.5) = -600\text{ N m}$
- Wall force $R_w$ at height $4.0\text{ m}$: torque = $+R_w(4.0) = 4.0R_w$

Sum: $-600 + 4.0R_w = 0$, so $R_w = 150\text{ N}$.

From Equation 1: $f = 150\text{ N}$.

**Why this makes sense:** The wall pushes with $150\text{ N}$ to prevent the ladder from falling, and friction at the ground provides an equal and opposite $150\text{ N}$ to prevent sliding. A rough calculation: the weight (400 N) at half the horizontal distance creates a torque balanced by the wall force over the full height.

---

## Practice Problems

### Problem 1
A $2.0\text{ m}$ uniform plank of mass $10\text{ kg}$ is supported at its centre. A $5.0\text{ kg}$ mass is placed $0.40\text{ m}$ to the left of the centre and a $3.0\text{ kg}$ mass is placed $0.60\text{ m}$ to the right of the centre. Taking $g = 10\text{ m s}^{-2}$, determine whether the plank is balanced. If not, in which direction does it tip?

### Problem 2
A uniform beam $6.0\text{ m}$ long weighing $500\text{ N}$ is supported $1.0\text{ m}$ from its left end and $1.5\text{ m}$ from its right end. A $300\text{ N}$ load is placed at the left end. Find the upward forces at both supports.

### Problem 3
A $50\text{ N}$ sign hangs from a uniform horizontal rod $2.0\text{ m}$ long weighing $30\text{ N}$. The rod is attached to a wall by a hinge at its left end and supported by a cable at its right end, making an angle of $30^\circ$ above the horizontal. The sign hangs from the right end. Find the tension in the cable.

### Problem 4
Explain why a longer wrench makes it easier to loosen a tight bolt, using the concept of torque.

### Problem 5 — IB-Style Examination Question
A uniform beam AB of length $3.0\text{ m}$ and weight $200\text{ N}$ is hinged to a wall at point A. The beam is held horizontal by a cable attached at point B, making an angle of $40^\circ$ with the beam. A $150\text{ N}$ weight hangs from the beam at a point $2.0\text{ m}$ from the hinge. Using $g = 10\text{ m s}^{-2}$:

(a) Draw a free-body diagram showing all forces acting on the beam. (2 marks)
(b) Write the condition for rotational equilibrium about point A. (1 mark)
(c) Calculate the tension in the cable. (2 marks)
(d) Determine the magnitude and direction of the reaction force at the hinge. (3 marks)

---

## Answers

### Answer 1
Weights: plank $= 100\text{ N}$ (at centre), left mass $= 50\text{ N}$, right mass $= 30\text{ N}$. About centre: left torque $= -(50)(0.40) = -20\text{ N m}$, right torque $= +(30)(0.60) = +18\text{ N m}$. Net torque $= -2\text{ N m}$. Not balanced — tips to the left.

### Answer 2
Support positions from left end: $L$ at $1.0\text{ m}$, $R$ at $4.5\text{ m}$. Beam weight at $3.0\text{ m}$ (centre). About left support: $-(500)(2.0) - (300)(-1.0) + F_R(3.5) = 0$. $F_R = 371\text{ N}$. From $\Sigma F_y = 0$: $F_L = 500 + 300 - 371 = 429\text{ N}$.

### Answer 3
About hinge: rod weight (torque $30 \times 1.0 = 30\text{ N m}$ clockwise), sign weight ($50 \times 2.0 = 100\text{ N m}$ clockwise), cable tension $T\sin 30^\circ \times 2.0$ counterclockwise. $T(0.5)(2.0) = 130$, $T = 130\text{ N}$.

### Answer 4
Torque $\tau = Fr$. For a given force, doubling the wrench length doubles the torque — the bolt experiences twice the turning effect. Equivalently, to achieve a given torque, a longer wrench requires proportionally less force. This is leverage: a small force at a large distance produces the same torque as a large force at a small distance.

### Answer 5 — IB-Style
**(a)** (2 marks) Forces: weight of beam ($200\text{ N}$ downward at $1.5\text{ m}$ from A), hanging weight ($150\text{ N}$ downward at $2.0\text{ m}$), cable tension $T$ at $40^\circ$ above horizontal at B ($3.0\text{ m}$ from A), hinge reaction with horizontal ($R_x$) and vertical ($R_y$) components at A.

**(b)** $\Sigma\tau_A = 0$: $-(200)(1.5) - (150)(2.0) + T\sin 40^\circ(3.0) = 0$. (1 mark)

**(c)** $3.0T\sin 40^\circ = 300 + 300 = 600$, so $T = 600/(3.0 \times 0.643) = 311\text{ N}$. (2 marks)

**(d)** (3 marks) $\Sigma F_x = 0$: $R_x - T\cos 40^\circ = 0$, $R_x = 311 \times 0.766 = 238\text{ N}$ (right). $\Sigma F_y = 0$: $R_y + T\sin 40^\circ - 200 - 150 = 0$, $R_y = 350 - 311 \times 0.643 = 350 - 200 = 150\text{ N}$ (up). Reaction: $R = \sqrt{238^2 + 150^2} = 281\text{ N}$ at $\theta = \tan^{-1}(150/238) = 32^\circ$ above horizontal.

---

## Key Takeaways

1. **Torque:** $\tau = Fr\sin\theta$ — the rotational analogue of force. Only the perpendicular component of force produces rotation.

2. **Static equilibrium requires BOTH** $\Sigma F = 0$ (no translation) AND $\Sigma\tau = 0$ (no rotation) about any axis.

3. **Choose the pivot to eliminate unknowns.** Put the pivot at a point where unknown forces act — they contribute zero torque there.

4. **Weight acts at centre of gravity.** For uniform objects, this is the geometric centre.

5. **A couple produces pure rotation** — two equal opposite forces separated by distance $d$ give $\tau = Fd$ with no net force.
