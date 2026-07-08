# Lesson 49: Radians, Arc Length, and Sector Area

## What Is a Radian?

A **radian** is a way of measuring angles — just like degrees, but based on the radius of a circle instead of the arbitrary number 360.

Imagine you take the radius of a circle and lay it along the circumference (the curved edge). The angle that this arc "opens up" at the center of the circle is **one radian**. More precisely: one radian is the angle at the center of a circle that is cut off by an arc whose length equals the radius.

One full revolution around a circle covers an arc equal to the whole circumference, which is 2πr. Since each radian corresponds to an arc of length r, there are exactly 2π radians in a full circle. This gives us the fundamental conversion:

**π radians = 180°**

From this one equation, every other conversion follows.

## Why Do We Use Radians?

Radians are not just another unit — they are the *natural* unit for angles in mathematics. The reason becomes clear in calculus: the derivative of sin x is cos x **only when x is measured in radians**. If you use degrees, extra conversion factors appear in every derivative and integral.

Radians also simplify formulas for arc length and sector area. In degrees, arc length is (θ/360)·2πr — a messy fraction. In radians, arc length is simply rθ. The radian was invented to make these formulas clean.

In the IB exam, you should default to radians for any problem involving calculus, arc length, or sector area, unless the question specifically uses degrees.

## Converting Between Radians and Degrees

- **Degrees → Radians:** Multiply by π/180.
- **Radians → Degrees:** Multiply by 180/π.

### Exact Values You Should Know Automatically

| Degrees | 0° | 30° | 45° | 60° | 90° | 180° | 270° | 360° |
|---|---|---|---|---|---|---|---|---|
| Radians | 0 | π/6 | π/4 | π/3 | π/2 | π | 3π/2 | 2π |

### Example 1: Conversions

**Problem:** Convert 150° to radians, and convert 3π/4 radians to degrees.

**Approach:** Apply the conversion factor directly.

150° to radians: 150 × (π/180). Simplify: 150/180 = 15/18 = 5/6. So the answer is 5π/6 radians.

3π/4 to degrees: (3π/4) × (180/π). The π cancels: (3/4) × 180 = 540/4 = 135°.

**Why this makes sense:** The factor π/180 is just the number of radians in one degree (≈ 0.01745). Multiplying by it changes the unit without changing the actual angle.

---

## 1. Arc Length

When you have a circle of radius r and a central angle θ (measured in radians), the length of the arc that the angle "cuts out" is:

**s = rθ**

This formula says: arc length equals radius times angle. If the angle is 2π (a full circle), the arc length is r·2π = 2πr, which is the full circumference — exactly as you would expect.

### Example 2: Simple Arc Length

**Problem:** A circle has radius 5 cm. Find the length of the arc cut off by a central angle of π/3 radians.

**Approach:** Substitute into s = rθ.

s = 5 × (π/3) = 5π/3 cm.

**Answer:** 5π/3 cm (approximately 5.24 cm).

### Example 3: Finding the Angle from Arc Length

**Problem:** An arc on a circle of radius 8 cm has length 12 cm. Find the central angle in radians and then convert to degrees.

**Approach:** Rearrange s = rθ to θ = s/r.

θ = 12/8 = 1.5 radians.

To convert to degrees: 1.5 × (180/π) ≈ 1.5 × 57.2958 ≈ 85.94°.

**Answer:** 1.5 radians, approximately 85.9°.

**Why this makes sense:** The angle in radians is literally "how many radii fit along the arc." Here, 1.5 radii fit, so the angle is 1.5 radians.

---

## 2. Sector Area

A **sector** is the "pizza slice" of a circle — the region bounded by two radii and the arc between them. The area of a sector is:

**A = ½ r²θ**

(where θ is in radians)

This formula comes from the idea of proportion: a sector with angle θ takes up the fraction θ/(2π) of the whole circle. The whole circle's area is πr². Multiply: (θ/(2π)) × πr² = ½ r²θ.

### Common Misconceptions

Many students forget the ½ in the formula and write A = r²θ instead. Think of it this way: when θ = 2π (a full circle), the formula must give πr². Now check: ½ r²·(2π) = πr². Correct. If you used r²θ you would get 2πr², which is twice the area of the circle — clearly wrong. The ½ is essential.

Another common error: using degrees in this formula. If θ = 60°, do NOT plug 60 into ½ r²θ. You must convert to radians first (60° = π/3).

### Example 4: Simple Sector Area

**Problem:** Find the area of a sector with radius 6 cm and central angle π/4 radians.

**Approach:** Substitute into A = ½ r²θ.

A = ½ × 6² × (π/4) = ½ × 36 × (π/4) = 18 × (π/4) = 9π/2 cm².

**Answer:** 9π/2 cm² (approximately 14.14 cm²).

### Example 5: Finding the Angle from Sector Area

**Problem:** A sector has area 20 cm² and radius 4 cm. Find the central angle in radians.

**Approach:** Rearrange A = ½ r²θ to θ = 2A / r².

θ = (2 × 20) / 4² = 40/16 = 2.5 radians.

**Answer:** 2.5 radians.

---

## 3. Segment Area

A **segment** is the region between a chord (a straight line connecting two points on the circle) and the arc that joins those same two points. Think of it as a sector with the triangular part removed.

To find the segment area: take the sector area and subtract the area of the triangle formed by the two radii and the chord.

**A_segment = A_sector − A_triangle = ½ r²θ − ½ r² sin θ = ½ r²(θ − sin θ)**

The triangle area formula ½ r² sin θ comes from the general formula for the area of a triangle with two sides of length r and included angle θ: Area = ½ × side1 × side2 × sin(included angle).

### Example 6: Segment Area

**Problem:** A circle has radius 10 cm. Find the area of the segment cut off by a central angle of π/3 radians.

**Approach:** Compute the sector area, compute the triangle area, then subtract.

Sector area = ½ × 10² × (π/3) = ½ × 100 × (π/3) = 50π/3.

Triangle area = ½ × 10² × sin(π/3) = ½ × 100 × (√3/2) = 50 × (√3/2) = 25√3.

Segment area = 50π/3 − 25√3.

**Answer:** (50π/3 − 25√3) cm². This is the exact form. If you need a decimal, it is approximately 52.36 − 43.30 = 9.06 cm².

**Why this makes sense:** When θ is small, the chord is almost as long as the arc, so the segment area is tiny. When θ = π (a semicircle), the triangle has zero area (the "chord" is the diameter and the radii point in opposite directions, giving sin π = 0), so the segment equals the sector — a half‑circle.

---

## 4. Practical Problem: Relating Perimeter and Area

Sometimes the IB combines arc length and sector area in one problem. You might be given the perimeter of a sector and asked for its area.

The **perimeter of a sector** is the sum of the two radii plus the arc: P = 2r + s = 2r + rθ.

### Example 7

**Problem:** A sector of radius 9 cm has a perimeter of 30 cm. Find the area of the sector.

**Approach:** Use the perimeter to find the arc length and then the angle. Then compute the area.

P = 2r + s → 30 = 2(9) + s → 30 = 18 + s → s = 12 cm.

Then θ = s/r = 12/9 = 4/3 radians.

Finally, A = ½ r²θ = ½ × 81 × (4/3) = (81 × 4)/(2 × 3) = 324/6 = 54 cm².

**Answer:** 54 cm².

**Why this makes sense:** The perimeter information gave us the arc length, which gave us the angle, which unlocked the area. This chain of reasoning — perimeter → arc → angle → area — is common in IB problems.

---

## Practice Problems

**Problem 1:** Convert each angle to radians: (a) 120°, (b) 225°, (c) −90°.

**Problem 2:** Convert each angle to degrees: (a) 2π/3, (b) 7π/6, (c) −π/2.

**Problem 3:** A circle has radius 12 cm. Find the length of the arc cut off by a central angle of 2π/3 radians.

**Problem 4:** A circle has radius 10 cm. Find the area of the sector with central angle 3π/5 radians.

**Problem 5 (IB Exam Style — 5 marks):** A sector of a circle has radius r cm and angle θ radians. The perimeter of the sector is 20 cm.
(a) Show that the area A of the sector is given by A = 10r − r². [3 marks]
(b) Find the value of r that maximises A, and state the corresponding value of θ. [2 marks]

**Problem 6:** A chord AB of a circle with radius 6 cm subtends a central angle of π/2 radians. Find the area of the segment between the chord and the arc.

---

## Answers

**Answer 1:** (a) 120 × π/180 = 2π/3. (b) 225 × π/180 = 5π/4. (c) −90 × π/180 = −π/2. The negative sign simply means the angle is measured clockwise instead of counterclockwise.

**Answer 2:** (a) (2π/3) × (180/π) = 120°. (b) (7π/6) × (180/π) = 210°. (c) (−π/2) × (180/π) = −90°.

**Answer 3:** s = rθ = 12 × (2π/3) = 8π cm. The π stays in the answer because 2π/3 is not a "nice" decimal — exact form is expected unless the question asks for an approximation.

**Answer 4:** A = ½ r²θ = ½ × 100 × (3π/5) = 50 × (3π/5) = 150π/5 = 30π cm². Notice that the ½ canceled with part of the 100 before multiplication — this makes the arithmetic cleaner.

**Answer 5:**
(a) Perimeter P = 2r + rθ = 20 → rθ = 20 − 2r → θ = (20 − 2r)/r = 20/r − 2.

Area A = ½ r²θ = ½ r²(20/r − 2) = ½ r(20 − 2r) = 10r − r². ✓

(b) A = 10r − r² is a quadratic opening downward. Maximum at r = −b/(2a) = −10/(2(−1)) = 5.

When r = 5, θ = 20/5 − 2 = 4 − 2 = 2 radians.

**Interpretation:** The sector with the largest area for a fixed perimeter of 20 cm has radius 5 cm and angle 2 radians, giving area A = 10(5) − 5² = 25 cm².

**Answer 6:** Sector area = ½ × 6² × (π/2) = ½ × 36 × (π/2) = 18 × (π/2) = 9π. Triangle area = ½ r² sin θ = ½ × 36 × sin(π/2) = 18 × 1 = 18. Segment area = 9π − 18 cm².

**Pitfall warning:** When θ = π/2, the triangle is a right‑angled triangle with both legs equal to the radius. Some students mistakenly use ½ × base × height with the wrong dimensions. The formula ½ r² sin θ handles all cases automatically.
