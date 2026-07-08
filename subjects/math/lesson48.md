# Lesson 48: Reciprocal and Inverse Trigonometric Functions

## What Is This Topic?

The trigonometric functions you already know — sine, cosine, and tangent — each have a **reciprocal function** and an **inverse function**. These are two very different ideas that share confusingly similar notation, so we will keep them separate.

A **reciprocal function** flips a fraction: the reciprocal of a number a is 1/a. So the reciprocal of sin x is 1/sin x, which we call **cosecant**, written **csc x** or cosec x. Similarly, **secant (sec x)** is 1/cos x, and **cotangent (cot x)** is 1/tan x, which also equals cos x / sin x.

An **inverse function** undoes the original function: if sin θ = 0.5, the inverse sine tells you that θ = 30° (or π/6). The inverse sine is written **arcsin x** (or sin⁻¹ x). The notation sin⁻¹ x does **not** mean 1/sin x — this is the single biggest source of confusion in this topic.

## Why Do We Learn This?

Reciprocal trig functions simplify many formulas in calculus and physics. For example, the derivative of tan x is sec²x — a very clean result. Inverse trig functions let you solve for an angle when you know its sine, cosine, or tangent value, and they appear in integration formulas such as ∫ 1/√(1 − x²) dx = arcsin x + C.

In the IB exam, you must know the definitions, graphs, domain and range, key identities, and basic derivatives of these functions.

---

## 1. Reciprocal Trigonometric Functions

### Definitions

For any angle x (except where the denominator is zero):

- **Secant:** sec x = 1 / cos x
- **Cosecant:** csc x = 1 / sin x
- **Cotangent:** cot x = 1 / tan x = cos x / sin x

### Domain and Range

Every trig function has values of x where it is undefined (where the denominator equals zero). A function's **domain** is the set of x‑values where the function exists; its **range** is the set of output values the function can produce.

| Function | Domain (where it exists) | Range |
|---|---|---|
| sec x | x ≠ π/2 + nπ (where cos x = 0) | (−∞, −1] ∪ [1, ∞) |
| csc x | x ≠ nπ (where sin x = 0) | (−∞, −1] ∪ [1, ∞) |
| cot x | x ≠ nπ (where sin x = 0) | all real numbers (ℝ) |

The range of sec x and csc x never includes numbers between −1 and 1. Think about why: if cos x is a small fraction, sec x = 1/cos x becomes a large number. The smallest absolute value sec x can ever have is 1 (when cos x = ±1).

### Key Exact Values Worth Remembering

- sec 0 = 1 (because cos 0 = 1, and 1/1 = 1)
- sec π/3 = 2 (because cos π/3 = 1/2, and 1/(1/2) = 2)
- sec π/2 is undefined (cos π/2 = 0, and you cannot divide by zero)
- csc π/6 = 2 (because sin π/6 = 1/2)
- csc π/2 = 1 (because sin π/2 = 1)
- cot π/4 = 1 (because tan π/4 = 1)
- cot π/2 = 0 (because cos π/2 = 0 and sin π/2 = 1, so 0/1 = 0)

---

## 2. Identities Involving Reciprocal Functions

From the Pythagorean identity sin²x + cos²x = 1, we can derive two more identities by dividing through by cos²x or sin²x.

Divide sin²x + cos²x = 1 by **cos²x**:

sin²x/cos²x + cos²x/cos²x = 1/cos²x → tan²x + 1 = sec²x.

Divide sin²x + cos²x = 1 by **sin²x**:

sin²x/sin²x + cos²x/sin²x = 1/sin²x → 1 + cot²x = csc²x.

These are the **Pythagorean identities for reciprocal functions**, and they are used constantly in proofs and in solving equations.

### Example 1: Prove that sec²x + csc²x = sec²x · csc²x.

**Problem:** Show that the sum sec²x + csc²x is always equal to the product sec²x · csc²x, for any x where both sides are defined.

**Approach:** Convert everything to sines and cosines, find a common denominator, and simplify using sin²x + cos²x = 1.

Left‑hand side = 1/cos²x + 1/sin²x.

Write with a common denominator sin²x cos²x:

Numerator = sin²x + cos²x = 1.

So LHS = 1 / (sin²x cos²x).

Right‑hand side = sec²x · csc²x = (1/cos²x)·(1/sin²x) = 1/(sin²x cos²x).

Both sides equal the same expression. The identity is proved.

**Why this makes sense:** Rewriting everything as sines and cosines reveals the hidden structure. Many reciprocal‑function proofs reduce to the basic Pythagorean identity.

---

## 3. Solving Equations with Reciprocal Functions

When you see sec, csc, or cot in an equation, rewrite them as 1/cos, 1/sin, or cos/sin — then solve as usual.

### Example 2: Solve sec x = 2 for 0 ≤ x ≤ 2π.

**Problem:** Find all angles x in [0, 2π] whose secant equals 2.

**Approach:** Convert to cosine: sec x = 2 means 1/cos x = 2, so cos x = 1/2. Then solve the basic cosine equation.

cos x = 1/2 → principal value = π/3. The second solution in [0, 2π) is 2π − π/3 = 5π/3.

**Answer:** x = π/3, 5π/3.

**Why this makes sense:** Taking the reciprocal of both sides converts an unfamiliar secant equation into a familiar cosine equation.

### Example 3: Solve cot x = −1 for 0 ≤ x ≤ 2π.

**Problem:** Find all angles x in [0, 2π] for which cot x equals −1.

**Approach:** cot x = −1 means cos x/sin x = −1, which means tan x = −1 (since cot is the reciprocal of tan). Solve tan x = −1.

The principal value for tan x = −1 is −π/4. Adding π brings it into [0, 2π): −π/4 + π = 3π/4. The next solution: 3π/4 + π = 7π/4.

**Answer:** x = 3π/4, 7π/4.

**Why this makes sense:** Cotangent is negative when sine and cosine have opposite signs — quadrants II and IV. The angles 3π/4 (QII) and 7π/4 (QIV) match this expectation.

---

## 4. Inverse Trigonometric Functions

### The Big Idea

The sine function takes an angle and gives a number between −1 and 1. The **inverse sine** (written arcsin x or sin⁻¹ x) does the opposite: it takes a number between −1 and 1 and gives the angle whose sine is that number.

But here is the problem: sin(π/6) = 1/2, and sin(5π/6) = 1/2, and sin(13π/6) = 1/2, and so on forever. If arcsin(1/2) had to return *every* possible angle, it would not be a function (a function must give exactly one output for each input).

To fix this, mathematicians **restrict the range** of each inverse function so that it returns only one angle — the **principal value**.

### Definitions and Restricted Ranges

| Function | Domain (allowed x) | Range (output angle) |
|---|---|---|
| arcsin x (or sin⁻¹ x) | [−1, 1] | [−π/2, π/2] |
| arccos x (or cos⁻¹ x) | [−1, 1] | [0, π] |
| arctan x (or tan⁻¹ x) | all real numbers (ℝ) | (−π/2, π/2) |

**Crucial warning:** arcsin x does NOT mean 1/sin x. It means "the angle whose sine is x." The notation sin⁻¹ x is unfortunately ambiguous, and many students mistake it for a power of −1. The IB uses both arcsin and sin⁻¹; you must treat them as the inverse function, not the reciprocal.

### Common Misconceptions

Many students write arcsin(1/2) = π/6 and 5π/6. But arcsin only returns the principal value — π/6. The 5π/6 is outside arcsin's range of [−π/2, π/2].

Similarly, many students think arccos(−1/2) = 4π/3, but the range of arccos is [0, π], so the correct answer is 2π/3.

### Worked Evaluations

- arcsin(1/2) = π/6. Why? Because sin(π/6) = 1/2 and π/6 is in [−π/2, π/2].
- arccos(−1/2) = 2π/3. Why? Because cos(2π/3) = −1/2 and 2π/3 is in [0, π].
- arctan(1) = π/4. Because tan(π/4) = 1 and π/4 is in (−π/2, π/2).
- arctan(−√3) = −π/3. Because tan(−π/3) = −√3 and −π/3 is in (−π/2, π/2).

---

## 5. Compositions — e.g. cos(arcsin x)

A common IB question asks you to evaluate something like cos(arcsin(3/5)). The strategy: name the inner angle, draw a right triangle, and use Pythagoras.

### Example 4: Evaluate cos(arcsin(3/5)).

**Problem:** Find the exact value of cos(θ) where θ = arcsin(3/5).

**Approach:** Let θ = arcsin(3/5). By definition, sin θ = 3/5 and θ is in [−π/2, π/2] (arcsin's range). In that range, cosine is never negative, so we expect a positive answer.

Draw a right triangle with opposite side 3 and hypotenuse 5. By the Pythagorean theorem, the adjacent side = √(5² − 3²) = √(25 − 9) = √16 = 4.

cos θ = adjacent / hypotenuse = 4/5.

**Answer:** 4/5.

**Why this makes sense:** The triangle method works because arcsin's range keeps θ in a region where both sine and cosine behave in a standard "right‑triangle" way. Always check that your sign matches the quadrant dictated by the inverse function's range.

### Example 5: Evaluate sin(arccos(−1/3)).

**Problem:** Find the exact value of sin(θ) where θ = arccos(−1/3).

**Approach:** Let θ = arccos(−1/3). Then cos θ = −1/3 and θ is in [0, π] (arccos's range). In [0, π], sine is always positive (or zero), so the answer will be positive.

Using sin²θ + cos²θ = 1: sin²θ = 1 − (−1/3)² = 1 − 1/9 = 8/9. So sin θ = √(8/9) = 2√2/3.

**Answer:** 2√2/3.

**Why this makes sense:** We did not need to draw a triangle here because the identity sin²θ + cos²θ = 1 directly links sine and cosine. Always decide whether a triangle or the identity is faster. Both work; choose the one that feels clearer to you.

---

## 6. Derivatives of Inverse Trigonometric Functions (IB HL)

The derivatives of arcsin, arccos, and arctan are standard results that you should memorize. They also appear in reverse when you integrate.

- d/dx [arcsin x] = 1 / √(1 − x²)
- d/dx [arccos x] = −1 / √(1 − x²)
- d/dx [arctan x] = 1 / (1 + x²)

Notice that the derivative of arccos is simply the negative of the derivative of arcsin. The derivative of arctan is a rational function with no square root, which makes it especially nice.

These formulas are why ∫ 1/√(1 − x²) dx = arcsin x + C and ∫ 1/(1 + x²) dx = arctan x + C appear in your integration toolkit.

---

## Practice Problems

**Problem 1:** Solve csc x = 2 for all angles x in the interval [0, 2π].

**Problem 2:** Simplify the expression (sec x − tan x)(sec x + tan x). What identity does this connect to?

**Problem 3:** Evaluate sec(π/4) and cot(π/3). Give exact values (with square roots, not decimals).

**Problem 4:** Evaluate tan(arccos(1/3)). Use the triangle method and give an exact answer.

**Problem 5 (IB Exam Style — 5 marks):**
(a) State the domain and range of f(x) = arcsin(2x − 1). [2 marks]
(b) Solve the equation arcsin(2x − 1) = π/6. [2 marks]
(c) Hence state the value of f⁻¹(π/6). [1 mark]

**Problem 6:** Find the derivative of f(x) = arctan(2x). Show each step.

---

## Answers

**Answer 1:** csc x = 2 means 1/sin x = 2, so sin x = 1/2. The two solutions in [0, 2π] are π/6 and 5π/6. **Pitfall:** some students try to solve csc x = 2 by thinking of arcsin — but csc is the reciprocal, not the inverse. Always convert to sin, cos, or tan first.

**Answer 2:** This is a difference of squares: (sec x − tan x)(sec x + tan x) = sec²x − tan²x. Using the identity sec²x = 1 + tan²x, we get sec²x − tan²x = (1 + tan²x) − tan²x = 1. This is the reciprocal‑function analogue of the basic Pythagorean identity. The expression always simplifies to 1 (where defined).

**Answer 3:** sec(π/4) = 1/cos(π/4) = 1/(√2/2) = 2/√2 = √2.

cot(π/3) = cos(π/3)/sin(π/3) = (1/2)/(√3/2) = 1/√3 = √3/3 (rationalized).

**Answer 4:** Let θ = arccos(1/3). Then cos θ = 1/3 and θ is in [0, π], so sin θ is positive. Draw a right triangle: adjacent = 1, hypotenuse = 3, so opposite = √(3² − 1²) = √8 = 2√2. Then tan θ = opposite/adjacent = 2√2 / 1 = 2√2.

**Answer 5:**
(a) arcsin accepts inputs in [−1, 1], so we need −1 ≤ 2x − 1 ≤ 1. Add 1: 0 ≤ 2x ≤ 2. Divide by 2: 0 ≤ x ≤ 1. Domain: [0, 1]. Range: arcsin always outputs [−π/2, π/2], regardless of the expression inside — as long as the expression stays in [−1, 1].

(b) arcsin(2x − 1) = π/6 means sin(π/6) = 2x − 1, so 1/2 = 2x − 1 → 2x = 3/2 → x = 3/4.

(c) Since f(3/4) = π/6, the inverse function gives f⁻¹(π/6) = 3/4.

**Answer 6:** Use the chain rule. Let u = 2x, so f(x) = arctan(u). d/dx [arctan(u)] = 1/(1 + u²) · du/dx.

du/dx = 2, so f '(x) = 1/(1 + (2x)²) · 2 = 2/(1 + 4x²).
