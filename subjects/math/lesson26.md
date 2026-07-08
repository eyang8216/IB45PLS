# Lesson 26 — Lines in Three-Dimensional Space

## What Is a Line in 3D?

### The "What"

In two dimensions, a line can be described by a single Cartesian equation like $y = 2x + 1$. In three dimensions, a single equation cannot describe a line — it describes a plane. To describe a line in 3D, you need a different approach.

A line in three-dimensional space is completely determined by two pieces of information:

- A **point** on the line (any one point will do).
- A **direction vector** — any non-zero vector that points along the line.

The idea is simple: start at the known point, then travel any distance in the direction of the direction vector (or opposite to it). This traces out the entire line.

### The "Why"

Lines in 3D appear everywhere in applications: the path of a moving object, the intersection of two planes, the line of sight from a camera. Being able to describe lines mathematically and to work with them (finding intersections, angles, and distances) is fundamental to 3D geometry.

---

## 1. Vector Equation of a Line

Let $A$ be a known point on the line. Let $\vec{a}$ be the **position vector** of $A$ (the vector from the origin to $A$). Let $\vec{d}$ be a non-zero **direction vector** parallel to the line.

The **vector equation** of the line is:

$$\boxed{\vec{r} = \vec{a} + \lambda\vec{d},\quad \lambda \in \mathbb{R}}$$

Here $\lambda$ (lambda) is a **parameter** — a real number that can take any value. Each value of $\lambda$ produces a position vector $\vec{r}$ for a different point on the line.

- When $\lambda = 0$, $\vec{r} = \vec{a}$, so we are at the known point $A$.
- When $\lambda = 1$, $\vec{r} = \vec{a} + \vec{d}$, so we have moved one step in the direction of $\vec{d}$.
- When $\lambda$ is negative, we move in the opposite direction of $\vec{d}$.

---

## 2. Parametric Equations of a Line

If the known point has coordinates $A(x_0, y_0, z_0)$ and the direction vector is $\vec{d} = \begin{pmatrix}d_1\\d_2\\d_3\end{pmatrix}$, then the vector equation expands into three separate equations, one for each coordinate:

$$\boxed{\begin{cases} x = x_0 + \lambda d_1 \\ y = y_0 + \lambda d_2 \\ z = z_0 + \lambda d_3 \end{cases}}$$

These are called the **parametric equations** of the line. The name comes from the fact that the coordinates are expressed in terms of the parameter $\lambda$.

---

## Worked Example 1: Writing Equations of a Line

**Problem:** Write the vector equation and the parametric equations of the line that passes through the point $A(2, -1, 4)$ and has direction vector $\vec{d} = \begin{pmatrix}3\\2\\-5\end{pmatrix}$.

**Approach:** Substitute the given point and direction vector directly into the formulas.

**Step 1 — Vector equation:**
$$\vec{r} = \begin{pmatrix}2\\-1\\4\end{pmatrix} + \lambda\begin{pmatrix}3\\2\\-5\end{pmatrix}, \quad \lambda \in \mathbb{R}$$

**Step 2 — Parametric equations:**
$$x = 2 + 3\lambda,\quad y = -1 + 2\lambda,\quad z = 4 - 5\lambda$$

**Why this makes sense:** When $\lambda = 0$, we get $(2, -1, 4)$, the given point. When $\lambda = 1$, we get $(5, 1, -1)$, which is one step along the direction vector.

---

## 3. Cartesian (Symmetric) Form of a Line

If none of the direction vector components $d_1, d_2, d_3$ is zero, we can solve each parametric equation for $\lambda$:

$$\lambda = \frac{x - x_0}{d_1} = \frac{y - y_0}{d_2} = \frac{z - z_0}{d_3}$$

This gives the **Cartesian form** (also called **symmetric form**):

$$\boxed{\frac{x - x_0}{d_1} = \frac{y - y_0}{d_2} = \frac{z - z_0}{d_3}}$$

**What if a component is zero?** If, for example, $d_1 = 0$, then $x$ never changes (it is always $x_0$). You cannot divide by zero, so you write $x = x_0$ separately and keep the equalities for the other two coordinates:

$$\frac{y - y_0}{d_2} = \frac{z - z_0}{d_3},\quad x = x_0$$

---

## Worked Example 2: Converting to Cartesian Form

**Problem:** Convert the line $\vec{r} = \begin{pmatrix}1\\-3\\2\end{pmatrix} + \lambda\begin{pmatrix}2\\4\\-6\end{pmatrix}$ to Cartesian form.

**Approach:** Write $\frac{x - x_0}{d_1} = \frac{y - y_0}{d_2} = \frac{z - z_0}{d_3}$, then simplify fractions if possible.

**Step 1 — Write the raw form:**
$$\frac{x - 1}{2} = \frac{y - (-3)}{4} = \frac{z - 2}{-6}$$
$$\frac{x - 1}{2} = \frac{y + 3}{4} = \frac{z - 2}{-6}$$

**Step 2 — Simplify by dividing each denominator by 2:**
$$\frac{x - 1}{1} = \frac{y + 3}{2} = \frac{z - 2}{-3}$$

**Answer:** $\dfrac{x - 1}{1} = \dfrac{y + 3}{2} = \dfrac{z - 2}{-3}$

---

## 4. Finding a Line Through Two Points

If you know two points $A$ and $B$ on a line, you can construct the line's equation by:

1. Using either point as the "known point" $\vec{a}$.
2. Computing the direction vector as the difference: $\vec{d} = \vec{b} - \vec{a} = \overrightarrow{AB}$.

The line through $A$ and $B$ is:

$$\boxed{\vec{r} = \vec{a} + \lambda(\vec{b} - \vec{a})}$$

An alternative form is $\vec{r} = (1-\lambda)\vec{a} + \lambda\vec{b}$. When $\lambda = 0$ this gives $\vec{a}$ (point $A$). When $\lambda = 1$ this gives $\vec{b}$ (point $B$).

---

## Worked Example 3: Line Through Two Points

**Problem:** Find the vector equation of the line passing through $P(3, 1, -2)$ and $Q(7, -3, 4)$.

**Approach:** Use $\vec{p}$ as the known point. Compute the direction vector $\vec{d} = \vec{q} - \vec{p}$.

**Step 1 — Compute the direction vector:**
$$\vec{d} = \begin{pmatrix}7\\-3\\4\end{pmatrix} - \begin{pmatrix}3\\1\\-2\end{pmatrix} = \begin{pmatrix}4\\-4\\6\end{pmatrix}$$

**Step 2 — Write the vector equation:**
$$\vec{r} = \begin{pmatrix}3\\1\\-2\end{pmatrix} + \lambda\begin{pmatrix}4\\-4\\6\end{pmatrix}$$

The direction vector can be simplified by dividing by $2$: $\begin{pmatrix}2\\-2\\3\end{pmatrix}$. Multiplying $\lambda$ by the same factor gives the same line.

**Check:** When $\lambda = 0$, $\vec{r} = \begin{pmatrix}3\\1\\-2\end{pmatrix} = P$. When $\lambda = 1$, $\vec{r} = \begin{pmatrix}7\\-3\\4\end{pmatrix} = Q$. Both points are on the line.

---

## 5. Parallel Lines

Two lines are **parallel** if their direction vectors are scalar multiples of each other.

If line $L_1$ has direction $\vec{d}_1$ and line $L_2$ has direction $\vec{d}_2$, then:

- $L_1 \parallel L_2$ exactly when $\vec{d}_1 = k\vec{d}_2$ for some non-zero real number $k$.

If the lines are parallel, there are two possibilities:

- **Distinct parallel lines:** The lines never intersect. They are like railway tracks.
- **Coincident lines:** The lines are the same line (one lies on top of the other). To check, test whether a point from one line lies on the other line.

If two lines are not parallel and do not intersect, they are called **skew lines**. Skew lines exist only in three or more dimensions.

---

## 6. Angle Between Two Lines

The angle between two lines is defined as the acute angle ($0^\circ$ to $90^\circ$) between their direction vectors. The formula uses the dot product with an absolute value (to ensure the angle is acute):

$$\boxed{\cos\theta = \frac{|\vec{d}_1 \cdot \vec{d}_2|}{|\vec{d}_1|\,|\vec{d}_2|}}$$

The absolute value in the numerator guarantees that $\cos\theta \geq 0$, so $\theta \leq 90^\circ$. This makes sense because lines do not have an orientation — the angle between a line and another line is the same as the angle between the first line and the reverse of the second.

---

## Worked Example 4: Angle Between Two Lines

**Problem:** Find the angle between the lines:

$L_1: \vec{r} = \begin{pmatrix}1\\0\\2\end{pmatrix} + \lambda\begin{pmatrix}2\\1\\-2\end{pmatrix}$

$L_2: \dfrac{x-3}{1} = \dfrac{y+1}{2} = \dfrac{z}{2}$

**Approach:** Extract the direction vector from each line. From $L_1$ it is directly visible. From $L_2$ (Cartesian form), the denominators are the components of the direction vector. Then use the angle formula.

**Step 1 — Extract direction vectors:**
$\vec{d}_1 = \begin{pmatrix}2\\1\\-2\end{pmatrix}$, $\vec{d}_2 = \begin{pmatrix}1\\2\\2\end{pmatrix}$.

**Step 2 — Compute magnitudes:**
$|\vec{d}_1| = \sqrt{4 + 1 + 4} = \sqrt{9} = 3$.
$|\vec{d}_2| = \sqrt{1 + 4 + 4} = \sqrt{9} = 3$.

**Step 3 — Compute the dot product:**
$\vec{d}_1 \cdot \vec{d}_2 = 2(1) + 1(2) + (-2)(2) = 2 + 2 - 4 = 0$.

**Step 4 — Compute the angle:**
$\cos\theta = \frac{|0|}{3 \times 3} = 0$, so $\theta = 90^\circ$.

**Answer:** The lines are perpendicular.

---

## Summary Table

| Form | Equation |
|------|----------|
| Vector | $\vec{r} = \vec{a} + \lambda\vec{d}$ |
| Parametric | $x = x_0+\lambda d_1,\; y = y_0+\lambda d_2,\; z = z_0+\lambda d_3$ |
| Cartesian | $\dfrac{x-x_0}{d_1}=\dfrac{y-y_0}{d_2}=\dfrac{z-z_0}{d_3}$ |
| Through two points | $\vec{r} = \vec{a} + \lambda(\vec{b}-\vec{a})$ |
| Parallel test | $\vec{d}_1 = k\vec{d}_2$ for some $k \neq 0$ |
| Angle between lines | $\cos\theta = \dfrac{|\vec{d}_1\cdot\vec{d}_2|}{|\vec{d}_1||\vec{d}_2|}$ |

---

## Practice Problems

**Problem 1:** Find the vector equation, parametric equations, and Cartesian equation of the line through $A(5, -2, 3)$ with direction vector $\vec{d} = \begin{pmatrix}2\\6\\-4\end{pmatrix}$.

**Problem 2:** Find the vector equation of the line passing through the points $P(2, 4, -1)$ and $Q(8, -2, 5)$. Simplify the direction vector if possible.

**Problem 3:** Determine whether the lines $L_1: \vec{r} = \begin{pmatrix}1\\3\\-2\end{pmatrix} + \lambda\begin{pmatrix}2\\-1\\4\end{pmatrix}$ and $L_2: \vec{r} = \begin{pmatrix}5\\1\\6\end{pmatrix} + \mu\begin{pmatrix}-4\\2\\-8\end{pmatrix}$ are parallel. If they are parallel, determine whether they are distinct or coincident.

**Problem 4:** Find the angle between the lines $L_1: \dfrac{x-2}{3} = \dfrac{y+1}{-2} = \dfrac{z-4}{1}$ and $L_2: \dfrac{x+1}{2} = \dfrac{y-3}{4} = \dfrac{z}{-1}$.

**Problem 5 (IB-style):** A line $L$ has Cartesian equation $\dfrac{x-3}{2} = \dfrac{y+4}{-3} = \dfrac{z-1}{5}$.
(a) Find the coordinates of the point on $L$ corresponding to the parameter value $\lambda = -1$. [1 mark]
(b) Find the coordinates of the point where $L$ meets the $xy$-plane. [2 marks]

**Problem 6:** Find the Cartesian equation of the line that passes through $A(3, 0, 5)$ and is parallel to the line given by $\vec{r} = \begin{pmatrix}1\\2\\-1\end{pmatrix} + t\begin{pmatrix}-2\\3\\4\end{pmatrix}$.

---

## Answers

**Answer 1:**

Vector: $\vec{r} = \begin{pmatrix}5\\-2\\3\end{pmatrix} + \lambda\begin{pmatrix}2\\6\\-4\end{pmatrix}$.

Parametric: $x = 5 + 2\lambda$, $y = -2 + 6\lambda$, $z = 3 - 4\lambda$.

For Cartesian form: $\dfrac{x-5}{2} = \dfrac{y+2}{6} = \dfrac{z-3}{-4}$.

Dividing each denominator by $2$: $\dfrac{x-5}{1} = \dfrac{y+2}{3} = \dfrac{z-3}{-2}$.

---

**Answer 2:**

Direction: $\vec{d} = \begin{pmatrix}8-2\\-2-4\\5-(-1)\end{pmatrix} = \begin{pmatrix}6\\-6\\6\end{pmatrix}$.

Simplify by dividing by $6$: $\vec{d} = \begin{pmatrix}1\\-1\\1\end{pmatrix}$.

$\vec{r} = \begin{pmatrix}2\\4\\-1\end{pmatrix} + \lambda\begin{pmatrix}1\\-1\\1\end{pmatrix}$.

---

**Answer 3:**

Check if direction vectors are scalar multiples: $\vec{d}_2 = \begin{pmatrix}-4\\2\\-8\end{pmatrix} = -2\begin{pmatrix}2\\-1\\4\end{pmatrix} = -2\vec{d}_1$. Yes, they are parallel.

To check coincidence: does the point $(5, 1, 6)$ from $L_2$ lie on $L_1$?

We need $\lambda$ such that $\begin{pmatrix}1\\3\\-2\end{pmatrix} + \lambda\begin{pmatrix}2\\-1\\4\end{pmatrix} = \begin{pmatrix}5\\1\\6\end{pmatrix}$.

From the $x$-coordinate: $1 + 2\lambda = 5$, so $\lambda = 2$.

Check $y$: $3 + 2(-1) = 3 - 2 = 1$. Matches.

Check $z$: $-2 + 2(4) = -2 + 8 = 6$. Matches.

Since the point lies on $L_1$, the lines are **coincident** (they are the same line).

---

**Answer 4:**

$\vec{d}_1 = \begin{pmatrix}3\\-2\\1\end{pmatrix}$, $|\vec{d}_1| = \sqrt{9 + 4 + 1} = \sqrt{14}$.

$\vec{d}_2 = \begin{pmatrix}2\\4\\-1\end{pmatrix}$, $|\vec{d}_2| = \sqrt{4 + 16 + 1} = \sqrt{21}$.

$\vec{d}_1\cdot\vec{d}_2 = 3(2) + (-2)(4) + 1(-1) = 6 - 8 - 1 = -3$.

$\cos\theta = \dfrac{|-3|}{\sqrt{14}\sqrt{21}} = \dfrac{3}{\sqrt{294}} = \dfrac{3}{7\sqrt{6}}$.

$\theta \approx 79.9^\circ$.

---

**Answer 5:**

First, write parametric equations: $x = 3 + 2\lambda$, $y = -4 - 3\lambda$, $z = 1 + 5\lambda$.

**(a)** For $\lambda = -1$: $x = 3 + 2(-1) = 1$, $y = -4 - 3(-1) = -1$, $z = 1 + 5(-1) = -4$.

Point: $(1, -1, -4)$.

**(b)** The $xy$-plane is where $z = 0$. Set $1 + 5\lambda = 0$, so $\lambda = -\frac{1}{5}$.

Then $x = 3 + 2(-\frac{1}{5}) = 3 - \frac{2}{5} = \frac{13}{5}$.

$y = -4 - 3(-\frac{1}{5}) = -4 + \frac{3}{5} = -\frac{17}{5}$.

Point: $\left(\frac{13}{5}, -\frac{17}{5}, 0\right)$.

---

**Answer 6:**

Parallel lines have the same direction vector. So $\vec{d} = \begin{pmatrix}-2\\3\\4\end{pmatrix}$.

The line passes through $(3, 0, 5)$.

Cartesian form: $\dfrac{x-3}{-2} = \dfrac{y-0}{3} = \dfrac{z-5}{4}$.
