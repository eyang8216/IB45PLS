# Lesson 11: Linear Inequalities & Systems of Inequalities

## What You'll Learn
- Graphing single linear inequalities: boundary lines, shading, and test points
- Solving systems of linear inequalities: finding the overlapping region
- Solid vs. dashed boundary lines: when equality is included
- The critical inequality flip rule: multiplying/dividing by a negative
- Translating word problem constraints into systems of inequalities
- SAT-specific inequality traps and Desmos strategies

## SAT Context

Linear inequality questions appear 2-4 times per SAT, often as systems of inequalities from word problems. The SAT rarely asks you to solve a simple inequality like $3x - 5 > 10$ in isolation—instead, it presents real-world constraint problems ("a company must produce at least X units while spending no more than Y dollars") and asks which system of inequalities models the situation, or which point satisfies all constraints. The graph-based questions involve identifying the correct shaded region. For an AAHL student, inequality algebra is straightforward, but the SAT's unique contribution is the word-problem-to-system translation and the graphical interpretation.

## Single Linear Inequalities

### The Basics
A linear inequality in two variables looks like:
$$y > mx + b \quad \text{or} \quad y \leq mx + b$$

### Graphing Steps
1. **Graph the boundary line** $y = mx + b$.
   - Solid line: $\leq$ or $\geq$ (points ON the line are included).
   - Dashed line: $<$ or $>$ (points ON the line are NOT included).
2. **Shade the correct side.**
   - $y > mx + b$: shade ABOVE the line.
   - $y < mx + b$: shade BELOW the line.
3. **Test a point** (like $(0,0)$) if unsure. Plug it in: if true, shade the side containing that point.

### The "Greater = Above" Rule
Memorize: $y >$ ... means shade **above** the line. $y <$ ... means shade **below**.

For inequalities NOT in $y =$ form (e.g., $2x + 3y < 6$), rearrange to $y$ form first, or test a point.

> **🚨 SAT TRAP ALERT: The Negative Multiplication/Division Flip.** When you multiply or divide both sides of an inequality by a **negative** number, you must **flip** the inequality sign.
>
> $$-2x > 6 \quad \Rightarrow \quad x < -3$$
>
> The SAT loves to put the "unflipped" answer among the choices. If you solve $-3x + 5 \leq 14$ and get $x \leq -3$ (which is wrong—should be $x \geq -3$), that wrong answer will be option A or B.
>
> **How to avoid:** When you see a negative coefficient on $x$, pause and consciously flip. Better yet, avoid dividing by negatives when possible: $5 - 2x > 11$ → subtract 5: $-2x > 6$ → divide by $-2$: $x < -3$. Or add $2x$ to both sides: $5 > 11 + 2x$ → $-6 > 2x$ → $-3 > x$, same result.

## Systems of Linear Inequalities

### What They Are
Multiple inequalities that must ALL be satisfied simultaneously. The solution is the **intersection** (overlap) of all shaded regions.

### Solution Steps
1. Graph each inequality separately (dashed/solid, shade above/below).
2. The solution region is where ALL shading overlaps.
3. Test a point in the overlap region to verify.

### Desmos Approach
Type each inequality into Desmos exactly as written. Desmos automatically uses solid/dashed lines and shading. The overlapping region is your solution. To check if a specific point is a solution, type it as a coordinate and see if it falls in the overlapping region.

### SAT Question Types

**Type 1: "Which point is a solution to the system?"**
Test each answer choice in all inequalities. The one that satisfies ALL of them is the answer.

**Type 2: "Which system of inequalities describes the shaded region?"**
Match the boundary lines and shading direction to the answer choices.

**Type 3: "Which graph represents the solution?"**
Identify slope, intercept, solid/dashed, and shading direction.

> **🔍 PATTERN RECOGNITION: Word problems with "at least," "at most," "no more than," "minimum," "maximum."** These keywords tell you which inequality sign to use:
> - "at least $k$" → $\geq k$
> - "at most $k$" / "no more than $k$" → $\leq k$
> - "more than $k$" → $> k$
> - "less than $k$" / "fewer than $k$" → $< k$
> - "minimum of $k$" → $\geq k$
> - "maximum of $k$" → $\leq k$
>
> When the SAT says "a company must produce at least 100 units and spend no more than $5,000," you immediately write: $x \geq 100$ and $\text{cost} \leq 5000$.

### Worked Example 1: Graphing a Single Inequality

**Problem:** Which of the following is the graph of $y \geq 2x - 3$?

A) Dashed line $y = 2x - 3$, shaded above
B) Dashed line $y = 2x - 3$, shaded below
C) Solid line $y = 2x - 3$, shaded above
D) Solid line $y = 2x - 3$, shaded below

**Solution:**
- $\geq$ means solid line (includes the boundary).
- $y \geq$ ... means shade above (greater y-values).
- So: solid line, shade above.

**Answer: C.**

**Wrong answer analysis:**
- A: wrong line type (dashed instead of solid).
- B: wrong line type AND wrong shading direction.
- D: wrong shading direction.

### Worked Example 2: System of Inequalities from a Word Problem

**Problem:** A baker makes cakes ($c$) and pies ($p$). Each cake requires 2 hours of labor, and each pie requires 1 hour of labor. The baker has at most 40 hours available. The baker must make at least 10 cakes and at least 5 pies. Which system models these constraints?

A) $2c + p \leq 40$, $c \geq 10$, $p \geq 5$
B) $2c + p \geq 40$, $c \leq 10$, $p \leq 5$
C) $c + 2p \leq 40$, $c \geq 10$, $p \geq 5$
D) $2c + p \leq 40$, $c \leq 10$, $p \leq 5$

**Solution:**
1. Labor constraint: $2c + 1p$ (hours) must be "at most" 40 → $2c + p \leq 40$.
2. "At least 10 cakes" → $c \geq 10$.
3. "At least 5 pies" → $p \geq 5$.

**Answer: A.**

**Wrong answer analysis:**
- B: Wrong inequality directions (swapped $\leq$ and $\geq$).
- C: Wrong coefficients ($c + 2p$ instead of $2c + p$—confused which gets 2 hours).
- D: "At least" constraints written as $\leq$ instead of $\geq$.

### Worked Example 3: Testing Points

**Problem:** Which point satisfies the system: $y > x + 1$ and $y \leq -2x + 5$?

A) $(0, 2)$
B) $(2, 4)$
C) $(2, 1)$
D) $(1, 0)$

**Solution:**
Test each point:

- A $(0, 2)$: $2 > 0 + 1 = 1$ ✓. $2 \leq -2(0) + 5 = 5$ ✓. **Satisfies both!**
- B $(2, 4)$: $4 > 2 + 1 = 3$ ✓. $4 \leq -2(2) + 5 = 1$? $4 \leq 1$ ✗.
- C $(2, 1)$: $1 > 2 + 1 = 3$? $1 > 3$ ✗.
- D $(1, 0)$: $0 > 1 + 1 = 2$? $0 > 2$ ✗.

**Answer: A.**

---

## Practice Problems

1. Solve: $-4x + 7 < 23$. Which is correct?
   A) $x > -4$
   B) $x < -4$
   C) $x > 4$
   D) $x < 4$

2. Which inequality corresponds to the description: "y is at most twice x decreased by 5"?
   A) $y \geq 2x - 5$
   B) $y \leq 2x - 5$
   C) $y > 2x - 5$
   D) $y = 2x - 5$

3. A system of inequalities is graphed with the overlapping region in the first quadrant. The boundary lines are $y = -x + 6$ (solid, shaded below) and $y = \frac{1}{2}x$ (dashed, shaded above). Which point is a solution?
   A) $(4, 3)$
   B) $(2, 2)$
   C) $(8, 2)$
   D) $(4, 1)$

4. A student has at most 3 hours (180 minutes) to study for math and science. She wants to spend at least twice as much time on math ($m$) as on science ($s$). Which system models this?
   A) $m + s \leq 180$, $m \geq 2s$
   B) $m + s \geq 180$, $m \leq 2s$
   C) $2m + s \leq 180$, $m \geq s$
   D) $m + s \leq 180$, $2m \leq s$

5. The solution to $y \geq x + 2$ and $y \leq -x + 6$ is a region bounded by two lines. What is the area of this region if it's a triangle formed with the y-axis?
   A) 4
   B) 6
   C) 8
   D) 12

6. **(Challenge)** A company produces two products, A and B. Product A requires 3 hours of machine time and 2 hours of labor. Product B requires 1 hour of machine time and 4 hours of labor. The company has at most 120 machine hours and 160 labor hours available. If $a$ and $b$ represent the number of units produced, which system models the constraints?
   A) $3a + b \leq 120$, $2a + 4b \leq 160$, $a \geq 0$, $b \geq 0$
   B) $3a + b \geq 120$, $2a + 4b \geq 160$
   C) $a + 3b \leq 120$, $4a + 2b \leq 160$
   D) $3a + b \leq 120$, $2a + 4b \leq 160$

---

## Answers

1. **Answer: A.** $-4x + 7 < 23$ → $-4x < 16$ → divide by $-4$ and **flip**: $x > -4$. **Wrong answers:** B is the "unflipped" trap ($x < -4$). C: $x > 4$ comes from $x < -\frac{16}{4}$ and flipping but with wrong arithmetic. D: $x < 4$, multiple errors.

2. **Answer: B.** "At most" = $\leq$. "Twice x decreased by 5" = $2x - 5$. So $y \leq 2x - 5$. **Wrong answers:** A uses $\geq$ (at least). C uses $>$ (strictly more than). D uses $=$ (exactly), not an inequality.

3. **Answer: A.** Test $(4, 3)$: $3 \leq -4 + 6 = 2$? $3 \leq 2$ ✗. Wait—that fails. Let me retest carefully. The question says $y = -x + 6$ with shading BELOW, and $y = \frac{1}{2}x$ dashed, shaded ABOVE.

   Test $(4, 3)$: For $y \leq -x + 6$: $3 \leq -4 + 6 = 2$ → $3 \leq 2$ ✗. So A fails.

   Let me pick a better answer. The region: below $y = -x + 6$ and above $y = \frac{1}{2}x$. In the first quadrant. The intersection of the lines: $-x + 6 = \frac{1}{2}x$ → $6 = 1.5x$ → $x = 4$, $y = 2$.

   Test $(2, 2)$: $2 \leq -2 + 6 = 4$ ✓. $2 > \frac{1}{2}(2) = 1$ ✓.

   **Answer: B.**

   **Wrong answers:** A $(4,3)$ fails the first inequality. C $(8,2)$: $2 \leq -8 + 6 = -2$ ✗. D $(4,1)$: $1 \leq -4 + 6 = 2$ ✓, $1 > \frac{1}{2}(4) = 2$ ✗.

4. **Answer: A.** At most 180 minutes: $m + s \leq 180$. "At least twice as much on math" → $m \geq 2s$. **Wrong answers:** B has $\geq$ 180 (at least—opposite) and $m \leq 2s$ (wrong direction). C has wrong coefficient. D has $2m \leq s$ (math is at most half of science—backward).

5. **Answer: C.** The region bounded by $y \geq x + 2$, $y \leq -x + 6$, and the y-axis ($x \geq 0$). The triangle vertices: (1) Intersection of $y = x + 2$ and $y = -x + 6$ → $x + 2 = -x + 6$ → $2x = 4$ → $x = 2, y = 4$. (2) Intersection of $y = x + 2$ and y-axis ($x = 0$) → $(0, 2)$. (3) Intersection of $y = -x + 6$ and y-axis → $(0, 6)$.

   Triangle: vertices $(0,2)$, $(0,6)$, $(2,4)$. Base on y-axis: length $6 - 2 = 4$. Height: $2$ (horizontal distance to $x=2$). Area: $\frac{1}{2} \times 4 \times 2 = 4$. Wait, that gives 4.

   Hmm, let me re-examine. The question says "bounded by two lines" and "formed with the y-axis." So we're looking at $x \geq 0$ as an additional constraint. The region satisfies: $y \geq x+2$, $y \leq -x+6$, $x \geq 0$. The triangle vertices: $(0,2)$, $(0,6)$, $(2,4)$. Base = 4, height = 2, area = 4.

   **Answer: A, 4.**

   **Wrong answers:** B (6): $\frac{1}{2} \times 4 \times 3 = 6$, using wrong height. C (8): $\frac{1}{2} \times 4 \times 4 = 8$, using wrong height. D (12): $4 \times 3 = 12$ (rectangle, not triangle).

6. **Answer: A.** Machine time: $3a + 1b \leq 120$. Labor: $2a + 4b \leq 160$. Non-negativity: $a \geq 0$, $b \geq 0$. **Wrong answers:** B has wrong inequality direction ($\geq$ instead of $\leq$). C scrambles the coefficients. D is almost correct but missing $a \geq 0, b \geq 0$ (which is technically part of the model, but on the SAT this is often implied). Actually, D matches A without the non-negativity constraints. On the SAT, answer choices usually imply non-negativity for production quantities. Let me make D clearly different: D: $a + 3b \leq 120$, $4a + 2b \leq 160$ (scrambled coefficients).

Let me fix the answer choices to make A uniquely correct by removing non-negativity from A and putting them all as implied, and making D different:

A) $3a + b \leq 120$, $2a + 4b \leq 160$
B) $3a + b \geq 120$, $2a + 4b \geq 160$
C) $a + 3b \leq 120$, $4a + 2b \leq 160$
D) $3a + b \leq 120$, $4a + 2b \leq 160$

With these, A is correct. D scrambles the labor coefficients.
