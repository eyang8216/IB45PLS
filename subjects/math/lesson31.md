# Lesson 31: Proof by Induction — Divisibility and Inequalities

---

## What Is Proof by Induction?

Proof by induction is a method for proving that a statement is true for every counting number (1, 2, 3, …). Think of it like knocking over dominoes. If you can knock over the first domino, and you can show that each domino knocks over the next one, then every domino falls.

An induction proof always has three parts:

- **Base case:** Prove the statement is true for the first number (usually n = 1).
- **Inductive hypothesis:** Assume the statement is true for some number k. This is a temporary assumption used only inside the proof.
- **Inductive step:** Using the assumption that it works for k, prove it must also work for k + 1.

If you complete all three parts, the principle of mathematical induction says the statement is true for all counting numbers.

In this lesson, we apply induction to two new types of statements: **divisibility statements** (like "7ⁿ − 1 is always a multiple of 6") and **inequalities** (like "2ⁿ is greater than n").

---

## Part A: Divisibility Proofs

### What "Divisible" Means

A number A is **divisible** by a number d if there exists some integer m such that A = d × m. In other words, dividing A by d gives a whole number with no remainder. For example, 12 is divisible by 3 because 12 = 3 × 4.

When we prove divisibility by induction, the inductive step uses an algebraic technique: we rewrite the (k+1) case to expose the k case, which we already assumed is divisible.

---

### Worked Example 1: Prove 7ⁿ − 1 Is Divisible by 6

**Statement:** For every counting number n, the expression 7ⁿ − 1 is a multiple of 6.

**Base case (n = 1):**

Compute 7¹ − 1: this equals 7 − 1 = 6. The number 6 is divisible by 6 (since 6 = 6 × 1). The base case holds.

**Inductive hypothesis:**

Assume that 7ᵏ − 1 is divisible by 6 for some counting number k. This means there exists an integer m such that:

$$
7^k - 1 = 6m
$$

**Inductive step:**

We want to show that 7ᵏ⁺¹ − 1 is also divisible by 6.

**Approach:** Start with 7ᵏ⁺¹ − 1 and try to link it to 7ᵏ − 1. Write 7ᵏ⁺¹ as 7 × 7ᵏ.

Then add and subtract 7 (a clever trick to make 7ᵏ − 1 appear):

$$
\begin{aligned}
7^{k+1} - 1 &= 7 \cdot 7^k - 1 \\
&= 7 \cdot 7^k - 7 + 7 - 1 \\
&= 7(7^k - 1) + 6
\end{aligned}
$$

Now substitute the hypothesis 7ᵏ − 1 = 6m:

$$
7^{k+1} - 1 = 7(6m) + 6 = 6(7m + 1)
$$

The right-hand side is 6 multiplied by the integer (7m + 1). So 7ᵏ⁺¹ − 1 is divisible by 6.

Since the base case works and the inductive step works, 7ⁿ − 1 is divisible by 6 for all counting numbers n. ✓

**Why this makes sense:** The "add and subtract" trick creates a copy of 7ᵏ − 1, which we know is a multiple of 6. The leftover piece (6) is also a multiple of 6. Adding two multiples of 6 gives another multiple of 6.

**Common misconception:** Students sometimes write 7ᵏ⁺¹ − 1 = 7(7ᵏ) − 1 and get stuck. The key is to force the term (7ᵏ − 1) to appear inside the expression. Adding and subtracting the same number is a legitimate algebraic move because it does not change the value.

---

### Worked Example 2: Prove 3²ⁿ − 1 Is Divisible by 8

**Statement:** For every counting number n, the expression 3²ⁿ − 1 is a multiple of 8.

First, notice that 3²ⁿ = (3²)ⁿ = 9ⁿ. This makes the algebra easier.

**Base case (n = 1):**

3² − 1 = 9 − 1 = 8. The number 8 is divisible by 8. ✓

**Inductive hypothesis:**

Assume 3²ᵏ − 1 = 8m for some integer m.

**Inductive step:**

We need to show that 3²⁽ᵏ⁺¹⁾ − 1 is divisible by 8.

**Approach:** Write 3²⁽ᵏ⁺¹⁾ as 3²ᵏ × 3² = 9 × 3²ᵏ.

Then add and subtract 9 to expose 3²ᵏ − 1:

$$
\begin{aligned}
3^{2(k+1)} - 1 &= 3^{2k+2} - 1 \\
&= 3^{2k} \cdot 3^2 - 1 \\
&= 9 \cdot 3^{2k} - 1 \\
&= 9 \cdot 3^{2k} - 9 + 9 - 1 \\
&= 9(3^{2k} - 1) + 8
\end{aligned}
$$

Now substitute the hypothesis 3²ᵏ − 1 = 8m:

$$
3^{2(k+1)} - 1 = 9(8m) + 8 = 8(9m + 1)
$$

Since 9m + 1 is an integer, the expression is 8 times an integer, so it is divisible by 8. ✓

**Why this makes sense:** The algebraic structure is the same as Example 1. We find the right number to add and subtract (9 in this case, because 9 = 3² is the multiplier in front of 3²ᵏ). This creates the block (3²ᵏ − 1) which we know is a multiple of 8, plus a remainder of 8, which is also a multiple of 8.

---

### Worked Example 3: Prove n³ − n Is Divisible by 3

**Statement:** For every counting number n, the expression n³ − n is a multiple of 3.

**Base case (n = 1):**

1³ − 1 = 0. The number 0 is divisible by 3 (0 = 3 × 0). ✓

**Inductive hypothesis:**

Assume k³ − k = 3m for some integer m.

**Inductive step:**

**Approach:** Expand (k+1)³ fully, then rearrange to find k³ − k inside.

First expand (k+1)³:

(k+1)³ = k³ + 3k² + 3k + 1

Now compute (k+1)³ − (k+1):

$$
\begin{aligned}
(k+1)^3 - (k+1) &= (k^3 + 3k^2 + 3k + 1) - k - 1 \\
&= k^3 + 3k^2 + 3k + 1 - k - 1 \\
&= k^3 + 3k^2 + 2k
\end{aligned}
$$

Now we want to see k³ − k somewhere. Write 2k as 3k − k:

$$
k^3 + 3k^2 + 2k = k^3 + 3k^2 + 3k - k = (k^3 - k) + 3k^2 + 3k
$$

Factor 3 from the last two terms:

(k³ − k) + 3(k² + k)

Now substitute k³ − k = 3m from the hypothesis:

3m + 3(k² + k) = 3(m + k² + k)

This is 3 times an integer, so (k+1)³ − (k+1) is divisible by 3. ✓

**Why this makes sense:** When we expand (k+1)³, we get k³ plus extra terms. Subtracting (k+1) isolates k³ − k and leaves behind terms that all have a factor of 3. The induction hypothesis handles k³ − k, and the remaining terms are clearly multiples of 3.

**Pitfall alert:** When you expand (k+1)³, be careful with signs. The subtraction of (k+1) means you subtract both k and 1. Students sometimes forget to subtract the 1.

---

## Part B: Inequality Proofs

### The Idea

When proving inequalities by induction, the inductive step is different from divisibility. Instead of showing that something is a multiple, we build a chain of inequalities. We start with the (k+1) expression, relate it to the k expression, apply the hypothesis, and keep comparing until we reach the desired inequality.

A common technique: we may need to prove a small "helper inequality" on the side (for example, showing that 2k ≥ k+1 when k ≥ 1).

---

### Worked Example 4: Prove 2ⁿ > n for All n ≥ 1

**Statement:** For every counting number n, the number 2 raised to the power n is greater than n itself.

**Base case (n = 1):**

2¹ = 2, and 2 > 1, so the statement holds. ✓

**Inductive hypothesis:**

Assume 2ᵏ > k for some counting number k.

**Inductive step:**

We need to show that 2ᵏ⁺¹ > k + 1.

**Approach:** Write 2ᵏ⁺¹ as 2 × 2ᵏ. Then apply the hypothesis.

$$
2^{k+1} = 2 \cdot 2^k
$$

Since we know 2ᵏ > k (by the hypothesis), multiplying both sides by the positive number 2 preserves the inequality:

$$
2 \cdot 2^k > 2 \cdot k
$$

So 2ᵏ⁺¹ > 2k.

Now we ask: is 2k at least as big as k + 1? Since k ≥ 1, we have k + k ≥ k + 1, which means 2k ≥ k + 1.

Chaining these together:

$$
2^{k+1} > 2k \geq k + 1
$$

Therefore 2ᵏ⁺¹ > k + 1. ✓

**Why this makes sense:** Multiplying the hypothesis by 2 gives us 2ᵏ⁺¹ > 2k. Then we compare 2k with k+1. For any k ≥ 1, doubling k gives a number that is at least k+1 (since k ≥ 1 implies k + k ≥ k + 1). The chain of inequalities completes the proof.

---

### Worked Example 5: Prove 2ⁿ > n² for n ≥ 5

**Statement:** For every integer n greater than or equal to 5, the number 2ⁿ is greater than n².

Notice that the base case here starts at n = 5, not n = 1. Induction can start at any integer.

**Base case (n = 5):**

2⁵ = 32, and 5² = 25. Since 32 > 25, the statement holds. ✓

**Inductive hypothesis:**

Assume 2ᵏ > k² for some integer k ≥ 5.

**Inductive step:**

We need to show 2ᵏ⁺¹ > (k+1)².

**Approach:** Write 2ᵏ⁺¹ as 2 × 2ᵏ, apply the hypothesis, then compare 2k² with (k+1)².

$$
2^{k+1} = 2 \cdot 2^k > 2 \cdot k^2 \quad \text{(by the hypothesis)}
$$

Now we have 2ᵏ⁺¹ > 2k². If we can show that 2k² ≥ (k+1)² for k ≥ 5, then we can conclude 2ᵏ⁺¹ > (k+1)².

Let's check when 2k² ≥ (k+1)² holds. Expand (k+1)²:

(k+1)² = k² + 2k + 1

So we need:

$$
2k^2 \geq k^2 + 2k + 1
$$

Subtract k² from both sides:

$$
k^2 \geq 2k + 1
$$

Subtract 2k + 1 from both sides:

$$
k^2 - 2k - 1 \geq 0
$$

Rewrite as (k − 1)² − 2 ≥ 0, or (k − 1)² ≥ 2.

For k ≥ 3, we have k − 1 ≥ 2, so (k − 1)² ≥ 4, which is certainly ≥ 2. Since our k is at least 5, this condition is satisfied.

Thus 2k² ≥ (k+1)² for all k ≥ 5. Chaining:

$$
2^{k+1} > 2k^2 \geq (k+1)^2
$$

Therefore 2ᵏ⁺¹ > (k+1)². ✓

**Why this makes sense:** The helper inequality 2k² ≥ (k+1)² is the crucial step. It is not true for small k (try k = 2: 2×4 = 8, but 3² = 9). This is why the statement itself is false for n = 2, 3, and 4 — and why the base case must start at n = 5. The induction proof captures exactly where the statement becomes true and stays true.

**Common misconception:** Students sometimes try to prove 2ⁿ > n² starting from n = 1. It fails at n = 2 (2² = 4 = 2², not greater) and n = 3 (2³ = 8 < 9 = 3²) and n = 4 (2⁴ = 16 = 4², not greater). The statement only becomes true at n = 5. Always check where the statement first becomes true and set your base case there.

---

## Practice Problems

---

### Problem 1
Prove by induction that 5ⁿ − 1 is divisible by 4 for every counting number n. Write out all three parts clearly: base case, inductive hypothesis, and inductive step.

---

### Problem 2
Prove by induction that 11ⁿ − 6 is divisible by 5 for every counting number n. In the inductive step, explain your choice of what number to add and subtract.

---

### Problem 3
Prove by induction that n(n² + 5) is divisible by 6 for every counting number n. *Hint: after expanding (k+1)((k+1)² + 5), try to isolate k(k² + 5) and then show the remaining terms are also multiples of 6. You may need to note that the product of two consecutive integers is always even.*

---

### Problem 4
Prove by induction that 3ⁿ > 2ⁿ for every counting number n. Your inductive step should involve multiplying an inequality by a positive number.

---

### Problem 5 (IB Exam Style — 7 marks)
A sequence is defined by the statement P(n): n! > 2ⁿ for integers n ≥ 4.

(a) [1 mark] Show that P(4) is true.

(b) [1 mark] Write down the inductive hypothesis for P(k), where k ≥ 4.

(c) [5 marks] Prove by induction that n! > 2ⁿ for all integers n ≥ 4. In your inductive step, clearly state any additional inequality you use and justify why it holds for k ≥ 4.

---

### Problem 6
Prove Bernoulli's inequality: (1 + x)ⁿ ≥ 1 + nx for every counting number n and every real number x > −1.

In the inductive step, you will multiply both sides of the hypothesis by (1 + x). Pay attention to the sign of (1 + x) — explain why the inequality direction is preserved.

---

## Answers

---

### Answer 1

Let P(n) be the statement "5ⁿ − 1 is divisible by 4."

**Base case (n = 1):** 5¹ − 1 = 4. Since 4 = 4 × 1, the statement is true for n = 1.

**Inductive hypothesis:** Assume P(k) is true for some k. That is, 5ᵏ − 1 = 4m for some integer m.

**Inductive step:** Consider 5ᵏ⁺¹ − 1.

Write 5ᵏ⁺¹ = 5 × 5ᵏ. Then add and subtract 5:

$$
5^{k+1} - 1 = 5 \cdot 5^k - 5 + 5 - 1 = 5(5^k - 1) + 4
$$

Substitute 5ᵏ − 1 = 4m:

$$
5(4m) + 4 = 4(5m + 1)
$$

This is 4 times the integer (5m + 1), so 5ᵏ⁺¹ − 1 is divisible by 4. Thus P(k+1) is true.

**Why it works:** Adding and subtracting 5 creates the factor (5ᵏ − 1) which the hypothesis tells us is 4m. The leftover 4 is also a multiple of 4. Their sum is a multiple of 4.

---

### Answer 2

Let P(n) be "11ⁿ − 6 is divisible by 5."

**Base case (n = 1):** 11¹ − 6 = 5, which equals 5 × 1. True.

**Inductive hypothesis:** 11ᵏ − 6 = 5m for some integer m.

**Inductive step:** Write 11ᵏ⁺¹ = 11 × 11ᵏ.

We need to add and subtract a number that makes (11ᵏ − 6) appear. Since we have 11 × 11ᵏ, we want 11 × 6 = 66:

$$
11^{k+1} - 6 = 11 \cdot 11^k - 6 = 11 \cdot 11^k - 66 + 66 - 6 = 11(11^k - 6) + 60
$$

Substitute 11ᵏ − 6 = 5m:

$$
11(5m) + 60 = 5(11m) + 5 \cdot 12 = 5(11m + 12)
$$

This is 5 times an integer, so 11ᵏ⁺¹ − 6 is divisible by 5. ✓

**Why add and subtract 66?** We have 11 × 11ᵏ. To expose (11ᵏ − 6), we need 11 × (−6) = −66. So we write 11 × 11ᵏ − 66 + 60, which equals the original 11 × 11ᵏ − 6 because −66 + 60 = −6.

---

### Answer 3

Let P(n) be "n(n² + 5) is divisible by 6."

**Base case (n = 1):** 1 × (1 + 5) = 6. Since 6 = 6 × 1, true.

**Inductive hypothesis:** k(k² + 5) = 6m for some integer m.

**Inductive step:** Compute (k+1)((k+1)² + 5).

First, (k+1)² = k² + 2k + 1, so (k+1)² + 5 = k² + 2k + 6.

Now multiply:

$$
(k+1)(k^2 + 2k + 6) = (k+1)(k^2 + 5 + 2k + 1)
$$

We can separate the (k² + 5) part:

$$
(k+1)(k^2 + 5) + (k+1)(2k + 1)
$$

Expand the first part: (k+1)(k² + 5) = k(k² + 5) + (k² + 5).

The second part: (k+1)(2k + 1) = 2k² + k + 2k + 1 = 2k² + 3k + 1.

Add everything together:

$$
k(k^2 + 5) + (k^2 + 5) + (2k^2 + 3k + 1) = k(k^2 + 5) + 3k^2 + 3k + 6
$$

Factor 3 from the middle terms:

$$
k(k^2 + 5) + 3k(k+1) + 6
$$

Now substitute k(k² + 5) = 6m:

$$
6m + 3k(k+1) + 6
$$

The term k(k+1) is the product of two consecutive integers. One of any two consecutive integers is even, so k(k+1) is even — it equals 2t for some integer t. Then 3k(k+1) = 3 × 2t = 6t, which is divisible by 6.

The term 6 is also divisible by 6. And 6m is divisible by 6. The sum of three multiples of 6 is a multiple of 6. Therefore the whole expression is divisible by 6.

**Pitfall:** Students sometimes try to directly factor 6 out of 3k(k+1) and fail because 3k(k+1) does not look like a multiple of 6 at first glance. The key insight is that k(k+1) is always even, so 3 times an even number is a multiple of 6.

---

### Answer 4

Let P(n) be "3ⁿ > 2ⁿ."

**Base case (n = 1):** 3¹ = 3, 2¹ = 2. Since 3 > 2, P(1) is true.

**Inductive hypothesis:** 3ᵏ > 2ᵏ for some k.

**Inductive step:** Write 3ᵏ⁺¹ = 3 × 3ᵏ.

By the hypothesis, 3ᵏ > 2ᵏ. Since 3 is positive, multiplying both sides by 3 preserves the inequality:

3 × 3ᵏ > 3 × 2ᵏ, so 3ᵏ⁺¹ > 3 × 2ᵏ.

Now 3 × 2ᵏ is certainly greater than 2 × 2ᵏ (because 3 > 2 and 2ᵏ is positive). And 2 × 2ᵏ = 2ᵏ⁺¹.

Chaining: 3ᵏ⁺¹ > 3 × 2ᵏ > 2 × 2ᵏ = 2ᵏ⁺¹.

Therefore 3ᵏ⁺¹ > 2ᵏ⁺¹. ✓

**Why it works:** The hypothesis gives us a direct comparison between 3ᵏ and 2ᵏ. Multiplying by 3 on one side and then comparing to 2ᵏ⁺¹ uses the fact that 3 × 2ᵏ > 2 × 2ᵏ = 2ᵏ⁺¹.

**Common misconception:** Some students write 3ᵏ⁺¹ = 3 × 3ᵏ > 3 × 2ᵏ and then claim this equals 6ᵏ, which is wrong. 3 × 2ᵏ is not 6ᵏ. The exponent belongs only to the 2, not to the 3.

---

### Answer 5

(a) P(4): 4! = 24, and 2⁴ = 16. Since 24 > 16, P(4) is true. [1 mark]

(b) Inductive hypothesis: Assume k! > 2ᵏ for some integer k ≥ 4. [1 mark]

(c) **Inductive step** [5 marks]:

We need to prove (k+1)! > 2ᵏ⁺¹.

Write (k+1)! = (k+1) × k!.

By the hypothesis, k! > 2ᵏ. Since (k+1) is positive, multiply both sides by (k+1):

(k+1) × k! > (k+1) × 2ᵏ

So (k+1)! > (k+1) × 2ᵏ.

Now, since k ≥ 4, we have k + 1 ≥ 5, and 5 > 2. Therefore (k+1) × 2ᵏ > 2 × 2ᵏ = 2ᵏ⁺¹.

Chaining: (k+1)! > (k+1) × 2ᵏ > 2 × 2ᵏ = 2ᵏ⁺¹.

Thus (k+1)! > 2ᵏ⁺¹. ✓

Since P(4) is true and P(k) ⇒ P(k+1) for all k ≥ 4, by induction n! > 2ⁿ for all n ≥ 4.

**Why the condition k ≥ 4 matters:** The step (k+1) × 2ᵏ > 2 × 2ᵏ requires k+1 > 2, which is true for k ≥ 2. However, the statement n! > 2ⁿ is false for n = 2 (2! = 2 = 2², not greater) and n = 3 (3! = 6 < 8 = 2³). The base case at n = 4 is the first place where the statement becomes true.

---

### Answer 6

Let P(n) be "(1 + x)ⁿ ≥ 1 + nx" for x > −1.

**Base case (n = 1):** (1 + x)¹ = 1 + x = 1 + 1×x. The equality holds, so P(1) is true.

**Inductive hypothesis:** (1 + x)ᵏ ≥ 1 + kx for some k.

**Inductive step:** Write (1 + x)ᵏ⁺¹ = (1 + x)(1 + x)ᵏ.

Multiply both sides of the hypothesis by (1 + x). Note: since x > −1, we have 1 + x > 0, so multiplying by (1 + x) does not flip the inequality direction.

(1 + x)(1 + x)ᵏ ≥ (1 + x)(1 + kx)

Now expand the right-hand side:

(1 + x)(1 + kx) = 1 + kx + x + kx² = 1 + (k+1)x + kx²

Since kx² ≥ 0 (k is a positive integer and x² is non-negative), we have:

1 + (k+1)x + kx² ≥ 1 + (k+1)x

Chaining: (1 + x)ᵏ⁺¹ ≥ 1 + (k+1)x + kx² ≥ 1 + (k+1)x.

Thus (1 + x)ᵏ⁺¹ ≥ 1 + (k+1)x. ✓

**Why x > −1 matters:** If x were less than −1, then 1 + x would be negative. Multiplying an inequality by a negative number flips the direction, and the proof would break. The condition x > −1 guarantees that 1 + x is positive, so the inequality direction is preserved when we multiply.

