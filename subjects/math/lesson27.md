# Lesson 27 — Planes and Intersections

## What Is a Plane?

### The "What"

A plane is a flat, two-dimensional surface that extends infinitely in all directions. In three-dimensional space, a plane is the analog of a line in two dimensions. While a line in 2D can be described by one linear equation ($ax + by = c$), a plane in 3D is described by one linear equation ($ax + by + cz = d$).

A plane is uniquely determined by:

- A **point** on the plane (any one point).
- A **normal vector** — a vector that is perpendicular to the plane.

The normal vector "points straight out" of the plane. Every vector that lies within the plane is perpendicular to the normal vector.

### The "Why"

Planes are fundamental in 3D geometry. The intersection of two planes is a line. The intersection of three planes may be a point. Distances from points to planes appear in optimization problems. Understanding plane equations and intersections is essential for IB AAHL vector problems.

---

## 1. Equation of a Plane

### Vector Form

Let $\vec{a}$ be the position vector of a known point $A$ on the plane. Let $\vec{n}$ be a normal vector (perpendicular to the plane). For any point $\vec{r}$ on the plane, the vector $\vec{r} - \vec{a}$ lies within the plane. Since every vector in the plane is perpendicular to $\vec{n}$, their dot product is zero:

$$\boxed{\vec{n} \cdot (\vec{r} - \vec{a}) = 0}$$

This is the **vector form** of the plane equation.

### Scalar (Cartesian) Form

If $\vec{n} = \begin{pmatrix}n_1\\n_2\\n_3\end{pmatrix}$ and $\vec{r} = \begin{pmatrix}x\\y\\z\end{pmatrix}$, expanding the vector form gives:

$$n_1(x - a_1) + n_2(y - a_2) + n_3(z - a_3) = 0$$

Rearranging:

$$\boxed{n_1 x + n_2 y + n_3 z = d}$$

where $d = \vec{n}\cdot\vec{a} = n_1 a_1 + n_2 a_2 + n_3 a_3$. The coefficients $n_1, n_2, n_3$ are exactly the components of the normal vector. This is the **scalar (Cartesian) form**.

---

## Worked Example 1: Plane from Normal and Point

**Problem:** Find the equation of the plane that passes through $A(2, -1, 3)$ and has normal vector $\vec{n} = \begin{pmatrix}1\\4\\-2\end{pmatrix}$. Give the answer in scalar form.

**Approach:** Substitute into $\vec{n}\cdot(\vec{r} - \vec{a}) = 0$, expand, and simplify.

**Step 1 — Write the vector form:**
$$1(x - 2) + 4(y - (-1)) + (-2)(z - 3) = 0$$

**Step 2 — Expand:**
$$(x - 2) + 4(y + 1) - 2(z - 3) = 0$$
$$x - 2 + 4y + 4 - 2z + 6 = 0$$

**Step 3 — Collect terms:**
$$x + 4y - 2z + 8 = 0$$

**Answer:** $x + 4y - 2z = -8$, or equivalently $x + 4y - 2z + 8 = 0$.

---

## 2. Finding a Plane Through Three Points

If you know three points $A, B, C$ on the plane (and they are not collinear — not all on the same line), you can find the plane's equation by:

1. Forming two vectors in the plane: $\overrightarrow{AB} = \vec{b} - \vec{a}$ and $\overrightarrow{AC} = \vec{c} - \vec{a}$.
2. Computing a normal vector by taking the cross product: $\vec{n} = \overrightarrow{AB} \times \overrightarrow{AC}$. (The cross product of two vectors in the plane gives a vector perpendicular to both, which is perpendicular to the plane.)
3. Using point $A$ and $\vec{n}$ in the vector form $\vec{n}\cdot(\vec{r} - \vec{a}) = 0$.

---

## Worked Example 2: Plane Through Three Points

**Problem:** Find the scalar equation of the plane containing the points $A(1, 0, 2)$, $B(3, -1, 4)$, and $C(2, 5, -1)$.

**Approach:** Compute $\overrightarrow{AB}$ and $\overrightarrow{AC}$, take their cross product for $\vec{n}$, then use the point-normal form.

**Step 1 — Compute vectors in the plane:**
$$\overrightarrow{AB} = \begin{pmatrix}3-1\\-1-0\\4-2\end{pmatrix} = \begin{pmatrix}2\\-1\\2\end{pmatrix}$$
$$\overrightarrow{AC} = \begin{pmatrix}2-1\\5-0\\-1-2\end{pmatrix} = \begin{pmatrix}1\\5\\-3\end{pmatrix}$$

**Step 2 — Compute the normal vector using the cross product:**
$$\vec{n} = \overrightarrow{AB} \times \overrightarrow{AC} = \begin{pmatrix}(-1)(-3) - (2)(5)\\(2)(1) - (2)(-3)\\(2)(5) - (-1)(1)\end{pmatrix} = \begin{pmatrix}3 - 10\\2 + 6\\10 + 1\end{pmatrix} = \begin{pmatrix}-7\\8\\11\end{pmatrix}$$

**Step 3 — Use point $A(1, 0, 2)$:**
$$-7(x - 1) + 8(y - 0) + 11(z - 2) = 0$$
$$-7x + 7 + 8y + 11z - 22 = 0$$
$$-7x + 8y + 11z - 15 = 0$$

**Answer:** $-7x + 8y + 11z = 15$, or equivalently $7x - 8y - 11z = -15$.

---

## 3. Intersection of a Line and a Plane

To find where a line meets a plane, substitute the parametric equations of the line into the scalar equation of the plane and solve for the parameter.

### The Three Possibilities

- **One intersection point:** The line pierces the plane at a single point. This happens when the line is not parallel to the plane.
- **No intersection:** The line is parallel to the plane and never meets it. You get a contradiction like $5 = 7$ when solving for $\lambda$.
- **Infinite intersections:** The line lies entirely in the plane. You get an identity like $0 = 0$ for all $\lambda$.

---

## Worked Example 3: Line-Plane Intersection

**Problem:** Find the intersection of the line $\vec{r} = \begin{pmatrix}3\\0\\4\end{pmatrix} + t\begin{pmatrix}1\\2\\-1\end{pmatrix}$ with the plane $x + 3y - 2z = 1$.

**Approach:** Write the parametric equations, substitute into the plane equation, and solve for $t$.

**Step 1 — Parametric equations:**
$$x = 3 + t,\quad y = 2t,\quad z = 4 - t$$

**Step 2 — Substitute into the plane equation:**
$$(3 + t) + 3(2t) - 2(4 - t) = 1$$
$$3 + t + 6t - 8 + 2t = 1$$
$$(3 - 8) + (t + 6t + 2t) = 1$$
$$-5 + 9t = 1$$
$$9t = 6$$
$$t = \frac{2}{3}$$

**Step 3 — Find the intersection point:**
$x = 3 + \frac{2}{3} = \frac{11}{3}$, $y = 2 \cdot \frac{2}{3} = \frac{4}{3}$, $z = 4 - \frac{2}{3} = \frac{10}{3}$.

**Answer:** $\left(\dfrac{11}{3}, \dfrac{4}{3}, \dfrac{10}{3}\right)$

---

## Worked Example 4: Line Parallel to a Plane

**Problem:** Find the intersection of $\vec{r} = \begin{pmatrix}1\\2\\-1\end{pmatrix} + \lambda\begin{pmatrix}2\\-1\\3\end{pmatrix}$ with the plane $2x + y - z = 7$.

**Approach:** Substitute and see what happens.

**Step 1 — Parametric equations:**
$$x = 1 + 2\lambda,\quad y = 2 - \lambda,\quad z = -1 + 3\lambda$$

**Step 2 — Substitute:**
$$2(1 + 2\lambda) + (2 - \lambda) - (-1 + 3\lambda) = 7$$
$$2 + 4\lambda + 2 - \lambda + 1 - 3\lambda = 7$$
$$(2 + 2 + 1) + (4\lambda - \lambda - 3\lambda) = 7$$
$$5 + 0\lambda = 7$$
$$5 = 7$$

This is a contradiction — no value of $\lambda$ can make $5 = 7$.

**Answer:** The line does not intersect the plane. It is parallel to the plane (the direction vector is perpendicular to the normal vector) and lies at a distance from it.

---

## 4. Intersection of Two Planes

Two non-parallel planes intersect in a **line**. To find this line, you need:

1. A **direction vector** for the line: $\vec{d} = \vec{n}_1 \times \vec{n}_2$. (This vector is perpendicular to both normals, so it lies in both planes.)
2. A **point** on both planes: set one variable to $0$ (or another convenient value) and solve the two plane equations for the other two variables.

---

## Worked Example 5: Intersection of Two Planes

**Problem:** Find the line of intersection of the planes $\Pi_1: x + 2y - z = 4$ and $\Pi_2: 2x - y + 3z = 1$.

**Approach:** Compute $\vec{d} = \vec{n}_1 \times \vec{n}_2$. Then find a common point by setting $z = 0$.

**Step 1 — Identify normal vectors:**
$\vec{n}_1 = \begin{pmatrix}1\\2\\-1\end{pmatrix}$, $\vec{n}_2 = \begin{pmatrix}2\\-1\\3\end{pmatrix}$.

**Step 2 — Compute the direction vector:**
$$\vec{d} = \vec{n}_1 \times \vec{n}_2 = \begin{pmatrix}2(3) - (-1)(-1)\\(-1)(2) - 1(3)\\1(-1) - 2(2)\end{pmatrix} = \begin{pmatrix}6 - 1\\-2 - 3\\-1 - 4\end{pmatrix} = \begin{pmatrix}5\\-5\\-5\end{pmatrix}$$

This simplifies to $\begin{pmatrix}1\\-1\\-1\end{pmatrix}$ (dividing by $5$).

**Step 3 — Find a common point (set $z = 0$):**
From $\Pi_1$: $x + 2y = 4$.
From $\Pi_2$: $2x - y = 1$.

From the second equation: $y = 2x - 1$. Substitute into the first:
$x + 2(2x - 1) = 4$, so $x + 4x - 2 = 4$, $5x = 6$, $x = \frac{6}{5}$.

Then $y = 2(\frac{6}{5}) - 1 = \frac{12}{5} - 1 = \frac{7}{5}$.

Point: $\left(\frac{6}{5}, \frac{7}{5}, 0\right)$.

**Step 4 — Write the line:**
$$\vec{r} = \begin{pmatrix}6/5\\7/5\\0\end{pmatrix} + \lambda\begin{pmatrix}1\\-1\\-1\end{pmatrix}$$

---

## 5. Distance from a Point to a Plane

The perpendicular distance from a point $P(x_1, y_1, z_1)$ to the plane $ax + by + cz = d$ is:

$$\boxed{\text{distance} = \frac{|ax_1 + by_1 + cz_1 - d|}{\sqrt{a^2 + b^2 + c^2}}}$$

The numerator is the absolute value of the result when you plug the point's coordinates into the plane equation (with $d$ on the right side). The denominator is the magnitude of the normal vector. This formula is the 3D analog of the 2D point-to-line distance formula.

---

## Worked Example 6: Distance from Point to Plane

**Problem:** Find the distance from the point $P(3, -1, 2)$ to the plane $2x - 2y + z = 5$.

**Approach:** Identify $a, b, c, d$, substitute the point's coordinates, and apply the formula.

**Step 1 — Identify coefficients:**
$a = 2$, $b = -2$, $c = 1$, $d = 5$.

**Step 2 — Compute the numerator:**
$|2(3) + (-2)(-1) + 1(2) - 5| = |6 + 2 + 2 - 5| = |5| = 5$.

**Step 3 — Compute the denominator:**
$\sqrt{2^2 + (-2)^2 + 1^2} = \sqrt{4 + 4 + 1} = \sqrt{9} = 3$.

**Step 4 — Distance:**
$\text{distance} = \frac{5}{3}$.

**Answer:** The distance is $\frac{5}{3}$ units.

---

## Summary Table

| Concept | Formula / Method |
|---------|------------------|
| Plane from normal and point | $\vec{n}\cdot(\vec{r} - \vec{a}) = 0$ |
| Scalar form | $n_1x + n_2y + n_3z = d$ |
| Plane through 3 points | $\vec{n} = \overrightarrow{AB} \times \overrightarrow{AC}$ |
| Line-plane intersection | Substitute parametric line into plane, solve for $\lambda$ |
| Two-plane intersection | $\vec{d} = \vec{n}_1 \times \vec{n}_2$, find common point |
| Point-to-plane distance | $\dfrac{|ax_1 + by_1 + cz_1 - d|}{\sqrt{a^2 + b^2 + c^2}}$ |

---

## Practice Problems

**Problem 1:** Find the scalar equation of the plane through $A(1, 3, -2)$ with normal vector $\vec{n} = \begin{pmatrix}2\\-1\\5\end{pmatrix}$.

**Problem 2:** Find the equation of the plane containing the three points $P(1, 2, 0)$, $Q(3, -1, 4)$, and $R(0, 5, 2)$. Give the answer in scalar form.

**Problem 3:** Find the intersection point of the line $\vec{r} = \begin{pmatrix}4\\-1\\2\end{pmatrix} + t\begin{pmatrix}3\\1\\-2\end{pmatrix}$ with the plane $x - 2y + z = 10$.

**Problem 4:** Find the line of intersection of the planes $\Pi_1: 2x + y - z = 3$ and $\Pi_2: x - 3y + 2z = 5$.

**Problem 5 (IB-style):** A point $P$ has coordinates $(2, -3, 1)$ and a plane $\Pi$ has equation $3x + 4y - 5z = 6$.
(a) Find the perpendicular distance from $P$ to $\Pi$. [2 marks]
(b) Hence, find the exact distance, leaving your answer in the form $\frac{p\sqrt{q}}{r}$ where $p$, $q$, and $r$ are integers. [1 mark]

**Problem 6:** Show that the line $\vec{r} = \begin{pmatrix}2\\1\\-3\end{pmatrix} + \lambda\begin{pmatrix}1\\-2\\1\end{pmatrix}$ lies entirely in the plane $x + 2y + 3z = -5$.

---

## Answers

**Answer 1:**

$2(x - 1) - 1(y - 3) + 5(z + 2) = 0$

$2x - 2 - y + 3 + 5z + 10 = 0$

$2x - y + 5z + 11 = 0$.

---

**Answer 2:**

$\overrightarrow{PQ} = \begin{pmatrix}2\\-3\\4\end{pmatrix}$, $\overrightarrow{PR} = \begin{pmatrix}-1\\3\\2\end{pmatrix}$.

$\vec{n} = \overrightarrow{PQ} \times \overrightarrow{PR} = \begin{pmatrix}(-3)(2) - (4)(3)\\(4)(-1) - (2)(2)\\(2)(3) - (-3)(-1)\end{pmatrix} = \begin{pmatrix}-6-12\\-4-4\\6-3\end{pmatrix} = \begin{pmatrix}-18\\-8\\3\end{pmatrix}$.

Using point $P(1, 2, 0)$: $-18(x-1) - 8(y-2) + 3(z-0) = 0$.

$-18x + 18 - 8y + 16 + 3z = 0$, so $-18x - 8y + 3z + 34 = 0$, or $18x + 8y - 3z = 34$.

---

**Answer 3:**

Parametric: $x = 4 + 3t$, $y = -1 + t$, $z = 2 - 2t$.

Substitute: $(4 + 3t) - 2(-1 + t) + (2 - 2t) = 10$.

$4 + 3t + 2 - 2t + 2 - 2t = 10$, so $8 - t = 10$, $t = -2$.

Point: $x = 4 + 3(-2) = -2$, $y = -1 + (-2) = -3$, $z = 2 - 2(-2) = 6$.

Intersection: $(-2, -3, 6)$.

---

**Answer 4:**

$\vec{n}_1 = \begin{pmatrix}2\\1\\-1\end{pmatrix}$, $\vec{n}_2 = \begin{pmatrix}1\\-3\\2\end{pmatrix}$.

$\vec{d} = \vec{n}_1 \times \vec{n}_2 = \begin{pmatrix}1(2) - (-1)(-3)\\(-1)(1) - 2(2)\\2(-3) - 1(1)\end{pmatrix} = \begin{pmatrix}2-3\\-1-4\\-6-1\end{pmatrix} = \begin{pmatrix}-1\\-5\\-7\end{pmatrix}$.

Find point (set $z = 0$): $2x + y = 3$, $x - 3y = 5$.

From the second: $x = 5 + 3y$. Substitute: $2(5 + 3y) + y = 3$, $10 + 6y + y = 3$, $7y = -7$, $y = -1$, $x = 2$.

Line: $\vec{r} = \begin{pmatrix}2\\-1\\0\end{pmatrix} + \lambda\begin{pmatrix}-1\\-5\\-7\end{pmatrix}$ (or multiply direction by $-1$: $\begin{pmatrix}1\\5\\7\end{pmatrix}$).

---

**Answer 5:**

**(a)** $\text{distance} = \dfrac{|3(2) + 4(-3) - 5(1) - 6|}{\sqrt{9 + 16 + 25}} = \dfrac{|6 - 12 - 5 - 6|}{\sqrt{50}} = \dfrac{|-17|}{5\sqrt{2}} = \dfrac{17}{5\sqrt{2}}$.

**(b)** Rationalizing: $\dfrac{17}{5\sqrt{2}} = \dfrac{17\sqrt{2}}{10}$. Here $p = 17$, $q = 2$, $r = 10$.

---

**Answer 6:**

Parametric: $x = 2 + \lambda$, $y = 1 - 2\lambda$, $z = -3 + \lambda$.

Substitute into the plane: $(2 + \lambda) + 2(1 - 2\lambda) + 3(-3 + \lambda)$.

$= 2 + \lambda + 2 - 4\lambda - 9 + 3\lambda = (2 + 2 - 9) + (\lambda - 4\lambda + 3\lambda) = -5 + 0 = -5$.

Since the result is exactly $-5$ for every value of $\lambda$, every point on the line satisfies the plane equation. The line lies entirely in the plane.
