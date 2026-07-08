# Lesson 25 — Vectors: Dot Product, Cross Product, and Angles

## What Are Vectors?

### The "What"

A **vector** is a mathematical object that has both **magnitude** (size, length) and **direction**. This is different from a scalar, which is just a number with no direction. For example, "the wind is blowing at 15 kilometers per hour" is a scalar (speed only). "The wind is blowing at 15 kilometers per hour toward the northeast" is a vector (speed and direction).

In three-dimensional space, a vector is written as an ordered triple of numbers. Each number is called a **component** of the vector. There are two common notations:

**Column (component) form:**
$$\vec{v} = \begin{pmatrix} x \\ y \\ z \end{pmatrix}$$

**Standard basis form ($\mathbf{i}, \mathbf{j}, \mathbf{k}$):**
$$\vec{v} = x\,\mathbf{i} + y\,\mathbf{j} + z\,\mathbf{k}$$

Here $\mathbf{i} = \begin{pmatrix}1\\0\\0\end{pmatrix}$, $\mathbf{j} = \begin{pmatrix}0\\1\\0\end{pmatrix}$, and $\mathbf{k} = \begin{pmatrix}0\\0\\1\end{pmatrix}$ are the **standard basis vectors**. They point along the positive $x$, $y$, and $z$ axes respectively, and each has magnitude $1$.

### The "Why"

Vectors are the language of physics, engineering, and three-dimensional geometry. Forces, velocities, displacements, and electric fields are all vectors. The operations we learn in this lesson — dot product, cross product, finding angles — are the essential tools for working with these quantities.

---

## 1. Magnitude of a Vector

The **magnitude** (also called **length** or **norm**) of a vector $\vec{v} = \begin{pmatrix}x\\y\\z\end{pmatrix}$ is the distance from the origin to the point $(x, y, z)$. By the Pythagorean theorem extended to three dimensions:

$$\boxed{|\vec{v}| = \sqrt{x^2 + y^2 + z^2}}$$

For a two-dimensional vector $\begin{pmatrix}x\\y\end{pmatrix}$, the magnitude is $|\vec{v}| = \sqrt{x^2 + y^2}$.

**Example:** The magnitude of $\begin{pmatrix}2\\-3\\6\end{pmatrix}$ is $\sqrt{2^2 + (-3)^2 + 6^2} = \sqrt{4 + 9 + 36} = \sqrt{49} = 7$.

A **unit vector** is a vector whose magnitude is exactly $1$. To create a unit vector that points in the same direction as a given vector $\vec{v}$, divide each component by the magnitude:

$$\hat{v} = \frac{\vec{v}}{|\vec{v}|}$$

The hat symbol ($\hat{v}$) is standard notation for a unit vector.

---

## 2. The Dot Product (Scalar Product)

### What It Is

The **dot product** (also called the **scalar product**) is an operation that takes two vectors and produces a single number (a scalar). There are two equivalent ways to compute it, each useful in different situations.

**Algebraic definition (using components):**
If $\vec{v} = \begin{pmatrix}v_1\\v_2\\v_3\end{pmatrix}$ and $\vec{w} = \begin{pmatrix}w_1\\w_2\\w_3\end{pmatrix}$, then:

$$\vec{v} \cdot \vec{w} = v_1 w_1 + v_2 w_2 + v_3 w_3$$

Multiply corresponding components and add the results.

**Geometric definition (using magnitudes and angle):**
If $\theta$ is the angle between $\vec{v}$ and $\vec{w}$ (with $0 \leq \theta \leq \pi$), then:

$$\vec{v} \cdot \vec{w} = |\vec{v}|\,|\vec{w}|\,\cos\theta$$

These two definitions are equivalent — they give the same result. The geometric definition reveals what the dot product actually measures: it is the product of the magnitudes, scaled by the cosine of the angle between them.

### Properties of the Dot Product

- **Commutative:** $\vec{v}\cdot\vec{w} = \vec{w}\cdot\vec{v}$. The order does not matter.
- **Distributive:** $\vec{u}\cdot(\vec{v}+\vec{w}) = \vec{u}\cdot\vec{v} + \vec{u}\cdot\vec{w}$.
- **Scalar multiplication:** $(k\vec{v})\cdot\vec{w} = k(\vec{v}\cdot\vec{w})$. You can pull a scalar factor out.
- **Self dot product:** $\vec{v}\cdot\vec{v} = |\vec{v}|^2$. The dot product of a vector with itself gives the square of its magnitude.

---

## 3. Finding the Angle Between Two Vectors

The most important application of the dot product is finding the angle between two vectors. By rearranging the geometric definition:

$$\boxed{\cos\theta = \frac{\vec{v}\cdot\vec{w}}{|\vec{v}|\,|\vec{w}|}}$$

To find $\theta$, compute the dot product, compute both magnitudes, divide, and then take the inverse cosine.

---

## Worked Example 1: Angle Between Two Vectors

**Problem:** Find the angle between $\vec{a} = \begin{pmatrix}1\\2\\2\end{pmatrix}$ and $\vec{b} = \begin{pmatrix}3\\0\\4\end{pmatrix}$.

**Approach:** Use the angle formula. Compute the dot product and both magnitudes, then take $\cos^{-1}$ of the result.

**Step 1 — Dot product:**
$$\vec{a}\cdot\vec{b} = 1(3) + 2(0) + 2(4) = 3 + 0 + 8 = 11$$

**Step 2 — Magnitudes:**
$$|\vec{a}| = \sqrt{1^2 + 2^2 + 2^2} = \sqrt{1 + 4 + 4} = \sqrt{9} = 3$$
$$|\vec{b}| = \sqrt{3^2 + 0^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5$$

**Step 3 — Compute $\cos\theta$:**
$$\cos\theta = \frac{11}{3 \times 5} = \frac{11}{15}$$

**Step 4 — Find $\theta$:**
$$\theta = \cos^{-1}\!\left(\frac{11}{15}\right) \approx 42.8^\circ$$

**Why this makes sense:** The angle is acute (less than $90^\circ$), which is consistent with a positive dot product ($11 > 0$). When the dot product is positive, the angle is acute. When it is negative, the angle is obtuse.

---

## 4. Orthogonal (Perpendicular) Vectors

Two non-zero vectors are **orthogonal** (another word for perpendicular) if the angle between them is $90^\circ$, which means $\cos\theta = 0$. From the dot product formula:

$$\boxed{\vec{v} \cdot \vec{w} = 0 \;\Longleftrightarrow\; \vec{v} \perp \vec{w}}$$

**A common misconception:** Students sometimes think that if the dot product is zero, one of the vectors must be the zero vector. That is not true. Two non-zero vectors can have a dot product of zero when they are perpendicular.

---

## Worked Example 2: Finding a Component for Orthogonality

**Problem:** Find the value of $k$ such that $\vec{p} = \begin{pmatrix}2\\k\\3\end{pmatrix}$ is orthogonal to $\vec{q} = \begin{pmatrix}1\\-2\\4\end{pmatrix}$.

**Approach:** For two vectors to be orthogonal, their dot product must be zero. Compute the dot product in terms of $k$, set it equal to zero, and solve.

**Step 1 — Compute the dot product:**
$$\vec{p}\cdot\vec{q} = 2(1) + k(-2) + 3(4) = 2 - 2k + 12 = 14 - 2k$$

**Step 2 — Set equal to zero and solve:**
$$14 - 2k = 0$$
$$2k = 14$$
$$k = 7$$

**Answer:** $k = 7$

---

## 5. The Cross Product (Vector Product)

### What It Is

The **cross product** (also called the **vector product**) is an operation that takes two vectors in three-dimensional space and produces a third vector. The result vector is perpendicular to both of the original vectors.

**A common misconception:** The dot product and cross product are completely different operations. The dot product produces a scalar. The cross product produces a vector. They are not interchangeable.

### Computing the Cross Product

If $\vec{v} = \begin{pmatrix}v_1\\v_2\\v_3\end{pmatrix}$ and $\vec{w} = \begin{pmatrix}w_1\\w_2\\w_3\end{pmatrix}$, then:

$$\boxed{\vec{v} \times \vec{w} = \begin{pmatrix} v_2 w_3 - v_3 w_2 \\ v_3 w_1 - v_1 w_3 \\ v_1 w_2 - v_2 w_1 \end{pmatrix}}$$

A convenient way to remember this uses the determinant of a matrix with $\mathbf{i}, \mathbf{j}, \mathbf{k}$ in the first row:

$$\vec{v} \times \vec{w} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ v_1 & v_2 & v_3 \\ w_1 & w_2 & w_3 \end{vmatrix}$$

### Key Properties of the Cross Product

- **Anti-commutative:** $\vec{v}\times\vec{w} = -(\vec{w}\times\vec{v})$. Swapping the order reverses the direction.
- **Magnitude:** $|\vec{v}\times\vec{w}| = |\vec{v}|\,|\vec{w}|\,\sin\theta$. This is the area of the parallelogram spanned by $\vec{v}$ and $\vec{w}$.
- **Parallel vectors:** If $\vec{v}$ and $\vec{w}$ are parallel (pointing in the same or opposite directions), then $\theta = 0$ or $\pi$, so $\sin\theta = 0$, and $\vec{v}\times\vec{w} = \vec{0}$.
- The direction of $\vec{v}\times\vec{w}$ is given by the **right-hand rule**: point your right hand's fingers in the direction of $\vec{v}$, curl them toward $\vec{w}$, and your thumb points in the direction of the cross product.

---

## Worked Example 3: Computing a Cross Product

**Problem:** Find $\vec{a}\times\vec{b}$ where $\vec{a} = \begin{pmatrix}2\\1\\0\end{pmatrix}$ and $\vec{b} = \begin{pmatrix}3\\-1\\2\end{pmatrix}$. Verify the result is perpendicular to both $\vec{a}$ and $\vec{b}$.

**Approach:** Use the component formula for the cross product. Then verify perpendicularity by checking that the dot product of the result with each original vector is zero.

**Step 1 — Compute each component:**
First component: $a_2 b_3 - a_3 b_2 = 1(2) - 0(-1) = 2$.

Second component: $a_3 b_1 - a_1 b_3 = 0(3) - 2(2) = -4$.

Third component: $a_1 b_2 - a_2 b_1 = 2(-1) - 1(3) = -5$.

$$\vec{a}\times\vec{b} = \begin{pmatrix}2\\-4\\-5\end{pmatrix}$$

**Step 2 — Verify perpendicularity with $\vec{a}$:**
$\vec{a}\cdot(\vec{a}\times\vec{b}) = 2(2) + 1(-4) + 0(-5) = 4 - 4 + 0 = 0$. This confirms perpendicularity.

**Step 3 — Verify perpendicularity with $\vec{b}$:**
$\vec{b}\cdot(\vec{a}\times\vec{b}) = 3(2) + (-1)(-4) + 2(-5) = 6 + 4 - 10 = 0$. Confirmed.

**Answer:** $\vec{a}\times\vec{b} = \begin{pmatrix}2\\-4\\-5\end{pmatrix}$

---

## Worked Example 4: Area of a Triangle Using Cross Product

**Problem:** Find the area of the triangle with vertices $A(0,0,0)$, $B(2,3,1)$, and $C(4,1,5)$.

**Approach:** The area of a triangle is half the area of the parallelogram formed by two side vectors. The area of the parallelogram is the magnitude of the cross product of those two side vectors.

**Step 1 — Find side vectors from $A$:**
$$\overrightarrow{AB} = \begin{pmatrix}2-0\\3-0\\1-0\end{pmatrix} = \begin{pmatrix}2\\3\\1\end{pmatrix}$$
$$\overrightarrow{AC} = \begin{pmatrix}4-0\\1-0\\5-0\end{pmatrix} = \begin{pmatrix}4\\1\\5\end{pmatrix}$$

**Step 2 — Compute the cross product:**
$$\overrightarrow{AB}\times\overrightarrow{AC} = \begin{pmatrix}3(5)-1(1)\\1(4)-2(5)\\2(1)-3(4)\end{pmatrix} = \begin{pmatrix}15-1\\4-10\\2-12\end{pmatrix} = \begin{pmatrix}14\\-6\\-10\end{pmatrix}$$

**Step 3 — Find the magnitude (parallelogram area):**
$$|\overrightarrow{AB}\times\overrightarrow{AC}| = \sqrt{14^2 + (-6)^2 + (-10)^2} = \sqrt{196 + 36 + 100} = \sqrt{332}$$

**Step 4 — Half for triangle area:**
$$\text{Area} = \frac{1}{2}\sqrt{332} = \sqrt{83}$$

**Answer:** The area is $\sqrt{83}$ square units.

---

## Summary of Key Formulas

| Concept | Formula |
|---------|---------|
| Magnitude | $|\vec{v}| = \sqrt{x^2 + y^2 + z^2}$ |
| Dot product (components) | $\vec{v}\cdot\vec{w} = v_1w_1 + v_2w_2 + v_3w_3$ |
| Dot product (geometric) | $\vec{v}\cdot\vec{w} = |\vec{v}||\vec{w}|\cos\theta$ |
| Angle between vectors | $\cos\theta = \dfrac{\vec{v}\cdot\vec{w}}{|\vec{v}||\vec{w}|}$ |
| Orthogonal test | $\vec{v}\cdot\vec{w} = 0$ |
| Cross product | $\vec{v}\times\vec{w} = \begin{pmatrix}v_2w_3-v_3w_2\\v_3w_1-v_1w_3\\v_1w_2-v_2w_1\end{pmatrix}$ |
| Cross product magnitude | $|\vec{v}\times\vec{w}| = |\vec{v}||\vec{w}|\sin\theta$ |

---

## Practice Problems

**Problem 1:** Let $\vec{a} = \begin{pmatrix}3\\-2\\4\end{pmatrix}$ and $\vec{b} = \begin{pmatrix}-1\\5\\2\end{pmatrix}$. Find:
(a) The magnitude $|\vec{a}|$.
(b) The dot product $\vec{a}\cdot\vec{b}$.
(c) The angle between $\vec{a}$ and $\vec{b}$, in degrees to one decimal place.

**Problem 2:** Show that the vectors $\vec{u} = \begin{pmatrix}4\\-1\\2\end{pmatrix}$ and $\vec{v} = \begin{pmatrix}3\\6\\-3\end{pmatrix}$ are orthogonal.

**Problem 3:** Find the value of $p$ such that the vector $\vec{m} = \begin{pmatrix}p\\2\\-1\end{pmatrix}$ is parallel to the vector $\vec{n} = \begin{pmatrix}6\\4\\-2\end{pmatrix}$.

**Problem 4:** Compute the cross product $\vec{a}\times\vec{b}$ for $\vec{a} = \mathbf{i} - 2\mathbf{j} + 3\mathbf{k}$ and $\vec{b} = 2\mathbf{i} + \mathbf{j} - 4\mathbf{k}$. Verify that your result is perpendicular to both $\vec{a}$ and $\vec{b}$.

**Problem 5 (IB-style):** Two vectors $\vec{p}$ and $\vec{q}$ are given by $\vec{p} = \begin{pmatrix}1\\3\\-2\end{pmatrix}$ and $\vec{q} = \begin{pmatrix}4\\0\\5\end{pmatrix}$.
(a) Find the area of the parallelogram formed by $\vec{p}$ and $\vec{q}$. [3 marks]
(b) A triangle has two sides represented by $\vec{p}$ and $\vec{q}$. Find the area of this triangle. [1 mark]

**Problem 6:** Given that $|\vec{a}| = 4$, $|\vec{b}| = 5$, and the angle between $\vec{a}$ and $\vec{b}$ is $60^\circ$, find:
(a) The dot product $\vec{a}\cdot\vec{b}$.
(b) The magnitude of the cross product, $|\vec{a}\times\vec{b}|$.
(c) The absolute value $|(\vec{a}+\vec{b})\cdot(\vec{a}-\vec{b})|$.

---

## Answers

**Answer 1:**

**(a)** $|\vec{a}| = \sqrt{3^2 + (-2)^2 + 4^2} = \sqrt{9 + 4 + 16} = \sqrt{29}$.

**(b)** $\vec{a}\cdot\vec{b} = 3(-1) + (-2)(5) + 4(2) = -3 - 10 + 8 = -5$.

**(c)** First find $|\vec{b}| = \sqrt{(-1)^2 + 5^2 + 2^2} = \sqrt{1 + 25 + 4} = \sqrt{30}$.

Then $\cos\theta = \frac{-5}{\sqrt{29}\sqrt{30}} \approx \frac{-5}{29.50} \approx -0.1695$.

$\theta = \cos^{-1}(-0.1695) \approx 99.7^\circ$.

The angle is obtuse because the dot product is negative.

---

**Answer 2:**

Compute the dot product: $\vec{u}\cdot\vec{v} = 4(3) + (-1)(6) + 2(-3) = 12 - 6 - 6 = 0$.

Since the dot product is zero and both vectors are non-zero, they are orthogonal.

---

**Answer 3:**

If two vectors are parallel, one is a scalar multiple of the other. There exists some $k$ such that:

$\begin{pmatrix}p\\2\\-1\end{pmatrix} = k\begin{pmatrix}6\\4\\-2\end{pmatrix}$

From the third component: $-1 = k(-2)$, so $k = \frac{1}{2}$.

Check the second component: $2 = \frac{1}{2}(4) = 2$, which is consistent.

From the first component: $p = \frac{1}{2}(6) = 3$.

**Answer:** $p = 3$

---

**Answer 4:**

$\vec{a} = \begin{pmatrix}1\\-2\\3\end{pmatrix}$, $\vec{b} = \begin{pmatrix}2\\1\\-4\end{pmatrix}$.

$\vec{a}\times\vec{b} = \begin{pmatrix}(-2)(-4) - (3)(1)\\(3)(2) - (1)(-4)\\(1)(1) - (-2)(2)\end{pmatrix} = \begin{pmatrix}8-3\\6+4\\1+4\end{pmatrix} = \begin{pmatrix}5\\10\\5\end{pmatrix}$.

Verification with $\vec{a}$: $5(1) + 10(-2) + 5(3) = 5 - 20 + 15 = 0$. ✓

Verification with $\vec{b}$: $5(2) + 10(1) + 5(-4) = 10 + 10 - 20 = 0$. ✓

Both dot products are zero, confirming perpendicularity.

---

**Answer 5:**

**(a)** $\vec{p}\times\vec{q} = \begin{pmatrix}3(5) - (-2)(0)\\(-2)(4) - 1(5)\\1(0) - 3(4)\end{pmatrix} = \begin{pmatrix}15\\-8-5\\-12\end{pmatrix} = \begin{pmatrix}15\\-13\\-12\end{pmatrix}$.

The area of the parallelogram is the magnitude: $\sqrt{15^2 + (-13)^2 + (-12)^2} = \sqrt{225 + 169 + 144} = \sqrt{538}$.

**(b)** The triangle area is half the parallelogram area: $\frac{1}{2}\sqrt{538}$ square units.

---

**Answer 6:**

**(a)** Using the geometric definition: $\vec{a}\cdot\vec{b} = |\vec{a}||\vec{b}|\cos 60^\circ = 4 \times 5 \times \frac{1}{2} = 10$.

**(b)** $|\vec{a}\times\vec{b}| = |\vec{a}||\vec{b}|\sin 60^\circ = 4 \times 5 \times \frac{\sqrt{3}}{2} = 10\sqrt{3}$.

**(c)** Expand the dot product:

$(\vec{a}+\vec{b})\cdot(\vec{a}-\vec{b}) = \vec{a}\cdot\vec{a} - \vec{a}\cdot\vec{b} + \vec{b}\cdot\vec{a} - \vec{b}\cdot\vec{b}$

Since the dot product is commutative, $-\vec{a}\cdot\vec{b} + \vec{b}\cdot\vec{a} = 0$.

So the expression simplifies to $|\vec{a}|^2 - |\vec{b}|^2 = 16 - 25 = -9$.

The absolute value is $|-9| = 9$.
