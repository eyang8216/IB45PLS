# Lesson 45: Rational Functions and Asymptotes

## What You Will Learn and Why It Matters

A **rational function** is a fraction where both the numerator and the denominator are polynomials. You have already worked with simple rational functions like $f(x) = \frac{1}{x}$. In this lesson, you will learn how to analyze more complicated rational functions by finding vertical asymptotes, horizontal asymptotes, oblique (slant) asymptotes, and intercepts. Rational functions appear in many areas of applied mathematics: they model rates, concentrations, and inverse relationships. In IB AAHL, you need to sketch rational functions, solve rational inequalities, and later, integrate them using partial fractions. Mastering the analysis of asymptotes now will make those topics much easier.

---

## 1. What Is a Rational Function?

A rational function has the form

$$f(x) = \frac{P(x)}{Q(x)}$$

where $P(x)$ and $Q(x)$ are polynomials. The **domain** of a rational function excludes every value of $x$ that makes $Q(x) = 0$, because division by zero is undefined.

---

## 2. Vertical Asymptotes

A **vertical asymptote** is a vertical line $x = a$ that the graph approaches but never touches. As $x$ gets closer and closer to $a$, the value of $f(x)$ grows without bound (either toward $+\infty$ or $-\infty$).

Vertical asymptotes occur where $Q(x) = 0$ AND the factor does not cancel with a matching factor in the numerator. If a factor does cancel, the graph has a **hole** (a removable discontinuity) instead of a vertical asymptote.

### Worked Example 1

**Problem:** Find any vertical asymptotes of $f(x) = \dfrac{x + 1}{x - 2}$.

**Approach:** Set the denominator equal to zero and check whether the numerator is also zero at that value.

**Step-by-step working:**
1. The denominator is $x - 2$. Set $x - 2 = 0$, giving $x = 2$.
2. Check the numerator at $x = 2$: $2 + 1 = 3$, which is not zero.
3. Since the denominator is zero but the numerator is not, there is a vertical asymptote at $x = 2$.

**Why this makes sense:** As $x$ approaches $2$, the denominator becomes very small while the numerator stays near $3$. A small denominator makes a fraction large in magnitude. From the right ($x > 2$), the denominator is positive, so the fraction goes to $+\infty$. From the left ($x < 2$), the denominator is negative, so the fraction goes to $-\infty$.

---

### Worked Example 2: Recognising a Hole

**Problem:** Analyze $f(x) = \dfrac{x^2 - 1}{x - 1}$ for vertical asymptotes and holes.

**Approach:** Factor the numerator and look for cancellation with the denominator.

**Step-by-step working:**
1. Factor the numerator: $x^2 - 1 = (x - 1)(x + 1)$.
2. The function becomes $f(x) = \dfrac{(x - 1)(x + 1)}{x - 1}$.
3. The factor $(x - 1)$ cancels, leaving $f(x) = x + 1$, but only for $x \neq 1$.
4. There is no vertical asymptote. Instead, there is a **hole** at $x = 1$. The hole's $y$-coordinate is found by plugging $x = 1$ into the simplified form: $y = 1 + 1 = 2$. The point $(1, 2)$ is missing from the graph.

**Common misconception:** Many students cancel the factor and then forget that the original function is still undefined at the cancelled value. The hole must be noted.

---

## 3. Horizontal Asymptotes

A **horizontal asymptote** is a horizontal line $y = L$ that the graph approaches as $x$ becomes very large (positive or negative). It describes the **end behavior** of the function.

To find the horizontal asymptote, compare the degree of the numerator $n$ with the degree of the denominator $m$:

- **If $n < m$:** The horizontal asymptote is $y = 0$. The denominator grows faster, pulling the fraction toward zero.
- **If $n = m$:** The horizontal asymptote is $y = \dfrac{\text{leading coefficient of } P}{\text{leading coefficient of } Q}$.
- **If $n > m$:** There is **no horizontal asymptote**. The function grows without bound. (It may instead have an oblique asymptote, discussed in the next section.)

### Worked Example 3

**Problem:** Find the horizontal asymptote of $f(x) = \dfrac{2x^2 + 1}{x^2 - 3}$.

**Approach:** Compare the degrees. Here $n = 2$ and $m = 2$, so they are equal. Divide the leading coefficients.

**Step-by-step working:**
1. The leading term of the numerator is $2x^2$. The leading term of the denominator is $x^2$.
2. As $x$ becomes very large, the $+1$ and $-3$ become negligible compared to the $x^2$ terms.
3. The function behaves like $\frac{2x^2}{x^2} = 2$.

The horizontal asymptote is $y = 2$.

**Why this makes sense:** For $x = 1000$, the numerator is approximately $2\,000\,001$ and the denominator is approximately $999\,997$. Their ratio is about $2.000004$, very close to $2$.

---

### Worked Example 4

**Problem:** Find the horizontal asymptote of $f(x) = \dfrac{3x}{x^2 + 1}$.

**Approach:** Here $n = 1$ and $m = 2$. Since $n < m$, the horizontal asymptote is $y = 0$.

**Why this makes sense:** The denominator grows quadratically ($x^2$) while the numerator grows only linearly ($x$). The denominator dominates, driving the fraction to zero as $x$ becomes very large.

---

## 4. Oblique (Slant) Asymptotes

When the degree of the numerator is exactly one more than the degree of the denominator ($n = m + 1$), the function does not have a horizontal asymptote. Instead, it has an **oblique asymptote** — a slanted line that the graph approaches as $x \to \pm\infty$.

To find the oblique asymptote, perform polynomial long division. The quotient (ignoring the remainder) is the equation of the oblique asymptote. As $x$ becomes very large, the remainder term approaches zero.

### Worked Example 5

**Problem:** Find the oblique asymptote of $f(x) = \dfrac{x^2 + 2x}{x - 1}$.

**Approach:** Divide $x^2 + 2x$ by $x - 1$ using polynomial long division.

**Step-by-step working:**
1. Divide $x^2$ by $x$ to get $x$. Multiply $(x - 1)$ by $x$ to get $x^2 - x$. Subtract from $x^2 + 2x$: $(x^2 + 2x) - (x^2 - x) = 3x$.
2. Divide $3x$ by $x$ to get $3$. Multiply $(x - 1)$ by $3$ to get $3x - 3$. Subtract: $3x - (3x - 3) = 3$.
3. So $f(x) = x + 3 + \dfrac{3}{x - 1}$.
4. As $x \to \pm\infty$, the fraction $\dfrac{3}{x - 1}$ approaches $0$.

The oblique asymptote is the line $y = x + 3$.

**Why this makes sense:** For very large $x$, the $+3$ remainder term becomes negligible, and the graph closely follows the line $y = x + 3$.

---

## 5. Full Analysis of a Rational Function

To fully analyze a rational function and sketch its graph, work through these steps in order:

1. **Factor** the numerator and denominator completely.
2. **Domain:** exclude values that make the denominator zero.
3. **Vertical asymptotes:** from uncancelled denominator factors.
4. **Holes:** from cancelled factors. Find the $y$-coordinate using the simplified form.
5. **Horizontal or oblique asymptote:** compare degrees.
6. **$x$-intercepts:** set the numerator equal to zero (after factoring).
7. **$y$-intercept:** evaluate $f(0)$, if $0$ is in the domain.
8. **Sign analysis:** test intervals between critical points to determine where the graph is positive or negative.

### Worked Example 6

**Problem:** Analyze the rational function $f(x) = \dfrac{x^2 - 4}{x^2 - 1}$.

**Approach:** Follow the eight steps above.

**Step-by-step working:**

1. **Factor:** $f(x) = \dfrac{(x - 2)(x + 2)}{(x - 1)(x + 1)}$.

2. **Domain:** The denominator is zero when $x = 1$ or $x = -1$. The domain is $\mathbb{R} \setminus \{-1, 1\}$.

3. **Vertical asymptotes:** Neither factor cancels with the numerator, so there are vertical asymptotes at $x = 1$ and $x = -1$.

4. **Holes:** None.

5. **Horizontal asymptote:** The degrees are $n = 2$ and $m = 2$, which are equal. The leading coefficients are $1$ and $1$, so the horizontal asymptote is $y = 1$.

6. **$x$-intercepts:** Set the numerator $(x - 2)(x + 2) = 0$, giving $x = 2$ and $x = -2$.

7. **$y$-intercept:** $f(0) = \dfrac{0 - 4}{0 - 1} = \dfrac{-4}{-1} = 4$.

8. **Sign analysis:** The critical points are $-2$, $-1$, $1$, and $2$. Test each interval by picking a sample $x$ value.

- $x < -2$ (e.g., $x = -3$): numerator $(-)(-) = (+)$, denominator $(-)(-) = (+)$, so $f(x) > 0$.
- $-2 < x < -1$ (e.g., $x = -1.5$): numerator $(+)(-) = (-)$, denominator $(-)(-) = (+)$, so $f(x) < 0$.
- $-1 < x < 1$ (e.g., $x = 0$): numerator $(+)(-) = (-)$, denominator $(-)(+) = (-)$, so $f(x) > 0$. (We already computed $f(0) = 4$.)
- $1 < x < 2$ (e.g., $x = 1.5$): numerator $(+)(-) = (-)$, denominator $(+)(+) = (+)$, so $f(x) < 0$.
- $x > 2$ (e.g., $x = 3$): numerator $(+)(+) = (+)$, denominator $(+)(+) = (+)$, so $f(x) > 0$.

The graph approaches $y = 1$ as $x \to \pm\infty$, shoots toward $\pm\infty$ near the vertical asymptotes, crosses the $x$-axis at $\pm 2$, and passes through the $y$-axis at $4$.

---

## 6. Rational Inequalities

To solve an inequality involving a rational function, find the critical points (where the numerator is zero or the denominator is zero). These points divide the number line into intervals. Test a sample point from each interval to determine the sign of the function on that interval.

### Worked Example 7

**Problem:** Solve the inequality $\dfrac{x + 2}{x - 3} > 0$.

**Approach:** Find critical points, mark them on a number line, and test each interval.

**Step-by-step working:**
1. Numerator zero: $x + 2 = 0$, giving $x = -2$.
2. Denominator zero: $x - 3 = 0$, giving $x = 3$.
3. These points divide the real line into three intervals: $x < -2$, $-2 < x < 3$, and $x > 3$.
4. Test $x = -3$ (first interval): $\frac{-3 + 2}{-3 - 3} = \frac{-1}{-6} = \frac{1}{6} > 0$. The interval $x < -2$ is part of the solution.
5. Test $x = 0$ (second interval): $\frac{0 + 2}{0 - 3} = \frac{2}{-3} = -\frac{2}{3} < 0$. The interval $-2 < x < 3$ is NOT part of the solution.
6. Test $x = 4$ (third interval): $\frac{4 + 2}{4 - 3} = \frac{6}{1} = 6 > 0$. The interval $x > 3$ is part of the solution.

The solution is $x < -2$ or $x > 3$. In interval notation: $(-\infty, -2) \cup (3, \infty)$.

**Common misconception:** Many students try to multiply both sides by $(x - 3)$, but this is dangerous because $(x - 3)$ could be negative, which would flip the inequality sign. The sign-table method avoids this problem entirely.

---

## Practice Problems

**1.** Find all asymptotes (vertical, horizontal, and oblique if any) of the function $f(x) = \dfrac{2x + 1}{x - 3}$.

**2.** For the function $f(x) = \dfrac{x}{x^2 - 4}$, state the domain, find all vertical asymptotes, and find the horizontal asymptote.

**3.** Find the oblique asymptote of $f(x) = \dfrac{2x^2 + x + 1}{x}$.

**4.** Solve the inequality $\dfrac{x - 1}{x + 2} \leq 0$.

**5.** (IB Exam Style) Consider the function $f(x) = \dfrac{x^2 - 1}{x^2 - 4}$.

(a) Factor the numerator and denominator fully. [1 mark]

(b) State the domain of $f$. [1 mark]

(c) Write the equations of all vertical and horizontal asymptotes. [2 marks]

(d) Find the coordinates of the $x$-intercepts and the $y$-intercept. [2 marks]

---

## Answers

**1.** The denominator $x - 3$ equals zero at $x = 3$, and the numerator $2(3) + 1 = 7 \neq 0$, so there is a vertical asymptote at $x = 3$. The degrees of numerator and denominator are both $1$, so the horizontal asymptote is $y = \frac{2}{1} = 2$. No oblique asymptote. A common mistake is to think the horizontal asymptote is $y = \frac{1}{-3}$, confusing coefficients with constants.

**2.** The denominator is $x^2 - 4 = (x - 2)(x + 2)$. The domain is all real numbers except $x = 2$ and $x = -2$. At both $x = 2$ and $x = -2$, the numerator is not zero (it is $2$ and $-2$ respectively), so there are vertical asymptotes at $x = 2$ and $x = -2$. The degree of the numerator ($1$) is less than the degree of the denominator ($2$), so the horizontal asymptote is $y = 0$. As $x$ grows without bound, the $x^2$ in the denominator dominates, pulling the fraction toward zero.

**3.** Divide: $\dfrac{2x^2 + x + 1}{x} = 2x + 1 + \dfrac{1}{x}$. As $x \to \pm\infty$, the term $\frac{1}{x}$ approaches $0$. The oblique asymptote is $y = 2x + 1$. This is a slanted line with slope $2$ and $y$-intercept $1$. Near $x = 0$, the function has a vertical asymptote because of the $\frac{1}{x}$ remainder term.

**4.** Critical points: numerator zero at $x = 1$, denominator zero at $x = -2$. Test intervals. For $x < -2$ (e.g., $x = -3$): $\frac{-4}{-1} = 4 > 0$, not part of solution. For $-2 < x < 1$ (e.g., $x = 0$): $\frac{-1}{2} = -\frac{1}{2} < 0$, part of solution. For $x > 1$ (e.g., $x = 2$): $\frac{1}{4} > 0$, not part of solution. At $x = 1$, the expression equals $0$, which satisfies $\leq 0$. At $x = -2$, the expression is undefined. The solution is $-2 < x \leq 1$. In interval notation: $(-2, 1]$.

**5.** (a) $f(x) = \dfrac{(x - 1)(x + 1)}{(x - 2)(x + 2)}$. [1 mark]

(b) The denominator is zero when $x = 2$ or $x = -2$. The domain is $\mathbb{R} \setminus \{-2, 2\}$. [1 mark]

(c) The vertical asymptotes are $x = 2$ and $x = -2$ (no factors cancel). The degrees are both $2$, and the leading coefficients are both $1$, so the horizontal asymptote is $y = 1$. [2 marks]

(d) The $x$-intercepts occur when the numerator is zero: $(x - 1)(x + 1) = 0$, giving $x = 1$ and $x = -1$. The coordinates are $(1, 0)$ and $(-1, 0)$. The $y$-intercept is $f(0) = \dfrac{0 - 1}{0 - 4} = \dfrac{-1}{-4} = \dfrac{1}{4}$, so the point is $\left(0, \frac{1}{4}\right)$. [2 marks]
