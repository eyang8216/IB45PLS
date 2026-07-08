# Lesson 36: The Binomial Distribution

---

## What Is the Binomial Distribution and Why Do We Need It?

Suppose you flip a coin 10 times and count how many heads you get. Or a factory inspects 20 items and counts how many are defective. Or you guess on 12 multiple-choice questions and want to know your chance of passing. All of these have the same underlying structure: a fixed number of independent trials, each with two possible outcomes (success or failure), and the same probability of success on every trial.

The **binomial distribution** is the probability distribution that describes exactly this situation. Instead of listing every possible sequence of outcomes (which gets impossible as the number of trials grows), the binomial formula gives a shortcut to compute the probability of getting any specific number of successes.

---

## What Is a Bernoulli Trial?

A **Bernoulli trial** (named after the Swiss mathematician Jacob Bernoulli) is the simplest possible random experiment: it has exactly two outcomes. We call one outcome a **success** (coded as 1) and the other a **failure** (coded as 0).

The probability of success is a number p between 0 and 1. The probability of failure is q = 1 − p.

**Examples of Bernoulli trials:**

- Flipping a fair coin: heads is a success, p = 0.5.
- Rolling a die and checking for a 6: rolling a 6 is a success, p = 1/6.
- Inspecting a product: finding it defective is a success (if that is what we are counting), p = 0.02.

---

## The Binomial Setting — Four Conditions

A random variable X follows a **binomial distribution** if all four of these conditions are satisfied:

1. **Fixed number of trials:** There is a specific number n of Bernoulli trials.
2. **Independent trials:** The outcome of one trial does not affect any other trial.
3. **Two outcomes per trial:** Each trial results in either success or failure.
4. **Constant probability:** The probability of success p is the same for every trial.

When these conditions hold, we write:

$$X \sim B(n, p)$$

This notation means "X follows a binomial distribution with n trials and success probability p." The symbol ∼ is read as "is distributed as."

---

## The Binomial Probability Formula

If X ~ B(n, p), the probability of getting exactly k successes is:

$$\boxed{P(X = k) = \binom{n}{k}\, p^k (1-p)^{n-k}, \quad k = 0, 1, 2, \ldots, n}$$

Let's break down what each piece means:

- **pᵏ:** The probability that k specific trials are all successes. Since each success has probability p and trials are independent, we multiply p by itself k times: pᵏ.
- **(1−p)ⁿ⁻ᵏ:** The probability that the remaining n−k trials are all failures. Each failure has probability (1−p), and there are n−k of them: (1−p)ⁿ⁻ᵏ.
- **\binom{n}{k}:** The **binomial coefficient**, read as "n choose k." It counts how many different ways we can select which k of the n trials will be the successes.

The binomial coefficient is calculated as:

$$\binom{n}{k} = \frac{n!}{k!(n-k)!}$$

where n! (n factorial) means n × (n−1) × (n−2) × … × 2 × 1. For example, 5! = 5 × 4 × 3 × 2 × 1 = 120.

---

## Worked Example 1: Fair Coin Tosses

**Problem:** A fair coin is tossed 10 times. Let X be the number of heads. Find the probability of getting exactly 6 heads.

**Approach:** The four binomial conditions are all met: n = 10 fixed tosses, tosses are independent, two outcomes per toss (heads or tails), and p = 0.5 for every toss. So X ~ B(10, 0.5).

**Step 1: Identify the values.** n = 10, k = 6, p = 0.5.

**Step 2: Compute the binomial coefficient.**

$$\binom{10}{6} = \frac{10!}{6!\,4!} = \frac{10 \times 9 \times 8 \times 7}{4 \times 3 \times 2 \times 1} = \frac{5040}{24} = 210$$

**Step 3: Plug into the formula.**

$$P(X = 6) = 210 \times (0.5)^6 \times (0.5)^4 = 210 \times (0.5)^{10}$$

Since (0.5)¹⁰ = 1/1024:

$$P(X = 6) = \frac{210}{1024} = \frac{105}{512} \approx 0.2051$$

**Interpretation:** If you toss a fair coin 10 times, you have about a 20.5% chance of getting exactly 6 heads. This is one of the more likely outcomes because 6 is close to the expected value (which is 10 × 0.5 = 5).

**Why this makes sense:** There are 210 different sequences of 10 coin tosses that contain exactly 6 heads (think HHHHHHTTTT, HHHHHTHTTT, and 208 others). Each sequence has probability (0.5)¹⁰ = 1/1024. So the total probability is 210/1024.

---

## Worked Example 2: Defective Products

**Problem:** A machine produces items with a 5% defect rate. In a random sample of 20 items, let X be the number of defective items.

(a) Find the probability of exactly 2 defective items.
(b) Find the probability of at most 1 defective.
(c) Find the probability of at least 1 defective.

**Approach:** The sample is random and each item is independent. n = 20, p = 0.05.

**(a) Exactly 2 defectives:**

$$P(X = 2) = \binom{20}{2}(0.05)^2(0.95)^{18}$$

Compute the binomial coefficient: \binom{20}{2} = 20×19/2 = 190.

(0.05)² = 0.0025.

Now (0.95)¹⁸ can be computed with a calculator: approximately 0.3972.

P(X = 2) ≈ 190 × 0.0025 × 0.3972 ≈ 0.1887.

So about an 18.9% chance of exactly 2 defectives.

**(b) At most 1 defective:**

"At most 1" means 0 or 1. We add the two probabilities:

P(X ≤ 1) = P(X = 0) + P(X = 1).

P(X = 0) = \binom{20}{0}(0.05)⁰(0.95)²⁰ = 1 × 1 × (0.95)²⁰ ≈ 0.3585.

P(X = 1) = \binom{20}{1}(0.05)¹(0.95)¹⁹ = 20 × 0.05 × (0.95)¹⁹.

(0.95)¹⁹ ≈ 0.3774, so P(X = 1) ≈ 20 × 0.05 × 0.3774 = 0.3774.

P(X ≤ 1) ≈ 0.3585 + 0.3774 = 0.7359.

So about a 73.6% chance of getting 0 or 1 defectives.

**(c) At least 1 defective:**

"At least 1" means 1, 2, 3, …, or 20. Computing all of these individually would be tedious. A much smarter approach: use the complement.

P(X ≥ 1) = 1 − P(X = 0) = 1 − 0.3585 = 0.6415.

**Why the complement works:** Every possible number of defectives (0 through 20) sums to probability 1. The event "at least 1" is everything except X = 0. So subtracting P(X = 0) from 1 gives the answer instantly.

**Common misconception:** Students sometimes try to compute P(X ≥ 1) by adding P(X = 1) + P(X = 2) + … + P(X = 20) individually. This is slow and error-prone. Always check if the complement (1 − something) is easier.

---

## Mean and Variance of a Binomial Random Variable

For X ~ B(n, p), the expected value and variance have very simple formulas:

$$\boxed{E(X) = np}$$

$$\boxed{\text{Var}(X) = np(1-p) = npq}$$

$$\boxed{\sigma = \sqrt{np(1-p)}}$$

You do not need to sum over all k values to find E(X) and Var(X). The formulas come from the fact that a binomial random variable is the sum of n independent Bernoulli trials, each with mean p and variance p(1−p). When you add independent random variables, their means add and their variances add.

**Example:** For X ~ B(100, 0.3):

- E(X) = 100 × 0.3 = 30
- Var(X) = 100 × 0.3 × 0.7 = 21
- σ = √21 ≈ 4.58

**Interpretation:** In 100 trials with a 30% success rate, you expect about 30 successes. The number of successes typically varies from 30 by about ±4.6.

---

## Shape of the Binomial Distribution

The shape of the binomial distribution depends on p:

- When p = 0.5, the distribution is **symmetric**. The bars for k successes and n−k successes have equal height.
- When p < 0.5, the distribution is **skewed to the right**. Lower numbers of successes are more likely, and there is a longer tail toward higher values.
- When p > 0.5, the distribution is **skewed to the left**. Higher numbers of successes are more likely.
- As n gets larger, the binomial distribution looks more and more like a bell-shaped normal curve (this is the Central Limit Theorem, which we preview in the next lesson).

---

## Calculator Use for Binomial Probabilities

In IB exams, you can use your graphing calculator to compute binomial probabilities directly:

- **TI-Nspire:** Menu → Probability → Distributions → Binomial Pdf (for P(X = k)) or Binomial Cdf (for P(X ≤ k)).
- **TI-84:** 2nd → DISTR → binompdf(n, p, k) or binomcdf(n, p, k).
- **Casio:** STAT → DIST → BINM → Bpd or Bcd.

"Pdf" stands for probability density function (gives P(X = k)) and "Cdf" stands for cumulative distribution function (gives P(X ≤ k)). Even with a calculator available, you should be able to write the formula and compute simple cases by hand, because some exam questions ask you to set up the expression.

---

## Worked Example 3: Multiple-Choice Test

**Problem:** A multiple-choice test has 12 questions, each with 4 options. A student guesses randomly on every question. Let X be the number of correct answers.

(a) State the distribution of X.
(b) Find E(X) and explain what it means.
(c) Find the probability of getting exactly 5 correct.
(d) Find the probability of passing, where passing means getting at least 6 correct.

**Approach:**

(a) n = 12 independent questions, each with probability p = 1/4 = 0.25 of being correct by guessing. So X ~ B(12, 0.25).

(b) E(X) = np = 12 × 0.25 = 3. **Interpretation:** A student who guesses on every question will get about 3 out of 12 correct on average. This is why random guessing is not a good strategy.

(c) P(X = 5) = \binom{12}{5}(0.25)⁵(0.75)⁷.

First, \binom{12}{5} = 12!/(5!·7!) = (12×11×10×9×8)/(5×4×3×2×1) = 95040/120 = 792.

(0.25)⁵ = (1/4)⁵ = 1/1024.

(0.75)⁷ = (3/4)⁷ = 3⁷/4⁷ = 2187/16384.

P(X = 5) = 792 × (1/1024) × (2187/16384).

Using a calculator: P(X = 5) ≈ 0.1032, or about 10.3%.

(d) P(pass) = P(X ≥ 6) = 1 − P(X ≤ 5).

Use a calculator: binomcdf(12, 0.25, 5) ≈ 0.9456.

P(X ≥ 6) ≈ 1 − 0.9456 = 0.0544.

**Interpretation:** There is only about a 5.4% chance of passing by guessing. This makes sense — to pass you need at least half the questions right, but on average you only get a quarter right by guessing.

---

## Practice Problems

---

### Problem 1
A fair six-sided die is rolled 8 times. Let X be the number of times a "6" appears.

(a) State the distribution of X (give n and p).
(b) Write the expression for P(X = 2) using the binomial formula, then compute it. Leave unsimplified factors if you wish, but give a decimal answer.
(c) Find P(X ≥ 1) — the probability of getting at least one 6.
(d) Find E(X) and Var(X).

---

### Problem 2
In a school, 30% of students study Spanish. A random sample of 15 students is selected. Let X be the number of students in the sample who study Spanish.

(a) Find P(X = 5). Use your calculator or compute by hand with the formula.
(b) Find P(3 ≤ X ≤ 6) — the probability that between 3 and 6 students (inclusive) study Spanish.
(c) Find the mode of X — that is, the most likely number of Spanish students in the sample. *Hint: the mode of a binomial is near np. Compute P(X = 4) and P(X = 5) and compare.*

---

### Problem 3
A biased coin lands heads with probability 0.4. It is tossed 20 times. Let X be the number of heads.

(a) Calculate E(X) and the standard deviation σ.
(b) Using the approximate rule that most values fall within 2 standard deviations of the mean (E(X) ± 2σ), give a range where you would expect the number of heads to fall about 95% of the time.

---

### Problem 4
A binomial experiment has n = 25 trials and success probability p = 0.2.

(a) Without using a calculator, write the full expression (with the binomial coefficient) for P(X = 3).
(b) Write the expression for P(X = 0) and verify that it simplifies to (0.8)²⁵. If a calculator gives P(X = 0) ≈ 0.0038, check that this is reasonable.
(c) Explain why P(X > 25) = 0 and P(X < 0) = 0. What does this tell you about the possible values of X?

---

### Problem 5 (IB Exam Style — 8 marks)
A new drug is effective for 80% of patients who take it. In a clinical trial, the drug is given to 10 patients. Assume the patients respond independently.

(a) [1 mark] State the distribution of X, the number of patients who respond to the drug.

(b) [2 marks] Find the probability that exactly 8 patients respond.

(c) [3 marks] Find the probability that at least 9 patients respond. Show your working clearly.

(d) [2 marks] The trial is considered a "strong success" if all 10 patients respond. Find the probability of a strong success. Is this outcome likely? Explain briefly.

---

## Answers

---

### Answer 1

(a) X ~ B(8, 1/6). There are n = 8 independent rolls, each with p = 1/6 chance of a 6.

(b) P(X = 2) = \binom{8}{2}(1/6)²(5/6)⁶.

\binom{8}{2} = 28. (1/6)² = 1/36. (5/6)⁶ = 15625/46656.

P(X = 2) = 28 × (1/36) × (15625/46656) = (28 × 15625)/(36 × 46656) = 437500/1679616 ≈ 0.2605.

(c) P(X ≥ 1) = 1 − P(X = 0). P(X = 0) = (5/6)⁸ = 390625/1679616 ≈ 0.2326. So P(X ≥ 1) ≈ 1 − 0.2326 = 0.7674.

**Why the complement?** Computing P(X = 1) + P(X = 2) + … + P(X = 8) would be slow. Using 1 − P(X = 0) is instant.

(d) E(X) = 8 × (1/6) = 8/6 = 4/3 ≈ 1.333.

Var(X) = 8 × (1/6) × (5/6) = 40/36 = 10/9 ≈ 1.111.

**Interpretation:** In 8 rolls, you expect about 1.33 sixes on average, with a variance of about 1.11.

---

### Answer 2

X ~ B(15, 0.30).

(a) P(X = 5) = \binom{15}{5}(0.3)⁵(0.7)¹⁰.

\binom{15}{5} = 3003. (0.3)⁵ = 0.00243. (0.7)¹⁰ ≈ 0.02825.

P(X = 5) ≈ 3003 × 0.00243 × 0.02825 ≈ 0.2061.

(b) P(3 ≤ X ≤ 6) = P(X ≤ 6) − P(X ≤ 2).

Using a calculator: binomcdf(15, 0.3, 6) ≈ 0.8689 and binomcdf(15, 0.3, 2) ≈ 0.1268.

P(3 ≤ X ≤ 6) ≈ 0.8689 − 0.1268 = 0.7421.

(c) The expected value is np = 15 × 0.3 = 4.5, so the mode should be near 4 or 5.

P(X = 4) = \binom{15}{4}(0.3)⁴(0.7)¹¹ = 1365 × 0.0081 × 0.01977 ≈ 0.2186.

P(X = 5) ≈ 0.2061 (from part a).

So P(X = 4) > P(X = 5). The mode is 4.

You can also use the rule: mode = floor((n+1)p) = floor(16 × 0.3) = floor(4.8) = 4. This is a quick check, but computing and comparing is more reliable on an exam.

---

### Answer 3

(a) E(X) = np = 20 × 0.4 = 8.

Var(X) = np(1−p) = 20 × 0.4 × 0.6 = 4.8.

σ = √4.8 ≈ 2.19.

(b) The approximate 95% range is E(X) ± 2σ:

8 − 2(2.19) = 8 − 4.38 = 3.62 (round to about 4)

8 + 2(2.19) = 8 + 4.38 = 12.38 (round to about 12)

So we expect the number of heads to be between 4 and 12 about 95% of the time.

**Why this works:** For large enough n, the binomial is approximately normal (the Central Limit Theorem). The empirical rule for normal distributions says about 95% of values lie within 2 standard deviations of the mean. Here n = 20 is moderately large, so the approximation is reasonable.

---

### Answer 4

(a) P(X = 3) = \binom{25}{3}(0.2)³(0.8)²².

\binom{25}{3} = (25×24×23)/(3×2×1) = 13800/6 = 2300.

So P(X = 3) = 2300 × (0.2)³ × (0.8)²² = 2300 × 0.008 × (0.8)²².

(b) P(X = 0) = \binom{25}{0}(0.2)⁰(0.8)²⁵ = 1 × 1 × (0.8)²⁵.

Since (0.8)²⁵ ≈ 0.00378, this matches the calculator value. It is small but not zero — it is possible (though unlikely) to get zero successes in 25 trials even with p = 0.2.

(c) X counts successes in 25 trials. The minimum possible number of successes is 0 (if all trials fail) and the maximum is 25 (if all succeed). There is no way to have more than 25 successes or fewer than 0, so P(X > 25) = 0 and P(X < 0) = 0.

This tells you that the binomial distribution only assigns positive probability to the integers 0, 1, 2, …, n. Anything outside this range is impossible.

---

### Answer 5

(a) X ~ B(10, 0.8). The 10 patients are independent trials, each with p = 0.8 chance of responding. [1 mark]

(b) P(X = 8) = \binom{10}{8}(0.8)⁸(0.2)².

\binom{10}{8} = \binom{10}{2} = 45.

(0.8)⁸ ≈ 0.1678. (0.2)² = 0.04.

P(X = 8) ≈ 45 × 0.1678 × 0.04 ≈ 0.3020. [2 marks]

(c) P(X ≥ 9) = P(X = 9) + P(X = 10).

P(X = 9) = \binom{10}{9}(0.8)⁹(0.2)¹ = 10 × (0.8)⁹ × 0.2.

(0.8)⁹ ≈ 0.1342. So P(X = 9) ≈ 10 × 0.1342 × 0.2 ≈ 0.2684.

P(X = 10) = (0.8)¹⁰ ≈ 0.1074.

P(X ≥ 9) ≈ 0.2684 + 0.1074 = 0.3758. [3 marks]

(d) P(X = 10) = (0.8)¹⁰ ≈ 0.1074, or about 10.7%.

This is not very likely — only about a 1 in 9 chance. Even though the drug is quite effective (80%), getting all 10 patients to respond is unlikely because each patient has a 20% chance of not responding. The probability (0.8)¹⁰ is like getting 10 independent successes in a row, each with probability 0.8. [2 marks]

