# Lesson 3: Momentum and Impulse

## What You'll Learn

In this lesson, you will encounter two new physical quantities—momentum and impulse—that give you a different way to analyze motion, especially when forces act over short time intervals like in collisions and explosions. You will learn the definition of momentum, how impulse relates to force and time, and how the impulse-momentum theorem connects these ideas. You will also learn about the conservation of linear momentum and how to apply it to isolated systems.

---

## 1. What Is Momentum?

### 1.1 Why This Matters

Imagine a bicycle and a truck both moving at the same speed. Which one would you rather step in front of? The bicycle, of course. But why? Both have the same velocity, yet the truck feels far more dangerous. The reason is that the truck has more "quantity of motion"—more momentum. Momentum captures the idea that the impact of a moving object depends on both its mass and its velocity. Understanding momentum is essential for analyzing collisions, explosions, rocket propulsion, and any situation where forces act briefly.

### 1.2 The Key Ideas

**Momentum** is the product of an object's mass and its velocity. It is a vector quantity, meaning it has both magnitude and direction. The symbol for momentum is \( \vec{p} \).

\( \vec{p} = m \vec{v} \)

Momentum is measured in kilogram-meters per second (kg·m/s). There is no special named unit for momentum.

Since momentum depends on velocity, it always points in the same direction as the velocity. If an object changes direction, its momentum changes direction. If an object speeds up, the magnitude of its momentum increases.

A crucial point: momentum is not the same as kinetic energy. Kinetic energy (\( \frac{1}{2} m v^2 \)) is a scalar and depends on the square of speed. Momentum is a vector and depends linearly on velocity. Two objects can have the same kinetic energy but different momenta if they have different masses. Conversely, two objects can have the same magnitude of momentum but different kinetic energies. We will explore this distinction more deeply in the lessons on energy.

### 1.3 Common Misconceptions

Many students think momentum is "how hard something hits." While related, this is imprecise. Momentum is a precisely defined quantity: \( m v \). The "hardness" of a hit involves force, which is related to how quickly momentum changes—a concept we will develop next.

Another misconception is that momentum is a measure of energy. It is not. They are separate quantities with different units, different meanings, and different conservation laws. Do not use the words interchangeably.

Students sometimes think that if an object is at rest, it has no physical significance. But an object at rest has zero momentum. That is still a valid value. And when forces act, that zero can change.

---

## 2. Impulse

### 2.1 Why This Matters

When you catch a ball, your hands move backward. When you jump off a chair, you bend your knees on landing. When cars have airbags, they increase the time over which your body stops. All of these are applications of impulse: the idea that the effect of a force depends on how long it acts.

### 2.2 The Key Ideas

**Impulse** is the product of a force and the time interval over which it acts. It is also a vector quantity.

\( \vec{J} = \vec{F} \Delta t \)

Impulse has the same units as momentum: newton-seconds (N·s), which are equivalent to kg·m/s. You can verify: 1 N·s = 1 (kg·m/s²)·s = 1 kg·m/s.

When the force is not constant, impulse is the area under a force-time graph. In IB Physics, you should be able to interpret force-time graphs and calculate impulse as the area under the curve.

The idea of impulse explains many everyday safety devices. Catching an egg: if you stop your hand abruptly, the egg breaks because the force is large (small \( \Delta t \)). If you "give" with the egg, moving your hand backward, the stopping time increases, reducing the force for the same change in momentum. Car airbags increase the time of impact; the same change in momentum happens over a longer time, so the force on your body is smaller.

### 2.3 Common Misconceptions

Students often think impulse is a type of force, or that impulse and force are the same thing. They are not. Force is the push or pull at an instant. Impulse is the cumulative effect of that force over time. You can have a large force with a tiny impulse (if it acts for a very short time), or a small force with a large impulse (if it acts for a long time).

---

## 3. The Impulse-Momentum Theorem

### 3.1 Derivation

The impulse-momentum theorem connects the two quantities we have defined. It follows directly from Newton's second law.

From Newton's second law: \( \vec{F} = m \vec{a} \).

Acceleration is the rate of change of velocity: \( \vec{a} = \frac{\Delta \vec{v}}{\Delta t} \).

Substitute: \( \vec{F} = m \frac{\Delta \vec{v}}{\Delta t} \).

Multiply both sides by \( \Delta t \): \( \vec{F} \Delta t = m \Delta \vec{v} \).

The left side is impulse \( \vec{J} \). The right side is \( m \Delta \vec{v} = m(\vec{v}_f - \vec{v}_i) = \vec{p}_f - \vec{p}_i = \Delta \vec{p} \).

Thus: **Impulse equals change in momentum.**

\( \vec{J} = \Delta \vec{p} \)

### 3.2 What This Means

The impulse-momentum theorem tells you that to change an object's momentum, you must apply a force over some time interval. The larger the impulse, the larger the change in momentum. For a given change in momentum, you can either apply a large force for a short time or a small force for a long time.

This theorem is particularly useful for analyzing collisions, where forces are large, complex, and act over very short times. You do not need to know the detailed force variation—you only need the total impulse, which equals the change in momentum.

### 3.3 How to Apply It

To use the impulse-momentum theorem:
1. Identify the initial and final velocities of the object.
2. Calculate the initial and final momentum: \( \vec{p}_i = m \vec{v}_i \), \( \vec{p}_f = m \vec{v}_f \).
3. Find the change in momentum: \( \Delta \vec{p} = \vec{p}_f - \vec{p}_i \) (vector subtraction).
4. This change equals the impulse delivered to the object.
5. If you know the time of contact, the average force is \( \vec{F}_{\text{avg}} = \frac{\Delta \vec{p}}{\Delta t} \).

### 3.4 Common Misconceptions

Many students think the force during a collision is the object's momentum divided by time. But the impulse-momentum theorem uses the *change* in momentum, not the momentum itself. If a ball hits a wall and rebounds with the same speed, the change in momentum is \( 2mv \), not \( mv \). Missing the direction reversal is one of the most common errors.

---

## 4. Conservation of Linear Momentum

### 4.1 Why This Matters

The conservation of momentum is one of the most powerful principles in all of physics. It applies in situations ranging from subatomic particle collisions to galactic mergers. Unlike Newton's laws, which require you to know all the forces, momentum conservation only requires you to know that no external forces act on the system. This makes it ideal for analyzing collisions and explosions.

### 4.2 The Principle

The law of conservation of linear momentum states: when the net external force on a system is zero, the total linear momentum of the system remains constant.

In equation form: \( \sum \vec{p}_{\text{before}} = \sum \vec{p}_{\text{after}} \).

This is a vector equation. In two dimensions, it means conservation holds independently in the x-direction and the y-direction.

### 4.3 What Is a System?

A **system** is a collection of objects you choose to focus on. Everything else is the "surroundings" or "environment." **Internal forces** are forces between objects within the system. **External forces** are forces exerted on objects in the system by objects outside the system.

Momentum is conserved only when the net external force on the system is zero. Internal forces do not change the total momentum of the system because, by Newton's third law, they come in equal and opposite pairs that cancel when you sum over the whole system.

For example, consider two ice skaters pushing off each other. If you define the system as both skaters, the forces they exert on each other are internal. The total momentum of the two skaters before pushing (zero) equals the total momentum after (also zero, but the skaters move in opposite directions). If friction from the ice is negligible, momentum is conserved.

### 4.4 When Is Momentum Conserved?

Momentum is conserved when the net external force is zero. In practice, this means:
- No external forces act at all (deep space).
- External forces exist but cancel (a book on a table: weight and normal cancel in the vertical direction).
- External forces are negligible compared to internal forces during a brief event. In a collision, the forces between colliding objects are enormous but brief. External forces like friction may be present but are tiny in comparison. We can approximate momentum as conserved during the collision.

This last point is crucial: in collision problems, you almost always apply momentum conservation, even if external forces exist, because the collision happens so fast that external forces do not have time to change the momentum significantly.

### 4.5 Common Misconceptions

A common error is applying momentum conservation when significant external forces act over a long time. If a block slides to a stop due to friction, momentum is not conserved for the block alone—friction is an external force that removes momentum.

Another error is treating momentum as a scalar and forgetting direction. If two objects move toward each other, one has positive momentum and the other has negative momentum (in your chosen coordinate system). They can add to zero. Many students add the magnitudes instead, which gives a wrong answer.

---

## 5. Elastic and Inelastic Interactions

### 5.1 Definitions

Interactions where momentum is conserved can be classified by what happens to kinetic energy.

In an **elastic collision**, both momentum and kinetic energy are conserved. Perfectly elastic collisions are rare in the macroscopic world—billiard ball collisions are close, as are collisions between hard steel balls. At the atomic and subatomic level, many collisions are perfectly elastic.

In an **inelastic collision**, momentum is conserved but kinetic energy is not. Some kinetic energy is converted to other forms: thermal energy, sound, deformation. Objects may stick together or deform.

A **perfectly inelastic collision** (sometimes called completely inelastic) is one where the objects stick together and move as a single object after the collision. This type maximizes the loss of kinetic energy (consistent with momentum conservation).

### 5.2 Key Equations

For a one-dimensional collision between two objects A and B:

**Momentum conservation (always):**
\( m_A v_{A,i} + m_B v_{B,i} = m_A v_{A,f} + m_B v_{B,f} \)

**Kinetic energy conservation (elastic only):**
\( \frac{1}{2} m_A v_{A,i}^2 + \frac{1}{2} m_B v_{B,i}^2 = \frac{1}{2} m_A v_{A,f}^2 + \frac{1}{2} m_B v_{B,f}^2 \)

For a perfectly inelastic collision where they stick together:
\( m_A v_{A,i} + m_B v_{B,i} = (m_A + m_B) v_f \)

### 5.3 Common Misconceptions

Many students think that if objects bounce apart, the collision must be elastic. This is false. Bouncing only means they separate; energy could still be lost to sound, heat, or deformation. Elastic means kinetic energy is exactly conserved, which is much more restrictive.

Another misconception is that momentum is always lost in inelastic collisions. Momentum is never lost—it is always conserved for an isolated system. Only kinetic energy is "lost" (converted to other forms).

---

## Worked Examples

### Worked Example 3.1: Impulse from a Kick

A football of mass 0.50 kg is initially at rest on the ground. A player kicks the ball, and it leaves the player's foot with a velocity of 20 m/s to the right. The foot is in contact with the ball for 0.050 seconds.

(a) Calculate the impulse delivered to the ball.
(b) Calculate the average force exerted by the foot on the ball.

**Approach:** The impulse equals the change in momentum. Since the ball starts from rest, the change in momentum is simply the final momentum. The average force is impulse divided by contact time.

**Step-by-step:**

(a) Initial momentum: \( p_i = m v_i = (0.50 \, \text{kg})(0 \, \text{m/s}) = 0 \, \text{kg·m/s} \)
Final momentum (taking right as positive): \( p_f = m v_f = (0.50 \, \text{kg})(20 \, \text{m/s}) = 10 \, \text{kg·m/s} \)
Impulse: \( J = \Delta p = p_f - p_i = 10 - 0 = 10 \, \text{N·s} \) to the right.

(b) \( F_{\text{avg}} = \frac{J}{\Delta t} = \frac{10 \, \text{N·s}}{0.050 \, \text{s}} = 200 \, \text{N} \) to the right.

**Why this makes sense:** A 200 N force is about the weight of a 20 kg mass. That a foot can exert such a force for a brief moment is plausible. The impulse of 10 N·s means the ball gained 10 kg·m/s of momentum.

### Worked Example 3.2: Catching a Ball

A cricket ball of mass 0.16 kg is moving horizontally at 25 m/s toward a fielder. The fielder catches the ball and brings it to rest. The fielder's hands move backward 0.40 m during the catch.

(a) Calculate the impulse delivered to the ball by the fielder's hands.
(b) Assuming constant deceleration, calculate the average force on the ball and the time of the catch.

**Approach:** Impulse equals change in momentum. The ball goes from 25 m/s to 0 m/s. For part (b), we use kinematics to find the time from the stopping distance and average velocity, then find the average force.

**Step-by-step:**

(a) Taking the ball's initial direction as positive. Initial momentum: \( p_i = (0.16 \, \text{kg})(25 \, \text{m/s}) = 4.0 \, \text{kg·m/s} \). Final momentum: \( p_f = 0 \). Impulse: \( J = \Delta p = 0 - 4.0 = -4.0 \, \text{N·s} \). The negative sign means the impulse is opposite to the ball's initial velocity—the hands push backward on the ball.

(b) The average velocity during constant deceleration: \( v_{\text{avg}} = \frac{v_i + v_f}{2} = \frac{25 + 0}{2} = 12.5 \, \text{m/s} \). The time to stop over 0.40 m: \( \Delta t = \frac{\text{distance}}{v_{\text{avg}}} = \frac{0.40 \, \text{m}}{12.5 \, \text{m/s}} = 0.032 \, \text{s} \). The average force: \( F_{\text{avg}} = \frac{J}{\Delta t} = \frac{-4.0 \, \text{N·s}}{0.032 \, \text{s}} = -125 \, \text{N} \). The negative indicates the force opposes the ball's motion. The magnitude is 125 N.

**Why this makes sense:** By moving the hands back 0.40 m, the fielder extends the stopping time, reducing the force. If the hands were rigid (stopping distance near zero), the time would be extremely short and the force enormous—which is why catching without "giving" hurts.

### Worked Example 3.3: Perfectly Inelastic Collision

A 1200 kg car traveling east at 15 m/s collides with an 800 kg car traveling north at 20 m/s at an intersection. The cars stick together after the collision. Find the velocity (speed and direction) of the wreckage immediately after the collision.

**Approach:** Momentum is conserved in both the x (east) and y (north) directions independently. We calculate the total momentum in each direction before the collision, then find the velocity of the combined mass after.

**Step-by-step:**

Step 1: Define east as +x, north as +y.

Step 2: Total x-momentum before: \( p_x = (1200 \, \text{kg})(15 \, \text{m/s}) + (800 \, \text{kg})(0) = 18\,000 \, \text{kg·m/s} \)

Step 3: Total y-momentum before: \( p_y = (1200 \, \text{kg})(0) + (800 \, \text{kg})(20 \, \text{m/s}) = 16\,000 \, \text{kg·m/s} \)

Step 4: After collision, combined mass = \( 1200 + 800 = 2000 \, \text{kg} \). By conservation:
\( p_x = m_{\text{total}} v_x \Rightarrow 18\,000 = 2000 v_x \Rightarrow v_x = 9.0 \, \text{m/s} \)
\( p_y = m_{\text{total}} v_y \Rightarrow 16\,000 = 2000 v_y \Rightarrow v_y = 8.0 \, \text{m/s} \)

Step 5: Speed: \( v = \sqrt{v_x^2 + v_y^2} = \sqrt{9.0^2 + 8.0^2} = \sqrt{81 + 64} = \sqrt{145} \approx 12.0 \, \text{m/s} \)

Direction: \( \theta = \arctan\left(\frac{v_y}{v_x}\right) = \arctan\left(\frac{8.0}{9.0}\right) \approx 41.6^\circ \) north of east.

**Why this makes sense:** The wreckage moves in a direction between east and north, closer to east because the eastbound car had more momentum (18,000 vs. 16,000). The speed is between the initial speeds, which is reasonable since momentum is conserved but the mass increased.

### Worked Example 3.4: Recoil (Explosion)

A 50 kg student on frictionless ice skates holds a 5.0 kg medicine ball. Initially both are at rest. The student throws the ball horizontally at 8.0 m/s to the right. Find the recoil velocity of the student.

**Approach:** Initially total momentum is zero. After throwing, the momentum of student plus ball must still be zero because no external horizontal forces act (frictionless ice). The student moves opposite to the ball.

**Step-by-step:**

Step 1: Define right as positive.

Step 2: Initial total momentum: both at rest, so \( p_{\text{total},i} = 0 \).

Step 3: After: \( p_{\text{total},f} = m_{\text{student}} v_{\text{student}} + m_{\text{ball}} v_{\text{ball}} = (50 \, \text{kg}) v_s + (5.0 \, \text{kg})(8.0 \, \text{m/s}) \)

Step 4: Conservation: \( 0 = 50 v_s + 40 \)
\( 50 v_s = -40 \)
\( v_s = -0.80 \, \text{m/s} \)

The negative sign means the student moves left at 0.80 m/s.

**Why this makes sense:** The student is 10 times more massive than the ball, so they recoil at one-tenth the speed in the opposite direction. This is the principle behind rocket propulsion and recoil of firearms.

### Worked Example 3.5: Force-Time Graph

A force sensor measures the force exerted on a 0.20 kg puck during a collision. The force-time graph is a triangle: force rises linearly from 0 to 40 N over 0.010 s, then falls linearly to 0 over the next 0.010 s. The puck was initially moving at 5.0 m/s in the direction of the force. Find the puck's final velocity.

**Approach:** Impulse is the area under the force-time graph. For a triangle, area = ½ × base × height. The impulse equals the change in momentum.

**Step-by-step:**

Step 1: The graph is a triangle with base \( \Delta t = 0.020 \, \text{s} \) and height \( F_{\text{max}} = 40 \, \text{N} \).

Step 2: Impulse = area = \( \frac{1}{2} \times 0.020 \, \text{s} \times 40 \, \text{N} = 0.40 \, \text{N·s} \)

Step 3: Change in momentum: \( \Delta p = J = 0.40 \, \text{kg·m/s} \)

Step 4: Initial momentum: \( p_i = m v_i = (0.20 \, \text{kg})(5.0 \, \text{m/s}) = 1.0 \, \text{kg·m/s} \)

Step 5: Final momentum: \( p_f = p_i + \Delta p = 1.0 + 0.40 = 1.40 \, \text{kg·m/s} \)

Step 6: Final velocity: \( v_f = \frac{p_f}{m} = \frac{1.40 \, \text{kg·m/s}}{0.20 \, \text{kg}} = 7.0 \, \text{m/s} \)

**Why this makes sense:** The impulse adds momentum in the direction of motion, so the puck speeds up. The increase is modest (from 5 to 7 m/s), which is reasonable for a brief 40 N force on a light puck.

---

## Practice Problems

### Problem 1

A tennis ball of mass 0.060 kg is served. It leaves the racket at 50 m/s after being struck from rest.

(a) Calculate the impulse delivered to the tennis ball by the racket.

(b) The ball is in contact with the racket strings for 0.0040 seconds. Calculate the average force exerted on the ball during the serve.

(c) A student says: "If the racket is swung faster, the impulse increases because the force is larger." Another student says: "If the racket is swung faster, the impulse increases because the contact time is longer." Discuss which student is correct, or whether both could be correct.

### Problem 2

A 0.15 kg ball is thrown horizontally at 12 m/s toward a wall. It hits the wall and rebounds horizontally at 8.0 m/s in the opposite direction. The ball is in contact with the wall for 0.030 seconds.

(a) Taking the initial direction of the ball as positive, calculate the initial and final momentum of the ball.

(b) Calculate the impulse delivered to the ball by the wall.

(c) Calculate the average force exerted on the ball by the wall.

### Problem 3

A 60 g golf ball is dropped from a height of 2.0 m onto a hard floor. It rebounds to a height of 1.2 m. Take \( g = 10 \, \text{m/s}^2 \).

(a) Calculate the speed of the golf ball just before it hits the floor.

(b) Calculate the speed of the golf ball just after it leaves the floor.

(c) If the ball is in contact with the floor for 0.0080 seconds, calculate the average force exerted by the floor on the ball during the impact. State the direction of this force.

### Problem 4

Two ice skaters, a 70 kg adult and a 30 kg child, stand facing each other on frictionless ice. They push off each other with their hands. After pushing, the child moves backward at 2.1 m/s.

(a) Explain why the total momentum of the two-skater system is conserved during the push.

(b) Calculate the velocity (speed and direction) of the adult after the push.

(c) Calculate the impulse delivered to the child by the adult during the push.

### Problem 5

On a frictionless air track, a glider A of mass 0.40 kg moves to the right at 6.0 m/s. It collides with glider B of mass 0.60 kg, which is initially at rest. After the collision, glider A moves to the right at 1.2 m/s.

(a) Calculate the velocity of glider B after the collision.

(b) Determine whether the collision is elastic. Show your working clearly.

(c) A different collision between the same two gliders results in them sticking together. Calculate the loss of kinetic energy in this perfectly inelastic collision.

### Problem 6 (IB Exam-Style)

A wooden block of mass \( M = 4.0 \, \text{kg} \) rests on a horizontal frictionless surface. The block is attached to a fixed wall by a horizontal spring that obeys Hooke's law. A bullet of mass \( m = 0.020 \, \text{kg} \) is fired horizontally with speed \( v = 300 \, \text{m/s} \) into the block. The bullet becomes embedded in the block, and the block (with bullet inside) then slides, compressing the spring.

(a) State the law of conservation of linear momentum and explain why it can be applied to the bullet-block collision even though the block is attached to a spring.
[3 marks]

(b) Calculate the speed of the block and bullet immediately after the collision.
[3 marks]

(c) The spring constant is \( k = 2000 \, \text{N/m} \). Calculate the maximum compression of the spring. (Hint: the kinetic energy of the block after the collision is converted to elastic potential energy in the spring.)
[3 marks]

(d) The student repeats the experiment with a bullet of equal mass but twice the speed. Predict, with a reason, whether the maximum compression of the spring will be exactly twice as large, more than twice as large, or less than twice as large.
[3 marks]

(e) In reality, the surface is not perfectly frictionless. Explain how this would affect the measured spring compression and suggest how the experiment could be modified to account for this.
[2 marks]

---

## Answers

### Answer 1

(a) The ball starts from rest, so initial momentum is zero. Final momentum: \( p_f = m v_f = (0.060 \, \text{kg})(50 \, \text{m/s}) = 3.0 \, \text{kg·m/s} \). Impulse equals change in momentum: \( J = 3.0 - 0 = 3.0 \, \text{N·s} \).

(b) Average force: \( F_{\text{avg}} = \frac{J}{\Delta t} = \frac{3.0 \, \text{N·s}}{0.0040 \, \text{s}} = 750 \, \text{N} \). This is a large force, consistent with the rapid acceleration of a tennis ball.

(c) Both students could be partially correct, but the primary effect is through force. The impulse-momentum theorem says \( J = F_{\text{avg}} \Delta t = \Delta p \). Swinging faster increases the racket speed, so the ball leaves with higher velocity and thus experiences a larger change in momentum (larger impulse). This could come from a larger average force, a longer contact time, or both. In practice, the contact time of tennis strings is largely determined by string tension and does not change dramatically with swing speed. So the dominant effect is likely a larger average force. Neither student is entirely wrong, but the first student's explanation is closer to what actually happens. A careful answer would note that the impulse increases because \( \Delta p \) increases, and the split between \( F_{\text{avg}} \) and \( \Delta t \) depends on the details of the racket-string-ball interaction.

### Answer 2

(a) Taking the initial direction as positive. Initial momentum: \( p_i = (0.15 \, \text{kg})(12 \, \text{m/s}) = 1.8 \, \text{kg·m/s} \). Final momentum: \( p_f = (0.15 \, \text{kg})(-8.0 \, \text{m/s}) = -1.2 \, \text{kg·m/s} \).

(b) Impulse: \( J = \Delta p = p_f - p_i = -1.2 - 1.8 = -3.0 \, \text{N·s} \). The negative sign means the impulse direction is opposite to the initial velocity (i.e., away from the wall).

A common mistake is to calculate \( \Delta p \) as \( 1.8 - 1.2 = 0.6 \, \text{kg·m/s} \), forgetting that velocity reverses direction. Always set a coordinate system and use signs consistently.

(c) Average force: \( F_{\text{avg}} = \frac{J}{\Delta t} = \frac{-3.0 \, \text{N·s}}{0.030 \, \text{s}} = -100 \, \text{N} \). The magnitude of the force is 100 N, directed away from the wall (the wall pushes the ball back).

### Answer 3

(a) Using \( v^2 = u^2 + 2as \) with \( u = 0 \), \( a = g = 10 \, \text{m/s}^2 \), \( s = 2.0 \, \text{m} \): \( v^2 = 0 + 2(10)(2.0) = 40 \), so \( v = \sqrt{40} \approx 6.32 \, \text{m/s} \) downward. Let downward be positive for the fall.

(b) The ball rebounds to 1.2 m. At maximum height, \( v = 0 \). Using \( v^2 = u^2 + 2as \) with \( v = 0 \), \( a = -10 \, \text{m/s}^2 \), \( s = 1.2 \, \text{m} \): \( 0 = u^2 - 2(10)(1.2) \), \( u^2 = 24 \), \( u = \sqrt{24} \approx 4.90 \, \text{m/s} \) upward.

Now redefine coordinates: take upward as positive for the collision. Then velocity just before impact (downward) is \(-6.32 \, \text{m/s}\). Velocity just after impact (upward) is \(+4.90 \, \text{m/s}\).

(c) Mass \( m = 0.060 \, \text{kg} \). Change in momentum: \( \Delta p = m(v_f - v_i) = 0.060(4.90 - (-6.32)) = 0.060(11.22) \approx 0.673 \, \text{kg·m/s} \). Impulse equals \( \Delta p \), so impulse ≈ 0.673 N·s upward. Average force: \( F_{\text{avg}} = \frac{0.673}{0.0080} \approx 84 \, \text{N} \) upward. The floor exerts an upward force on the ball to reverse its direction.

### Answer 4

(a) The system consists of both skaters. The forces they exert on each other during the push are internal forces. By Newton's third law, these forces are equal and opposite. The only external forces are weight and the normal force from the ice, which cancel in the vertical direction. Horizontally, there is no friction (the ice is frictionless). Since the net external horizontal force on the system is zero, horizontal momentum is conserved.

(b) Initially, both are at rest: total momentum = 0. After push: momentum of child + momentum of adult = 0. Taking the child's direction as positive: \( (30 \, \text{kg})(2.1 \, \text{m/s}) + (70 \, \text{kg}) v_a = 0 \). So \( v_a = \frac{-63}{70} = -0.90 \, \text{m/s} \). The adult moves at 0.90 m/s in the direction opposite to the child.

(c) Impulse on child = change in child's momentum = \( (30 \, \text{kg})(2.1 \, \text{m/s}) - 0 = 63 \, \text{N·s} \) in the direction the child moves.

### Answer 5

(a) Momentum conservation: \( m_A v_{A,i} + m_B v_{B,i} = m_A v_{A,f} + m_B v_{B,f} \).
\( (0.40)(6.0) + (0.60)(0) = (0.40)(1.2) + (0.60) v_{B,f} \)
\( 2.4 = 0.48 + 0.60 v_{B,f} \)
\( 0.60 v_{B,f} = 1.92 \)
\( v_{B,f} = 3.2 \, \text{m/s} \) to the right.

(b) For an elastic collision, kinetic energy must be conserved.

Initial KE: \( \frac{1}{2}(0.40)(6.0)^2 + 0 = 0.20 \times 36 = 7.2 \, \text{J} \)

Final KE: \( \frac{1}{2}(0.40)(1.2)^2 + \frac{1}{2}(0.60)(3.2)^2 = 0.20(1.44) + 0.30(10.24) = 0.288 + 3.072 = 3.36 \, \text{J} \)

Since 7.2 J ≠ 3.36 J, kinetic energy is not conserved. The collision is inelastic.

(c) Perfectly inelastic: they stick together. \( (0.40)(6.0) = (0.40 + 0.60) v_f \), so \( v_f = \frac{2.4}{1.0} = 2.4 \, \text{m/s} \).

Initial KE = 7.2 J (as above). Final KE = \( \frac{1}{2}(1.0)(2.4)^2 = 0.50 \times 5.76 = 2.88 \, \text{J} \). Loss = \( 7.2 - 2.88 = 4.32 \, \text{J} \).

### Answer 6 (IB Exam-Style)

(a) [3 marks] The law of conservation of linear momentum states that when the net external force on a system is zero, the total momentum of the system remains constant [1 mark]. During the brief collision between the bullet and the block, the spring force is negligible compared to the enormous forces between bullet and block—the collision happens in milliseconds, while the spring force is initially zero (spring at natural length) and grows slowly with displacement [1 mark]. Therefore, the net external force on the bullet-block system during the collision is effectively zero, and momentum is conserved [1 mark].

(b) [3 marks] By conservation of momentum: \( m v = (M + m) V \) [1 mark]. \( (0.020 \, \text{kg})(300 \, \text{m/s}) = (4.0 \, \text{kg} + 0.020 \, \text{kg}) V \) [1 mark]. \( 6.0 = 4.02 V \), so \( V = \frac{6.0}{4.02} \approx 1.49 \, \text{m/s} \approx 1.5 \, \text{m/s} \) [1 mark].

(c) [3 marks] Kinetic energy after collision: \( KE = \frac{1}{2}(M+m)V^2 = \frac{1}{2}(4.02)(1.49)^2 \) [1 mark]. This is converted to spring potential energy: \( \frac{1}{2} k x_{\text{max}}^2 = \frac{1}{2}(M+m)V^2 \) [1 mark]. \( x_{\text{max}} = \sqrt{\frac{(M+m)V^2}{k}} = \sqrt{\frac{4.02 \times 2.22}{2000}} = \sqrt{\frac{8.92}{2000}} \approx \sqrt{0.00446} \approx 0.067 \, \text{m} = 6.7 \, \text{cm} \) [1 mark]. (Accept 6.7 cm or 0.067 m.)

(d) [3 marks] If bullet speed doubles from \( v \) to \( 2v \), the post-collision speed \( V = \frac{m(2v)}{M+m} = 2V_0 \) [1 mark]. The kinetic energy after collision is \( \frac{1}{2}(M+m)(2V_0)^2 = 4 \times \frac{1}{2}(M+m)V_0^2 \), which is four times larger [1 mark]. Since \( x_{\text{max}} \propto V \) (from \( \frac{1}{2}kx_{\text{max}}^2 = KE \)), and KE quadruples, \( x_{\text{max}} \propto \sqrt{KE} \), so \( x_{\text{max}} \) doubles. The compression will be exactly twice as large [1 mark].

(e) [2 marks] Friction would do negative work, removing some kinetic energy before all energy is converted to spring potential energy [1 mark]. The measured spring compression would be smaller than the theoretical value. To account for this, the student could measure the friction force and calculate the work done against friction, or use an air track to minimize friction [1 mark].

---

## Key Takeaways

1. Momentum is the product of mass and velocity: \( \vec{p} = m\vec{v} \). It is a vector quantity measured in kg·m/s.
2. Impulse is the product of force and time: \( \vec{J} = \vec{F}\Delta t \). It is also measured in N·s (equivalent to kg·m/s).
3. The impulse-momentum theorem: \( \vec{J} = \Delta\vec{p} \). Impulse equals change in momentum.
4. To reduce impact force for a given change in momentum, increase the time over which the change occurs (airbags, cushioning, "giving" when catching).
5. Momentum is conserved when the net external force on a system is zero. Internal forces do not affect total momentum.
6. In collisions, momentum is conserved (approximately, because collision forces dominate external forces).
7. Elastic collisions conserve kinetic energy as well as momentum. Inelastic collisions do not. Perfectly inelastic collisions result in the objects sticking together.
8. Momentum is a vector. In 2D problems, apply conservation independently in the x and y directions.
9. A force-time graph gives impulse as the area under the curve.
10. The change in momentum—not the momentum itself—determines impulse and average force in an interaction.
