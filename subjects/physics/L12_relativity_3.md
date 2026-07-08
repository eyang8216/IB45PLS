# Lesson 12: Special Relativity III — Spacetime Diagrams (HL)

## What You'll Learn
- Draw and interpret Minkowski spacetime diagrams ($ct$ vs. $x$)
- Identify worldlines for stationary objects, moving objects, and light
- Understand light cones and causality
- Determine simultaneity in different reference frames using diagrams

---

## 1. What Is a Spacetime Diagram?

### 1.1 Uniting Space and Time

In Newtonian physics, space and time are separate. In special relativity, they are woven together into a four-dimensional fabric called spacetime. A Minkowski diagram simplifies this to two dimensions: one spatial ($x$, horizontal) and one temporal ($ct$, vertical). We plot $ct$ rather than $t$ so both axes have units of distance (metres), and so light rays travel at $45^\circ$.

### 1.2 Worldlines — The Path Through Spacetime

Every object traces a path through spacetime called a **worldline**:
- A stationary object: vertical line (position constant, time advances)
- An object moving at constant velocity: straight diagonal line (steeper = slower)
- Light: diagonal at exactly $45^\circ$ (one unit of space per unit of time — speed $c$)
- An accelerating object: curved line

The slope of a worldline tells you the speed: $v/c = \Delta x/\Delta (ct) = \text{slope}$.

---

## 2. Light Cones — The Geometry of Causality

### 2.1 What a Light Cone Is

At any event (point in spacetime) $A$, draw lines at $45^\circ$ representing light rays emanating in both directions. These form the **light cone**. The interior of the future light cone contains all events that could possibly be influenced by $A$ (signals travelling at $v \leq c$ can reach them). The interior of the past light cone contains all events that could have influenced $A$.

Events OUTSIDE the light cone cannot have any causal connection with $A$ — no signal, no matter how fast, could travel between them without exceeding $c$. Such events are "spacelike separated."

### 2.2 Causality Is Preserved

Special relativity never violates causality. If event $A$ causes event $B$, then $B$ must be inside or on $A$'s future light cone in ALL inertial frames. Different observers may disagree about the time interval between $A$ and $B$, but they all agree that $A$ came first. The order of causally connected events is invariant.

---

## 3. Simultaneity on Spacetime Diagrams

### 3.1 The Relativity of Simultaneity

Two events that are simultaneous in one frame (same $ct$) are NOT simultaneous in another frame moving relative to the first. On a Minkowski diagram, the $x$-axis of the moving frame is tilted relative to the stationary frame. Events that lie on a horizontal line in the stationary frame do NOT lie on the moving frame's $x'$-axis — they have different $ct'$ coordinates.

### 3.2 The Train-and-Platform Example

A passenger at the centre of a moving train sees lightning strike both ends simultaneously. An observer on the platform sees the strike at the REAR of the train first, then the strike at the FRONT. Both are correct — simultaneity depends on reference frame. On the diagram: the two lightning strikes are on the same horizontal line in the train frame but on a tilted line in the platform frame.

---

## Worked Examples

### Worked Example 12.1 — Drawing Worldlines

**Problem:** On a Minkowski diagram, draw worldlines for: (a) a particle at rest at $x = 2$, (b) a particle moving right at $0.5c$ passing $x = 0$ at $t = 0$, (c) a light pulse emitted from $x = 0$ at $t = 0$ travelling right.

**Solution:**
(a) Vertical line at $x = 2$.
(b) Straight line through origin with slope $\Delta x/\Delta(ct) = 0.5$, so rise of 1 unit $ct$ per 2 units $x$.
(c) Line at $45^\circ$ through origin (slope = 1).

---

### Worked Example 12.2 — Causality

**Problem:** Event A occurs at $(x=0, ct=0)$. Event B occurs at $(x=8, ct=5)$. Could event A have caused event B? Could event B have caused event A?

**Solution:**
Slope from A to B = $\Delta x/\Delta(ct) = 8/5 = 1.6 > 1$. This exceeds the $45^\circ$ light cone — the events are spacelike separated. Neither could have caused the other; no signal could travel from one to the other in time. They are causally disconnected.

---

### Worked Example 12.3 — IB-Style Simultaneity

**Problem:** In frame S, event P is at $(x=0, ct=0)$ and event Q is at $(x=6, ct=4)$. Frame S' moves at $0.60c$ in the $+x$ direction. Show that P and Q are not simultaneous in S'.

**Solution:**
Lorentz transformation: $ct' = \gamma(ct - \beta x)$ where $\beta = v/c = 0.60$, $\gamma = 1.25$.

For event P: $ct'_P = 1.25(0 - 0.60 \times 0) = 0$.
For event Q: $ct'_Q = 1.25(4 - 0.60 \times 6) = 1.25(4 - 3.6) = 1.25(0.4) = 0.5$.

$ct'_P \neq ct'_Q$ → events are NOT simultaneous in S'. Q occurs after P in S'.

---

## Practice Problems

### Problem 1
Draw worldlines for: a train at rest, a bird flying at $0.3c$, and a light signal. Label your axes.

### Problem 2
Event A is at $(0, 0)$, event B at $(3, 4)$. Can A and B be causally connected? Explain using the light cone.

### Problem 3
Two lightning strikes are simultaneous in Earth's frame, occurring at $x = 0$ and $x = 10\text{ ls}$ (light-seconds). A spaceship moves at $0.8c$ in the $+x$ direction. Which strike occurs first in the ship's frame? Use $\gamma = 1.667$.

### Problem 4
Explain why a particle travelling faster than $c$ would lead to violations of causality.

### Problem 5 — IB-Style
A spacetime diagram has axes $x$ and $ct$. Frame S' moves at $0.50c$ relative to S.

(a) On the diagram, draw the $ct'$ and $x'$ axes for frame S'. (2 marks)
(b) Event P is at $(x=2, ct=3)$ in frame S. Using the Lorentz transformations, find the coordinates of P in frame S'. (3 marks)
(c) Verify that the spacetime interval $(\Delta s)^2 = (c\Delta t)^2 - (\Delta x)^2$ has the same value in both frames. (2 marks)

---

## Answers

### Answer 1
Train at rest: vertical line. Bird at $0.3c$: straight line with slope 0.3 (less steep than $45^\circ$). Light: $45^\circ$ line. All lines labelled.

### Answer 2
Slope $= 3/4 = 0.75 < 1$. B is inside A's future light cone. Yes, they can be causally connected — a signal travelling at $0.75c$ could go from A to B.

### Answer 3
$ct' = \gamma(ct - \beta x) = 1.667(ct - 0.8x)$. For $x=0$: $ct' = 1.667ct$. For $x=10$: $ct' = 1.667(ct - 8) < 1.667ct$. The strike at $x=10$ occurs EARLIER in the ship's frame.

### Answer 4
A particle faster than $c$ would travel outside the light cone — spacelike separated events could become causally connected. In some frames, the effect would precede the cause (the particle would arrive before it departed). This violates the fundamental principle that causes must precede effects. The speed of light limit preserves causality.

### Answer 5 — IB-Style
**(a)** (2 marks) $ct'$ axis: line $x = 0.50(ct)$ (slope 0.5 in $x$–$ct$ coordinates). $x'$ axis: line $ct = 0.50x$ (slope 2). Both symmetric about the $45^\circ$ line.

**(b)** (3 marks) $\gamma = 1/\sqrt{1-0.25} = 1.155$. $x' = \gamma(x - \beta ct) = 1.155(2 - 0.50 \times 3) = 1.155(2 - 1.5) = 0.578$. $ct' = \gamma(ct - \beta x) = 1.155(3 - 0.50 \times 2) = 1.155(3 - 1) = 2.31$. P' = $(0.578, 2.31)$.

**(c)** (2 marks) In S: $\Delta s^2 = 3^2 - 2^2 = 9 - 4 = 5$. In S': $\Delta s^2 = 2.31^2 - 0.578^2 = 5.34 - 0.334 = 5.0$. Same — the interval is invariant.

---

## Key Takeaways

1. **Minkowski diagram:** $ct$ vs. $x$. Worldlines show paths through spacetime. Slope gives speed relative to $c$.

2. **Light cone:** $45^\circ$ lines. Events inside can be causally connected. Events outside cannot.

3. **Simultaneity is relative.** Events simultaneous in one frame have different times in another.

4. **Lorentz transformations** convert coordinates between frames. The spacetime interval $(\Delta s)^2 = (c\Delta t)^2 - (\Delta x)^2$ is invariant.
