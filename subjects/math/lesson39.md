# Lesson 39: The Binomial Theorem — Expanding Powers of (a + b)

## What is the Binomial Theorem?

A **binomial** is an expression with two terms, like (x + 2) or (2a − 3b). The **binomial theorem** is a formula that lets you expand (a + b)^n — that is, multiply (a + b) by itself n times — without doing the multiplication term by term. This is a core IB AAHL Topic 1 skill that connects algebra with combinatorics (counting) and also appears in infinite series.

## Why Learn This?

If someone asks you to expand (x + 2)^4, you could multiply (x + 2)(x + 2)(x + 2)(x + 2) by hand and collect terms. That works for n = 4, but what about (x + 2)^20? The binomial theorem gives you a shortcut. It also lets you find a single specific term — like "what is the coefficient of x^7 in (2x − 1)^10?" — without expanding the whole thing. This shows up regularly in IB exams.

---

## Part 1: The Binomial Coefficient

Before we can use the theorem, we need to understand a symbol called the **binomial coefficient**, written as:

$$\binom{n}{r}$$

This is pronounced "n choose r." It tells you the number of ways to select r items from a group of n items (you will see this again in Lesson 40 on counting). For now, think of it as a number that appears in the expansion formula.

The formula is:

$$\binom{n}{r} = \frac{n!}{r!(n-r)!}$$

**What does n! mean?** The symbol n! (pronounced "n factorial") means you multiply all positive whole numbers from n down to 1. For example:
- 5! = 5 × 4 × 3 × 2 × 1 = 120
- 3! = 3 × 2 × 1 = 6
- 1! = 1
- 0! is defined as 1 (this is a special convention that makes formulas work).

There is also a shortcut for computing binomial coefficients without writing all the factorials:

$$\binom{n}{r} = \frac{n(n-1)(n-2)\cdots(n-r+1)}{r!}$$

This means: start at n, multiply downward r terms, then divide by r!.

**Examples:**
- $\binom{5}{2} = \frac{5 \times 4}{2 \times 1} = \frac{20}{2} = 10$.
- $\binom{7}{3} = \frac{7 \times 6 \times 5}{3 \times 2 \times 1} = \frac{210}{6} = 35$.

**Special values to memorize:**
- $\binom{n}{0} = 1$ (there is exactly one way to choose nothing).
- $\binom{n}{1} = n$ (there are n ways to choose one item).
- $\binom{n}{n} = 1$ (there is exactly one way to choose everything).

---

## Part 2: Binomial Theorem for Positive Integer n

When n is a positive whole number (n = 1, 2, 3, 4, ...), the expansion looks like this:

$$(a+b)^n = \sum_{r=0}^{n} \binom{n}{r} a^{n-r} b^r$$

The symbol Σ (capital sigma) means "sum all the terms from r = 0 to r = n." Let's write out what this means, term by term:

$$(a+b)^n = \binom{n}{0}a^n b^0 + \binom{n}{1}a^{n-1}b^1 + \binom{n}{2}a^{n-2}b^2 + \cdots + \binom{n}{n}a^0 b^n$$

Notice the pattern:
- The powers of a go down: a^n, a^{n−1}, a^{n−2}, ..., a^0.
- The powers of b go up: b^0, b^1, b^2, ..., b^n.
- In each term, the two exponents add up to n.
- The binomial coefficient tells you how many of that type of term appear when you multiply everything out.

### Worked Example 1: Expand (x + 2)^4

**Problem:** Write (x + 2)^4 as a polynomial in x.

**Approach:** Use the formula with a = x, b = 2, n = 4. We write terms for r = 0, 1, 2, 3, 4.

r = 0: $\binom{4}{0}x^4(2)^0 = 1 \cdot x^4 \cdot 1 = x^4$.

r = 1: $\binom{4}{1}x^3(2)^1 = 4 \cdot x^3 \cdot 2 = 8x^3$.

r = 2: $\binom{4}{2}x^2(2)^2 = 6 \cdot x^2 \cdot 4 = 24x^2$.

r = 3: $\binom{4}{3}x^1(2)^3 = 4 \cdot x \cdot 8 = 32x$.

r = 4: $\binom{4}{4}x^0(2)^4 = 1 \cdot 1 \cdot 16 = 16$.

Add all terms: $(x + 2)^4 = x^4 + 8x^3 + 24x^2 + 32x + 16$.

**Why this makes sense:** If you multiplied (x + 2)(x + 2)(x + 2)(x + 2) by hand, you would pick one term from each bracket and multiply. The term 8x^3 comes from picking x from three brackets and 2 from one bracket — and there are $\binom{4}{1} = 4$ ways to choose which bracket contributes the 2. The factor of 2³ = 8 gives 4 × 8 = 32 for the x term, and so on. The binomial coefficient counts the combinations.

### Worked Example 2: Find a Specific Coefficient

**Problem:** Find the coefficient of x³ in the expansion of (2x − 3)^5. (Do not expand the whole expression.)

**Approach:** In the binomial formula, a = 2x, b = −3, n = 5. The term with x³ means the power on a = 2x must be 3, so n − r = 3, which gives r = 2.

The term for r = 2 is: $\binom{5}{2} (2x)^3 (-3)^2$.

Compute each piece:
- $\binom{5}{2} = \frac{5 \times 4}{2} = 10$.
- $(2x)^3 = 8x^3$.
- $(-3)^2 = 9$.

Multiply: $10 \cdot 8x^3 \cdot 9 = 720x^3$.

**Answer:** The coefficient is **720**.

---

## Part 3: The General Binomial Theorem (for n That Is Not a Positive Integer)

What if n is a fraction, like 1/2, or a negative number, like −1? The formula changes. Instead of stopping at n terms, the expansion goes on forever (it is an **infinite series**). This only works when |x| < 1 (the absolute value of x is less than 1), because otherwise the infinite series does not settle down to a finite value.

For any real number n (not necessarily a positive integer):

$$(1+x)^n = 1 + nx + \frac{n(n-1)}{2!}x^2 + \frac{n(n-1)(n-2)}{3!}x^3 + \cdots$$

The pattern is: the coefficient of x^k is $\frac{n(n-1)(n-2)\cdots(n-k+1)}{k!}$.

This is valid for |x| < 1.

### Worked Example 3: Expand (1 + x)^(−1) up to x³

**Problem:** Expand (1 + x)^(−1) as far as the term in x³. State when the expansion is valid.

**Approach:** Use n = −1 in the formula.

Coefficient of x: n = −1 → −1.

Coefficient of x²: $\frac{n(n-1)}{2!} = \frac{(-1)(-2)}{2} = \frac{2}{2} = 1$.

Coefficient of x³: $\frac{n(n-1)(n-2)}{3!} = \frac{(-1)(-2)(-3)}{6} = \frac{-6}{6} = -1$.

So: $(1+x)^{-1} = 1 - x + x^2 - x^3 + \cdots$

This is valid for |x| < 1.

**Why this makes sense:** You might recognize this pattern from algebra: $\frac{1}{1+x} = 1 - x + x^2 - x^3 + \cdots$ is the geometric series. The binomial theorem reproduces that familiar result. The signs alternate (positive, negative, positive, negative) because we are multiplying an odd number of negatives for every other term.

### Worked Example 4: Expand √(1 + x) up to x³

**Problem:** Expand √(1 + x), which means (1 + x)^(1/2), up to the term in x³.

**Approach:** Use n = 1/2.

Term 1: 1.

Term 2 (x): $n = \frac{1}{2}$, so coefficient = $\frac{1}{2}$.

Term 3 (x²): $\frac{n(n-1)}{2!} = \frac{\frac{1}{2} \times \left(-\frac{1}{2}\right)}{2} = \frac{-\frac{1}{4}}{2} = -\frac{1}{8}$.

Term 4 (x³): $\frac{n(n-1)(n-2)}{3!} = \frac{\frac{1}{2} \times \left(-\frac{1}{2}\right) \times \left(-\frac{3}{2}\right)}{6} = \frac{\frac{3}{8}}{6} = \frac{3}{48} = \frac{1}{16}$.

So: $\sqrt{1+x} = (1+x)^{1/2} = 1 + \frac{1}{2}x - \frac{1}{8}x^2 + \frac{1}{16}x^3 + \cdots$

This is valid for |x| < 1.

### Worked Example 5: Use the Expansion to Estimate a Value

**Problem:** Use the expansion from Example 4 to estimate √1.04 to three decimal places.

**Approach:** √1.04 = (1 + 0.04)^(1/2). Set x = 0.04 in the expansion.

$\sqrt{1.04} \approx 1 + \frac{1}{2}(0.04) - \frac{1}{8}(0.04)^2 + \frac{1}{16}(0.04)^3$.

Compute term by term:
- Term 1: 1.
- Term 2: 0.5 × 0.04 = 0.02.
- Term 3: 0.125 × 0.0016 = 0.0002. (Since it is subtracted: −0.0002.)
- Term 4: (1/16) × 0.000064 ≈ 0.000004.

Sum: 1 + 0.02 − 0.0002 + 0.000004 = 1.019804.

Rounded to three decimal places: **1.020**.

---

## A Critical IB Trap and How to Avoid It

The formula above works for (1 + x)^n, but what if you are given something like (4 + x)^(1/2)? The base is not 1 — it is 4. You **cannot** just plug 4 + x into the formula directly.

**The fix:** Factor out the constant so the expression starts with 1.

$$(4 + x)^{1/2} = 4^{1/2}\left(1 + \frac{x}{4}\right)^{1/2} = 2\left(1 + \frac{x}{4}\right)^{1/2}$$

Now expand $\left(1 + \frac{x}{4}\right)^{1/2}$ using the formula with n = 1/2 and x replaced by x/4, then multiply everything by 2.

**General rule:** For (a + bx)^n, rewrite as $a^n\left(1 + \frac{b}{a}x\right)^n$, then expand $(1 + \frac{b}{a}x)^n$.

---

## Common Misconceptions

**Misconception 1:** "Binomial coefficients are always whole numbers." For positive integer n, yes — they are always whole numbers because they count combinations. But in the general binomial theorem, the coefficients involve n, n−1, n−2, etc., and can be fractions.

**Misconception 2:** "The expansion for (1 + x)^n always stops." Only when n is a positive integer. For any other n (fraction, negative, irrational), the expansion is an infinite series.

**Misconception 3:** "I can just substitute x = 2 into (1 + x)^(1/2) and get √3." No — the infinite series only converges (settles down to the right answer) when |x| < 1. For x = 2, the terms grow and the series does not work.

**Misconception 4:** "The binomial coefficient and the term coefficient are the same thing." The **binomial coefficient** is $\binom{n}{r}$. The **term coefficient** in (a + bx)^n is $\binom{n}{r} a^{n-r} b^r$. For example, in (2x − 3)^5, the term with x³ has coefficient 720, but the binomial coefficient $\binom{5}{2}$ is only 10. The 720 comes from multiplying 10 by (2)³ and (−3)².

---

## Practice Problems

**1.** Expand (2x − 1)^4 fully. Write the result as a polynomial in x.

**2.** In the expansion of (x + 1/x)^6, find the term that does not contain x (the **constant term**, also called the term independent of x).

**3.** Find the coefficient of x^4 in the expansion of (x + 3)^7. Do not expand the whole thing — target the specific term.

**4.** Expand (1 − x)^(−2) up to the term in x³. State the range of x values for which this expansion is valid.

**5.** Expand √(4 + x) as far as the term in x². (Hint: factor out 4 first, then use the binomial theorem for (1 + x/4)^(1/2).)

**6. [IB Exam Style — 6 marks]** Use the binomial theorem to estimate (1.02)^10 to two decimal places.

(a) Write (1.02)^10 as (1 + x)^n and identify x and n. [1 mark]

(b) Write out the first four terms of the binomial expansion of (1 + x)^n. [2 marks]

(c) Substitute x = 0.02 and compute the sum of these four terms. [2 marks]

(d) Round your result to two decimal places. [1 mark]

---

## Answers

**1.** Using (a + b)^4 with a = 2x, b = −1:
$\binom{4}{0}(2x)^4(-1)^0 = 1 \cdot 16x^4 \cdot 1 = 16x^4$.
$\binom{4}{1}(2x)^3(-1)^1 = 4 \cdot 8x^3 \cdot (-1) = -32x^3$.
$\binom{4}{2}(2x)^2(-1)^2 = 6 \cdot 4x^2 \cdot 1 = 24x^2$.
$\binom{4}{3}(2x)^1(-1)^3 = 4 \cdot 2x \cdot (-1) = -8x$.
$\binom{4}{4}(2x)^0(-1)^4 = 1 \cdot 1 \cdot 1 = 1$.
Answer: $16x^4 - 32x^3 + 24x^2 - 8x + 1$.

**2.** In (x + 1/x)^6, a = x, b = 1/x = x^{−1}. The general term is $\binom{6}{r} x^{6-r} (x^{-1})^r = \binom{6}{r} x^{6-2r}$. We need the exponent of x to be zero: 6 − 2r = 0 → r = 3. The term is $\binom{6}{3} x^0 = 20$. Answer: **20**.

**3.** In (x + 3)^7, the term with x^4 has n − r = 4, so r = 3 (since n = 7). The term is $\binom{7}{3} x^4 (3)^3 = 35 \cdot x^4 \cdot 27 = 945x^4$. Coefficient: **945**.

**4.** n = −2. First four coefficients: r = 0: 1. r = 1: n = −2. r = 2: $\frac{(-2)(-3)}{2!} = \frac{6}{2} = 3$. r = 3: $\frac{(-2)(-3)(-4)}{3!} = \frac{-24}{6} = -4$. But careful — the expression is (1 − x)^(−2), so we replace x in the formula with (−x):
$(1 + (-x))^{-2} = 1 + (-2)(-x) + 3(-x)^2 + (-4)(-x)^3 + \cdots = 1 + 2x + 3x^2 + 4x^3 + \cdots$.
Valid for |−x| < 1, meaning **|x| < 1**.

**5.** $\sqrt{4+x} = 4^{1/2}(1 + x/4)^{1/2} = 2(1 + x/4)^{1/2}$. Expand $(1 + x/4)^{1/2}$ using n = 1/2 and replacing x with x/4:
$(1 + x/4)^{1/2} = 1 + \frac{1}{2}(x/4) - \frac{1}{8}(x/4)^2 + \cdots = 1 + \frac{x}{8} - \frac{x^2}{128} + \cdots$.
Multiply by 2: $\sqrt{4+x} = 2 + \frac{x}{4} - \frac{x^2}{64} + \cdots$.

**6.** (a) (1.02)^10 = (1 + 0.02)^10, so x = 0.02, n = 10. [1 mark]

(b) $(1+x)^{10} = \binom{10}{0} + \binom{10}{1}x + \binom{10}{2}x^2 + \binom{10}{3}x^3 + \cdots = 1 + 10x + 45x^2 + 120x^3 + \cdots$. [2 marks]

(c) Substitute x = 0.02: 1 + 10(0.02) + 45(0.0004) + 120(0.000008) = 1 + 0.2 + 0.018 + 0.00096 = 1.21896. [2 marks]

(d) Rounded to two decimal places: **1.22**. (The exact value of 1.02^10 is approximately 1.218994, so our estimate is very close. The small error comes from the terms we omitted.) [1 mark]
