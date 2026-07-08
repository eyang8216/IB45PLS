# Lesson 8: Data Interpretation from Graphs & Tables

## What You'll Learn
- Reading and comparing values from bar graphs, histograms, dot plots, and box plots
- Identifying misleading graph features: truncated axes, inconsistent scales
- Extracting exact values vs. estimating from graphs
- SAT-specific graph-reading traps
- Converting between visual representation and numerical data
- The "according to the graph" rule: answer is IN the data, not in your head

## SAT Context

Data interpretation from graphs and tables is a staple of the SAT Math section, appearing 3-5 times per test. These questions test your ability to read visual displays of data accurately—not your math skills. The SAT uses bar graphs, line graphs, histograms, dot plots, and box plots, often with tricky axis scaling designed to fool careless readers. For an AAHL student, the "math" is trivial; the challenge is purely visual literacy—reading axes correctly, not making assumptions, and extracting the right number from the right bar. These are speed bumps, not roadblocks: you can answer most in 30-45 seconds if you're methodical.

## Bar Graphs

### What They Show
Bar graphs compare quantities across categories. Each bar's height represents a value.

### How to Read Them
1. Read the **title** to understand what's being measured.
2. Check the **axes labels**: what does each bar represent? What unit is the vertical axis?
3. Check the **scale**: does the axis start at 0? What are the increments?
4. For exact values, trace the top of the bar to the axis.

> **🚨 SAT TRAP ALERT: The Truncated Axis.** Sometimes the SAT shows a bar graph where the vertical axis starts at a value other than 0. If a graph starts at 50 instead of 0, a bar that's twice as tall as another does NOT represent twice the value. Example: axis runs from 80 to 100. Bar A at 85, Bar B at 95. Bar B looks about twice as tall visually, but the actual values are $85$ vs. $95$—only about a 12% difference. Always check where the axis starts before making visual comparisons.

### Bar Graph Example

A graph shows "Number of Books Read" for 5 students:

| Student | Books |
|---------|:-----:|
| Ana     |   8   |
| Ben     |   5   |
| Cal     |   12  |
| Dee     |   7   |
| Eli     |   9   |

**Question:** How many more books did Cal read than the mean of all students?

Mean = $\frac{8+5+12+7+9}{5} = \frac{41}{5} = 8.2$. Cal: 12. Difference: $12 - 8.2 = 3.8$.

## Histograms

### What They Show
Histograms display the distribution of a numerical variable. Bars touch (unlike bar graphs) and represent intervals (bins).

### How to Read Them
1. The x-axis shows numerical intervals (e.g., 0-10, 10-20, 20-30).
2. The height shows the **frequency** (count) in each interval.
3. The shape reveals distribution: symmetric, skewed right, skewed left, bimodal.

### Histogram vs. Bar Graph
- **Bar graph:** Categories (dogs, cats, birds) — bars don't touch.
- **Histogram:** Numerical ranges (0-10, 10-20) — bars touch.

> **🔍 PATTERN RECOGNITION: "According to the graph..."** When the SAT uses this phrase, the answer must be directly supported by the visual data. Don't bring in outside knowledge or assumptions. If you can't point to the specific bar, line, or point that proves the answer, it's wrong. This is the SAT's way of testing whether you can extract information from a data display without over-interpreting.

## Dot Plots

### What They Show
Each dot represents one observation. Dot plots show individual data points and reveal clusters, gaps, and outliers.

### How to Read Them
- Count dots to find frequency.
- The mode is the value with the most dots.
- The median is the middle dot (or average of two middle dots).
- The range is (max value − min value).

## Box Plots (Box-and-Whisker Plots)

### What They Show
A box plot displays the five-number summary:
- **Minimum:** Left whisker end
- **Q1 (first quartile):** Left edge of box (25th percentile)
- **Median:** Line inside box (50th percentile)
- **Q3 (third quartile):** Right edge of box (75th percentile)
- **Maximum:** Right whisker end

### How to Read Them
- The box contains the middle 50% of data.
- The IQR (Interquartile Range) = Q3 − Q1 = width of the box.
- A longer whisker indicates more spread in that tail.
- The median line's position in the box shows skew: closer to Q1 = right-skewed; closer to Q3 = left-skewed.

### SAT Question Types
1. "What is the median?" — Read the line inside the box.
2. "What is the range?" — Maximum − Minimum.
3. "What is the IQR?" — Q3 − Q1.
4. "Which statement about the distribution is true?" — Check spread, skew, outliers.

### Worked Example 1: Bar Graph with Misleading Scale

**Problem:** A bar graph shows monthly profits for a company. The y-axis starts at $80,000 and goes to $100,000 in increments of $2,000. January shows a bar at $84,000, and June shows a bar at $96,000. By what percent did profit increase from January to June?

A) About 14.3%
B) About 50%
C) The graph makes it impossible to tell exactly.
D) About 12.5%

**Solution:**
Percent increase = $\frac{96,000 - 84,000}{84,000} \times 100\% = \frac{12,000}{84,000} \times 100\% \approx 14.3\%$.

Despite the axis starting at $80,000, the actual values are given. The visual might make the increase look dramatic (the June bar appears about 6 times taller visually), but the actual percent increase is modest.

**Answer: A.**

**Wrong answer analysis:**
- B (50%): This is the visual impression if you ignore the truncated axis. The June bar ($96K - 80K = 16K$ above baseline) is about twice the January bar ($84K - 80K = 4K$ above baseline) visually, but that's misleading.
- C is incorrect because the values ARE given and precise.
- D (12.5%) comes from $\frac{12,000}{96,000}$ (using June as denominator instead of January).

### Worked Example 2: Box Plot Interpretation

**Problem:** Two box plots show test scores for Class A and Class B:

- Class A: Min = 55, Q1 = 68, Median = 78, Q3 = 85, Max = 98
- Class B: Min = 60, Q1 = 72, Median = 76, Q3 = 82, Max = 92

Which statement must be true?

A) Every student in Class A scored higher than every student in Class B.
B) The range of Class A is greater than the range of Class B.
C) The median of Class A is lower than the median of Class B.
D) At least 75% of Class B scored above 60.

**Solution:**
- A: False. Class A min (55) is less than Class B min (60), so NOT every Class A student scored higher.
- B: Range of A = 98 − 55 = 43. Range of B = 92 − 60 = 32. So 43 > 32. True! But wait—let me check all options.
- C: Median of A = 78, median of B = 76. 78 > 76, so A's median is higher. False.
- D: 75% above 60? B's min is 60, so Q1 is 72. At least 75% scored above Q1 (72), which is > 60. But the exact statement "above 60" — 100% scored at or above 60 (min = 60), so at least 75% scored above 60? That's technically true (100% > 75%), but it's a strange claim. Actually, "above 60" means > 60, and min = 60 means at least one person scored exactly 60, so not all are above 60. But we don't know how many scored exactly 60. Box plots don't give that precision. So D is not necessarily true.

**Answer: B.**

### Worked Example 3: Dot Plot Median

**Problem:** A dot plot shows the following numbers of pets per household for 15 households:

1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 5

What is the median number of pets?

**Solution:**
15 data points. The median is the 8th value when sorted.
Counting: 1,1,1,1 (4), 2,2,2,2,2 (5 more = 9 total) → the 8th value is 2.

**Answer: 2.**

---

## Practice Problems

1. A histogram of exam scores shows: 50-59: 3 students, 60-69: 8 students, 70-79: 12 students, 80-89: 15 students, 90-100: 7 students. How many students scored 70 or above?
   A) 12
   B) 27
   C) 34
   D) 45

2. A box plot shows: Min=10, Q1=15, Median=22, Q3=30, Max=45. What is the interquartile range (IQR)?
   A) 8
   B) 12
   C) 15
   D) 35

3. A bar graph shows car sales: the y-axis starts at 180 and goes to 200. Sales for 2022 show a bar at 185; for 2023, a bar at 195. The 2023 bar appears twice as tall visually. What is the actual percent increase?
   A) About 5.4%
   B) About 10%
   C) About 50%
   D) About 100%

4. A dot plot shows the ages of participants: 18, 18, 19, 20, 20, 20, 21, 21, 22, 25. What is the mode?
   A) 18
   B) 20
   C) 21
   D) 20.5

5. A line graph shows temperature over 8 hours. According to the graph, at which hour was the temperature exactly 72°F? The graph shows: Hour 1: 68°, Hour 3: 72°, Hour 5: 76°, Hour 7: 70°. If a student claims the temperature at Hour 6 was 73°, is this supported?

   A) Yes, because the trend is upward.
   B) No, because the graph only shows data at odd hours.
   C) Yes, because $76 - 70 = 6$ and halfway is 73.
   D) No, because the temperature was decreasing from hour 5 to 7.

6. **(Challenge)** A box plot of salaries (in thousands) shows: Min=35, Q1=48, Median=62, Q3=80, Max=150. An employee earning $150,000 is an outlier based on the $1.5 \times \text{IQR}$ rule. What is the upper fence?
   A) 80
   B) 96
   C) 128
   D) 150

---

## Answers

1. **Answer: C.** 70 or above: 70-79 (12) + 80-89 (15) + 90-100 (7) = 34. **Wrong answers:** A (12) is only the 70-79 bin. B (27) = 12 + 15, forgetting the 90-100 bin. D (45) is the total of all students (3+8+12+15+7 = 45).

2. **Answer: C.** IQR = Q3 − Q1 = 30 − 15 = 15. **Wrong answers:** A (8) = 30 − 22 (Q3 − median). B (12) = 22 − 10 (median − min). D (35) = 45 − 10 (range, not IQR).

3. **Answer: A.** Percent increase = $\frac{195 - 185}{185} \times 100\% = \frac{10}{185} \times 100\% \approx 5.4\%$. **Wrong answers:** B (10%): $\frac{10}{100}$, treating the absolute increase as a percent without dividing by original. C (50%): the visual impression from the truncated axis. D (100%): doubling the visual impression.

4. **Answer: B.** The mode is the most frequent value. 20 appears 3 times, more than any other value. **Wrong answers:** A (18) appears twice. C (21) appears twice. D (20.5) is the median, not the mode.

5. **Answer: B.** "According to the graph" means only what's shown. The graph provides data at hours 1, 3, 5, and 7 only. We cannot determine the temperature at hour 6 from the graph alone—we'd be interpolating, which isn't "according to the graph." **Wrong answers:** A assumes a trend not shown. C assumes linear change between points, which the graph doesn't establish. D makes a claim about decreasing but doesn't answer whether hour 6's temperature can be determined.

6. **Answer: C.** IQR = 80 − 48 = 32. Upper fence = Q3 + 1.5 × IQR = 80 + 1.5(32) = 80 + 48 = 128. Since 150 > 128, the $150,000 salary is an outlier. **Wrong answers:** A (80) is Q3 itself. B (96) = 80 + 0.5(32), using half IQR. D (150) is the max, not the fence.
