# Lesson 21: The Argand Diagram and Geometric Interpretation

## WHAT Is the Argand Diagram?

The **Argand diagram** is a flat plane where you can draw complex numbers as points or arrows. It looks exactly like the ordinary \((x, y)\) coordinate plane you have used in algebra, but the axes have different meanings:

- The **horizontal axis** (what used to be the \(x\)-axis) represents the **real part** of a complex number.
- The **vertical axis** (what used to be the \(y\)-axis) represents the **imaginary part** of a complex number.

So a complex number \(z = a + bi\) gets plotted at the point with coordinates \((a, b)\). You can also think of it as an arrow (a vector) starting at the origin \((0, 0)\) and ending at \((a, b)\).

## WHY Use the Argand Diagram?

Drawing complex numbers on a plane turns abstract algebra into something you can see. Addition looks like vector addition. The modulus becomes a length you can measure with a ruler. The argument becomes an angle you can measure with a protractor. Locus problems — which ask "where are all the points that satisfy a certain condition?" — become questions about circles, lines, and rays that you can sketch and reason about geometrically. This visual approach is heavily tested in IB exams.

---

## 1. Plotting Complex Numbers

To plot \(z = a + bi\), go \(a\) units along the horizontal (real) axis and \(b\) units along the vertical (imaginary) axis.

**Examples:**
- \(z = 2 + 3i\) is at the point \((2, 3)\).
- \(z = -3 + i\) is at \((-3, 1)\).
- \(z = 3 - 2i\) is at \((3, -2)\).
- \(z = -1 - i\) is at \((-1, -1)\).

A real number like \(z = 4\) lies on the horizontal axis. A purely imaginary number like \(z = 5i\) lies on the vertical axis.

---

## 2. Addition as Vector Addition

When you add two complex numbers, you add their real parts and their imaginary parts separately. On the Argand diagram, this is exactly the same as adding two vectors using the **parallelogram rule** or the **tip-to-tail method**.

**Worked Example:** Let \(z_1 = 2 + i\) and \(z_2 = 1 + 3i\). Their sum is \(z_1 + z_2 = (2 + 1) + (1 + 3)i = 3 + 4i\).

Geometrically, you can draw an arrow for \(z_1\) from the origin to \((2, 1)\), then draw an arrow for \(z_2\) starting at the tip of \(z_1\). The arrow from the origin to the final tip lands at \((3, 4)\), which is exactly \(z_1 + z_2\).

---

## 3. The Modulus as Distance

In Lesson 20, you learned that \(|z| = \sqrt{a^2 + b^2}\). On the Argand diagram, this formula should look familiar — it is the distance from the origin \((0, 0)\) to the point \((a, b)\), found using the Pythagorean theorem.

More generally, the distance between any two complex numbers \(z = a + bi\) and \(w = c + di\) is given by:

\[
\boxed{|z - w| = \sqrt{(a - c)^2 + (b - d)^2}}
\]

This is just the Pythagorean distance between the two points \((a, b)\) and \((c, d)\).

**Worked Example:** Find the distance between \(z = 3 + 4i\) and \(w = -1 + i\).

**Approach:** Subtract \(w\) from \(z\), then find the modulus of the result.

**Step 1:** \(z - w = (3 + 4i) - (-1 + i) = (3 + 1) + (4 - 1)i = 4 + 3i\).

**Step 2:** \(|z - w| = \sqrt{4^2 + 3^2} = \sqrt{16 + 9} = \sqrt{25} = 5\).

**Answer:** The distance is 5 units.

---

## 4. The Argument

The **argument** of a complex number \(z = a + bi\) is the angle that the arrow from the origin to \((a, b)\) makes with the positive real axis. The argument is measured counterclockwise and is written as \(\arg(z)\).

\[
\boxed{\tan(\arg(z)) = \frac{b}{a}}
\]

To find the argument, you compute \(\arctan(b/a)\), but you must then adjust for the quadrant. The calculator's arctan function only returns angles between \(-\frac{\pi}{2}\) and \(\frac{\pi}{2}\) (that is, between \(-90^\circ\) and \(90^\circ\)), which only covers quadrants I and IV correctly. Here is how to handle each case:

- **Quadrant I:** \(a > 0\) and \(b > 0\). The angle is simply \(\arctan(b/a)\). This is already correct.
- **Quadrant II:** \(a < 0\) and \(b > 0\). The calculator gives a negative angle, but the actual angle is in the second quadrant. Add \(\pi\) (or \(180^\circ\)) to the calculator's result.
- **Quadrant III:** \(a < 0\) and \(b < 0\). The calculator gives a positive angle (because negative divided by negative is positive), but the actual angle is in the third quadrant. Add \(\pi\) (or \(180^\circ\)), or equivalently subtract \(\pi\) if you prefer a negative angle.
- **Quadrant IV:** \(a > 0\) and \(b < 0\). The calculator gives a negative angle, which is already correct for the fourth quadrant.

The IB convention is to give the **principal argument** in the range \((-\pi, \pi]\), which means between \(-180^\circ\) and \(180^\circ\) (not including \(-180^\circ\), including \(180^\circ\)).

**Common misconception:** Many students take \(\arctan(b/a)\) and stop, forgetting to check which quadrant the point is in. This gives the wrong answer whenever \(a\) is negative.

### Worked Examples for Argument

**Example 1:** \(z = 1 + i\). Here \(a = 1 > 0\) and \(b = 1 > 0\) (Quadrant I). \(\arg(z) = \arctan(1/1) = \arctan(1) = \frac{\pi}{4}\) (which is \(45^\circ\)).

**Example 2:** \(z = -1 + i\). Here \(a = -1 < 0\) and \(b = 1 > 0\) (Quadrant II). The calculator gives \(\arctan(1/(-1)) = \arctan(-1) = -\frac{\pi}{4}\). But the point is in quadrant II, so we add \(\pi\): \(\arg(z) = -\frac{\pi}{4} + \pi = \frac{3\pi}{4}\) (which is \(135^\circ\)).

**Example 3:** \(z = -1 - i\). Here \(a = -1 < 0\) and \(b = -1 < 0\) (Quadrant III). The calculator gives \(\arctan((-1)/(-1)) = \arctan(1) = \frac{\pi}{4}\). But the point is in quadrant III, so the principal argument is \(-\pi + \frac{\pi}{4} = -\frac{3\pi}{4}\) (which is \(-135^\circ\)).

**Example 4:** \(z = 1 - i\). Here \(a = 1 > 0\) and \(b = -1 < 0\) (Quadrant IV). \(\arg(z) = \arctan(-1/1) = -\frac{\pi}{4}\) (which is \(-45^\circ\)).

---

## 5. Locus Problems on the Argand Diagram

A **locus** (plural: loci) is the set of all points that satisfy a given condition. Drawing loci on the Argand diagram is a major IB topic because it connects algebra and geometry.

### Locus 1: A Circle Centered at the Origin

The condition \(|z| = r\) means "the distance from \(z\) to the origin is \(r\)." All points at a fixed distance from a center form a circle. So \(|z| = r\) is a circle with radius \(r\), centered at \((0, 0)\).

\[
\boxed{|z| = r}
\]

**Example:** \(|z| = 3\) is a circle of radius 3 centered at the origin.

### Locus 2: A Circle Centered at Any Point

The condition \(|z - a| = r\) means "the distance from \(z\) to the fixed complex number \(a\) is \(r\)." This is a circle with radius \(r\) centered at the point representing \(a\).

\[
\boxed{|z - a| = r}
\]

**Example:** \(|z - (2 + i)| = 3\) is a circle of radius 3 centered at \((2, 1)\).

### Locus 3: The Perpendicular Bisector

The condition \(|z - a| = |z - b|\) means "the distance from \(z\) to \(a\) equals the distance from \(z\) to \(b\)." The set of all points equidistant from two fixed points is the **perpendicular bisector** of the line segment connecting them.

\[
\boxed{|z - a| = |z - b|}
\]

### Worked Locus Example: Perpendicular Bisector

**Problem:** Describe the locus given by \(|z - i| = |z - 3|\).

**Approach:** Let \(z = x + yi\). Write both sides as distances and set them equal.

**Step 1 — Express each side in terms of \(x\) and \(y\):**
\(z - i = x + yi - i = x + (y - 1)i\). So \(|z - i| = \sqrt{x^2 + (y - 1)^2}\).
\(z - 3 = (x - 3) + yi\). So \(|z - 3| = \sqrt{(x - 3)^2 + y^2}\).

**Step 2 — Set them equal and square both sides (removing square roots):**
\[
x^2 + (y - 1)^2 = (x - 3)^2 + y^2
\]

**Step 3 — Expand:**
\[
x^2 + y^2 - 2y + 1 = x^2 - 6x + 9 + y^2
\]

**Step 4 — Cancel \(x^2\) and \(y^2\) from both sides:**
\[
-2y + 1 = -6x + 9
\]

**Step 5 — Rearrange:**
\[
6x - 2y = 8 \quad\Longrightarrow\quad 3x - y = 4 \quad\Longrightarrow\quad y = 3x - 4
\]

**Answer:** The locus is the straight line \(y = 3x - 4\). This is the perpendicular bisector of the segment joining the points \(i = (0, 1)\) and \(3 = (3, 0)\).

### Locus 4: A Ray (Half-Line)

The condition \(\arg(z - a) = \theta\) means "the arrow from \(a\) to \(z\) makes an angle \(\theta\) with the positive real axis." This describes a **ray** (a half-line) that starts at \(a\) and extends outward at angle \(\theta\). The point \(a\) itself is not included (the ray is open at its starting point).

\[
\boxed{\arg(z - a) = \theta}
\]

**Example:** \(\arg(z - 1) = \frac{\pi}{3}\) is a ray starting at \((1, 0)\) pointing at an angle of \(60^\circ\).

---

## 6. Worked Example: Full Locus Problem

**Problem:** Describe geometrically the locus of points \(z\) satisfying \(|z - 3| = |z + i|\).

**Approach:** Let \(z = x + yi\) and convert to a Cartesian equation.

**Step 1 — Write each side:**
\(|z - 3| = |(x - 3) + yi| = \sqrt{(x - 3)^2 + y^2}\).
\(|z + i| = |x + (y + 1)i| = \sqrt{x^2 + (y + 1)^2}\).

**Step 2 — Equate and square:**
\[
(x - 3)^2 + y^2 = x^2 + (y + 1)^2
\]

**Step 3 — Expand:**
\(x^2 - 6x + 9 + y^2 = x^2 + y^2 + 2y + 1\).

**Step 4 — Cancel \(x^2\) and \(y^2\):**
\(-6x + 9 = 2y + 1\).

**Step 5 — Solve for \(y\):**
\(2y = -6x + 8\), so \(y = -3x + 4\).

**Answer:** The locus is the straight line \(y = -3x + 4\). This is the perpendicular bisector of the segment joining \(3 = (3, 0)\) and \(-i = (0, -1)\).

---

## Practice Problems

**Problem 1:** Plot the complex numbers \(z_1 = 2 + 3i\) and \(z_2 = -3 + i\) on an Argand diagram. Then find \(|z_1 - z_2|\) and explain what this value represents.

**Problem 2:** Find the modulus and the principal argument of \(z = -\sqrt{3} + i\). Give the argument in radians.

**Problem 3:** Describe geometrically the locus given by \(|z + 2 - i| = 4\). State the center and radius.

**Problem 4:** Find the Cartesian equation of the locus \(|z - 1| = |z - i|\). What shape is the locus?

**Problem 5 (IB Exam Style):** The point \(z\) lies on the circle \(|z - 3| = 2\).
(a) Sketch the circle on an Argand diagram. [1 mark]
(b) By considering the geometry of the Argand diagram, find the maximum possible value of \(|z|\). [3 marks]
(c) Find the minimum possible value of \(|z|\). [2 marks]

**Problem 6:** On the same Argand diagram, sketch the region defined by both of these conditions: \(|z - 2| \leq 3\) and \(0 \leq \arg(z) \leq \frac{\pi}{4}\). Describe the region in words.

---

## Answers

**Answer 1:** On the Argand diagram, \(z_1 = 2 + 3i\) is at \((2, 3)\) and \(z_2 = -3 + i\) is at \((-3, 1)\).

Now compute \(z_1 - z_2 = (2 + 3i) - (-3 + i) = 5 + 2i\).

The modulus is \(|z_1 - z_2| = \sqrt{5^2 + 2^2} = \sqrt{25 + 4} = \sqrt{29}\).

This value, \(\sqrt{29}\) (approximately 5.39), is the straight-line distance between the two points \((2, 3)\) and \((-3, 1)\) on the Argand diagram.

**Answer 2:** The modulus is \(|z| = \sqrt{(-\sqrt{3})^2 + 1^2} = \sqrt{3 + 1} = \sqrt{4} = 2\).

For the argument: \(\tan\theta = \frac{1}{-\sqrt{3}} = -\frac{1}{\sqrt{3}}\). The basic reference angle (ignoring the negative sign) is \(\arctan(1/\sqrt{3}) = \frac{\pi}{6}\) (which is \(30^\circ\)).

Now check the quadrant: \(a = -\sqrt{3} < 0\) and \(b = 1 > 0\). This is Quadrant II. We must add \(\pi\) to the calculator's result. The calculator would give \(\arctan(-1/\sqrt{3}) = -\frac{\pi}{6}\), so \(\arg(z) = -\frac{\pi}{6} + \pi = \frac{5\pi}{6}\) (which is \(150^\circ\)).

**Pitfall:** If you simply compute \(\arctan(1/(-\sqrt{3}))\) without adjusting for the quadrant, you get \(-\frac{\pi}{6}\), which is wrong. Always draw a quick sketch of the quadrant.

**Answer 3:** Rewrite: \(|z + 2 - i| = |z - (-2 + i)| = 4\). This is in the form \(|z - a| = r\) with center \(a = -2 + i\) and radius \(r = 4\).

Geometrically, this describes a circle centered at the point \((-2, 1)\) on the Argand diagram with a radius of 4 units.

**Answer 4:** Let \(z = x + yi\). Then \(|z - 1| = |(x - 1) + yi| = \sqrt{(x - 1)^2 + y^2}\) and \(|z - i| = |x + (y - 1)i| = \sqrt{x^2 + (y - 1)^2}\).

Set them equal and square: \((x - 1)^2 + y^2 = x^2 + (y - 1)^2\).

Expand: \(x^2 - 2x + 1 + y^2 = x^2 + y^2 - 2y + 1\).

Cancel \(x^2\), \(y^2\), and \(1\) from both sides: \(-2x = -2y\), so \(y = x\).

The locus is the line \(y = x\). This is the perpendicular bisector of the line segment connecting the points \((1, 0)\) (representing \(1\)) and \((0, 1)\) (representing \(i\)). It bisects the segment at \((0.5, 0.5)\) at a \(45^\circ\) angle.

**Answer 5:**

(a) The circle \(|z - 3| = 2\) has center at \((3, 0)\) and radius 2.

(b) The quantity \(|z|\) is the distance from the origin \((0, 0)\) to the point \(z\). Since \(z\) must lie on the circle, we want the farthest point on the circle from the origin.

The center of the circle is at \((3, 0)\), which is 3 units from the origin. The circle extends 2 units in every direction from its center. The point on the circle farthest from the origin lies on the line connecting the origin to the center, on the far side of the circle. Its distance is the distance to the center plus the radius: \(3 + 2 = 5\).

So the maximum value of \(|z|\) is 5.

(c) The point on the circle closest to the origin lies on the same line, but on the near side of the circle. Its distance is the distance to the center minus the radius: \(3 - 2 = 1\).

So the minimum value of \(|z|\) is 1.

**Why this makes sense:** The origin is at \((0, 0)\) and the circle is centered at \((3, 0)\) with radius 2. The circle touches the point \((1, 0)\) at its closest approach and extends to \((5, 0)\) at its farthest reach.

**Answer 6:** The condition \(|z - 2| \leq 3\) describes all points inside or on the circle centered at \((2, 0)\) with radius 3. This is a filled disk.

The condition \(0 \leq \arg(z) \leq \frac{\pi}{4}\) describes all points whose position vectors make an angle between \(0^\circ\) and \(45^\circ\) with the positive real axis. This is an infinite wedge (a sector) in the first quadrant.

The region satisfying both conditions is the intersection: the part of the wedge (from angle \(0\) to \(\frac{\pi}{4}\)) that also lies inside the disk centered at \((2, 0)\) of radius 3.
