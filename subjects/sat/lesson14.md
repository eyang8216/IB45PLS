# Lesson 14: Function Notation & Graph Interpretation (SAT Style)

## What You'll Learn
- How to read and evaluate $f(x)$ notation in every SAT context
- Navigating composite functions: $f(g(x))$, $g(f(x))$, and nested evaluation
- Interpreting graphs: domain, range, intercepts, zeros, maximum, minimum
- How transformations affect function graphs — especially the left/right shift trap
- Translating between algebraic expressions and their graphical meaning
- How to answer "for what value of $x$ does $f(x) = \ldots$" efficiently

## SAT Context
Function notation is the language of the SAT Math section. Approximately **10–12 questions** across both modules involve interpreting function notation, reading graphs, or understanding transformations. The SAT tests whether you can move fluidly between the algebraic and graphical representations of a function. Many questions don't require heavy computation — they require you to **understand what the notation is asking**. A common pattern: the question gives you a graph of $y = f(x)$ and asks for a specific input or output value. Your IB AAHL experience with functions provides deep conceptual understanding; this lesson bridges that understanding to the specific question types and traps the SAT employs.

---

## Evaluating $f(x)$: The Basics

$f(x)$ means "the output of function $f$ when the input is $x$." The SAT tests this in several ways:

### Direct Evaluation
If $f(x) = 2x^2 - 3x + 1$, find $f(4)$:
$$f(4) = 2(4)^2 - 3(4) + 1 = 2(16) - 12 + 1 = 32 - 12 + 1 = 21$$

### "For what value of $x$ does $f(x) = k$?"
This means: find the **input** $x$ that produces output $k$. Set up and solve: $f(x) = k$.

> **🔍 PATTERN RECOGNITION:** When the SAT says "find $x$ such that $f(x) = 7$," they are asking you to solve an equation. When they say "find $f(7)$," they are asking you to plug in 7. These are opposite operations. Many students rush and do the wrong one.

### Worked Example 1: Input vs. Output

**Problem:** If $f(x) = 3x - 5$, what is the value of $x$ for which $f(x) = 16$?

**Solution:** Set $f(x) = 16$:
$$3x - 5 = 16$$
$$3x = 21$$
$$x = 7$$

**Contrast:** If the question asked for $f(16)$, it would be $f(16) = 3(16) - 5 = 43$. Same numbers, completely different answer.

---

## Composite Functions

The notation $f(g(x))$ means: apply $g$ to $x$ first, then apply $f$ to that result.

> **🚨 SAT TRAP ALERT:** $f(g(x))$ and $g(f(x))$ are generally NOT the same. The order matters. Read carefully which function is on the outside (applied second).

### Worked Example 2: Composite Function Evaluation

**Problem:** If $f(x) = x^2 + 1$ and $g(x) = 2x - 3$, find $f(g(4))$.

**Solution:** Work inside out.
$$g(4) = 2(4) - 3 = 8 - 3 = 5$$
$$f(g(4)) = f(5) = 5^2 + 1 = 25 + 1 = 26$$

If instead we computed $g(f(4))$:
$$f(4) = 4^2 + 1 = 16 + 1 = 17$$
$$g(f(4)) = g(17) = 2(17) - 3 = 34 - 3 = 31$$

Different answers — $26 \neq 31$ — confirming that order matters.

---

## Reading Graphs: Domain and Range

### Domain
The set of all possible $x$-values (inputs) for which the function is defined. On a graph, look left and right.

- **Discrete points:** Domain is the set of $x$-coordinates of those points
- **Continuous curve:** Domain is the interval from the leftmost to rightmost $x$-value
- **Algebraic restrictions:** Denominators $\neq 0$, radicands $\geq 0$

### Range
The set of all possible $y$-values (outputs) the function produces. On a graph, look down and up.

> **🔍 PATTERN RECOGNITION:** SAT questions about domain and range often pair with inequality notation. If a graph extends infinitely in one direction, the answer uses $\infty$ or $-\infty$. The SAT prefers interval notation or inequality notation depending on the answer choices.

### Worked Example 3: Graph Reading

**Problem:** The graph of $y = f(x)$ is a parabola opening upward with vertex at $(2, -3)$ and extending infinitely in both directions. What are the domain and range?

**Solution:**
- **Domain:** The parabola extends left and right without bound → all real numbers, or $(-\infty, \infty)$
- **Range:** The lowest $y$-value is $-3$ (at the vertex), and the parabola goes up forever → $[-3, \infty)$

---

## Zeros, Intercepts, and Key Features

| Feature | Meaning on Graph | How to Find |
|:---|:---|:---|
| $x$-intercept / zero / root | Graph crosses $x$-axis ($y=0$) | Solve $f(x)=0$ |
| $y$-intercept | Graph crosses $y$-axis ($x=0$) | Evaluate $f(0)$ |
| Maximum | Highest $y$-value on the graph | Look for peak; may be absolute or local |
| Minimum | Lowest $y$-value on the graph | Look for valley; may be absolute or local |
| Increasing interval | Graph goes up as $x$ moves right | $f'(x) > 0$ (or visual inspection on SAT) |
| Decreasing interval | Graph goes down as $x$ moves right | $f'(x) < 0$ (or visual inspection) |

> **🚨 SAT TRAP ALERT:** The question "how many times does the graph intersect the $x$-axis?" is NOT the same as "what are the $x$-intercepts?" The first asks for a count; the second asks for values. Read every word.

---

## Function Transformations (The SAT's Favorite Trap)

For a function $f(x)$:

| Transformation | Effect on Graph |
|:---|:---|
| $f(x) + k$ | Shift UP by $k$ units |
| $f(x) - k$ | Shift DOWN by $k$ units |
| $f(x + h)$ | Shift **LEFT** by $h$ units |
| $f(x - h)$ | Shift **RIGHT** by $h$ units |
| $-f(x)$ | Reflect across $x$-axis |
| $f(-x)$ | Reflect across $y$-axis |
| $a \cdot f(x)$ where $a > 1$ | Vertical stretch |
| $a \cdot f(x)$ where $0 < a < 1$ | Vertical compression |

> **🚨 SAT TRAP ALERT (CRITICAL):** $f(x+2)$ shifts the graph **LEFT** by 2 units, not right. This feels backwards because "$+2$" intuitively suggests moving in the positive (right) direction. The reason: to produce the same output, $x$ must be 2 units smaller. For example, $f(x+2)$ at $x = 3$ gives $f(5)$ — the graph of $f$ at input 5 now appears at $x = 3$, which is left of 5. The SAT will include the wrong-direction answer as a distractor nearly every time.

### Worked Example 4: Transformation Trap

**Problem:** The graph of $y = f(x)$ is shown with a vertex at $(3, 5)$. What are the coordinates of the vertex of $y = f(x+4) - 2$?

**Solution:**
- $f(x+4)$ shifts the graph **left** by 4: the vertex moves from $(3, 5)$ to $(-1, 5)$
- $-2$ shifts the graph **down** by 2: $(-1, 5) \to (-1, 3)$

**Answer:** $(-1, 3)$

**Common wrong answers:**
- $(7, 3)$ — shifted **right** by 4 instead of left
- $(3, 7)$ — shifted up instead of down, and ignored horizontal shift
- $(7, 7)$ — both transformations backwards

---

## Interpreting Graphs in Context

Many SAT graphs represent real-world situations. Key skills:

### Slope as Rate of Change
In a linear graph, the slope tells you the rate: dollars per hour, meters per second, students per year.

### Meaning of Intercepts
- $y$-intercept: the starting value (at $x = 0$, at time zero, with zero items, etc.)
- $x$-intercept: when the quantity reaches zero (break-even point, depletion time, etc.)

### Worked Example 5: Contextual Graph

**Problem:** The graph shows the height $h(t)$ of a ball in feet, $t$ seconds after being thrown. The graph is a parabola with a maximum at $(2, 64)$ and $x$-intercepts at $(0, 0)$ and $(4, 0)$. What does $h(2) = 64$ mean in context?

**Solution:** $h(2) = 64$ means that 2 seconds after the ball is thrown, its height is 64 feet. This is the maximum height.

**Follow-up:** What does the $x$-intercept at $(4, 0)$ mean? The ball hits the ground 4 seconds after being thrown.

---

## "How Many Solutions?" Questions from Graphs

When the SAT asks "how many solutions does $f(x) = g(x)$ have?", it's asking: **how many intersection points do the graphs of $f$ and $g$ have?**

> **🔍 PATTERN RECOGNITION:** The equation $f(x) = g(x)$ can be rewritten as $f(x) - g(x) = 0$, or $h(x) = 0$. The number of solutions equals the number of $x$-intercepts of $h(x)$, which equals the number of intersection points of $f$ and $g$. On the SAT, you can often count intersections directly from the graph without solving algebraically.

---

## Practice Problems

### Problem 1
The graph of $y = f(x)$ passes through the points $(1, 4)$ and $(3, 10)$. What is the value of $f(f(1))$?

### Problem 2
If $f(x) = 2x + 3$ and $g(x) = x^2 - 1$, what is $g(f(-2))$?

(A) 0  
(B) 2  
(C) 3  
(D) 8

### Problem 3
The graph of $y = f(x)$ is shown. If the vertex of this parabola is at $(-1, 4)$, what is the vertex of $y = f(x - 3) + 2$?

(A) $(2, 6)$  
(B) $(-4, 6)$  
(C) $(2, 2)$  
(D) $(-4, 2)$

### Problem 4
A function $f$ is defined by $f(x) = \sqrt{x-4}$. What is the domain of $f$?

(A) $x \geq 0$  
(B) $x \geq 4$  
(C) $x \leq 4$  
(D) All real numbers

### Problem 5
The graphs of $f(x) = x^2 - 4$ and $g(x) = x + 2$ are drawn on the same coordinate plane. At how many points do the graphs intersect?

(A) 0  
(B) 1  
(C) 2  
(D) 3

---

## Answers

### Problem 1 — Answer: 10

$f(1) = 4$ (from the point $(1, 4)$). Then $f(f(1)) = f(4)$. But we don't have the point $(4, y)$ directly. However, looking at the given points, we can find the slope: $m = (10-4)/(3-1) = 6/2 = 3$. So $f(x) = 3x + 1$ (check: $f(1) = 4$ ✓, $f(3) = 10$ ✓). Then $f(4) = 3(4) + 1 = 13$.

Wait — the problem only gave two points, implying the function is linear (or we use only those). With $f(1) = 4$: $f(f(1)) = f(4)$. The slope is 3, so $f(4) = f(3) + 3 = 10 + 3 = 13$. Actually, re-reading: with only two points, we assume linearity. $f(1)=4$, $f(3)=10$. Interpolate: each unit of $x$ increases $f(x)$ by 3, so $f(4) = 13$.

Wait — the problem as stated says passes through $(1,4)$ and $(3,10)$. If the function is linear: $f(4) = 13$. Then $f(f(1)) = f(4) = 13$. However, let me re-examine: if it's linear, $f(1)=4$, $f(4)$ we can compute, then $f(f(1)) = f(4) = 13$.

Actually, $f(1) = 4$, so $f(f(1)) = f(4)$. Since two points determine a line: $f(x) = 3x + 1$ (since $f(1)=4$, $f(3)=10$). $f(4) = 13$. **Answer: 13**.

---

### Problem 2 — Answer: (A) 0

$$f(-2) = 2(-2) + 3 = -4 + 3 = -1$$
$$g(f(-2)) = g(-1) = (-1)^2 - 1 = 1 - 1 = 0$$

**Wrong-answer analysis:**
- (B) 2 — might come from $g(1)$ instead of $g(-1)$
- (C) 3 — might come from $f(g(-2))$ instead of $g(f(-2))$
- (D) 8 — might come from $(g(-2))^2 - 1 = 9-1 = 8$, misreading the composite

---

### Problem 3 — Answer: (A) $(2, 6)$

Original vertex: $(-1, 4)$.
- $f(x-3)$ shifts **right** by 3: $(-1, 4) \to (2, 4)$
- $+2$ shifts **up** by 2: $(2, 4) \to (2, 6)$

**Wrong-answer analysis:**
- (B) $(-4, 6)$ — shifted left by 3 instead of right
- (C) $(2, 2)$ — shifted down instead of up
- (D) $(-4, 2)$ — both transformations backwards

---

### Problem 4 — Answer: (B) $x \geq 4$

For $f(x) = \sqrt{x-4}$ to be defined (real-valued), the radicand must be non-negative:
$$x - 4 \geq 0$$
$$x \geq 4$$

**Wrong-answer analysis:**
- (A) $x \geq 0$ — only considered the outer form $\sqrt{\ldots}$, ignoring the "$-4$"
- (C) $x \leq 4$ — reversed the inequality
- (D) All real numbers — domain of a square root is never all real numbers

---

### Problem 5 — Answer: (C) 2

Solve $f(x) = g(x)$:
$$x^2 - 4 = x + 2$$
$$x^2 - x - 6 = 0$$
$$(x-3)(x+2) = 0$$
$$x = 3 \text{ or } x = -2$$

Two intersection points: at $x = 3$ (point $(3, 5)$) and $x = -2$ (point $(-2, 0)$).

**Wrong-answer analysis:**
- (A) 0 — might think "parabola and line don't intersect" without solving
- (B) 1 — might only find one solution, or count the $y$-intercept intersection
- (D) 3 — a line and a parabola can intersect at most twice

---

## Key Takeaways

1. $f(g(x))$ means apply $g$ first, then $f$. Don't reverse the order.
2. $f(x+h)$ shifts the graph **LEFT**. This is one of the most-tested transformation concepts.
3. "Find $x$ such that $f(x) = k$" is solving $f(x) = k$, not computing $f(k)$.
4. For domain: denominators $\neq 0$, even-root radicands $\geq 0$.
5. Intersections of $f$ and $g$ = solutions to $f(x) = g(x)$.
