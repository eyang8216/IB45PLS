# IB AAHL Unit 6: Proof & Probability — Practice Problems

---

## Problem 1
Prove by mathematical induction that for all positive integers \(n\):

\[
\sum_{r=1}^{n} r(r + 1) = \frac{n(n + 1)(n + 2)}{3}.
\]

---

## Problem 2
Prove by induction that \(5^n − 3^n\) is divisible by 2 for all \(n \in \mathbb{Z}^+\).

---

## Problem 3
Prove by mathematical induction that \(2^n > n^2\) for all integers \(n \geq 5\).

---

## Problem 4
Let \(A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}\). Prove by induction that for all positive integers \(n\),

\[
A^n = \begin{pmatrix} 1 & 2n \\ 0 & 1 \end{pmatrix}.
\]

---

## Problem 5
A bag contains 5 red marbles and 7 blue marbles. Two marbles are drawn at random without replacement.

- (a) Draw a fully labelled tree diagram showing all possible outcomes.
- (b) Find the probability that both marbles are the same colour.
- (c) Find the probability that the second marble is red given that the first marble was blue.

---

## Problem 6
In a certain town, the probability that a randomly selected resident owns a car is 0.7. The probability that a resident owns a bicycle is 0.4. The probability that a resident owns both is 0.25.

- (a) Find the probability that a randomly selected resident owns a car or a bicycle (or both).
- (b) Find the probability that a resident owns a car given that they own a bicycle.
- (c) Determine whether the events "owns a car" and "owns a bicycle" are independent. Justify your answer.

---

## Problem 7
A diagnostic test for a disease has the following properties: the probability that the test is positive given that a person has the disease is 0.98 (sensitivity), and the probability that the test is negative given that a person does not have the disease is 0.95 (specificity). The disease occurs in 1% of the population.

- (a) Draw a tree diagram to represent the situation.
- (b) Find the probability that a randomly selected person tests positive.
- (c) Use Bayes' theorem to find the probability that a person actually has the disease given that they test positive.
- (d) Comment on your answer to part (c).

---

## Problem 8
A factory has three machines: A, B, and C. Machine A produces 30% of the items, machine B produces 45%, and machine C produces 25%. The defect rates are: A — 2%, B — 3%, C — 1%.

- (a) Find the probability that a randomly selected item is defective.
- (b) If an item is found to be defective, what is the probability it came from machine B?
- (c) If an item is found to be non-defective, what is the probability it came from machine C?

---

## Problem 9
A discrete random variable \(X\) has the following probability distribution:

\[
\begin{array}{c|cccc}
x & 0 & 1 & 2 & 3 \\
\hline
P(X = x) & 0.1 & 0.3 & 0.4 & 0.2
\end{array}
\]

- (a) Find \(E(X)\).
- (b) Find \(E(X^2)\).
- (c) Hence find \(\operatorname{Var}(X)\).

---

## Problem 10
A fair six-sided die is rolled. The random variable \(X\) is defined as \(X = (\text{score})^2\).

- (a) Write down the probability distribution of \(X\).
- (b) Compute \(E(X)\).
- (c) Compute \(\operatorname{Var}(X)\).

---

## Problem 11
A fair coin is tossed 8 times. Let \(X\) be the number of heads obtained.

- (a) State the distribution of \(X\), including its parameters.
- (b) Find \(P(X = 5)\).
- (c) Find \(P(X \geq 3)\).
- (d) State \(E(X)\) and \(\operatorname{Var}(X)\).

---

## Problem 12
In a multiple-choice quiz, there are 20 questions. Each question has four options and exactly one is correct. A student guesses every answer independently. Let \(Y\) be the number of correct answers.

- (a) State the distribution of \(Y\) and its parameters.
- (b) Find the probability that the student gets exactly 6 questions correct.
- (c) Find the probability that the student gets at least 10 questions correct.
- (d) Find \(E(Y)\) and \(\operatorname{Var}(Y)\).

---

## Problem 13
The random variable \(Z\) follows a standard normal distribution, \(Z \sim N(0, 1)\).

- (a) Find \(P(Z < 1.25)\).
- (b) Find \(P(−0.8 < Z < 1.5)\).
- (c) Find the value of \(c\) such that \(P(Z > c) = 0.05\).

---

## Problem 14
The heights of adult males in a population are normally distributed with mean 175 cm and standard deviation 7 cm. A man is selected at random.

- (a) Find the probability that his height is less than 168 cm.
- (b) Find the probability that his height is between 170 cm and 185 cm.
- (c) Find the height above which the tallest 10% of men fall.

---

## Problem 15
The masses of apples from an orchard are normally distributed with mean 150 g and standard deviation 20 g. Apples with mass less than 120 g are classified as "small."

- (a) Find the proportion of apples classified as small.
- (b) A random sample of 5 apples is taken. Find the probability that exactly 2 of them are classified as small.
- (c) Find the mass \(m\) such that 90% of apples have mass greater than \(m\).

---

## Problem 16
The number of phone calls received by a call centre in a given hour follows a Poisson distribution with mean 4.5.

- (a) Find the probability that exactly 3 calls are received in a given hour.
- (b) Find the probability that at most 2 calls are received in a given hour.
- (c) Find the probability that more than 5 calls are received in a given hour.

---

## Problem 17
A binomial random variable \(X \sim B(300, 0.02)\).

- (a) Explain why a Poisson distribution can be used to approximate the distribution of \(X\).
- (b) State the parameter of the approximating Poisson distribution.
- (c) Using the Poisson approximation, find \(P(X \leq 4)\).
- (d) Using the Poisson approximation, find \(P(X = 6)\).

---

## Problem 18
A continuous random variable \(X\) has probability density function

\[
f(x) = \begin{cases}
kx(2 − x), & 0 \leq x \leq 2, \\
0, & \text{otherwise}.
\end{cases}
\]

- (a) Show that \(k = \frac{3}{4}\).
- (b) Find \(E(X)\).
- (c) Find the probability that \(X > 1\).

---

## Problem 19
A continuous random variable \(Y\) has probability density function

\[
f(y) = \begin{cases}
\frac{1}{2}\sin y, & 0 \leq y \leq \pi, \\
0, & \text{otherwise}.
\end{cases}
\]

- (a) Verify that \(f(y)\) is a valid probability density function.
- (b) Find \(E(Y)\). (Hint: use integration by parts.)
- (c) Find the median of \(Y\), i.e., the value \(m\) such that \(P(Y \leq m) = 0.5\).

---

## Problem 20
A factory produces light bulbs whose lifetimes are normally distributed with mean 800 hours and standard deviation 40 hours.

- (a) Find the probability that a randomly selected bulb lasts more than 850 hours.
- (b) A quality control inspector takes a random sample of 10 bulbs. Find the probability that at least 8 of them last more than 850 hours.
- (c) Find the expected number of bulbs in the sample that last more than 850 hours.

---

## Problem 21
Prove by mathematical induction that for all positive integers \(n\),

\[
\sum_{r=1}^{n} \frac{1}{r(r + 1)} = \frac{n}{n + 1}.
\]

- (a) Verify the base case \(n = 1\).
- (b) State the inductive hypothesis.
- (c) Prove the inductive step, showing that if the formula holds for \(n = k\), then it holds for \(n = k + 1\).

---

## Problem 22
The random variable \(X\) has the probability distribution:

\[
P(X = x) = \frac{k}{x!},\quad x = 0, 1, 2, 3, \dots
\]

- (a) Using the Maclaurin series for \(e^x\), find the value of \(k\).
- (b) Show that \(E(X) = 1\).
- (c) Find \(\operatorname{Var}(X)\).

---

## Problem 23
A bag contains \(n\) red marbles and 3 blue marbles. Two marbles are drawn without replacement. The probability that both are red is \(\frac{5}{14}\).

- (a) Show that \(n\) satisfies the equation \(n(n − 1) = \frac{5}{14}(n + 3)(n + 2)\).
- (b) Hence find the value of \(n\).

---

## Problem 24
Prove by induction that \(7^n + 4^n + 1\) is divisible by 6 for all positive integers \(n\).

---

## Problem 25
A random variable \(X\) has a Poisson distribution with mean \(\lambda\). It is known that \(P(X = 1) = P(X = 2)\).

- (a) Find the value of \(\lambda\).
- (b) Hence find \(P(X = 0)\).
- (c) Find \(P(X \geq 3)\).
