# Lesson 50: Volumes of Revolution

## What Is This Topic?

A **volume of revolution** is the three‑dimensional shape you get when you take a flat region (an area under a curve) and spin it around a straight axis. The resulting solid is symmetric around that axis — like a vase spun on a potter's wheel, or a wine glass, or a bullet.

To calculate the volume of such a solid, we use integration. The idea is to slice the solid into infinitely many thin disks (or washers) perpendicular to the axis of rotation, find the volume of each tiny slice, and add them all up with an integral.

## Why Do We Learn This?

Volumes of revolution appear in engineering whenever you design a rotationally symmetric object — pipes, bottles, pistons, nose cones, storage tanks. Architects use these ideas for domes and arches. In the IB exam, volumes of revolution test your ability to visualize 3D shapes, set up integrals correctly, and handle the algebra of squaring functions.

---

## 1. Rotation About the x‑axis — The Disk Method

Imagine the region under a curve y = f(x), between x = a and x = b, sitting above the x‑axis. Now spin that region 360° around the x‑axis. Each vertical "strip" at position x sweeps out a circular disk of radius f(x) and thickness dx. The volume of one such disk is:

Volume of one disk = π × (radius)² × thickness = π [f(x)]² dx.

Summing all disks from a to b gives the integral:

**V = π ∫ₐᵇ [f(x)]² dx**

### What Each Part Means

- π: the constant that appears in every circle area formula.
- [f(x)]²: the square of the radius. Important: you square the **whole** function, not just x.
- dx: the infinitely thin thickness of each disk.
- The integral sign ∫ with limits a and b: "add up all the disks from x = a to x = b."

### Common Misconceptions

Many students write π ∫ [f(x)] dx (forgetting to square). That would give π times the area under the curve, not the volume. The squaring is essential because volume involves πr², not πr.

Another common error: squaring only part of f(x). If f(x) = x² + 1, then [f(x)]² = (x² + 1)² = x⁴ + 2x² + 1, **not** x⁴ + 1.

### Example 1: y = √x, from x = 0 to x = 4, rotated about the x‑axis

**Problem:** The region under the curve y = √x from x = 0 to x = 4 is rotated 360° about the x‑axis. Find the volume of the resulting solid.

**Approach:** Write the formula V = π ∫₀⁴ [√x]² dx. Notice that [√x]² simplifies to x — this makes the integral very simple.

V = π ∫₀⁴ x dx.

Now integrate: ∫ x dx = x²/2. Evaluate from 0 to 4:

V = π [x²/2]₀⁴ = π [(4²/2) − (0²/2)] = π [16/2 − 0] = π × 8 = 8π.

**Answer:** 8π cubic units.

**Why this makes sense:** The curve y = √x is a sideways parabola. Rotating it produces a shape like a bowl or a satellite dish. The volume 8π is exact; there is no approximation involved.

### Example 2: y = x² + 1, from x = 0 to x = 2, rotated about the x‑axis

**Problem:** Find the volume when the region under y = x² + 1, from x = 0 to x = 2, is rotated about the x‑axis.

**Approach:** Set up V = π ∫₀² (x² + 1)² dx. Expand the square carefully: (x² + 1)² = x⁴ + 2x² + 1.

V = π ∫₀² (x⁴ + 2x² + 1) dx.

Integrate term by term:

∫ x⁴ dx = x⁵/5, ∫ 2x² dx = 2x³/3, ∫ 1 dx = x.

So V = π [x⁵/5 + 2x³/3 + x]₀².

Plug in x = 2:

= π [(32/5) + (16/3) + 2].

Put over common denominator 15: 32/5 = 96/15, 16/3 = 80/15, 2 = 30/15.

Sum = (96 + 80 + 30)/15 = 206/15.

**Answer:** 206π/15 cubic units.

**Why this makes sense:** The function x² + 1 is always at least 1, so the solid is wider than a simple cone. The volume is larger than Example 1 because the radius is bigger everywhere on the interval.

---

## 2. The Washer Method — When There Is a Hole

Sometimes the region being rotated does not touch the axis of rotation — there is a gap. The solid then has a hole through the middle, like a doughnut or a pipe. You handle this by subtracting the volume of the "hole" from the volume of the "outer" solid.

If y = f(x) is the outer curve (further from the axis) and y = g(x) is the inner curve (closer to the axis), the volume is:

**V = π ∫ₐᵇ ([f(x)]² − [g(x)]²) dx**

Think of it as: (volume of the big solid) − (volume of the hole). The π factors out of both terms.

### Important: Which Curve Is Outer?

Between x = a and x = b, the "outer" curve is the one with the **larger y‑value** — the one further from the x‑axis. You must check this for your specific interval. Don't assume that f(x) > g(x) everywhere; sketch or test a point if unsure.

### Example 3: Region Between y = x and y = x², Rotated About the x‑axis

**Problem:** The region bounded by y = x (a straight line) and y = x² (a parabola), from x = 0 to x = 1, is rotated about the x‑axis. Find the volume.

**Approach:** First determine which curve is on top for 0 < x < 1. Test x = 0.5: the line gives y = 0.5; the parabola gives y = 0.25. So y = x is the outer curve and y = x² is the inner curve.

Set up the washer integral:

V = π ∫₀¹ (x² − (x²)²) dx = π ∫₀¹ (x² − x⁴) dx.

Integrate: ∫ x² dx = x³/3, ∫ x⁴ dx = x⁵/5.

V = π [x³/3 − x⁵/5]₀¹ = π [(1/3 − 1/5) − (0 − 0)] = π [(5/15 − 3/15)] = π × 2/15.

**Answer:** 2π/15 cubic units.

**Why this makes sense:** The curves intersect at x = 0 and x = 1, so the region is a "lens" shape. The hole is formed by the parabola rotating; the outer surface comes from the line.

---

## 3. Rotation About the y‑axis

Everything works the same way when you rotate around the y‑axis, but you must express everything in terms of y instead of x. The curve becomes x = g(y), the limits become y‑values, and the integral uses dy.

**V = π ∫_c^d [g(y)]² dy**

where y goes from c to d (the bottom and top of the region).

### Example 4: y = x² Rotated About the y‑axis

**Problem:** The region in the first quadrant bounded by y = x², the x‑axis, and the line x = 3 is rotated about the y‑axis. Find the volume. (The region runs from y = 0 to y = 9, because 3² = 9.)

**Approach:** Solve y = x² for x: x = √y (positive root since we are in the first quadrant). So g(y) = √y, and [g(y)]² = y.

Limits: from y = 0 to y = 9.

V = π ∫₀⁹ y dy = π [y²/2]₀⁹ = π [81/2 − 0] = 81π/2.

**Answer:** 81π/2 cubic units.

**Why this makes sense:** Rotating a parabola about the y‑axis produces a paraboloid — a bowl shape. The volume formula using y is often simpler than using x because the square root disappears when you square g(y).

---

## 4. Choosing the Right Method — A Summary

| Rotation Axis | Variable | Formula |
|---|---|---|
| x‑axis (solid) | dx | π ∫ [f(x)]² dx |
| x‑axis (hollow) | dx | π ∫ ([f(x)]² − [g(x)]²) dx |
| y‑axis (solid) | dy | π ∫ [g(y)]² dy |
| y‑axis (hollow) | dy | π ∫ ([g(y)]² − [h(y)]²) dy |

**Decision rule:** If the axis of rotation is horizontal (like the x‑axis), try using dx and functions of x first. If the axis is vertical (like the y‑axis), try dy and functions of y. But if one choice leads to an easier integral, always prefer the easier one.

---

## 5. Known Cross‑Sections (Bonus Topic)

Sometimes the solid is not formed by rotation at all. Instead, you are told the shape of the cross‑section perpendicular to an axis. If the cross‑sectional area at position x is A(x), then:

**V = ∫ₐᵇ A(x) dx**

### Example 5: Square Cross‑Sections

**Problem:** The base of a solid is the region bounded by y = 4 − x² and the x‑axis (a parabola opening downward, crossing at x = −2 and x = 2). Every cross‑section perpendicular to the x‑axis is a square. Find the volume.

**Approach:** At any position x, the vertical "height" of the base is (4 − x²). Since the cross‑section is a square, the side length equals that height, and the area is (4 − x²)².

A(x) = (4 − x²)² = 16 − 8x² + x⁴.

V = ∫₋₂² (16 − 8x² + x⁴) dx.

Since the integrand is even (all powers are even), we can double the integral from 0 to 2:

V = 2 ∫₀² (16 − 8x² + x⁴) dx = 2 [16x − 8x³/3 + x⁵/5]₀².

At x = 2: 16(2) = 32, 8(8)/3 = 64/3, 32/5.

So [16x − 8x³/3 + x⁵/5]₀² = 32 − 64/3 + 32/5.

Common denominator 15: 32 = 480/15, 64/3 = 320/15, 32/5 = 96/15.

Sum = (480 − 320 + 96)/15 = 256/15.

Then V = 2 × (256/15) = 512/15.

**Answer:** 512/15 cubic units.

**Why this makes sense:** The doubling shortcut works because the shape is symmetric about the y‑axis. Always check for symmetry before computing a long antiderivative from −a to a.

---

## Practice Problems

**Problem 1:** The region under the line y = x from x = 1 to x = 3 is rotated about the x‑axis. Find the volume.

**Problem 2:** The region under the curve y = √x, above the x‑axis, from x = 0 to x = 4, is rotated about the x‑axis. Find the volume.

**Problem 3:** The region bounded by the curves y = x² and y = x (from x = 0 to x = 1) is rotated about the x‑axis. Find the volume.

**Problem 4:** The region bounded by the curve y = ln x, the x‑axis, and the vertical line x = e is rotated about the y‑axis. Find the volume. (You will need to express x in terms of y first.)

**Problem 5 (IB Exam Style — 7 marks):** The region R is bounded by the curve y = eˣ, the lines x = 0 and x = 1, and the x‑axis.
(a) Find the volume when R is rotated 360° about the x‑axis. [3 marks]
(b) Find the volume when R is rotated 360° about the y‑axis. [4 marks]

---

## Answers

**Answer 1:** V = π ∫₁³ x² dx. ∫ x² dx = x³/3. V = π [x³/3]₁³ = π [27/3 − 1/3] = π [9 − 1/3] = π(26/3) = 26π/3.

**Interpretation:** The solid is a truncated cone (a cone with the tip cut off). The volume formula confirms this: the radius grows linearly from 1 to 3, so the shape is a frustum.

**Answer 2:** V = π ∫₀⁴ (√x)² dx = π ∫₀⁴ x dx = π [x²/2]₀⁴ = π(16/2) = 8π.

**Pitfall:** This is the same as Example 1. Notice that [√x]² = x makes the integral trivial. Some students mistakenly write (√x)² = x² — don't do that.

**Answer 3:** The curves intersect at x = 0 and x = 1. For 0 < x < 1, the line y = x is above y = x² (test x = 0.5: 0.5 > 0.25). So outer = x, inner = x².

V = π ∫₀¹ [x² − (x²)²] dx = π ∫₀¹ (x² − x⁴) dx = π [x³/3 − x⁵/5]₀¹ = π(1/3 − 1/5) = π(5/15 − 3/15) = 2π/15.

**Answer 4:** Rotating about the y‑axis means we need x in terms of y. From y = ln x we get x = eʸ. The region goes from y = 0 (where ln x = 0, i.e., x = 1) to y = 1 (where x = e). So:

V = π ∫₀¹ (eʸ)² dy = π ∫₀¹ e²ʸ dy.

∫ e²ʸ dy = (1/2)e²ʸ (by the reverse chain rule: derivative of e²ʸ is 2e²ʸ, so we need 1/2).

V = π [(1/2)e²ʸ]₀¹ = π [(1/2)e² − (1/2)e⁰] = π [(1/2)e² − 1/2] = (π/2)(e² − 1).

**Answer 5:**
(a) About x‑axis: V = π ∫₀¹ (eˣ)² dx = π ∫₀¹ e²ˣ dx.

∫ e²ˣ dx = (1/2)e²ˣ. So V = π [(1/2)e²ˣ]₀¹ = π [(1/2)e² − (1/2)] = (π/2)(e² − 1).

(b) About y‑axis: The region R in terms of y: x ranges from x = 0 to x = 1, so y = eˣ ranges from y = e⁰ = 1 to y = e¹ = e. Also x = ln y. But careful — the region extends left to the y‑axis (x = 0), so the outer radius is x = 1 (a vertical line) and the inner radius is x = ln y (the curve).

This is a washer: outer radius = 1 (the line x = 1), inner radius = ln y (the curve). Limits: y = 1 to y = e.

V = π ∫₁ᵉ [1² − (ln y)²] dy = π ∫₁ᵉ [1 − (ln y)²] dy.

This requires integration by parts for ∫ (ln y)² dy. The result (which you can verify) is:

∫ (ln y)² dy = y(ln y)² − 2y ln y + 2y.

So ∫₁ᵉ [1 − (ln y)²] dy = [y − (y(ln y)² − 2y ln y + 2y)]₁ᵉ = [−y(ln y)² + 2y ln y − y]₁ᵉ.

At y = e: −e(1)² + 2e(1) − e = −e + 2e − e = 0.
At y = 1: −1(0)² + 2(1)(0) − 1 = −1.

So the definite integral = 0 − (−1) = 1.

V = π × 1 = π.

**Interpretation:** The volume when rotated about the y‑axis (π) is much smaller than when rotated about the x‑axis ((π/2)(e² − 1) ≈ 10.04). This makes sense: the region is tall and thin extending away from the y‑axis, producing a narrower solid.
