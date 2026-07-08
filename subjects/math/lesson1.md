# Lesson 1: L'Hôpital's Rule & Continuity

## What You'll Learn
Two foundational calculus tools: L'Hôpital's rule for evaluating tricky limits, and the formal definition of continuity. Both are essential for everything that follows.

---

## Part 1: L'Hôpital's Rule

### What It Is and Why It Matters

When you evaluate a limit and get an expression like 0/0 or ∞/∞, the limit could be anything — zero, infinity, or some finite number. These are called **indeterminate forms** because the value is not determined by the form alone.

L'Hôpital's rule gives you a systematic way to resolve these indeterminate forms. Instead of guessing or trying to factor, you differentiate the numerator and denominator separately (this is NOT the quotient rule) and take the limit again.

### The Rule

If the limit of f(x)/g(x) as x approaches a gives the indeterminate form 0/0 or ∞/∞, then:

$$\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}$$

provided the new limit exists. You can apply this rule repeatedly if the result is still indeterminate.

**Common misconception:** Many students apply the quotient rule when using L'Hôpital. You must differentiate the numerator and denominator independently — do not use the quotient rule formula.

### Forms That Work Directly

| Form | You can apply L'Hôpital immediately |
|---|---|
| 0/0 | Example: (e^x − 1 − x)/x² as x → 0 |
| ∞/∞ | Example: ln x / x as x → ∞ |

### Forms That Need Conversion First

| Form | Strategy |
|---|---|
| 0 · ∞ | Rewrite as 0/0 or ∞/∞. Example: x·ln x = ln x / (1/x) |
| ∞ − ∞ | Combine into a single fraction |
| 1^∞, 0^0, ∞^0 | Take natural log, use L'Hôpital on the result, then exponentiate |

---

### Worked Example 1: Two Applications

**Problem:** Evaluate \(\lim_{x \to 0} \frac{e^x - 1 - x}{x^2}\).

**Approach:** Substitute x = 0 first. The numerator gives e^0 − 1 − 0 = 0, and the denominator gives 0. This is the 0/0 indeterminate form, so we can apply L'Hôpital's rule. We will need to apply it twice because the first application still produces 0/0.

**Step 1 — First application of L'Hôpital:**
Differentiate the numerator: d/dx(e^x − 1 − x) = e^x − 1.
Differentiate the denominator: d/dx(x^2) = 2x.

The limit becomes \(\lim_{x \to 0} \frac{e^x - 1}{2x}\).

Substituting x = 0 still gives 0/0, so we apply L'Hôpital again.

**Step 2 — Second application:**
Differentiate the new numerator: d/dx(e^x − 1) = e^x.
Differentiate the new denominator: d/dx(2x) = 2.

The limit is now \(\lim_{x \to 0} \frac{e^x}{2} = \frac{1}{2}\).

**Why this makes sense:** The function (e^x − 1 − x)/x^2 behaves like 1/2 near x = 0. You can verify this by checking the Taylor series: e^x = 1 + x + x^2/2 + x^3/6 + ..., so the numerator is x^2/2 + higher terms, and dividing by x^2 gives 1/2 as x → 0.

---

### Worked Example 2: ∞/∞ Form

**Problem:** Evaluate \(\lim_{x \to \infty} \frac{\ln x}{x}\).

**Approach:** As x → ∞, ln x → ∞ and x → ∞, giving the ∞/∞ indeterminate form. We can apply L'Hôpital's rule directly.

**Step 1:** Differentiate the numerator: d/dx(ln x) = 1/x.
Differentiate the denominator: d/dx(x) = 1.

The limit becomes \(\lim_{x \to \infty} \frac{1/x}{1} = \lim_{x \to \infty} \frac{1}{x} = 0\).

**Why this makes sense:** Logarithmic functions grow much more slowly than polynomial functions. As x becomes extremely large, ln x is dwarfed by x, so the ratio approaches zero.

---

### Worked Example 3: 0·∞ Form (Conversion Required)

**Problem:** Evaluate \(\lim_{x \to 0^+} x \ln x\).

**Approach:** As x → 0^+, x → 0 but ln x → −∞. This gives the indeterminate form 0·(−∞), which does not directly fit L'Hôpital's rule. We need to rewrite the product as a quotient by moving one factor to the denominator.

**Step 1 — Rewrite:** Place ln x in the numerator and 1/x in the denominator:
\(x \ln x = \frac{\ln x}{1/x}\).

**Step 2 — Check the form:** As x → 0^+, ln x → −∞ and 1/x → ∞. This is now the ∞/∞ form, so L'Hôpital applies.

**Step 3 — Apply L'Hôpital:**
Differentiate numerator: d/dx(ln x) = 1/x.
Differentiate denominator: d/dx(1/x) = −1/x^2.
\(\lim_{x \to 0^+} \frac{1/x}{-1/x^2} = \lim_{x \to 0^+} (-x) = 0\).

**Why this makes sense:** The polynomial factor x dominates the logarithmic factor ln x near zero. Even though ln x → −∞, the factor x goes to zero fast enough to pull the product to zero.

---

## Part 2: Continuity

### What It Means

A function is **continuous** at a point x = a if you can draw the graph through that point without lifting your pen. More precisely, three conditions must hold simultaneously:

1. The function value f(a) must exist (the point is defined).
2. The limit as x approaches a must exist (the left-hand and right-hand limits agree).
3. The limit must equal the function value: lim(x→a) f(x) = f(a).

If any of these three conditions fails, the function has a **discontinuity** at that point.

**Common misconception:** Many students think a function is continuous if "the graph looks smooth." A function can have a sharp corner (like |x| at x = 0) and still be continuous. Continuity is about having no gaps or jumps — a corner is not a discontinuity.

---

### Worked Example 4: Checking Continuity at a Point

**Problem:** Determine whether the function

\[
f(x) = \begin{cases}
x^2 + 1, & x < 2 \\
5, & x = 2 \\
3x - 1, & x > 2
\end{cases}
\]

is continuous at x = 2.

**Approach:** We need to check all three conditions for continuity. The function is defined piecewise, so we must use the correct piece when computing each limit.

**Step 1 — Check that f(2) exists:**
The function explicitly assigns f(2) = 5. The value exists.

**Step 2 — Check the left-hand limit:**
As x approaches 2 from the left (x → 2^−), we use the first piece: f(x) = x^2 + 1.
lim(x→2^−) (x^2 + 1) = 2^2 + 1 = 5.

**Step 3 — Check the right-hand limit:**
As x approaches 2 from the right (x → 2^+), we use the third piece: f(x) = 3x − 1.
lim(x→2^+) (3x − 1) = 3(2) − 1 = 5.

**Step 4 — Compare:**
The left-hand limit is 5, the right-hand limit is 5, and f(2) is 5. All three values agree.

The function is continuous at x = 2 because f(2) exists, the two-sided limit exists (both one-sided limits equal 5), and the limit equals the function value.

**Why this makes sense:** Although the function is defined in three separate pieces, all three pieces converge to the same point (2, 5). There is no gap or jump in the graph at x = 2.

---

### The Intermediate Value Theorem (IVT)

If a function f is continuous on a closed interval [a, b], then for any value N between f(a) and f(b), there exists at least one number c in [a, b] such that f(c) = N.

In simpler terms: a continuous function cannot skip values. If it starts at one height and ends at another, it must pass through every height in between.

The IVT is especially useful for proving that equations have solutions. If f(a) and f(b) have opposite signs and f is continuous, then there must be at least one root in the interval (a, b).

---

### Worked Example 5: Proving a Root Exists

**Problem:** Show that the equation x^3 − 3x + 1 = 0 has a root between 0 and 1.

**Approach:** Define f(x) = x^3 − 3x + 1. Since polynomials are continuous everywhere, we can apply the Intermediate Value Theorem on the interval [0, 1]. We just need to show that f(0) and f(1) have opposite signs.

**Step 1 — Evaluate at the endpoints:**
f(0) = 0^3 − 3(0) + 1 = 1, which is positive.
f(1) = 1^3 − 3(1) + 1 = 1 − 3 + 1 = −1, which is negative.

**Step 2 — Apply IVT:**
f is continuous on [0, 1] because it is a polynomial. f(0) = 1 > 0 and f(1) = −1 < 0. Since the function changes from positive to negative on the interval, and since it is continuous, there must be some number c between 0 and 1 where f(c) = 0.

The equation x^3 − 3x + 1 = 0 has at least one solution in the interval (0, 1).

**Why this makes sense:** The graph of the cubic crosses the x-axis somewhere between x = 0 and x = 1 because it goes from above the axis to below the axis, and a continuous curve cannot jump over the axis without touching it.

---

## Practice Problems

**1.** Evaluate the limit \(\lim_{x \to 1} \frac{x^3 - 1}{x - 1}\) by applying L'Hôpital's rule.

**2.** Evaluate \(\lim_{x \to 0} \frac{1 - \cos x}{x^2}\). You will need to apply L'Hôpital's rule twice.

**3.** Evaluate \(\lim_{x \to \infty} \frac{e^x}{x^3}\). Determine how many times you need to apply L'Hôpital's rule before the limit is resolved.

**4.** Is the function f(x) = 1/x continuous at x = 0? Explain your reasoning by checking all three conditions for continuity.

**5.** (IB Exam Style — 6 marks) A piecewise function is defined by
\[
g(x) = \begin{cases}
x^2 + k, & x \leq 1 \\
4x - 1, & x > 1
\end{cases}
\]
where k is a constant.
(a) Find the value of k for which g is continuous at x = 1. [3 marks]
(b) For the value of k found in part (a), sketch the graph of y = g(x) on the interval [−1, 3], labelling the coordinates of the point where the two pieces meet. [3 marks]

**6.** Use the Intermediate Value Theorem to show that the equation 2x^3 − x^2 − 7 = 0 has a solution in the interval [1, 2].

---

## Answers

**1.** Substituting x = 1 gives the indeterminate form 0/0 because the numerator is 1 − 1 = 0 and the denominator is 1 − 1 = 0. Applying L'Hôpital's rule, we differentiate the numerator to get 3x^2 and the denominator to get 1. The limit becomes lim(x→1) 3x^2 = 3(1)^2 = 3. The answer is 3. A common mistake is to apply the quotient rule here — remember that L'Hôpital's rule requires differentiating the numerator and denominator separately.

**2.** Substituting x = 0 gives (1 − 1)/0 = 0/0, which is indeterminate. We apply L'Hôpital's rule the first time: the derivative of the numerator 1 − cos x is sin x, and the derivative of the denominator x^2 is 2x. The limit becomes lim(x→0) sin x / (2x). This still gives the indeterminate form 0/0 because sin 0 = 0 and 2(0) = 0. We apply L'Hôpital's rule a second time: the derivative of sin x is cos x, and the derivative of 2x is 2. The limit becomes lim(x→0) cos x / 2 = 1/2. The answer is 1/2. A common pitfall is stopping after the first application and incorrectly concluding the limit is 0 just because sin x → 0.

**3.** As x → ∞, both e^x and x^3 approach infinity, giving the indeterminate form ∞/∞. We apply L'Hôpital's rule repeatedly. First application: the derivative of e^x is e^x, and the derivative of x^3 is 3x^2. The limit becomes lim(x→∞) e^x / (3x^2), which is still ∞/∞. Second application: the derivative of e^x is e^x, and the derivative of 3x^2 is 6x. The limit is now lim(x→∞) e^x / (6x), still ∞/∞. Third application: the derivative of e^x is e^x, and the derivative of 6x is 6. The limit becomes lim(x→∞) e^x / 6 = ∞. We needed to apply L'Hôpital's rule three times. The answer is infinity. This illustrates that exponential functions grow faster than any polynomial — no matter how many times you differentiate x^3, it eventually becomes a constant (6), while e^x remains e^x and continues to grow without bound.

**4.** The function f(x) = 1/x is not continuous at x = 0. We check the three conditions. Condition 1: f(0) must be defined. However, f(0) = 1/0 is undefined because division by zero has no meaning in the real numbers. The function already fails the first condition, so we do not need to check the other two. For completeness: even though the left-hand limit as x → 0^− is −∞ and the right-hand limit as x → 0^+ is +∞, these one-sided limits are not finite and they do not agree with each other, so the two-sided limit does not exist either. A common misconception is to say that 1/x is "discontinuous at x = 0 because there is an asymptote." While this is a useful intuition, the formal reason is that f(0) is simply not defined — continuity requires the point to exist in the domain of the function.

**5.** (a) For g to be continuous at x = 1, the left-hand limit, the right-hand limit, and the function value must all be equal. The function value g(1) uses the first piece (x ≤ 1): g(1) = 1^2 + k = 1 + k. The right-hand limit as x → 1^+ uses the second piece: lim(x→1^+) (4x − 1) = 4(1) − 1 = 3. Setting these equal gives 1 + k = 3, so k = 2.
(b) With k = 2, the first piece is y = x^2 + 2 for x ≤ 1. At x = 1, this gives y = 1^2 + 2 = 3. The second piece is y = 4x − 1 for x > 1, which also approaches y = 3 as x → 1^+. The pieces meet at the point (1, 3). On the interval [−1, 3], the left piece y = x^2 + 2 is a parabola that starts at (−1, 3), dips to (0, 2), and rises to (1, 3). The right piece y = 4x − 1 is a straight line from (1, 3) through (2, 7) to (3, 11). The graph has no break or jump at x = 1 — the pieces join smoothly in terms of position, though there is a sharp change in direction.

**6.** Define f(x) = 2x^3 − x^2 − 7. This is a polynomial, so it is continuous on every interval, including [1, 2]. Evaluate the function at the endpoints of the interval. f(1) = 2(1)^3 − 1^2 − 7 = 2 − 1 − 7 = −6, which is negative. f(2) = 2(8) − 4 − 7 = 16 − 4 − 7 = 5, which is positive. Since f is continuous on [1, 2] and f(1) and f(2) have opposite signs, the Intermediate Value Theorem guarantees that there exists some number c in the interval (1, 2) such that f(c) = 0. Therefore the equation 2x^3 − x^2 − 7 = 0 has at least one solution in [1, 2]. A common mistake is to forget to state explicitly that f is continuous — the IVT cannot be applied without this justification, even for a polynomial.
