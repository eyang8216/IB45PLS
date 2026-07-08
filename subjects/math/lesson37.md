# Lesson 37: The Normal Distribution

---

## What Is the Normal Distribution?

In the previous lesson, we studied the binomial distribution, which counts successes in discrete trials. But many quantities in the real world are not counts — they are measurements. Heights of people, IQ scores, the diameter of a manufactured bolt, the weight of a bag of flour. These quantities can take any value within a range, not just whole numbers. They are **continuous** random variables.

The **normal distribution** is the most important probability distribution for continuous measurements. Its graph is the famous bell-shaped curve. It appears everywhere: in nature (heights, blood pressure), in manufacturing (tolerances, fill volumes), in testing (exam scores), and in statistics (sampling distributions, confidence intervals).

The normal distribution is important for two reasons:

1. Many real-world variables are approximately normally distributed.
2. Even when data are not normal, averages of large samples tend to be normal. This is called the **Central Limit Theorem** — we will explore it more in later lessons.

---

## Continuous Random Variables — A Quick Picture

For a discrete random variable like the binomial, we find probabilities by adding up values from the probability mass function. For a continuous random variable, probability is represented by **area under a curve.**

The curve is called a **probability density function (PDF)**. It has these properties:

- The curve never goes below the horizontal axis: f(x) ≥ 0 for all x.
- The total area under the entire curve equals exactly 1.
- The probability that X falls between two numbers a and b is the area under the curve from a to b.

Because a continuous random variable can take infinitely many values, the probability that X equals any *single* value is zero. We always talk about intervals: P(a ≤ X ≤ b).

---

## The Normal Distribution — Two Parameters

A normal distribution is completely described by two numbers:

- **μ (mu): the mean.** This is the center of the bell curve. The curve is symmetric, so the mean, median, and mode are all at the same point.
- **σ (sigma): the standard deviation.** This controls how spread out the curve is. A larger σ makes the curve wider and flatter. A smaller σ makes it taller and narrower.

We write:

$$X \sim N(\mu, \sigma^2)$$

This means "X follows a normal distribution with mean μ and variance σ²." Note that the second parameter inside the parentheses is the **variance** (σ²), not the standard deviation. This is a common source of confusion — always check whether a problem gives σ or σ².

The formula for the normal density curve is:

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$

You do NOT need to memorize or use this formula in IB. It is shown here only so you know what the curve looks like mathematically. All computations are done with tables or a calculator.

---

## The 68–95–99.7 Rule (The Empirical Rule)

For any normal distribution, the following approximate percentages hold:

- About **68%** of all values lie within 1 standard deviation of the mean: between μ − σ and μ + σ.
- About **95%** lie within 2 standard deviations: between μ − 2σ and μ + 2σ.
- About **99.7%** lie within 3 standard deviations: between μ − 3σ and μ + 3σ.

These numbers are useful for quick estimates. They also tell you that values more than 2σ from the mean are unusual, and values more than 3σ from the mean are very rare.

---

## The Standard Normal Distribution — Z-Scores

There are infinitely many normal distributions (one for every choice of μ and σ). To work with them all using a single table or calculator function, we convert every normal problem into the **standard normal distribution**, which has mean 0 and standard deviation 1:

$$Z \sim N(0, 1)$$

The conversion uses the **z-score formula:**

$$\boxed{z = \frac{x - \mu}{\sigma}}$$

A z-score tells you how many standard deviations a value x is above or below the mean. If z = 2, the value is 2 standard deviations above the mean. If z = −1.5, the value is 1.5 standard deviations below the mean.

---

## Worked Example 1: Finding a Probability (Forward)

**Problem:** IQ scores are normally distributed with mean μ = 100 and standard deviation σ = 15. What proportion of people have an IQ below 115?

**Approach:** We want P(X < 115) where X ~ N(100, 15²).

**Step 1: Convert to a z-score.**

$$z = \frac{115 - 100}{15} = \frac{15}{15} = 1$$

So P(X < 115) = P(Z < 1).

**Step 2: Find P(Z < 1).**

Using a calculator or z-table: P(Z < 1) ≈ 0.8413.

**Interpretation:** About 84.1% of people have an IQ below 115. This makes sense: 115 is one standard deviation above the mean, and the 68–95–99.7 rule tells us that about 68% are within ±1σ. The remaining 32% are split equally in the two tails (16% in each), so about 50% + 34% = 84% are below +1σ.

---

## Worked Example 2: Probability Between Two Values

**Problem:** Using the same IQ distribution (μ = 100, σ = 15), what proportion of people have an IQ between 85 and 115?

**Approach:** We want P(85 < X < 115).

**Step 1: Convert both boundaries to z-scores.**

For x = 85: z = (85 − 100)/15 = −15/15 = −1.

For x = 115: z = 115 − 100)/15 = 15/15 = 1.

So P(85 < X < 115) = P(−1 < Z < 1).

**Step 2: Compute using the standard normal.**

P(−1 < Z < 1) = P(Z < 1) − P(Z < −1).

P(Z < 1) ≈ 0.8413. P(Z < −1) ≈ 0.1587.

P(−1 < Z < 1) = 0.8413 − 0.1587 = 0.6826.

**Interpretation:** About 68.3% of people have IQs between 85 and 115. This matches the 68–95–99.7 rule: about 68% of values lie within 1 standard deviation of the mean.

**Why this makes sense:** The interval [85, 115] is exactly μ ± σ. The empirical rule predicted about 68%, and our calculation gives 68.26%.

---

## Worked Example 3: Inverse Normal — Finding a Value Given a Probability

**Problem:** Still using IQ ~ N(100, 15²). What IQ score separates the top 5% from the rest? In other words, find c such that P(X > c) = 0.05.

**Approach:** This is an **inverse normal** problem — we know the probability and need to find the value.

**Step 1: Express in terms of the left tail.**

P(X > c) = 0.05 means P(X < c) = 0.95 (because 1 − 0.05 = 0.95). Most calculators and tables use P(Z < z), so it is easier to work with the left tail.

**Step 2: Find the z-score for the 95th percentile.**

Using a calculator or z-table: the z-score such that P(Z < z) = 0.95 is approximately z = 1.645.

**Step 3: Convert the z-score back to the original scale.**

c = μ + z·σ = 100 + 1.645 × 15 = 100 + 24.675 = 124.675.

**Interpretation:** An IQ of about 125 is needed to be in the top 5%. This is about 1.645 standard deviations above the mean.

---

## Worked Example 4: Manufacturing Tolerance

**Problem:** A machine produces bolts whose diameters are normally distributed with mean μ = 10 mm and standard deviation σ = 0.2 mm. A bolt passes quality control if its diameter is between 9.7 mm and 10.3 mm. What proportion of bolts pass?

**Approach:** We want P(9.7 < X < 10.3) where X ~ N(10, 0.2²).

**Step 1: Convert to z-scores.**

For 9.7: z = (9.7 − 10)/0.2 = −0.3/0.2 = −1.5.

For 10.3: z = (10.3 − 10)/0.2 = 0.3/0.2 = 1.5.

**Step 2: Compute P(−1.5 < Z < 1.5).**

P(Z < 1.5) ≈ 0.9332. P(Z < −1.5) ≈ 0.0668.

P(−1.5 < Z < 1.5) = 0.9332 − 0.0668 = 0.8664.

**Interpretation:** About 86.6% of bolts pass inspection. The remaining 13.4% are rejected — half (about 6.7%) are too narrow and half are too wide, because the distribution is symmetric.

---

## The Poisson Distribution — Brief Introduction (IB HL Bonus)

While the normal distribution handles continuous measurements, the **Poisson distribution** handles counts of rare events happening in a fixed interval of time, space, or volume. Examples: number of calls to a call center per minute, number of typos per page, number of radioactive decays per second.

If X follows a Poisson distribution with mean rate λ (lambda), then:

$$P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}, \quad k = 0, 1, 2, \ldots$$

The number e ≈ 2.71828 is Euler's number, a fundamental constant in mathematics.

A unique property of the Poisson distribution: the mean and variance are equal. E(X) = Var(X) = λ.

**Example:** A call center receives an average of 3 calls per minute. What is the probability of exactly 5 calls in a given minute?

$$P(X = 5) = \frac{3^5 e^{-3}}{5!} = \frac{243 \times 0.0498}{120} \approx 0.101$$

So about a 10.1% chance.

**Connection to binomial:** When n is very large and p is very small, with np = λ held constant, the binomial distribution B(n, p) is approximately Poisson(λ). This is why the Poisson is sometimes called the "law of rare events."

---

## Practice Problems

---

### Problem 1
Let X ~ N(50, 10²). Find P(X > 65).

---

### Problem 2
Let X ~ N(200, 30²). Find the proportion of values that lie between 170 and 230.

---

### Problem 3
X ~ N(75, 8²). Find the value c such that P(X < c) = 0.10. That is, find the 10th percentile.

---

### Problem 4
Exam scores are normally distributed with mean 65 and standard deviation 12. The top 5% of students receive an A. What score is needed to earn an A?

---

### Problem 5 (IB Exam Style — 6 marks)
The heights of adult males in a population are normally distributed with mean μ = 170 cm and standard deviation σ = 10 cm.

(a) [2 marks] Find the probability that a randomly selected adult male is taller than 190 cm.

(b) [2 marks] In a random sample of 1000 adult males from this population, estimate how many would be expected to be taller than 190 cm.

(c) [2 marks] Find the height that is exceeded by only the tallest 2.5% of the population. Give your answer to one decimal place.

---

### Problem 6 (Poisson — HL bonus)
Arrivals at a bus stop follow a Poisson distribution with a mean of 4 arrivals per hour. Find the probability of exactly 2 arrivals in a randomly chosen hour. Give your answer to 3 decimal places.

---

## Answers

---

### Answer 1

We want P(X > 65) where X ~ N(50, 10²).

**Step 1: z-score.** z = (65 − 50)/10 = 15/10 = 1.5.

**Step 2: Find the probability.** P(X > 65) = P(Z > 1.5).

P(Z > 1.5) = 1 − P(Z < 1.5). Using a table or calculator: P(Z < 1.5) ≈ 0.9332.

P(Z > 1.5) = 1 − 0.9332 = 0.0668.

**Interpretation:** About 6.7% of values are above 65. This makes sense: 65 is 1.5σ above the mean. From the 68–95–99.7 rule, we know roughly 16% are above μ+σ, and even fewer above μ+1.5σ.

**Pitfall:** Always check whether the question asks for P(X > c) or P(X < c). If it asks for the upper tail, use 1 − P(Z < z).

---

### Answer 2

We want P(170 < X < 230) where X ~ N(200, 30²).

**Step 1: z-scores.**

z₁ = (170 − 200)/30 = −30/30 = −1.

z₂ = (230 − 200)/30 = 30/30 = 1.

**Step 2: Compute.** P(−1 < Z < 1) = P(Z < 1) − P(Z < −1).

P(Z < 1) ≈ 0.8413. P(Z < −1) ≈ 0.1587.

0.8413 − 0.1587 = 0.6826.

**Interpretation:** About 68.3% of values lie between 170 and 230. This is the μ ± σ interval, which the empirical rule says contains about 68% of values.

---

### Answer 3

We want c such that P(X < c) = 0.10, where X ~ N(75, 8²).

**Step 1: Find the z-score for the 10th percentile.** P(Z < z) = 0.10.

From a table or calculator: z ≈ −1.28 (since the 10th percentile is below the mean, z is negative).

**Step 2: Convert back.** c = μ + z·σ = 75 + (−1.28)(8) = 75 − 10.24 = 64.76.

**Interpretation:** The 10th percentile is about 64.8. Only 10% of values are below this number.

**Why z is negative:** The 10th percentile is below the mean. If you got a positive z-score, your answer would be above 75, which would mean more than 50% of values are below it — clearly wrong for the 10th percentile. Always check that your answer makes sense relative to the mean.

---

### Answer 4

We want c such that P(X > c) = 0.05, where X ~ N(65, 12²).

**Step 1: Convert to left tail.** P(X < c) = 0.95.

**Step 2: Find the z-score.** P(Z < z) = 0.95 ⇒ z ≈ 1.645.

**Step 3: Convert back.** c = 65 + 1.645 × 12 = 65 + 19.74 = 84.74.

**Interpretation:** A student needs to score about 85 (rounding to the nearest whole number) to earn an A. Only the top 5% achieve this.

---

### Answer 5

X ~ N(170, 10²).

(a) **P(X > 190):**

z = (190 − 170)/10 = 20/10 = 2.

P(Z > 2) = 1 − P(Z < 2) = 1 − 0.9772 = 0.0228.

About 2.28% of males are taller than 190 cm.

[2 marks]

(b) **Expected count in a sample of 1000:**

Expected number = 1000 × 0.0228 = 22.8.

So approximately 23 people in a sample of 1000 would be taller than 190 cm.

[2 marks]

(c) **Height exceeded by only the tallest 2.5%:**

P(X > c) = 0.025, so P(X < c) = 0.975.

z for 0.975 ≈ 1.96.

c = 170 + 1.96 × 10 = 170 + 19.6 = 189.6 cm.

The tallest 2.5% are taller than 189.6 cm.

[2 marks]

---

### Answer 6

X ~ Poisson(λ = 4).

$$P(X = 2) = \frac{4^2 e^{-4}}{2!} = \frac{16 \times e^{-4}}{2}$$

e⁻⁴ ≈ 0.01832 (using calculator).

P(X = 2) = 16 × 0.01832 / 2 = 0.1466 / 2 ≈ 0.147.

**Interpretation:** There is about a 14.7% chance of exactly 2 arrivals in a given hour.

