# Lesson 5: Work, Energy and Power

## What You'll Learn

By the end of this lesson, you will be able to:
- Define work and calculate it for forces at any angle to displacement
- Use the work-energy theorem to relate work done to changes in kinetic energy
- Apply conservation of energy to problems involving kinetic, gravitational potential, and elastic potential energy
- Calculate power as the rate of doing work and relate it to force and velocity
- Determine the efficiency of energy transfers

---

## 1. Work — What Does It Mean to "Do Work" in Physics?

### 1.1 Why This Matters

The word "work" in everyday language means effort or labour. In physics, work has a precise meaning: work is done when a force causes an object to move in the direction of the force. If you push against a wall and it does not move, you might feel tired, but you have done zero work on the wall in the physics sense. The wall did not move. This is not just pedantry — it is the foundation of how energy transfers are quantified across all of physics.

Work is the mechanism by which energy is transferred from one object to another. When you lift a book, you do work on the book, transferring energy from your muscles to the book's gravitational potential energy. Understanding work is the bridge between forces (which we studied in Lessons 2–4) and energy (which we study here).

### 1.2 The Key Ideas

**Definition of work:** When a constant force $F$ acts on an object while the object moves through a displacement $s$, the work done by that force is:

$$W = Fs\cos\theta$$

where $\theta$ is the angle between the force vector and the displacement vector.

The SI unit of work is the joule (J). One joule is the work done when a force of one newton moves an object through one metre in the direction of the force: $1\text{ J} = 1\text{ N} \cdot 1\text{ m}$.

Let us understand why the cosine appears. Imagine pulling a sled with a rope. If you pull horizontally in the direction of motion, $\theta = 0^\circ$ and $\cos 0^\circ = 1$, so $W = Fs$ — all of your force contributes to moving the sled. If you pull at an angle, only the horizontal component $F\cos\theta$ moves the sled forward; the vertical component lifts it slightly but does not contribute to forward motion. If you pull perpendicular to the motion ($\theta = 90^\circ$), $\cos 90^\circ = 0$ and you do zero work — none of your force moves the sled forward.

**Important clarification:** Work can be positive, negative, or zero.
- **Positive work:** The force has a component in the same direction as the displacement. The force adds energy to the object. Example: pushing a box forward.
- **Negative work:** The force has a component opposite to the displacement. The force removes energy from the object. Example: friction slowing a sliding box. The friction force points backward while the displacement is forward, so $\theta = 180^\circ$ and $\cos 180^\circ = -1$, giving $W = -Fs$.
- **Zero work:** The force is perpendicular to the displacement, or there is no displacement. Example: carrying a box horizontally at constant height — the upward force from your hands is perpendicular to the horizontal motion.

The sign of work tells you whether energy is entering or leaving the object.

### 1.3 Common Misconceptions

**Misconception 1:** "Holding a heavy object stationary means you are doing work." In physics, you are not. No displacement means no work, regardless of how tired your arms feel. Your muscles are doing internal work (contracting and relaxing) but no work is done ON the object.

**Misconception 2:** "Work and energy are different things." Work IS the transfer of energy. They are measured in the same unit (joules). When you do 50 J of work on an object, you transfer 50 J of energy to it.

---

## 2. Kinetic Energy — Energy of Motion

### 2.1 Why This Matters

A moving object can do work. A moving hammer drives a nail; a moving car crushes in a collision. The energy an object possesses because of its motion is called kinetic energy. Every time you see an object speed up or slow down, kinetic energy is being gained or lost, and work is being done.

### 2.2 The Key Ideas

The kinetic energy of an object of mass $m$ moving at speed $v$ is:

$$E_k = \frac{1}{2}mv^2$$

The unit is the joule (J). Notice that kinetic energy depends on the square of the speed. This has an important consequence: doubling the speed quadruples the kinetic energy. A car travelling at 60 m s⁻¹ has four times the kinetic energy of the same car at 30 m s⁻¹, which is why high-speed collisions are so much more destructive.

**The work-energy theorem** connects work and kinetic energy directly:

$$W_{\text{net}} = \Delta E_k = \frac{1}{2}mv^2 - \frac{1}{2}mu^2$$

The net work done on an object equals its change in kinetic energy. This is one of the most powerful problem-solving tools in mechanics. If you can calculate the net work, you can find the final speed without ever using SUVAT.

### 2.3 Common Misconceptions

**Misconception:** "Kinetic energy is always $\frac{1}{2}mv^2$." This is true at everyday speeds, but near the speed of light, the formula changes (this is covered in special relativity, Lesson 13). At IB HL, you need to know both.

---

## 3. Gravitational Potential Energy — Energy of Position

### 3.1 Why This Matters

Lift a book from the floor to a shelf. You do work against gravity. That work is stored as gravitational potential energy (GPE). When the book falls, that stored energy converts back to kinetic energy. This idea — that energy can be stored by position in a field and later released — appears throughout physics: in electric fields, magnetic fields, and nuclear physics.

### 3.2 The Key Ideas

Near the Earth's surface, the change in gravitational potential energy when an object of mass $m$ changes height by $\Delta h$ is:

$$\Delta E_p = mg\Delta h$$

The unit is the joule (J). This formula assumes $g$ is constant, which is a good approximation near the Earth's surface. Far from Earth (orbital distances), $g$ varies and we use a different formula (covered in gravitational fields, Lesson 45).

The zero of gravitational potential energy is arbitrary. We usually choose the lowest point in the problem as $h = 0$. Only changes in GPE matter physically.

**Important:** The formula gives the CHANGE in GPE. If an object moves upward ($\Delta h$ positive), GPE increases. If it moves downward ($\Delta h$ negative), GPE decreases.

---

## 4. Elastic Potential Energy — Energy Stored in Deformation

### 4.1 Why This Matters

Stretch a spring or an elastic band. You do work to deform it, and that energy is stored. When released, the spring snaps back, converting stored energy to kinetic energy. This principle appears in everything from car suspensions to molecular bonds.

### 4.2 The Key Ideas

For an ideal spring obeying Hooke's Law ($F = kx$), the elastic potential energy stored when the spring is stretched or compressed by a displacement $x$ from its natural length is:

$$E_p = \frac{1}{2}kx^2$$

where $k$ is the spring constant (N m⁻¹) — a measure of the spring's stiffness. A stiff spring has a large $k$; a soft spring has a small $k$.

The energy stored depends on the square of the displacement. Doubling the stretch stores four times the energy.

---

## 5. Conservation of Energy

### 5.1 Why This Matters

The principle of conservation of energy is arguably the most important law in all of physics: energy cannot be created or destroyed; it can only be transferred from one form to another or from one object to another. This single principle allows us to solve problems that would be extremely difficult using forces and kinematics alone.

### 5.2 The Key Ideas

In a closed system (no energy enters or leaves), the total energy is constant:

$$E_{\text{total}} = E_k + E_p + E_{\text{thermal}} + \dots = \text{constant}$$

For many IB problems, we consider systems where only kinetic energy and gravitational potential energy change:

$$\frac{1}{2}mu^2 + mgh_i = \frac{1}{2}mv^2 + mgh_f$$

If friction or air resistance is present, some energy is converted to thermal energy (heat). The total energy is still conserved — it is just distributed differently.

### 5.3 Common Misconceptions

**Misconception:** "Energy is 'used up'." Energy is never used up. It is transferred or transformed. When a car brakes, the kinetic energy does not disappear — it becomes thermal energy in the brakes and tyres. The total amount of energy in the universe is constant.

---

## 6. Power — The Rate of Doing Work

### 6.1 Why This Matters

Two people lift identical boxes to the same height. They do the same amount of work. But if one person lifts twice as fast, they are more powerful. Power tells us how quickly energy is transferred, not how much is transferred.

### 6.2 The Key Ideas

Power is the rate at which work is done or energy is transferred:

$$P = \frac{W}{t} = \frac{\Delta E}{t}$$

The SI unit of power is the watt (W). One watt equals one joule per second: $1\text{ W} = 1\text{ J s}^{-1}$.

For an object moving at constant velocity $v$ under a force $F$ (where the force is in the direction of motion):

$$P = Fv$$

This follows from $P = W/t = Fs/t = Fv$. This formula is particularly useful for vehicles: the power needed to maintain a given speed against resistive forces.

### 6.3 Efficiency

No real machine transfers all input energy to useful output. Some energy is always lost to thermal energy, sound, or other forms. Efficiency quantifies this:

$$\eta = \frac{\text{useful work out}}{\text{total work in}} = \frac{\text{useful power out}}{\text{total power in}}$$

Efficiency is a ratio, often expressed as a percentage. A perfect machine would have $\eta = 1$ (100%); real machines always have $\eta < 1$.

---

## Worked Examples

### Worked Example 5.1 — Work Done by a Force at an Angle

**Problem:** A person pulls a sled with a force of 50 N using a rope angled at 30° above the horizontal. The sled moves 12 m horizontally across ice. Calculate the work done by the pulling force.

**Approach:** The work done by a constant force is $W = Fs\cos\theta$. We know $F = 50\text{ N}$, $s = 12\text{ m}$, and the angle between the force and the displacement is $\theta = 30^\circ$. The displacement is horizontal, and the force is at 30° to the horizontal, so the angle between them is indeed 30°.

**Solution:**
$$W = Fs\cos\theta$$
$$W = (50)(12)\cos 30^\circ$$
$$W = 600 \times \frac{\sqrt{3}}{2}$$
$$W = 600 \times 0.866$$
$$W = 520\text{ J}$$

**Why this makes sense:** The force is 50 N and the sled moves 12 m. If the force were perfectly horizontal, the work would be $50 \times 12 = 600\text{ J}$. At 30°, only about 87% of the force contributes to forward motion, so we get about 520 J — slightly less than 600 J, which is reasonable.

---

### Worked Example 5.2 — Work-Energy Theorem

**Problem:** A 1200 kg car travelling at 15 m s⁻¹ accelerates uniformly to 25 m s⁻¹ over a distance of 80 m. Calculate the net work done on the car and the average net force acting on it.

**Approach:** The work-energy theorem states that the net work equals the change in kinetic energy. We can calculate $\Delta E_k$ directly from the initial and final speeds. Then, knowing the distance, we can find the average net force from $W = Fs$.

**Solution:**

Change in kinetic energy:
$$\Delta E_k = \frac{1}{2}mv^2 - \frac{1}{2}mu^2$$
$$\Delta E_k = \frac{1}{2}(1200)(25)^2 - \frac{1}{2}(1200)(15)^2$$
$$\Delta E_k = 600 \times 625 - 600 \times 225$$
$$\Delta E_k = 375,000 - 135,000$$
$$\Delta E_k = 240,000\text{ J}$$

By the work-energy theorem, $W_{\text{net}} = \Delta E_k = 240,000\text{ J}$.

To find the average net force:
$$W = Fs$$
$$240,000 = F \times 80$$
$$F = 3,000\text{ N}$$

**Why this makes sense:** A 3,000 N force acting over 80 m does 240,000 J of work, which increases the car's kinetic energy. The speed increase from 15 to 25 m s⁻¹ is significant — the kinetic energy increases by about 64% (from 135 kJ to 375 kJ), which requires substantial work.

---

### Worked Example 5.3 — Conservation of Energy (Roller Coaster)

**Problem:** A roller coaster car of mass 500 kg starts from rest at the top of a hill 40 m above the ground. It descends to ground level and then rises to a second hill. Neglecting friction, calculate: (a) the speed of the car at ground level, and (b) the maximum height of the second hill if the car's speed at its top is 10 m s⁻¹. Use $g = 10\text{ m s}^{-2}$.

**Approach:** With no friction, mechanical energy is conserved. At each point, the total energy is the sum of kinetic energy and gravitational potential energy. We set the ground as $h = 0$.

**Solution (a):**

At the top of the first hill: $E = mgh + \frac{1}{2}mu^2 = (500)(10)(40) + 0 = 200,000\text{ J}$.

At ground level: $E = mgh + \frac{1}{2}mv^2 = 0 + \frac{1}{2}(500)v^2$.

By conservation of energy:
$$200,000 = \frac{1}{2}(500)v^2$$
$$200,000 = 250v^2$$
$$v^2 = 800$$
$$v = \sqrt{800} = 28.3\text{ m s}^{-1}$$

**Solution (b):**

The total energy is still 200,000 J. At the top of the second hill, the car has speed 10 m s⁻¹ and is at some height $h$:

$$200,000 = mgh + \frac{1}{2}mv^2$$
$$200,000 = (500)(10)h + \frac{1}{2}(500)(10)^2$$
$$200,000 = 5,000h + 25,000$$
$$5,000h = 175,000$$
$$h = 35\text{ m}$$

**Why this makes sense:** The car starts at 40 m with zero speed. At ground level, all GPE has converted to KE, giving maximum speed. The second hill is lower than the first (35 m vs. 40 m) because some energy remains as kinetic energy — the car is still moving at the top.

---

### Worked Example 5.4 — Power of an Accelerating Car

**Problem:** A car of mass 1000 kg accelerates from rest to 20 m s⁻¹ in 5.0 seconds on a level road. Calculate: (a) the average power delivered by the engine during this acceleration, and (b) the instantaneous power when the car reaches 20 m s⁻¹, assuming the net force is constant.

**Approach:** For average power, we use $P = W/t$ where $W$ is the total work done (equal to the gain in kinetic energy). For instantaneous power, we use $P = Fv$, where $F$ is the net force and $v$ is the instantaneous speed.

**Solution (a):**

Total work done:
$$W = \Delta E_k = \frac{1}{2}mv^2 - 0 = \frac{1}{2}(1000)(20)^2 = 500 \times 400 = 200,000\text{ J}$$

Average power:
$$P_{\text{avg}} = \frac{W}{t} = \frac{200,000}{5.0} = 40,000\text{ W} = 40\text{ kW}$$

**Solution (b):**

First, find the acceleration:
$$a = \frac{v - u}{t} = \frac{20 - 0}{5.0} = 4.0\text{ m s}^{-2}$$

Net force:
$$F = ma = 1000 \times 4.0 = 4,000\text{ N}$$

Instantaneous power at $v = 20\text{ m s}^{-1}$:
$$P = Fv = 4,000 \times 20 = 80,000\text{ W} = 80\text{ kW}$$

**Why this makes sense:** The instantaneous power at the final speed (80 kW) is twice the average power (40 kW). This is because power increases linearly with speed when force is constant — at the start ($v = 0$), the power is zero, and it rises to 80 kW by the end. The average of 0 and 80 kW is 40 kW.

---

### Worked Example 5.5 — Spring Energy (IB-Style)

**Problem:** A spring with spring constant $k = 200\text{ N m}^{-1}$ is compressed by 0.15 m from its natural length. A 0.050 kg ball is placed against the compressed spring on a frictionless horizontal surface. The spring is released. Calculate: (a) the elastic potential energy stored in the compressed spring, (b) the speed of the ball when it leaves the spring, and (c) the maximum height the ball would reach if launched vertically upward with the same initial speed. Use $g = 10\text{ m s}^{-2}$.

**Approach:** The spring's elastic potential energy converts entirely to the ball's kinetic energy (no friction). For the vertical launch, the kinetic energy converts to gravitational potential energy at maximum height.

**Solution (a):**
$$E_p = \frac{1}{2}kx^2 = \frac{1}{2}(200)(0.15)^2 = 100 \times 0.0225 = 2.25\text{ J}$$

**Solution (b):**

By energy conservation, all elastic PE becomes KE:
$$\frac{1}{2}mv^2 = 2.25$$
$$\frac{1}{2}(0.050)v^2 = 2.25$$
$$0.025v^2 = 2.25$$
$$v^2 = 90$$
$$v = \sqrt{90} = 9.49\text{ m s}^{-1} \approx 9.5\text{ m s}^{-1}$$

**Solution (c):**

At maximum height, all KE has converted to GPE:
$$mgh = 2.25$$
$$(0.050)(10)h = 2.25$$
$$0.50h = 2.25$$
$$h = 4.5\text{ m}$$

**Why this makes sense:** The spring stores a modest amount of energy (2.25 J — about the energy to lift a 1 kg book 0.23 m). This gives a light 50 g ball a speed of about 9.5 m s⁻¹, and would launch it 4.5 m vertically — plausible for a small spring-powered launcher.

---

## Practice Problems

### Problem 1
A worker pushes a crate with a constant horizontal force of 200 N across a rough floor. The crate moves 5.0 m at constant velocity. (a) Calculate the work done by the worker on the crate. (b) The crate moves at constant velocity, which means the net force on it is zero. Calculate the work done by friction during the same 5.0 m displacement. (c) Explain why the net work done on the crate is zero even though both the worker and friction are doing work.

### Problem 2
A 2.0 kg object is dropped from a height of 15 m above the ground. Using $g = 10\text{ m s}^{-2}$ and neglecting air resistance, use energy considerations to calculate: (a) the speed of the object just before it hits the ground, and (b) the speed of the object when it is 5.0 m above the ground.

### Problem 3
A spring with spring constant $k = 400\text{ N m}^{-1}$ is stretched by 0.10 m from its natural length. Calculate: (a) the elastic potential energy stored in the spring, and (b) the additional work required to stretch it from 0.10 m to 0.20 m. Explain why the answer to (b) is larger than the answer to (a).

### Problem 4
An electric motor lifts a 50 kg mass vertically upward at a constant speed of 2.0 m s⁻¹. Using $g = 10\text{ m s}^{-2}$, calculate: (a) the force that the motor must exert, (b) the power output of the motor, and (c) the energy transferred by the motor in 30 seconds. If the motor has an efficiency of 80%, calculate (d) the electrical power input to the motor.

### Problem 5 — IB-Style Examination Question
A cyclist and her bicycle have a combined mass of 80 kg. She freewheels down a slope of constant angle, starting from rest at point A, which is 25 m vertically above point B at the bottom of the slope. At point B, her speed is 18 m s⁻¹. The distance along the slope from A to B is 150 m.

(a) Calculate the total mechanical energy lost by the cyclist and bicycle between A and B. (2 marks)

(b) Determine the average resistive force (due to friction and air resistance) acting on the cyclist during her descent. (2 marks)

(c) After point B, the road is level. The cyclist continues to pedal, delivering a constant power of 200 W to overcome the same average resistive force as in part (b). Calculate her maximum steady speed on the level road. (3 marks)

(d) Suggest and explain one reason why the resistive force on the level road might differ from the average resistive force on the slope. (2 marks)

---

## Answers

### Answer 1

**(a)** The worker applies a horizontal force in the direction of motion ($\theta = 0^\circ$):
$$W_{\text{worker}} = Fs\cos\theta = (200)(5.0)(1) = 1,000\text{ J}$$

**(b)** Since the crate moves at constant velocity, the net force is zero, so the friction force must equal the applied force in magnitude (200 N) but act in the opposite direction. The angle between friction and displacement is $180^\circ$:
$$W_{\text{friction}} = Fs\cos\theta = (200)(5.0)(-1) = -1,000\text{ J}$$

**(c)** The net work is $W_{\text{net}} = 1,000 + (-1,000) = 0\text{ J}$. This is consistent with the work-energy theorem: since the velocity is constant, $\Delta E_k = 0$, so $W_{\text{net}} = 0$. The worker and friction do equal and opposite amounts of work. The energy transferred by the worker (1,000 J) is entirely dissipated as thermal energy by friction. No net energy is added to the crate.

---

### Answer 2

**(a)** At height 15 m with zero initial speed, the total energy is purely gravitational potential energy (taking ground as $h = 0$):
$$E_{\text{initial}} = mgh = (2.0)(10)(15) = 300\text{ J}$$

Just before hitting the ground ($h = 0$), this has all converted to kinetic energy:
$$\frac{1}{2}mv^2 = 300$$
$$\frac{1}{2}(2.0)v^2 = 300$$
$$v^2 = 300$$
$$v = \sqrt{300} = 17.3\text{ m s}^{-1}$$

**(b)** At height 5.0 m, the energy is split between GPE and KE. The total energy is still 300 J:
$$mgh + \frac{1}{2}mv^2 = 300$$
$$(2.0)(10)(5.0) + \frac{1}{2}(2.0)v^2 = 300$$
$$100 + v^2 = 300$$
$$v^2 = 200$$
$$v = \sqrt{200} = 14.1\text{ m s}^{-1}$$

A common mistake is to use SUVAT with displacement 10 m (15 m minus 5 m) and initial speed zero, as if the object were dropped from 10 m. That would give $v = \sqrt{2 \times 10 \times 10} = 14.1\text{ m s}^{-1}$ — the same answer. This works because gravity is the only force, but the energy method is more general and does not require remembering SUVAT equations.

---

### Answer 3

**(a)** For $x = 0.10\text{ m}$:
$$E_p = \frac{1}{2}kx^2 = \frac{1}{2}(400)(0.10)^2 = 200 \times 0.010 = 2.0\text{ J}$$

**(b)** The energy stored at $x = 0.20\text{ m}$ is:
$$E_p = \frac{1}{2}(400)(0.20)^2 = 200 \times 0.040 = 8.0\text{ J}$$

The additional work required is the difference:
$$W = 8.0 - 2.0 = 6.0\text{ J}$$

The answer to (b) is larger than (a) because elastic potential energy depends on $x^2$, not $x$. Doubling the stretch from 0.10 m to 0.20 m quadruples the stored energy (from 2.0 J to 8.0 J). The additional work to go from 0.10 m to 0.20 m is 6.0 J, which is three times the energy stored at 0.10 m. This is because the spring gets stiffer as you stretch it — the force increases with displacement, so each additional centimetre requires more work than the previous one.

---

### Answer 4

**(a)** At constant speed, the upward force from the motor equals the weight:
$$F = mg = (50)(10) = 500\text{ N}$$

**(b)** Power output:
$$P = Fv = (500)(2.0) = 1,000\text{ W} = 1.0\text{ kW}$$

**(c)** Energy transferred in 30 seconds:
$$E = Pt = (1,000)(30) = 30,000\text{ J} = 30\text{ kJ}$$

**(d)** At 80% efficiency, the electrical power input is larger than the mechanical power output:
$$P_{\text{input}} = \frac{P_{\text{output}}}{\eta} = \frac{1,000}{0.80} = 1,250\text{ W}$$

The extra 250 W is lost as thermal energy in the motor's windings and bearings.

---

### Answer 5 — IB-Style Full Solution with Mark Scheme

**(a)** Mechanical energy lost (2 marks)

Initial mechanical energy (at A, starting from rest):
$$E_A = mgh = (80)(10)(25) = 20,000\text{ J}$$

Final mechanical energy (at B, all kinetic):
$$E_B = \frac{1}{2}mv^2 = \frac{1}{2}(80)(18)^2 = 40 \times 324 = 12,960\text{ J}$$

Energy lost: $\Delta E = 20,000 - 12,960 = 7,040\text{ J} \approx 7.0\text{ kJ}$

1 mark for calculating both initial and final mechanical energies. 1 mark for correct energy loss. Accept answers in the range 7,000–7,100 J depending on rounding.

**(b)** Average resistive force (2 marks)

The work done by the resistive force equals the energy lost. The force acts along the entire 150 m slope, opposite to the direction of motion:
$$W = F_{\text{res}} \times d$$
$$7,040 = F_{\text{res}} \times 150$$
$$F_{\text{res}} = 47\text{ N}$$

1 mark for relating work done to energy lost. 1 mark for correct force with unit.

**(c)** Maximum steady speed on level road (3 marks)

At steady speed on the level, the net force is zero, so the driving force equals the resistive force: $F_{\text{drive}} = 47\text{ N}$.

Using $P = Fv$:
$$200 = 47 \times v$$
$$v = \frac{200}{47} = 4.26\text{ m s}^{-1} \approx 4.3\text{ m s}^{-1}$$

Breakdown: 1 mark for recognising that driving force equals resistive force at steady speed. 1 mark for using $P = Fv$. 1 mark for correct speed with unit.

**(d)** Reason for difference in resistive force (2 marks)

On the slope, the cyclist's speed was higher (she reached 18 m s⁻¹), which means air resistance would have been significantly larger because air resistance increases with speed (approximately proportional to $v^2$). On the level road at 4.3 m s⁻¹, air resistance is much smaller. Alternatively: the normal reaction force is smaller on a slope (it is $mg\cos\theta$ rather than $mg$), which would reduce friction between tyres and road slightly.

1 mark for a valid physical reason. 1 mark for explaining why this would change the resistive force. Accept any physically sound reasoning.

---

## Key Takeaways

1. **Work is force × displacement × cosine of the angle between them.** Work can be positive, negative, or zero depending on the direction of the force relative to the motion.

2. **The work-energy theorem** ($W_{\text{net}} = \Delta E_k$) is often the fastest way to solve problems involving changes in speed along a known distance.

3. **Energy is conserved** — it transforms between kinetic, gravitational potential, elastic potential, and thermal forms, but the total never changes.

4. **Power is the rate of energy transfer.** For a constant force at constant velocity, $P = Fv$. This is an essential formula for vehicle and motor problems.

5. **Efficiency is always less than 1 in real systems.** The "lost" energy is not destroyed — it becomes thermal energy, which is why machines get warm.
