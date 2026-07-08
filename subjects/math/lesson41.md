# Lesson 41: Polynomial Theorems — Factor Theorem, Remainder Theorem, and Complex Roots

## What Are These Theorems?

A **polynomial** is an expression like $x^3 - 4x^2 + 2x - 5$ — it is a sum of terms where each term is a constant times a power of x. The **degree** of a polynomial is the highest power of x (e.g., the polynomial above has degree 3).

This lesson covers three interconnected ideas:
- The **Remainder Theorem**: a shortcut for finding the remainder when dividing a polynomial by (x − a).
- The **Factor Theorem**: a way to check whether (x − a) divides a polynomial evenly.
- The behavior of **complex roots**: how imaginary and complex numbers appear as roots of polynomial equations.

These are core IB AAHL Topic 1 tools. They let you factor polynomials, find roots, and solve equations without always doing long division.

## Why Learn This?

In IB exams, you are often asked to factor a cubic or quartic polynomial, to find an unknown coefficient given a condition, or to find all roots (including complex ones). The remainder and factor theorems give you quick methods, and the rule about complex conjugate pairs prevents you from missing roots.

---

## Part 1: The Remainder Theorem

**Statement:** When you divide a polynomial P(x) by (x − a), the remainder of that division is equal to P(a).

In other words, you do not need to perform long division to find the remainder. Just plug x = a into the polynomial and evaluate.

**What does "remainder" mean here?** In polynomial division, the remainder is what is left over. If P(x) divided by (x − a) gives quotient Q(x) and remainder R, we can write:
$$P(x) = (x - a) \cdot Q(x) + R$$
The remainder R is always a constant (a number, not an expression involving x) when dividing by a linear factor like (x − a).

### Worked Example 1: Find a Remainder

**Problem:** Find the remainder when $P(x) = x^3 - 4x^2 + 2x - 5$ is divided by (x − 3).

**Approach:** By the Remainder Theorem, the remainder equals P(3).

$P(3) = (3)^3 - 4(3)^2 + 2(3) - 5$.
$P(3) = 27 - 4(9) + 6 - 5$.
$P(3) = 27 - 36 + 6 - 5$.
$P(3) = -8$.

**Answer:** The remainder is **−8**. No long division was needed.

### Worked Example 2: Find an Unknown Coefficient

**Problem:** The polynomial $P(x) = 2x^3 + kx^2 - x + 4$ has remainder 6 when divided by (x + 1). Find the value of k.

**Approach:** First, rewrite (x + 1) in the form (x − a). Since (x + 1) = (x − (−1)), we have a = −1.

By the Remainder Theorem, P(−1) must equal 6.

$P(-1) = 2(-1)^3 + k(-1)^2 - (-1) + 4$.
$P(-1) = 2(-1) + k(1) + 1 + 4$.
$P(-1) = -2 + k + 1 + 4 = k + 3$.

Set equal to 6:
$k + 3 = 6$
$k = 3$.

**Answer:** k = 3.

---

## Part 2: The Factor Theorem

**Statement:** (x − a) is a factor of P(x) **if and only if** P(a) = 0.

This follows directly from the Remainder Theorem. If the remainder is zero, then the divisor divides the polynomial exactly, which means the divisor is a factor.

**What does "if and only if" mean?** It means two things:
- If (x − a) is a factor, then P(a) = 0.
- If P(a) = 0, then (x − a) is a factor.

### Worked Example 3: Test Whether (x − 2) Is a Factor

**Problem:** Is (x − 2) a factor of $P(x) = x^3 - 5x^2 + 8x - 4$?

**Approach:** Test P(2). If P(2) = 0, then (x − 2) is a factor.

$P(2) = (2)^3 - 5(2)^2 + 8(2) - 4$.
$P(2) = 8 - 5(4) + 16 - 4$.
$P(2) = 8 - 20 + 16 - 4 = 0$.

**Answer:** Yes, (x − 2) is a factor because P(2) = 0.

### Worked Example 4: Full Factorization of a Cubic

**Problem:** Factorize $P(x) = x^3 - 3x^2 - 4x + 12$ completely.

**Approach:** We systematically test small integer values of x to find a root.

**Step 1: Test x = 1.**
$P(1) = 1 - 3 - 4 + 12 = 6$. Not zero, so (x − 1) is not a factor.

**Step 2: Test x = 2.**
$P(2) = 8 - 12 - 8 + 12 = 0$. Bingo — (x − 2) is a factor.

**Step 3: Divide P(x) by (x − 2).** We can use polynomial long division or synthetic division. The result of dividing $x^3 - 3x^2 - 4x + 12$ by (x − 2) is the quadratic $x^2 - x - 6$.

**Step 4: Factor the quadratic.**
$x^2 - x - 6 = (x - 3)(x + 2)$.

**Step 5: Write the full factorization.**
$P(x) = (x - 2)(x - 3)(x + 2)$.

**Answer:** $x^3 - 3x^2 - 4x + 12 = (x - 2)(x - 3)(x + 2)$. The roots are x = 2, x = 3, and x = −2.

---

## Part 3: The Fundamental Theorem of Algebra and Complex Conjugate Roots

The **Fundamental Theorem of Algebra** says: every polynomial of degree n with complex coefficients has exactly n complex roots, if you count each root as many times as its multiplicity (how many times it repeats).

For our purposes in IB AAHL, the most important consequence is about polynomials with **real coefficients** (coefficients that are ordinary real numbers, not imaginary):

**If a polynomial has real coefficients and a complex number a + bi is a root, then its complex conjugate a − bi is also a root.**

The **complex conjugate** of a number reverses the sign of the imaginary part. The conjugate of 3 + 4i is 3 − 4i. The conjugate of −2 − 5i is −2 + 5i. The conjugate of a real number (like 7) is just itself (7 − 0i = 7).

**Why does this matter?** Complex roots always come in pairs for polynomials with real coefficients. If you find one complex root, you automatically get a second one for free.

### Worked Example 5: Find the Missing Root

**Problem:** A cubic polynomial with real coefficients has roots at x = 2 and x = 3 + i. Find the third root.

**Approach:** Since the coefficients are real, complex roots must come in conjugate pairs. The conjugate of 3 + i is 3 − i.

**Answer:** The three roots are 2, 3 + i, and **3 − i**.

### Worked Example 6: Build a Polynomial from Its Roots

**Problem:** Find a polynomial with real coefficients, leading coefficient 1, that has roots 1, −2, and i.

**Approach:** Since coefficients must be real and i is a root, its conjugate −i must also be a root. So we actually have four roots: 1, −2, i, −i.

The polynomial is the product of factors (x − root):

$P(x) = (x - 1)(x - (-2))(x - i)(x - (-i))$
$P(x) = (x - 1)(x + 2)(x - i)(x + i)$.

Now multiply the conjugate pair: $(x - i)(x + i) = x^2 - i^2 = x^2 - (-1) = x^2 + 1$.

Multiply the real factors: $(x - 1)(x + 2) = x^2 + 2x - x - 2 = x^2 + x - 2$.

Now multiply these two quadratics:
$P(x) = (x^2 + x - 2)(x^2 + 1)$.
$= x^2(x^2 + 1) + x(x^2 + 1) - 2(x^2 + 1)$.
$= x^4 + x^2 + x^3 + x - 2x^2 - 2$.
$= x^4 + x^3 - x^2 + x - 2$.

**Answer:** $P(x) = x^4 + x^3 - x^2 + x - 2$.

---

## Part 4: Sum and Product of Roots (Vieta's Formulas)

For a quadratic $ax^2 + bx + c = 0$ with roots α and β:
- Sum of roots: $\alpha + \beta = -\frac{b}{a}$.
- Product of roots: $\alpha\beta = \frac{c}{a}$.

For a cubic $ax^3 + bx^2 + cx + d = 0$ with roots α, β, γ:

$$\alpha + \beta + \gamma = -\frac{b}{a}$$

$$\alpha\beta + \alpha\gamma + \beta\gamma = \frac{c}{a}$$

$$\alpha\beta\gamma = -\frac{d}{a}$$

These relationships are called **Vieta's formulas** (or Vieta's relations). They let you find information about the roots without solving the equation directly.

### Worked Example 7: Roots with a Repeated Value

**Problem:** The equation $2x^3 - 3x^2 - 12x + 20 = 0$ has two equal roots. Find all three roots.

**Approach:** Let the roots be p, p, and q (p is the value that repeats).

**Step 1: Use the sum formula.**
Sum = p + p + q = 2p + q = $-\frac{b}{a} = -\frac{(-3)}{2} = \frac{3}{2}$.
So $2p + q = \frac{3}{2}$, which means $q = \frac{3}{2} - 2p$.

**Step 2: Use the product formula.**
Product = $p \cdot p \cdot q = p^2 q = -\frac{d}{a} = -\frac{20}{2} = -10$.

**Step 3: Substitute q from Step 1.**
$p^2 \left(\frac{3}{2} - 2p\right) = -10$.
$\frac{3}{2}p^2 - 2p^3 = -10$.

Multiply both sides by 2:
$3p^2 - 4p^3 = -20$.

Rearrange:
$4p^3 - 3p^2 - 20 = 0$.

**Step 4: Find p.** Test small integers. Try p = 2: $4(8) - 3(4) - 20 = 32 - 12 - 20 = 0$. So p = 2 works.

**Step 5: Find q.**
$q = \frac{3}{2} - 2(2) = \frac{3}{2} - 4 = \frac{3}{2} - \frac{8}{2} = -\frac{5}{2}$.

**Answer:** The three roots are 2, 2, and $-\frac{5}{2}$.

---

## Common Misconceptions

**Misconception 1:** "P(a) gives the answer when dividing by (x − a)." No — P(a) gives the **remainder**, not the quotient. The quotient is still a polynomial that you would need to find through division.

**Misconception 2:** "If (x − a) is a factor, then a is the only root." A polynomial can have many factors and many roots. Finding one factor is just the first step. After dividing it out, you need to factor what is left.

**Misconception 3:** "Complex roots only appear when the polynomial has complex coefficients." Complex roots can appear even when all coefficients are real. For example, $x^2 + 1 = 0$ has real coefficients but roots i and −i. The rule is: if coefficients are real, complex roots come in conjugate pairs.

**Misconception 4:** "The sum and product formulas only work for quadratics." They work for polynomials of any degree, though the formulas get more complicated. For a cubic there are three formulas; for a quartic there are four, and so on.

**Misconception 5:** "I should test every integer to find a factor." Start with small integers: 0, ±1, ±2, ±3. Also, if the leading coefficient is not 1, try fractions of the form (factor of constant term)/(factor of leading coefficient). This is called the **Rational Root Theorem** — a useful extension of the Factor Theorem.

---

## Practice Problems

**1.** Find the remainder when $P(x) = x^4 - 3x^3 + 2x - 7$ is divided by (x + 1).

**2.** The polynomial $P(x) = x^3 + kx^2 - x - 6$ has (x − 2) as a factor. Find the value of k, then factorize P(x) completely.

**3.** Show that (x + 3) is a factor of $x^3 + 5x^2 + 8x + 6$. Then find all roots of the polynomial.

**4.** Find all roots (real and complex) of the equation $x^3 - 6x^2 + 11x - 6 = 0$.

**5.** A cubic polynomial has roots 1, −3, and 4. The leading coefficient (the coefficient of x³) is 2. Write the polynomial in standard form.

**6. [IB Exam Style — 7 marks]** The cubic equation $x^3 + px^2 + qx + 6 = 0$ has roots 1, 2, and r, where p, q, and r are real numbers.

(a) Use the relationship between the roots and the coefficients to find the value of r. [2 marks]

(b) Find the values of p and q. [3 marks]

(c) Write the equation in the form $(x - 1)(x - 2)(x - r) = 0$ and verify that your values of p and q are correct. [2 marks]

---

## Answers

**1.** For (x + 1), a = −1. P(−1) = (−1)⁴ − 3(−1)³ + 2(−1) − 7 = 1 − 3(−1) − 2 − 7 = 1 + 3 − 2 − 7 = −5. The remainder is **−5**.

**2.** Since (x − 2) is a factor, P(2) = 0. P(2) = (2)³ + k(2)² − 2 − 6 = 8 + 4k − 8 = 4k. So 4k = 0 → k = 0. The polynomial is P(x) = x³ − x − 6. Divide by (x − 2) to get x² + 2x + 3. The quadratic $x^2 + 2x + 3$ has discriminant $\Delta = 4 - 12 = -8 < 0$, so it has no real roots. Answer: $P(x) = (x - 2)(x^2 + 2x + 3)$.

**3.** Show P(−3) = 0: P(−3) = (−27) + 5(9) + 8(−3) + 6 = −27 + 45 − 24 + 6 = 0. Since P(−3) = 0, (x + 3) is a factor. Divide $x^3 + 5x^2 + 8x + 6$ by (x + 3) to get $x^2 + 2x + 2$. The quadratic $x^2 + 2x + 2 = 0$ gives $x = \frac{-2 \pm \sqrt{4 - 8}}{2} = \frac{-2 \pm \sqrt{-4}}{2} = \frac{-2 \pm 2i}{2} = -1 \pm i$. Roots: −3, −1 + i, −1 − i.

**4.** Test x = 1: $1 - 6 + 11 - 6 = 0$, so (x − 1) is a factor. Divide to get $x^2 - 5x + 6$, which factors as (x − 2)(x − 3). Roots: **1, 2, 3**.

**5.** The polynomial is $P(x) = 2(x - 1)(x + 3)(x - 4)$. Multiply the factors: $(x - 1)(x + 3) = x^2 + 2x - 3$. Then $(x^2 + 2x - 3)(x - 4) = x^3 - 4x^2 + 2x^2 - 8x - 3x + 12 = x^3 - 2x^2 - 11x + 12$. Multiply by 2: **$2x^3 - 4x^2 - 22x + 24$**.

**6.** (a) Product of roots: $1 \times 2 \times r = -\frac{d}{a} = -\frac{6}{1} = -6$. So $2r = -6$, hence $r = -3$. [2 marks]

(b) Sum of roots: $1 + 2 + (-3) = 0 = -\frac{p}{1}$, so $p = 0$. Sum of pairwise products: $(1)(2) + (1)(-3) + (2)(-3) = 2 - 3 - 6 = -7 = \frac{q}{1}$, so $q = -7$. [3 marks]

(c) $(x - 1)(x - 2)(x + 3) = (x^2 - 3x + 2)(x + 3) = x^3 + 3x^2 - 3x^2 - 9x + 2x + 6 = x^3 - 7x + 6$. This matches $x^3 + 0x^2 - 7x + 6$, confirming p = 0 and q = −7. [2 marks]
