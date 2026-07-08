# Lesson 11: The Ratio Test and Alternating Series

## What Are These Tests and Why Do They Matter?

In Lesson 10 we learned how to handle series that behave like $p$-series — series involving powers of $n$. But what about series that contain **factorials** like $n!$ (where $n! = 1 \times 2 \times 3 \times \cdots \times n$), or terms like $n^n$, or combinations of exponentials and factorials? The Integral Test and Comparison Tests are not designed for those.

The **Ratio Test** is designed exactly for series with factorials, exponentials, and combinations of them. It works by looking at how each term relates to the one before it — the ratio of consecutive terms.

We also introduce **alternating series** — series whose terms switch signs between positive and negative, like $1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \cdots$. These have their own special test (the Alternating Series Test), and they reveal an important distinction between two types of convergence: absolute and conditional.

---

## Part A: The Ratio Test

### The Core Idea

Imagine you have a series and you want to know whether the sum stays finite. One way to think about it: compare the size of each term to the size of the term right before it. If each term is eventually much smaller than the previous one — say, each term is at most one-tenth of the preceding term — then the terms shrink so fast that the sum must converge.

The Ratio Test makes this precise by computing a single limit, called $\rho$ (the Greek letter "rho"), which is the limiting ratio of consecutive term sizes.

### The Ratio Test: Step by Step

For a series $\sum a_n$, compute:

$$\rho = \lim_{n\to\infty} \left|\frac{a_{n+1}}{a_n}\right|$$

The absolute value bars are important — we only care about the magnitude (size) of the ratio, not its sign.

Then interpret the result:

- If $\rho < 1$, the series **converges** (in fact, it converges absolutely, a term we define later).
- If $\rho > 1$ (or the limit is infinite), the series **diverges**.
- If $\rho = 1$, the Ratio Test gives **no information**. The series could converge or diverge. You must use a different test.

Many students get frustrated when the Ratio Test gives $\rho = 1$. But this is actually a feature, not a bug: when $\rho = 1$, the series behaves like a $p$-series, and the Ratio Test wisely admits it cannot decide — just as the Integral Test or Comparison Tests are needed for $p$-series.

---

### Worked Example 1: Factorial in the Denominator

**Does $\displaystyle\sum_{n=1}^{\infty} \frac{1}{n!}$ converge?**

**Approach:** This series involves a factorial. The factorial $n!$ grows incredibly fast (for example, $5! = 120$, $10! = 3\,628\,800$). The Ratio Test is perfect here.

**Step 1:** Identify $a_n = \frac{1}{n!}$ and $a_{n+1} = \frac{1}{(n+1)!}$.

**Step 2:** Compute the ratio of consecutive terms:

$$\left|\frac{a_{n+1}}{a_n}\right| = \frac{\frac{1}{(n+1)!}}{\frac{1}{n!}} = \frac{n!}{(n+1)!}$$

**Step 3:** Simplify the factorial fraction. Remember that $(n+1)! = (n+1) \times n!$:

$$\frac{n!}{(n+1)!} = \frac{n!}{(n+1) \times n!} = \frac{1}{n+1}$$

**Step 4:** Take the limit as $n \to \infty$:

$$\rho = \lim_{n\to\infty} \frac{1}{n+1} = 0$$

**Step 5:** Since $0 < 1$, the Ratio Test says the series converges.

**Why this makes sense:** The terms $\frac{1}{n!}$ shrink incredibly fast. The first few terms are $1$, $\frac{1}{2} = 0.5$, $\frac{1}{6} \approx 0.167$, $\frac{1}{24} \approx 0.042$, $\frac{1}{120} \approx 0.008$. After just a few terms, the additions are tiny. The sum actually equals $e - 1 \approx 1.718$.

---

### Worked Example 2: Factorial in the Numerator

**Does $\displaystyle\sum_{n=1}^{\infty} \frac{n!}{2^n}$ converge?**

**Approach:** This time the factorial is on top, competing against an exponential $2^n$ on the bottom. Factorials eventually outgrow exponentials. Let's see whether the series converges or diverges.

**Step 1:** $a_n = \frac{n!}{2^n}$, $a_{n+1} = \frac{(n+1)!}{2^{n+1}}$.

**Step 2:** Compute the ratio:

$$\left|\frac{a_{n+1}}{a_n}\right| = \frac{\frac{(n+1)!}{2^{n+1}}}{\frac{n!}{2^n}} = \frac{(n+1)!}{n!} \times \frac{2^n}{2^{n+1}}$$

**Step 3:** Simplify. $\frac{(n+1)!}{n!} = n+1$, and $\frac{2^n}{2^{n+1}} = \frac{1}{2}$:

$$\left|\frac{a_{n+1}}{a_n}\right| = (n+1) \times \frac{1}{2} = \frac{n+1}{2}$$

**Step 4:** Take the limit:

$$\rho = \lim_{n\to\infty} \frac{n+1}{2} = \infty$$

**Step 5:** $\rho = \infty$, which is certainly greater than $1$. The series diverges.

**Why this makes sense:** A factorial in the numerator grows so fast that even dividing by $2^n$ cannot tame it. For $n = 10$, the term is $\frac{10!}{2^{10}} = \frac{3\,628\,800}{1024} \approx 3544$, which is huge. The terms actually get larger and larger, so the sum is doomed.

---

### Worked Example 3: A Balanced Ratio

**Does $\displaystyle\sum_{n=1}^{\infty} \frac{n}{3^n}$ converge?**

**Approach:** Here the numerator grows only linearly ($n$), while the denominator grows exponentially ($3^n$). The exponential should win, so we expect convergence.

**Step 1:** $a_n = \frac{n}{3^n}$, $a_{n+1} = \frac{n+1}{3^{n+1}}$.

**Step 2:** Compute the ratio:

$$\left|\frac{a_{n+1}}{a_n}\right| = \frac{\frac{n+1}{3^{n+1}}}{\frac{n}{3^n}} = \frac{n+1}{3^{n+1}} \times \frac{3^n}{n} = \frac{n+1}{n} \times \frac{3^n}{3^{n+1}}$$

**Step 3:** Simplify. $\frac{3^n}{3^{n+1}} = \frac{1}{3}$, so:

$$\left|\frac{a_{n+1}}{a_n}\right| = \frac{n+1}{n} \times \frac{1}{3}$$

**Step 4:** Take the limit. As $n \to \infty$, $\frac{n+1}{n} \to 1$:

$$\rho = \lim_{n\to\infty} \left(\frac{n+1}{n} \times \frac{1}{3}\right) = 1 \times \frac{1}{3} = \frac{1}{3}$$

**Step 5:** $\frac{1}{3} < 1$, so the series converges.

---

### Worked Example 4: When the Ratio Test Is Inconclusive

**Apply the Ratio Test to $\displaystyle\sum_{n=1}^{\infty} \frac{1}{n^2}$.**

**Approach:** We know from Lesson 10 that this series converges. Let us see what the Ratio Test says — or does not say — about it.

**Step 1:** $a_n = \frac{1}{n^2}$, $a_{n+1} = \frac{1}{(n+1)^2}$.

**Step 2:** Compute the ratio:

$$\left|\frac{a_{n+1}}{a_n}\right| = \frac{\frac{1}{(n+1)^2}}{\frac{1}{n^2}} = \frac{n^2}{(n+1)^2} = \left(\frac{n}{n+1}\right)^2$$

**Step 3:** Take the limit:

$$\rho = \lim_{n\to\infty} \left(\frac{n}{n+1}\right)^2 = 1^2 = 1$$

**Step 4:** $\rho = 1$, so the Ratio Test is inconclusive. It cannot tell us whether the series converges or diverges.

**Important takeaway:** The Ratio Test gives $\rho = 1$ for any $p$-series $\sum \frac{1}{n^p}$. That is why you need the Integral Test or Comparison Tests for $p$-series — the Ratio Test simply cannot handle them.

---

### Worked Example 5: The $n^n$ Term

**Does $\displaystyle\sum_{n=1}^{\infty} \frac{n^n}{n!}$ converge?**

**Approach:** Both the numerator ($n^n$) and the denominator ($n!$) grow extremely fast. The Ratio Test will reveal which one dominates.

**Step 1:** $a_n = \frac{n^n}{n!}$, $a_{n+1} = \frac{(n+1)^{n+1}}{(n+1)!}$.

**Step 2:** Compute the ratio:

$$\frac{a_{n+1}}{a_n} = \frac{(n+1)^{n+1}}{(n+1)!} \times \frac{n!}{n^n}$$

**Step 3:** Simplify the factorials: $\frac{n!}{(n+1)!} = \frac{1}{n+1}$. So:

$$= \frac{(n+1)^{n+1}}{n+1} \times \frac{1}{n^n} = \frac{(n+1)^n}{n^n} = \left(\frac{n+1}{n}\right)^n = \left(1 + \frac{1}{n}\right)^n$$

**Step 4:** This is a famous limit: $\lim_{n\to\infty} \left(1 + \frac{1}{n}\right)^n = e \approx 2.718$.

**Step 5:** $\rho = e > 1$, so the series diverges.

**Why this makes sense:** $n^n$ grows faster than $n!$ (roughly like $e^n$ times faster), so the terms do not shrink to zero fast enough, and the series diverges.

---

## Part B: Alternating Series

### What Is an Alternating Series?

An **alternating series** is a series where the signs of the terms alternate: positive, negative, positive, negative, and so on. The standard way to write an alternating series is:

$$\sum_{n=1}^{\infty} (-1)^{n-1} b_n = b_1 - b_2 + b_3 - b_4 + b_5 - \cdots$$

where each $b_n$ is a positive number. The factor $(-1)^{n-1}$ produces the sign alternation: when $n = 1$, $(-1)^0 = +1$; when $n = 2$, $(-1)^1 = -1$; and so on.

---

### The Alternating Series Test (Leibniz Test)

There is a simple test for alternating series. If the positive parts $b_n$ satisfy two conditions:

1. **The terms decrease in size:** $b_{n+1} \leq b_n$ for all $n$ (eventually). Each term's magnitude is smaller than or equal to the previous one.
2. **The terms approach zero:** $\lim_{n\to\infty} b_n = 0$.

Then the alternating series $\sum (-1)^{n-1} b_n$ converges.

This test is elegant because you do not need to compare to any other series. If the conditions are met, convergence is guaranteed.

---

### Worked Example 6: The Alternating Harmonic Series

**Does $\displaystyle\sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{n} = 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \cdots$ converge?**

**Approach:** Identify $b_n = \frac{1}{n}$ and check the two conditions of the Alternating Series Test.

**Step 1:** Check decreasing. $b_{n+1} = \frac{1}{n+1}$ is indeed less than $b_n = \frac{1}{n}$ for all $n$. Each term is smaller in magnitude than the one before it. ✓

**Step 2:** Check limit. $\lim_{n\to\infty} \frac{1}{n} = 0$. ✓

**Step 3:** Both conditions are satisfied. By the Alternating Series Test, the series converges.

**Why this is remarkable:** The ordinary harmonic series $\sum \frac{1}{n}$ diverges (as we proved in Lesson 10). But simply alternating the signs — making every other term negative — is enough to make the series converge. The alternating signs create a cancellation effect that keeps the sum under control. The sum is actually $\ln 2 \approx 0.693$.

---

### Worked Example 7: When the Alternating Series Test Cannot Help

**Does $\displaystyle\sum_{n=1}^{\infty} (-1)^{n-1} \cdot \frac{n}{n+1}$ converge?**

**Approach:** Identify $b_n = \frac{n}{n+1}$ and check the conditions.

**Step 1:** Check the limit. $\lim_{n\to\infty} \frac{n}{n+1} = 1 \neq 0$. The terms do not approach zero.

**Step 2:** Since the second condition fails immediately, the Alternating Series Test does not apply. But we can go further: because the terms do not approach zero, the $n$-th term test (from Lesson 9) tells us the series actually diverges, regardless of the alternating signs.

---

## Absolute and Conditional Convergence

### Two Kinds of Convergence

When a series $\sum a_n$ converges, we can ask a deeper question: does it converge because the terms themselves are small, or because the cancellation between positive and negative terms saves it?

This leads to two definitions:

- **Absolute convergence:** A series $\sum a_n$ **converges absolutely** if the series of absolute values $\sum |a_n|$ converges. In other words, even if you remove all the sign cancellations and make every term positive, the sum is still finite.

- **Conditional convergence:** A series **converges conditionally** if $\sum a_n$ converges, but $\sum |a_n|$ diverges. The series only converges because of the sign cancellations.

Every absolutely convergent series is automatically convergent (you can prove this rigorously). But the reverse is false: there are series that converge without converging absolutely.

---

### Worked Example 8: Absolute Convergence

**Classify $\displaystyle\sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{n^2}$.**

Take absolute values: $\sum \left|\frac{(-1)^{n-1}}{n^2}\right| = \sum \frac{1}{n^2}$. This is a $p$-series with $p = 2$, which converges.

Since the series of absolute values converges, the original series **converges absolutely**.

---

### Worked Example 9: Conditional Convergence

**Classify $\displaystyle\sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{n}$.**

We already proved (Worked Example 6) that this alternating harmonic series converges by the Alternating Series Test.

Now take absolute values: $\sum \left|\frac{(-1)^{n-1}}{n}\right| = \sum \frac{1}{n}$. This is the harmonic series, which diverges.

Since the series converges but the series of absolute values diverges, $\sum \frac{(-1)^{n-1}}{n}$ **converges conditionally**.

---

## How to Choose the Right Test

| What the series looks like | Test to use |
|---|---|
| Has factorials ($n!$), terms like $n^n$, or exponentials with $n$ in the base ($r^n$) | Ratio Test |
| Has $(-1)^n$ or $(-1)^{n-1}$ with terms that shrink to zero | Alternating Series Test |
| Looks like $\frac{1}{n^p}$ (with or without extra terms in numerator/denominator) | Integral Test or Comparison Tests |
| The Ratio Test gives $\rho = 1$ | Switch to a different test — Integral or Comparison |

---

## Summary

| Test | What You Compute | Conclusion |
|---|---|---|
| **Ratio Test** | $\rho = \lim \left|\frac{a_{n+1}}{a_n}\right|$ | $\rho < 1$: converges; $\rho > 1$: diverges; $\rho = 1$: no conclusion |
| **Alternating Series Test** | Check: $b_n$ decreasing and $b_n \to 0$ | If both true, alternating series converges |
| **Absolute convergence** | Check $\sum \|a_n\|$ | If it converges, the original converges absolutely |
| **Conditional convergence** | $\sum a_n$ converges but $\sum \|a_n\|$ diverges | Series converges conditionally |

---

## Practice Problems

**Problem 1**

Use the Ratio Test to determine whether the series $\displaystyle\sum_{n=1}^{\infty} \frac{2^n}{n!}$ converges or diverges. Show the ratio calculation, the limit, and your conclusion.

**Problem 2**

Use the Ratio Test to determine whether the series $\displaystyle\sum_{n=1}^{\infty} \frac{n!}{n^n}$ converges or diverges. Simplify the ratio carefully — you should end up with a limit involving the mathematical constant $e$.

**Problem 3**

Use the Ratio Test to determine whether the series $\displaystyle\sum_{n=1}^{\infty} \frac{5^n}{n^2}$ converges or diverges. State the limit and interpret it.

**Problem 4**

Use the Alternating Series Test to determine whether $\displaystyle\sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{\sqrt{n}}$ converges or diverges. Check both conditions explicitly.

**Problem 5** (IB-style)

Consider the series $\displaystyle\sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{n^3}$.

(a) Determine whether the series converges or diverges. State the test you used and verify that the conditions of that test are satisfied. [3 marks]

(b) Classify the convergence as absolute or conditional. Justify your answer by considering the series of absolute values. [3 marks]

**Problem 6**

For the series $\displaystyle\sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{\sqrt[3]{n}}$, determine (i) whether the series converges, and (ii) whether the convergence is absolute or conditional. Show all reasoning.

---

## Answers

**Answer 1**

Let $a_n = \frac{2^n}{n!}$. Then $a_{n+1} = \frac{2^{n+1}}{(n+1)!}$.

Compute the ratio:

$$\left|\frac{a_{n+1}}{a_n}\right| = \frac{2^{n+1}}{(n+1)!} \times \frac{n!}{2^n} = \frac{2^{n+1}}{2^n} \times \frac{n!}{(n+1)!} = 2 \times \frac{1}{n+1} = \frac{2}{n+1}$$

Now take the limit:

$$\rho = \lim_{n\to\infty} \frac{2}{n+1} = 0$$

Since $0 < 1$, by the Ratio Test the series converges (absolutely).

---

**Answer 2**

Let $a_n = \frac{n!}{n^n}$. Then $a_{n+1} = \frac{(n+1)!}{(n+1)^{n+1}}$.

Compute the ratio:

$$\left|\frac{a_{n+1}}{a_n}\right| = \frac{(n+1)!}{(n+1)^{n+1}} \times \frac{n^n}{n!} = \frac{n+1}{(n+1)^{n+1}} \times n^n = \frac{n^n}{(n+1)^n} = \left(\frac{n}{n+1}\right)^n$$

Rewrite as:

$$\left(\frac{n}{n+1}\right)^n = \frac{1}{\left(\frac{n+1}{n}\right)^n} = \frac{1}{\left(1 + \frac{1}{n}\right)^n}$$

Now take the limit. The limit of $(1 + \frac{1}{n})^n$ as $n \to \infty$ is $e$:

$$\rho = \lim_{n\to\infty} \frac{1}{(1 + \frac{1}{n})^n} = \frac{1}{e} \approx 0.368$$

Since $\frac{1}{e} < 1$, by the Ratio Test the series converges (absolutely).

---

**Answer 3**

Let $a_n = \frac{5^n}{n^2}$. Then $a_{n+1} = \frac{5^{n+1}}{(n+1)^2}$.

Compute the ratio:

$$\left|\frac{a_{n+1}}{a_n}\right| = \frac{5^{n+1}}{(n+1)^2} \times \frac{n^2}{5^n} = 5 \times \frac{n^2}{(n+1)^2} = 5 \times \left(\frac{n}{n+1}\right)^2$$

Now take the limit:

$$\rho = \lim_{n\to\infty} 5 \times \left(\frac{n}{n+1}\right)^2 = 5 \times 1^2 = 5$$

Since $5 > 1$, by the Ratio Test the series diverges.

(Why: the geometric growth of $5^n$ dominates the quadratic growth of $n^2$ in the denominator. The terms actually grow, so the series cannot converge.)

---

**Answer 4**

We have an alternating series with $b_n = \frac{1}{\sqrt{n}}$.

Condition 1 (decreasing): For any $n$, $\sqrt{n+1} > \sqrt{n}$, so $\frac{1}{\sqrt{n+1}} < \frac{1}{\sqrt{n}}$. The terms decrease in magnitude. ✓

Condition 2 (limit): $\lim_{n\to\infty} \frac{1}{\sqrt{n}} = 0$. ✓

Both conditions are satisfied, so by the Alternating Series Test, the series converges.

However, $\sum |a_n| = \sum \frac{1}{\sqrt{n}} = \sum \frac{1}{n^{1/2}}$ is a $p$-series with $p = \frac{1}{2} \leq 1$, which diverges. So the convergence is conditional, not absolute.

---

**Answer 5**

**(a)** The series is $\sum \frac{(-1)^{n-1}}{n^3}$, an alternating series with $b_n = \frac{1}{n^3}$.

Check the Alternating Series Test conditions:
- Decreasing: $\frac{1}{(n+1)^3} < \frac{1}{n^3}$ for all $n$, since a larger denominator gives a smaller fraction. ✓
- Limit: $\lim_{n\to\infty} \frac{1}{n^3} = 0$. ✓

Both conditions are satisfied, so the series converges by the Alternating Series Test.

[3 marks: 1 for identifying the correct test, 1 for verifying the decreasing condition, 1 for verifying the limit condition and stating the conclusion.]

**(b)** Take absolute values: $\sum \left|\frac{(-1)^{n-1}}{n^3}\right| = \sum \frac{1}{n^3}$. This is a $p$-series with $p = 3$. Since $3 > 1$, this $p$-series converges.

Because the series of absolute values converges, the original series converges **absolutely**.

[3 marks: 1 for writing the series of absolute values, 1 for recognizing it as a convergent $p$-series with $p = 3$, 1 for the correct classification.]

---

**Answer 6**

The series is $\sum \frac{(-1)^{n-1}}{\sqrt[3]{n}} = \sum \frac{(-1)^{n-1}}{n^{1/3}}$.

**(i) Convergence:** This is an alternating series with $b_n = \frac{1}{n^{1/3}}$.

- Decreasing: $n^{1/3}$ increases with $n$, so $\frac{1}{(n+1)^{1/3}} < \frac{1}{n^{1/3}}$. ✓
- Limit: $\lim_{n\to\infty} \frac{1}{n^{1/3}} = 0$. ✓

Both conditions are satisfied. By the Alternating Series Test, the series converges.

**(ii) Classification:** Take absolute values: $\sum \frac{1}{n^{1/3}}$. This is a $p$-series with $p = \frac{1}{3}$. Since $\frac{1}{3} \leq 1$, this $p$-series diverges.

The series converges (by the Alternating Series Test) but the series of absolute values diverges. Therefore the series **converges conditionally**.

(Common pitfall: students sometimes assume that if the Alternating Series Test says a series converges, it must converge absolutely. But absolute convergence requires checking the series of absolute values separately.)
