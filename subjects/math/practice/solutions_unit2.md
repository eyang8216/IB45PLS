# Unit 2: Sequences & Series — Solutions

## Problem 1
**Approach:** Evaluate the limit of the sequence by dividing numerator and denominator by the highest power of \(n\).

\[
a_n = \frac{2n^2 + 3n}{n^2 - n + 1}
\]

Divide numerator and denominator by \(n^2\):

\[
a_n = \frac{2 + \frac{3}{n}}{1 - \frac{1}{n} + \frac{1}{n^2}}
\]

As \(n \to \infty\), the terms \(\frac{3}{n}\), \(\frac{1}{n}\), and \(\frac{1}{n^2}\) all approach 0:

\[
\lim_{n\to\infty} a_n = \frac{2 + 0}{1 - 0 + 0} = 2
\]

**Answer:** The sequence converges to 2.

*Pitfall: Students sometimes forget to divide every term by the same power. Make sure the division in the denominator is applied to each term individually.*

---

## Problem 2
**Approach:** Examine the behavior of the magnitude and the sign separately.

\[
b_n = \frac{(-1)^n \cdot n}{n+1}
\]

First, consider the magnitude:

\[
|b_n| = \frac{n}{n+1} = \frac{1}{1 + \frac{1}{n}} \to 1 \quad \text{as } n \to \infty
\]

The magnitude approaches 1, not 0. Moreover, the factor \((-1)^n\) causes the sign to alternate. Since the magnitude does not approach 0, the sequence oscillates between values approaching \(+1\) (for even \(n\)) and \(-1\) (for odd \(n\)).

**Answer:** The sequence diverges (it does not approach a unique limit; it oscillates).

*Pitfall: A common mistake is to think that because \(|b_n| \to 1\), the sequence converges to 1. The alternating sign prevents convergence.*

---

## Problem 3
**Approach:** Identify the first term and common ratio, then apply the infinite geometric series formula.

Given: \(12 + 6 + 3 + \frac{3}{2} + \cdots\)

First term: \(a = 12\)

Common ratio: \(r = \dfrac{6}{12} = \dfrac{3}{6} = \dfrac{1.5}{3} = \dfrac{1}{2}\). Since \(|r| = \frac{1}{2} < 1\), the series converges.

Sum formula for an infinite geometric series:

\[
S = \frac{a}{1 - r} = \frac{12}{1 - \frac{1}{2}} = \frac{12}{\frac{1}{2}} = 24
\]

**Answer:** Common ratio \(r = \frac{1}{2}\); the series converges to 24.

*Pitfall: Using the finite sum formula \(S_n = \frac{a(1-r^n)}{1-r}\) instead of the infinite sum formula \(S = \frac{a}{1-r}\).*

---

## Problem 4
**Approach:** Express the repeating decimal as an infinite geometric series and sum it.

\[
0.\overline{72} = 0.727272\ldots = \frac{72}{100} + \frac{72}{10000} + \frac{72}{1000000} + \cdots
\]

This is a geometric series with:

\[
a = \frac{72}{100} = \frac{18}{25}, \quad r = \frac{1}{100}
\]

Since \(|r| < 1\), the sum is:

\[
S = \frac{a}{1 - r} = \frac{\frac{72}{100}}{1 - \frac{1}{100}} = \frac{\frac{72}{100}}{\frac{99}{100}} = \frac{72}{99}
\]

Simplify by dividing numerator and denominator by 9:

\[
\frac{72}{99} = \frac{8}{11}
\]

**Answer:** \(0.\overline{72} = \dfrac{8}{11}\)

*Pitfall: Setting the common ratio as \(1/10\) instead of \(1/100\) because the repeating block is two digits. For a two-digit repeating block, the denominator is 99, not 9.*

---

## Problem 5
**Approach:** Rewrite the series in standard geometric form and evaluate.

\[
\sum_{n=1}^{\infty} \frac{3}{4^n} = 3 \sum_{n=1}^{\infty} \left(\frac{1}{4}\right)^n
\]

(a) This is a geometric series. Write out the first few terms:

\[
\frac{3}{4} + \frac{3}{16} + \frac{3}{64} + \cdots
\]

First term: \(a = \frac{3}{4}\). Common ratio: \(r = \frac{1}{4}\).

(b) Since \(|r| = \frac{1}{4} < 1\), the series converges. The sum is:

\[
S = \frac{a}{1 - r} = \frac{\frac{3}{4}}{1 - \frac{1}{4}} = \frac{\frac{3}{4}}{\frac{3}{4}} = 1
\]

**Answer:** (a) First term \(a = \frac{3}{4}\), common ratio \(r = \frac{1}{4}\). (b) The series converges absolutely to 1.

*Pitfall: Forgetting that the index starts at \(n=1\), so the first term is \(3/4^1 = 3/4\), not 3.*

---

## Problem 6
**Approach:** Recall the p-series test and apply it.

The p-series \(\sum_{n=1}^{\infty} \frac{1}{n^p}\) converges if and only if \(p > 1\). It diverges if \(p \leq 1\).

For \(\sum_{n=1}^{\infty} \frac{1}{n^{1.5}}\), we have \(p = 1.5\). Since \(1.5 > 1\), the series converges.

**Answer:** The p-series converges for \(p > 1\). The series \(\sum_{n=1}^{\infty} \frac{1}{n^{1.5}}\) converges.

*Pitfall: Confusing "\(p > 1\)" with "\(p \geq 1\)". The harmonic series (\(p = 1\)) diverges, so the threshold is strictly greater than 1.*

---

## Problem 7
**Approach:** Apply the Integral Test. The function \(f(x) = \frac{1}{x^2+1}\) is positive, continuous, and decreasing for \(x \geq 1\).

\[
\int_1^{\infty} \frac{1}{x^2+1} \, dx = \lim_{b\to\infty} \int_1^b \frac{1}{x^2+1} \, dx = \lim_{b\to\infty} \left[\arctan x\right]_1^b
\]

\[
= \lim_{b\to\infty} (\arctan b - \arctan 1) = \frac{\pi}{2} - \frac{\pi}{4} = \frac{\pi}{4}
\]

The improper integral converges to a finite value (\(\pi/4\)). By the Integral Test, the series converges.

**Answer:** The series converges.

*Pitfall: Forgetting to verify that \(f(x)\) is positive, continuous, and decreasing on \([1,\infty)\) before applying the Integral Test.*

---

## Problem 8
**Approach:** Use the Comparison Test with a known convergent series.

For all \(n \geq 1\):

\[
n^2 + 3n \geq n^2 \quad \Longrightarrow \quad \frac{1}{n^2 + 3n} \leq \frac{1}{n^2}
\]

The series \(\sum_{n=1}^{\infty} \frac{1}{n^2}\) is a p-series with \(p = 2 > 1\), so it converges. Since each term of our series is less than or equal to the corresponding term of a convergent series of positive terms, by the Direct Comparison Test, \(\sum_{n=1}^{\infty} \frac{1}{n^2 + 3n}\) converges.

**Answer:** The series converges.

*Pitfall: Choosing a comparison series that diverges, which gives no information. The comparison must be with a series that dominates the terms and converges, or is dominated by the terms and diverges.*

---

## Problem 9
**Approach:** Use the Limit Comparison Test with the harmonic series.

Let \(a_n = \frac{n}{n^2 + 1}\). For large \(n\), \(a_n \approx \frac{n}{n^2} = \frac{1}{n}\). Compare with \(b_n = \frac{1}{n}\):

\[
\lim_{n\to\infty} \frac{a_n}{b_n} = \lim_{n\to\infty} \frac{\frac{n}{n^2+1}}{\frac{1}{n}} = \lim_{n\to\infty} \frac{n^2}{n^2+1} = \lim_{n\to\infty} \frac{1}{1 + \frac{1}{n^2}} = 1
\]

The limit is \(1\), which is finite and positive (\(0 < 1 < \infty\)). Since \(\sum \frac{1}{n}\) (the harmonic series) diverges, by the Limit Comparison Test, \(\sum \frac{n}{n^2+1}\) also diverges.

**Answer:** The series diverges.

*Pitfall: Using the wrong comparison series. The dominant behavior comes from comparing degrees: numerator degree 1, denominator degree 2, so the terms behave like \(1/n\), which diverges.*

---

## Problem 10
**Approach:** Apply the Ratio Test.

Let \(a_n = \frac{3^n}{n!}\).

\[
\lim_{n\to\infty} \left| \frac{a_{n+1}}{a_n} \right| = \lim_{n\to\infty} \frac{3^{n+1} / (n+1)!}{3^n / n!} = \lim_{n\to\infty} \frac{3^{n+1}}{3^n} \cdot \frac{n!}{(n+1)!} = \lim_{n\to\infty} 3 \cdot \frac{1}{n+1} = \lim_{n\to\infty} \frac{3}{n+1} = 0
\]

Since \(0 < 1\), the series converges absolutely by the Ratio Test.

**Answer:** The series converges.

*Pitfall: Mishandling the factorial simplification. Remember: \((n+1)! = (n+1) \cdot n!\), so the ratio of factorials is \(\frac{1}{n+1}\).*

---

## Problem 11
**Approach:** Apply the Ratio Test.

Let \(a_n = \frac{n^2}{2^n}\).

\[
\lim_{n\to\infty} \left| \frac{a_{n+1}}{a_n} \right| = \lim_{n\to\infty} \frac{(n+1)^2 / 2^{n+1}}{n^2 / 2^n} = \lim_{n\to\infty} \frac{(n+1)^2}{n^2} \cdot \frac{2^n}{2^{n+1}} = \lim_{n\to\infty} \left(\frac{n+1}{n}\right)^2 \cdot \frac{1}{2}
\]

\[
= \lim_{n\to\infty} \left(1 + \frac{1}{n}\right)^2 \cdot \frac{1}{2} = 1^2 \cdot \frac{1}{2} = \frac{1}{2}
\]

Since \(\frac{1}{2} < 1\), the series converges absolutely by the Ratio Test.

**Answer:** The series converges.

*Pitfall: Forgetting to square the \((n+1)/n\) term. As \(n \to \infty\), \((1 + 1/n)^2 \to 1\), but you must track both the square and the factor of \(1/2\).*

---

## Problem 12
**Approach:** Apply the Alternating Series Test, then check for absolute convergence.

The series is \(\sum_{n=1}^{\infty} \frac{(-1)^n}{n}\). Let \(b_n = \frac{1}{n}\).

Check the Alternating Series Test conditions:
1. \(b_n > 0\) for all \(n\).
2. \(\lim_{n\to\infty} b_n = \lim_{n\to\infty} \frac{1}{n} = 0\).
3. \(b_{n+1} = \frac{1}{n+1} < \frac{1}{n} = b_n\), so the sequence is decreasing.

All three conditions are satisfied, so the alternating series converges.

Now test for absolute convergence: \(\sum_{n=1}^{\infty} \left|\frac{(-1)^n}{n}\right| = \sum_{n=1}^{\infty} \frac{1}{n}\) is the harmonic series, which diverges (\(p=1\)).

Therefore, the series converges conditionally (but not absolutely).

**Answer:** The series converges conditionally.

*Pitfall: Assuming that convergence of the alternating series implies absolute convergence. Always check the series of absolute values separately.*

---

## Problem 13
**Approach:** Apply the Alternating Series Test, then test absolute convergence.

The series is \(\sum_{n=1}^{\infty} \frac{(-1)^n}{\sqrt{n}}\). Let \(b_n = \frac{1}{\sqrt{n}}\).

Alternating Series Test:
1. \(b_n > 0\) for all \(n\).
2. \(\lim_{n\to\infty} b_n = 0\).
3. \(b_{n+1} = \frac{1}{\sqrt{n+1}} < \frac{1}{\sqrt{n}} = b_n\), so decreasing.

The series converges by the Alternating Series Test.

Now check absolute convergence: \(\sum_{n=1}^{\infty} \frac{1}{\sqrt{n}} = \sum_{n=1}^{\infty} \frac{1}{n^{1/2}}\) is a p-series with \(p = \frac{1}{2} < 1\), which diverges.

Since the series converges but does not converge absolutely, it converges conditionally.

**Answer:** The series converges conditionally.

*Pitfall: Forgetting to verify the decreasing condition of the AST. Here \(1/\sqrt{n}\) is clearly decreasing, but always check explicitly.*

---

## Problem 14
**Approach:** Apply the Ratio Test to the power series to find the radius of convergence.

\[
\sum_{n=0}^{\infty} \frac{x^n}{2^n} = \sum_{n=0}^{\infty} \left(\frac{x}{2}\right)^n
\]

Using the Ratio Test:

\[
\lim_{n\to\infty} \left| \frac{a_{n+1}}{a_n} \right| = \lim_{n\to\infty} \left| \frac{(x/2)^{n+1}}{(x/2)^n} \right| = \lim_{n\to\infty} \left| \frac{x}{2} \right| = \left| \frac{x}{2} \right|
\]

For convergence, we need \(\left|\frac{x}{2}\right| < 1\), i.e., \(|x| < 2\).

**Answer:** The radius of convergence is \(R = 2\).

*Pitfall: Confusing radius of convergence with interval of convergence. The radius is always half the length of the interval of convergence (when the center is at 0).*

---

## Problem 15
**Approach:** Use the Ratio Test to find the radius, then test endpoints for the interval.

\[
\sum_{n=1}^{\infty} \frac{(x-3)^n}{n \cdot 2^n}
\]

Apply the Ratio Test with \(a_n = \frac{(x-3)^n}{n \cdot 2^n}\):

\[
\lim_{n\to\infty} \left| \frac{a_{n+1}}{a_n} \right| = \lim_{n\to\infty} \left| \frac{(x-3)^{n+1}}{(n+1) \cdot 2^{n+1}} \cdot \frac{n \cdot 2^n}{(x-3)^n} \right| = \lim_{n\to\infty} \frac{|x-3|}{2} \cdot \frac{n}{n+1}
\]

\[
= \frac{|x-3|}{2} \cdot \lim_{n\to\infty} \frac{n}{n+1} = \frac{|x-3|}{2} \cdot 1 = \frac{|x-3|}{2}
\]

For convergence, we need \(\frac{|x-3|}{2} < 1\), i.e., \(|x-3| < 2\). Radius of convergence: \(R = 2\).

The interval without endpoints: \(-2 < x-3 < 2 \Rightarrow 1 < x < 5\).

**Check endpoints:**

At \(x = 1\): \(x-3 = -2\), so the series becomes \(\sum_{n=1}^{\infty} \frac{(-2)^n}{n \cdot 2^n} = \sum_{n=1}^{\infty} \frac{(-1)^n}{n}\). This is the alternating harmonic series, which converges conditionally (see Problem 12). So \(x = 1\) is included.

At \(x = 5\): \(x-3 = 2\), so the series becomes \(\sum_{n=1}^{\infty} \frac{2^n}{n \cdot 2^n} = \sum_{n=1}^{\infty} \frac{1}{n}\). This is the harmonic series, which diverges. So \(x = 5\) is excluded.

**Answer:** Radius of convergence \(R = 2\). Interval of convergence: \([1, 5)\).

*Pitfall: Forgetting to test endpoints. The Ratio Test is inconclusive at the endpoints (\(|x-3|/2 = 1\)), so you must substitute and use other convergence tests.*

---

## Problem 16
**Approach:** Recognize \(f(x) = \frac{1}{1+x}\) as a geometric series with ratio \(-x\).

\[
f(x) = \frac{1}{1+x} = \frac{1}{1 - (-x)} = \sum_{n=0}^{\infty} (-x)^n = \sum_{n=0}^{\infty} (-1)^n x^n
\]

Expanding up to the \(x^4\) term:

\[
n = 0: (-1)^0 x^0 = 1
\]
\[
n = 1: (-1)^1 x^1 = -x
\]
\[
n = 2: (-1)^2 x^2 = x^2
\]
\[
n = 3: (-1)^3 x^3 = -x^3
\]
\[
n = 4: (-1)^4 x^4 = x^4
\]

**Answer:** \(1 - x + x^2 - x^3 + x^4 + \cdots\)

*Pitfall: Confusing \(\frac{1}{1+x}\) with \(\frac{1}{1-x}\). The former has alternating signs; the latter has all positive signs.*

---

## Problem 17
**Approach:** Compute derivatives of \(f(x) = \sin x\) at \(x = 0\) and construct the Maclaurin series.

\[
\begin{aligned}
f(x) &= \sin x, & f(0) &= 0 \\
f'(x) &= \cos x, & f'(0) &= 1 \\
f''(x) &= -\sin x, & f''(0) &= 0 \\
f'''(x) &= -\cos x, & f'''(0) &= -1 \\
f^{(4)}(x) &= \sin x, & f^{(4)}(0) &= 0 \\
f^{(5)}(x) &= \cos x, & f^{(5)}(0) &= 1
\end{aligned}
\]

Maclaurin series up to \(x^5\):

\[
\sin x \approx 0 + \frac{1}{1!}x + \frac{0}{2!}x^2 + \frac{-1}{3!}x^3 + \frac{0}{4!}x^4 + \frac{1}{5!}x^5 = x - \frac{x^3}{6} + \frac{x^5}{120}
\]

In sigma notation:

\[
\sin x = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{(2n+1)!}
\]

**Answer:** \(x - \dfrac{x^3}{6} + \dfrac{x^5}{120}\). Sigma notation: \(\displaystyle \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{(2n+1)!}\)

*Pitfall: Mixing up the pattern — note that only odd powers appear, and the signs alternate starting with positive.*

---

## Problem 18
**Approach:** Compute derivatives of \(f(x) = \ln x\) at the center \(x = 1\) and construct the Taylor series.

\[
\begin{aligned}
f(x) &= \ln x, & f(1) &= \ln 1 = 0 \\
f'(x) &= \frac{1}{x}, & f'(1) &= 1 \\
f''(x) &= -\frac{1}{x^2}, & f''(1) &= -1 \\
f'''(x) &= \frac{2}{x^3}, & f'''(1) &= 2
\end{aligned}
\]

Taylor series about \(x = 1\):

\[
\ln x \approx f(1) + \frac{f'(1)}{1!}(x-1) + \frac{f''(1)}{2!}(x-1)^2 + \frac{f'''(1)}{3!}(x-1)^3
\]

\[
= 0 + 1 \cdot (x-1) + \frac{-1}{2}(x-1)^2 + \frac{2}{6}(x-1)^3
\]

\[
= (x-1) - \frac{(x-1)^2}{2} + \frac{(x-1)^3}{3}
\]

**Answer:** \((x-1) - \dfrac{(x-1)^2}{2} + \dfrac{(x-1)^3}{3} + \cdots\)

*Pitfall: Applying the Maclaurin formula (center at 0) instead of the Taylor formula (center at 1). \(\ln x\) is undefined at \(x=0\), so a Maclaurin series does not exist.*

---

## Problem 19
**Approach:** Substitute \(2x\) into the known Maclaurin series for \(e^x\).

The Maclaurin series for \(e^x\) is:

\[
e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \cdots
\]

Replace \(x\) with \(2x\):

\[
e^{2x} = \sum_{n=0}^{\infty} \frac{(2x)^n}{n!} = \sum_{n=0}^{\infty} \frac{2^n x^n}{n!}
\]

Expanding up to \(x^4\):

\[
\begin{aligned}
n = 0 &: \frac{2^0 x^0}{0!} = 1 \\
n = 1 &: \frac{2^1 x^1}{1!} = 2x \\
n = 2 &: \frac{2^2 x^2}{2!} = \frac{4x^2}{2} = 2x^2 \\
n = 3 &: \frac{2^3 x^3}{3!} = \frac{8x^3}{6} = \frac{4}{3}x^3 \\
n = 4 &: \frac{2^4 x^4}{4!} = \frac{16x^4}{24} = \frac{2}{3}x^4
\end{aligned}
\]

**Answer:** \(1 + 2x + 2x^2 + \dfrac{4}{3}x^3 + \dfrac{2}{3}x^4 + \cdots\)

*Pitfall: Forgetting to simplify the factorial denominators after substitution. Each coefficient must be fully reduced.*

---

## Problem 20
**Approach:** Use the known Maclaurin series for \(\cos x\) and substitute \(x^2\).

\[
\cos x = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n}}{(2n)!} = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \frac{x^8}{8!} - \cdots
\]

Substitute \(x^2\) for \(x\):

\[
\cos(x^2) = \sum_{n=0}^{\infty} \frac{(-1)^n (x^2)^{2n}}{(2n)!} = \sum_{n=0}^{\infty} \frac{(-1)^n x^{4n}}{(2n)!}
\]

The first four non-zero terms:

\[
\begin{aligned}
n = 0 &: \frac{(-1)^0 x^{0}}{0!} = 1 \\
n = 1 &: \frac{(-1)^1 x^{4}}{2!} = -\frac{x^4}{2} \\
n = 2 &: \frac{(-1)^2 x^{8}}{4!} = \frac{x^8}{24} \\
n = 3 &: \frac{(-1)^3 x^{12}}{6!} = -\frac{x^{12}}{720}
\end{aligned}
\]

**Answer:** \(1 - \dfrac{x^4}{2} + \dfrac{x^8}{24} - \dfrac{x^{12}}{720}\)

*Pitfall: Using the wrong factorial. The denominator uses \((2n)!\), not \((4n)!\). For example, the \(x^8\) term corresponds to \(n=2\), so the denominator is \(4! = 24\).*

---

## Problem 21
**Approach:** Expand \(\sin x\) as a Maclaurin series, simplify, and take the limit.

\[
\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots = x - \frac{x^3}{6} + \frac{x^5}{120} - \cdots
\]

Then:

\[
\sin x - x = \left(x - \frac{x^3}{6} + \frac{x^5}{120} - \cdots\right) - x = -\frac{x^3}{6} + \frac{x^5}{120} - \cdots
\]

\[
\frac{\sin x - x}{x^3} = \frac{-\frac{x^3}{6} + \frac{x^5}{120} - \cdots}{x^3} = -\frac{1}{6} + \frac{x^2}{120} - \cdots
\]

Now take the limit as \(x \to 0\):

\[
\lim_{x \to 0} \frac{\sin x - x}{x^3} = \lim_{x \to 0} \left(-\frac{1}{6} + \frac{x^2}{120} - \cdots\right) = -\frac{1}{6}
\]

**Answer:** \(-\dfrac{1}{6}\)

*Pitfall: Trying to apply L'Hôpital's Rule three times — it works but is far more cumbersome. The series approach is cleaner and reveals why the limit is \(-1/6\).*

---

## Problem 22
**Approach:** Substitute the given derivative values into the Maclaurin polynomial formula.

The Maclaurin polynomial of degree \(n\) is:

\[
P_n(x) = \sum_{k=0}^{n} \frac{f^{(k)}(0)}{k!} x^k
\]

Given values:
- \(f(0) = 2\)
- \(f'(0) = 1\)
- \(f''(0) = -2\)
- \(f'''(0) = 6\)
- \(f^{(4)}(0) = -24\)

\[
\begin{aligned}
k=0&: \frac{f(0)}{0!}x^0 = \frac{2}{1} = 2 \\
k=1&: \frac{f'(0)}{1!}x^1 = \frac{1}{1}x = x \\
k=2&: \frac{f''(0)}{2!}x^2 = \frac{-2}{2}x^2 = -x^2 \\
k=3&: \frac{f'''(0)}{3!}x^3 = \frac{6}{6}x^3 = x^3 \\
k=4&: \frac{f^{(4)}(0)}{4!}x^4 = \frac{-24}{24}x^4 = -x^4
\end{aligned}
\]

**Answer:** \(P_4(x) = 2 + x - x^2 + x^3 - x^4\)

*Pitfall: Forgetting to divide by the appropriate factorial. The coefficient for \(x^k\) is \(f^{(k)}(0)/k!\), not just \(f^{(k)}(0)\).*

---

## Problem 23
**Approach:** Apply the Lagrange error bound formula for Taylor polynomials.

The Maclaurin polynomial of degree 3 for \(\sin x\) is:

\[
P_3(x) = x - \frac{x^3}{6}
\]

The next derivative is \(f^{(4)}(x) = \sin x\). The Lagrange error bound states:

\[
|R_3(x)| \leq \frac{M |x|^{4}}{4!}
\]

where \(M\) is an upper bound on \(|f^{(4)}(c)|\) for \(c\) between 0 and \(x\). Since all derivatives of \(\sin x\) are bounded by 1, we have \(M = 1\).

At \(x = 0.5\):

\[
|R_3(0.5)| \leq \frac{1 \cdot (0.5)^4}{4!} = \frac{0.0625}{24} = \frac{1}{384} \approx 0.002604
\]

**Answer:** The error is at most \(\frac{1}{384} \approx 0.002604\).

*Pitfall: Using the degree of the polynomial as \(n\) but then using \(|x|^{n+1}\) in the numerator. For degree 3, the error involves the 4th derivative and \(|x|^4\).*

---

## Problem 24
**Approach:** Use the Alternating Series Estimation Theorem.

For an alternating series \(\sum_{n=1}^{\infty} (-1)^{n+1} b_n\) that satisfies the AST conditions, the error after \(n\) terms is bounded by the first omitted term:

\[
|R_n| \leq b_{n+1}
\]

Here, \(b_n = \frac{1}{n^2}\). We need \(b_{n+1} < 0.001\):

\[
\frac{1}{(n+1)^2} < 0.001 = \frac{1}{1000}
\]

\[
(n+1)^2 > 1000
\]

\[
n+1 > \sqrt{1000} \approx 31.62
\]

\[
n+1 \geq 32 \quad \Longrightarrow \quad n \geq 31
\]

Thus, at least 31 terms are needed. Let's verify: after 31 terms, the first omitted term is \(b_{32} = 1/32^2 = 1/1024 \approx 0.000977 < 0.001\). After 30 terms, the first omitted term is \(b_{31} = 1/31^2 = 1/961 \approx 0.00104 > 0.001\).

**Answer:** 31 terms are needed.

*Pitfall: Confusing the number of terms \(n\) with the index of the next term. The error after \(n\) terms is bounded by the \((n+1)\)-th term, not the \(n\)-th term.*

---

## Problem 25
**Approach:** (a) Apply the Ratio Test. (b) Relate the series to the Maclaurin series for \(e^x\).

(a) Let \(a_n = \frac{2^n}{n!}\).

\[
\lim_{n\to\infty} \left| \frac{a_{n+1}}{a_n} \right| = \lim_{n\to\infty} \frac{2^{n+1} / (n+1)!}{2^n / n!} = \lim_{n\to\infty} \frac{2}{n+1} = 0
\]

Since \(0 < 1\), the series converges absolutely by the Ratio Test.

(b) The Maclaurin series for \(e^x\) is:

\[
e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots
\]

Setting \(x = 2\):

\[
e^2 = \sum_{n=0}^{\infty} \frac{2^n}{n!} = 1 + \sum_{n=1}^{\infty} \frac{2^n}{n!}
\]

Therefore:

\[
\sum_{n=1}^{\infty} \frac{2^n}{n!} = e^2 - 1
\]

**Answer:** (a) The series converges by the Ratio Test. (b) The sum is \(e^2 - 1\).

*Pitfall: Forgetting that the Maclaurin series for \(e^x\) starts at \(n=0\) (which gives the term \(1\)), while the given series starts at \(n=1\). The sum is \(e^2 - 1\), not simply \(e^2\).*
