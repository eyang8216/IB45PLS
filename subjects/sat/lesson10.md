# Lesson 10: Mean, Median, Mode, Range & Standard Deviation

## What You'll Learn
- Choosing between mean and median: the effect of outliers
- Calculating and interpreting range and interquartile range (IQR)
- Understanding standard deviation as a measure of spread
- How adding, removing, or changing data affects center and spread
- SAT-specific standard deviation interpretation questions
- Common misconceptions that become wrong answer choices

## SAT Context

Questions about mean, median, standard deviation, and data spread appear 2-4 times per SAT. The SAT rarely asks you to compute standard deviation by hand—instead, it asks you to interpret what it means and how data changes affect it. The most common SAT question type: "A new data point is added. How does this affect the mean and median?" or "Which data set has the larger standard deviation?" For an AAHL student, the calculations are elementary, but the SAT tests conceptual understanding, not computation. The key is knowing the *properties* of these statistics, not just their formulas.

## Mean vs. Median: The Outlier Effect

### Mean (Average)
$$\text{Mean} = \frac{\text{sum of all values}}{\text{number of values}}$$

The mean is **sensitive to outliers**. A single extreme value can pull the mean far from the bulk of the data.

### Median
The middle value when data is sorted. The median is **resistant to outliers**. Adding an extreme value barely moves the median.

### When to Use Which
- **Use the median** when data is skewed or has outliers (e.g., income, housing prices).
- **Use the mean** when data is roughly symmetric without outliers (e.g., heights, test scores).

> **🚨 SAT TRAP ALERT: Outlier's Effect on Mean vs. Median.** A classic SAT question: "A class of 20 students has a mean test score of 75. A new student joins with a score of 100. What happens to the mean and median?" The mean definitely increases. The median... you can't be sure without knowing the original data distribution. The SAT's trap: claiming the median also increases. The median might not change at all if the new score is already above the original median. Don't assume both always move together.

### Example: Income Data

Salaries (in thousands): 35, 38, 40, 42, 45, 48, 50, 55, 60, 500

- Mean = $\frac{35+38+40+42+45+48+50+55+60+500}{10} = \frac{913}{10} = 91.3$K
- Median = average of 5th and 6th values: $\frac{45+48}{2} = 46.5$K

The mean ($91.3$K) is nearly double the median ($46.5$K) because of the one person earning $500$K. In this case, the median gives a better picture of "typical" income.

## Range and IQR

### Range
$$\text{Range} = \text{Max} - \text{Min}$$

Simple but extremely sensitive to outliers.

### Interquartile Range (IQR)
$$\text{IQR} = Q3 - Q1$$

The range of the middle 50% of data. Much more resistant to outliers.

### SAT Question Pattern
"Which is more affected by removing the outlier: the range or the IQR?"

Answer: The range. The IQR only looks at the middle 50%, so an extreme outlier doesn't affect it at all (unless the outlier changes the quartile positions, which it usually doesn't for a single outlier).

## Standard Deviation

### What It Measures
Standard deviation (SD) measures how spread out the data is around the mean. A larger SD means more variability.

### What the SAT Expects You to Know
1. **SD is about spread, not the data values themselves.** A dataset of {100, 105, 110} has a SMALLER standard deviation than {1, 50, 99}, even though the first set has much larger numbers. SD measures how far values are from their mean.
2. **SD is always non-negative.** SD = 0 only when all values are identical.
3. **Adding a constant to every value does NOT change the SD.** ({1, 2, 3} and {101, 102, 103} have the same SD.)
4. **Multiplying every value by a constant multiplies the SD by |constant|.** ({1, 2, 3} × 10 → SD also multiplies by 10.)

> **🚨 SAT TRAP ALERT: Standard Deviation ≠ Range.** A common wrong answer on the SAT confuses SD with the range. A dataset can have a large range but small SD (e.g., {0, 50, 50, 50, 50, 100}: the range is 100, but most values are clustered at 50, so SD is relatively small). Conversely, {0, 10, 20, 30, ..., 100} evenly spread has both large range and large SD. Don't assume one implies the other.

> **🔍 PATTERN RECOGNITION: "Which data set has the greater standard deviation?"** Look for clustering vs. spread. The data set where values are more "spread out" from their mean has the larger SD. Don't be fooled by larger numbers—compare variability, not magnitude. {1, 2, 3, 4, 5} has LARGER SD than {100, 100, 100, 100, 101} even though the second has larger numbers.

### Worked Example 1: Effect of Adding Data

**Problem:** The mean of 8 numbers is 15. If a 9th number, 24, is added, what is the new mean?

**Solution:**
1. Sum of original 8 numbers: $8 \times 15 = 120$.
2. New sum: $120 + 24 = 144$.
3. New mean: $\frac{144}{9} = 16$.

**Key insight:** The new value (24) is above the original mean (15), so the mean increases.

### Worked Example 2: Standard Deviation After Transformation

**Problem:** A data set has mean 40 and standard deviation 5. If every value in the data set is multiplied by 3 and then 10 is subtracted, what are the new mean and standard deviation?

**Solution:**
- New mean: $3 \times 40 - 10 = 120 - 10 = 110$.
- New SD: $|3| \times 5 = 15$. (Subtracting 10 doesn't affect SD—only the multiplicative change matters.)

**General rules:**
- $y = ax + b$: $\text{mean}_y = a \cdot \text{mean}_x + b$, $\text{SD}_y = |a| \cdot \text{SD}_x$.

### Worked Example 3: Comparing Standard Deviations

**Problem:** Three data sets:
- Set A: {5, 5, 5, 5, 5}
- Set B: {4, 4, 5, 6, 6}
- Set C: {1, 3, 5, 7, 9}

Order the sets from smallest to largest standard deviation.

**Solution:**
- Set A: All values identical → SD = 0.
- Set B: Values cluster around 5, with slight spread → small SD.
- Set C: Values evenly spread across a wide range → larger SD.

Order: A < B < C.

---

## Practice Problems

1. A class of 10 students has the following test scores: 72, 75, 78, 80, 82, 85, 88, 90, 92, 95. What is the median score?
   A) 82
   B) 83.5
   C) 85
   D) 83.7

2. A data set of 5 values has mean 20 and median 18. If a new value of 40 is added, which statement must be true?
   A) Both the mean and median increase.
   B) The mean increases, but the effect on the median cannot be determined.
   C) The median increases, but the effect on the mean cannot be determined.
   D) Neither the mean nor the median changes.

3. Data Set X: {10, 12, 14, 16, 18}. Data Set Y: {100, 102, 104, 106, 108}. How do their standard deviations compare?
   A) SD of Y is much larger than SD of X.
   B) SD of Y is much smaller than SD of X.
   C) SD of Y equals SD of X.
   D) Cannot be determined.

4. The mean monthly rent for 9 apartments is $1,400. A 10th apartment rents for $2,200. What is the new mean?
   A) $1,440
   B) $1,460
   C) $1,480
   D) $1,500

5. A data set has minimum 12, Q1 = 18, median = 25, Q3 = 34, maximum = 55. If the maximum value is changed from 55 to 100, which statistics change?
   A) Only the range
   B) Range and mean
   C) Range, mean, and IQR
   D) Range, mean, median, and IQR

6. **(Challenge)** A data set has a standard deviation of 0. Which of the following must be true?
   A) All values equal the mean.
   B) All values are positive.
   C) The mean equals the median.
   D) Both A and C.

---

## Answers

1. **Answer: B.** With 10 values (even), the median is the average of the 5th and 6th values: $\frac{82 + 85}{2} = 83.5$. **Wrong answers:** A (82) is the 5th value (lower median). C (85) is the 6th value (upper median). D (83.7) is the mean, not the median.

2. **Answer: B.** The new value 40 is above the mean (20), so the mean increases. The effect on the median depends on the original data distribution—we only know the median was 18 and 40 is above it, but we don't know if the median shifts or by how much. **Wrong answers:** A assumes median must increase—not necessarily true. C has it backward. D is clearly false for the mean.

3. **Answer: C.** Y = X + 90. Adding a constant shifts all values but doesn't change spread. The standard deviations are identical. **Wrong answers:** A incorrectly associates larger numbers with larger SD. B also confuses magnitude with spread. D is wrong—it can be determined: SDs are equal.

4. **Answer: C.** Sum of 9 = $9 \times 1400 = 12,600$. New sum = $12,600 + 2,200 = 14,800$. New mean = $\frac{14,800}{10} = 1,480$. **Wrong answers:** A ($1,440$): $1400 + \frac{2200-1400}{10} = 1400 + 80 = 1480$ — wait, that's correct. A might be $1400 + \frac{2200}{?}$ miscalculated. B ($1,460$): $1400 + 60$ (using wrong denominator or wrong difference). D ($1,500$): $\frac{1400+2200}{?}$ incorrectly weighted.

5. **Answer: B.** Changing the max from 55 to 100: the range changes (88 instead of 43), and the mean changes (sum increases by 45, divided by N). The median and Q1/Q3 are unaffected because they're based on position, not value, and the max doesn't affect the middle positions. IQR (Q3−Q1) is unchanged. **Wrong answers:** A misses the mean change. C incorrectly includes IQR. D incorrectly includes median and IQR.

6. **Answer: D.** SD = 0 means all values are identical. If all values are identical, they all equal the mean (A is true). And if all values are identical, the mean equals the median equals every value (C is true). **Wrong answers:** A alone is true but incomplete. B is not necessarily true—values could be negative or zero. C alone is true but incomplete.
