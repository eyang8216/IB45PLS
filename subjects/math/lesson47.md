# Lesson 47: Solving Trigonometric Equations

## What Is This Topic?

A **trigonometric equation** is any equation that contains a trigonometric function — like sin x, cos x, or tan x — with the unknown angle x. Solving such an equation means finding every angle (in a given range) that makes the equation true. For example, "sin x = 0.5" is a trigonometric equation, and its solutions are all angles whose sine equals one half.

## Why Do We Learn This?

Trigonometric equations appear whenever something repeats in a cycle: sound waves, tides, the swing of a pendulum, alternating electric current, and satellite orbits all involve periodic motion described by sine and cosine. If you want to know *when* a wave reaches a certain height, you are solving a trigonometric equation. In the IB exam, you will often be told to find all solutions in the interval [0, 2π] (radians) or [0°, 360°] (degrees).

## Key Terms Defined

A **principal value** is the first solution your calculator gives you — it is the simplest angle, always chosen from a specific narrow range. For sine, the principal value falls between −π/2 and π/2. For cosine, between 0 and π. For tangent, between −π/2 and π/2.

The **unit circle** is a circle of radius 1 centered at the origin. An angle is measured counterclockwise from the positive x‑axis. The x‑coordinate of a point on the unit circle equals cos θ, and the y‑coordinate equals sin θ.

A **reference angle** is the acute (less than 90°) angle between the terminal side of your angle and the x‑axis. It helps you find related solutions in other quadrants.

The **period** of a trig function is how far you must travel along the x‑axis before the function repeats. sin x and cos x have period 2π; tan x has period π.

## Common Misconceptions

Many students think a trigonometric equation has only one answer because their calculator shows one number. However, sine, cosine, and tangent each repeat forever, so an equation like sin x = 0.5 has infinitely many solutions. The IB usually asks for only the solutions that fall inside a specific interval.

Another common error is forgetting to check which quadrants produce the correct sign. If sin x = −0.5, the angle must be in quadrant III or quadrant IV (where sine is negative). Always draw a quick sketch of the unit circle and label which functions are positive in each quadrant.

---

## 1. The General Approach to Solving

When you face a trigonometric equation, follow these steps in order:

**Step 1 — Isolate the trigonometric function.** Rearrange the equation until you have something like sin x = a, cos x = b, or tan x = c.

**Step 2 — Find the principal value.** Use your calculator or your knowledge of exact values to find the first angle that satisfies the equation.

**Step 3 — Find all solutions in the given interval.** Use the symmetry properties of the three functions:

- For **sin x = a**: if the principal value is θ, the second solution in [0, 2π) is π − θ. After that, add multiples of 2π to both base solutions and keep only those inside your interval.
- For **cos x = a**: if the principal value is θ, the second solution is 2π − θ (or equivalently −θ). Then add multiples of 2π.
- For **tan x = a**: if the principal value is θ, all solutions are θ + nπ (where n is any integer). Tangent repeats every π, not every 2π.

---

## 2. Basic Equations — Worked Examples

### Example 1: sin x = 1/2, 0 ≤ x ≤ 2π

**Problem:** Find every angle x between 0 and 2π for which sin x equals one half.

**Approach:** Identify the principal value. Then use the sine symmetry rule: if sin x = a and the principal value is θ, the other solution in one full revolution is π − θ.

The principal value for sin x = 1/2 is x = π/6 (that is 30°). This is because sin(π/6) = 1/2.

The second solution in [0, 2π) is π − π/6 = 5π/6. To check: sin(5π/6) = sin(π/6) = 1/2, and both angles lie inside the required interval.

**Answer:** x = π/6, 5π/6.

**Why this makes sense:** Sine is positive in quadrants I and II. The principal value π/6 is in quadrant I; the mirror angle across the y‑axis, 5π/6, is in quadrant II, where sine is also positive.

---

### Example 2: cos x = −√2/2, 0 ≤ x ≤ 2π

**Problem:** Find all angles x in [0, 2π] for which cos x equals negative root‑two over two.

**Approach:** Ignore the negative sign for a moment and find the reference angle for cos x = √2/2. Then place that reference angle in the quadrants where cosine is negative (quadrants II and III).

The reference angle for cos = √2/2 is π/4 (because cos(π/4) = √2/2).

Cosine is negative in quadrants II and III. In quadrant II, the angle is π − π/4 = 3π/4. In quadrant III, the angle is π + π/4 = 5π/4.

**Answer:** x = 3π/4, 5π/4.

**Why this makes sense:** The cosine function gives the x‑coordinate on the unit circle. That x‑coordinate is negative when the point sits to the left of the y‑axis — exactly quadrants II and III.

---

### Example 3: tan x = √3, 0 ≤ x ≤ 2π

**Problem:** Find all angles x in [0, 2π] for which tan x equals √3.

**Approach:** Find the principal value, then add multiples of π (the period of tangent) until you leave the interval.

The principal value is x = π/3, because tan(π/3) = √3.

Tangent repeats every π, so the next solution is π/3 + π = 4π/3. Adding another π would give 7π/3, which is larger than 2π and therefore outside the required interval.

**Answer:** x = π/3, 4π/3.

**Why this makes sense:** Tangent is positive in quadrants I and III. The principal value π/3 lands in quadrant I; adding half a revolution (π) lands at 4π/3, which is in quadrant III.

---

## 3. Equations That Need Trigonometric Identities

Sometimes the equation contains sin²x, cos 2x, or a mix of different functions. In these cases you need to replace one expression with an equivalent one — this is called using a **trigonometric identity**.

A **trigonometric identity** is a formula that is always true, such as cos(2x) = 1 − 2 sin²x or sin²x + cos²x = 1.

### Example 4: 2 sin²x − sin x − 1 = 0, 0 ≤ x ≤ 2π

**Problem:** Solve the quadratic‑looking equation 2 sin²x − sin x − 1 = 0 for every angle x in [0, 2π].

**Approach:** Treat sin x as a single unknown. Substitute u = sin x to get a standard quadratic: 2u² − u − 1 = 0. Factor it, then solve for u, then find the angles x that give each u‑value.

Factor: 2u² − u − 1 = (2u + 1)(u − 1) = 0. So u = −1/2 or u = 1.

Now return to sin x:

- If sin x = 1, the only angle in [0, 2π] with that sine is x = π/2.
- If sin x = −1/2, sine is negative in quadrants III and IV. The reference angle for sin = 1/2 is π/6. In quadrant III: π + π/6 = 7π/6. In quadrant IV: 2π − π/6 = 11π/6.

**Answer:** x = π/2, 7π/6, 11π/6.

**Why this makes sense:** Replacing sin x with a letter turns a trigonometric puzzle into a familiar algebra problem. After solving the algebra, you translate each answer back to an angle using the unit circle.

---

### Example 5: cos(2x) = sin x, 0 ≤ x ≤ 2π

**Problem:** Solve cos(2x) = sin x for all angles x in [0, 2π].

**Approach:** The equation mixes cosine of a double angle with sine of a single angle. Use the identity cos(2x) = 1 − 2 sin²x to rewrite everything in terms of sin x.

Substitute: 1 − 2 sin²x = sin x → 0 = 2 sin²x + sin x − 1.

Factor: (2 sin x − 1)(sin x + 1) = 0.

- 2 sin x − 1 = 0 gives sin x = 1/2 → x = π/6, 5π/6.
- sin x + 1 = 0 gives sin x = −1 → x = 3π/2.

**Answer:** x = π/6, 5π/6, 3π/2.

**Why this makes sense:** The double‑angle identity converts a "mixed" equation into one that uses only sin x, which you already know how to solve.

---

## 4. Equations with a Multiple Angle — e.g. sin(3x)

When the angle inside the trig function is multiplied by a number (like 3x instead of x), the equation has more solutions squeezed into the same interval, because the function completes its cycle faster.

### Example 6: sin(3x) = 1/2, 0 ≤ x ≤ 2π

**Problem:** Find every angle x between 0 and 2π such that sin(3x) = 1/2.

**Approach:** Introduce a helper variable: let θ = 3x. Solve sin θ = 1/2 first. Then divide each solution for θ by 3 to get x. Finally, keep only the x‑values that fit the original interval.

sin θ = 1/2 → θ = π/6 + 2πn or θ = 5π/6 + 2πn, for any integer n.

Since 0 ≤ x ≤ 2π and x = θ/3, the variable θ must range from 0 to 6π. Now list all θ‑values in [0, 6π]:

From the first family (π/6 + 2πn): π/6, 13π/6, 25π/6.
From the second family (5π/6 + 2πn): 5π/6, 17π/6, 29π/6.

The next value in each family would be π/6 + 6π = 37π/6, which is bigger than 6π, so we stop.

Now divide by 3: x = π/18, 5π/18, 13π/18, 17π/18, 25π/18, 29π/18.

**Answer:** Six solutions: π/18, 5π/18, 13π/18, 17π/18, 25π/18, 29π/18.

**Why this makes sense:** The function sin(3x) oscillates three times as fast as sin x. Therefore, in the same interval [0, 2π], it hits the value 1/2 three times as often — producing six solutions instead of two.

**Common pitfall:** Many students forget to expand the range of θ. If x goes from 0 to 2π, then 3x goes from 0 to 6π. Always multiply the interval endpoints by the coefficient.

---

## 5. The Auxiliary Angle (R Method)

An equation like a sin x + b cos x = c cannot be solved by isolating a single trig function directly. Instead, you combine the left side into a single sine (or cosine) wave.

The rule: **a sin x + b cos x = R sin(x + α)**, where R = √(a² + b²) and tan α = b/a (with α chosen in the correct quadrant based on the signs of a and b).

### Example 7: sin x + √3 cos x = 1, 0 ≤ x ≤ 2π

**Problem:** Solve sin x + √3 cos x = 1 for all angles x in [0, 2π].

**Approach:** Identify a = 1, b = √3. Compute R and α, rewrite the left side, then solve the resulting simple sine equation.

R = √(1² + (√3)²) = √(1 + 3) = 2.

tan α = √3/1 = √3 → α = π/3 (since both a and b are positive, α is in quadrant I).

The original equation becomes: 2 sin(x + π/3) = 1 → sin(x + π/3) = 1/2.

Now solve sin(θ) = 1/2 where θ = x + π/3:

θ = π/6 + 2πn or θ = 5π/6 + 2πn.

So x = π/6 − π/3 + 2πn = −π/6 + 2πn, or x = 5π/6 − π/3 + 2πn = π/2 + 2πn.

Now choose n so that x falls in [0, 2π]:

- From x = −π/6 + 2πn: n = 1 gives x = −π/6 + 2π = 11π/6. n = 0 gives −π/6 (negative — discard). n = 2 gives 23π/6 (too big).
- From x = π/2 + 2πn: n = 0 gives π/2. n = 1 gives 5π/2 (too big).

**Answer:** x = π/2, 11π/6.

**Why this makes sense:** The R‑method collapses a sum of two different trig functions into a single shifted sine wave. Once you have a single trig function isolated, you fall back on the basic method from Section 2.

---

## Practice Problems

**Problem 1:** Solve cos x = 1/2 for all angles x in the interval [0, 2π].

**Problem 2:** Solve 2 sin²x = 1 for all angles x in the interval [0, 2π]. Think carefully: what happens when you take the square root?

**Problem 3:** Solve tan²x − 3 = 0 for all angles x in the interval [0, 2π].

**Problem 4:** Solve sin(2x) = cos x for all angles x in the interval [0, 2π]. You will need the double‑angle identity sin(2x) = 2 sin x cos x and then factor.

**Problem 5 (IB Exam Style — 6 marks):** A water depth in a harbour is modelled by D(t) = 3 sin t + 4 cos t + 10, where t is the time in hours after midnight and D is depth in metres.
(a) Express 3 sin t + 4 cos t in the form R sin(t + α). [3 marks]
(b) Hence find all times between midnight and noon when the depth is exactly 12 metres. Give answers to the nearest minute. [3 marks]

**Problem 6:** Solve cos(2x) + cos x = 0 for all angles x in the interval [0, 2π]. Use the identity cos(2x) = 2 cos²x − 1.

---

## Answers

**Answer 1:** Cosine is positive in quadrants I and IV. The principal value for cos x = 1/2 is π/3 (quadrant I). The other solution in [0, 2π) is 2π − π/3 = 5π/3 (quadrant IV). So x = π/3, 5π/3.

**Answer 2:** Divide both sides by 2: sin²x = 1/2. Take the square root: sin x = ±1/√2. **Pitfall:** the square root introduces both a positive and a negative branch — many students forget the negative branch.

For sin x = 1/√2, the principal value is π/4; the second solution is π − π/4 = 3π/4.
For sin x = −1/√2, the principal value is −π/4, which becomes 7π/4 in [0, 2π); the second solution is π − (−π/4) = 5π/4.

All four solutions: x = π/4, 3π/4, 5π/4, 7π/4.

**Answer 3:** tan²x = 3 → tan x = ±√3. For tan x = √3: principal value π/3, then π/3 + π = 4π/3. For tan x = −√3: principal value −π/3, which becomes 2π/3 in [0, 2π) by adding π; the next is 2π/3 + π = 5π/3. So x = π/3, 2π/3, 4π/3, 5π/3.

**Answer 4:** Use sin(2x) = 2 sin x cos x to rewrite: 2 sin x cos x = cos x. Bring everything to one side: 2 sin x cos x − cos x = 0 → cos x(2 sin x − 1) = 0. **Pitfall:** do not divide both sides by cos x — you would lose the solutions where cos x = 0. Instead, factor.

- cos x = 0 → x = π/2, 3π/2.
- 2 sin x − 1 = 0 → sin x = 1/2 → x = π/6, 5π/6.

All solutions: x = π/6, π/2, 5π/6, 3π/2.

**Answer 5:**
(a) R = √(3² + 4²) = √(9 + 16) = √25 = 5. tan α = 4/3 → α = arctan(4/3) ≈ 0.9273 radians. Since both coefficients are positive, α is in quadrant I. So 3 sin t + 4 cos t = 5 sin(t + 0.9273).

(b) D(t) = 12 → 5 sin(t + 0.9273) + 10 = 12 → 5 sin(t + 0.9273) = 2 → sin(t + 0.9273) = 0.4.

sin θ = 0.4 → θ = arcsin(0.4) ≈ 0.4115 or θ = π − 0.4115 ≈ 2.7301.

So t + 0.9273 = 0.4115 + 2πn or t + 0.9273 = 2.7301 + 2πn.

t = 0.4115 − 0.9273 = −0.5158 (discard — before midnight) or t = 2.7301 − 0.9273 = 1.8028.

Add 2π to the negative solution: t = −0.5158 + 2π ≈ 5.7674.

Both 1.8028 and 5.7674 fall between 0 and 12 (noon).

Converting: 1.8028 hours = 1 hour 48 minutes (0.8028×60 ≈ 48). 5.7674 hours = 5 hours 46 minutes (0.7674×60 ≈ 46).

**Interpretation:** The depth reaches 12 metres at approximately 1:48 am and 5:46 am.

**Answer 6:** Substitute cos(2x) = 2 cos²x − 1: 2 cos²x − 1 + cos x = 0 → 2 cos²x + cos x − 1 = 0. Factor: (2 cos x − 1)(cos x + 1) = 0.

- 2 cos x − 1 = 0 → cos x = 1/2 → x = π/3, 5π/3.
- cos x + 1 = 0 → cos x = −1 → x = π.

All solutions: x = π/3, π, 5π/3.
