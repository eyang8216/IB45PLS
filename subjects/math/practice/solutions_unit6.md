# Unit 6: Proof & Probability — Solutions

---

## Problem 1

**Approach:** Use mathematical induction. Verify the base case \(n = 1\), then assume the formula holds for \(n = k\) and prove it holds for \(n = k + 1\) by adding the \((k+1)\)-th term and simplifying.

**Base case (\(n = 1\)):**

\[
\text{LHS} = \sum_{r=1}^{1} r(r+1) = 1 \cdot 2 = 2.
\]

\[
\text{RHS} = \frac{1(1+1)(1+2)}{3} = \frac{1 \cdot 2 \cdot 3}{3} = 2.
\]

LHS = RHS, so the formula holds for \(n = 1\).

**Inductive hypothesis:** Assume the formula holds for some positive integer \(n = k\). That is,

\[
\sum_{r=1}^{k} r(r+1) = \frac{k(k+1)(k+2)}{3}.
\]

**Inductive step:** We must prove the formula holds for \(n = k + 1\).

\[
\begin{aligned}
\sum_{r=1}^{k+1} r(r+1) &= \left( \sum_{r=1}^{k} r(r+1) \right) + (k+1)(k+2) \\[4pt]
&= \frac{k(k+1)(k+2)}{3} + (k+1)(k+2) \quad \text{(by inductive hypothesis)} \\[4pt]
&= (k+1)(k+2) \left( \frac{k}{3} + 1 \right) \\[4pt]
&= (k+1)(k+2) \left( \frac{k+3}{3} \right) \\[4pt]
&= \frac{(k+1)(k+2)(k+3)}{3}.
\end{aligned}
\]

This is exactly \(\frac{(k+1)\big((k+1)+1\big)\big((k+1)+2\big)}{3}\), which is the formula with \(n = k+1\).

**Conclusion:** By the principle of mathematical induction, the formula holds for all positive integers \(n\).

**Answer:** \(\displaystyle\sum_{r=1}^{n} r(r+1) = \frac{n(n+1)(n+2)}{3}\) for all \(n \in \mathbb{Z}^+\).

---

## Problem 2

**Approach:** Use induction. The base case is \(n = 1\). For the inductive step, express \(5^{k+1} - 3^{k+1}\) in terms of \(5^k - 3^k\) to show divisibility by 2 is preserved.

**Base case (\(n = 1\)):**

\[
5^1 - 3^1 = 5 - 3 = 2.
\]

2 is divisible by 2, so the statement holds for \(n = 1\).

**Inductive hypothesis:** Assume that for some positive integer \(n = k\),

\[
5^k - 3^k = 2m \quad \text{for some integer } m.
\]

**Inductive step:** Prove the statement for \(n = k + 1\).

\[
\begin{aligned}
5^{k+1} - 3^{k+1} &= 5 \cdot 5^k - 3 \cdot 3^k \\
&= 5 \cdot 5^k - 5 \cdot 3^k + 5 \cdot 3^k - 3 \cdot 3^k \quad \text{(adding and subtracting } 5 \cdot 3^k\text{)} \\
&= 5(5^k - 3^k) + 3^k(5 - 3) \\
&= 5(2m) + 3^k \cdot 2 \quad \text{(by inductive hypothesis)} \\
&= 2(5m + 3^k).
\end{aligned}
\]

Since \(5m + 3^k\) is an integer, \(5^{k+1} - 3^{k+1}\) is an integer multiple of 2, i.e., divisible by 2.

**Conclusion:** By mathematical induction, \(5^n - 3^n\) is divisible by 2 for all \(n \in \mathbb{Z}^+\).

**Answer:** \(5^n - 3^n\) is divisible by 2 for all positive integers \(n\).

---

## Problem 3

**Approach:** Use induction with base case \(n = 5\). For the inductive step, we need to show that if \(2^k > k^2\) then \(2^{k+1} > (k+1)^2\). This involves showing \(2k^2 > (k+1)^2\) for \(k \geq 5\).

**Base case (\(n = 5\)):**

\[
2^5 = 32, \quad 5^2 = 25.
\]

Since \(32 > 25\), the inequality holds for \(n = 5\).

**Inductive hypothesis:** Assume that for some integer \(k \geq 5\),

\[
2^k > k^2.
\]

**Inductive step:** Prove that \(2^{k+1} > (k+1)^2\).

\[
\begin{aligned}
2^{k+1} &= 2 \cdot 2^k \\
&> 2 \cdot k^2 \quad \text{(by inductive hypothesis)}.
\end{aligned}
\]

Now we need to show that \(2k^2 > (k+1)^2\) for \(k \geq 5\).

\[
\begin{aligned}
2k^2 - (k+1)^2 &= 2k^2 - (k^2 + 2k + 1) \\
&= k^2 - 2k - 1 \\
&= (k-1)^2 - 2.
\end{aligned}
\]

For \(k \geq 5\), we have \(k-1 \geq 4\), so \((k-1)^2 \geq 16\), and therefore \((k-1)^2 - 2 \geq 14 > 0\). Thus \(2k^2 > (k+1)^2\) for all \(k \geq 5\).

Putting this together:

\[
2^{k+1} > 2k^2 > (k+1)^2.
\]

**Conclusion:** By mathematical induction, \(2^n > n^2\) for all integers \(n \geq 5\).

**Answer:** \(2^n > n^2\) for all integers \(n \geq 5\).

---

## Problem 4

**Approach:** Use induction on the power of the matrix. Verify \(n = 1\), then assume the formula for \(n = k\) and multiply by \(A\) to obtain the formula for \(n = k + 1\).

**Base case (\(n = 1\)):**

\[
A^1 = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 2 \cdot 1 \\ 0 & 1 \end{pmatrix}.
\]

The formula holds for \(n = 1\).

**Inductive hypothesis:** Assume that for some \(n = k\),

\[
A^k = \begin{pmatrix} 1 & 2k \\ 0 & 1 \end{pmatrix}.
\]

**Inductive step:** Prove the formula holds for \(n = k + 1\).

\[
\begin{aligned}
A^{k+1} &= A^k \cdot A \\
&= \begin{pmatrix} 1 & 2k \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} \\
&= \begin{pmatrix} 1 \cdot 1 + 2k \cdot 0 & 1 \cdot 2 + 2k \cdot 1 \\ 0 \cdot 1 + 1 \cdot 0 & 0 \cdot 2 + 1 \cdot 1 \end{pmatrix} \\
&= \begin{pmatrix} 1 & 2 + 2k \\ 0 & 1 \end{pmatrix} \\
&= \begin{pmatrix} 1 & 2(k+1) \\ 0 & 1 \end{pmatrix}.
\end{aligned}
\]

**Conclusion:** By mathematical induction, the formula holds for all positive integers \(n\).

**Answer:** \(A^n = \begin{pmatrix} 1 & 2n \\ 0 & 1 \end{pmatrix}\) for all \(n \in \mathbb{Z}^+\).

---

## Problem 5

**Approach:** For part (a), draw a tree with first draw and second draw branching. For (b), sum probabilities of two same-colour paths. For (c), use the conditional probability directly from the tree.

**(a) Tree diagram:**

```
                    ┌─── R (4/11)
    ┌─── R (5/12) ──┤
    │               └─── B (7/11)
───┤
    │               ┌─── R (5/11)
    └─── B (7/12) ──┤
                    └─── B (6/11)
```

There are 5 red marbles and 7 blue marbles, giving a total of \(5 + 7 = 12\) marbles. On the first draw, P(Red) = \(\frac{5}{12}\) and P(Blue) = \(\frac{7}{12}\).

If the first marble drawn is red, there are 4 red and 7 blue marbles left (11 total). So P(Red | first Red) = \(\frac{4}{11}\) and P(Blue | first Red) = \(\frac{7}{11}\).

If the first marble drawn is blue, there are 5 red and 6 blue marbles left (11 total). So P(Red | first Blue) = \(\frac{5}{11}\) and P(Blue | first Blue) = \(\frac{6}{11}\).

**(b) Probability that both marbles are the same colour:**

This happens in two mutually exclusive ways: both red (RR) or both blue (BB).

\[
\begin{aligned}
P(\text{same colour}) &= P(\text{RR}) + P(\text{BB}) \\
&= \frac{5}{12} \cdot \frac{4}{11} + \frac{7}{12} \cdot \frac{6}{11} \\
&= \frac{20}{132} + \frac{42}{132} \\
&= \frac{62}{132} \\
&= \frac{31}{66}.
\end{aligned}
\]

**(c) Probability that the second marble is red given that the first was blue:**

This is read directly from the tree: if the first is blue, there are 5 red out of 11 remaining marbles.

\[
P(\text{second is Red} \mid \text{first is Blue}) = \frac{5}{11}.
\]

**Answer:** (b) \(\frac{31}{66}\)  (c) \(\frac{5}{11}\)

---

## Problem 6

**Approach:** Use the addition rule for unions, the definition of conditional probability, and the test for independence.

Let \(C\) be the event "owns a car" and \(B\) be the event "owns a bicycle."

Given: \(P(C) = 0.7\), \(P(B) = 0.4\), \(P(C \cap B) = 0.25\).

**(a) Probability of owning a car or a bicycle (or both):**

Using the addition rule:

\[
\begin{aligned}
P(C \cup B) &= P(C) + P(B) - P(C \cap B) \\
&= 0.7 + 0.4 - 0.25 \\
&= 0.85.
\end{aligned}
\]

**(b) Probability of owning a car given that the resident owns a bicycle:**

Using the definition of conditional probability:

\[
\begin{aligned}
P(C \mid B) &= \frac{P(C \cap B)}{P(B)} \\
&= \frac{0.25}{0.4} \\
&= 0.625.
\end{aligned}
\]

**(c) Independence check:**

Events \(C\) and \(B\) are independent if and only if \(P(C \cap B) = P(C) \cdot P(B)\).

\[
P(C) \cdot P(B) = 0.7 \times 0.4 = 0.28.
\]

But \(P(C \cap B) = 0.25\), which is not equal to 0.28.

Therefore the events are **not independent**. The fact that \(P(C \cap B) < P(C) \cdot P(B)\) indicates that owning a car and owning a bicycle are negatively associated in this town.

**Answer:** (a) 0.85  (b) 0.625  (c) Not independent, since \(P(C \cap B) = 0.25 \neq 0.28 = P(C) \cdot P(B)\).

---

## Problem 7

**Approach:** Construct a tree with disease status first, then test result. Use the law of total probability for part (b) and Bayes' theorem for part (c).

Let \(D\) be "has the disease" and \(+\) be "tests positive."

Given:
- \(P(+ \mid D) = 0.98\) (sensitivity)
- \(P(- \mid D') = 0.95\) ⇒ \(P(+ \mid D') = 0.05\) (false positive rate)
- \(P(D) = 0.01\) (prevalence)

**(a) Tree diagram:**

```
                    ┌─── Positive (0.98)
    ┌─── D (0.01) ──┤
    │               └─── Negative (0.02)
───┤
    │               ┌─── Positive (0.05)
    └─── D' (0.99) ─┤
                    └─── Negative (0.95)
```

**(b) Probability that a randomly selected person tests positive:**

Using the law of total probability:

\[
\begin{aligned}
P(+) &= P(+ \mid D) \cdot P(D) + P(+ \mid D') \cdot P(D') \\
&= 0.98 \times 0.01 + 0.05 \times 0.99 \\
&= 0.0098 + 0.0495 \\
&= 0.0593.
\end{aligned}
\]

**(c) Probability of having the disease given a positive test (Bayes' theorem):**

\[
\begin{aligned}
P(D \mid +) &= \frac{P(+ \mid D) \cdot P(D)}{P(+)} \\
&= \frac{0.98 \times 0.01}{0.0593} \\
&= \frac{0.0098}{0.0593} \\
&\approx 0.1653.
\end{aligned}
\]

**(d) Comment:**

The probability that a person actually has the disease given a positive test result is only about 16.5%. This surprisingly low value occurs because the disease is very rare (only 1% of the population has it). Despite the test having a high sensitivity (98%), the number of false positives among the large healthy population (5% of 99% = 4.95% of the population) greatly outnumbers the true positives (98% of 1% = 0.98% of the population). This is a classic illustration of the importance of base rates (prevalence) when interpreting diagnostic test results.

**Answer:** (b) 0.0593  (c) ≈0.1653  (d) See comment above.

---

## Problem 8

**Approach:** Use the law of total probability for part (a), Bayes' theorem for part (b), and a variant using complements for part (c).

Let \(A\), \(B\), \(C\) be the events that an item comes from machine A, B, or C, and let \(D\) be the event that the item is defective.

Given:
- \(P(A) = 0.30\), \(P(B) = 0.45\), \(P(C) = 0.25\)
- \(P(D \mid A) = 0.02\), \(P(D \mid B) = 0.03\), \(P(D \mid C) = 0.01\)

**(a) Probability that a randomly selected item is defective:**

\[
\begin{aligned}
P(D) &= P(D \mid A)P(A) + P(D \mid B)P(B) + P(D \mid C)P(C) \\
&= 0.02 \times 0.30 + 0.03 \times 0.45 + 0.01 \times 0.25 \\
&= 0.006 + 0.0135 + 0.0025 \\
&= 0.022.
\end{aligned}
\]

**(b) Probability that a defective item came from machine B:**

Using Bayes' theorem:

\[
\begin{aligned}
P(B \mid D) &= \frac{P(D \mid B) \cdot P(B)}{P(D)} \\
&= \frac{0.03 \times 0.45}{0.022} \\
&= \frac{0.0135}{0.022} \\
&= \frac{27}{44} \approx 0.6136.
\end{aligned}
\]

**(c) Probability that a non-defective item came from machine C:**

First, \(P(D') = 1 - P(D) = 1 - 0.022 = 0.978\).

Also, \(P(D' \mid C) = 1 - P(D \mid C) = 1 - 0.01 = 0.99\).

\[
\begin{aligned}
P(C \mid D') &= \frac{P(D' \mid C) \cdot P(C)}{P(D')} \\
&= \frac{0.99 \times 0.25}{0.978} \\
&= \frac{0.2475}{0.978} \\
&\approx 0.2531.
\end{aligned}
\]

**Answer:** (a) 0.022  (b) \(\frac{27}{44} \approx 0.6136\)  (c) ≈0.2531

---

## Problem 9

**Approach:** Compute \(E(X)\) directly from the probability distribution table. Then compute \(E(X^2)\) similarly and use \(\operatorname{Var}(X) = E(X^2) - [E(X)]^2\).

Given distribution:

| \(x\) | 0 | 1 | 2 | 3 |
|-------|---|---|---|---|
| \(P(X = x)\) | 0.1 | 0.3 | 0.4 | 0.2 |

**(a) Find \(E(X)\):**

\[
\begin{aligned}
E(X) &= \sum x \cdot P(X = x) \\
&= 0 \times 0.1 + 1 \times 0.3 + 2 \times 0.4 + 3 \times 0.2 \\
&= 0 + 0.3 + 0.8 + 0.6 \\
&= 1.7.
\end{aligned}
\]

**(b) Find \(E(X^2)\):**

\[
\begin{aligned}
E(X^2) &= \sum x^2 \cdot P(X = x) \\
&= 0^2 \times 0.1 + 1^2 \times 0.3 + 2^2 \times 0.4 + 3^2 \times 0.2 \\
&= 0 + 0.3 + 1.6 + 1.8 \\
&= 3.7.
\end{aligned}
\]

**(c) Find \(\operatorname{Var}(X)\):**

\[
\begin{aligned}
\operatorname{Var}(X) &= E(X^2) - [E(X)]^2 \\
&= 3.7 - (1.7)^2 \\
&= 3.7 - 2.89 \\
&= 0.81.
\end{aligned}
\]

**Answer:** (a) 1.7  (b) 3.7  (c) 0.81

---

## Problem 10

**Approach:** The die roll gives scores 1 through 6, each with probability \(\frac{1}{6}\). Square each to find the possible values of \(X\), then compute \(E(X)\) and \(E(X^2)\) and use \(\operatorname{Var}(X) = E(X^2) - [E(X)]^2\).

**(a) Probability distribution of \(X\):**

The possible scores are 1, 2, 3, 4, 5, 6, so \(X = (\text{score})^2\) takes values 1, 4, 9, 16, 25, 36, each with probability \(\frac{1}{6}\).

\[
\begin{array}{c|cccccc}
x & 1 & 4 & 9 & 16 & 25 & 36 \\
\hline
P(X = x) & \frac{1}{6} & \frac{1}{6} & \frac{1}{6} & \frac{1}{6} & \frac{1}{6} & \frac{1}{6}
\end{array}
\]

**(b) Compute \(E(X)\):**

\[
\begin{aligned}
E(X) &= \sum x \cdot P(X = x) \\
&= \frac{1}{6}(1 + 4 + 9 + 16 + 25 + 36) \\
&= \frac{91}{6} \approx 15.17.
\end{aligned}
\]

**(c) Compute \(\operatorname{Var}(X)\):**

First compute \(E(X^2)\):

\[
\begin{aligned}
E(X^2) &= \sum x^2 \cdot P(X = x) \\
&= \frac{1}{6}(1^2 + 4^2 + 9^2 + 16^2 + 25^2 + 36^2) \\
&= \frac{1}{6}(1 + 16 + 81 + 256 + 625 + 1296) \\
&= \frac{2275}{6}.
\end{aligned}
\]

Then:

\[
\begin{aligned}
\operatorname{Var}(X) &= E(X^2) - [E(X)]^2 \\
&= \frac{2275}{6} - \left(\frac{91}{6}\right)^2 \\
&= \frac{2275}{6} - \frac{8281}{36} \\
&= \frac{13650 - 8281}{36} \\
&= \frac{5369}{36} \approx 149.14.
\end{aligned}
\]

**Answer:** (a) See table above.  (b) \(\frac{91}{6} \approx 15.17\)  (c) \(\frac{5369}{36} \approx 149.14\)

---

## Problem 11

**Approach:** This is a binomial distribution. Use the formula \(P(X = r) = \binom{n}{r} p^r (1-p)^{n-r}\). For \(P(X \geq 3)\), use the complement \(1 - P(X \leq 2)\).

**(a) Distribution of \(X\):**

\(X \sim B(8, 0.5)\). That is, \(X\) follows a binomial distribution with \(n = 8\) trials and probability of success (heads) \(p = 0.5\).

**(b) Find \(P(X = 5)\):**

\[
\begin{aligned}
P(X = 5) &= \binom{8}{5} (0.5)^5 (0.5)^{3} \\
&= 56 \times (0.5)^8 \\
&= \frac{56}{256} \\
&= \frac{7}{32} = 0.21875.
\end{aligned}
\]

**(c) Find \(P(X \geq 3)\):**

\[
\begin{aligned}
P(X \geq 3) &= 1 - P(X \leq 2) \\
&= 1 - [P(X = 0) + P(X = 1) + P(X = 2)].
\end{aligned}
\]

Compute each term:

\[
\begin{aligned}
P(X = 0) &= \binom{8}{0} (0.5)^8 = \frac{1}{256}, \\
P(X = 1) &= \binom{8}{1} (0.5)^8 = \frac{8}{256}, \\
P(X = 2) &= \binom{8}{2} (0.5)^8 = \frac{28}{256}.
\end{aligned}
\]

\[
P(X \leq 2) = \frac{1 + 8 + 28}{256} = \frac{37}{256} \approx 0.14453.
\]

\[
P(X \geq 3) = 1 - \frac{37}{256} = \frac{219}{256} \approx 0.8555.
\]

**(d) State \(E(X)\) and \(\operatorname{Var}(X)\):**

For a binomial distribution \(B(n, p)\):

\[
E(X) = np = 8 \times 0.5 = 4.
\]

\[
\operatorname{Var}(X) = np(1-p) = 8 \times 0.5 \times 0.5 = 2.
\]

**Answer:** (a) \(X \sim B(8, 0.5)\)  (b) \(\frac{7}{32} = 0.21875\)  (c) \(\frac{219}{256} \approx 0.8555\)  (d) \(E(X) = 4\), \(\operatorname{Var}(X) = 2\)

---

## Problem 12

**Approach:** This is a binomial distribution with \(n = 20\), \(p = 0.25\). Use the binomial probability formula and the complement rule for cumulative probabilities.

**(a) Distribution of \(Y\):**

\(Y \sim B(20, 0.25)\). There are \(n = 20\) independent questions, each with probability of success (guessing correctly) \(p = \frac{1}{4} = 0.25\).

**(b) Find the probability of exactly 6 correct:**

\[
\begin{aligned}
P(Y = 6) &= \binom{20}{6} (0.25)^6 (0.75)^{14}.
\end{aligned}
\]

First, \(\binom{20}{6} = \frac{20 \times 19 \times 18 \times 17 \times 16 \times 15}{6 \times 5 \times 4 \times 3 \times 2 \times 1} = 38760\).

\[
\begin{aligned}
P(Y = 6) &= 38760 \times (0.25)^6 \times (0.75)^{14} \\
&\approx 0.1686.
\end{aligned}
\]

**(c) Find the probability of at least 10 correct:**

\[
P(Y \geq 10) = \sum_{k=10}^{20} \binom{20}{k} (0.25)^k (0.75)^{20-k} \approx 0.01386.
\]

**(d) Find \(E(Y)\) and \(\operatorname{Var}(Y)\):**

\[
E(Y) = np = 20 \times 0.25 = 5.
\]

\[
\operatorname{Var}(Y) = np(1-p) = 20 \times 0.25 \times 0.75 = 3.75.
\]

**Answer:** (a) \(Y \sim B(20, 0.25)\)  (b) ≈0.1686  (c) ≈0.0139  (d) \(E(Y) = 5\), \(\operatorname{Var}(Y) = 3.75\)

---

## Problem 13

**Approach:** Use the standard normal distribution table (or calculator). Standardize where necessary (though here \(Z\) is already standard normal).

**(a) Find \(P(Z < 1.25)\):**

From the standard normal table, \(\Phi(1.25) \approx 0.8944\).

\[
P(Z < 1.25) = 0.8944.
\]

**(b) Find \(P(-0.8 < Z < 1.5)\):**

\[
\begin{aligned}
P(-0.8 < Z < 1.5) &= \Phi(1.5) - \Phi(-0.8) \\
&= \Phi(1.5) - [1 - \Phi(0.8)] \\
&= 0.9332 - (1 - 0.7881) \\
&= 0.9332 - 0.2119 \\
&= 0.7213.
\end{aligned}
\]

**(c) Find \(c\) such that \(P(Z > c) = 0.05\):**

This means \(\Phi(c) = 0.95\). The 95th percentile of the standard normal distribution is \(c \approx 1.6449\).

\[
P(Z > 1.6449) = 0.05.
\]

**Answer:** (a) 0.8944  (b) 0.7213  (c) \(c = 1.6449\)

---

## Problem 14

**Approach:** Let \(H \sim N(175, 7^2)\). Standardize to \(Z\)-scores: \(Z = \frac{H - 175}{7}\). Then use the standard normal table.

**(a) Probability that height is less than 168 cm:**

\[
Z = \frac{168 - 175}{7} = \frac{-7}{7} = -1.00.
\]

\[
P(H < 168) = P(Z < -1.00) = 1 - \Phi(1.00) = 1 - 0.8413 = 0.1587.
\]

**(b) Probability that height is between 170 cm and 185 cm:**

\[
Z_1 = \frac{170 - 175}{7} \approx -0.7143, \quad Z_2 = \frac{185 - 175}{7} \approx 1.4286.
\]

\[
\begin{aligned}
P(170 < H < 185) &= P(-0.7143 < Z < 1.4286) \\
&= \Phi(1.4286) - \Phi(-0.7143) \\
&\approx 0.9234 - (1 - 0.7625) \\
&= 0.9234 - 0.2375 \\
&= 0.6859.
\end{aligned}
\]

**(c) Height above which the tallest 10% fall:**

We need \(h\) such that \(P(H > h) = 0.10\). Equivalently, \(P(H < h) = 0.90\).

The 90th percentile of the standard normal distribution is \(z_{0.90} \approx 1.2816\).

\[
h = \mu + z_{0.90} \cdot \sigma = 175 + 1.2816 \times 7 = 175 + 8.9712 = 183.97 \text{ cm}.
\]

**Answer:** (a) 0.1587  (b) 0.6859  (c) 183.97 cm

---

## Problem 15

**Approach:** Let \(M \sim N(150, 20^2)\). For (a), standardize and use the normal table. For (b), treat "small" as a binomial event with \(p\) from part (a). For (c), find the 10th percentile.

**(a) Proportion of apples classified as small (mass < 120 g):**

\[
Z = \frac{120 - 150}{20} = \frac{-30}{20} = -1.50.
\]

\[
P(M < 120) = P(Z < -1.50) = 1 - \Phi(1.50) = 1 - 0.9332 = 0.0668.
\]

So approximately 6.68% of apples are classified as small.

**(b) Probability that exactly 2 out of 5 are small:**

Let \(p = 0.0668\) (from part (a)). The number of small apples in a sample of 5 follows \(X \sim B(5, p)\).

\[
\begin{aligned}
P(X = 2) &= \binom{5}{2} \cdot p^2 \cdot (1-p)^3 \\
&= 10 \times (0.0668)^2 \times (0.9332)^3 \\
&\approx 10 \times 0.004462 \times 0.8127 \\
&\approx 0.0363.
\end{aligned}
\]

**(c) Mass \(m\) such that 90% of apples have mass greater than \(m\):**

This means \(P(M > m) = 0.90\), so \(P(M < m) = 0.10\). The 10th percentile of the standard normal distribution is \(z_{0.10} \approx -1.2816\).

\[
m = 150 + (-1.2816) \times 20 = 150 - 25.632 = 124.37 \text{ g}.
\]

**Answer:** (a) 0.0668 (6.68%)  (b) ≈0.0363  (c) 124.37 g

---

## Problem 16

**Approach:** Let \(X \sim \text{Poisson}(4.5)\). Use the Poisson probability formula \(P(X = k) = \frac{e^{-\lambda}\lambda^k}{k!}\).

**(a) Probability of exactly 3 calls:**

\[
\begin{aligned}
P(X = 3) &= \frac{e^{-4.5} \cdot (4.5)^3}{3!} \\
&= \frac{e^{-4.5} \cdot 91.125}{6} \\
&\approx 0.1687.
\end{aligned}
\]

**(b) Probability of at most 2 calls:**

\[
\begin{aligned}
P(X \leq 2) &= P(X = 0) + P(X = 1) + P(X = 2) \\
&= e^{-4.5} \left( \frac{4.5^0}{0!} + \frac{4.5^1}{1!} + \frac{4.5^2}{2!} \right) \\
&= e^{-4.5} \left( 1 + 4.5 + \frac{20.25}{2} \right) \\
&= e^{-4.5} (1 + 4.5 + 10.125) \\
&= e^{-4.5} \times 15.625 \\
&\approx 0.1736.
\end{aligned}
\]

**(c) Probability of more than 5 calls:**

\[
\begin{aligned}
P(X > 5) &= 1 - P(X \leq 5) \\
&= 1 - e^{-4.5} \left( 1 + 4.5 + \frac{4.5^2}{2} + \frac{4.5^3}{6} + \frac{4.5^4}{24} + \frac{4.5^5}{120} \right) \\
&= 1 - e^{-4.5} \big( 1 + 4.5 + 10.125 + 15.1875 + 17.0859 + 15.3773 \big) \\
&= 1 - e^{-4.5} \times 63.2757 \\
&\approx 1 - 0.7029 \\
&= 0.2971.
\end{aligned}
\]

**Answer:** (a) ≈0.1687  (b) ≈0.1736  (c) ≈0.2971

---

## Problem 17

**Approach:** A binomial distribution \(B(n, p)\) can be approximated by a Poisson distribution \(\text{Poisson}(\lambda)\) with \(\lambda = np\) when \(n\) is large and \(p\) is small. Use the Poisson formula.

**(a) Explanation:**

The binomial distribution \(X \sim B(300, 0.02)\) satisfies the conditions for a Poisson approximation:
- \(n = 300\) is large.
- \(p = 0.02\) is small.
- \(\lambda = np = 300 \times 0.02 = 6\) is moderate (not too large or too small).

Under these conditions, the binomial probabilities are well approximated by a Poisson distribution with the same mean.

**(b) Parameter of the approximating Poisson distribution:**

\[
\lambda = np = 300 \times 0.02 = 6.
\]

So we use \(X \approx \text{Poisson}(6)\).

**(c) \(P(X \leq 4)\) using the Poisson approximation:**

\[
\begin{aligned}
P(X \leq 4) &\approx e^{-6} \left( \frac{6^0}{0!} + \frac{6^1}{1!} + \frac{6^2}{2!} + \frac{6^3}{3!} + \frac{6^4}{4!} \right) \\
&= e^{-6} \left( 1 + 6 + \frac{36}{2} + \frac{216}{6} + \frac{1296}{24} \right) \\
&= e^{-6} \left( 1 + 6 + 18 + 36 + 54 \right) \\
&= e^{-6} \times 115 \\
&\approx 0.2851.
\end{aligned}
\]

**(d) \(P(X = 6)\) using the Poisson approximation:**

\[
\begin{aligned}
P(X = 6) &\approx \frac{e^{-6} \cdot 6^6}{6!} \\
&= \frac{e^{-6} \cdot 46656}{720} \\
&= e^{-6} \times 64.8 \\
&\approx 0.1606.
\end{aligned}
\]

**Answer:** (a) \(n\) large, \(p\) small, \(np = 6\) moderate — Poisson approximation appropriate.  (b) \(\lambda = 6\)  (c) ≈0.2851  (d) ≈0.1606

---

## Problem 18

**Approach:** For (a), integrate the pdf over its domain and set equal to 1 to solve for \(k\). For (b), compute \(E(X) = \int x f(x)\,dx\). For (c), integrate the pdf from 1 to 2.

**(a) Show that \(k = \frac{3}{4}\):**

For \(f(x)\) to be a valid probability density function, the total area must equal 1:

\[
\int_{0}^{2} kx(2 - x)\,dx = 1.
\]

\[
\begin{aligned}
\int_{0}^{2} kx(2 - x)\,dx &= k \int_{0}^{2} (2x - x^2)\,dx \\
&= k \left[ x^2 - \frac{x^3}{3} \right]_{0}^{2} \\
&= k \left( 4 - \frac{8}{3} \right) \\
&= k \left( \frac{12}{3} - \frac{8}{3} \right) \\
&= k \cdot \frac{4}{3}.
\end{aligned}
\]

Setting this equal to 1: \(k \cdot \frac{4}{3} = 1 \implies k = \frac{3}{4}\). ✓

**(b) Find \(E(X)\):**

\[
\begin{aligned}
E(X) &= \int_{0}^{2} x \cdot f(x)\,dx = \int_{0}^{2} x \cdot \frac{3}{4}x(2 - x)\,dx \\
&= \frac{3}{4} \int_{0}^{2} x^2(2 - x)\,dx \\
&= \frac{3}{4} \int_{0}^{2} (2x^2 - x^3)\,dx \\
&= \frac{3}{4} \left[ \frac{2x^3}{3} - \frac{x^4}{4} \right]_{0}^{2} \\
&= \frac{3}{4} \left( \frac{16}{3} - \frac{16}{4} \right) \\
&= \frac{3}{4} \left( \frac{16}{3} - 4 \right) \\
&= \frac{3}{4} \left( \frac{16 - 12}{3} \right) \\
&= \frac{3}{4} \cdot \frac{4}{3} = 1.
\end{aligned}
\]

**(c) Find \(P(X > 1)\):**

\[
\begin{aligned}
P(X > 1) &= \int_{1}^{2} \frac{3}{4}x(2 - x)\,dx \\
&= \frac{3}{4} \int_{1}^{2} (2x - x^2)\,dx \\
&= \frac{3}{4} \left[ x^2 - \frac{x^3}{3} \right]_{1}^{2} \\
&= \frac{3}{4} \left[ \left(4 - \frac{8}{3}\right) - \left(1 - \frac{1}{3}\right) \right] \\
&= \frac{3}{4} \left[ \frac{12 - 8}{3} - \frac{3 - 1}{3} \right] \\
&= \frac{3}{4} \left[ \frac{4}{3} - \frac{2}{3} \right] \\
&= \frac{3}{4} \cdot \frac{2}{3} = \frac{1}{2} = 0.5.
\end{aligned}
\]

**Answer:** (a) \(k = \frac{3}{4}\)  (b) \(E(X) = 1\)  (c) \(P(X > 1) = 0.5\)

---

## Problem 19

**Approach:** For (a), verify the total integral equals 1 and that the function is non-negative. For (b), use integration by parts with \(u = y\), \(dv = \sin y\,dy\). For (c), solve \(\int_0^m f(y)\,dy = 0.5\).

**(a) Verify that \(f(y)\) is a valid pdf:**

First, \(f(y) = \frac{1}{2}\sin y \geq 0\) for all \(y \in [0, \pi]\) because \(\sin y \geq 0\) on this interval.

Now check the total area:

\[
\begin{aligned}
\int_{0}^{\pi} \frac{1}{2} \sin y\,dy &= \frac{1}{2} \left[ -\cos y \right]_{0}^{\pi} \\
&= \frac{1}{2} \big( -\cos\pi - (-\cos 0) \big) \\
&= \frac{1}{2} \big( -(-1) + 1 \big) \\
&= \frac{1}{2} (1 + 1) = 1.
\end{aligned}
\]

Since \(f(y) \geq 0\) on its domain and the total integral is 1, \(f(y)\) is a valid probability density function. ✓

**(b) Find \(E(Y)\):**

\[
E(Y) = \int_{0}^{\pi} y \cdot \frac{1}{2} \sin y\,dy = \frac{1}{2} \int_{0}^{\pi} y \sin y\,dy.
\]

Use integration by parts. Let \(u = y\), \(dv = \sin y\,dy\). Then \(du = dy\) and \(v = -\cos y\).

\[
\begin{aligned}
\int y \sin y\,dy &= -y \cos y - \int (-\cos y)\,dy \\
&= -y \cos y + \int \cos y\,dy \\
&= -y \cos y + \sin y.
\end{aligned}
\]

Evaluating the definite integral:

\[
\begin{aligned}
\int_{0}^{\pi} y \sin y\,dy &= \Big[ -y \cos y + \sin y \Big]_{0}^{\pi} \\
&= \big( -\pi \cos\pi + \sin\pi \big) - \big( -0 \cdot \cos 0 + \sin 0 \big) \\
&= \big( -\pi(-1) + 0 \big) - (0 + 0) \\
&= \pi.
\end{aligned}
\]

Therefore:

\[
E(Y) = \frac{1}{2} \cdot \pi = \frac{\pi}{2}.
\]

**(c) Find the median \(m\):**

The median satisfies \(P(Y \leq m) = 0.5\), i.e.:

\[
\int_{0}^{m} \frac{1}{2} \sin y\,dy = 0.5.
\]

\[
\frac{1}{2} \left[ -\cos y \right]_{0}^{m} = 0.5.
\]

\[
\frac{1}{2} \big( -\cos m - (-\cos 0) \big) = 0.5.
\]

\[
\frac{1}{2} (-\cos m + 1) = 0.5.
\]

\[
-\cos m + 1 = 1 \implies \cos m = 0.
\]

On the interval \([0, \pi]\), the solution is \(m = \frac{\pi}{2}\).

**Answer:** (a) Verified — total area = 1, \(f(y) \geq 0\).  (b) \(E(Y) = \frac{\pi}{2}\)  (c) \(m = \frac{\pi}{2}\)

---

## Problem 20

**Approach:** Let \(L \sim N(800, 40^2)\). For (a), standardize. For (b), treat "lasting more than 850 hours" as a Bernoulli event with probability \(p\) from part (a) and use the binomial distribution for a sample of 10. For (c), use \(E = np\).

**(a) Probability a bulb lasts more than 850 hours:**

\[
Z = \frac{850 - 800}{40} = \frac{50}{40} = 1.25.
\]

\[
P(L > 850) = P(Z > 1.25) = 1 - \Phi(1.25) = 1 - 0.8944 = 0.1056.
\]

**(b) Probability at least 8 out of 10 last more than 850 hours:**

Let \(p = 0.1056\) be the probability a bulb lasts more than 850 hours. In a random sample of \(n = 10\) bulbs, the number \(Y\) that last more than 850 hours follows \(Y \sim B(10, 0.1056)\).

\[
\begin{aligned}
P(Y \geq 8) &= P(Y = 8) + P(Y = 9) + P(Y = 10) \\
&= \binom{10}{8} p^8 (1-p)^2 + \binom{10}{9} p^9 (1-p) + \binom{10}{10} p^{10} \\
&= 45 \times (0.1056)^8 \times (0.8944)^2 + 10 \times (0.1056)^9 \times 0.8944 + (0.1056)^{10} \\
&\approx 5.74 \times 10^{-7}.
\end{aligned}
\]

This is an extremely small probability, which makes sense because each bulb only has about a 10.6% chance of exceeding 850 hours, so getting 8 or more out of 10 would be a very rare event.

**(c) Expected number lasting more than 850 hours:**

\[
E(Y) = np = 10 \times 0.1056 = 1.056 \text{ bulbs}.
\]

**Answer:** (a) 0.1056  (b) ≈5.7 × 10⁻⁷  (c) 1.056 bulbs

---

## Problem 21

**Approach:** This is a structured induction problem. Follow the given sub-parts: verify the base case, state the inductive hypothesis, then prove the inductive step by adding the \((k+1)\)-th term and simplifying.

**(a) Verify the base case \(n = 1\):**

\[
\text{LHS} = \sum_{r=1}^{1} \frac{1}{r(r+1)} = \frac{1}{1 \cdot 2} = \frac{1}{2}.
\]

\[
\text{RHS} = \frac{1}{1 + 1} = \frac{1}{2}.
\]

LHS = RHS, so the base case holds. ✓

**(b) State the inductive hypothesis:**

Assume that the formula holds for some positive integer \(n = k\). That is,

\[
\sum_{r=1}^{k} \frac{1}{r(r+1)} = \frac{k}{k+1}.
\]

**(c) Prove the inductive step:**

We need to show that if the formula holds for \(n = k\), then it also holds for \(n = k + 1\).

\[
\begin{aligned}
\sum_{r=1}^{k+1} \frac{1}{r(r+1)} &= \left( \sum_{r=1}^{k} \frac{1}{r(r+1)} \right) + \frac{1}{(k+1)(k+2)} \\
&= \frac{k}{k+1} + \frac{1}{(k+1)(k+2)} \quad \text{(by inductive hypothesis)}.
\end{aligned}
\]

Place both terms over the common denominator \((k+1)(k+2)\):

\[
\begin{aligned}
\frac{k}{k+1} &= \frac{k(k+2)}{(k+1)(k+2)}.
\end{aligned}
\]

\[
\begin{aligned}
\sum_{r=1}^{k+1} \frac{1}{r(r+1)} &= \frac{k(k+2)}{(k+1)(k+2)} + \frac{1}{(k+1)(k+2)} \\
&= \frac{k(k+2) + 1}{(k+1)(k+2)} \\
&= \frac{k^2 + 2k + 1}{(k+1)(k+2)} \\
&= \frac{(k+1)^2}{(k+1)(k+2)} \\
&= \frac{k+1}{k+2} \\
&= \frac{k+1}{(k+1)+1}.
\end{aligned}
\]

This is exactly the formula with \(n = k+1\). The inductive step is proved. ✓

**Conclusion:** By the principle of mathematical induction, the formula holds for all positive integers \(n\).

**Answer:** \(\displaystyle\sum_{r=1}^{n} \frac{1}{r(r+1)} = \frac{n}{n+1}\) for all \(n \in \mathbb{Z}^+\).

---

## Problem 22

**Approach:** For (a), use the fact that the sum of all probabilities must be 1 and recognize the Maclaurin series \(e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!}\). For (b) and (c), compute \(E(X)\) and \(E(X^2)\) using series manipulations, noting that \(x^2 = x(x-1) + x\).

**(a) Find the value of \(k\):**

The sum of all probabilities must equal 1:

\[
\sum_{x=0}^{\infty} P(X = x) = \sum_{x=0}^{\infty} \frac{k}{x!} = k \sum_{x=0}^{\infty} \frac{1}{x!} = 1.
\]

The Maclaurin series for \(e^x\) is \(\sum_{x=0}^{\infty} \frac{x^n}{n!}\) (here \(x\) is the variable of the series). Setting \(x = 1\):

\[
\sum_{x=0}^{\infty} \frac{1}{x!} = e^1 = e.
\]

Therefore:

\[
k \cdot e = 1 \implies k = \frac{1}{e}.
\]

**(b) Show that \(E(X) = 1\):**

\[
\begin{aligned}
E(X) &= \sum_{x=0}^{\infty} x \cdot P(X = x) = \sum_{x=0}^{\infty} x \cdot \frac{k}{x!} = k \sum_{x=1}^{\infty} \frac{x}{x!} \quad (\text{the } x=0 \text{ term is zero}) \\
&= k \sum_{x=1}^{\infty} \frac{1}{(x-1)!}.
\end{aligned}
\]

Let \(y = x - 1\). Then as \(x\) runs from 1 to \(\infty\), \(y\) runs from 0 to \(\infty\):

\[
E(X) = k \sum_{y=0}^{\infty} \frac{1}{y!} = k \cdot e = \frac{1}{e} \cdot e = 1.
\]

**(c) Find \(\operatorname{Var}(X)\):**

First compute \(E(X^2)\). Write \(x^2 = x(x-1) + x\):

\[
\begin{aligned}
E(X^2) &= \sum_{x=0}^{\infty} x^2 \cdot \frac{k}{x!} = k \sum_{x=0}^{\infty} \frac{x^2}{x!} \\
&= k \sum_{x=0}^{\infty} \frac{x(x-1) + x}{x!} \\
&= k \sum_{x=0}^{\infty} \frac{x(x-1)}{x!} + k \sum_{x=0}^{\infty} \frac{x}{x!}.
\end{aligned}
\]

The second sum is just \(E(X) = 1\). For the first sum, note that terms with \(x = 0, 1\) are zero, so we start from \(x = 2\):

\[
k \sum_{x=2}^{\infty} \frac{x(x-1)}{x!} = k \sum_{x=2}^{\infty} \frac{1}{(x-2)!}.
\]

Let \(y = x - 2\). As \(x\) runs from 2 to \(\infty\), \(y\) runs from 0 to \(\infty\):

\[
k \sum_{y=0}^{\infty} \frac{1}{y!} = k \cdot e = 1.
\]

Therefore:

\[
E(X^2) = 1 + 1 = 2.
\]

\[
\operatorname{Var}(X) = E(X^2) - [E(X)]^2 = 2 - 1^2 = 1.
\]

**Answer:** (a) \(k = \frac{1}{e}\)  (b) \(E(X) = 1\)  (c) \(\operatorname{Var}(X) = 1\)

---

## Problem 23

**Approach:** Set up the probability of drawing two red marbles without replacement. Equate this to \(\frac{5}{14}\) and solve the resulting quadratic equation for \(n\).

**(a) Show that \(n\) satisfies the given equation:**

There are \(n\) red marbles and 3 blue marbles, so the total number of marbles is \(n + 3\).

The probability that both drawn marbles are red (without replacement) is:

\[
P(\text{both red}) = \frac{n}{n+3} \cdot \frac{n-1}{n+2} = \frac{n(n-1)}{(n+3)(n+2)}.
\]

We are told this probability equals \(\frac{5}{14}\):

\[
\frac{n(n-1)}{(n+3)(n+2)} = \frac{5}{14}.
\]

Multiplying both sides by \((n+3)(n+2)\):

\[
n(n-1) = \frac{5}{14}(n+3)(n+2).
\]

This is exactly the required equation. ✓

**(b) Find the value of \(n\):**

\[
\begin{aligned}
n(n-1) &= \frac{5}{14}(n+3)(n+2) \\[4pt]
14n(n-1) &= 5(n+3)(n+2) \\[4pt]
14n^2 - 14n &= 5(n^2 + 5n + 6) \\[4pt]
14n^2 - 14n &= 5n^2 + 25n + 30 \\[4pt]
9n^2 - 39n - 30 &= 0 \\[4pt]
3n^2 - 13n - 10 &= 0.
\end{aligned}
\]

Solve the quadratic:

\[
n = \frac{13 \pm \sqrt{(-13)^2 - 4 \cdot 3 \cdot (-10)}}{2 \cdot 3} = \frac{13 \pm \sqrt{169 + 120}}{6} = \frac{13 \pm \sqrt{289}}{6} = \frac{13 \pm 17}{6}.
\]

This gives \(n = \frac{30}{6} = 5\) or \(n = \frac{-4}{6} = -\frac{2}{3}\).

Since \(n\) must be a positive integer (number of marbles), we take \(n = 5\).

**Check:** With \(n = 5\), there are 5 red and 3 blue marbles, total 8.
\(P(\text{both red}) = \frac{5}{8} \cdot \frac{4}{7} = \frac{20}{56} = \frac{5}{14}\). ✓

**Answer:** (a) Equation shown above.  (b) \(n = 5\)

---

## Problem 24

**Approach:** Use induction. Verify the base case, then express \(7^{k+1} + 4^{k+1} + 1\) in terms of \(7^k + 4^k + 1\) plus additional terms that are also divisible by 6.

**Base case (\(n = 1\)):**

\[
7^1 + 4^1 + 1 = 7 + 4 + 1 = 12 = 6 \times 2.
\]

12 is divisible by 6, so the statement holds for \(n = 1\).

**Inductive hypothesis:** Assume that for some positive integer \(n = k\),

\[
7^k + 4^k + 1 = 6m \quad \text{for some integer } m.
\]

**Inductive step:** Prove that \(7^{k+1} + 4^{k+1} + 1\) is divisible by 6.

Write \(7^{k+1} = 7 \cdot 7^k\) and \(4^{k+1} = 4 \cdot 4^k\).

Now express \(7^{k+1} + 4^{k+1} + 1\) in a way that uses the inductive hypothesis. Write \(7 = (6+1)\) and \(4 = (3+1)\):

\[
\begin{aligned}
7^{k+1} + 4^{k+1} + 1 &= (6+1)7^k + (3+1)4^k + 1 \\
&= 6 \cdot 7^k + 7^k + 3 \cdot 4^k + 4^k + 1 \\
&= 6 \cdot 7^k + 3 \cdot 4^k + (7^k + 4^k + 1) \\
&= 6 \cdot 7^k + 3 \cdot 4^k + 6m \quad \text{(by inductive hypothesis)} \\
&= 6(7^k + m) + 3 \cdot 4^k.
\end{aligned}
\]

Now we need to show that \(3 \cdot 4^k\) is divisible by 6. Note that \(4^k = (2^2)^k = 2^{2k}\). Since \(2k \geq 2\) for \(k \geq 1\), we have \(2^{2k}\) is divisible by \(2\), i.e. \(4^k = 2 \cdot t\) for some integer \(t = 2^{2k-1}\).

Then \(3 \cdot 4^k = 3 \cdot 2 \cdot t = 6t\), which is divisible by 6.

Therefore:

\[
7^{k+1} + 4^{k+1} + 1 = 6(7^k + m) + 6t = 6(7^k + m + t).
\]

Since \(7^k + m + t\) is an integer, \(7^{k+1} + 4^{k+1} + 1\) is a multiple of 6. ✓

**Conclusion:** By mathematical induction, \(7^n + 4^n + 1\) is divisible by 6 for all positive integers \(n\).

**Answer:** \(7^n + 4^n + 1\) is divisible by 6 for all \(n \in \mathbb{Z}^+\).

---

## Problem 25

**Approach:** For a Poisson random variable, use \(P(X = k) = \frac{e^{-\lambda}\lambda^k}{k!}\). Set \(P(X=1) = P(X=2)\) to solve for \(\lambda\). Then compute the required probabilities.

**(a) Find the value of \(\lambda\):**

Given \(P(X = 1) = P(X = 2)\):

\[
\frac{e^{-\lambda}\lambda^1}{1!} = \frac{e^{-\lambda}\lambda^2}{2!}.
\]

Cancel \(e^{-\lambda}\) (which is non-zero):

\[
\lambda = \frac{\lambda^2}{2}.
\]

Multiply both sides by 2:

\[
2\lambda = \lambda^2.
\]

\[
\lambda^2 - 2\lambda = 0 \implies \lambda(\lambda - 2) = 0.
\]

So \(\lambda = 0\) or \(\lambda = 2\). For a Poisson distribution, \(\lambda > 0\). Therefore:

\[
\lambda = 2.
\]

**(b) Find \(P(X = 0)\):**

\[
P(X = 0) = \frac{e^{-2} \cdot 2^0}{0!} = e^{-2} \approx 0.1353.
\]

**(c) Find \(P(X \geq 3)\):**

\[
\begin{aligned}
P(X \geq 3) &= 1 - P(X \leq 2) \\
&= 1 - [P(X = 0) + P(X = 1) + P(X = 2)] \\
&= 1 - e^{-2} \left( \frac{2^0}{0!} + \frac{2^1}{1!} + \frac{2^2}{2!} \right) \\
&= 1 - e^{-2} \left( 1 + 2 + 2 \right) \\
&= 1 - 5e^{-2} \\
&\approx 1 - 5 \times 0.1353 \\
&= 1 - 0.6767 = 0.3233.
\end{aligned}
\]

**Answer:** (a) \(\lambda = 2\)  (b) \(e^{-2} \approx 0.1353\)  (c) \(1 - 5e^{-2} \approx 0.3233\)
