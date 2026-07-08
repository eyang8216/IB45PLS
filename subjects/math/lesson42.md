# Lesson 42: Function Fundamentals — Domain, Range, Composition, and Inverses

## What You Will Learn and Why It Matters

A **function** is a rule that assigns each input to exactly one output. You write this as $f(x)$ where $x$ is the input. This lesson covers four foundational ideas: the set of allowed inputs (domain), the set of possible outputs (range), combining two functions into one (composition), and reversing a function to get the input back from the output (inverse). These ideas appear throughout the IB AAHL syllabus — in calculus, in probability density functions, in transformations of graphs, and in solving equations. If you do not fully understand domain and inverse functions now, later topics like derivatives of inverse trig functions or integration by substitution will feel much harder than they actually are.

---

## 1. Domain: The Set of Allowed Inputs

The **domain** of a function is the set of all real numbers $x$ that you can safely plug into the function without causing a mathematical error. There are three operations that restrict the domain: division by zero, square roots (or any even-indexed root) of a negative number, and logarithms of zero or negative numbers.

When you see a fraction, set the denominator not equal to zero and solve. When you see a square root, set the expression inside the square root to be greater than or equal to zero. When you see a logarithm, set the argument strictly greater than zero.

To write the domain, use either inequality notation ($x \geq 3$) or interval notation ($[3, \infty)$). Both are acceptable on IB exams, but you should be comfortable with both.

---

### Worked Example 1

**Problem:** Find the domain of the function $f(x) = \sqrt{x - 3}$.

**Approach:** A square root requires the expression inside it to be non-negative. Write that inequality and solve.

**Step-by-step working:**
1. The expression under the square root is $x - 3$.
2. For the square root to be defined, we need $x - 3 \geq 0$.
3. Adding $3$ to both sides gives $x \geq 3$.

The domain is $\{x \in \mathbb{R} \mid x \geq 3\}$, which in interval notation is $[3, \infty)$.

**Why this makes sense:** If you try $x = 2$, you get $\sqrt{-1}$, which is not a real number. If you try $x = 3$, you get $\sqrt{0} = 0$, which is fine. Any number larger than $3$ also works.

---

### Worked Example 2

**Problem:** Find the domain of the function $f(x) = \dfrac{1}{x^2 - 4}$.

**Approach:** This is a fraction. The denominator cannot be zero. Set the denominator equal to zero, find the forbidden values, and exclude them from all real numbers.

**Step-by-step working:**
1. The denominator is $x^2 - 4$.
2. Set $x^2 - 4 = 0$, which gives $x^2 = 4$.
3. Taking square roots on both sides gives $x = 2$ or $x = -2$.
4. These are the values that make the denominator zero.

The domain is all real numbers except $2$ and $-2$. In interval notation: $(-\infty, -2) \cup (-2, 2) \cup (2, \infty)$.

**Why this makes sense:** At $x = 2$, the fraction becomes $\frac{1}{0}$, which is undefined. At $x = -2$, same problem. Every other number gives a real output.

---

## 2. Range: The Set of All Possible Outputs

The **range** of a function is the set of all $y$ values (outputs) that the function can produce when you use every $x$ in the domain.

Finding the range is often harder than finding the domain. For simple functions, you can figure out the range by asking: "What values can this expression produce?" For example, a square root can never give a negative output. A squared expression is always non-negative. A fraction with a constant numerator and a quadratic denominator has certain behaviors near asymptotes and far away from them.

---

### Worked Example 3

**Problem:** Find the range of $f(x) = \sqrt{x - 3}$.

**Approach:** Determine what outputs the square root can produce given the domain $x \geq 3$.

**Step-by-step working:**
1. The smallest value in the domain is $x = 3$.
2. When $x = 3$, $f(3) = \sqrt{0} = 0$.
3. As $x$ increases, $x - 3$ increases.
4. The square root of ever-larger numbers produces ever-larger outputs, with no upper bound.

The range is $\{y \in \mathbb{R} \mid y \geq 0\}$, or $[0, \infty)$.

**Why this makes sense:** The square root symbol always denotes the non-negative root. Even if the expression inside gets very large, the output is always zero or positive, never negative.

---

### Worked Example 4

**Problem:** Find the range of $f(x) = \dfrac{1}{x^2 - 4}$, where $x \neq \pm 2$.

**Approach:** Analyze the behavior of the fraction as $x$ approaches the excluded values and as $x$ becomes very large (positive or negative). Identify the output values that appear.

**Step-by-step working:**
1. As $x$ approaches $2$ from the right, $x^2 - 4$ is a small positive number, so the fraction becomes very large and positive. As $x$ approaches $2$ from the left, $x^2 - 4$ is a small negative number, so the fraction becomes very large and negative. Similar behavior occurs near $x = -2$.
2. As $x \to \infty$ or $x \to -\infty$, $x^2 - 4$ becomes very large, so $\frac{1}{x^2 - 4}$ approaches $0$ from the positive side if $|x| > 2$, and from the negative side if $|x| < 2$.
3. Between $-2$ and $2$, the denominator $x^2 - 4$ is negative. At $x = 0$, it is $-4$, giving $f(0) = -\frac{1}{4}$. This is the maximum value in that negative portion.
4. For $|x| > 2$, the output is always positive and can take any positive value.

The range is $(-\infty, -\frac{1}{4}] \cup (0, \infty)$. Notice that $-\frac{1}{4}$ is included because it is achieved at $x = 0$. Zero is not included because the output never actually reaches zero; it only approaches zero as $x$ grows without bound.

**Common misconception:** Many students think the range must be all real numbers except something. But a function like this one has a gap: values between $-\frac{1}{4}$ and $0$ (excluding $-\frac{1}{4}$ itself and excluding $0$) are never produced.

---

## 3. Composite Functions

A **composite function** applies one function to the output of another. The notation $(f \circ g)(x)$ means "apply $g$ to $x$ first, then apply $f$ to that result." Written out: $(f \circ g)(x) = f(g(x))$.

The **domain of a composite function** $(f \circ g)$ consists of all $x$ such that:
- $x$ is in the domain of $g$ (so you can compute $g(x)$), AND
- $g(x)$ is in the domain of $f$ (so you can plug the result into $f$).

Many students skip the second condition. Do not skip it.

---

### Worked Example 5

**Problem:** Let $f(x) = 2x + 1$ and $g(x) = x^2$. Find both $(f \circ g)(x)$ and $(g \circ f)(x)$. Then explain why they are different.

**Approach:** For $(f \circ g)(x)$, substitute $g(x)$ into $f$ by replacing every $x$ in $f(x)$ with $x^2$. For $(g \circ f)(x)$, do the reverse.

**Step-by-step working:**
1. $(f \circ g)(x) = f(g(x)) = f(x^2) = 2(x^2) + 1 = 2x^2 + 1$.
2. $(g \circ f)(x) = g(f(x)) = g(2x + 1) = (2x + 1)^2 = 4x^2 + 4x + 1$.

The two results are different: $2x^2 + 1$ versus $4x^2 + 4x + 1$.

**Why this makes sense:** Composition is not like multiplication. The order matters because you are changing which operation happens first. Squaring then doubling and adding 1 is not the same as doubling and adding 1 then squaring.

---

### Worked Example 6

**Problem:** Let $f(x) = \sqrt{x}$ and $g(x) = x - 5$. Find the domain of the composite function $(f \circ g)(x)$.

**Approach:** First form the composite: $f(g(x)) = \sqrt{x - 5}$. Then apply both domain conditions.

**Step-by-step working:**
1. $g(x) = x - 5$ is defined for all real numbers. So the first condition places no restriction.
2. The output of $g$ is $x - 5$. This must be in the domain of $f$, which requires the input to be $\geq 0$ (since $f$ is a square root).
3. So we need $x - 5 \geq 0$, which gives $x \geq 5$.

The domain of $(f \circ g)$ is $[5, \infty)$.

**Common misconception:** Some students think the domain of the composite is just the domain of the inner function $g$. Here, $g$ is defined for all real numbers, but the composite is only defined for $x \geq 5$.

---

## 4. Inverse Functions

An **inverse function** undoes what the original function did. If $f(a) = b$, then $f^{-1}(b) = a$. The notation $f^{-1}$ does NOT mean $\frac{1}{f}$. It means the inverse function.

To find the inverse function algebraically:
1. Write $y = f(x)$.
2. Swap every $x$ for $y$ and every $y$ for $x$.
3. Solve the resulting equation for $y$. The result is $y = f^{-1}(x)$.

A function has an inverse **only if it is one-to-one** on its domain. A one-to-one function is a function where each output comes from exactly one input. Graphically, a one-to-one function passes the **horizontal line test**: any horizontal line crosses the graph at most once.

Graphically, the inverse function is the reflection of the original function across the line $y = x$.

---

### Worked Example 7

**Problem:** Find the inverse of $f(x) = \dfrac{2x - 1}{x + 3}$, where $x \neq -3$.

**Approach:** Write $y = f(x)$, swap $x$ and $y$, then solve for $y$.

**Step-by-step working:**
1. Write $y = \dfrac{2x - 1}{x + 3}$.
2. Swap: $x = \dfrac{2y - 1}{y + 3}$.
3. Multiply both sides by $(y + 3)$: $x(y + 3) = 2y - 1$.
4. Expand: $xy + 3x = 2y - 1$.
5. Group terms containing $y$ on one side: $xy - 2y = -3x - 1$.
6. Factor out $y$: $y(x - 2) = -3x - 1$.
7. Multiply both sides by $-1$: $y(2 - x) = 3x + 1$.
8. Divide by $(2 - x)$: $y = \dfrac{3x + 1}{2 - x}$.

So $f^{-1}(x) = \dfrac{3x + 1}{2 - x}$, with domain $x \neq 2$.

**Why this makes sense:** You can check by composing: $f(f^{-1}(x))$ should equal $x$. If you plug $\frac{3x+1}{2-x}$ into the original formula for $f$, the algebra will simplify to $x$.

---

## 5. Odd and Even Functions

A function is **even** if $f(-x) = f(x)$ for every $x$ in the domain. This means the graph is symmetric about the $y$-axis. Common examples include $x^2$, $\cos x$, and $|x|$.

A function is **odd** if $f(-x) = -f(x)$ for every $x$ in the domain. This means the graph has rotational symmetry of 180 degrees about the origin. Common examples include $x^3$, $\sin x$, and $x$.

Many functions are neither even nor odd. To classify, compute $f(-x)$ and compare it to $f(x)$ and $-f(x)$.

---

### Worked Example 8

**Problem:** Classify $f(x) = x^3 - 3x$ as even, odd, or neither.

**Approach:** Compute $f(-x)$ by substituting $-x$ everywhere $x$ appears. Then simplify and compare to $f(x)$ and $-f(x)$.

**Step-by-step working:**
1. $f(-x) = (-x)^3 - 3(-x) = -x^3 + 3x$.
2. Factor out $-1$: $f(-x) = -(x^3 - 3x) = -f(x)$.
3. Since $f(-x) = -f(x)$, the function is odd.

**Why this makes sense:** If you pick $x = 2$, then $f(2) = 8 - 6 = 2$ and $f(-2) = -8 + 6 = -2$, which is indeed $-f(2)$.

---

## Practice Problems

**1.** Find the domain and range of $f(x) = \ln(x + 2)$.

**2.** Let $f(x) = \dfrac{1}{x}$ and $g(x) = 3x - 2$. Find and simplify both $(f \circ g)(x)$ and $(g \circ f)(x)$. State the domain of each composite function.

**3.** Find the inverse function of $f(x) = 2e^x - 1$. State the domain of the inverse.

**4.** Classify $f(x) = |x|$ as even, odd, or neither. Justify your answer by showing the calculation.

**5.** (IB Exam Style) A function $f$ is defined by $f(x) = \sqrt{x^2 - 9}$.

(a) Find the domain of $f$. [2 marks]

(b) Find the range of $f$. [2 marks]

(c) Explain why $f$ does not have an inverse function on its maximal domain, and suggest a domain restriction that would make $f$ invertible. [2 marks]

**6.** The functions $f$ and $g$ are defined by $f(x) = 2x + 1$ and $(f \circ g)(x) = 6x + 5$. Find an expression for $g(x)$.

---

## Answers

**1.** The function $\ln(x + 2)$ contains a natural logarithm. The argument of a logarithm must be strictly greater than zero. So $x + 2 > 0$, which gives $x > -2$. The domain is $(-2, \infty)$. For the range, the natural logarithm function can output any real number. As $x$ approaches $-2$ from the right, $x + 2$ approaches $0^+$ and $\ln(x+2)$ approaches $-\infty$. As $x$ grows without bound, $\ln(x+2)$ grows without bound. Every real number is achieved somewhere. The range is $\mathbb{R}$, or $(-\infty, \infty)$. A common mistake is to think the range is $[0, \infty)$ because of the square-root pattern, but logarithms behave differently from square roots.

**2.** For $(f \circ g)(x)$: substitute $g(x) = 3x - 2$ into $f(x) = \frac{1}{x}$. This gives $(f \circ g)(x) = \frac{1}{3x - 2}$. The denominator cannot be zero, so $3x - 2 \neq 0$, meaning $x \neq \frac{2}{3}$. The domain of $f \circ g$ is all real numbers except $\frac{2}{3}$. For $(g \circ f)(x)$: substitute $f(x) = \frac{1}{x}$ into $g(x) = 3x - 2$. This gives $(g \circ f)(x) = 3\left(\frac{1}{x}\right) - 2 = \frac{3}{x} - 2$. The domain of $f$ itself requires $x \neq 0$, so the domain of $g \circ f$ is all real numbers except $0$.

**3.** Start with $y = 2e^x - 1$. Swap $x$ and $y$: $x = 2e^y - 1$. Add $1$ to both sides: $x + 1 = 2e^y$. Divide by $2$: $\frac{x+1}{2} = e^y$. Take the natural logarithm of both sides: $y = \ln\left(\frac{x+1}{2}\right)$. Thus $f^{-1}(x) = \ln\left(\frac{x+1}{2}\right)$. For this inverse to be defined, the argument of the logarithm must be positive, so $\frac{x+1}{2} > 0$, which gives $x > -1$. The domain of $f^{-1}$ is $(-1, \infty)$. Notice that this matches the range of the original function: $f(x) = 2e^x - 1$ always gives outputs greater than $-1$, because $e^x > 0$ so $2e^x > 0$ and $2e^x - 1 > -1$.

**4.** Compute $f(-x) = |{-x}|$. The absolute value of $-x$ equals the absolute value of $x$, because absolute value measures distance from zero regardless of sign. So $f(-x) = |x| = f(x)$. Since $f(-x) = f(x)$ for all real $x$, the function $f(x) = |x|$ is even. Many students incorrectly guess that $|x|$ is odd because the graph has a sharp corner, but the test is purely algebraic: $f(-x)$ must equal either $f(x)$ or $-f(x)$.

**5.** (a) The expression under the square root must be non-negative: $x^2 - 9 \geq 0$. This means $x^2 \geq 9$, so $|x| \geq 3$. The domain is $(-\infty, -3] \cup [3, \infty)$. [2 marks]

(b) At the boundary points $x = \pm 3$, $f(x) = \sqrt{0} = 0$. As $|x|$ increases, $x^2 - 9$ grows without bound, so $\sqrt{x^2 - 9}$ grows without bound. The square root always gives a non-negative output. Therefore the range is $[0, \infty)$. [2 marks]

(c) The function fails the horizontal line test because $f(4) = \sqrt{7}$ and $f(-4) = \sqrt{7}$ — two different inputs give the same output. So $f$ is not one-to-one on its full domain. To make $f$ invertible, restrict the domain to $[3, \infty)$ (the right branch only). Then each output comes from exactly one input. Alternatively, one could restrict to $(-\infty, -3]$. [2 marks]

**6.** We know that $(f \circ g)(x) = f(g(x)) = 2 \cdot g(x) + 1$. The problem tells us this equals $6x + 5$. So we set up the equation: $2g(x) + 1 = 6x + 5$. Subtract $1$ from both sides: $2g(x) = 6x + 4$. Divide by $2$: $g(x) = 3x + 2$. To verify: $f(g(x)) = 2(3x + 2) + 1 = 6x + 4 + 1 = 6x + 5$, which matches the given information.
