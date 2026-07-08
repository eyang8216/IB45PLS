# Lesson 6: Scatterplots & Line of Best Fit

## What You'll Learn
- Interpreting scatterplots: positive/negative correlation and strength
- The correlation coefficient $r$ and what it tells you
- Finding and using the line of best fit equation
- Making predictions: interpolation (safe) vs. extrapolation (risky)
- The critical distinction: correlation ≠ causation
- SAT question pattern: "which equation best models the data?"

## SAT Context

Scatterplot and line-of-best-fit questions appear consistently on the SAT, typically 2-4 per test. These are data analysis questions that AAHL does not cover in depth. The SAT will show you a scatterplot—sometimes with the line of best fit drawn, sometimes asking you to choose which equation fits—and ask you to interpret the slope, make a prediction, or evaluate a claim. The math is simple (you're not calculating the line by hand), but the interpretation traps are numerous and subtle. This is an area where you cannot lean on your AAHL algebra skills; you must learn SAT-specific data reasoning.

## Understanding Scatterplots

### What a Scatterplot Shows
Each point represents one observation with two measurements: an $x$-value (independent variable) and a $y$-value (dependent variable).

### Correlation Direction
- **Positive correlation:** As $x$ increases, $y$ tends to increase. (Points slope upward.)
- **Negative correlation:** As $x$ increases, $y$ tends to decrease. (Points slope downward.)
- **No correlation:** No discernible pattern. (Points form a cloud.)

### Correlation Strength
- **Strong:** Points cluster tightly around a line.
- **Moderate:** Points follow a trend but with more scatter.
- **Weak:** Points barely suggest a trend.

The **correlation coefficient $r$** quantifies strength and direction:
- $r$ ranges from $-1$ to $+1$.
- $r > 0$: positive correlation. $r < 0$: negative correlation.
- $|r|$ close to 1: strong. $|r|$ close to 0: weak.
- $r = 0.9$ is strong positive; $r = -0.3$ is weak negative.

> **SAT Note:** The digital SAT may ask you to identify which $r$ value matches a given scatterplot. Look at the direction first (positive or negative) to eliminate half the options, then judge strength.

## The Line of Best Fit

The line of best fit (also called the regression line or trend line) is the line that minimizes the total distance from all points. On the SAT, it's usually given as:
$$y = mx + b$$
where $m$ is the slope and $b$ is the $y$-intercept.

### Interpreting Slope in Context
The slope $m$ means: "For each increase of 1 in $x$, the predicted $y$ increases by $m$."

**Example:** If a line of best fit for hours studied ($x$) vs. test score ($y$) has slope 8.5, then: "For each additional hour studied, the predicted test score increases by 8.5 points."

### Interpreting Intercept in Context
The $y$-intercept $b$ means: "When $x = 0$, the predicted $y$ is $b$." But be careful—the intercept may not be meaningful if $x = 0$ is outside the data range.

### Finding the Line of Best Fit with Desmos

If the SAT gives you a table of data and asks for the line of best fit:
1. Enter the data in a Desmos table (add a table, enter $x_1$ and $y_1$ values).
2. Type: `y1 ~ m x1 + b`
3. Desmos shows you $m$ and $b$ instantly.

The tilde `~` tells Desmos to perform regression.

## Predictions: Interpolation vs. Extrapolation

### Interpolation
Predicting within the range of the data. **Generally reliable.**

**Example:** Data has $x$ from 10 to 50. Predicting $y$ when $x = 30$ is interpolation.

### Extrapolation
Predicting beyond the range of the data. **Risky and often unreliable.**

**Example:** Data has $x$ from 10 to 50. Predicting $y$ when $x = 80$ is extrapolation. The trend might not continue.

> **🚨 SAT TRAP ALERT: Correlation ≠ Causation.** This is the single most tested statistical reasoning concept on the SAT. Just because two variables are correlated does NOT mean one causes the other. Example: "There is a strong positive correlation between ice cream sales and drowning deaths." Does ice cream cause drowning? No. A third variable (hot weather) causes both. The SAT LOVES to give you a correlation and ask whether a causal claim is valid. The answer is almost always "No, correlation does not imply causation" or "The data shows only an association, not a cause-effect relationship."

> **🔍 PATTERN RECOGNITION: "Which equation best models the data?"** When you see this question with answer choices in the form $y = mx + b$:
> 1. Check the $y$-intercept ($b$): look at where the line hits the $y$-axis on the graph. Eliminate choices with clearly wrong intercepts.
> 2. Check the slope ($m$): is it positive or negative? Steep or shallow? Eliminate choices with wrong signs.
> 3. For the remaining choices, test one point from the graph (pick an easy one) in each equation. The equation that gives the closest $y$ is the best.

### Worked Example 1: Interpreting Slope from a Scatterplot

**Problem:** A scatterplot shows the relationship between the number of employees ($x$) at a company and the company's annual revenue ($y$, in millions of dollars). The line of best fit has equation $y = 0.15x + 2.3$. What does the slope 0.15 represent?

A) The revenue of a company with 0 employees.
B) The predicted revenue for each additional employee, in millions of dollars.
C) The total revenue, in millions of dollars.
D) The number of employees when revenue is 0.

**Solution:**
The slope is the rate of change: for each additional unit of $x$ (1 employee), $y$ (revenue) changes by 0.15 (million dollars, or $150,000).

**Answer: B.**

**Wrong answer analysis:**
- A describes the $y$-intercept 2.3, not the slope.
- C is too vague; it doesn't specify "per employee" or "additional."
- D describes the $x$-intercept (solving $0.15x + 2.3 = 0$), not the slope.

### Worked Example 2: Correlation vs. Causation

**Problem:** A study finds a strong negative correlation ($r = -0.92$) between the number of hours students spend on social media and their GPA. Which of the following conclusions is valid?

A) Spending more time on social media causes students' GPAs to decrease.
B) Students with higher GPAs are more disciplined and therefore use social media less.
C) There is an association between social media use and GPA, but causation cannot be determined.
D) Reducing social media use to zero would guarantee a 4.0 GPA.

**Solution:**
The study shows correlation, not causation. We don't know if social media causes lower GPA, if lower GPA causes more social media use, or if a third factor (like sleep or study habits) affects both.

**Answer: C.**

**Wrong answer analysis:**
- A assumes causation from correlation—invalid.
- B does the same in the opposite direction—also invalid.
- D is absurd on multiple levels (extrapolation, assuming causation, overstatement).

### Worked Example 3: Picking the Best Model Equation

**Problem:** A scatterplot shows data points that trend upward, roughly passing through $(0, 5)$ and $(10, 35)$. Which equation best models the data?

A) $y = 2x + 5$
B) $y = 3x + 5$
C) $y = 5x + 2$
D) $y = -3x + 35$

**Solution:**
1. Direction: upward = positive slope. Eliminate D (negative slope).
2. $y$-intercept: The line passes near $(0, 5)$, so $b \approx 5$. Eliminate C ($b=2$) and check A and B.
3. Slope: from $(0, 5)$ to $(10, 35)$, slope = $\frac{35-5}{10-0} = \frac{30}{10} = 3$.
4. Equation: $y = 3x + 5$.

**Answer: B.**

**Wrong answer analysis:**
- A has the right intercept but wrong slope (too shallow).
- C has wrong intercept and wrong slope.
- D has negative slope (wrong direction) and wrong intercept.

---

## Practice Problems

1. A scatterplot shows the relationship between daily high temperature ($x$, °F) and number of ice cream cones sold ($y$). The points trend upward in a roughly linear pattern. Which $r$ value is most plausible?
   A) $r = -0.85$
   B) $r = -0.15$
   C) $r = 0.15$
   D) $r = 0.85$

2. The line of best fit for data relating hours of exercise per week ($x$) and resting heart rate ($y$, bpm) is $y = -2.5x + 78$. What does the slope of $-2.5$ indicate?
   A) The resting heart rate of someone who doesn't exercise.
   B) For each additional hour of exercise per week, predicted resting heart rate decreases by 2.5 bpm.
   C) Resting heart rate decreases by 2.5 bpm per week regardless of exercise.
   D) The correlation is negative, so the data is unreliable.

3. Data on study time ($x$, hours) and exam score ($y$, points) has line of best fit $y = 8.2x + 52$. The data ranges from $x = 1$ to $x = 10$ hours. Which prediction is most reliable?
   A) The score for 5 hours of study.
   B) The score for 0 hours of study.
   C) The score for 20 hours of study.
   D) The score for 100 hours of study.

4. A study finds a strong positive correlation between the number of firefighters at a fire and the amount of damage caused. Which statement is correct?
   A) More firefighters cause more damage, so fewer should be sent.
   B) The correlation is likely due to a third variable: larger fires require more firefighters and cause more damage.
   C) The data proves that adding firefighters increases damage.
   D) There is no relationship; the correlation is coincidental.

5. A scatterplot shows data with the following summary: when $x = 0$, $y$ is approximately 12; when $x = 20$, $y$ is approximately 72. Which line of best fit is consistent with these observations?
   A) $y = 3x + 12$
   B) $y = 3x - 12$
   C) $y = 12x + 3$
   D) $y = 60x + 12$

6. **(Challenge)** A scatterplot shows a strong linear relationship. The mean of the $x$-values is 50, and the mean of the $y$-values is 75. The line of best fit must pass through which point?
   A) $(0, 0)$
   B) $(0, 75)$
   C) $(50, 0)$
   D) $(50, 75)$

---

## Answers

1. **Answer: D.** Upward trend → positive $r$, so eliminate A and B. "Roughly linear" suggests a strong correlation, so $r = 0.85$ is more plausible than $0.15$. **Wrong answers:** A has strong negative correlation—wrong direction. B has weak negative correlation—wrong direction and too weak. C is positive but too weak for a "roughly linear" trend.

2. **Answer: B.** The slope is the rate of change: for each 1-unit increase in $x$ (hours of exercise), $y$ (resting heart rate) changes by $-2.5$ (decreases by 2.5 bpm). **Wrong answers:** A describes the $y$-intercept (78), not the slope. C removes the connection to exercise and states it as a universal fact—wrong. D incorrectly links negative correlation with unreliability; negative correlation is perfectly valid.

3. **Answer: A.** 5 hours is within the data range (1-10), so this is interpolation—generally reliable. **Wrong answers:** B ($x=0$) is technically extrapolation (data starts at $x=1$) and the intercept may not be meaningful. C ($x=20$) and D ($x=100$) are extreme extrapolations far beyond the data range; the linear trend may not continue.

4. **Answer: B.** This is the classic "correlation ≠ causation" example. Larger fires (third variable) cause both more firefighters to be sent AND more damage. **Wrong answers:** A assumes causation and makes a dangerous recommendation. C falsely claims "proves." D dismisses the correlation entirely when it likely has a real (if indirect) explanation.

5. **Answer: A.** At $x=0$, $y \approx 12$ → intercept $b = 12$. Slope: $\frac{72-12}{20-0} = \frac{60}{20} = 3$. Equation: $y = 3x + 12$. **Wrong answers:** B has wrong sign on intercept ($-12$ instead of $+12$). C swaps slope and intercept. D has absurdly steep slope of 60.

6. **Answer: D.** A fundamental property of the least-squares regression line: it always passes through the point $(\bar{x}, \bar{y})$, the mean of $x$ and mean of $y$. So it passes through $(50, 75)$. **Wrong answers:** A $(0,0)$ is the origin, which regression lines do not generally pass through. B $(0,75)$ and C $(50,0)$ are also not general properties of the regression line.
