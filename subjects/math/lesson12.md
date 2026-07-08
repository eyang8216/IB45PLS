# Lesson 12: Power Series and the Radius of Convergence

## 1. What Is a Power Series?

A power series is a new kind of mathematical object. Instead of adding a finite list of numbers, a power series adds infinitely many terms, and each term contains a variable raised to a power. This means a power series is like a machine: you feed in a value for the variable, and the machine either produces a finite number (it converges) or it blows up (it diverges). Power series are important because they let us represent functions—such as the exponential, sine, and cosine—as infinite polynomials. This representation is the foundation for approximating functions, solving differential equations, and modelling physical systems.

The general form of a power series centered at a number **a** (which we call the **center**) is:

$$\sum_{n=0}^{\infty} c_n (x - a)^n = c_0 + c_1(x-a) + c_2(x-a)^2 + c_3(x-a)^3 + \cdots$$

Each symbol $c_n$ (read "c sub n") is called a **coefficient**. A coefficient is simply a constant number that multiplies the power term $(x-a)^n$. The center $a$ is a fixed number that tells us where the series is "anchored." The variable $x$ is what we plug in. When $a=0$, the series simplifies to $\sum c_n x^n$, which is called a power series centered at the origin.

Many students assume that a power series behaves like a finite polynomial and always gives a number. This is not true. For some values of $x$, the infinite sum may grow without bound and fail to converge. The central question of this lesson is: for which values of $x$ does a given power series converge?

---

## 2. The Interval of Convergence

The set of all $x$ values for which a power series converges is called the **interval of convergence**. To build intuition, consider the simplest power series:

$$\sum_{n=0}^{\infty} x^n = 1 + x + x^2 + x^3 + \cdots$$

This is a geometric series. A geometric series has the form $a + ar + ar^2 + \cdots$ and converges exactly when the common ratio $r$ satisfies $|r| < 1$. Here the common ratio is $x$ itself, so the series converges when $|x| < 1$ and diverges when $|x| \geq 1$. The interval of convergence is therefore $(-1, 1)$.

Not all power series have such a simple interval. Some converge for all $x$, some converge only at the center, and most converge inside some finite radius around the center. The concept that captures this is the **radius of convergence**.

---

## 3. The Radius of Convergence

For any power series $\sum c_n (x-a)^n$, exactly one of three situations occurs:

- **Radius $R = 0$**: The series converges only at $x = a$ and diverges everywhere else. The interval of convergence is just the single point $\{a\}$.
- **Radius $R > 0$ (finite)**: There exists a positive number $R$ such that the series converges for all $x$ with $|x-a| < R$ and diverges for all $x$ with $|x-a| > R$. The behavior at the endpoints $x = a-R$ and $x = a+R$ must be checked separately.
- **Radius $R = \infty$**: The series converges for every real number $x$. The interval of convergence is $(-\infty, \infty)$.

The radius $R$ is the distance from the center $a$ to the edge of the region where convergence is guaranteed. A common misunderstanding is that the endpoints are automatically included if the radius is finite. They are not—each endpoint must be tested individually by plugging it into the original series.

---

## 4. Finding the Radius with the Ratio Test

The Ratio Test (covered in the previous lesson) is the primary tool for finding the radius of convergence. To apply the Ratio Test to a power series $\sum c_n (x-a)^n$, we form the limit:

$$\rho = \lim_{n\to\infty} \left|\frac{c_{n+1}(x-a)^{n+1}}{c_n(x-a)^n}\right|$$

We can factor out $|x-a|$ because it does not depend on $n$:

$$\rho = \lim_{n\to\infty} \left|\frac{c_{n+1}}{c_n}\right| \cdot |x-a|$$

Define $L = \lim_{n\to\infty} \left|\frac{c_{n+1}}{c_n}\right|$ (assuming this limit exists). Then $\rho = L \cdot |x-a|$.

The Ratio Test says the series converges when $\rho < 1$, so we solve:

$$L \cdot |x-a| < 1 \quad \Rightarrow \quad |x-a| < \frac{1}{L}$$

The radius of convergence is therefore:

$$\boxed{R = \frac{1}{L} = \lim_{n\to\infty} \left|\frac{c_n}{c_{n+1}}\right|}$$

If $L = 0$, then $R = \infty$ (the series converges everywhere). If $L = \infty$, then $R = 0$ (the series converges only at the center).

---

## 5. Worked Examples

### Worked Example 1

**Problem:** Find the radius and interval of convergence for $\displaystyle\sum_{n=0}^{\infty} \frac{x^n}{n!}$.

**Approach:** Identify the center and coefficients, then apply the Ratio Test. The factorial in the denominator suggests the series might converge for all $x$, because factorials grow extremely fast and overwhelm any power.

**Step 1:** The center is $a = 0$ and the coefficients are $c_n = \frac{1}{n!}$.

**Step 2:** Apply the Ratio Test:

$$\rho = \lim_{n\to\infty} \left|\frac{x^{n+1}/(n+1)!}{x^n/n!}\right| = \lim_{n\to\infty} \left|\frac{x^{n+1}}{(n+1)!} \cdot \frac{n!}{x^n}\right|$$

Simplify: $\frac{x^{n+1}}{x^n} = |x|$, and $\frac{n!}{(n+1)!} = \frac{1}{n+1}$.

$$\rho = \lim_{n\to\infty} \frac{|x|}{n+1} = |x| \cdot 0 = 0$$

Since $\rho = 0 < 1$ for every real number $x$, the series converges for all $x$.

**Step 3:** The radius of convergence is $R = \infty$. The interval of convergence is $(-\infty, \infty)$.

**Why this makes sense:** The factorial $n!$ grows faster than any exponential $|x|^n$, so the terms shrink to zero rapidly regardless of the size of $x$.

---

### Worked Example 2

**Problem:** Find the radius and interval of convergence for $\displaystyle\sum_{n=1}^{\infty} \frac{x^n}{n}$.

**Approach:** Apply the Ratio Test to find the radius. Because the coefficients are $\frac{1}{n}$, the radius should be finite. Then test both endpoints separately by plugging them into the original series.

**Step 1:** Center $a = 0$, coefficients $c_n = \frac{1}{n}$.

**Step 2:** Apply the Ratio Test:

$$\rho = \lim_{n\to\infty} \left|\frac{x^{n+1}/(n+1)}{x^n/n}\right| = \lim_{n\to\infty} \frac{n}{n+1} \cdot |x| = 1 \cdot |x| = |x|$$

We need $\rho < 1$, so $|x| < 1$. The radius is $R = 1$.

**Step 3:** Test the endpoints.

When $x = 1$: the series becomes $\sum_{n=1}^{\infty} \frac{1}{n}$, which is the harmonic series. The harmonic series diverges because its partial sums grow without bound.

When $x = -1$: the series becomes $\sum_{n=1}^{\infty} \frac{(-1)^n}{n}$, which is the alternating harmonic series. This series converges by the Alternating Series Test, because the terms $\frac{1}{n}$ decrease to zero.

**Step 4:** The interval of convergence is $[-1, 1)$ — the left endpoint is included, the right endpoint is not.

**Why this makes sense:** At $x=1$ we get the harmonic series, famous for diverging despite its terms approaching zero. At $x=-1$, the alternating signs save the series.

---

### Worked Example 3

**Problem:** Find the radius and interval of convergence for $\displaystyle\sum_{n=0}^{\infty} n! \, x^n$.

**Approach:** Here the factorial is in the numerator, not the denominator. This should make the terms grow rapidly, so convergence is unlikely except at the center.

**Step 1:** Center $a = 0$, coefficients $c_n = n!$.

**Step 2:** Apply the Ratio Test:

$$\rho = \lim_{n\to\infty} \left|\frac{(n+1)! \, x^{n+1}}{n! \, x^n}\right| = \lim_{n\to\infty} \frac{(n+1)!}{n!} \cdot |x| = \lim_{n\to\infty} (n+1) \cdot |x|$$

When $x = 0$, every term of the series after the first is zero, so the series converges (its sum is actually $0! \cdot 0^0$, and by convention $0^0 = 1$ here, giving sum $1$).

When $x \neq 0$: the limit is $\infty \cdot |x| = \infty > 1$, so the series diverges.

**Step 3:** The radius of convergence is $R = 0$. The interval of convergence is $\{0\}$.

**Why this makes sense:** The factorial in the numerator makes the terms explode for any nonzero $x$. Only at $x=0$ does the series collapse to a single nonzero term.

---

### Worked Example 4

**Problem:** Find the radius and interval of convergence for $\displaystyle\sum_{n=1}^{\infty} \frac{(x-2)^n}{3^n}$.

**Approach:** Identify the center from the $(x-2)^n$ term — here the center is $a=2$. Apply the Ratio Test with $c_n = \frac{1}{3^n}$.

**Step 1:** The center is $a = 2$, and $c_n = \frac{1}{3^n}$.

**Step 2:** Apply the Ratio Test:

$$\rho = \lim_{n\to\infty} \left|\frac{(x-2)^{n+1}/3^{n+1}}{(x-2)^n/3^n}\right| = \lim_{n\to\infty} \frac{|x-2|}{3} = \frac{|x-2|}{3}$$

We need $\rho < 1$, so $\frac{|x-2|}{3} < 1$, which gives $|x-2| < 3$. The radius is $R = 3$.

**Step 3:** Test the endpoints $x = 2 \pm 3$.

When $x = 5$ (that is, $x-2 = 3$): the series is $\sum \frac{3^n}{3^n} = \sum 1$. This series diverges because each term is $1$, so the partial sums grow without bound.

When $x = -1$ (that is, $x-2 = -3$): the series is $\sum \frac{(-3)^n}{3^n} = \sum (-1)^n$. This series diverges because the terms oscillate between $1$ and $-1$ and never approach zero.

**Step 4:** The interval of convergence is $(-1, 5)$ — an open interval with neither endpoint included.

**Why this makes sense:** The endpoints both produce series that fail the simplest test: the terms do not tend to zero.

---

### Worked Example 5

**Problem:** Find the radius and interval of convergence for $\displaystyle\sum_{n=1}^{\infty} \frac{(x+1)^n}{n^2}$.

**Approach:** Recognize that $x+1 = x - (-1)$, so the center is $a = -1$. The coefficients $\frac{1}{n^2}$ suggest the series might converge at both endpoints because $\sum \frac{1}{n^2}$ converges.

**Step 1:** Center $a = -1$, $c_n = \frac{1}{n^2}$.

**Step 2:** Ratio Test:

$$\rho = \lim_{n\to\infty} \left|\frac{(x+1)^{n+1}/(n+1)^2}{(x+1)^n/n^2}\right| = \lim_{n\to\infty} \frac{n^2}{(n+1)^2} \cdot |x+1| = 1 \cdot |x+1| = |x+1|$$

We need $|x+1| < 1$, so $R = 1$.

**Step 3:** Test endpoints.

When $x+1 = 1$ (so $x = 0$): the series is $\sum \frac{1}{n^2}$, a $p$-series with $p=2 > 1$, which converges.

When $x+1 = -1$ (so $x = -2$): the series is $\sum \frac{(-1)^n}{n^2}$, which converges absolutely because $\sum \frac{1}{n^2}$ converges.

**Step 4:** The interval of convergence is $[-2, 0]$ — a closed interval with both endpoints included.

**Why this makes sense:** The $n^2$ denominator tames the series enough to make it converge even at the endpoints.

---

## 6. Summary of the Method

To find the radius and interval of convergence for a power series $\sum c_n (x-a)^n$:

1. Identify the center $a$ by looking at the expression $(x-a)^n$. If you see $(x+1)^n$, rewrite it as $(x - (-1))^n$ to see that $a = -1$.
2. Apply the Ratio Test to obtain $\rho = \lim \left|\frac{c_{n+1}}{c_n}\right| \cdot |x-a|$.
3. Set $\rho < 1$ and solve for $|x-a| < R$ to find the radius.
4. Check each endpoint separately by plugging that $x$ value into the original series and using any convergence test. The Ratio Test always gives $\rho = 1$ at endpoints, so it cannot decide convergence there.

---

## 7. Three Archetypal Series

These three series provide useful intuition for how factorials affect convergence:

| Series | Radius $R$ | Interval (center 0) | Why |
|---|---|---|---|
| $\sum \dfrac{x^n}{n!}$ | $\infty$ | $(-\infty, \infty)$ | Factorial in denominator overwhelms any $x$ |
| $\sum \dfrac{x^n}{n}$ | $1$ | $[-1, 1)$ | Harmonic-like behavior at endpoints |
| $\sum n! \, x^n$ | $0$ | $\{0\}$ | Factorial in numerator makes terms explode |

---

## Practice Problems

**Problem 1**
Find the radius and interval of convergence for the power series $\displaystyle\sum_{n=1}^{\infty} \frac{x^n}{4^n}$.

**Problem 2**
Find the radius and interval of convergence for the power series $\displaystyle\sum_{n=0}^{\infty} \frac{x^n}{n^2+1}$.

**Problem 3**
Find the radius and interval of convergence for the power series $\displaystyle\sum_{n=0}^{\infty} \frac{(x-3)^n}{n!}$.

**Problem 4**
Find the radius and interval of convergence for the power series $\displaystyle\sum_{n=1}^{\infty} \frac{(x+2)^n}{n \cdot 5^n}$.

**Problem 5 (IB-style)**
Consider the power series $\displaystyle\sum_{n=1}^{\infty} \frac{n}{2^n}(x-1)^n$.

(a) Determine the radius of convergence of the series. [3 marks]

(b) Determine the interval of convergence of the series by testing the behavior at the endpoints. [4 marks]

---

## Answers

**Answer 1**
The series is $\sum \frac{x^n}{4^n} = \sum \left(\frac{x}{4}\right)^n$, a geometric series with common ratio $r = \frac{x}{4}$. A geometric series converges when $|r| < 1$. Applying the Ratio Test directly: $\rho = \lim_{n\to\infty} \left|\frac{x^{n+1}/4^{n+1}}{x^n/4^n}\right| = \frac{|x|}{4}$. Setting $\rho < 1$ gives $|x| < 4$, so the radius is $R = 4$.

Now test the endpoints. At $x = 4$: the series is $\sum 1$, which diverges because the terms do not approach zero. At $x = -4$: the series is $\sum (-1)^n$, which also diverges because the terms oscillate between $1$ and $-1$. Therefore the interval of convergence is $(-4, 4)$.

A common mistake is to forget that geometric series with $|r| = 1$ always diverge because the terms do not tend to zero. The radius alone does not tell you the full interval—you must always check endpoints.

---

**Answer 2**
Apply the Ratio Test with $c_n = \frac{1}{n^2+1}$:

$\rho = \lim_{n\to\infty} \left|\frac{x^{n+1}/((n+1)^2+1)}{x^n/(n^2+1)}\right| = \lim_{n\to\infty} \frac{n^2+1}{(n+1)^2+1} \cdot |x| = 1 \cdot |x| = |x|$.

Setting $\rho < 1$ gives $|x| < 1$, so $R = 1$.

Test $x = 1$: the series is $\sum \frac{1}{n^2+1}$. Compare this to the convergent $p$-series $\sum \frac{1}{n^2}$: for all $n \geq 1$, we have $\frac{1}{n^2+1} < \frac{1}{n^2}$, so by the Comparison Test the series converges at $x = 1$.

Test $x = -1$: the series is $\sum \frac{(-1)^n}{n^2+1}$. This series converges absolutely because $\sum \frac{1}{n^2+1}$ converges, as shown above.

The interval of convergence is $[-1, 1]$, with both endpoints included.

---

**Answer 3**
Apply the Ratio Test with $c_n = \frac{1}{n!}$:

$\rho = \lim_{n\to\infty} \left|\frac{(x-3)^{n+1}/(n+1)!}{(x-3)^n/n!}\right| = \lim_{n\to\infty} \frac{1}{n+1} \cdot |x-3| = 0 \cdot |x-3| = 0$.

Since $\rho = 0 < 1$ for every real number $x$, the series converges for all $x$. The radius of convergence is $R = \infty$, and the interval of convergence is $(-\infty, \infty)$. No endpoint testing is needed because there are no finite endpoints.

---

**Answer 4**
The center is $a = -2$ (since $x+2 = x - (-2)$), and $c_n = \frac{1}{n \cdot 5^n}$.

Apply the Ratio Test:

$\rho = \lim_{n\to\infty} \left|\frac{(x+2)^{n+1}}{(n+1) \cdot 5^{n+1}} \cdot \frac{n \cdot 5^n}{(x+2)^n}\right| = \lim_{n\to\infty} \frac{n}{n+1} \cdot \frac{|x+2|}{5} = \frac{|x+2|}{5}$.

Setting $\rho < 1$ gives $\frac{|x+2|}{5} < 1$, so $|x+2| < 5$. The radius is $R = 5$.

Test the endpoint $x+2 = 5$, which means $x = 3$: the series becomes $\sum \frac{5^n}{n \cdot 5^n} = \sum \frac{1}{n}$, the harmonic series, which diverges.

Test the endpoint $x+2 = -5$, which means $x = -7$: the series becomes $\sum \frac{(-5)^n}{n \cdot 5^n} = \sum \frac{(-1)^n}{n}$, the alternating harmonic series, which converges by the Alternating Series Test.

The interval of convergence is $[-7, 3)$, with the left endpoint included and the right endpoint excluded.

A common pitfall is to misidentify the center. The expression $(x+2)^n$ means the center is $-2$, not $2$. Always rewrite $(x+k)^n$ as $(x - (-k))^n$ to find the center correctly.

---

**Answer 5 (IB-style)**
**(a)** The center is $a = 1$ and $c_n = \frac{n}{2^n}$. Apply the Ratio Test:

$\rho = \lim_{n\to\infty} \left|\frac{(n+1)(x-1)^{n+1}/2^{n+1}}{n(x-1)^n/2^n}\right| = \lim_{n\to\infty} \frac{n+1}{n} \cdot \frac{|x-1|}{2} = 1 \cdot \frac{|x-1|}{2} = \frac{|x-1|}{2}$.

For convergence we require $\rho < 1$, so $\frac{|x-1|}{2} < 1$, giving $|x-1| < 2$. The radius of convergence is $R = 2$. [3 marks]

**(b)** The endpoints are $x = 1 - 2 = -1$ and $x = 1 + 2 = 3$.

At $x = 3$: the series is $\sum \frac{n}{2^n}(3-1)^n = \sum \frac{n \cdot 2^n}{2^n} = \sum n$. The terms $n$ grow without bound, so they do not approach zero. By the $n$th Term Test for Divergence, the series diverges at $x = 3$.

At $x = -1$: the series is $\sum \frac{n}{2^n}(-1-1)^n = \sum \frac{n(-2)^n}{2^n} = \sum n(-1)^n$. The terms are $n(-1)^n$, whose absolute values $n$ grow without bound. Since the terms do not approach zero, the series diverges at $x = -1$ by the $n$th Term Test.

Therefore the interval of convergence is $(-1, 3)$, an open interval with neither endpoint included. [4 marks]
