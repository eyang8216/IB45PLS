# Lesson 44: Modulus Functions and Inequalities

## What You Will Learn and Why It Matters

The **modulus** (or absolute value) of a number is its distance from zero on the number line. Distance is never negative, so the modulus of any number is always zero or positive. The modulus function appears throughout IB AAHL: in solving equations where a quantity could be positive or negative, in inequalities that describe a range around a central value, and in graph sketching where parts of a curve below the $x$-axis get reflected upward. Understanding the modulus deeply also prepares you for topics like complex numbers, where $|z|$ represents the distance from the origin in the complex plane.

---

## 1. Defining the Modulus Function

The modulus of $x$ is written as $|x|$ and is defined piecewise:

$$|x| = \begin{cases} x, & \text{if } x \geq 0 \\ -x, & \text{if } x < 0 \end{cases}$$

When $x$ is negative, multiplying by $-1$ makes it positive. For example, $|5| = 5$ and $|{-5}| = 5$. Both 5 and $-5$ are five units away from zero.

Three important properties of the modulus:
- $|x| \geq 0$ for every real number $x$. The modulus can never be negative.
- $|ab| = |a| \cdot |b|$. The modulus of a product equals the product of the moduli.
- $|a + b| \leq |a| + |b|$. This is called the **triangle inequality**. The direct distance from 0 to $a + b$ is never greater than going from 0 to $a$ and then from $a$ to $b$.

---

## 2. Solving Modulus Equations

### Type 1: $|f(x)| = k$ where $k \geq 0$

The equation $|f(x)| = k$ means the quantity $f(x)$ is exactly $k$ units away from zero. This happens when $f(x) = k$ OR $f(x) = -k$. You must solve both equations.

If $k < 0$, there is no solution, because a modulus can never equal a negative number.

### Worked Example 1

**Problem:** Solve the equation $|2x - 3| = 5$.

**Approach:** Write two separate equations: $2x - 3 = 5$ and $2x - 3 = -5$. Solve each one.

**Step-by-step working:**
1. First equation: $2x - 3 = 5$. Add $3$: $2x = 8$. Divide by $2$: $x = 4$.
2. Second equation: $2x - 3 = -5$. Add $3$: $2x = -2$. Divide by $2$: $x = -1$.

The solutions are $x = -1$ and $x = 4$.

**Why this makes sense:** When $x = 4$, $|2(4) - 3| = |8 - 3| = |5| = 5$. When $x = -1$, $|2(-1) - 3| = |{-2} - 3| = |{-5}| = 5$. Both work.

---

### Type 2: $|f(x)| = |g(x)|$

If two expressions have the same modulus, then either they are equal or they are opposites. Solve $f(x) = g(x)$ and $f(x) = -g(x)$.

### Worked Example 2

**Problem:** Solve the equation $|x + 1| = |2x - 3|$.

**Approach:** Set up two equations: $x + 1 = 2x - 3$ and $x + 1 = -(2x - 3)$. Solve both.

**Step-by-step working:**
1. First equation: $x + 1 = 2x - 3$. Subtract $x$: $1 = x - 3$. Add $3$: $x = 4$.
2. Second equation: $x + 1 = -2x + 3$. Add $2x$: $3x + 1 = 3$. Subtract $1$: $3x = 2$. Divide by $3$: $x = \frac{2}{3}$.

The solutions are $x = \frac{2}{3}$ and $x = 4$.

**Why this makes sense:** At $x = 4$, $|4 + 1| = 5$ and $|2(4) - 3| = |5| = 5$. At $x = \frac{2}{3}$, $|\frac{2}{3} + 1| = |\frac{5}{3}| = \frac{5}{3}$ and $|2(\frac{2}{3}) - 3| = |\frac{4}{3} - \frac{9}{3}| = |{-\frac{5}{3}}| = \frac{5}{3}$. Both match.

---

## 3. Solving Modulus Inequalities

### Type A: $|f(x)| < k$ where $k > 0$

The expression $|f(x)| < k$ means the value of $f(x)$ is less than $k$ units from zero. This happens when $f(x)$ is between $-k$ and $k$. The inequality is equivalent to:

$$-k < f(x) < k$$

### Worked Example 3

**Problem:** Solve the inequality $|x - 2| < 3$.

**Approach:** Rewrite as a double inequality: $-3 < x - 2 < 3$. Then isolate $x$.

**Step-by-step working:**
1. $-3 < x - 2 < 3$.
2. Add $2$ to all three parts: $-3 + 2 < x < 3 + 2$.
3. Simplify: $-1 < x < 5$.

The solution is all real numbers $x$ such that $-1 < x < 5$. In interval notation: $(-1, 5)$.

---

### Type B: $|f(x)| > k$ where $k \geq 0$

The expression $|f(x)| > k$ means the value of $f(x)$ is more than $k$ units from zero. This happens when $f(x) < -k$ OR $f(x) > k$. The two regions are separate.

### Worked Example 4

**Problem:** Solve the inequality $|2x + 1| \geq 5$.

**Approach:** Split into two inequalities: $2x + 1 \leq -5$ OR $2x + 1 \geq 5$. Solve each.

**Step-by-step working:**
1. First branch: $2x + 1 \leq -5$. Subtract $1$: $2x \leq -6$. Divide by $2$: $x \leq -3$.
2. Second branch: $2x + 1 \geq 5$. Subtract $1$: $2x \geq 4$. Divide by $2$: $x \geq 2$.

The solution is $x \leq -3$ or $x \geq 2$. In interval notation: $(-\infty, -3] \cup [2, \infty)$.

**Common misconception:** Some students write $-5 \geq 2x + 1 \geq 5$ for this type. That is wrong. The inequality $|f(x)| > k$ splits into two separate intervals, not a double inequality.

---

## 4. Graphs Involving Modulus

There are two distinct types of modulus graphs that students often confuse.

**Type 1: $y = |f(x)|$.** Take the original graph of $y = f(x)$. Any portion that lies below the $x$-axis (where $f(x) < 0$) gets reflected upward to become positive. Portions already above the $x$-axis stay unchanged.

**Type 2: $y = f(|x|)$.** Take the portion of the original graph for $x \geq 0$ (the right half). Mirror it across the $y$-axis to produce the left half. The graph becomes symmetric about the $y$-axis.

### Worked Example 5

**Problem:** Describe the graph of $y = |x^2 - 4|$.

**Approach:** Start with the parabola $y = x^2 - 4$, which opens upward and crosses the $x$-axis at $x = \pm 2$. Between $-2$ and $2$, the parabola is below the $x$-axis. Reflect that portion upward.

**Step-by-step working:**
1. For $|x| \geq 2$, the parabola $x^2 - 4$ is already non-negative. The graph stays as $y = x^2 - 4$.
2. For $|x| < 2$, the parabola is negative. The modulus reflects it: $y = -(x^2 - 4) = 4 - x^2$.

The graph looks like a parabola that dips to $y = -4$ at $x = 0$ in its original form, but the modulus version bounces that dip upward, creating a W-shaped curve with a peak at $(0, 4)$ and touching the $x$-axis at $x = \pm 2$.

---

## 5. Advanced Modulus Inequalities with Multiple Terms

When an inequality contains more than one modulus term, like $|x - a| + |x - b| < c$, the most reliable method is to identify **critical points** where each expression inside a modulus equals zero. These points divide the number line into intervals. On each interval, every modulus expression has a definite sign, so you can remove the modulus bars and solve a regular inequality.

### Worked Example 6

**Problem:** Solve $|x - 1| + |x - 3| < 5$.

**Approach:** Find the critical points by setting each expression inside modulus to zero: $x = 1$ and $x = 3$. These split the real line into three intervals: $x < 1$, $1 \leq x < 3$, and $x \geq 3$. On each interval, determine whether $(x - 1)$ and $(x - 3)$ are positive or negative, replace the modulus signs accordingly, and solve.

**Step-by-step working:**

**Interval 1: $x < 1$.** Here $x - 1 < 0$ and $x - 3 < 0$. So $|x - 1| = -(x - 1) = 1 - x$ and $|x - 3| = -(x - 3) = 3 - x$. The inequality becomes $(1 - x) + (3 - x) < 5$, which simplifies to $4 - 2x < 5$. Subtract $4$: $-2x < 1$. Divide by $-2$ (reversing the inequality): $x > -\frac{1}{2}$. Combined with $x < 1$, this interval gives $-\frac{1}{2} < x < 1$.

**Interval 2: $1 \leq x < 3$.** Here $x - 1 \geq 0$ and $x - 3 < 0$. So $|x - 1| = x - 1$ and $|x - 3| = 3 - x$. The inequality becomes $(x - 1) + (3 - x) < 5$, which simplifies to $2 < 5$. This is always true. So the entire interval $1 \leq x < 3$ is part of the solution.

**Interval 3: $x \geq 3$.** Here both $x - 1 \geq 0$ and $x - 3 \geq 0$. So $|x - 1| = x - 1$ and $|x - 3| = x - 3$. The inequality becomes $(x - 1) + (x - 3) < 5$, which simplifies to $2x - 4 < 5$. Add $4$: $2x < 9$. Divide by $2$: $x < \frac{9}{2}$. Combined with $x \geq 3$, this interval gives $3 \leq x < \frac{9}{2}$.

**Union of all intervals:** $-\frac{1}{2} < x < \frac{9}{2}$.

**Why this makes sense:** The expression $|x - 1| + |x - 3|$ represents the sum of distances from $x$ to $1$ and from $x$ to $3$. The smallest possible sum is $2$, which occurs when $x$ is between $1$ and $3$ (the distance between the two points). The inequality asks for values where this sum is less than $5$, which is a generous bound, giving an interval larger than $[-1, 5]$ by half a unit on each side.

---

## Practice Problems

**1.** Solve the equation $|3x - 6| = 9$.

**2.** Solve the equation $|x + 4| = |2x - 1|$.

**3.** Solve the inequality $|x - 5| \leq 7$. Write your answer in interval notation.

**4.** Solve the inequality $|2x + 3| > 8$. Write your answer as a union of intervals.

**5.** (IB Exam Style) Solve the inequality $|x + 1| > 2|x - 1|$.

(a) By squaring both sides, transform the inequality into a quadratic inequality in $x$. [2 marks]

(b) Solve the resulting quadratic inequality. [2 marks]

(c) State the final solution as an interval and verify that $x = 0$ satisfies the original inequality while $x = 4$ does not. [2 marks]

**6.** Solve the equation $|x^2 - x - 2| = 2$.

---

## Answers

**1.** Split into two equations. First: $3x - 6 = 9$, so $3x = 15$ and $x = 5$. Second: $3x - 6 = -9$, so $3x = -3$ and $x = -1$. The solutions are $x = -1$ and $x = 5$. A common mistake is to forget the negative branch, giving only $x = 5$.

**2.** Set $x + 4 = 2x - 1$ or $x + 4 = -(2x - 1)$. First equation: $x + 4 = 2x - 1$, subtract $x$ and add $1$: $5 = x$. Second equation: $x + 4 = -2x + 1$, add $2x$ and subtract $4$: $3x = -3$, so $x = -1$. Solutions: $x = -1$ and $x = 5$.

**3.** Rewrite as $-7 \leq x - 5 \leq 7$. Add $5$ to all three parts: $-2 \leq x \leq 12$. In interval notation: $[-2, 12]$. Visually, this is all points within 7 units of 5 on the number line.

**4.** Split into two inequalities. First: $2x + 3 < -8$, so $2x < -11$ and $x < -\frac{11}{2}$. Second: $2x + 3 > 8$, so $2x > 5$ and $x > \frac{5}{2}$. Solution: $(-\infty, -\frac{11}{2}) \cup (\frac{5}{2}, \infty)$. Note that strict inequality in the original means open intervals in the answer.

**5.** (a) Square both sides: $(x + 1)^2 > 4(x - 1)^2$. Expand: $x^2 + 2x + 1 > 4(x^2 - 2x + 1) = 4x^2 - 8x + 4$. Bring all terms to one side: $0 > 3x^2 - 10x + 3$, or equivalently $3x^2 - 10x + 3 < 0$. [2 marks]

(b) Factor the quadratic: $3x^2 - 10x + 3 = (3x - 1)(x - 3)$. The roots are $x = \frac{1}{3}$ and $x = 3$. Since the quadratic opens upward (coefficient of $x^2$ is positive), it is negative between the roots. So $\frac{1}{3} < x < 3$. [2 marks]

(c) Solution: $\left(\frac{1}{3}, 3\right)$. Check $x = 0$: $|0 + 1| = 1$ and $2|0 - 1| = 2$. Is $1 > 2$? No. Wait — $x = 0$ is outside the interval and does NOT satisfy. Let us check $x = 2$: $|2 + 1| = 3$ and $2|2 - 1| = 2$. Is $3 > 2$? Yes. And $2$ is inside $\left(\frac{1}{3}, 3\right)$. For $x = 4$: $|4 + 1| = 5$ and $2|4 - 1| = 6$. Is $5 > 6$? No. Correct. [2 marks]

**6.** This is $|f(x)| = k$, so solve $x^2 - x - 2 = 2$ and $x^2 - x - 2 = -2$. First equation: $x^2 - x - 2 = 2$, so $x^2 - x - 4 = 0$. Using the quadratic formula: $x = \frac{1 \pm \sqrt{1 + 16}}{2} = \frac{1 \pm \sqrt{17}}{2}$. Second equation: $x^2 - x - 2 = -2$, so $x^2 - x = 0$, which factors as $x(x - 1) = 0$, giving $x = 0$ or $x = 1$. Solutions: $x = 0$, $x = 1$, $x = \frac{1 + \sqrt{17}}{2}$, $x = \frac{1 - \sqrt{17}}{2}$.
