# Lesson 35: Discrete Random Variables, Expectation, and Variance

---

## What Is a Random Variable?

Imagine you flip a coin three times and count how many heads you get. The result could be 0, 1, 2, or 3. But before you flip, you do not know which one it will be. The number of heads is an example of a **random variable**.

A **random variable** is a way to attach a number to every possible outcome of a random experiment. We usually denote random variables with capital letters like X, Y, or Z. This lesson focuses on **discrete** random variables — ones that can only take certain separate values (like whole numbers), as opposed to continuous measurements like height or time.

**Example:** Toss a fair coin 3 times. Let X = the number of heads observed. The eight equally likely outcomes and the value of X for each are:

| Outcome | HHH | HHT | HTH | THH | HTT | THT | TTH | TTT |
|---|---|---|---|---|---|---|---|---|
| Value of X | 3 | 2 | 2 | 2 | 1 | 1 | 1 | 0 |

X is a discrete random variable because it only takes the values 0, 1, 2, or 3.

---

## Probability Mass Function (PMF)

For a discrete random variable X, we want to know how likely each possible value is. The **probability mass function**, written P(X = x), gives the probability that X equals a specific value x.

**Example continued:** For the 3-coin-toss experiment, we can count how many outcomes give each value.

- X = 0: only TTT — probability 1/8.
- X = 1: HTT, THT, TTH — probability 3/8.
- X = 2: HHT, HTH, THH — probability 3/8.
- X = 3: only HHH — probability 1/8.

We can display this as a table:

| x | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| P(X = x) | 1/8 | 3/8 | 3/8 | 1/8 |

A probability mass function must satisfy two conditions:

1. Every probability is between 0 and 1: 0 ≤ P(X = x) ≤ 1.
2. The sum of all the probabilities equals 1.

For our example: 1/8 + 3/8 + 3/8 + 1/8 = 8/8 = 1. ✓

---

## Expected Value — The Long-Run Average

The **expected value** of a random variable X, written E(X), is the average value you would get if you repeated the experiment an enormous number of times. It is a weighted average: each possible value is weighted by its probability.

$$\boxed{E(X) = \sum_x x \cdot P(X = x)}$$

The symbol Σ (sigma) means "sum over all possible values of x." For each value, multiply the value by its probability, then add everything up.

**Example continued:**

E(X) = 0·(1/8) + 1·(3/8) + 2·(3/8) + 3·(1/8)

= (0 + 3 + 6 + 3) / 8 = 12/8 = 1.5

This tells us that if you toss a fair coin 3 times, over and over, the average number of heads per set of 3 tosses will be 1.5. The expected value does not have to be a possible value of X — you cannot actually get 1.5 heads in 3 tosses. It is an average, not an individual outcome.

**Common misconception:** E(X) is not necessarily the "most likely" value. For example, in our 3-coin case, X = 1 and X = 2 each have probability 3/8, which is higher than the probability of X = 1.5 (which is zero). The expected value is the balance point of the distribution, not the peak.

---

## Variance — How Spread Out Is the Distribution?

Two random variables can have the same expected value but very different patterns. For example, X = number of heads in 3 fair coin tosses has E(X) = 1.5. But a different random variable that always equals exactly 1.5 would also have E = 1.5. The difference is in how much the values vary.

**Variance**, written Var(X), measures the average squared distance of X from its mean. It tells us how spread out the distribution is.

The definition is:

$$\text{Var}(X) = E[(X - \mu)^2] = \sum_x (x - \mu)^2 \cdot P(X = x)$$

where μ (the Greek letter mu) is E(X).

However, there is a much easier formula to use:

$$\boxed{\text{Var}(X) = E(X^2) - [E(X)]^2}$$

Here, E(X²) means: square each value first, then take the weighted average:

$$E(X^2) = \sum_x x^2 \cdot P(X = x)$$

The **standard deviation**, written σ (sigma), is the square root of the variance:

$$\sigma = \sqrt{\text{Var}(X)}$$

The standard deviation has the same units as X, which makes it easier to interpret than variance.

**Example continued:** We already know E(X) = 1.5.

Compute E(X²):

E(X²) = 0²·(1/8) + 1²·(3/8) + 2²·(3/8) + 3²·(1/8)

= (0 + 3 + 12 + 9) / 8 = 24/8 = 3

Now use the shortcut formula:

Var(X) = E(X²) − [E(X)]² = 3 − (1.5)² = 3 − 2.25 = 0.75

σ = √0.75 = √3/2 ≈ 0.866

**Interpretation:** In 3 fair coin tosses, the number of heads typically varies from the mean of 1.5 by about 0.87 heads. Since the standard deviation is less than 1, most outcomes (0, 1, 2, or 3 heads) are within about one standard deviation of the mean.

---

## Linear Transformations — What Happens When We Add or Multiply?

Suppose we take a random variable X and create a new variable Y by multiplying X by a constant a and adding a constant b: Y = aX + b. How do the mean and variance change?

$$\boxed{E(aX + b) = aE(X) + b}$$

$$\boxed{\text{Var}(aX + b) = a^2\,\text{Var}(X)}$$

These formulas have an important practical meaning:

- Adding a constant shifts every value of X up or down by the same amount, so the mean shifts by that amount. But variance does not change — the spread stays the same.
- Multiplying by a constant scales both the mean and the spread. But variance scales by the *square* of the constant. For example, if you double X, the variance quadruples.

**Example:** Suppose E(X) = 1.5 and Var(X) = 0.75. Define Y = 2X + 5.

- E(Y) = 2·E(X) + 5 = 2·(1.5) + 5 = 3 + 5 = 8
- Var(Y) = 2²·Var(X) = 4·(0.75) = 3
- Standard deviation of Y: σ_Y = √3 ≈ 1.732

---

## Worked Example 1: A Game of Chance

**Problem:** A game costs $5 to play. You roll a fair six-sided die. If you roll a 6, you win $20. If you roll a 5, you win $10. If you roll 1, 2, 3, or 4, you win nothing. Let X be your net profit (winnings minus the $5 cost). Find E(X) and interpret what it means.

**Approach:** First, list each possible outcome, the net profit for that outcome, and its probability.

| Die Roll | Winnings | Net Profit x | P(X = x) |
|---|---|---|---|
| 6 | $20 | 20 − 5 = 15 | 1/6 |
| 5 | $10 | 10 − 5 = 5 | 1/6 |
| 1, 2, 3, 4 | $0 | 0 − 5 = −5 | 4/6 |

Now compute E(X):

E(X) = 15·(1/6) + 5·(1/6) + (−5)·(4/6) = (15 + 5 − 20)/6 = 0/6 = 0

**Interpretation:** The expected net profit is $0. This means the game is **fair** — if you play many times, you will neither gain nor lose money on average. Of course, in any single game you either win $15, win $5, or lose $5, but over the long run these outcomes balance out.

**Why this makes sense:** The probability of winning something (rolling 5 or 6) is 2/6 = 1/3. When you win, you win $15 or $5. When you lose (probability 2/3), you lose $5. The expected gain from winning (average $10 when you win, happening 1/3 of the time) roughly balances the expected loss ($5 happening 2/3 of the time).

---

## Worked Example 2: Finding an Unknown Constant in a PMF

**Problem:** A discrete random variable X has the probability mass function P(X = x) = kx for x = 1, 2, 3, 4, and P(X = x) = 0 for any other x.

(a) Find the value of k.
(b) Find E(X) and Var(X).

**Approach for (a):** The sum of all probabilities must equal 1. So:

P(X = 1) + P(X = 2) + P(X = 3) + P(X = 4) = 1

k·1 + k·2 + k·3 + k·4 = k(1 + 2 + 3 + 4) = k·10 = 1

Therefore k = 1/10 = 0.1.

So the PMF is: P(X = 1) = 0.1, P(X = 2) = 0.2, P(X = 3) = 0.3, P(X = 4) = 0.4.

**Approach for (b):** First find E(X):

E(X) = 1·(0.1) + 2·(0.2) + 3·(0.3) + 4·(0.4)

= 0.1 + 0.4 + 0.9 + 1.6 = 3.0

Next find E(X²):

E(X²) = 1²·(0.1) + 2²·(0.2) + 3²·(0.3) + 4²·(0.4)

= 1·(0.1) + 4·(0.2) + 9·(0.3) + 16·(0.4)

= 0.1 + 0.8 + 2.7 + 6.4 = 10.0

Now apply the shortcut formula:

Var(X) = E(X²) − [E(X)]² = 10.0 − 3² = 10 − 9 = 1

σ = √1 = 1

**Interpretation:** The distribution is centered at 3 with a standard deviation of 1. Since higher values of X are more likely than lower ones (the probabilities increase from 0.1 to 0.4 as x increases), the mean is pulled above the midpoint of 2.5.

---

## Connecting to Sample Statistics

The ideas in this lesson are population-level concepts. When you collect actual data from a sample, you calculate the sample mean (x̄) and sample variance (s²). These are estimates of E(X) and Var(X). The formulas look similar:

| Concept | Population (Random Variable) | Sample (Data) |
|---|---|---|
| Center | E(X) = Σ x·P(X = x) | x̄ = (1/n)·Σ xᵢ |
| Spread | Var(X) = E(X²) − [E(X)]² | s² = [1/(n−1)]·Σ (xᵢ − x̄)² |

The population parameters E(X) and Var(X) describe the underlying random process. Sample statistics are what we compute from actual observations to estimate those parameters.

---

## Practice Problems

---

### Problem 1
A fair coin is tossed 4 times. Let X be the number of heads that appear.

(a) List all possible values of X and give the probability of each. This is the probability mass function of X.

(b) Compute E(X), the expected number of heads.

(c) Compute Var(X) and the standard deviation σ.

---

### Problem 2
A discrete random variable Y has the following probability mass function:

P(Y = −1) = 0.2, P(Y = 0) = 0.5, P(Y = 2) = 0.3.

(a) Find E(Y).

(b) Find Var(Y).

(c) Define a new random variable W = 3Y − 4. Find E(W) and Var(W).

---

### Problem 3
A random variable X has E(X) = 5 and Var(X) = 9. Using the linear transformation rules (without knowing the actual distribution of X), find:

(a) E(2X + 1)

(b) Var(2X + 1)

(c) E(X²) — *Hint: use the variance shortcut formula solved for E(X²).*

---

### Problem 4
The probability mass function of X is given by P(X = x) = c/x for x = 1, 2, 3, and P(X = x) = 0 otherwise.

(a) Find the constant c that makes this a valid PMF.

(b) Find E(X) and Var(X). Give your answers as exact fractions.

---

### Problem 5 (IB Exam Style — 8 marks)
A card is drawn at random from a standard 52-card deck. The net profit X is defined as follows:

- If the card is an Ace, you win $10.
- If the card is a King, you win $5.
- If the card is anything else, you lose $2.

(a) [2 marks] Write the probability mass function of X as a table showing each possible value of X and its probability. Express probabilities as simplified fractions.

(b) [2 marks] Calculate E(X).

(c) [2 marks] Based on E(X), state whether the game is favorable, fair, or unfavorable to the player, and explain what the expected value means in practical terms.

(d) [2 marks] Calculate Var(X) and the standard deviation of X.

---

### Problem 6
In a lottery, 1000 tickets are sold at $2 each. There is one prize of $500 and two prizes of $100. Let X be the net profit for a person who buys one ticket (the prize amount minus the $2 cost, or −$2 if no prize is won).

(a) Give the PMF of X.

(b) Find E(X) and interpret what it tells you about the lottery.

---

## Answers

---

### Answer 1

(a) For 4 fair coin tosses, each of the 16 outcomes is equally likely. The number of heads follows a pattern:

- X = 0: TTTT — 1 outcome — P(X = 0) = 1/16
- X = 1: HTTT, THTT, TTHT, TTTH — 4 outcomes — P(X = 1) = 4/16 = 1/4
- X = 2: HHTT, HTHT, HTTH, THHT, THTH, TTHH — 6 outcomes — P(X = 2) = 6/16 = 3/8
- X = 3: HHHT, HHTH, HTHH, THHH — 4 outcomes — P(X = 3) = 4/16 = 1/4
- X = 4: HHHH — 1 outcome — P(X = 4) = 1/16

Check sum: 1 + 4 + 6 + 4 + 1 = 16. ✓

(b) E(X) = 0·(1/16) + 1·(4/16) + 2·(6/16) + 3·(4/16) + 4·(1/16)

= (0 + 4 + 12 + 12 + 4)/16 = 32/16 = 2

**Interpretation:** In 4 tosses of a fair coin, you expect 2 heads on average.

(c) E(X²) = 0²·(1/16) + 1²·(4/16) + 2²·(6/16) + 3²·(4/16) + 4²·(1/16)

= (0 + 4 + 24 + 36 + 16)/16 = 80/16 = 5

Var(X) = E(X²) − [E(X)]² = 5 − 2² = 5 − 4 = 1

σ = √1 = 1

**Interpretation:** The number of heads typically varies from the mean of 2 by about 1 head.

---

### Answer 2

(a) E(Y) = (−1)·(0.2) + 0·(0.5) + 2·(0.3) = −0.2 + 0 + 0.6 = 0.4

(b) E(Y²) = (−1)²·(0.2) + 0²·(0.5) + 2²·(0.3) = 1·(0.2) + 0 + 4·(0.3) = 0.2 + 1.2 = 1.4

Var(Y) = E(Y²) − [E(Y)]² = 1.4 − (0.4)² = 1.4 − 0.16 = 1.24

(c) E(W) = E(3Y − 4) = 3·E(Y) − 4 = 3·(0.4) − 4 = 1.2 − 4 = −2.8

Var(W) = Var(3Y − 4) = 3²·Var(Y) = 9·(1.24) = 11.16

---

### Answer 3

(a) E(2X + 1) = 2·E(X) + 1 = 2·(5) + 1 = 10 + 1 = 11

(b) Var(2X + 1) = 2²·Var(X) = 4·(9) = 36

(c) We know Var(X) = E(X²) − [E(X)]². Solve for E(X²):

E(X²) = Var(X) + [E(X)]² = 9 + 5² = 9 + 25 = 34

**Why the +1 does not affect variance:** Adding a constant shifts every value but does not change how far values are from the mean, so variance stays the same. The +1 disappears in the variance calculation.

---

### Answer 4

(a) The sum of probabilities must be 1:

c/1 + c/2 + c/3 = c·(1 + 1/2 + 1/3) = c·(6/6 + 3/6 + 2/6) = c·(11/6) = 1

So c = 6/11.

The PMF is: P(X = 1) = 6/11, P(X = 2) = 3/11, P(X = 3) = 2/11.

(b) E(X) = 1·(6/11) + 2·(3/11) + 3·(2/11) = (6 + 6 + 6)/11 = 18/11 ≈ 1.636

E(X²) = 1²·(6/11) + 2²·(3/11) + 3²·(2/11) = (6 + 12 + 18)/11 = 36/11

Var(X) = E(X²) − [E(X)]² = 36/11 − (18/11)² = 36/11 − 324/121

Convert to denominator 121: 36/11 = 396/121

Var(X) = 396/121 − 324/121 = 72/121 ≈ 0.595

---

### Answer 5

(a) There are 4 Aces, 4 Kings, and 44 other cards in the deck.

| Outcome | Net Profit x | P(X = x) |
|---|---|---|
| Ace | 10 | 4/52 = 1/13 |
| King | 5 | 4/52 = 1/13 |
| Other | −2 | 44/52 = 11/13 |

[2 marks]

(b) E(X) = 10·(1/13) + 5·(1/13) + (−2)·(11/13)

= (10 + 5 − 22)/13 = −7/13 ≈ −0.538

[2 marks]

(c) The game is **unfavorable** to the player because E(X) is negative. In practical terms, the player loses about $0.54 per game on average. If the player played 100 games, they would expect to lose about $54.

[2 marks]

(d) E(X²) = 10²·(1/13) + 5²·(1/13) + (−2)²·(11/13)

= 100·(1/13) + 25·(1/13) + 4·(11/13)

= (100 + 25 + 44)/13 = 169/13 = 13

Var(X) = E(X²) − [E(X)]² = 13 − (−7/13)² = 13 − 49/169

Convert 13 to 169ths: 13 = 2197/169

Var(X) = 2197/169 − 49/169 = 2148/169 ≈ 12.71

σ = √(2148/169) = √2148 / 13 ≈ 46.35 / 13 ≈ 3.57

[2 marks]

---

### Answer 6

(a) Out of 1000 tickets: 1 wins $500 (net $498), 2 win $100 (net $98 each), 997 win nothing (net −$2).

| Prize | Net Profit x | P(X = x) |
|---|---|---|
| $500 | 498 | 1/1000 |
| $100 | 98 | 2/1000 |
| None | −2 | 997/1000 |

(b) E(X) = 498·(1/1000) + 98·(2/1000) + (−2)·(997/1000)

= (498 + 196 − 1994)/1000 = −1300/1000 = −1.30

**Interpretation:** On average, a ticket holder loses $1.30 per $2 ticket. The expected net loss is $1.30, which means the lottery keeps 65% of the ticket revenue on average. This is why lotteries are profitable for the organizers — the expected value for a player is always negative.

