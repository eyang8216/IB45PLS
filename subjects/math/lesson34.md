# Lesson 34: Bayes' Theorem

---

## What Is Bayes' Theorem and Why Do We Need It?

Suppose a medical test for a disease is 95% accurate. If a patient tests positive, what are the chances they actually have the disease? You might guess 95%, but the real answer is often much lower. Why? Because the disease itself might be very rare.

Bayes' Theorem is a mathematical rule that helps us answer exactly this kind of question. It lets us "flip" a conditional probability: if we know the probability of a positive test *given* the disease, Bayes' Theorem tells us the probability of the disease *given* a positive test.

The theorem is named after Thomas Bayes, an 18th-century mathematician. It is one of the most powerful tools in probability because it shows us how to update our beliefs when we receive new evidence.

---

## The Basic Idea: Flipping a Conditional Probability

A **conditional probability** P(A | B) (read as "the probability of A given B") tells us how likely A is when we already know that B happened. In the previous lesson, you learned that:

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$$

This formula works forward: from condition B to outcome A. But sometimes we have the "reverse" information. For example, we might know:

- P(positive test | disease) — the test's detection rate.
- But we want P(disease | positive test) — what the patient actually cares about.

Bayes' Theorem gives us a way to compute this reverse probability.

---

## Deriving Bayes' Theorem

We start from the definition of conditional probability. For any two events A and B:

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)} \quad \text{and} \quad P(B \mid A) = \frac{P(A \cap B)}{P(A)}$$

Both formulas contain the same intersection P(A ∩ B) (the probability that both A and B happen). If we solve each for the intersection, we get:

$$P(A \cap B) = P(A \mid B) \cdot P(B) = P(B \mid A) \cdot P(A)$$

Now set the two equal and solve for P(B | A):

$$\boxed{P(B \mid A) = \frac{P(A \mid B) \cdot P(B)}{P(A)}}$$

This is **Bayes' Theorem**. The denominator P(A) can be expanded using the **Law of Total Probability**. If B and B′ (read as "not B") are the only two possibilities, then:

$$P(A) = P(A \mid B) \cdot P(B) + P(A \mid B') \cdot P(B')$$

Putting everything together gives the full two-event form of Bayes' Theorem:

$$\boxed{P(B \mid A) = \frac{P(A \mid B)\, P(B)}{P(A \mid B)\, P(B) + P(A \mid B')\, P(B')}}$$

---

## Important Vocabulary

When using Bayes' Theorem, the quantities have special names. Understanding these names helps you set up problems correctly.

- **Prior probability:** P(B) — your belief about B *before* you see the evidence A.
- **Likelihood:** P(A | B) — the probability of observing evidence A if B is true.
- **Posterior probability:** P(B | A) — your updated belief about B *after* seeing evidence A.
- **False positive:** Saying "positive" when the truth is negative — P(A | B′), where A is the evidence and B′ means "not B."

---

## Two Methods for Solving Bayes Problems

You can use the formula directly, or you can build a tree diagram or a table. Both methods are valid, but the tree/table method often makes it easier to see what is happening and reduces the chance of arithmetic mistakes. We will demonstrate both approaches.

---

## Worked Example 1: The Medical Test (Tree Method)

**Problem:** A disease affects 1% of the population. A test for the disease gives a positive result for 95% of people who have the disease. However, the test also returns a (false) positive for 10% of people who do not have the disease. A randomly chosen person takes the test and gets a positive result. What is the probability this person actually has the disease?

**Approach:** Let D mean "has the disease" and T⁺ mean "tests positive." We know:

- P(D) = 0.01 (prior — the disease is rare)
- P(T⁺ | D) = 0.95 (the test catches 95% of sick people)
- P(T⁺ | D′) = 0.10 (the test falsely alarms 10% of healthy people)

We want P(D | T⁺).

**Step 1: Build a tree.** Start at the root and branch according to whether the person has the disease or not. Then from each branch, split according to the test result.

```
                ┌── T⁺ (0.95)  →  P(D ∩ T⁺) = 0.01 × 0.95 = 0.0095
      ┌── D (0.01)
      │         └── T⁻ (0.05)  →  P(D ∩ T⁻) = 0.01 × 0.05 = 0.0005
Start │
      │         ┌── T⁺ (0.10)  →  P(D′ ∩ T⁺) = 0.99 × 0.10 = 0.0990
      └── D′ (0.99)
                └── T⁻ (0.90)  →  P(D′ ∩ T⁻) = 0.99 × 0.90 = 0.8910
```

**Step 2: Find P(D | T⁺).** By definition of conditional probability:

$$P(D \mid T^+) = \frac{P(D \cap T^+)}{P(T^+)}$$

The numerator P(D ∩ T⁺) = 0.0095. The denominator P(T⁺) is the sum of all paths that lead to T⁺: 0.0095 + 0.0990 = 0.1085.

$$P(D \mid T^+) = \frac{0.0095}{0.1085} \approx 0.0876$$

**Interpretation:** The probability is about 8.76%. This is surprisingly low! Even though the test is 95% accurate, the disease is so rare (only 1% of people have it) that most positive test results are actually false positives.

**Why this makes sense:** Imagine 1000 people. About 10 have the disease (1%), and about 9.5 of them test positive. About 990 do not have the disease, and about 99 of *them* test positive (10% false positive rate). So among the roughly 108.5 positive tests, only about 9.5 are true positives. The ratio 9.5/108.5 ≈ 8.76%.

**Common misconception:** People often confuse P(T⁺ | D) with P(D | T⁺). The test being "95% accurate" means P(T⁺ | D) = 0.95. It does NOT mean P(D | T⁺) = 0.95. These two probabilities are very different when the disease is rare.

---

## Worked Example 2: Two Factories (Table Method)

**Problem:** Factory A produces 60% of a company's light bulbs. Factory B produces the remaining 40%. Of the bulbs from Factory A, 2% are defective. Of the bulbs from Factory B, 5% are defective. A bulb is chosen at random from the combined output and is found to be defective. What is the probability it came from Factory A?

**Approach:** We want P(A | defective). We know:

- P(A) = 0.60, P(B) = 0.40
- P(defective | A) = 0.02, P(defective | B) = 0.05

**Step 1: Create a table with a convenient total.** Use 1000 bulbs as the total.

|  | Defective | Not Defective | Total |
|---|---|---|---|
| Factory A | 600 × 0.02 = 12 | 600 − 12 = 588 | 600 |
| Factory B | 400 × 0.05 = 20 | 400 − 20 = 380 | 400 |
| Total | 32 | 968 | 1000 |

**Step 2: Read the probability directly from the table.**

$$P(A \mid \text{defective}) = \frac{\text{defective from A}}{\text{all defective}} = \frac{12}{32} = \frac{3}{8} = 0.375$$

**Interpretation:** About 37.5% of defective bulbs come from Factory A. Even though Factory A has a lower defect rate (2% vs 5%), it produces more bulbs, so it still contributes a significant share of the defects.

**Why this makes sense:** The table makes the counting explicit. Out of 32 defective bulbs, we simply count how many came from Factory A (12). The ratio 12/32 gives the conditional probability directly.

---

## Worked Example 3: Screening Test with Two Stages

**Problem:** A school screens students for a condition. The condition affects 5% of students. The screening test has sensitivity 98% (probability of a positive test if the student has the condition) and specificity 93% (probability of a negative test if the student does not have the condition). Find the probability that a student who tests positive actually has the condition.

**Approach:** Let C mean "has the condition." We know:

- P(C) = 0.05, P(C′) = 0.95
- P(T⁺ | C) = 0.98 (sensitivity)
- P(T⁻ | C′) = 0.93 (specificity), so P(T⁺ | C′) = 1 − 0.93 = 0.07

**Step 1: Apply Bayes' Theorem.**

$$P(C \mid T^+) = \frac{P(T^+ \mid C)\,P(C)}{P(T^+ \mid C)\,P(C) + P(T^+ \mid C')\,P(C')}$$

**Step 2: Substitute the numbers.**

$$P(C \mid T^+) = \frac{0.98 \times 0.05}{0.98 \times 0.05 + 0.07 \times 0.95} = \frac{0.049}{0.049 + 0.0665} = \frac{0.049}{0.1155} \approx 0.424$$

**Interpretation:** About 42.4%. Even with a high-sensitivity test (98%) and decent specificity (93%), only about 42% of positive test results are true positives. The condition is uncommon enough (5%) that false positives still matter.

---

## General Bayes' Theorem: More Than Two Causes

Sometimes there are more than two categories. If events B₁, B₂, …, Bₙ form a **partition** of the sample space (meaning they are mutually exclusive and together cover all possibilities), then:

$$P(B_k \mid A) = \frac{P(A \mid B_k)\,P(B_k)}{\displaystyle\sum_{i=1}^{n} P(A \mid B_i)\,P(B_i)}$$

The formula looks intimidating, but the idea is the same: the numerator is the probability of the one path you care about, and the denominator is the sum of probabilities of all paths that lead to A.

---

## Practice Problems

---

### Problem 1
A box contains 3 fair coins and 2 biased coins. A fair coin lands heads with probability 0.5. A biased coin lands heads with probability 0.8. A coin is chosen at random from the box and flipped. It lands heads.

(a) Draw a tree diagram showing all branches, their probabilities, and the intersection probabilities at the end of each path.

(b) Find the probability that the chosen coin was biased, given that it landed heads.

---

### Problem 2
A disease affects 2% of the population. A test gives a positive result for 99% of people who have the disease. However, the test also gives a (false) positive for 3% of people who do not have the disease.

(a) What proportion of all tests come back positive? In other words, find P(T⁺).

(b) If a randomly chosen person tests positive, what is the probability they actually have the disease?

---

### Problem 3
Urn I contains 4 white balls and 6 black balls. Urn II contains 7 white balls and 3 black balls. You first choose an urn at random (each urn is equally likely). Then you draw one ball from the chosen urn.

(a) Find the overall probability of drawing a white ball, P(white).

(b) Given that the ball drawn is white, find the probability it came from Urn II.

---

### Problem 4
On rainy days, the probability Sam is late for school is 0.4. On dry days, the probability Sam is late is 0.1. The probability of rain on any given day is 0.25. Sam arrives late to school today. What is the probability that it is raining?

---

### Problem 5 (IB Exam Style — 6 marks)
A factory has three machines: X, Y, and Z. Machine X produces 50% of the items and has a defect rate of 1%. Machine Y produces 30% and has a defect rate of 3%. Machine Z produces 20% and has a defect rate of 5%.

A randomly selected item from the factory's output is found to be defective.

(a) [1 mark] Calculate the total probability that a randomly selected item is defective.

(b) [3 marks] Find the probability the defective item came from Machine X.

(c) [2 marks] Find the probability the defective item came from Machine Z, and explain why the result makes sense even though Machine Z has the highest defect rate.

---

## Answers

---

### Answer 1

(a) **Tree diagram:**

```
                ┌── H (0.5)  →  P(Fair ∩ H) = 0.6 × 0.5 = 0.30
      ┌── Fair (3/5 = 0.6)
      │         └── T (0.5)  →  P(Fair ∩ T) = 0.6 × 0.5 = 0.30
Start │
      │         ┌── H (0.8)  →  P(Biased ∩ H) = 0.4 × 0.8 = 0.32
      └── Biased (2/5 = 0.4)
                └── T (0.2)  →  P(Biased ∩ T) = 0.4 × 0.2 = 0.08
```

(b) P(Biased | H) is the intersection probability for biased-and-heads divided by the total probability of heads:

$$P(\text{Biased} \mid H) = \frac{P(\text{Biased} \cap H)}{P(H)} = \frac{0.32}{0.30 + 0.32} = \frac{0.32}{0.62} = \frac{32}{62} = \frac{16}{31} \approx 0.516$$

**Interpretation:** Given a head, the coin is slightly more likely to be biased than fair (about 51.6% vs 48.4%). This makes sense because biased coins produce heads more often, but fair coins are more numerous (3 vs 2), so the two effects nearly balance.

---

### Answer 2

Let D = has disease, T⁺ = positive test. Given: P(D) = 0.02, P(T⁺ | D) = 0.99, P(T⁺ | D′) = 0.03.

(a) **P(T⁺):** Use the Law of Total Probability.

P(T⁺) = P(T⁺ | D)·P(D) + P(T⁺ | D′)·P(D′) = 0.99 × 0.02 + 0.03 × 0.98 = 0.0198 + 0.0294 = 0.0492.

So 4.92% of all tests come back positive.

(b) **P(D | T⁺):** Apply Bayes' Theorem.

$$P(D \mid T^+) = \frac{P(T^+ \mid D)\,P(D)}{P(T^+)} = \frac{0.0198}{0.0492} \approx 0.4024$$

**Interpretation:** About 40.2% of positive tests are true positives. Even with a 99% accurate test for detecting the disease, the rarity of the disease (2%) means more than half of positive results are false positives.

**Pitfall:** Students often compute the denominator incorrectly by forgetting to include the false positive path. Every path that leads to T⁺ must be summed in the denominator.

---

### Answer 3

(a) **P(white):** Use the Law of Total Probability.

P(white) = P(white | I)·P(I) + P(white | II)·P(II) = (4/10)·(1/2) + (7/10)·(1/2) = 0.4·0.5 + 0.7·0.5 = 0.2 + 0.35 = 0.55.

(b) **P(II | white):** Apply Bayes' Theorem.

$$P(II \mid \text{white}) = \frac{P(\text{white} \mid II)\,P(II)}{P(\text{white})} = \frac{0.7 \times 0.5}{0.55} = \frac{0.35}{0.55} = \frac{35}{55} = \frac{7}{11} \approx 0.636$$

**Interpretation:** Given a white ball, there is about a 63.6% chance it came from Urn II. This is higher than 50% (the prior) because Urn II has a higher proportion of white balls (70% vs 40%). The evidence (white) shifts the probability toward Urn II.

---

### Answer 4

Let R = rain, L = late. Given: P(R) = 0.25, P(L | R) = 0.4, P(L | R′) = 0.1.

**Apply Bayes' Theorem:**

P(R | L) = [P(L | R)·P(R)] / [P(L | R)·P(R) + P(L | R′)·P(R′)]

= (0.4 × 0.25) / (0.4 × 0.25 + 0.1 × 0.75) = 0.10 / (0.10 + 0.075) = 0.10 / 0.175.

Simplify: 0.10 / 0.175 = 100/175 = 4/7 ≈ 0.571.

**Interpretation:** There is about a 57.1% chance it is raining given that Sam is late. Before knowing Sam was late, the probability of rain was only 25%. The observation that Sam is late raises the rain probability substantially, because Sam is much more likely to be late on rainy days (0.4) than on dry days (0.1).

---

### Answer 5

(a) **Total defect probability:**

P(D) = P(D | X)·P(X) + P(D | Y)·P(Y) + P(D | Z)·P(Z)

= 0.01 × 0.50 + 0.03 × 0.30 + 0.05 × 0.20 = 0.005 + 0.009 + 0.010 = 0.024.

So 2.4% of all items are defective. [1 mark]

(b) **P(X | D):** Using Bayes' Theorem:

P(X | D) = [P(D | X)·P(X)] / P(D) = 0.005 / 0.024 = 5/24 ≈ 0.208. [3 marks]

(c) **P(Z | D):** P(Z | D) = 0.010 / 0.024 = 10/24 = 5/12 ≈ 0.417.

[2 marks]

**Why it makes sense:** Machine Z has the highest defect rate (5%), and it produces a small share (20%). But when an item *is* defective, Z is the most likely source (41.7%) because its defect rate is five times X's rate. Even though Z produces fewer items, the ones it does produce are much more likely to be defective, so Z dominates the defective pool. Machine X, despite producing half of all items, accounts for only 20.8% of defects because its defect rate is so low.

Check: 5/24 + 9/24 + 10/24 = 24/24 = 1. All probabilities sum to 1, as they should since the defective item must come from one of the three machines.

