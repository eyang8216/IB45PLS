# Lesson 10: The Integral Test and Comparison Tests

## What Are Convergence Tests and Why Do They Matter?

In Lesson 9, we learned that a geometric series $\sum ar^{n-1}$ converges exactly when $|r| < 1$, and we have a nice formula for the sum. But what if a series is not geometric? How do we tell whether it converges?

Most series you encounter do not have a simple closed-form sum. Yet it is still important to know whether the series converges at all — because if it diverges, then treating it as if it had a finite sum would produce nonsense. Convergence tests are tools that let you determine convergence or divergence without needing to find the actual sum.

In this lesson we learn two families of tests: the **Integral Test** (which connects series to integrals) and the **Comparison Tests** (which compare a mysterious series to one you already understand).

---

## The Integral Test: Connecting Series to Integrals

### The Big Idea

Suppose the terms of a series come from a function $f(x)$ — in other words, the $n$-th term of the series is $f(n)$. If the function $f(x)$ is **positive** (always above the $x$-axis), **continuous** (no jumps or holes), and **decreasing** (going downward as $x$ increases) for all $x$ beyond some point, then something remarkable happens:

The infinite series $\displaystyle\sum_{n=k}^{\infty} f(n)$ and the improper integral $\displaystyle\int_{k}^{\infty} f(x)\,dx$ share the same fate. They either both converge or both diverge.

To understand why, imagine plotting the function $f(x)$ and drawing rectangles of width $1$ and height $f(n)$ for each integer $n$. The total area of those rectangles approximates the series sum. The area under the curve is the integral. If the integral area is finite, the rectangle areas should also add up to a finite total. If the integral area is infinite, the rectangles overwhelm it too.

**A crucial point:** even when both converge, the series and the integral do NOT give the same numerical value. The Integral Test only tells you whether the series converges — it does not give you the sum.

---

### Formal Statement of the Integral Test

Let $f(x)$ be a function that is continuous, positive, and decreasing on $[k, \infty)$, and let $a_n = f(n)$. Then:

- If $\displaystyle\int_k^{\infty} f(x)\,dx$ converges (equals a finite number), then $\displaystyle\sum_{n=k}^{\infty} a_n$ converges.
- If $\displaystyle\int_k^{\infty} f(x)\,dx$ diverges (is infinite or does not exist), then $\displaystyle\sum_{n=k}^{\infty} a_n$ diverges.

---

### Worked Example 1: The Harmonic Series

**Does the harmonic series $\displaystyle\sum_{n=1}^{\infty} \frac{1}{n}$ converge?**

**Approach:** Define $f(x) = \frac{1}{x}$. We need to verify that $f$ is positive, continuous, and decreasing on $[1, \infty)$, then evaluate the improper integral.

**Step 1:** Check the function. For $x \geq 1$, the function $f(x) = \frac{1}{x}$ is certainly positive (since $x > 0$), continuous (the only problem is at $x = 0$, which is not in our interval), and decreasing (as $x$ gets larger, $\frac{1}{x}$ gets smaller). All conditions are met.

**Step 2:** Set up the improper integral:

$$\int_1^{\infty} \frac{1}{x}\,dx = \lim_{b\to\infty} \int_1^b \frac{1}{x}\,dx$$

**Step 3:** Evaluate the definite integral. The antiderivative of $\frac{1}{x}$ is $\ln x$:

$$\int_1^b \frac{1}{x}\,dx = \bigl[\ln x\bigr]_1^b = \ln b - \ln 1 = \ln b - 0 = \ln b$$

**Step 4:** Take the limit as $b \to \infty$:

$$\lim_{b\to\infty} \ln b = \infty$$

The integral diverges (goes to infinity). Therefore, by the Integral Test, the harmonic series $\sum \frac{1}{n}$ diverges.

**Why this matters:** This result is deeply counterintuitive. The terms $\frac{1}{n}$ do get smaller and smaller, approaching $0$. Many students think that if terms approach zero, the series must converge. The harmonic series is the simplest proof that this is false. The terms shrink, but they shrink too slowly for the sum to stay finite.

---

### Worked Example 2: A Convergent $p$-series

**Does $\displaystyle\sum_{n=1}^{\infty} \frac{1}{n^2}$ converge?**

**Approach:** Define $f(x) = \frac{1}{x^2}$, verify the conditions, and evaluate the improper integral.

**Step 1:** On $[1, \infty)$, $f(x) = x^{-2}$ is positive, continuous, and decreasing. Conditions are met.

**Step 2:** Set up the integral:

$$\int_1^{\infty} \frac{1}{x^2}\,dx = \lim_{b\to\infty} \int_1^b x^{-2}\,dx$$

**Step 3:** The antiderivative of $x^{-2}$ is $-x^{-1} = -\frac{1}{x}$:

$$\int_1^b x^{-2}\,dx = \left[-\frac{1}{x}\right]_1^b = \left(-\frac{1}{b}\right) - \left(-\frac{1}{1}\right) = -\frac{1}{b} + 1$$

**Step 4:** Take the limit:

$$\lim_{b\to\infty} \left(1 - \frac{1}{b}\right) = 1 - 0 = 1$$

The integral converges to $1$. Therefore, by the Integral Test, the series $\sum \frac{1}{n^2}$ converges.

The actual sum of this series is $\frac{\pi^2}{6} \approx 1.645$, not $1$ — this illustrates that the integral test does not give the sum.

---

### Worked Example 3: A Trickier Integral

**Does $\displaystyle\sum_{n=2}^{\infty} \frac{1}{n \ln n}$ converge?**

**Approach:** Define $f(x) = \frac{1}{x \ln x}$, check conditions for $x \geq 2$, and evaluate the integral using substitution.

**Step 1:** For $x \geq 2$, $x$ and $\ln x$ are both positive, so $f(x)$ is positive. The function is continuous on $[2, \infty)$. It is also decreasing (both $x$ and $\ln x$ increase, making the denominator larger). Conditions are met.

**Step 2:** Set up the integral:

$$\int_2^{\infty} \frac{1}{x \ln x}\,dx$$

**Step 3:** Use the substitution $u = \ln x$, so $du = \frac{1}{x}\,dx$. When $x = 2$, $u = \ln 2$. When $x \to \infty$, $u \to \infty$. The integral becomes:

$$\int_{\ln 2}^{\infty} \frac{1}{u}\,du$$

**Step 4:** The antiderivative of $\frac{1}{u}$ is $\ln u$. So:

$$\int_{\ln 2}^{\infty} \frac{1}{u}\,du = \lim_{b\to\infty} \bigl[\ln u\bigr]_{\ln 2}^b = \lim_{b\to\infty} (\ln b - \ln(\ln 2)) = \infty$$

The integral diverges. Therefore the series $\sum \frac{1}{n \ln n}$ diverges — even though its terms shrink to zero even faster than the harmonic series!

---

## The $p$-Series: A Family You Must Know

A **$p$-series** is any series of the form:

$$\sum_{n=1}^{\infty} \frac{1}{n^p} = 1 + \frac{1}{2^p} + \frac{1}{3^p} + \frac{1}{4^p} + \cdots$$

where $p$ is a constant. Using the Integral Test with $f(x) = x^{-p}$, we can determine exactly when a $p$-series converges:

- If $p > 1$, the $p$-series **converges**.
- If $p \leq 1$, the $p$-series **diverges**.

Why? The integral $\int_1^\infty x^{-p}\,dx$ is finite exactly when the exponent $-p$ is less than $-1$, which means $p > 1$.

Here are some examples to build intuition:

| Value of $p$ | Series | Converges? | Why? |
|---|---|---|---|
| $p = 0.5$ | $\sum \frac{1}{\sqrt{n}}$ | Diverges | $0.5 \leq 1$ |
| $p = 1$ | $\sum \frac{1}{n}$ (harmonic) | Diverges | $p = 1$ |
| $p = 1.0001$ | $\sum \frac{1}{n^{1.0001}}$ | Converges | $p > 1$ |
| $p = 2$ | $\sum \frac{1}{n^2}$ | Converges | $2 > 1$ |

Notice something subtle: $\sum \frac{1}{n^{1.0001}}$ converges, even though its terms are almost as large as the harmonic series terms. The line between convergence and divergence at $p = 1$ is extremely sharp. Even the tiniest amount above $1$ is enough to make the series converge.

---

## The Direct Comparison Test (DCT)

### The Idea

Imagine you have two stacks of coins. The stack on the left is shorter than the stack on the right. If the right stack is only $10$ cm tall, the left stack must also be at most $10$ cm. And if the left stack is already taller than you, the right stack must also be taller than you.

The Direct Comparison Test is exactly this idea applied to series. You compare the series you are investigating to another series that you already understand (usually a $p$-series or a geometric series).

### Formal Statement

Suppose $0 \leq a_n \leq b_n$ for all $n$ beyond some starting point.

- If the larger series $\sum b_n$ **converges**, then the smaller series $\sum a_n$ must also **converge**. (If the big pile is finite, the small pile cannot be infinite.)
- If the smaller series $\sum a_n$ **diverges**, then the larger series $\sum b_n$ must also **diverge**. (If the small pile is already infinite, the big pile cannot be finite.)

---

### Worked Example 4: Direct Comparison — Convergence

**Does $\displaystyle\sum_{n=1}^{\infty} \frac{1}{n^2 + 3}$ converge?**

**Approach:** Compare this to a familiar $p$-series. The denominator $n^2 + 3$ is larger than $n^2$, so the fraction $\frac{1}{n^2 + 3}$ is smaller than $\frac{1}{n^2}$.

**Step 1:** Set up the inequality. For every $n \geq 1$, we have $n^2 + 3 > n^2$, and therefore:

$$\frac{1}{n^2 + 3} < \frac{1}{n^2}$$

**Step 2:** The comparison series is $\sum \frac{1}{n^2}$. This is a $p$-series with $p = 2 > 1$, so it converges.

**Step 3:** Since each term of our series is smaller than the corresponding term of a convergent series, our series must also converge. The big pile ($\sum 1/n^2$) is finite, so the smaller pile ($\sum 1/(n^2+3)$) cannot be infinite.

**Answer: The series converges.**

---

### Worked Example 5: Direct Comparison — Divergence

**Does $\displaystyle\sum_{n=2}^{\infty} \frac{1}{\sqrt{n} - 1}$ converge?**

**Approach:** We need to find a comparison. For $n \geq 2$, the denominator $\sqrt{n} - 1$ is smaller than $\sqrt{n}$ (because we are subtracting $1$). When the denominator is smaller, the entire fraction is larger.

**Step 1:** Set up the inequality:

$$\sqrt{n} - 1 < \sqrt{n} \quad \Longrightarrow \quad \frac{1}{\sqrt{n} - 1} > \frac{1}{\sqrt{n}}$$

**Step 2:** The comparison series is $\sum \frac{1}{\sqrt{n}} = \sum \frac{1}{n^{1/2}}$. This is a $p$-series with $p = \frac{1}{2} \leq 1$, so it diverges.

**Step 3:** Since each term of our series is larger than the corresponding term of a divergent series, our series must also diverge. The small pile ($\sum 1/\sqrt{n}$) is already infinite, so the larger pile must be infinite too.

**Answer: The series diverges.**

---

## The Limit Comparison Test (LCT)

### The Idea

Sometimes the Direct Comparison Test is awkward to set up. You might not be sure which way the inequality goes, or the terms might not be clearly smaller or larger than a known series.

The Limit Comparison Test solves this by looking at the **ratio** of the two series' terms in the long run. Instead of asking "is every term smaller?", it asks "what is the proportion between the two series as $n$ gets large?"

### Formal Statement

Let $a_n > 0$ and $b_n > 0$ for all large $n$. Compute the limit:

$$L = \lim_{n\to\infty} \frac{a_n}{b_n}$$

If $L$ is a finite, positive number (meaning $0 < L < \infty$), then the two series $\sum a_n$ and $\sum b_n$ either both converge or both diverge. They behave identically.

This works because if the ratio approaches a nonzero constant, the two series are essentially scalar multiples of each other for large $n$. Multiplying every term of a series by a constant does not change whether it converges.

---

### Worked Example 6: Limit Comparison — Convergence

**Does $\displaystyle\sum_{n=1}^{\infty} \frac{n}{n^3 + 2}$ converge?**

**Approach:** For very large $n$, the highest powers dominate. The numerator is approximately $n$, and the denominator is approximately $n^3$, so the term behaves like $\frac{n}{n^3} = \frac{1}{n^2}$. We will compare to the convergent $p$-series $\sum \frac{1}{n^2}$.

**Step 1:** Set $a_n = \frac{n}{n^3 + 2}$ and choose $b_n = \frac{1}{n^2}$.

**Step 2:** Compute the limit ratio:

$$\lim_{n\to\infty} \frac{a_n}{b_n} = \lim_{n\to\infty} \frac{\frac{n}{n^3 + 2}}{\frac{1}{n^2}} = \lim_{n\to\infty} \frac{n \cdot n^2}{n^3 + 2} = \lim_{n\to\infty} \frac{n^3}{n^3 + 2}$$

**Step 3:** Divide numerator and denominator by $n^3$:

$$\lim_{n\to\infty} \frac{1}{1 + \frac{2}{n^3}} = \frac{1}{1 + 0} = 1$$

**Step 4:** The limit $L = 1$ is finite and positive ($0 < 1 < \infty$). Since $\sum b_n = \sum \frac{1}{n^2}$ converges (a $p$-series with $p = 2$), the Limit Comparison Test tells us that $\sum a_n$ also converges.

**Answer: The series converges.**

---

### Worked Example 7: Limit Comparison — Divergence

**Does $\displaystyle\sum_{n=1}^{\infty} \frac{2n^2 + 1}{\sqrt{n^7 + 4}}$ converge?**

**Approach:** Identify the dominant terms. The numerator's leading term is $2n^2$. The denominator is $\sqrt{n^7 + 4}$, and for large $n$ this behaves like $\sqrt{n^7} = n^{7/2}$. So the term behaves like $\frac{2n^2}{n^{7/2}} = \frac{2}{n^{3/2}}$. We will compare to $\sum \frac{1}{n^{3/2}}$, a $p$-series with $p = 1.5 > 1$, which converges.

**Step 1:** Set $a_n = \frac{2n^2 + 1}{\sqrt{n^7 + 4}}$ and $b_n = \frac{1}{n^{3/2}}$.

**Step 2:** Compute the limit:

$$L = \lim_{n\to\infty} \frac{\frac{2n^2 + 1}{\sqrt{n^7 + 4}}}{\frac{1}{n^{3/2}}} = \lim_{n\to\infty} \frac{(2n^2 + 1) \cdot n^{3/2}}{\sqrt{n^7 + 4}}$$

**Step 3:** In the numerator, $n^{3/2} \cdot n^2 = n^{7/2}$. So:

$$L = \lim_{n\to\infty} \frac{2n^{7/2} + n^{3/2}}{\sqrt{n^7 + 4}}$$

Factor out $n^{7/2}$ from the numerator and $n^{7/2}$ from the denominator (since $\sqrt{n^7} = n^{7/2}$):

$$L = \lim_{n\to\infty} \frac{n^{7/2}(2 + n^{-2})}{n^{7/2}\sqrt{1 + \frac{4}{n^7}}} = \lim_{n\to\infty} \frac{2 + n^{-2}}{\sqrt{1 + \frac{4}{n^7}}} = \frac{2 + 0}{\sqrt{1 + 0}} = 2$$

**Step 4:** $L = 2$ is finite and positive. Since $\sum b_n = \sum \frac{1}{n^{3/2}}$ converges ($p = 1.5 > 1$), the series $\sum a_n$ also converges.

**Answer: The series converges.**

---

## Summary Table

| Series | Test Used | Reasoning | Result |
|---|---|---|---|
| $\sum \frac{1}{n}$ | Integral Test | $\int \frac{dx}{x}$ diverges | Diverges |
| $\sum \frac{1}{n^2}$ | Integral Test | $\int \frac{dx}{x^2}$ converges | Converges |
| $\sum \frac{1}{n^p}$ | Integral → $p$-series rule | Converges exactly when $p > 1$ | — |
| $\sum \frac{1}{n^2 + 3}$ | Direct Comparison | Smaller than $\sum 1/n^2$ | Converges |
| $\sum \frac{n}{n^3 + 2}$ | Limit Comparison | Ratio limit to $1/n^2$ is $1$ | Converges |

---

## Practice Problems

**Problem 1**

Use the Integral Test to determine whether the series $\displaystyle\sum_{n=1}^{\infty} \frac{1}{n^3}$ converges or diverges. You should verify that the function meets the conditions of the test, set up the improper integral, evaluate it, and state your conclusion.

**Problem 2**

Use the Integral Test to determine whether the series $\displaystyle\sum_{n=2}^{\infty} \frac{1}{n(\ln n)^2}$ converges or diverges. You will need to use the substitution $u = \ln x$ when evaluating the integral.

**Problem 3**

Use the Direct Comparison Test to determine whether $\displaystyle\sum_{n=1}^{\infty} \frac{\sin^2 n}{n^2}$ converges or diverges. (Hint: what is the maximum possible value of $\sin^2 n$?)

**Problem 4**

Use the Direct Comparison Test to determine whether $\displaystyle\sum_{n=1}^{\infty} \frac{1}{n + \sqrt{n}}$ converges or diverges. Set up a clear inequality and state which known series you are comparing to.

**Problem 5** (IB-style)

Consider the series $\displaystyle\sum_{n=1}^{\infty} \frac{n+1}{n^3 + n}$.

(a) By considering the behaviour of the general term for large $n$, suggest a suitable $p$-series to compare with. [2 marks]

(b) Use the Limit Comparison Test to determine whether the series converges or diverges, showing clearly the limit calculation. [4 marks]

**Problem 6**

Use the Limit Comparison Test to determine whether $\displaystyle\sum_{n=1}^{\infty} \frac{3n^2 - 2}{n^4 + 5n}$ converges or diverges. State your choice of comparison series, compute the limit, and interpret the result.

---

## Answers

**Answer 1**

We define $f(x) = \frac{1}{x^3}$ for $x \geq 1$. The function is positive (since $x^3 > 0$), continuous (no breaks in the domain), and decreasing (as $x$ grows, $x^3$ grows, making the fraction smaller). All Integral Test conditions are satisfied.

Now set up the improper integral:

$$\int_1^{\infty} \frac{1}{x^3}\,dx = \lim_{b\to\infty} \int_1^b x^{-3}\,dx$$

The antiderivative of $x^{-3}$ is $\frac{x^{-2}}{-2} = -\frac{1}{2x^2}$:

$$\int_1^b x^{-3}\,dx = \left[-\frac{1}{2x^2}\right]_1^b = \left(-\frac{1}{2b^2}\right) - \left(-\frac{1}{2}\right) = \frac{1}{2} - \frac{1}{2b^2}$$

Take the limit: $\lim_{b\to\infty} \left(\frac{1}{2} - \frac{1}{2b^2}\right) = \frac{1}{2} - 0 = \frac{1}{2}$.

The integral converges to $\frac{1}{2}$. Therefore, by the Integral Test, the series $\sum \frac{1}{n^3}$ converges. (This is also a $p$-series with $p = 3 > 1$, which confirms the result.)

---

**Answer 2**

Define $f(x) = \frac{1}{x(\ln x)^2}$ for $x \geq 2$. The function is positive (all factors are positive), continuous on $[2, \infty)$, and decreasing (as $x$ grows, both $x$ and $(\ln x)^2$ grow). The conditions are met.

Set up the integral and use the substitution $u = \ln x$, so $du = \frac{1}{x}dx$. When $x = 2$, $u = \ln 2$. As $x \to \infty$, $u \to \infty$. The integral becomes:

$$\int_2^{\infty} \frac{1}{x(\ln x)^2}\,dx = \int_{\ln 2}^{\infty} \frac{1}{u^2}\,du$$

Now evaluate: $\int \frac{1}{u^2}\,du = -\frac{1}{u}$. So:

$$\int_{\ln 2}^{\infty} \frac{1}{u^2}\,du = \lim_{b\to\infty} \left[-\frac{1}{u}\right]_{\ln 2}^b = \lim_{b\to\infty} \left(-\frac{1}{b} + \frac{1}{\ln 2}\right) = 0 + \frac{1}{\ln 2} = \frac{1}{\ln 2}$$

The integral converges to $\frac{1}{\ln 2}$. By the Integral Test, the series converges.

---

**Answer 3**

The key observation is that $\sin^2 n$ is always between $0$ and $1$ inclusive, for any value of $n$. Therefore:

$$0 \leq \frac{\sin^2 n}{n^2} \leq \frac{1}{n^2}$$

We compare to $\sum \frac{1}{n^2}$, which is a $p$-series with $p = 2 > 1$, so it converges.

Since each term of our series is less than or equal to the corresponding term of a convergent series, the Direct Comparison Test tells us that $\sum \frac{\sin^2 n}{n^2}$ also converges.

(Common pitfall: $\sin^2 n$ oscillates and does not have a limit, but that does not matter. The DCT only requires the inequality, not that the terms have a nice limit.)

---

**Answer 4**

We need to compare $\frac{1}{n + \sqrt{n}}$ to a known series. Notice that $n + \sqrt{n} < n + n = 2n$ for all $n \geq 1$ (since $\sqrt{n} < n$ for $n > 1$, and for $n = 1$ the inequality still holds: $1 + 1 = 2 = 2 \times 1$).

Because the denominator is smaller than $2n$, the fraction is larger than $\frac{1}{2n}$:

$$\frac{1}{n + \sqrt{n}} > \frac{1}{2n}$$

Now $\sum \frac{1}{2n} = \frac{1}{2} \sum \frac{1}{n}$ is half of the harmonic series. The harmonic series diverges, and multiplying by $\frac{1}{2}$ does not change that — it still diverges.

Since each term of our series is larger than the corresponding term of this divergent series, the Direct Comparison Test tells us that $\sum \frac{1}{n + \sqrt{n}}$ diverges.

(Alternative approach: use the Limit Comparison Test with $b_n = \frac{1}{n}$. The limit would be $1$, and since $\sum 1/n$ diverges, our series also diverges.)

---

**Answer 5**

**(a)** For very large $n$, the highest powers dominate. The numerator $n+1$ behaves like $n$, and the denominator $n^3 + n$ behaves like $n^3$. So the general term behaves like $\frac{n}{n^3} = \frac{1}{n^2}$. A suitable $p$-series to compare with is $\sum \frac{1}{n^2}$, which is a $p$-series with $p = 2 > 1$ and therefore converges.

[2 marks: 1 for identifying the dominant behaviour, 1 for choosing the correct $p$-series.]

**(b)** Let $a_n = \frac{n+1}{n^3 + n}$ and $b_n = \frac{1}{n^2}$. Compute the limit:

$$L = \lim_{n\to\infty} \frac{a_n}{b_n} = \lim_{n\to\infty} \frac{\frac{n+1}{n^3 + n}}{\frac{1}{n^2}} = \lim_{n\to\infty} \frac{(n+1)n^2}{n^3 + n} = \lim_{n\to\infty} \frac{n^3 + n^2}{n^3 + n}$$

Divide numerator and denominator by $n^3$:

$$L = \lim_{n\to\infty} \frac{1 + \frac{1}{n}}{1 + \frac{1}{n^2}} = \frac{1 + 0}{1 + 0} = 1$$

The limit $L = 1$ is finite and positive ($0 < 1 < \infty$). Since $\sum \frac{1}{n^2}$ converges, the Limit Comparison Test tells us that $\sum \frac{n+1}{n^3 + n}$ also converges.

[4 marks: 1 for writing the limit, 1 for correct algebra simplification, 1 for evaluating the limit, 1 for correct conclusion.]

---

**Answer 6**

Let $a_n = \frac{3n^2 - 2}{n^4 + 5n}$. For large $n$, the dominant terms are $3n^2$ in the numerator and $n^4$ in the denominator, so $a_n$ behaves like $\frac{3n^2}{n^4} = \frac{3}{n^2}$. We choose $b_n = \frac{1}{n^2}$ as our comparison series. This is a $p$-series with $p = 2$, which converges.

Now compute the limit:

$$L = \lim_{n\to\infty} \frac{a_n}{b_n} = \lim_{n\to\infty} \frac{\frac{3n^2 - 2}{n^4 + 5n}}{\frac{1}{n^2}} = \lim_{n\to\infty} \frac{(3n^2 - 2) \cdot n^2}{n^4 + 5n} = \lim_{n\to\infty} \frac{3n^4 - 2n^2}{n^4 + 5n}$$

Divide numerator and denominator by $n^4$:

$$L = \lim_{n\to\infty} \frac{3 - \frac{2}{n^2}}{1 + \frac{5}{n^3}} = \frac{3 - 0}{1 + 0} = 3$$

The limit $L = 3$ is finite and positive ($0 < 3 < \infty$). Since $\sum \frac{1}{n^2}$ converges, the Limit Comparison Test tells us that $\sum \frac{3n^2 - 2}{n^4 + 5n}$ also converges.
