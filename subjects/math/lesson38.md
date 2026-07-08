# Lesson 38: Optimization Problems — Using Derivatives to Find Best Values

## What is Optimization?

**Optimization** means finding the best possible value of something — the **maximum** (largest) or the **minimum** (smallest). In real life, you might want to maximize profit, minimize cost, maximize area given a fixed amount of fencing, or minimize the material needed to make a can that holds a certain volume.

## Why Learn This?

Optimization problems appear frequently on the IB AAHL exam. They test whether you can take a real-world situation, turn it into a mathematical function, and then use derivatives (which you learned in earlier lessons) to find where that function reaches its highest or lowest point. The diagnostic test showed this is an area that needs more practice — so let's build it from the ground up.

## What is a Derivative? (Brief Reminder)

A **derivative** of a function f(x) tells you the slope of the function at any point x. When a function reaches a maximum or minimum, the slope is zero — the graph is flat at that moment. So to find maximum or minimum values, we find where the derivative equals zero. These points are called **critical points**.

## The General Strategy

Here is a step-by-step method for every optimization problem. Keep this list handy.

1. **Draw a picture.** Sketch the situation and label everything you know.
2. **Name your variables.** Write down what each letter stands for (e.g., let x = width in meters).
3. **Write the quantity you want to optimize** (area, volume, cost, distance) as an expression involving your variables.
4. **Find a constraint** — a piece of information that relates your variables (e.g., total fencing = 400m, or a point lies on a circle). Use the constraint to rewrite your expression so it uses **only one variable**.
5. **State the domain** — what values can that one variable realistically take? (e.g., a length cannot be negative or exceed the total available amount.)
6. **Differentiate** the single-variable function and set the derivative equal to zero. Solve for the variable. These solutions are your critical points.
7. **Test each critical point** to decide if it gives a maximum or a minimum. You can use the second derivative: if f''(x) < 0, the point is a maximum; if f''(x) > 0, it is a minimum. You should also check the endpoints of the domain — sometimes the best value happens at an edge, not where the derivative is zero.
8. **Answer in context.** State what the dimensions are, with units. Don't stop at "x = 5" — say "the width is 5 meters and the height is 3 meters."

---

## Worked Example 1: Rectangle in a Semicircle

**Problem:** A rectangle is placed inside a semicircle of radius R. The base of the rectangle lies on the diameter of the semicircle, and the top two corners touch the curved edge. Find the width and height of the rectangle that give the largest possible area.

**Approach:** We will follow the 8-step strategy.

**Step 1 — Draw and label.** Picture a semicircle sitting on the x-axis, centered at the origin. The rectangle sits inside it, with its base on the x-axis. Let the rectangle extend from −w to w horizontally, so its full width is 2w. Let its height be h.

**Step 2 — Name variables.**
- Let w = half the width of the rectangle (so full width = 2w).
- Let h = height of the rectangle.
- R is the radius of the semicircle (a constant).

**Step 3 — Quantity to optimize.** We want to maximize the area A.
A = (full width) × (height) = 2w × h = 2wh.

**Step 4 — Find and use the constraint.** The top-right corner of the rectangle sits at the point (w, h). This point must lie on the semicircle. The equation of a circle of radius R centered at the origin is x² + y² = R². Since the top-right corner is on this circle: w² + h² = R².

Solve for h in terms of w:
h = √(R² − w²).

Substitute into the area:
A = 2w × √(R² − w²) = 2w(R² − w²)^(1/2).

Now area is a function of one variable: A(w) = 2w(R² − w²)^(1/2).

**Step 5 — Domain.** w is a horizontal distance from the center to the side of the rectangle. It cannot be negative or larger than R (the radius). So 0 ≤ w ≤ R.

**Step 6 — Differentiate and find critical points.** We use the product rule: if A(w) = u × v with u = 2w and v = (R² − w²)^(1/2), then A'(w) = u'v + uv'.

u' = 2.
v' = (1/2)(R² − w²)^(−1/2) × (−2w) = −w / √(R² − w²).

So:
A'(w) = 2 × √(R² − w²) + 2w × [−w / √(R² − w²)]
A'(w) = 2√(R² − w²) − 2w² / √(R² − w²).

Set A'(w) = 0:
2√(R² − w²) = 2w² / √(R² − w²).

Multiply both sides by √(R² − w²):
2(R² − w²) = 2w².
R² − w² = w².
R² = 2w².
w² = R²/2.
w = R/√2. (We take the positive root since w is a distance.)

**Step 7 — Confirm it is a maximum.** We could use the second derivative, but there is a simpler check: at the endpoints w = 0 and w = R, the area is zero (if w = 0, width is 0; if w = R, height is 0). Since the area is positive at w = R/√2, and the endpoints give zero, this critical point must be the maximum.

**Step 8 — Answer in context.**
Half-width = R/√2, so full width = 2R/√2 = R√2.
Height: h = √(R² − R²/2) = √(R²/2) = R/√2.

**Answer:** The rectangle with maximum area has width = R√2 and height = R/√2. Notice the width is exactly twice the height.

**Why this makes sense:** A very wide, flat rectangle has almost no height. A very tall, thin rectangle has almost no width. The best shape balances width and height so the rectangle stretches far into the curved part of the semicircle — and the math tells us the optimal width-to-height ratio is 2:1.

---

## Worked Example 2: Fencing Against a Wall

**Problem:** A farmer owns 400 meters of fencing. She wants to build a rectangular pen against a long, straight barn wall, so only three sides need fencing (the barn wall serves as the fourth side). What dimensions give the largest possible area for the pen?

**Approach:** Two sides perpendicular to the wall, one side parallel to it.

**Step 1 — Draw.** Picture a rectangle where one long side is the barn wall. The other three sides are made of fencing.

**Step 2 — Name variables.**
- Let x = length of each of the two sides perpendicular to the wall (in meters).
- Let y = length of the side parallel to the wall (in meters).

**Step 3 — Quantity to optimize.** We want to maximize the area A = x × y.

**Step 4 — Use the constraint.** Total fencing used is 2x + y = 400 (the two x sides plus the one y side). Solve for y:
y = 400 − 2x.

Substitute into area:
A(x) = x(400 − 2x) = 400x − 2x².

**Step 5 — Domain.** x must be at least 0 and cannot exceed 200 (because if x > 200, then y = 400 − 2x would be negative, which is meaningless for a length). So 0 ≤ x ≤ 200.

**Step 6 — Differentiate.**
A'(x) = 400 − 4x.

Set A'(x) = 0:
400 − 4x = 0 → 4x = 400 → x = 100.

**Step 7 — Confirm maximum.** A''(x) = −4, which is negative for all x. A negative second derivative means the function is curving downward, so x = 100 gives a maximum. Also check endpoints: if x = 0, area = 0; if x = 200, y = 0, area = 0. So x = 100 is definitely the maximum.

**Step 8 — Answer.** x = 100 m, so y = 400 − 2(100) = 200 m. Maximum area = 100 × 200 = 20,000 m².

**Answer:** The pen should be 100 m deep (perpendicular to the wall) and 200 m wide (parallel to the wall). The maximum area is 20,000 square meters.

**Why this makes sense:** If you make the pen very deep (large x), you use up fencing on the sides and have little left for the long parallel side. If you make it very wide (large y), the sides become tiny. The optimum splits the fencing so that the single parallel side gets half the total fencing (200 m) and the two perpendicular sides share the other half (100 m each).

---

## Worked Example 3: Box Made by Cutting Corners

**Problem:** You have a square sheet of cardboard measuring 12 cm by 12 cm. From each corner, you cut out a square of side length x cm. Then you fold up the four flaps to make an open-top box. What value of x gives the largest possible volume for the box?

**Approach:** After cutting out squares of side x from each corner, the base of the box becomes a square of side (12 − 2x), and the height of the box is x.

**Volume function:**
V(x) = (base side)² × height = (12 − 2x)² × x.

Expand (12 − 2x)²:
(12 − 2x)² = 144 − 48x + 4x².

So:
V(x) = x(144 − 48x + 4x²) = 144x − 48x² + 4x³.

**Domain:** x is the size of the cut-out square. It must be at least 0 and cannot exceed 6 (if x = 6, the entire sheet is cut away). So 0 ≤ x ≤ 6.

**Differentiate:**
V'(x) = 144 − 96x + 12x².

Factor out 12:
V'(x) = 12(x² − 8x + 12).

Factor the quadratic: x² − 8x + 12 = (x − 2)(x − 6).

So V'(x) = 12(x − 2)(x − 6).

Set V'(x) = 0: x = 2 or x = 6.

**Check which is the maximum:**
- At x = 6, the volume is V(6) = 6 × (0)² = 0. This is the minimum (a flat box with no base).
- At x = 2: use the second derivative.
V''(x) = −96 + 24x.
V''(2) = −96 + 48 = −48, which is negative. So x = 2 gives a maximum.

**Answer:** Cut squares of side 2 cm from each corner. The resulting box has a base of 8 cm × 8 cm and a height of 2 cm. Maximum volume = 8 × 8 × 2 = 128 cm³.

**Why this makes sense:** If you cut tiny squares (x near 0), you have a wide base but almost no height, so the volume is tiny. If you cut large squares (x near 6), you get a tall box but the base shrinks to almost nothing. The optimum balances base area against height, which happens when x = 2.

---

## Worked Example 4: Cylinder Inside a Sphere

**Problem:** Find the dimensions of the cylinder with the largest possible volume that can fit completely inside a sphere of radius R. The cylinder's axis aligns with a diameter of the sphere.

**Approach:** Draw a cross-section through the center. You see a rectangle (the cylinder's side view) inscribed in a circle of radius R. The rectangle has width 2r (the cylinder's diameter) and height 2h (the cylinder's total height).

**Constraint:** The top-right corner of the rectangle, at (r, h), must lie on the circle: r² + h² = R². Solve for r²: r² = R² − h².

**Volume to maximize:**
V = πr² × (total height) = π(R² − h²) × 2h = 2π(R²h − h³).

So V(h) = 2π(R²h − h³), with domain 0 ≤ h ≤ R.

**Differentiate:**
V'(h) = 2π(R² − 3h²).

Set V'(h) = 0:
R² − 3h² = 0 → h² = R²/3 → h = R/√3.

**Check maximum:** V''(h) = 2π(−6h) = −12πh, which is negative for h > 0. So h = R/√3 gives a maximum.

**Find r:** r² = R² − R²/3 = 2R²/3, so r = R√(2/3).

**Answer:** The cylinder of maximum volume has radius r = R√(2/3) and height = 2h = 2R/√3.

---

## Common Misconceptions

**Misconception 1:** "The derivative being zero always means I found the answer." Actually, the derivative being zero only gives you **critical points**. A critical point could be a maximum, a minimum, or neither (a point of inflection). You must always test — using the second derivative or checking endpoints.

**Misconception 2:** "I only need to check where the derivative is zero." The maximum or minimum could happen at the **endpoint** of the domain, where the derivative may not be zero. Always check endpoints.

**Misconception 3:** "Variables can be anything." Every variable in an optimization problem has a real-world meaning (length, area, time). This limits what values it can take. Always write down the domain.

---

## Practice Problems

**1.** Find two positive numbers whose product is 100 and whose sum is as small as possible. (Hint: let the numbers be x and 100/x. Then minimize the sum S(x) = x + 100/x.)

**2.** You need to design a rectangular box with a square base and no top. The box must have a volume of 32,000 cm³. Find the dimensions (side of square base and height) that use the smallest possible amount of material — that is, minimize the surface area. (Hint: if the square base has side x and the height is h, then volume = x²h = 32,000 and surface area = x² + 4xh.)

**3.** Find the point on the curve y = √x that is closest to the point (3, 0). (Hint: instead of minimizing distance, you can minimize the square of the distance. The distance squared from a point (x, √x) to (3, 0) is D = (x − 3)² + (√x − 0)². Work with D as your function to minimize.)

**4.** A wire 60 cm long is cut into two pieces. One piece is bent into a square, the other into an equilateral triangle. How should you cut the wire to maximize the total enclosed area? (Important: check the endpoints — the maximum might occur when all the wire goes to one shape.)

**5. [IB Exam Style — 7 marks]** A company manufactures cylindrical cans with both a top and a bottom. Each can must hold exactly 1000 cm³ of liquid.

(a) Let the radius be r cm and the height be h cm. Write an equation relating r and h to the volume. [1 mark]

(b) Write an expression for the total surface area S of the can (including top and bottom) in terms of r and h. [1 mark]

(c) Use the volume constraint to express h in terms of r, and then write S as a function of r alone. [2 marks]

(d) Find the radius that minimizes the surface area. [2 marks]

(e) Find the ratio of height to radius (h : r) for the can with minimal surface area. [1 mark]

---

## Answers

**1.** Let the numbers be x and y, with xy = 100, so y = 100/x. Sum S(x) = x + 100/x, with domain x > 0. S'(x) = 1 − 100/x². Set S'(x) = 0: 1 = 100/x² → x² = 100 → x = 10 (positive solution). Then y = 10. S''(x) = 200/x³, and S''(10) = 200/1000 = 0.2 > 0, so it is a minimum. The two numbers are 10 and 10, and the minimum sum is 20.

**Why this makes sense:** For a fixed product, the sum is smallest when the two numbers are equal. This is a general principle: symmetry often gives the optimum.

**2.** Volume: x²h = 32,000, so h = 32,000/x². Surface area A = x² + 4xh = x² + 4x(32,000/x²) = x² + 128,000/x. Domain: x > 0. A'(x) = 2x − 128,000/x². Set A'(x) = 0: 2x = 128,000/x² → 2x³ = 128,000 → x³ = 64,000 → x = ³√64,000 = 40. Then h = 32,000/1,600 = 20. A''(40) = 2 + 256,000/64,000 = 6 > 0, so minimum. Dimensions: base 40 cm × 40 cm, height 20 cm.

**3.** Let D(x) = (x − 3)² + (√x)² = (x − 3)² + x = x² − 6x + 9 + x = x² − 5x + 9. Domain: x ≥ 0. D'(x) = 2x − 5. Set D'(x) = 0: x = 2.5. D''(x) = 2 > 0, so minimum. The point is (2.5, √2.5) ≈ (2.5, 1.581).

**4.** Let x cm go to the square. The square has perimeter x, so side = x/4, area = (x/4)² = x²/16. The remaining (60 − x) cm goes to the equilateral triangle. The triangle has 3 equal sides, so each side = (60 − x)/3. The area of an equilateral triangle with side s is (√3/4)s², so triangle area = (√3/4) × ((60 − x)/3)² = (√3/4) × (60 − x)²/9 = √3(60 − x)²/36. Total area A(x) = x²/16 + √3(60 − x)²/36, domain 0 ≤ x ≤ 60. A'(x) = x/8 − √3(60 − x)/18. Set A'(x) = 0: x/8 = √3(60 − x)/18 → 18x = 8√3(60 − x) → 18x = 480√3 − 8√3·x → x(18 + 8√3) = 480√3 → x ≈ 24.3. This is a **minimum** (check A'': positive). The endpoints: if x = 60 (all square), area = 3600/16 = 225. If x = 0 (all triangle), area = √3(3600)/36 = 100√3 ≈ 173.2. Since the critical point is a minimum, the **maximum** happens at an endpoint: x = 60. **Answer:** Use all 60 cm for the square — do not cut the wire at all. Maximum area = 225 cm².

**Pitfall:** Many students find the critical point and stop. Always check endpoints when the domain is closed. The derivative finds interior optima; the boundary might be better.

**5. [IB Exam Style — Answers]**

(a) Volume = πr²h = 1000. [1 mark]

(b) S = 2πr² (top and bottom) + 2πrh (curved side). [1 mark]

(c) From (a): h = 1000/(πr²). Substitute into S: S(r) = 2πr² + 2πr × (1000/(πr²)) = 2πr² + 2000/r. [2 marks]

(d) S'(r) = 4πr − 2000/r². Set S'(r) = 0: 4πr = 2000/r² → 4πr³ = 2000 → r³ = 500/π → r = ³√(500/π). [2 marks]

(e) Find h: h = 1000/(πr²). Ratio h/r = [1000/(πr²)] / r = 1000/(πr³). Substitute r³ = 500/π: h/r = 1000/(π × 500/π) = 1000/500 = 2. So h : r = 2 : 1. The height equals the diameter. [1 mark]
