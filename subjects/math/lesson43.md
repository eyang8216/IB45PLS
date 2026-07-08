# Lesson 43: Function Transformations

## What You Will Learn and Why It Matters

A **transformation** changes a function's graph by shifting it, stretching it, or reflecting it. Instead of plotting hundreds of points for each new function, you can take a parent function you already know — like $x^2$, $\sin x$, or $e^x$ — and apply a few simple rules to produce the new graph. IB AAHL exam questions routinely test your ability to describe a sequence of transformations, to find the equation of a transformed graph, and to determine how a specific point on the original graph moves under the transformation. If you master the six basic transformations and the correct order in which to apply them, you will handle these questions quickly and accurately.

---

## 1. The Six Basic Transformations

Start with a parent function $y = f(x)$. Each of the six transformations below modifies either the input ($x$) or the output ($y$).

### Vertical transformations (act on the output)

- **Vertical shift up by $k$:** Add $k$ to the output. Equation: $y = f(x) + k$. Every point on the graph moves up by $k$ units.
- **Vertical shift down by $k$:** Subtract $k$. Equation: $y = f(x) - k$.
- **Vertical stretch by factor $a$:** Multiply the output by $a$. Equation: $y = a \cdot f(x)$. If $a > 1$, the graph gets taller. If $0 < a < 1$, the graph gets shorter.
- **Reflection in the $x$-axis:** Negate the output. Equation: $y = -f(x)$. The graph flips over the $x$-axis.

### Horizontal transformations (act on the input — and they feel "backwards")

- **Horizontal shift right by $h$:** Replace $x$ with $(x - h)$. Equation: $y = f(x - h)$. Despite the minus sign, the graph moves to the right. This is the source of more mistakes than any other transformation.
- **Horizontal shift left by $h$:** Replace $x$ with $(x + h)$. Equation: $y = f(x + h)$.
- **Horizontal stretch by factor $\frac{1}{b}$:** Replace $x$ with $bx$. Equation: $y = f(bx)$. If $b > 1$, the graph compresses horizontally. If $0 < b < 1$, the graph stretches horizontally.
- **Reflection in the $y$-axis:** Negate the input. Equation: $y = f(-x)$. The graph flips over the $y$-axis.

**Why the horizontal ones feel backwards:** When you write $f(x - 2)$, you are asking: "At what input does the function now see the value that it used to see at $x$?" It sees the old value at $x - 2$, which is two units to the left of $x$. To compensate, the whole graph shifts two units to the right. Many students memorize "inside does the opposite." A better understanding: horizontal transformations change the $x$ before the function acts on it, so the effect on the graph is the reverse of the arithmetic operation inside the parentheses.

---

## 2. Combining Multiple Transformations

When a function has several transformations, you must apply them in a consistent order. The safest approach is to think from the **inside out**, following BIDMAS in reverse: handle what is closest to the $x$ first, then work outward.

### Worked Example 1

**Problem:** Describe all transformations needed to change $f(x) = x^2$ into $g(x) = 3(x + 1)^2 - 4$.

**Approach:** Identify the operations applied, working from inside the function (closest to the $x$) outward.

**Step-by-step working:**
1. Inside the parentheses: $x$ becomes $x + 1$. This is a horizontal shift **left** by $1$ unit. (The $+1$ feels backwards — it moves the graph left.)
2. Outside the squared term: the result is multiplied by $3$. This is a vertical stretch by factor $3$.
3. At the very end: $4$ is subtracted. This is a vertical shift **down** by $4$ units.

**Why this makes sense:** If you pick a test point on the original graph, say $(0, 0)$ from $y = x^2$, then:
- After the left shift: $(-1, 0)$
- After the vertical stretch: $(-1, 0)$ (zero times anything is still zero)
- After the down shift: $(-1, -4)$
And indeed, $g(-1) = 3(0)^2 - 4 = -4$. The vertex has moved from $(0, 0)$ to $(-1, -4)$.

---

### Worked Example 2

**Problem:** The graph of $y = f(x)$ is translated 2 units to the right, then reflected in the $x$-axis, then stretched vertically by a factor of 3. Find the equation of the resulting graph in terms of $f$.

**Approach:** Apply each transformation in the order given, building the equation step by step.

**Step-by-step working:**
1. Translate 2 units right: replace $x$ with $x - 2$. Equation becomes $y = f(x - 2)$.
2. Reflect in the $x$-axis: multiply the output by $-1$. Equation becomes $y = -f(x - 2)$.
3. Stretch vertically by factor 3: multiply the output by $3$. Equation becomes $y = -3f(x - 2)$.

The final equation is $y = -3f(x - 2)$.

**Common misconception:** Many students write $y = -3f(x + 2)$ for a right shift because they confuse the direction of the horizontal shift. A shift to the right uses $(x - 2)$, not $(x + 2)$.

---

### Worked Example 3

**Problem:** The graph of $y = f(x)$ is transformed to $y = 2f(3x - 6) + 1$. Describe the sequence of transformations in the correct order.

**Approach:** Rewrite the argument so the factor of $x$ is isolated: $3x - 6 = 3(x - 2)$. Now work from inside out.

**Step-by-step working:**
1. The expression $3(x - 2)$ means: first shift right by $2$ (from $x - 2$), then horizontally compress by factor $\frac{1}{3}$ (from the $3$ multiplying the whole bracket).
2. Outside the function: multiply the output by $2$. This is a vertical stretch by factor $2$.
3. Add $1$ at the end. This is a vertical shift up by $1$ unit.

**Why the rewrite matters:** If you do not factor out the $3$, you might incorrectly think the horizontal shift is $6$ units right. The rewrite $3x - 6 = 3(x - 2)$ reveals the true shift is only $2$ units right.

---

## 3. Transformations of Specific Function Families

### Exponential functions: $f(x) = e^x$

The parent graph $y = e^x$ passes through $(0, 1)$, is always positive, and increases rapidly. Transformations follow the same rules:
- $y = e^{x - a}$ shifts the graph right by $a$.
- $y = Ae^x$ stretches the graph vertically by factor $A$.
- $y = e^x + C$ shifts the graph up by $C$. The horizontal asymptote moves from $y = 0$ to $y = C$.

### Trigonometric functions: $y = A\sin(Bx + C) + D$

For a sine or cosine graph in the form $y = A\sin(Bx + C) + D$:
- $|A|$ is the **amplitude**: the distance from the midline to a peak.
- The **period** (length of one full cycle) is $\frac{2\pi}{|B|}$.
- The **phase shift** (horizontal displacement) is $-\frac{C}{B}$. Factor out $B$ first: $Bx + C = B\!\left(x + \frac{C}{B}\right)$, so the shift is $-\frac{C}{B}$.
- $D$ is the **vertical shift**. The midline moves from $y = 0$ to $y = D$.

---

### Worked Example 4

**Problem:** For the function $y = 3\sin\!\left(2x - \frac{\pi}{3}\right) + 1$, find the amplitude, period, phase shift, and vertical shift.

**Approach:** Factor the argument of sine: $2x - \frac{\pi}{3} = 2\!\left(x - \frac{\pi}{6}\right)$. Then read off each parameter.

**Step-by-step working:**
1. Amplitude: $|A| = |3| = 3$. The graph oscillates between $3$ units above and $3$ units below the midline.
2. Period: $\frac{2\pi}{|B|} = \frac{2\pi}{2} = \pi$.
3. Phase shift: The factorized form shows $-\frac{C}{B} = \frac{\pi}{6}$. Since it is $x - \frac{\pi}{6}$, the shift is $\frac{\pi}{6}$ to the right.
4. Vertical shift: $D = 1$. The midline is $y = 1$. The graph ranges from $1 - 3 = -2$ to $1 + 3 = 4$.

---

## Practice Problems

**1.** Describe the sequence of transformations that maps $f(x)$ onto $g(x) = -2f(x - 1) + 3$.

**2.** The point $(2, 5)$ lies on the graph of $y = f(x)$. Determine the coordinates of the image of this point on the graph of $y = f(2x + 4)$.

**3.** The graph of $y = |x|$ is shifted 3 units to the right, then reflected in the $x$-axis, then shifted 2 units up. Find the equation of the resulting graph.

**4.** For the function $y = 4\cos(3x + \pi) - 2$, find the amplitude, the period, the phase shift (state whether left or right), and the vertical shift.

**5.** (IB Exam Style) The graph of $y = \dfrac{1}{x}$ is transformed by a vertical stretch with scale factor 2, followed by a horizontal translation of 1 unit to the left, followed by a vertical translation of 3 units down.

(a) Write the equation of the transformed function. [2 marks]

(b) Write down the equations of all asymptotes of the transformed graph. [2 marks]

(c) Find the coordinates of the point on the transformed graph that corresponds to the point $(1, 1)$ on the original graph. [2 marks]

**6.** The function $f(x) = x^2$ undergoes the following transformations in order: a horizontal compression by factor $\frac{1}{2}$, a reflection in the $x$-axis, a horizontal translation 3 units to the right, and a vertical translation 1 unit up. Find the equation of the resulting function and state the coordinates of its vertex.

---

## Answers

**1.** Starting from $f(x)$: the $(x - 1)$ inside means shift **right** by 1 unit. The $-2$ multiplying $f$ means a vertical stretch by factor $2$ combined with a reflection in the $x$-axis (the negative sign). The $+3$ at the end means shift **up** by 3 units. The order matters: the horizontal shift happens first, the stretch and reflection are applied second, and the vertical shift is last. A common mistake is to apply the reflection before the stretch or to confuse the direction of the horizontal shift.

**2.** First factor the argument: $2x + 4 = 2(x + 2)$. This represents a horizontal compression by factor $\frac{1}{2}$ and a shift left by $2$. To find the new location of the point $(2, 5)$, let the original $x$ coordinate $2$ be the input to $f$. After the transformation, we need $2(x_{\text{new}} + 2) = 2$, so $x_{\text{new}} + 2 = 1$, giving $x_{\text{new}} = -1$. The $y$ coordinate is unchanged because no vertical transformation was applied. The image point is $(-1, 5)$. Many students forget to factor out the $2$ and incorrectly solve $2x + 4 = 2$ giving $x = -1$ by coincidence — but the method of factoring is essential for understanding.

**3.** Start with $y = |x|$. Shift 3 right: $y = |x - 3|$. Reflect in $x$-axis: $y = -|x - 3|$. Shift 2 up: $y = -|x - 3| + 2$. The vertex of the V-shaped graph is now at $(3, 2)$, and the V opens downward.

**4.** Factor the argument: $3x + \pi = 3\!\left(x + \frac{\pi}{3}\right)$. Amplitude: $|4| = 4$. Period: $\frac{2\pi}{3}$. Phase shift: $\frac{\pi}{3}$ to the **left** (because the factorized form has $+ \frac{\pi}{3}$ inside the brackets). Vertical shift: $2$ units **down**. The midline is $y = -2$, and the graph oscillates between $-6$ and $2$.

**5.** (a) Start with $y = \frac{1}{x}$. Vertical stretch by factor 2: $y = \frac{2}{x}$. Horizontal translation 1 unit left: $y = \frac{2}{x + 1}$. Vertical translation 3 down: $y = \frac{2}{x + 1} - 3$. [2 marks]

(b) The original graph of $y = \frac{1}{x}$ has asymptotes at $x = 0$ (vertical) and $y = 0$ (horizontal). The horizontal shift left by 1 moves the vertical asymptote to $x = -1$. The vertical shift down by 3 moves the horizontal asymptote to $y = -3$. The vertical stretch does not affect the location of asymptotes. So the asymptotes are $x = -1$ and $y = -3$. [2 marks]

(c) The original point $(1, 1)$ moves: left 1 to $x = 0$, then the $y$-value is stretched and shifted. Compute directly: when $x = 0$, $y = \frac{2}{0 + 1} - 3 = 2 - 3 = -1$. So the corresponding point is $(0, -1)$. [2 marks]

**6.** Start with $f(x) = x^2$. Horizontal compression by factor $\frac{1}{2}$: replace $x$ with $2x$, giving $(2x)^2 = 4x^2$. Reflection in $x$-axis: $y = -4x^2$. Horizontal translation 3 right: replace $x$ with $x - 3$, giving $y = -4(x - 3)^2$. Vertical translation 1 up: $y = -4(x - 3)^2 + 1$. The vertex was at $(0, 0)$. After shifting 3 right and 1 up, the vertex is at $(3, 1)$. The parabola opens downward because of the negative sign.
