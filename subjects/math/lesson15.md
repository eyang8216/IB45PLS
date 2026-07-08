# Lesson 15: Separable Differential Equations

## 1. What Is a Differential Equation?

A **differential equation** is an equation that involves an unknown function together with one or more of its derivatives. The unknown is not a number—it is an entire function. To solve a differential equation means to find all functions that make the equation true.

Differential equations matter because they describe how things change. The rate at which a population grows, the speed at which a radioactive substance decays, the temperature of a cooling object, and the motion of a vibrating spring are all governed by differential equations. In each case, the equation links the current state of a system to how that state is changing.

The simplest differential equation looks like this:

$$\frac{dy}{dx} = 2x$$

This equation says: "the derivative of $y$ with respect to $x$ equals $2x$." The solution is any function $y(x)$ whose derivative is $2x$. You can find it by integrating both sides: $y = \int 2x\,dx = x^2 + C$, where $C$ is an arbitrary constant.

---

## 2. Order, General Solutions, and Particular Solutions

The **order** of a differential equation is the highest derivative that appears in it. The equation $\frac{dy}{dx} = 2x$ is **first order** because only the first derivative appears. The equation $\frac{d^2y}{dx^2} + 3y = 0$ is **second order** because the second derivative appears. In IB AAHL, we focus on first-order differential equations.

When you solve a differential equation, you typically get a **general solution**—a family of functions that all satisfy the equation, differing from each other by a constant $C$. The general solution contains all possible solutions.

If you are also given an **initial condition**—a specific pair of values, such as $y(1) = 5$, meaning "when $x = 1$, the function value is $5$"—then you can determine the specific value of $C$. The resulting single function is called a **particular solution**.

For example, the general solution of $\frac{dy}{dx} = 2x$ is $y = x^2 + C$. If we add the initial condition $y(1) = 5$, then substituting gives $5 = 1^2 + C$, so $C = 4$. The particular solution is $y = x^2 + 4$.

---

## 3. What Makes a Differential Equation Separable?

A first-order differential equation is called **separable** if it can be written in the form:

$$\frac{dy}{dx} = g(x) \cdot h(y)$$

The right-hand side must factor into a product of two functions: one that depends only on $x$, multiplied by one that depends only on $y$. The key insight is that we can "separate" the variables—move all $y$ expressions to one side with $dy$, and all $x$ expressions to the other side with $dx$.

The method works because we treat $\frac{dy}{dx}$ as a ratio of differentials. Rewriting the equation gives:

$$\frac{1}{h(y)}\,dy = g(x)\,dx$$

Then we integrate both sides:

$$\int \frac{1}{h(y)}\,dy = \int g(x)\,dx$$

After integrating, we solve for $y$ if possible, and apply any initial condition to find the constant.

Many students try to apply separation to equations that are not separable. Always check: can you write the right-hand side as a product $g(x) \cdot h(y)$? If $y$ appears inside a function like $\sin(y)$ or $e^y$, separation may still work—those are functions of $y$ alone. But if $x$ and $y$ appear added together, like $x + y$, separation fails and a different method is needed.

---

## 4. Worked Examples

### Worked Example 1

**Problem:** Solve the differential equation $\frac{dy}{dx} = xy$.

**Approach:** Identify that the right-hand side is $x \cdot y$, which is a product of a function of $x$ alone and a function of $y$ alone. This is separable.

**Step 1:** Write the equation and separate variables:

$$\frac{dy}{dx} = x \cdot y \quad \Rightarrow \quad \frac{1}{y}\,dy = x\,dx$$

**Step 2:** Integrate both sides:

$$\int \frac{1}{y}\,dy = \int x\,dx$$

$$\ln|y| = \frac{x^2}{2} + C$$

Notice that the constant $C$ appears on only one side. You never need two constants because they would combine into one.

**Step 3:** Solve for $y$. Exponentiate both sides:

$$|y| = e^{x^2/2 + C} = e^C \cdot e^{x^2/2}$$

Since $e^C$ is an arbitrary positive constant, and the absolute value allows a sign change, we can replace $\pm e^C$ with a single new constant $A$ (which can be any nonzero real number):

$$y = A\,e^{x^2/2}$$

This is the general solution. The constant $A$ can be positive, negative, or zero (checking $y=0$ confirms it is also a solution).

**Why this makes sense:** The equation says the rate of change is proportional to both $x$ and $y$. When $x$ is large, $y$ changes faster. The solution grows like $e^{x^2/2}$, which is even faster than exponential growth—consistent with the multiplying factor of $x$.

---

### Worked Example 2

**Problem:** Solve $\frac{dy}{dx} = \frac{2x}{y}$ with the initial condition $y(0) = 3$.

**Approach:** This is separable: $g(x) = 2x$ and $h(y) = \frac{1}{y}$. Multiply both sides by $y\,dx$ to separate.

**Step 1:** Separate variables:

$$y\,dy = 2x\,dx$$

**Step 2:** Integrate:

$$\int y\,dy = \int 2x\,dx$$

$$\frac{y^2}{2} = x^2 + C$$

**Step 3:** Multiply by $2$:

$$y^2 = 2x^2 + 2C$$

Let $K = 2C$ (a new constant):

$$y^2 = 2x^2 + K$$

**Step 4:** Apply the initial condition $y(0) = 3$:

$$3^2 = 2(0)^2 + K \quad \Rightarrow \quad 9 = K$$

**Step 5:** The equation becomes $y^2 = 2x^2 + 9$. Taking the square root gives $y = \pm\sqrt{2x^2 + 9}$. Because $y(0) = 3$ is positive, we take the positive root:

$$y = \sqrt{2x^2 + 9}$$

A common mistake is forgetting the $\pm$ sign and not using the initial condition to choose the correct branch. Always check the sign of $y$ at the initial point.

**Why this makes sense:** As $x$ grows large, $y \approx \sqrt{2}|x|$, so the function grows roughly linearly. The initial value determines which branch of the square root to use.

---

### Worked Example 3

**Problem:** Solve $\frac{dy}{dx} = y\cos x$ with $y(0) = 2$.

**Approach:** The right-hand side is $y \cdot \cos x$, clearly separable.

**Step 1:** Separate variables:

$$\frac{1}{y}\,dy = \cos x\,dx$$

**Step 2:** Integrate:

$$\ln|y| = \sin x + C$$

**Step 3:** Exponentiate:

$$|y| = e^{\sin x + C} = e^C \cdot e^{\sin x}$$

Let $A = \pm e^C$:

$$y = A e^{\sin x}$$

**Step 4:** Apply $y(0) = 2$:

$$2 = A e^{\sin 0} = A e^0 = A$$

So $A = 2$ and the particular solution is $y = 2e^{\sin x}$.

**Why this makes sense:** The function grows and shrinks between $2e^{-1} \approx 0.74$ and $2e^1 \approx 5.44$ as $\sin x$ oscillates, which matches the intuition that $\cos x$ drives alternating growth and decay.

---

### Worked Example 4 — Exponential Growth

**Problem:** A population $P(t)$ grows at a rate proportional to its current size: $\frac{dP}{dt} = kP$, where $k$ is a constant. The initial population is $P(0) = P_0$. Find the formula for $P(t)$.

**Approach:** This is separable with $g(t) = k$ and $h(P) = P$.

**Step 1:** Separate:

$$\frac{1}{P}\,dP = k\,dt$$

**Step 2:** Integrate:

$$\ln|P| = kt + C$$

**Step 3:** Exponentiate:

$$P = A e^{kt}$$

**Step 4:** Apply $P(0) = P_0$: $P_0 = A e^0 = A$, so $A = P_0$.

$$P(t) = P_0 e^{kt}$$

If $k > 0$, the population grows exponentially. If $k < 0$, it decays exponentially. This formula underpins models of bacterial growth, radioactive decay, compound interest, and many other phenomena.

**Why this makes sense:** Exponential growth means the larger the population, the faster it grows—a positive feedback loop captured perfectly by $\frac{dP}{dt} = kP$.

---

### Worked Example 5 — Implicit Solution

**Problem:** Solve $\frac{dy}{dx} = \frac{x}{y^2 + 1}$.

**Approach:** The right-hand side factors as $x \cdot \frac{1}{y^2+1}$, so this is separable.

**Step 1:** Separate:

$$(y^2 + 1)\,dy = x\,dx$$

**Step 2:** Integrate:

$$\frac{y^3}{3} + y = \frac{x^2}{2} + C$$

At this point, we cannot easily solve for $y$ in terms of $x$ using elementary functions. That is acceptable. We leave the solution in **implicit form**: an equation relating $x$ and $y$ that defines the solution curve.

**Why this makes sense:** Not every differential equation yields a nice explicit formula for $y$. The implicit form still defines a valid relationship between $x$ and $y$, and you can use it to find specific values or analyze the behavior of solutions.

---

## Practice Problems

**Problem 1**
Solve the differential equation $\frac{dy}{dx} = 3x^2 \cdot y$. Write the general solution.

**Problem 2**
Solve the differential equation with the given initial condition: $\frac{dy}{dx} = \frac{x}{y}$, with $y(2) = 4$.

**Problem 3**
Solve the differential equation $\frac{dy}{dx} = \frac{y}{x}$ with the initial condition $y(1) = 5$.

**Problem 4**
A radioactive substance decays at a rate proportional to its mass. Let the mass at time $t$ (measured in days) be $m(t)$ grams. Initially the mass is $100$ grams, and after $5$ days the mass is $80$ grams. Find the mass after $10$ days.

**Problem 5 (IB-style)**
Consider the differential equation $\frac{dy}{dx} = y^2 \sin x$ with the initial condition $y(0) = 1$.

(a) Show that the differential equation is separable. [1 mark]

(b) Find the particular solution to the differential equation, giving $y$ explicitly in terms of $x$. [5 marks]

(c) State the domain of the solution. [1 mark]

---

## Answers

**Answer 1**
The equation is $\frac{dy}{dx} = 3x^2 \cdot y$. Here $g(x) = 3x^2$ and $h(y) = y$, so the equation is separable.

Separate: $\frac{1}{y}\,dy = 3x^2\,dx$.

Integrate both sides: $\ln|y| = x^3 + C$.

Solve for $y$: $|y| = e^{x^3+C} = e^C e^{x^3}$, so $y = A e^{x^3}$ where $A$ is an arbitrary constant (which can be positive, negative, or zero).

The general solution is $y = A e^{x^3}$.

---

**Answer 2**
The equation is $\frac{dy}{dx} = \frac{x}{y}$. Separate variables by multiplying both sides by $y\,dx$: $y\,dy = x\,dx$.

Integrate both sides: $\frac{y^2}{2} = \frac{x^2}{2} + C$.

Multiply by $2$: $y^2 = x^2 + 2C$. Let $K = 2C$, so $y^2 = x^2 + K$.

Apply the initial condition $y(2) = 4$: $4^2 = 2^2 + K$, giving $16 = 4 + K$, so $K = 12$.

Thus $y^2 = x^2 + 12$. Since $y(2) = 4 > 0$, we take the positive square root: $y = \sqrt{x^2 + 12}$.

A common mistake is to forget the $\pm$ sign when taking the square root. Always use the initial condition to determine which branch is correct.

---

**Answer 3**
The equation is $\frac{dy}{dx} = \frac{y}{x}$. Separate: $\frac{1}{y}\,dy = \frac{1}{x}\,dx$.

Integrate: $\ln|y| = \ln|x| + C$.

This can be rewritten as $\ln|y| = \ln|x| + \ln(e^C) = \ln(e^C |x|)$, so $|y| = e^C |x|$.

Let $A = \pm e^C$: $y = A x$.

Apply $y(1) = 5$: $5 = A \cdot 1$, so $A = 5$. The particular solution is $y = 5x$.

Note that this solution is a straight line through the origin. The differential equation $\frac{dy}{dx} = \frac{y}{x}$ says the slope at any point equals the ratio $y/x$, which is exactly what straight lines through the origin satisfy.

---

**Answer 4**
The decay is modeled by $\frac{dm}{dt} = -km$, where $k > 0$ is the decay constant. The negative sign indicates that the mass decreases over time.

Separate: $\frac{1}{m}\,dm = -k\,dt$. Integrate: $\ln|m| = -kt + C$. Exponentiate: $m = A e^{-kt}$.

Apply $m(0) = 100$: $100 = A e^0 = A$, so $m(t) = 100 e^{-kt}$.

Apply $m(5) = 80$: $80 = 100 e^{-5k}$, so $e^{-5k} = 0.8$. Taking the natural log: $-5k = \ln(0.8)$, so $k = -\frac{\ln(0.8)}{5}$.

For the mass after $10$ days, substitute $t = 10$:

$m(10) = 100 e^{-10k} = 100 \left(e^{-5k}\right)^2 = 100 \times (0.8)^2 = 100 \times 0.64 = 64$ grams.

The mass after $10$ days is $64$ grams. Notice that we did not need to compute $k$ explicitly—using the fact that $e^{-10k} = (e^{-5k})^2$ allowed us to use the given $80$-gram datum directly.

---

**Answer 5 (IB-style)**

**(a)** The right-hand side is $y^2 \sin x$, which can be written as $(\sin x) \cdot (y^2)$. This is a product of a function of $x$ alone, $g(x) = \sin x$, and a function of $y$ alone, $h(y) = y^2$. Therefore the differential equation is separable. [1 mark]

**(b)** Separate variables: $\frac{1}{y^2}\,dy = \sin x\,dx$.

Integrate both sides: $\int y^{-2}\,dy = \int \sin x\,dx$.

$-y^{-1} = -\cos x + C$, which simplifies to $-\frac{1}{y} = -\cos x + C$.

Multiply by $-1$: $\frac{1}{y} = \cos x - C$.

Apply the initial condition $y(0) = 1$: $\frac{1}{1} = \cos 0 - C$, so $1 = 1 - C$, giving $C = 0$.

Thus $\frac{1}{y} = \cos x$, and the particular solution is $y = \frac{1}{\cos x} = \sec x$. [5 marks]

A common error is mishandling the constant when applying the initial condition. The equation after integration is $-\frac{1}{y} = -\cos x + C$, and substituting $y=1, x=0$ gives $-1 = -1 + C$, so $C = 0$. Another common error is losing the negative sign when integrating $y^{-2}$; the integral is $-y^{-1}$, not $y^{-1}$.

**(c)** The solution is $y = \sec x$, which is defined when $\cos x \neq 0$. This means $x \neq \frac{\pi}{2} + n\pi$ for any integer $n$. Since the initial condition is at $x = 0$, the domain containing the initial point is $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$. [1 mark]
