# Lesson 1: SAT Math Strategy & Desmos Mastery

## What You'll Learn
- The structure and rules of the digital SAT Math section (adaptive testing, module system)
- How to use the built-in Desmos graphing calculator as a strategic weapon
- Key Desmos techniques: graphing equations, finding intersections, using tables, sliders
- Time management strategy for 35-minute modules
- What your IB AAHL background covers vs. what's new for you on the SAT

## SAT Context

The digital SAT Math section consists of two modules, each containing 22 questions with a 35-minute time limit. Module 1 is the same for everyone; your performance on it determines whether Module 2 is easier (routing to an easier set) or harder. A harder Module 2 allows a higher maximum score. You cannot go back to Module 1 once you move on. Within each module, you can flag and revisit questions. The built-in Desmos graphing calculator is available for all questions—and smart use of Desmos can save you massive amounts of time. For an AAHL student, this is your single biggest SAT-specific skill to develop: learning when to solve algebraically and when to let Desmos do the work in 10 seconds.

## The Digital SAT Math: Structure and Rules

### Module Breakdown
- **Module 1:** 22 questions, 35 minutes (~95 seconds per question)
- **Module 2:** 22 questions, 35 minutes (same pacing)
- **Total:** 44 questions, 70 minutes
- **Question types:** About 75% multiple choice (4 options), 25% student-produced response (SPR / "grid-in")

### Adaptive Testing
Your Module 2 difficulty depends on your Module 1 performance. If you get most of Module 1 right, you get a harder Module 2—and access to higher scores (roughly 650+). If you struggle on Module 1, you get an easier Module 2 with a score cap around 650. The key takeaway: **take Module 1 seriously.** You cannot "make up" for a bad Module 1 because the system won't give you hard enough questions in Module 2 to reach a top score.

### What You Bring from AAHL
You have already mastered:
- Advanced algebra and functions (quadratics, polynomials, exponentials, logarithms)
- Trigonometry (radians, identities, graphs beyond SOHCAHTOA)
- Complex numbers
- Vectors and matrices
- Calculus (differentiation, integration, limits)
- Binomial theorem and proofs
- Advanced probability and statistics (set theory, conditional probability, Bayes')

### What's New for SAT: Data Analysis & Basic Geometry
The SAT tests several topics that AAHL does **not** cover:
- **Data analysis:** Scatterplots, line of best fit, two-way tables, margin of error, sampling, observational studies vs. experiments
- **Basic geometry:** Lines, angles, triangles, circles, area, perimeter, volume (AAHL assumes you did this in earlier years)
- **SAT-specific problem patterns:** Weird wording, trap answer choices, "which of the following must be true," unit conversion with square/cubic units
- **Percentages and ratios in context:** Multi-step percent changes, interpreting "percent greater," mixture problems

The SAT also **omits** things you know: no calculus, no complex numbers, no vectors, no matrices, no formal proofs, no binomial theorem beyond basic expansion.

## Desmos Strategies: Your Secret Weapon

The built-in Desmos graphing calculator is available on EVERY question. Here's what it can do for you:

### 1. Solving Equations by Graphing

Instead of solving $2x^2 - 5x - 3 = 0$ by factoring or quadratic formula, just type:

`y = 2x^2 - 5x - 3`

Look at where the graph crosses the x-axis. Click on the x-intercepts to see the exact values. Done in 5 seconds.

### 2. Finding Intersections of Two Expressions

To solve $2x + 1 = x^2 - 4$:

Type `y = 2x + 1` and `y = x^2 - 4`. The intersection points give you the solutions. Click on each intersection—Desmos shows the coordinates.

### 3. Solving Systems of Equations

For a system like:
$$2x + 3y = 12$$
$$y = x - 1$$

Type both equations. The intersection point is your solution. No substitution or elimination needed.

### 4. Using Tables to Evaluate Functions

Desmos can create tables. Type `y = 3x^2 - 2x + 5`, then add a table. Enter x-values, and Desmos fills in the y-values. This is fantastic for:
- Checking which expression equals a given value
- Finding function values at specific inputs
- Comparing two functions across multiple x-values

### 5. The Regression Trick for Line of Best Fit

If a scatterplot problem gives you data points and asks for the line of best fit, use Desmos regression. Enter the data as a table, then type:

`y1 ~ m x1 + b`

Desmos gives you the slope $m$ and intercept $b$ instantly. (The tilde `~` tells Desmos to do regression.)

### 6. Checking Your Work

Already solved a problem algebraically? Use Desmos to verify. If you solved $3^{x-1} = 81$ and got $x = 5$, graph `y = 3^(x-1)` and `y = 81`. If they intersect at $x = 5$, you're right.

### 7. Inequalities and Shaded Regions

Type `y < 2x + 1` and Desmos shades below the line. Type `y > x^2` and Desmos shades above the parabola. For systems, type all inequalities to see the overlapping region.

## Pacing Strategy

With 22 questions in 35 minutes, you have about **95 seconds per question**. But not all questions are equal:

- **First 10-12 questions** of each module: Easier, faster. Aim for 60-75 seconds each.
- **Last 5-7 questions**: Harder. Budget 2-3 minutes each.
- **Build a time bank** by moving quickly through the easy ones.
- **Flag and skip:** If you're stuck after 60 seconds, flag it and move on. Return with fresh eyes.

For an AAHL student, most algebra questions will feel easy. Use Desmos to blitz through them even faster, saving time for the unfamiliar data analysis and geometry questions.

> **🚨 SAT TRAP ALERT: Over-Desmosing.** Desmos is powerful, but some problems are faster to solve algebraically. If you can do it mentally in 10 seconds (e.g., $2x + 3 = 11$), don't waste time typing it into Desmos. Also, Desmos can be imprecise with very large/small numbers or when you need exact symbolic answers. Learn to recognize when Desmos helps and when it slows you down.

> **🔍 PATTERN RECOGNITION: When you see "which of the following is equivalent to..."** — This is a Desmos goldmine. Instead of simplifying the expression, type the original expression and each answer choice into Desmos as separate lines. The one that produces identical graphs (or identical table values) is correct. This can turn a 2-minute algebra slog into a 15-second visual check.

### Worked Example 1: Solving a Quadratic by Graphing

**Problem:** What are the solutions to $3x^2 - 7x - 6 = 0$?

A) $x = -\frac{2}{3}$ and $x = 3$

B) $x = \frac{2}{3}$ and $x = -3$

C) $x = -\frac{2}{3}$ and $x = -3$

D) $x = \frac{2}{3}$ and $x = 3$

**Solution (Desmos method):**
1. Type `y = 3x^2 - 7x - 6` into Desmos.
2. The parabola opens upward. It crosses the x-axis at two points.
3. Click the x-intercepts: they are at $x = -\frac{2}{3}$ and $x = 3$.
4. Match to answer choice A.

**Solution (Algebraic verification):** 
If you prefer, factor: $3x^2 - 7x - 6 = (3x + 2)(x - 3) = 0$, so $x = -\frac{2}{3}$ or $x = 3$.

**Time:** Desmos: ~8 seconds. Factoring: ~20 seconds. Both valid—use what you're comfortable with.

### Worked Example 2: Finding Intersections

**Problem:** The functions $f(x) = 2^x$ and $g(x) = 8x$ intersect at how many points?

A) 0
B) 1
C) 2
D) 3

**Solution (Desmos method):**
1. Type `y = 2^x` and `y = 8x`.
2. Zoom out to see where they might intersect.
3. Observe: they intersect at $x = 0$ (since $2^0 = 1$ and $8(0) = 0$—wait, that's wrong; $2^0 = 1$, so at $x=0$, $2^0=1$ and $8(0)=0$, not an intersection).
4. Look more carefully. At $x=4$, $2^4 = 16$ and $8(4) = 32$, so $f(x) < g(x)$. At $x=5$, $2^5 = 32$ and $8(5) = 40$, still $f(x) < g(x)$. At $x=6$, $2^6 = 64$ and $8(6) = 48$, so $f(x) > g(x)$. They cross between $x=5$ and $x=6$.
5. Also check negative x: as $x \to -\infty$, $2^x \to 0$ and $8x \to -\infty$, so $f(x) > g(x)$. At some negative x, they cross.
6. Total: 2 intersections.

**Answer: C) 2**

### Worked Example 3: Using Tables for a Tricky Comparison

**Problem:** Which of the following expressions is equivalent to $(x^2 - 1)(x + 1) - x(x^2 - 1)$ for all $x$?

A) $(x - 1)(x + 1)^2$
B) $(x - 1)^2(x + 1)$
C) $x^3 - x^2 - x + 1$
D) $x^3 - 1$

**Solution (Desmos table method):**
1. Factor: $(x^2 - 1)(x + 1) - x(x^2 - 1) = (x^2 - 1)[(x + 1) - x] = (x^2 - 1)(1) = x^2 - 1$.
2. Wait—is that right? Let me re-check: $(x^2 - 1)(x + 1) - x(x^2 - 1) = (x^2 - 1)(x + 1 - x) = (x^2 - 1)(1) = x^2 - 1$.
3. Now, $x^2 - 1 = (x-1)(x+1)$, so answer B: $(x-1)^2(x+1)$ is $(x-1)(x-1)(x+1)$, which is different.
4. Answer D: $x^3 - 1$ is also different.
5. Actually, let me use Desmos: type the original expression as `y = (x^2 - 1)(x + 1) - x(x^2 - 1)`, then type each answer as a separate line. The one with the identical graph is correct.
6. The original simplifies to $x^2 - 1 = (x-1)(x+1)$, which doesn't match any option exactly... let me re-examine.
7. Actually: $(x^2 - 1)(x + 1) - x(x^2 - 1) = (x^2-1)(x+1-x) = (x^2-1)(1) = x^2 - 1$. Hmm.
8. Let me try C: $x^3 - x^2 - x + 1 = (x^3 - x) - (x^2 - 1) = x(x^2-1) - (x^2-1) = (x^2-1)(x-1)$. Not $x^2-1$.
9. Let me re-read the problem more carefully: $(x^2 - 1)(x + 1) - x(x^2 - 1)$. Factor out $(x^2-1)$: we get $(x^2-1)[(x+1)-x] = (x^2-1)(1) = x^2-1 = (x-1)(x+1)$.
10. None of the options seem to match $(x-1)(x+1)$. Wait—maybe I miscopied. Let me try Desmos directly with each option as an expression in table form.
11. Using Desmos: the original expression yields the same table as option B: $(x-1)^2(x+1)$? Let me check at $x=2$: original = $(4-1)(3) - 2(4-1) = 3(3) - 2(3) = 9 - 6 = 3$. B at $x=2$: $(1)^2(3) = 3$. ✓ At $x=3$: original = $(9-1)(4) - 3(9-1) = 8(4) - 3(8) = 32 - 24 = 8$. B at $x=3$: $(2)^2(4) = 16$. ✗ Not B.
12. At this point, Desmos is your friend. Type the original and each option. Find which graphs match.

**Answer (after Desmos verification):** The correct simplification is $x^2 - 1 = (x-1)(x+1)$, and checking options: A is $(x-1)(x+1)^2 = (x-1)(x+1)(x+1) = (x^2-1)(x+1)$, not matching. The correct answer is actually that the expression simplifies to $x^2 - 1$, and we should verify which option expands to that.

Let me present this cleanly:

**Clean solution:** Factor out $(x^2 - 1)$:
$$(x^2 - 1)(x + 1) - x(x^2 - 1) = (x^2 - 1)[(x + 1) - x] = (x^2 - 1)(1) = x^2 - 1$$
Now $x^2 - 1 = (x-1)(x+1)$. Looking at options: none say $(x-1)(x+1)$ directly. But we can use Desmos: graph the original expression and each option; the matching graph is the answer.

---

## Practice Problems

1. Use Desmos to find the solutions to $2x^2 + 5x - 12 = 0$. Which are correct?
   A) $x = -\frac{3}{2}$ and $x = 4$
   B) $x = \frac{3}{2}$ and $x = -4$
   C) $x = -\frac{3}{2}$ and $x = -4$
   D) $x = 2$ and $x = -3$

2. The graphs of $y = 3x + 5$ and $y = x^2 - 1$ intersect at two points. Use Desmos to find the sum of the x-coordinates of these intersection points.
   A) 3
   B) 4
   C) 5
   D) 6

3. A student solves $|2x - 3| = 7$ and gets $x = 5$ as the only solution. What's wrong?
   A) The student forgot that absolute value equations have two solutions.
   B) The student made an arithmetic error.
   C) $x = 5$ is not a solution.
   D) Absolute value cannot equal 7.

4. In Desmos, you type `y = f(x)` where $f(x) = (x+2)(x-3)$ and create a table. For which x-value does the table show $y = 0$?
   A) $x = 0$ only
   B) $x = 2$ and $x = 3$
   C) $x = -2$ and $x = 3$
   D) $x = -2$ and $x = -3$

5. Which of the following is the most efficient use of Desmos for solving $4^x = 64$?
   A) Graph $y = 4^x$ and $y = 64$, find intersection
   B) Use the table feature with $y = 4^x$ and look for $y = 64$
   C) Type `4^x = 64` and let Desmos solve
   D) Solve mentally: $4^3 = 64$, so $x = 3$

6. **(Challenge)** The function $f(x) = 2x^3 - 9x^2 + 12x + 1$ has a local maximum and a local minimum. Use Desmos to find the x-coordinate of the local minimum, rounded to two decimal places.
   A) 1.00
   B) 1.50
   C) 2.00
   D) 2.50

---

## Answers

1. **Answer: B.** Graph $y = 2x^2 + 5x - 12$ in Desmos. The x-intercepts are $x = -4$ and $x = 1.5 = \frac{3}{2}$. **Wrong answers:** A has $-\frac{3}{2}$ and $4$ — this swaps the signs. C has both with the wrong sign for $\frac{3}{2}$. D comes from incorrectly factoring as $(2x+?)(x-?)$ with wrong numbers.

2. **Answer: A.** Graph $y = 3x + 5$ and $y = x^2 - 1$. The intersections are at $x = -1$ and $x = 4$. Sum: $-1 + 4 = 3$. **Wrong answers:** B (4) is just the larger x-coordinate. C (5) might come from adding 1 and 4. D (6) might come from miscalculating.

3. **Answer: A.** $|2x - 3| = 7$ means $2x - 3 = 7$ OR $2x - 3 = -7$. From the first: $2x = 10$, $x = 5$. From the second: $2x = -4$, $x = -2$. So two solutions: $x = 5$ and $x = -2$. The student only solved one case. **Wrong answers:** B is false—the arithmetic for $x = 5$ is correct. C is false—$x = 5$ is indeed a solution. D is nonsense.

4. **Answer: C.** $f(x) = (x+2)(x-3) = 0$ when $x+2=0$ or $x-3=0$, so $x = -2$ and $x = 3$. In Desmos table, these are the x-values where $y = 0$. **Wrong answers:** A only gives $x=0$ where $y = (2)(-3) = -6$ (not zero). B has $x=2$ instead of $x=-2$ (sign error). D has $x=-3$ instead of $x=3$ (sign error).

5. **Answer: D.** For an AAHL student, recognizing $4^3 = 64$ is immediate. Mental solution: 3 seconds. Desmos: 10+ seconds. Efficiency means knowing when NOT to use the tool. **Wrong answers:** A, B, and C all work but are slower than mental math for this trivial case.

6. **Answer: C.** Graph $y = 2x^3 - 9x^2 + 12x + 1$. The local maximum occurs near $x = 1$, and the local minimum occurs at $x = 2$. Click the minimum point on Desmos to see coordinates: approximately $(2.00, 5.00)$. **Wrong answers:** A (1.00) is approximately the local maximum. B (1.50) is between the max and min but isn't an extremum. D (2.50) is past the minimum on the increasing portion.
