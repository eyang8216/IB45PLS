# Lesson 33 — Probability Basics and Conditional Probability

## What is Probability and Why Learn It?

Probability is the branch of mathematics that measures how likely an event is to occur. It assigns a number between 0 and 1 to every possible outcome of a random experiment. A probability of 0 means the event is impossible. A probability of 1 means the event is certain.

Probability is the foundation of statistics, data science, risk assessment, and decision-making under uncertainty. In IB AAHL, you need to calculate probabilities, work with conditional statements, and determine whether events are independent. This lesson builds these concepts from the ground up.

## 1. Sample Spaces and Events

A **random experiment** is any process whose outcome cannot be predicted with certainty. The **sample space**, denoted by $S$, is the set of all possible outcomes of a random experiment.

An **event** is any collection of outcomes — that is, a subset of the sample space. We use capital letters like $A$ and $B$ to name events.

When every outcome in the sample space has the same chance of occurring, we say the outcomes are **equally likely**. For equally likely outcomes, the probability of an event $A$ is:

$$P(A) = \frac{|A|}{|S|}$$

The notation $|A|$ means "the number of elements in set $A$." So $P(A)$ is the number of outcomes that make up event $A$, divided by the total number of possible outcomes.

### Worked Example 1

**Problem:** A fair six-sided die is rolled once. Find the probability of rolling an even number.

**Approach:** First identify the sample space, then count how many outcomes satisfy "even number," then divide.

The sample space is $S = \{1, 2, 3, 4, 5, 6\}$, so $|S| = 6$.

The event "roll an even number" is $A = \{2, 4, 6\}$, so $|A| = 3$.

$$P(A) = \frac{3}{6} = \frac{1}{2}$$

**Why this makes sense:** Half the faces of the die show even numbers, so the probability is 0.5.

---

## 2. The Complement Rule

The **complement** of an event $A$, written as $A'$ (or sometimes $A^c$), is the event that $A$ does not happen. In set language, $A'$ contains every outcome in $S$ that is not in $A$.

Since every outcome is either in $A$ or in $A'$, and these two sets have no overlap, their probabilities must sum to 1:

$$P(A') = 1 - P(A)$$

### Worked Example 2

**Problem:** The probability that it rains on a given day in a certain city is 0.3. What is the probability that it does NOT rain?

**Approach:** Use the complement rule directly.

$$P(\text{no rain}) = 1 - P(\text{rain}) = 1 - 0.3 = 0.7$$

**Why this makes sense:** If there is a 30% chance of rain, then 70% of the time it does not rain. These two probabilities must add to 100%.

---

## 3. The Addition Rule for "OR"

The **union** of two events $A$ and $B$, written $A \cup B$, is the event that $A$ happens, $B$ happens, or both happen. The notation $\cup$ means "union" and corresponds to the word "or."

The **intersection** of two events $A$ and $B$, written $A \cap B$, is the event that both $A$ and $B$ happen. The notation $\cap$ means "intersection" and corresponds to the word "and."

To find $P(A \cup B)$, you cannot simply add $P(A)$ and $P(B)$, because any outcomes that belong to both events would be counted twice. The correct formula subtracts the overlap once:

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

### Worked Example 3

**Problem:** In a class of 30 students, 18 students study French, 14 students study Spanish, and 8 students study both languages. One student is chosen at random. Find the probability that this student studies French or Spanish.

**Approach:** Let $F$ be the event "studies French" and $S$ be the event "studies Spanish." We use the addition rule.

$P(F) = \frac{18}{30}$, $P(S) = \frac{14}{30}$, $P(F \cap S) = \frac{8}{30}$

$$P(F \cup S) = \frac{18}{30} + \frac{14}{30} - \frac{8}{30} = \frac{24}{30} = 0.8$$

**Why this makes sense:** If you simply added 18 and 14 you would get 32 students out of 30, which is impossible. The 8 students who study both were counted twice, so they must be subtracted once.

---

## 4. Mutually Exclusive Events

Two events are called **mutually exclusive** if they cannot both happen at the same time. In set language, their intersection is empty: $A \cap B = \emptyset$.

When events are mutually exclusive, the intersection probability is zero: $P(A \cap B) = 0$. The addition rule simplifies to:

$$P(A \cup B) = P(A) + P(B)$$

Many students confuse "mutually exclusive" with "independent." They are completely different concepts. Mutually exclusive means the events cannot occur together. Independence means the occurrence of one does not affect the probability of the other.

### Worked Example 4

**Problem:** A card is drawn at random from a standard deck of 52 playing cards. Find the probability that the card is a King or a Queen.

**Approach:** A single card cannot be both a King and a Queen, so these events are mutually exclusive.

$P(\text{King}) = \frac{4}{52}$ (there are 4 Kings in the deck).

$P(\text{Queen}) = \frac{4}{52}$ (there are 4 Queens in the deck).

$$P(\text{King} \cup \text{Queen}) = \frac{4}{52} + \frac{4}{52} = \frac{8}{52} = \frac{2}{13}$$

---

## 5. Conditional Probability

**Conditional probability** is the probability that one event occurs, given that another event has already occurred. The notation $P(A \mid B)$ is read as "the probability of $A$ given $B$."

The formula for conditional probability is:

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$$

This formula makes sense if you think about "zooming in" on the reduced world where $B$ has definitely happened. The denominator $P(B)$ is the size of this reduced world. The numerator $P(A \cap B)$ is the part of that reduced world where $A$ also happens.

A crucial condition is that $P(B) > 0$. You cannot condition on an impossible event.

### Worked Example 5

**Problem:** A fair six-sided die is rolled. Given that the outcome is even, what is the probability that it is a 6?

**Approach:** Let $B$ be "the outcome is even" and $A$ be "the outcome is 6." Then find $P(A \mid B)$.

The sample space is $\{1, 2, 3, 4, 5, 6\}$. The event $B$ (even) is $\{2, 4, 6\}$, so $P(B) = \frac{3}{6} = \frac{1}{2}$.

The event $A$ (rolling a 6) is $\{6\}$. The intersection $A \cap B = \{6\}$, so $P(A \cap B) = \frac{1}{6}$.

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)} = \frac{1/6}{1/2} = \frac{1}{6} \times \frac{2}{1} = \frac{1}{3}$$

**Why this makes sense:** In the reduced sample space $\{2, 4, 6\}$, there are three equally likely outcomes. Only one of them is a 6, so the conditional probability is $1/3$.

### Worked Example 6

**Problem:** Using the class from Worked Example 3 (30 students: 18 French, 14 Spanish, 8 both), find the probability that a randomly chosen student studies French, given that the student studies Spanish.

**Approach:** This is $P(F \mid S)$.

$$P(F \mid S) = \frac{P(F \cap S)}{P(S)} = \frac{8/30}{14/30} = \frac{8}{14} = \frac{4}{7}$$

**Why this makes sense:** Among the 14 Spanish students, 8 also study French. So the conditional probability is $8/14$.

---

## 6. Independence

Two events $A$ and $B$ are **independent** if knowing whether one occurred gives no information about whether the other occurred. There are three equivalent ways to check for independence:

1. $P(A \cap B) = P(A) \times P(B)$
2. $P(A \mid B) = P(A)$
3. $P(B \mid A) = P(B)$

If any one of these three equations is true, the other two are automatically true, and the events are independent. If any one is false, the events are dependent.

### Worked Example 7

**Problem:** A fair coin is tossed twice. Let $H_1$ be "the first toss is heads" and $H_2$ be "the second toss is heads." Are $H_1$ and $H_2$ independent?

**Approach:** We check whether $P(H_1 \cap H_2) = P(H_1) \times P(H_2)$.

$P(H_1) = \frac{1}{2}$, $P(H_2) = \frac{1}{2}$, $P(H_1 \cap H_2) = \frac{1}{4}$ (only the outcome HH satisfies both).

$P(H_1) \times P(H_2) = \frac{1}{2} \times \frac{1}{2} = \frac{1}{4}$

Since $P(H_1 \cap H_2) = P(H_1) \times P(H_2)$, the events are independent.

**Why this makes sense:** The result of the first coin toss has no physical effect on the second toss. The coin does not "remember" what it did before.

### Worked Example 8

**Problem:** A bag contains 5 red marbles and 3 blue marbles. You draw two marbles without replacement. Let $R_1$ be "the first marble is red" and $R_2$ be "the second marble is red." Are $R_1$ and $R_2$ independent?

**Approach:** Check whether $P(R_2 \mid R_1)$ equals $P(R_2)$.

First, $P(R_1) = \frac{5}{8}$ (5 red out of 8 total).

If the first marble was red, then 4 red marbles remain out of 7 total marbles. So $P(R_2 \mid R_1) = \frac{4}{7}$.

What would $P(R_2)$ be without any condition? It is actually still $\frac{5}{8}$, but careful reasoning is needed. Regardless, $\frac{4}{7} \neq \frac{5}{8}$, so $P(R_2 \mid R_1) \neq P(R_2)$. The events are NOT independent.

**Why this makes sense:** Removing a marble changes the composition of the bag. The outcome of the first draw physically affects the probabilities for the second draw.

---

## 7. Tree Diagrams

A **tree diagram** represents sequential events. Each branch from a node shows a possible outcome and its probability. The probabilities on all branches from a single node must sum to 1.

To find the probability of a complete path (a sequence of outcomes), multiply the probabilities along the branches.

To find the total probability of an event that can occur through multiple paths, add the probabilities of all those paths.

### Worked Example 9

**Problem:** A bag contains 4 red marbles and 6 blue marbles. Two marbles are drawn one after the other without replacement. Find the probability of drawing exactly one red marble.

**Approach:** Draw the tree, compute the probability of each path, and add the paths that give exactly one red.

**First draw:** $P(R) = \frac{4}{10} = \frac{2}{5}$, $P(B) = \frac{6}{10} = \frac{3}{5}$.

**Second draw after red:** 3 red and 6 blue remain, so $P(R \mid \text{first }R) = \frac{3}{9} = \frac{1}{3}$ and $P(B \mid \text{first }R) = \frac{6}{9} = \frac{2}{3}$.

**Second draw after blue:** 4 red and 5 blue remain, so $P(R \mid \text{first }B) = \frac{4}{9}$ and $P(B \mid \text{first }B) = \frac{5}{9}$.

Path RB (first red, then blue): $\frac{4}{10} \times \frac{6}{9} = \frac{24}{90}$.

Path BR (first blue, then red): $\frac{6}{10} \times \frac{4}{9} = \frac{24}{90}$.

Total probability of exactly one red: $\frac{24}{90} + \frac{24}{90} = \frac{48}{90} = \frac{8}{15}$.

**Why this makes sense:** The two paths RB and BR each have the same probability because the numbers are symmetric. Their sum simplifies nicely.

---

## 8. Two-Way Tables

A **two-way table** (also called a contingency table) organizes data by two categorical variables. The cells show counts (or probabilities) for each combination of categories. The row totals and column totals appear in the margins.

### Worked Example 10

**Problem:** A survey of 100 people collected data on gender and coffee preference. Among the 60 males, 30 like coffee. Among the 40 females, 20 like coffee. Organize this data in a two-way table and find $P(\text{likes coffee} \mid \text{male})$.

**Approach:** Construct the table, then use the conditional probability formula.

|           | Likes Coffee | Does Not Like | Total |
|-----------|:------------:|:-------------:|:-----:|
| **Male**  |      30      |      30       |  60   |
| **Female**|      20      |      20       |  40   |
| **Total** |      50      |      50       |  100  |

$$P(\text{likes coffee} \mid \text{male}) = \frac{30}{60} = 0.5$$

Also note: $P(\text{male} \mid \text{likes coffee}) = \frac{30}{50} = 0.6$. These two conditional probabilities are different — a common point of confusion. The order of conditioning matters.

In this particular table, $P(\text{coffee}) = 0.5$ and $P(\text{coffee} \mid \text{male}) = 0.5$, so coffee preference and gender happen to be independent in this dataset.

---

## Glossary

| Term | Meaning |
|------|---------|
| Sample space $S$ | The set of all possible outcomes of a random experiment |
| Event $A$ | A subset of the sample space |
| Complement $A'$ | The event that $A$ does not happen |
| Union $A \cup B$ | The event that $A$ or $B$ or both happen |
| Intersection $A \cap B$ | The event that both $A$ and $B$ happen |
| Conditional probability $P(A \mid B)$ | The probability of $A$ given that $B$ has occurred |
| Independent events | Events where $P(A \cap B) = P(A) \times P(B)$ |
| Mutually exclusive events | Events that cannot both happen: $A \cap B = \emptyset$ |

---

## Practice Problems

### Problem 1
A fair coin is tossed three times in a row.

(a) Write out the sample space $S$ explicitly. How many outcomes are there?

(b) Find the probability of getting exactly two heads.

(c) Find the probability of getting at least one head.

### Problem 2
A card is drawn at random from a standard 52-card deck. A "face card" is defined as a Jack, Queen, or King.

(a) Find the probability that the card is a Heart or a face card.

(b) Are the events "Heart" and "face card" mutually exclusive? Explain your answer.

(c) Find the probability that the card is a Heart, given that it is a face card.

### Problem 3
For two events $A$ and $B$, suppose $P(A) = 0.5$, $P(B) = 0.3$, and $P(A \cap B) = 0.2$.

(a) Find $P(A \cup B)$.

(b) Find $P(A \mid B)$.

(c) Find $P(B \mid A)$.

(d) Are $A$ and $B$ independent? Justify your answer using a calculation.

### Problem 4
There are two urns. Urn 1 contains 5 white balls and 3 black balls. Urn 2 contains 4 white balls and 6 black balls. A fair coin is flipped to decide which urn to use. Then one ball is drawn from the chosen urn.

(a) Draw a fully labeled tree diagram.

(b) Find the probability that the drawn ball is white.

(c) Given that the ball drawn is white, find the probability that it came from Urn 1.

### Problem 5 (IB Exam Style)
In a survey of students at a school, 70% own a laptop, 50% own a tablet, and 35% own both a laptop and a tablet. A student is selected at random.

(a) Find the probability that the student owns a laptop or a tablet. **[2 marks]**

(b) Determine whether owning a laptop and owning a tablet are independent events. Show your reasoning clearly. **[2 marks]**

(c) Given that the student owns a laptop, find the probability that they also own a tablet. **[2 marks]**

---

## Answers

### Problem 1

(a) The sample space is $S = \{HHH, HHT, HTH, HTT, THH, THT, TTH, TTT\}$. There are 8 outcomes.

(b) The outcomes with exactly two heads are $\{HHT, HTH, THH\}$. There are 3 favorable outcomes out of 8, so the probability is $\frac{3}{8}$.

(c) Rather than counting all outcomes with at least one head, it is easier to use the complement. The only outcome with no heads is $TTT$, which has probability $\frac{1}{8}$. Therefore $P(\text{at least one head}) = 1 - \frac{1}{8} = \frac{7}{8}$.

### Problem 2

(a) There are 13 Hearts and 12 face cards (3 per suit × 4 suits). Among the Hearts, 3 cards (Jack, Queen, King of Hearts) are face cards. Using the addition rule: $P(\text{Heart} \cup \text{Face}) = \frac{13}{52} + \frac{12}{52} - \frac{3}{52} = \frac{22}{52} = \frac{11}{26}$.

(b) They are NOT mutually exclusive, because the Jack, Queen, and King of Hearts are simultaneously Hearts and face cards. For mutual exclusivity, the intersection must be empty, but here there are 3 cards in the intersection.

(c) $P(\text{Heart} \mid \text{Face}) = \frac{P(\text{Heart} \cap \text{Face})}{P(\text{Face})} = \frac{3/52}{12/52} = \frac{3}{12} = \frac{1}{4}$. Among the 12 face cards in the deck, exactly 3 are Hearts.

### Problem 3

(a) $P(A \cup B) = 0.5 + 0.3 - 0.2 = 0.6$.

(b) $P(A \mid B) = \frac{P(A \cap B)}{P(B)} = \frac{0.2}{0.3} = \frac{2}{3}$.

(c) $P(B \mid A) = \frac{P(A \cap B)}{P(A)} = \frac{0.2}{0.5} = 0.4$.

(d) To check independence, compute $P(A) \times P(B) = 0.5 \times 0.3 = 0.15$. Since $P(A \cap B) = 0.2 \neq 0.15$, the events are NOT independent. The product rule fails.

### Problem 4

(a) Tree diagram: first branch is choosing Urn 1 (probability 0.5) or Urn 2 (probability 0.5). From Urn 1, branches are White ($\frac{5}{8}$) and Black ($\frac{3}{8}$). From Urn 2, branches are White ($\frac{4}{10} = \frac{2}{5}$) and Black ($\frac{6}{10} = \frac{3}{5}$).

(b) $P(\text{White}) = P(\text{Urn 1}) \times P(\text{White} \mid \text{Urn 1}) + P(\text{Urn 2}) \times P(\text{White} \mid \text{Urn 2}) = 0.5 \times \frac{5}{8} + 0.5 \times \frac{4}{10} = \frac{5}{16} + \frac{2}{10} = \frac{5}{16} + \frac{1}{5}$.

To add, use a common denominator of 80: $\frac{25}{80} + \frac{16}{80} = \frac{41}{80} = 0.5125$.

(c) $P(\text{Urn 1} \mid \text{White}) = \frac{P(\text{Urn 1} \cap \text{White})}{P(\text{White})} = \frac{5/16}{41/80} = \frac{5}{16} \times \frac{80}{41} = \frac{25}{41}$.

### Problem 5

Let $L$ be the event "owns a laptop" and $T$ be the event "owns a tablet." Then $P(L) = 0.7$, $P(T) = 0.5$, $P(L \cap T) = 0.35$.

(a) $P(L \cup T) = 0.7 + 0.5 - 0.35 = 0.85$. **[2 marks]**

(b) Compute $P(L) \times P(T) = 0.7 \times 0.5 = 0.35$. Since $P(L \cap T) = 0.35 = P(L) \times P(T)$, the events ARE independent. The product rule holds exactly. **[2 marks]**

(c) $P(T \mid L) = \frac{P(T \cap L)}{P(L)} = \frac{0.35}{0.7} = 0.5$. Notice that $P(T \mid L) = P(T)$, which is another way to confirm independence. **[2 marks]**
