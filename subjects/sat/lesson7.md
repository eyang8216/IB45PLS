# Lesson 7: Two-Way Tables & Frequency Analysis

## What You'll Learn
- Reading and interpreting two-way (contingency) tables
- Calculating joint frequency, marginal frequency, and conditional relative frequency
- Distinguishing row percentages from column percentages
- The SAT question pattern: "given that X, what's the probability of Y?"
- Avoiding the most common table-reading mistakes on the SAT
- Converting between raw counts and relative frequencies

## SAT Context

Two-way table questions appear 1-3 times per SAT. These are pure data analysis—no algebra required, just careful reading and the ability to extract the right numbers. The SAT's favorite move: giving you a full table and asking a conditional probability question where students grab the wrong row/column. For an AAHL student, the probability notation $P(A|B)$ is familiar, but the SAT asks these in plain English ("among those who..., what fraction...?"), and misreading the table accounts for most errors.

## Anatomy of a Two-Way Table

A two-way table shows how two categorical variables relate. Here's a template:

|               | Category X | Category Y | **Total** |
|---------------|:----------:|:----------:|:---------:|
| **Category A**|     a      |     b      |  **a+b**  |
| **Category B**|     c      |     d      |  **c+d**  |
| **Total**     |  **a+c**   |  **b+d**   | **a+b+c+d** |

### Three Types of Frequencies

**1. Joint Frequencies (individual cells)**
The count in a single cell: $a, b, c, d$.

**2. Marginal Frequencies (row/column totals)**
The totals in the margins: $a+b$, $c+d$, $a+c$, $b+d$.

**3. Conditional Relative Frequencies**
A proportion calculated within a row or column:
- Row: $\frac{a}{a+b}$ = proportion of Category A that is Category X.
- Column: $\frac{a}{a+c}$ = proportion of Category X that is Category A.

### The Grand Total
The bottom-right cell ($a+b+c+d$) is the total number of observations.

## SAT Question Patterns

### Pattern 1: "What fraction of [group] are [characteristic]?"

**Key:** The phrase after "of" tells you the **denominator** (the restricted group).

**Example:** "What fraction of **students who passed** are **female**?"

Denominator: total students who passed.
Numerator: female students who passed.

### Pattern 2: "Given that a randomly selected [person] is [characteristic], what's the probability..."

**Key:** "Given that" = condition = denominator.

**Example:** "Given that a randomly selected student is **male**, what is the probability the student **passed**?"

Denominator: total male students.
Numerator: male students who passed.

### Pattern 3: Joint relative frequency

"What proportion of **all** students are female and passed?"

Denominator: grand total.
Numerator: female students who passed.

> **🚨 SAT TRAP ALERT: Using the Wrong Denominator.** The SAT will put answer choices that use the wrong denominator—the grand total when you should use a row total, the row total when you should use the column total, etc. Always identify: what is the *universe* for this question? Is it everyone? A specific row? A specific column? Read the "of" or "given that" phrase carefully. If a question says "of the students who passed," your denominator is the "passed" total, NOT the grand total.

> **🔍 PATTERN RECOGNITION: "Among..., what percent...?"** Any time you see "among" in a two-way table question, it signals a conditional relative frequency. "Among X" means: restrict to group X, then find the proportion within that group. Similarly, "of the..." at the beginning of a question signals the denominator. Highlight or underline the conditional phrase before touching the numbers.

### Worked Example 1: Reading a Two-Way Table

**Problem:** A survey of 200 people asked about pet ownership:

|               | Own a Dog | No Dog | Total |
|---------------|:---------:|:------:|:-----:|
| **Own a Cat** |     40    |   30   |  70   |
| **No Cat**    |     60    |   70   |  130  |
| **Total**     |    100    |  100   |  200  |

What fraction of dog owners also own a cat?

A) $\frac{40}{200}$
B) $\frac{40}{100}$
C) $\frac{40}{70}$
D) $\frac{70}{100}$

**Solution:**
"Of dog owners" → restrict to the "Own a Dog" column → denominator = 100.
"Also own a cat" → the cell in the "Own a Cat" row and "Own a Dog" column → numerator = 40.

Fraction: $\frac{40}{100} = 0.4 = 40\%$.

**Answer: B.**

**Wrong answer analysis:**
- A ($\frac{40}{200}$): This uses the grand total. It answers "what fraction of ALL people own both a dog and a cat?" Not the question asked.
- C ($\frac{40}{70}$): This restricts to cat owners instead of dog owners (column vs. row confusion).
- D ($\frac{70}{100}$): This is the proportion of dog owners who own a cat? No—70 is ALL cat owners, and 100 is dog owners. This fraction is meaningless in context; it asks "what fraction of dog owners are cat owners?" but uses the wrong numerator.

### Worked Example 2: Conditional Probability Wording

**Problem:** The same table as above. Given that a randomly selected person does NOT own a cat, what is the probability the person owns a dog?

**Solution:**
"Given that... does NOT own a cat" → restrict to "No Cat" row → denominator = 130.
"Owns a dog" → the cell in "No Cat" row and "Own a Dog" column → numerator = 60.

Probability: $\frac{60}{130} = \frac{6}{13} \approx 0.462$.

This is $P(\text{Dog} \mid \text{No Cat}) = \frac{60}{130}$.

### Worked Example 3: Finding Missing Values

**Problem:** A two-way table is partially complete:

|               | Passed | Failed | Total |
|---------------|:------:|:------:|:-----:|
| **Studied**   |   72   |        |       |
| **Didn't Study** |      |   30   |   50  |
| **Total**     |        |   42   |  120  |

What is the probability that a randomly selected student who passed also studied?

**Solution:**
First, complete the table:

- Grand total = 120, "Didn't Study" row total = 50, so "Studied" row total = 120 − 50 = 70.
- "Failed" total = 42, so "Passed" total = 120 − 42 = 78.
- "Studied" and "Passed" = 72, so "Studied" and "Failed" = 70 − 72 = −2... That can't be right.

Let me re-check. "Studied" row: 72 passed, total studied = 120 − 50 = 70. But 72 > 70, which is impossible. I need different numbers.

Let me redesign the table:

|               | Passed | Failed | Total |
|---------------|:------:|:------:|:-----:|
| **Studied**   |   54   |        |   60  |
| **Didn't Study** |      |   30   |   40  |
| **Total**     |        |   36   |  100  |

Complete:
- "Studied" and "Failed": 60 − 54 = 6.
- "Didn't Study" and "Passed": 40 − 30 = 10.
- "Passed" total: 54 + 10 = 64. (Check: 64 + 36 = 100 ✓)
- "Failed" total: 6 + 30 = 36. ✓

Now: "probability that a randomly selected student who passed also studied" = $\frac{54}{64} = \frac{27}{32} = 0.84375$.

---

## Practice Problems

Use this table for problems 1-4:

A survey of 150 high school students about whether they play a sport and/or a musical instrument:

|                        | Plays Instrument | No Instrument | Total |
|------------------------|:----------------:|:-------------:|:-----:|
| **Plays a Sport**      |        35        |      55       |  90   |
| **Does Not Play Sport**|        25        |      35       |  60   |
| **Total**              |        60        |      90       |  150  |

1. What fraction of the students play both a sport and an instrument?
   A) $\frac{35}{150}$
   B) $\frac{35}{90}$
   C) $\frac{35}{60}$
   D) $\frac{90}{150}$

2. Among the students who play an instrument, what percent also play a sport?
   A) About 23.3%
   B) About 38.9%
   C) About 58.3%
   D) About 60.0%

3. Given that a student plays a sport, what is the probability the student does NOT play an instrument?
   A) $\frac{55}{90}$
   B) $\frac{55}{150}$
   C) $\frac{35}{90}$
   D) $\frac{55}{60}$

4. A student claims that "most students who play an instrument also play a sport." Is this claim supported by the data?
   A) Yes, because $\frac{35}{60} > 0.5$
   B) Yes, because $\frac{35}{150} > 0.5$
   C) No, because $\frac{35}{60} \approx 0.583$ which is > 0.5, so actually yes
   D) No, because $\frac{25}{60} \approx 0.417$, which means most instrument players do NOT play a sport.

   *(Wait—$\frac{35}{60} \approx 0.583 > 0.5$, so the claim IS supported. Let me revise the question.)*

   **Revised:** A student claims that "most students who play an instrument also play a sport." Is this claim supported?
   A) Yes, because 35 out of 60 instrument players (about 58.3%) also play a sport.
   B) No, because 35 is less than 55.
   C) No, because only $\frac{35}{150} = 23.3\%$ of all students are in that category.
   D) No, because more students play sports without instruments (55) than with instruments (35).

5. A two-way table has row totals of 80 and 120, and column totals of 90 and 110. What is the grand total?
   A) 190
   B) 200
   C) 210
   D) Cannot be determined

6. **(Challenge)** In a school, 60% of students take Art, 45% take Music, and 20% take both. What percent of students take neither Art nor Music?
   A) 5%
   B) 10%
   C) 15%
   D) 25%

---

## Answers

1. **Answer: A.** The question asks "what fraction of **the students**" — meaning of ALL students (grand total). Students who play both = 35. Fraction = $\frac{35}{150}$. **Wrong answers:** B uses only sport players as denominator. C uses instrument players. D is the fraction who play sports.

2. **Answer: C.** "Among the students who play an instrument" → denominator = 60 (instrument column total). "Also play a sport" → numerator = 35. $\frac{35}{60} \times 100\% \approx 58.3\%$. **Wrong answers:** A: $\frac{35}{150} \approx 23.3\%$, using grand total. B: $\frac{35}{90} \approx 38.9\%$, using sport players as denominator. D: $\frac{90}{150} = 60\%$, percentage of all students who play sports.

3. **Answer: A.** "Given that a student plays a sport" → denominator = 90. "Does NOT play an instrument" → numerator = 55. $\frac{55}{90}$. **Wrong answers:** B uses grand total. C gives probability of playing an instrument given sports ($\frac{35}{90}$). D restricts to non-instrument players as denominator.

4. **Answer: A.** The claim is about "students who play an instrument" (denominator = 60). Among them, 35 also play sports, which is $\frac{35}{60} \approx 58.3\% > 50\%$. The claim is supported. **Wrong answers:** B uses the wrong denominator (grand total) and also gets a result < 0.5. C and D are incorrect interpretations or calculations.

5. **Answer: B.** Row totals: $80 + 120 = 200$. Column totals: $90 + 110 = 200$. Both should equal the grand total. **Wrong answers:** A (190) adds incorrectly. C (210) adds incorrectly. D is wrong because the grand total is determined by both row and column sums (they must match).

6. **Answer: C.** Using the principle: $P(\text{Art} \cup \text{Music}) = P(\text{Art}) + P(\text{Music}) - P(\text{Both}) = 60\% + 45\% - 20\% = 85\%$. So neither = $100\% - 85\% = 15\%$. **Wrong answers:** A (5%): $100\% - 60\% - 45\% + 20\% = 15\%$ — wait, that gives 15% too. Let me recalculate: A might be from $100 - 60 - 45 = -5$, ignoring the "both" overlap correction but getting the magnitude wrong. B (10%): perhaps $100 - 60 - 45 + 20 = 15$ miscalculated as 10. C is correct at 15%. D (25%) = $100 - 60 - 45 + 50$ (using 50% instead of 20%).
