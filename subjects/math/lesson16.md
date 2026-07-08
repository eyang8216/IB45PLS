# Lesson 16: Slope Fields and Graphical Solutions

## 1. What Is a Slope Field?

A **slope field** (also called a direction field) is a visual tool for understanding a first-order differential equation without solving it algebraically. Given a differential equation of the form $\frac{dy}{dx} = f(x, y)$, the slope field is created by choosing many points in the $xy$-plane and, at each point $(x, y)$, drawing a short line segment whose slope equals $f(x, y)$—the value of the derivative at that point.

The result is a grid of tiny tangent lines that show you the "flow" of solutions. Any curve that is tangent to these line segments at every point is a **solution curve** (also called an integral curve) of the differential equation. The slope field reveals the behavior of all possible solutions at once, even when an explicit formula is impossible to find.

Slope fields matter because many differential equations cannot be solved with algebraic formulas. In those situations, the slope field gives us qualitative information: we can see whether solutions increase or decrease, where they level off, and what happens in the long run. This qualitative understanding is often as valuable as an exact formula.

---

## 2. How to Read and Sketch Slope Fields

To construct part of a slope field by hand, you pick a set of grid points, compute the slope $m = f(x, y)$ at each point, and draw a short line segment with that slope. A segment with slope $0$ is horizontal. A segment with a positive slope tilts upward to the right. A negative slope tilts downward. A very large slope (positive or negative) produces a nearly vertical segment.

### Example 1

Consider the differential equation $\frac{dy}{dx} = x + y$. Compute slopes at several points:

| $(x, y)$ | $m = x + y$ | Segment direction |
|---|---|---|
| $(0, 0)$ | $0$ | Horizontal |
| $(1, 0)$ | $1$ | Up-right at $45^\circ$ |
| $(0, 1)$ | $1$ | Up-right at $45^\circ$ |
| $(-1, 0)$ | $-1$ | Down-right at $45^\circ$ |
| $(1, 1)$ | $2$ | Steeper up-right |
| $(-1, 1)$ | $0$ | Horizontal |
| $(1, -1)$ | $0$ | Horizontal |

An **isocline** is a curve along which the slope is constant. For this equation, setting $x + y = k$ gives the line $y = -x + k$, and along this entire line the slope is $k$. The line $y = -x$ (where $k = 0$) is a special isocline where all slope segments are horizontal.

---

### Example 2

Consider $\frac{dy}{dx} = \frac{x}{y}$. At points where $y = 0$ (the $x$-axis), the slope is undefined, so we either draw vertical segments or leave those points blank. At points where $x = 0$ (the $y$-axis), the slope is $0$, so all segments on the $y$-axis are horizontal.

Computing a few values:

| $(x, y)$ | $m = x/y$ |
|---|---|
| $(1, 1)$ | $1$ |
| $(2, 1)$ | $2$ |
| $(1, 2)$ | $0.5$ |
| $(-1, 1)$ | $-1$ |
| $(-1, -1)$ | $1$ |

A common mistake is to draw slope segments without regard for undefined points. Where $y=0$, the differential equation itself breaks down; solution curves cannot cross the $x$-axis.

---

## 3. Solution Curves

A **solution curve** is a smooth curve drawn through the slope field that is tangent to every slope segment it passes near. Given an initial condition $(x_0, y_0)$, the solution curve is the unique curve that passes through that point and follows the flow of the slope field.

To sketch a solution curve:
1. Mark the initial point $(x_0, y_0)$.
2. Observe the direction of the slope segments at that point.
3. Move a small distance in that direction, then check the slope at the new location.
4. Continue, connecting these small steps into a smooth curve.
5. The curve must never have sharp corners; it should be smooth and follow the overall flow.

Different initial conditions produce different solution curves. Together, the family of all solution curves fills the plane (except where the differential equation is undefined). The slope field shows this entire family.

Many students think that slope fields uniquely determine one solution. In fact, a slope field shows all possible solutions; you need an initial condition to pick out a specific one.

---

## 4. Equilibrium Solutions and Stability

An **equilibrium solution** (also called a steady-state or constant solution) is a solution of the form $y = c$ (a constant) that satisfies $\frac{dy}{dx} = 0$ for all $x$. These appear in the slope field as horizontal lines where every slope segment is flat.

For example, consider $\frac{dy}{dx} = y(1 - y)$. Setting $\frac{dy}{dx} = 0$ gives $y(1-y) = 0$, so $y = 0$ and $y = 1$ are equilibrium solutions.

The **stability** of an equilibrium describes what happens to solutions that start nearby:

- A **stable** equilibrium attracts nearby solutions: if you start slightly away from it, you move toward it over time. Think of a ball resting at the bottom of a bowl—push it slightly and it rolls back.
- An **unstable** equilibrium repels nearby solutions: if you start slightly away, you move farther away. Think of a ball balanced on top of a hill.
- A **semi-stable** equilibrium attracts from one side but repels from the other.

For $\frac{dy}{dx} = y(1-y)$:
- Near $y = 0$: If $y$ is slightly above $0$, $\frac{dy}{dx} > 0$, so $y$ increases, moving away from $0$. If $y$ is slightly below $0$, $\frac{dy}{dx} < 0$, so $y$ decreases, also moving away. Thus $y = 0$ is **unstable**.
- Near $y = 1$: If $y$ is slightly below $1$, $\frac{dy}{dx} > 0$, so $y$ increases toward $1$. If $y$ is slightly above $1$, $\frac{dy}{dx} < 0$, so $y$ decreases toward $1$. Thus $y = 1$ is **stable**.

---

## 5. Euler's Method — Numerical Approximation

**Euler's method** is a simple numerical technique for approximating a solution curve when an exact formula is unavailable. The idea is to take small steps along the slope field, using the tangent line at each point to project forward.

Given $\frac{dy}{dx} = f(x, y)$, an initial point $(x_0, y_0)$, and a step size $h$:

$$x_{n+1} = x_n + h$$
$$y_{n+1} = y_n + h \cdot f(x_n, y_n)$$

At each step, we evaluate the slope at the current point, multiply by the step size to get the change in $y$, and add it to the current $y$. This is equivalent to following the tangent line for a distance $h$ before recomputing the slope.

A key limitation: Euler's method accumulates error at each step. Smaller step sizes give better accuracy but require more computation. The error is roughly proportional to $h$, so halving the step size roughly halves the error.

---

### Euler's Method Example

**Problem:** Use Euler's method with step size $h = 0.5$ to approximate $y(1)$ for the differential equation $\frac{dy}{dx} = x + y$ with initial condition $y(0) = 1$.

| $n$ | $x_n$ | $y_n$ | $f(x_n, y_n) = x_n + y_n$ | $y_{n+1} = y_n + 0.5 \cdot f$ |
|---|---|---|---|---|
| $0$ | $0$ | $1$ | $0 + 1 = 1$ | $1 + 0.5(1) = 1.5$ |
| $1$ | $0.5$ | $1.5$ | $0.5 + 1.5 = 2$ | $1.5 + 0.5(2) = 2.5$ |
| $2$ | $1.0$ | $2.5$ | — | — |

The approximation is $y(1) \approx 2.5$. The exact solution to this equation is $y = 2e^x - x - 1$, which gives $y(1) = 2e - 2 \approx 3.437$. The error is about $0.937$, which is large because the step size $h = 0.5$ is coarse. Using $h = 0.1$ would give a much better approximation.

---

## Practice Problems

**Problem 1**
Consider the differential equation $\frac{dy}{dx} = y - x$.

(a) Compute the slope at each of the following points: $(0, 0)$, $(1, 0)$, $(0, 1)$, $(1, 1)$, $(-1, 0)$, $(0, -1)$, and $(2, 2)$.

(b) Find the equation of the line along which $\frac{dy}{dx} = 0$.

(c) Describe in words what the isoclines of this differential equation look like.

**Problem 2**
Consider the differential equation $\frac{dy}{dx} = y^2 - 1$.

(a) Find all equilibrium solutions.

(b) Determine the stability of each equilibrium by analyzing the sign of $\frac{dy}{dx}$ in the regions between equilibria.

**Problem 3**
A slope field for the differential equation $\frac{dy}{dx} = -\frac{x}{y}$ is drawn on the $xy$-plane. A particular solution curve passes through the point $(3, 4)$.

(a) What is the slope of the solution curve at $(3, 4)$?

(b) The family of solution curves for this differential equation consists of circles centered at the origin. Find the equation of the specific circle that passes through $(3, 4)$.

**Problem 4**
Use Euler's method with step size $h = 0.5$ to approximate $y(1)$ for the differential equation $\frac{dy}{dx} = 2x$ with initial condition $y(0) = 0$. Compare your result with the exact solution $y = x^2$.

**Problem 5 (IB-style)**
Consider the differential equation $\frac{dy}{dx} = \sin y$ for $-\pi < y < \pi$.

(a) Find all equilibrium solutions of the differential equation in the given range. [2 marks]

(b) By considering the sign of $\sin y$ near $y = 0$, determine whether $y = 0$ is a stable or unstable equilibrium. Justify your answer. [3 marks]

(c) Given that $y(0) = 0.1$, determine the value of $\lim_{x \to \infty} y(x)$, explaining your reasoning with reference to the slope field. [2 marks]

---

## Answers

**Answer 1**

**(a)** Slopes at each point:

| $(x, y)$ | $m = y - x$ |
|---|---|
| $(0, 0)$ | $0$ |
| $(1, 0)$ | $-1$ |
| $(0, 1)$ | $1$ |
| $(1, 1)$ | $0$ |
| $(-1, 0)$ | $1$ |
| $(0, -1)$ | $-1$ |
| $(2, 2)$ | $0$ |

**(b)** The slope is zero when $y - x = 0$, which is the line $y = x$.

**(c)** The isoclines are lines of the form $y - x = k$, or equivalently $y = x + k$. Along each such line, the slope is constant and equal to $k$. These isoclines form a family of parallel lines with slope $1$.

---

**Answer 2**

**(a)** Set $\frac{dy}{dx} = y^2 - 1 = 0$. This gives $y^2 = 1$, so $y = 1$ and $y = -1$ are the equilibrium solutions.

**(b)** Analyze the sign of $y^2 - 1 = (y-1)(y+1)$:

For $y < -1$: both $(y-1)$ and $(y+1)$ are negative, so their product is positive. Thus $\frac{dy}{dx} > 0$, meaning $y$ is increasing, moving toward $-1$.

For $-1 < y < 1$: $(y-1)$ is negative and $(y+1)$ is positive, so their product is negative. Thus $\frac{dy}{dx} < 0$, meaning $y$ is decreasing. In this region, if $y$ is above $-1$, it decreases toward $-1$.

For $y > 1$: both factors are positive, so $\frac{dy}{dx} > 0$, meaning $y$ is increasing, moving away from $1$.

Conclusion: $y = -1$ is stable (solutions approach it from both sides). $y = 1$ is unstable (solutions move away from it on both sides).

---

**Answer 3**

**(a)** At $(3, 4)$, the slope is $m = -\frac{3}{4} = -0.75$. The segment at this point points downward to the right.

**(b)** Separating the differential equation: $y\,dy = -x\,dx$. Integrating: $\frac{y^2}{2} = -\frac{x^2}{2} + C$. Multiplying by $2$: $x^2 + y^2 = 2C$, which is the equation of a circle centered at the origin with radius $\sqrt{2C}$.

For the curve through $(3, 4)$: $3^2 + 4^2 = 9 + 16 = 25$, so $2C = 25$ and the circle is $x^2 + y^2 = 25$, a circle of radius $5$.

---

**Answer 4**
The differential equation is $\frac{dy}{dx} = 2x$, with $y(0) = 0$. Euler's method with $h = 0.5$:

| $n$ | $x_n$ | $y_n$ | $f = 2x_n$ | $y_{n+1} = y_n + 0.5 \cdot 2x_n = y_n + x_n$ |
|---|---|---|---|---|
| $0$ | $0$ | $0$ | $0$ | $0 + 0 = 0$ |
| $1$ | $0.5$ | $0$ | $1$ | $0 + 0.5 = 0.5$ |
| $2$ | $1.0$ | $0.5$ | — | — |

So $y(1) \approx 0.5$.

The exact solution is found by integrating: $y = x^2 + C$. With $y(0) = 0$, we get $C = 0$, so $y = x^2$. The exact value is $y(1) = 1$.

The Euler approximation gives $0.5$, while the true value is $1$. The error is $0.5$, which is large because $h = 0.5$ is a coarse step size. With $h = 0.1$, Euler's method would give a much more accurate result.

---

**Answer 5 (IB-style)**

**(a)** Equilibrium solutions satisfy $\frac{dy}{dx} = \sin y = 0$. In the interval $(-\pi, \pi)$, the solutions to $\sin y = 0$ are $y = -\pi$, $y = 0$, and $y = \pi$. [2 marks]

**(b)** Near $y = 0$, we examine the sign of $\sin y$. For small positive $y$ (for example, $y = 0.1$), $\sin(0.1) > 0$, so $\frac{dy}{dx} > 0$, meaning $y$ increases—it moves away from $0$ toward larger values. For small negative $y$ (for example, $y = -0.1$), $\sin(-0.1) < 0$, so $\frac{dy}{dx} < 0$, meaning $y$ decreases—it also moves away from $0$, toward more negative values. Since nearby solutions on both sides move away from $y = 0$, the equilibrium is unstable. [3 marks]

**(c)** With $y(0) = 0.1$, the solution starts slightly above the unstable equilibrium at $y = 0$. Since $\sin y > 0$ for $0 < y < \pi$, the derivative is positive, so $y$ increases. As $y$ approaches $\pi$, $\sin y$ remains positive but becomes smaller, so the growth slows. The solution approaches $y = \pi$ asymptotically. Therefore $\lim_{x \to \infty} y(x) = \pi$.

This conclusion can be seen from the slope field: arrows above $y = 0$ all point upward toward $y = \pi$, which acts as a stable equilibrium (solutions above $\pi$ have $\sin y < 0$ and move downward toward $\pi$). [2 marks]
