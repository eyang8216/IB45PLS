# Lesson 24: Roots of Unity and Solving $z^n = c$

## What Are Roots of Complex Numbers?

### The "What"

In real numbers, the equation $x^2 = 4$ has two solutions: $x = 2$ and $x = -2$. The equation $x^3 = 8$ has one real solution: $x = 2$. But the equation $x^2 = -1$ has no real solutions at all.

In complex numbers, everything changes. The equation $z^n = c$ (where $c$ is any non-zero complex number and $n$ is a positive integer) always has exactly $n$ distinct solutions. These solutions are called the **$n$th roots** of $c$.

For example, the equation $z^3 = 8$ has three solutions in the complex numbers, not just one. Two of them are non-real.

### The "Why"

Understanding roots of complex numbers is essential for solving polynomial equations completely. The Fundamental Theorem of Algebra states that every polynomial of degree $n$ has exactly $n$ complex roots (counting multiplicity). Many of those roots may be non-real, even when the coefficients are real numbers. The techniques in this lesson give you a systematic way to find all of them.

---

## 1. The General Formula for $n$th Roots

Let $c$ be a non-zero complex number. Write $c$ in exponential form: $c = re^{i\theta}$, where $r = |c|$ and $\theta = \arg(c)$.

We want to find all complex numbers $z$ such that $z^n = c$. Write $z$ in exponential form: $z = \rho e^{i\phi}$, where $\rho = |z|$ and $\phi = \arg(z)$.

Then:
$$(\rho e^{i\phi})^n = re^{i\theta}$$

This gives $\rho^n e^{in\phi} = re^{i\theta}$.

Equating the moduli: $\rho^n = r$, so $\rho = r^{1/n}$. (Here $r^{1/n}$ means the positive real $n$th root of the positive real number $r$.)

Equating the arguments: $n\phi = \theta + 2\pi k$, where $k$ is any integer. The reason we add $2\pi k$ is that angles are periodic: adding $2\pi$ to an angle does not change the direction it points.

Dividing by $n$: $\phi = \frac{\theta + 2\pi k}{n}$.

Different values of $k$ give different angles. However, after $k = 0, 1, 2, \ldots, n-1$, the angles start repeating (because adding $n$ to $k$ adds $2\pi$ to $\phi$, which is the same direction).

Therefore, the $n$ distinct $n$th roots of $c$ are:

$$\boxed{z_k = r^{1/n} \cdot \exp\!\left(i\,\frac{\theta + 2\pi k}{n}\right),\quad k = 0, 1, 2, \ldots, n-1}$$

**A common misconception:** Some students think that $z^n = c$ has only the "obvious" real root. For example, they might think $z^3 = 8$ has only $z = 2$. But in the complex numbers, there are three cube roots of $8$, equally spaced around a circle of radius $2$ in the complex plane.

---

## 2. Roots of Unity: The Special Case $z^n = 1$

When $c = 1$, the equation $z^n = 1$ has a special name: its solutions are the **$n$th roots of unity**.

Since $1 = 1 \cdot e^{i \cdot 0}$, we have $r = 1$ and $\theta = 0$. The formula simplifies to:

$$\boxed{z_k = \exp\!\left(i\,\frac{2\pi k}{n}\right),\quad k = 0, 1, 2, \ldots, n-1}$$

All $n$th roots of unity lie on the **unit circle** (the circle of radius $1$ centered at the origin). They are equally spaced, with an angle of $\frac{2\pi}{n}$ between consecutive roots. The first root, $z_0$, is always $1$.

---

## Worked Example 1: Cube Roots of Unity

**Problem:** Find all solutions to $z^3 = 1$ and express them in Cartesian form.

**Approach:** Use the roots of unity formula with $n = 3$. There will be three solutions, spaced $120^\circ$ apart on the unit circle.

**Step 1 — Apply the formula:**
$n = 3$, so $z_k = \exp\!\left(i\frac{2\pi k}{3}\right)$ for $k = 0, 1, 2$.

**Step 2 — Compute each root:**

$k = 0$: $z_0 = e^{i \cdot 0} = 1$.

$k = 1$: $z_1 = e^{i \cdot 2\pi/3} = \cos\frac{2\pi}{3} + i\sin\frac{2\pi}{3} = -\frac{1}{2} + i\frac{\sqrt{3}}{2}$.

$k = 2$: $z_2 = e^{i \cdot 4\pi/3} = \cos\frac{4\pi}{3} + i\sin\frac{4\pi}{3} = -\frac{1}{2} - i\frac{\sqrt{3}}{2}$.

**Answer:** $z = 1,\; -\frac{1}{2} + i\frac{\sqrt{3}}{2},\; -\frac{1}{2} - i\frac{\sqrt{3}}{2}$.

The non-real cube roots are often denoted by the Greek letter $\omega$ (omega): $\omega = e^{i2\pi/3} = -\frac{1}{2} + i\frac{\sqrt{3}}{2}$ and $\omega^2 = e^{i4\pi/3} = -\frac{1}{2} - i\frac{\sqrt{3}}{2}$.

**Key property:** The sum of all cube roots of unity is zero: $1 + \omega + \omega^2 = 0$. This is true for all $n$th roots of unity when $n > 1$.

**Why this makes sense:** On the unit circle, these three points form an equilateral triangle. Their vector sum is zero because they are symmetrically arranged.

---

## Worked Example 2: Fourth Roots of Unity

**Problem:** Find all solutions to $z^4 = 1$.

**Approach:** Use $n = 4$ in the roots of unity formula.

**Step 1 — Apply the formula:**
$z_k = \exp\!\left(i\frac{2\pi k}{4}\right) = \exp\!\left(i\frac{\pi k}{2}\right)$ for $k = 0, 1, 2, 3$.

**Step 2 — Compute each root:**

$k = 0$: $z_0 = 1$.

$k = 1$: $z_1 = e^{i\pi/2} = i$.

$k = 2$: $z_2 = e^{i\pi} = -1$.

$k = 3$: $z_3 = e^{i3\pi/2} = -i$.

**Answer:** $z = 1, i, -1, -i$.

These are the four cardinal points on the unit circle. Their sum is $1 + i - 1 - i = 0$.

---

## 3. Solving $z^n = c$ for a General Complex $c$

### Worked Example 3: Solve $z^3 = 8i$

**Problem:** Find all cube roots of $8i$. Give answers in Cartesian form.

**Approach:** Write $8i$ in polar form, then apply the general $n$th roots formula with $n = 3$.

**Step 1 — Polar form of $8i$:**
$|8i| = 8$, $\arg(8i) = \frac{\pi}{2}$ (it lies on the positive imaginary axis).
So $8i = 8e^{i\pi/2}$.

**Step 2 — Apply the formula with $n = 3$, $r = 8$, $\theta = \frac{\pi}{2}$:**
$r^{1/3} = 8^{1/3} = 2$.

$z_k = 2 \cdot \exp\!\left(i\frac{\pi/2 + 2\pi k}{3}\right) = 2 \cdot \exp\!\left(i\frac{\pi + 4\pi k}{6}\right)$ for $k = 0, 1, 2$.

**Step 3 — Compute each root:**

$k = 0$: $z_0 = 2e^{i\pi/6} = 2\left(\frac{\sqrt{3}}{2} + i\frac{1}{2}\right) = \sqrt{3} + i$.

$k = 1$: $z_1 = 2e^{i5\pi/6} = 2\left(-\frac{\sqrt{3}}{2} + i\frac{1}{2}\right) = -\sqrt{3} + i$.

$k = 2$: $z_2 = 2e^{i9\pi/6} = 2e^{i3\pi/2} = 2(0 - i) = -2i$.

**Answer:** $z = \sqrt{3} + i,\; -\sqrt{3} + i,\; -2i$.

**Why this makes sense:** Check $(-2i)^3 = (-2)^3 \cdot i^3 = -8 \cdot (-i) = 8i$. This confirms one root. The three roots are equally spaced $120^\circ$ apart on a circle of radius $2$.

---

### Worked Example 4: Solve $z^4 = -16$

**Problem:** Find all four fourth roots of $-16$. Give answers in Cartesian form.

**Approach:** Express $-16$ in polar form and apply the formula with $n = 4$.

**Step 1 — Polar form of $-16$:**
$-16 = 16 \cdot (-1) = 16e^{i\pi}$.

$r^{1/4} = 16^{1/4} = 2$.

**Step 2 — Apply the formula:**
$z_k = 2 \cdot \exp\!\left(i\frac{\pi + 2\pi k}{4}\right)$ for $k = 0, 1, 2, 3$.

**Step 3 — Compute each root:**

$k = 0$: $z_0 = 2e^{i\pi/4} = 2\left(\frac{\sqrt{2}}{2} + i\frac{\sqrt{2}}{2}\right) = \sqrt{2} + i\sqrt{2}$.

$k = 1$: $z_1 = 2e^{i3\pi/4} = 2\left(-\frac{\sqrt{2}}{2} + i\frac{\sqrt{2}}{2}\right) = -\sqrt{2} + i\sqrt{2}$.

$k = 2$: $z_2 = 2e^{i5\pi/4} = 2\left(-\frac{\sqrt{2}}{2} - i\frac{\sqrt{2}}{2}\right) = -\sqrt{2} - i\sqrt{2}$.

$k = 3$: $z_3 = 2e^{i7\pi/4} = 2\left(\frac{\sqrt{2}}{2} - i\frac{\sqrt{2}}{2}\right) = \sqrt{2} - i\sqrt{2}$.

**Answer:** $z = \sqrt{2} + i\sqrt{2},\; -\sqrt{2} + i\sqrt{2},\; -\sqrt{2} - i\sqrt{2},\; \sqrt{2} - i\sqrt{2}$.

All four roots have modulus $2$ and are spaced $90^\circ$ apart, starting at angle $\frac{\pi}{4}$.

---

## 4. Primitive Roots of Unity

An $n$th root of unity $\zeta$ is called **primitive** if the powers $\zeta, \zeta^2, \zeta^3, \ldots, \zeta^{n-1}, \zeta^n = 1$ generate all $n$ of the $n$th roots of unity. In other words, a primitive root can produce every other root through repeated multiplication.

A root $\zeta_k = e^{i2\pi k/n}$ is primitive exactly when $k$ and $n$ share no common factor other than $1$ (that is, $\gcd(k, n) = 1$).

**Example:** For $n = 4$, the roots are $1, i, -1, -i$.

- $\zeta_1 = i$ (where $k = 1$, $\gcd(1,4) = 1$): powers are $i, i^2 = -1, i^3 = -i, i^4 = 1$. This generates all four roots. So $i$ is primitive.
- $\zeta_3 = -i$ (where $k = 3$, $\gcd(3,4) = 1$): powers are $-i, (-i)^2 = -1, (-i)^3 = i, (-i)^4 = 1$. This also generates all four. So $-i$ is primitive.
- $\zeta_2 = -1$ (where $k = 2$, $\gcd(2,4) = 2$): powers are $-1, 1$. This only generates two of the four roots. So $-1$ is not primitive.

---

## 5. Sum of All $n$th Roots of Unity

For any $n > 1$, the sum of all $n$th roots of unity is zero:

$$\sum_{k=0}^{n-1} e^{i2\pi k/n} = 0$$

**Why this is true:** The roots form a geometric series with first term $1$ and common ratio $\omega = e^{i2\pi/n}$. The sum of a geometric series with $n$ terms is:

$$S = \frac{1 - \omega^n}{1 - \omega} = \frac{1 - e^{i2\pi}}{1 - \omega} = \frac{1 - 1}{1 - \omega} = 0$$

This works because $\omega \neq 1$ (as long as $n > 1$).

---

## 6. Connection to Polynomial Equations

Knowing roots of unity helps factor polynomials. For example:

$$z^3 - 1 = (z - 1)(z^2 + z + 1)$$

The quadratic factor $z^2 + z + 1 = 0$ has roots $z = \frac{-1 \pm i\sqrt{3}}{2}$, which are precisely the non-real cube roots of unity $\omega$ and $\omega^2$.

---

## Practice Problems

**Problem 1:** Find all cube roots of $-8$ and express each in Cartesian form $a + bi$.

**Problem 2:** Solve the equation $z^4 = 81i$. Give all solutions in polar form $re^{i\theta}$.

**Problem 3:** Solve the quadratic equation $z^2 + z + 1 = 0$. Show that the solutions are the non-real cube roots of unity.

**Problem 4:** Solve the equation $z^5 = 32$. State how many of the solutions are real numbers and how many are non-real.

**Problem 5 (IB-style):** Let $\omega = e^{i2\pi/3}$ be a primitive cube root of unity.
(a) Show that $1 + \omega + \omega^2 = 0$. [2 marks]
(b) Hence, simplify the expression $(1 + \omega)(1 + \omega^2)$. [3 marks]

**Problem 6:** Find all fifth roots of unity in exponential form. Verify by direct calculation that their sum is zero.

---

## Answers

**Answer 1:**

Write $-8$ in polar form: $-8 = 8e^{i\pi}$ (or $8e^{-i\pi}$; both work since they differ by $2\pi$).

$r^{1/3} = 8^{1/3} = 2$.

$z_k = 2 \cdot \exp\!\left(i\frac{\pi + 2\pi k}{3}\right)$ for $k = 0, 1, 2$.

$k = 0$: $z_0 = 2e^{i\pi/3} = 2\left(\frac{1}{2} + i\frac{\sqrt{3}}{2}\right) = 1 + i\sqrt{3}$.

$k = 1$: $z_1 = 2e^{i\pi} = -2$.

$k = 2$: $z_2 = 2e^{i5\pi/3} = 2\left(\frac{1}{2} - i\frac{\sqrt{3}}{2}\right) = 1 - i\sqrt{3}$.

The three cube roots of $-8$ are $-2$, $1 + i\sqrt{3}$, and $1 - i\sqrt{3}$.

---

**Answer 2:**

$81i = 81e^{i\pi/2}$. $r^{1/4} = 81^{1/4} = 3$.

$z_k = 3 \cdot \exp\!\left(i\frac{\pi/2 + 2\pi k}{4}\right) = 3 \cdot \exp\!\left(i\frac{\pi + 4\pi k}{8}\right)$ for $k = 0, 1, 2, 3$.

The four solutions are: $3e^{i\pi/8}$, $3e^{i5\pi/8}$, $3e^{i9\pi/8}$, $3e^{i13\pi/8}$.

---

**Answer 3:**

Using the quadratic formula: $z = \frac{-1 \pm \sqrt{1 - 4}}{2} = \frac{-1 \pm \sqrt{-3}}{2} = \frac{-1 \pm i\sqrt{3}}{2}$.

These are $-\frac{1}{2} + i\frac{\sqrt{3}}{2}$ and $-\frac{1}{2} - i\frac{\sqrt{3}}{2}$.

The cube roots of unity are $1$, $-\frac{1}{2} + i\frac{\sqrt{3}}{2}$, and $-\frac{1}{2} - i\frac{\sqrt{3}}{2}$. So the two solutions of $z^2 + z + 1 = 0$ are exactly the two non-real cube roots of unity.

---

**Answer 4:**

$32 = 32e^{i \cdot 0}$. $r^{1/5} = 32^{1/5} = 2$.

$z_k = 2 \cdot \exp\!\left(i\frac{2\pi k}{5}\right)$ for $k = 0, 1, 2, 3, 4$.

When $k = 0$: $z_0 = 2$ (a real number).

For $k = 1, 2, 3, 4$, the arguments are $\frac{2\pi}{5}, \frac{4\pi}{5}, \frac{6\pi}{5}, \frac{8\pi}{5}$, none of which are multiples of $\pi$, so none of these are real numbers.

There is exactly one real solution ($z = 2$) and four non-real complex solutions.

---

**Answer 5:**

**(a)** The cube roots of unity are $1$, $\omega$, and $\omega^2$. They are the three solutions of $z^3 = 1$, which can be factored as $(z - 1)(z^2 + z + 1) = 0$. Since $\omega$ and $\omega^2$ are roots of $z^2 + z + 1 = 0$, they satisfy $\omega^2 + \omega + 1 = 0$. Therefore $1 + \omega + \omega^2 = 0$.

**(b)** Using the result from (a): $1 + \omega + \omega^2 = 0$, so $\omega + \omega^2 = -1$.

Then $(1 + \omega)(1 + \omega^2) = 1 + \omega + \omega^2 + \omega^3 = (1 + \omega + \omega^2) + \omega^3$.

Since $1 + \omega + \omega^2 = 0$ and $\omega^3 = 1$, this equals $0 + 1 = 1$.

---

**Answer 6:**

Fifth roots of unity: $z_k = e^{i2\pi k/5}$ for $k = 0, 1, 2, 3, 4$.

Sum $S = 1 + e^{i2\pi/5} + e^{i4\pi/5} + e^{i6\pi/5} + e^{i8\pi/5}$.

This is a geometric series with ratio $e^{i2\pi/5}$:

$S = \frac{1 - (e^{i2\pi/5})^5}{1 - e^{i2\pi/5}} = \frac{1 - e^{i2\pi}}{1 - e^{i2\pi/5}} = \frac{1 - 1}{1 - e^{i2\pi/5}} = 0$.

The sum is zero, as expected.
