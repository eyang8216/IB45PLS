# Lesson 14: Error Bounds — Lagrange Remainder and Alternating Series Error

## 1. Why Error Bounds Matter

When we use a Taylor series to approximate a function, we cannot write down infinitely many terms. Instead, we stop after a finite number of terms, producing what is called a **Taylor polynomial**. The Taylor polynomial of degree $n$, denoted $T_n(x)$, is the sum of the first $n+1$ terms of the Taylor series (from the constant term up to the $(x-a)^n$ term).

The relationship between the true function value $f(x)$, the Taylor polynomial $T_n(x)$, and the error is:

$$f(x) = T_n(x) + R_n(x)$$

Here $R_n(x)$ is called the **remainder** or the **error term**. It represents the difference between the true value of the function and the approximation given by the polynomial. Knowing the size of $R_n(x)$ is important for two reasons: it tells us how accurate our approximation is, and it tells us how many terms we need to achieve a desired level of accuracy.

Many students focus only on computing the Taylor polynomial and forget about the error. But in any real application—engineering, physics, finance—knowing the error bound is just as important as knowing the approximation itself. Without an error bound, you cannot guarantee that your approximation is reliable.

---

## 2. The Lagrange Remainder

The **Lagrange remainder** (also called Taylor's Inequality) provides a formula for bounding the error. If a function $f$ can be differentiated $n+1$ times, then for the Taylor polynomial of degree $n$ centered at $a$, the remainder after $n$ terms can be written as:

$$R_n(x) = \frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}$$

for some number $c$ that lies between $a$ and $x$. The exact value of $c$ is unknown—the theorem only guarantees that such a $c$ exists. But we do not need to know $c$ exactly. By finding the maximum possible value of $|f^{(n+1)}(t)|$ for all $t$ between $a$ and $x$, we can obtain an upper bound on the error:

$$|R_n(x)| \leq \frac{M}{(n+1)!}|x-a|^{n+1}$$

where $M$ is the maximum value of $|f^{(n+1)}(t)|$ on the interval between $a$ and $x$. The quantity $M$ is a number we can often estimate without knowing the exact maximum, by using a safe overestimate.

---

### Worked Example 1 — Bounding an Exponential Approximation

**Problem:** Use the third-degree Maclaurin polynomial for $e^x$ to estimate $e^{0.5}$. Then find an upper bound on the error in this estimate.

**Approach:** First write the polynomial, evaluate it at $x = 0.5$, and then use the Lagrange formula. For the error bound, we need the maximum of the fourth derivative of $e^x$ on the interval from $0$ to $0.5$.

**Step 1:** The third-degree Maclaurin polynomial for $e^x$ is:

$$T_3(x) = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!}$$

**Step 2:** Evaluate at $x = 0.5$:

$$T_3(0.5) = 1 + 0.5 + \frac{0.25}{2} + \frac{0.125}{6} = 1 + 0.5 + 0.125 + 0.020833\ldots = 1.645833\ldots$$

**Step 3:** For the error bound, we need $M$, the maximum of $|f^{(4)}(t)|$ on $[0, 0.5]$. Since $f(x) = e^x$, all derivatives are $e^x$. On the interval $[0, 0.5]$, the function $e^t$ is increasing, so its maximum occurs at $t = 0.5$. The value $e^{0.5}$ is what we are trying to estimate, so we do not know it exactly. But we can use a safe overestimate: $e^{0.5} < e^1 < 3$, so we can take $M = 3$ (or even $M = 2$, since $\sqrt{e} \approx 1.65$).

**Step 4:** Apply the Lagrange bound with $n = 3$, $a = 0$, $M = 2$, and $x = 0.5$:

$$|R_3(0.5)| \leq \frac{M}{4!} \cdot |0.5|^4 = \frac{2}{24} \cdot \frac{1}{16} = \frac{2}{384} = \frac{1}{192} \approx 0.00521$$

**Step 5:** Therefore $e^{0.5} = 1.6458 \pm 0.0053$. The true value is approximately $1.648721$, so the actual error is about $0.00289$, which is comfortably within our bound.

**Why this makes sense:** The Lagrange bound is a safe overestimate—it gives a worst-case scenario. The actual error is smaller than the bound, which is exactly what we want for a guarantee.

---

### Worked Example 2 — Determining How Many Terms Are Needed

**Problem:** How many terms of the Maclaurin series for $e^x$ are needed to estimate $e$ (that is, $e^1$) with an error less than $0.001$?

**Approach:** Set up the Lagrange bound inequality and solve for the smallest $n$ that satisfies it.

**Step 1:** For $f(x) = e^x$, all derivatives are $e^x$. We are approximating at $x = 1$, and the center is $a = 0$. On the interval $[0, 1]$, the maximum of $e^t$ is $e^1 = e < 3$. So we can use $M = 3$.

**Step 2:** The Lagrange bound after $n$ terms (degree $n$) is:

$$|R_n(1)| \leq \frac{3}{(n+1)!} \cdot 1^{n+1} = \frac{3}{(n+1)!}$$

**Step 3:** We want this bound to be less than $0.001$:

$$\frac{3}{(n+1)!} < 0.001 \quad \Rightarrow \quad (n+1)! > 3000$$

**Step 4:** Test successive values of $(n+1)!$:

$n=5$: $(6)! = 720$, which is less than $3000$—not enough.

$n=6$: $(7)! = 5040$, which is greater than $3000$—this works.

**Step 5:** We need a polynomial of degree $n = 6$, which contains $7$ terms (for $n = 0$ through $n = 6$).

**Why this makes sense:** The factorial grows very quickly, so the required number of terms jumps from insufficient to sufficient over just one increment of $n$. This rapid growth of the factorial is what makes Taylor approximations so effective.

---

### Worked Example 3 — Lagrange for a Trigonometric Function

**Problem:** Use the third-degree Maclaurin polynomial for $\sin x$ to estimate $\sin(0.2)$, and bound the error.

**Approach:** The third-degree polynomial for sine has only two nonzero terms (since the $x^2$ term is zero). Compute the approximation, then use the Lagrange bound with a safe estimate for the fourth derivative of sine.

**Step 1:** The Maclaurin series for $\sin x$ has zeros at even powers. The third-degree polynomial is:

$$T_3(x) = x - \frac{x^3}{3!} = x - \frac{x^3}{6}$$

**Step 2:** Evaluate at $x = 0.2$:

$$T_3(0.2) = 0.2 - \frac{0.008}{6} = 0.2 - 0.001333\ldots = 0.198667$$

**Step 3:** For the error bound, we need $|f^{(4)}(t)|$. The derivatives of $\sin x$ cycle: the fourth derivative is $\sin x$ again. On the interval $[0, 0.2]$, the maximum of $|\sin t|$ is at $t = 0.2$. We can use a safe bound: $|\sin t| \leq 0.2$ on this interval (since $\sin x \leq x$ for $x \geq 0$). So $M = 0.2$.

**Step 4:** Apply the Lagrange bound:

$$|R_3(0.2)| \leq \frac{0.2}{4!} \cdot (0.2)^4 = \frac{0.2}{24} \cdot 0.0016 = \frac{0.00032}{24} \approx 0.0000133$$

**Step 5:** So $\sin(0.2) \approx 0.198667 \pm 0.000013$. The true value is approximately $0.198669$, giving an actual error of about $0.000002$, well within the bound.

**Why this makes sense:** The error is tiny because $(0.2)^4$ is very small and $4! = 24$ is reasonably large. For small $x$, Taylor polynomials of even modest degree are remarkably accurate.

---

## 3. The Alternating Series Error Bound

For series that alternate in sign and satisfy the conditions of the Alternating Series Test (the absolute values of the terms decrease to zero), there is a much simpler error bound:

$$|R_n| \leq b_{n+1}$$

This says: **the error after $n$ terms is less than or equal to the absolute value of the first omitted term**. In other words, if you stop after the $n$-th term, the error is no larger than the very next term you chose not to include.

This bound is far easier to use than the Lagrange remainder, but it only applies to alternating series that satisfy the decreasing condition. Many students try to use this bound for all series; this is a mistake. The alternating series error bound works only when the terms alternate, decrease in absolute value, and tend to zero.

---

### Worked Example 4 — Alternating Series Error

**Problem:** Use the first four terms of the series for $\ln(1+x)$ at $x = 1$ to estimate $\ln(2)$, and bound the error.

**Approach:** Write out the series at $x = 1$, sum the first four terms, and apply the alternating series error bound.

**Step 1:** The series for $\ln(2)$ is:

$$\ln(2) = 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \frac{1}{5} - \frac{1}{6} + \cdots$$

**Step 2:** The sum of the first four terms is:

$$S_4 = 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} = 1 - 0.5 + 0.33333\ldots - 0.25 = 0.58333\ldots$$

**Step 3:** The first omitted term (the fifth term) is $b_5 = \frac{1}{5} = 0.2$. By the alternating series error bound:

$$|R_4| \leq 0.2$$

**Step 4:** So $\ln(2) \approx 0.583 \pm 0.2$. The true value is $\ln(2) \approx 0.6931$, and the actual error is $0.1098$, which is indeed less than $0.2$.

**Why this makes sense:** This series converges quite slowly. To get the error below $0.001$, you would need the first omitted term $\frac{1}{n+1} < 0.001$, meaning $n > 1000$ terms. This slow convergence is a well-known property of the alternating harmonic series.

---

### Worked Example 5 — Determining Terms with Alternating Series Error

**Problem:** How many terms of the series $\sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{n^2}$ are needed to guarantee an error less than $0.01$?

**Approach:** Identify $b_n = \frac{1}{n^2}$, then set $b_{n+1} < 0.01$ and solve for $n$.

**Step 1:** The series is alternating with terms $b_n = \frac{1}{n^2}$, which decrease to zero. The alternating series error bound applies.

**Step 2:** We need the first omitted term to be less than $0.01$:

$$b_{n+1} = \frac{1}{(n+1)^2} < 0.01$$

**Step 3:** Solve: $(n+1)^2 > 100$, so $n+1 > 10$, giving $n > 9$. The smallest integer satisfying this is $n = 10$.

**Step 4:** Ten terms are sufficient. The first omitted term is $\frac{1}{11^2} = \frac{1}{121} \approx 0.0083$, which is indeed less than $0.01$.

**Why this makes sense:** Because the terms decrease as $\frac{1}{n^2}$, they shrink much faster than the harmonic series $\frac{1}{n}$. Only $10$ terms are needed compared to the $1000+$ terms needed for $\sum \frac{(-1)^{n-1}}{n}$.

---

## 4. Comparing the Two Error Bound Methods

| Feature | Lagrange Remainder | Alternating Series Bound |
|---|---|---|
| When to use | Any Taylor series | Only alternating series satisfying the Alternating Series Test |
| Formula | $\frac{M}{(n+1)!}|x-a|^{n+1}$ | $b_{n+1}$ |
| Difficulty | Requires bounding a derivative | Just look at the next term |
| Tightness | Usually a safe overestimate | Often very tight (close to actual error) |

When both methods apply (because the Taylor series happens to be alternating), the alternating series bound is almost always easier and more precise. Use it whenever you can.

---

## Practice Problems

**Problem 1**
Use the second-degree Maclaurin polynomial for $e^x$ to estimate $\sqrt{e} = e^{0.5}$. Then use the Lagrange remainder to find an upper bound on the error in this estimate. Use $M = 2$ as a safe bound for the third derivative on $[0, 0.5]$.

**Problem 2**
How many terms of the Maclaurin series for $\cos x$ are needed to estimate $\cos(0.5)$ with an error less than $0.0001$? Use the fact that all derivatives of $\cos x$ are bounded in absolute value by $1$ for any $x$, so you may take $M = 1$ in the Lagrange bound.

**Problem 3**
Consider the series $\sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{n^3}$. Use the first three terms to estimate the sum of the infinite series, and bound the error using the alternating series error bound.

**Problem 4**
Use the first three nonzero terms of the Maclaurin series for $\cos x$ to estimate $\cos(0.3)$. Bound the error using the alternating series error bound.

**Problem 5 (IB-style)**
Consider the function $f(x) = \ln x$ and its Taylor polynomial of degree $3$ centered at $a = 1$.

(a) Write down the third-degree Taylor polynomial $T_3(x)$ for $\ln x$ about $x = 1$. [2 marks]

(b) Use $T_3(x)$ to estimate $\ln(1.2)$. [1 mark]

(c) The fourth derivative of $\ln x$ is $f^{(4)}(x) = -\frac{6}{x^4}$. Use the Lagrange remainder to find an upper bound on the error in your estimate from part (b). [3 marks]

(d) Explain why the alternating series error bound could also be used for this estimate, and verify that it gives the same error bound as the Lagrange method. [2 marks]

---

## Answers

**Answer 1**
The second-degree Maclaurin polynomial for $e^x$ is $T_2(x) = 1 + x + \frac{x^2}{2}$.

Evaluate at $x = 0.5$: $T_2(0.5) = 1 + 0.5 + \frac{0.25}{2} = 1 + 0.5 + 0.125 = 1.625$.

For the error bound, the third derivative is $f'''(x) = e^x$. On $[0, 0.5]$, we use $M = 2$ as given. With $n = 2$, $a = 0$, $x = 0.5$:

$$|R_2| \leq \frac{2}{3!} \cdot (0.5)^3 = \frac{2}{6} \cdot 0.125 = \frac{0.25}{6} \approx 0.0417$$

The estimate is $e^{0.5} \approx 1.625 \pm 0.042$. The true value is approximately $1.6487$, so the actual error is $0.0237$, well within the bound.

A common mistake in this type of problem is to forget to divide $M$ by $(n+1)!$. The factorial in the denominator significantly reduces the error bound.

**Answer 2**
The derivatives of $\cos x$ cycle among $\pm\cos x$ and $\pm\sin x$, all of which satisfy $|f^{(k)}(x)| \leq 1$ for every $x$. So $M = 1$ is valid on any interval.

The Lagrange bound after $n$ terms at $x = 0.5$ is:

$$|R_n(0.5)| \leq \frac{1}{(n+1)!} \cdot (0.5)^{n+1}$$

We test values of $n$:
- $n=3$: $\frac{(0.5)^4}{4!} = \frac{0.0625}{24} \approx 0.00260$, which exceeds $0.0001$.
- $n=4$: $\frac{(0.5)^5}{5!} = \frac{0.03125}{120} \approx 0.000260$, still too large.
- $n=5$: $\frac{(0.5)^6}{6!} = \frac{0.015625}{720} \approx 0.0000217$, which is less than $0.0001$.

We need $n = 5$, meaning a polynomial of degree $5$. For $\cos x$, the degree-$5$ polynomial is the same as the degree-$4$ polynomial: $T_5(x) = 1 - \frac{x^2}{2!} + \frac{x^4}{4!}$. This contains three nonzero terms.

The answer is three nonzero terms (degree 4 or 5, which are identical for cosine since odd-degree terms are zero).

**Answer 3**
The series is $\frac{1}{1^3} - \frac{1}{2^3} + \frac{1}{3^3} - \frac{1}{4^3} + \cdots$.

Sum of first three terms: $S_3 = 1 - \frac{1}{8} + \frac{1}{27} = 1 - 0.125 + 0.037037 = 0.912037$.

The first omitted term is the fourth term: $b_4 = \frac{1}{4^3} = \frac{1}{64} = 0.015625$.

By the alternating series error bound: $|R_3| \leq 0.015625$.

The estimate is $0.9120 \pm 0.0156$. This means the true sum of the infinite series lies between $0.8964$ and $0.9277$.

**Answer 4**
The Maclaurin series for $\cos x$ is $\cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \cdots$.

The first three nonzero terms at $x = 0.3$ are:

$T = 1 - \frac{(0.3)^2}{2} + \frac{(0.3)^4}{24} = 1 - \frac{0.09}{2} + \frac{0.0081}{24} = 1 - 0.045 + 0.0003375 = 0.9553375$.

This is an alternating series with terms $b_1 = 1$, $b_2 = \frac{x^2}{2!} = 0.045$, $b_3 = \frac{x^4}{4!} = 0.0003375$, $b_4 = \frac{x^6}{6!}$.

After three terms, the error bound is $|R| \leq b_4 = \frac{(0.3)^6}{720} = \frac{0.000729}{720} \approx 0.00000101$.

The estimate is $\cos(0.3) \approx 0.9553375 \pm 0.0000010$. The true value is approximately $0.9553365$, so the actual error is about $0.0000010$, which matches the bound almost exactly. This shows how tight the alternating series error bound can be.

**Answer 5 (IB-style)**

**(a)** The Taylor series for $\ln x$ centered at $a = 1$ is:

$\ln x = (x-1) - \frac{(x-1)^2}{2} + \frac{(x-1)^3}{3} - \frac{(x-1)^4}{4} + \cdots$

The third-degree Taylor polynomial is the sum of terms up to $(x-1)^3$:

$T_3(x) = (x-1) - \frac{(x-1)^2}{2} + \frac{(x-1)^3}{3}$. [2 marks]

**(b)** At $x = 1.2$, we have $x-1 = 0.2$:

$T_3(1.2) = 0.2 - \frac{0.04}{2} + \frac{0.008}{3} = 0.2 - 0.02 + 0.0026667 = 0.1826667$. [1 mark]

**(c)** The fourth derivative is $f^{(4)}(x) = -\frac{6}{x^4}$, so $|f^{(4)}(x)| = \frac{6}{x^4}$. On the interval $[1, 1.2]$, this function is decreasing, so its maximum occurs at the left endpoint $x = 1$. Thus $M = \frac{6}{1^4} = 6$.

With $n = 3$ and $\Delta x = 0.2$:

$|R_3| \leq \frac{6}{4!} \cdot (0.2)^4 = \frac{6}{24} \cdot 0.0016 = 0.25 \cdot 0.0016 = 0.0004$. [3 marks]

**(d)** The Taylor series for $\ln(1.2) = \ln(1 + 0.2)$ is an alternating series: $0.2 - \frac{0.2^2}{2} + \frac{0.2^3}{3} - \frac{0.2^4}{4} + \cdots$. The terms decrease in absolute value and tend to zero because the powers of $0.2$ shrink faster than the linear growth of the denominator.

After three terms, the alternating series error bound is $|R_3| \leq b_4 = \frac{(0.2)^4}{4} = \frac{0.0016}{4} = 0.0004$.

This matches the Lagrange bound exactly. When both methods apply, they should give consistent results, though the alternating series bound is much faster to compute. [2 marks]
