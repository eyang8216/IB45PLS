# Lesson 17: First-Order Linear Differential Equations and the Integrating Factor

## What Is a First-Order Linear Differential Equation and Why Does It Matter?

A **differential equation** (often shortened to DE) is an equation that involves a function and its derivatives. Differential equations describe how things change — the rate at which a population grows, the speed at which a cup of coffee cools, the flow of current in an electrical circuit. If you can solve a differential equation, you can predict how a system will behave over time.

In this lesson we focus on a particular type: the **first-order linear differential equation**. "First-order" means the equation contains only the first derivative $\frac{dy}{dx}$ (not $\frac{d^2y}{dx^2}$ or higher derivatives). "Linear" means that both $\frac{dy}{dx}$ and $y$ itself appear only to the first power — no $y^2$, no $\sin y$, no $\left(\frac{dy}{dx}\right)^3$.

These equations can always be written in **standard form**:

$$\boxed{\frac{dy}{dx} + P(x)\,y = Q(x)}$$

Here $P(x)$ and $Q(x)$ are functions that depend only on $x$. They can be constants, polynomials, trig functions, or anything else — as long as they do not involve $y$.

### Examples: Linear or Not?

| Differential Equation | Linear? | Why? |
|---|---|---|
| $\frac{dy}{dx} + 2xy = x$ | Yes | $P(x) = 2x$, $Q(x) = x$ — fits the standard form |
| $\frac{dy}{dx} + \frac{y}{x} = x^2$ | Yes | $P(x) = \frac{1}{x}$, $Q(x) = x^2$ — fits the standard form |
| $\frac{dy}{dx} = y^2$ | No | The $y^2$ term is nonlinear |
| $\frac{dy}{dx} + \sin y = x$ | No | $\sin y$ is not of the form $P(x)\,y$ |

---

## The Integrating Factor: A Clever Trick

The key to solving $\frac{dy}{dx} + P(x)y = Q(x)$ is to multiply both sides by a specially chosen function called an **integrating factor**. The integrating factor is a function of $x$, which we write as $\mu(x)$ (the Greek letter "mu"), defined by:

$$\boxed{\mu(x) = e^{\int P(x)\,dx}}$$

The integral $\int P(x)\,dx$ means we find any antiderivative of $P(x)$. For this purpose you can ignore the constant of integration $+C$ — any antiderivative will work.

### Why This Works

When we multiply the entire differential equation by $\mu(x)$, the left-hand side becomes a perfect derivative. Here is how:

The original equation is $\frac{dy}{dx} + P(x)y = Q(x)$. Multiply every term by $\mu$:

$$\mu\frac{dy}{dx} + \mu P(x) y = \mu Q(x)$$

Now, because of how we defined $\mu$, the left-hand side is exactly $\frac{d}{dx}(\mu y)$. To see why, use the product rule:

$$\frac{d}{dx}(\mu y) = \mu\frac{dy}{dx} + y\frac{d\mu}{dx}$$

But $\frac{d\mu}{dx} = \frac{d}{dx} e^{\int P\,dx} = e^{\int P\,dx} \cdot P(x) = \mu P(x)$. So the two expressions match.

This means the equation simplifies to:

$$\frac{d}{dx}(\mu y) = \mu Q(x)$$

Now we integrate both sides with respect to $x$:

$$\mu y = \int \mu Q(x)\,dx$$

And finally solve for $y$:

$$y = \frac{1}{\mu} \int \mu Q(x)\,dx$$

Many students worry about forgetting the formula, but the recipe is easier to remember than the final formula. Let us learn the recipe.

---

## The Step-by-Step Recipe

For a differential equation in the form $\frac{dy}{dx} + P(x)y = Q(x)$:

1. **Identify** $P(x)$ and $Q(x)$. Make sure the equation is in standard form first.
2. **Compute the integrating factor:** $\mu = e^{\int P(x)\,dx}$. You may drop the $+C$ in the integral.
3. **Multiply** every term of the DE by $\mu$.
4. **Recognise** that the left-hand side is now $\frac{d}{dx}(\mu y)$.
5. **Integrate** both sides with respect to $x$. The left side becomes $\mu y$. The right side is the integral of $\mu Q(x)$.
6. **Solve** for $y$ by dividing by $\mu$.
7. If the problem gives an **initial condition** (like $y(1) = 2$), substitute the $x$ and $y$ values into your solution to find the constant $C$.

---

## Worked Examples

### Worked Example 1: A Simple Constant-P Case

**Solve the differential equation $\displaystyle\frac{dy}{dx} + 2xy = x$.**

**Approach:** The equation is already in standard form. Identify $P(x)$ and $Q(x)$, find $\mu$, and follow the recipe.

**Step 1:** $P(x) = 2x$, $Q(x) = x$.

**Step 2:** Compute the integrating factor:

$$\mu = e^{\int 2x\,dx} = e^{x^2}$$

**Step 3:** Multiply the entire DE by $e^{x^2}$:

$$e^{x^2}\frac{dy}{dx} + 2x e^{x^2} y = x e^{x^2}$$

**Step 4:** The left-hand side is $\frac{d}{dx}\big(e^{x^2} y\big)$:

$$\frac{d}{dx}\big(e^{x^2} y\big) = x e^{x^2}$$

**Step 5:** Integrate both sides:

$$e^{x^2} y = \int x e^{x^2}\,dx$$

For the integral on the right, use the substitution $u = x^2$, so $du = 2x\,dx$, which means $x\,dx = \frac{du}{2}$:

$$\int x e^{x^2}\,dx = \int e^u \cdot \frac{du}{2} = \frac{1}{2}e^u = \frac{1}{2}e^{x^2}$$

So we have:

$$e^{x^2} y = \frac{1}{2}e^{x^2} + C$$

**Step 6:** Divide both sides by $e^{x^2}$:

$$y = \frac{1}{2} + C e^{-x^2}$$

**Why this makes sense:** As $x$ gets very large (positive or negative), $e^{-x^2}$ becomes extremely small, so $y$ approaches $\frac{1}{2}$. The constant term $\frac{1}{2}$ is called the steady-state solution.

---

### Worked Example 2: With the $1/x$ Function and an Initial Condition

**Solve $\displaystyle\frac{dy}{dx} + \frac{y}{x} = x^2$, given that $y(1) = 2$.**

**Approach:** Standard form with $P(x) = \frac{1}{x}$. The integrating factor will involve a logarithm.

**Step 1:** $P(x) = \frac{1}{x}$, $Q(x) = x^2$.

**Step 2:** Compute $\mu$:

$$\mu = e^{\int \frac{1}{x}\,dx} = e^{\ln|x|} = |x|$$

For $x > 0$ (a reasonable domain since the initial condition is at $x = 1$), we can drop the absolute value and use $\mu = x$.

**Step 3:** Multiply the DE by $x$:

$$x\frac{dy}{dx} + y = x^3$$

**Step 4:** The left-hand side is $\frac{d}{dx}(xy)$:

$$\frac{d}{dx}(xy) = x^3$$

**Step 5:** Integrate:

$$xy = \int x^3\,dx = \frac{x^4}{4} + C$$

**Step 6:** Solve for $y$:

$$y = \frac{x^3}{4} + \frac{C}{x}$$

**Step 7:** Apply the initial condition $y(1) = 2$. Substitute $x = 1$, $y = 2$:

$$2 = \frac{1^3}{4} + \frac{C}{1} \quad\Longrightarrow\quad 2 = \frac{1}{4} + C \quad\Longrightarrow\quad C = 2 - \frac{1}{4} = \frac{7}{4}$$

Therefore:

$$y = \frac{x^3}{4} + \frac{7}{4x}$$

**Why this makes sense:** You can check by differentiating: $\frac{dy}{dx} = \frac{3x^2}{4} - \frac{7}{4x^2}$, and $\frac{y}{x} = \frac{x^2}{4} + \frac{7}{4x^2}$. Adding them gives $\frac{3x^2}{4} + \frac{x^2}{4} = x^2$, which matches the right-hand side.

---

### Worked Example 3: A Constant-Coefficient DE

**Solve $\displaystyle\frac{dy}{dx} + 3y = 6$, with $y(0) = 5$.**

**Approach:** $P(x) = 3$ is a constant, so the integrating factor is a simple exponential.

**Step 1:** $P(x) = 3$, $Q(x) = 6$.

**Step 2:** $\mu = e^{\int 3\,dx} = e^{3x}$.

**Step 3:** Multiply:

$$e^{3x}\frac{dy}{dx} + 3e^{3x}y = 6e^{3x}$$

**Step 4:** Left side is $\frac{d}{dx}(e^{3x}y)$:

$$\frac{d}{dx}(e^{3x}y) = 6e^{3x}$$

**Step 5:** Integrate:

$$e^{3x}y = \int 6e^{3x}\,dx = 6 \cdot \frac{1}{3}e^{3x} + C = 2e^{3x} + C$$

**Step 6:** Divide by $e^{3x}$:

$$y = 2 + C e^{-3x}$$

**Step 7:** Apply $y(0) = 5$:

$$5 = 2 + C \cdot e^0 = 2 + C \quad\Longrightarrow\quad C = 3$$

Therefore:

$$y = 2 + 3e^{-3x}$$

**Why this makes sense:** As $x \to \infty$, the term $3e^{-3x}$ dies away to zero, and $y$ approaches $2$. This is the steady-state or equilibrium solution — the value $y$ settles into over time.

---

### Worked Example 4: A DE Involving Trigonometric Functions

**Solve $\displaystyle\frac{dy}{dx} - y\tan x = \sec x$, with $y(0) = 1$.**

**Approach:** First rewrite in standard form to identify $P(x)$. Note that the equation is $\frac{dy}{dx} + (-\tan x)y = \sec x$.

**Step 1:** In standard form, $P(x) = -\tan x$ and $Q(x) = \sec x$.

**Step 2:** Compute $\mu$:

$$\mu = e^{\int -\tan x\,dx}$$

The integral of $-\tan x$ is $\ln|\cos x|$ (since $\int \tan x\,dx = -\ln|\cos x|$). So:

$$\mu = e^{\ln|\cos x|} = \cos x$$

**Step 3:** Multiply the DE by $\cos x$:

$$\cos x \cdot \frac{dy}{dx} - \cos x \cdot \tan x \cdot y = \cos x \cdot \sec x$$

Now simplify. Since $\tan x = \frac{\sin x}{\cos x}$, we have $\cos x \cdot \tan x = \sin x$. And $\cos x \cdot \sec x = \cos x \cdot \frac{1}{\cos x} = 1$:

$$\cos x \frac{dy}{dx} - \sin x \cdot y = 1$$

**Step 4:** The left-hand side is $\frac{d}{dx}(\cos x \cdot y)$:

$$\frac{d}{dx}(\cos x \cdot y) = 1$$

**Step 5:** Integrate:

$$\cos x \cdot y = \int 1\,dx = x + C$$

**Step 6:** Solve for $y$:

$$y = \frac{x + C}{\cos x} = (x + C)\sec x$$

**Step 7:** Apply $y(0) = 1$:

$$1 = \frac{0 + C}{\cos 0} = \frac{C}{1} = C \quad\Longrightarrow\quad C = 1$$

Therefore:

$$y = (x + 1)\sec x$$

---

### Worked Example 5: A DE That is Both Linear and Separable

**Solve $\displaystyle\frac{dy}{dx} + y = 0$ using both separation of variables and the integrating factor method, and check that the answers agree.**

**Method 1 — Separation:** Rewrite as $\frac{dy}{dx} = -y$. Separate: $\frac{1}{y}\,dy = -dx$. Integrate: $\ln|y| = -x + C$, so $y = Ae^{-x}$ where $A = e^C$.

**Method 2 — Integrating Factor:** $P(x) = 1$, so $\mu = e^{\int 1\,dx} = e^x$. Multiply: $e^x\frac{dy}{dx} + e^x y = 0$, so $\frac{d}{dx}(e^x y) = 0$. Integrate: $e^x y = C$, so $y = C e^{-x}$.

Both methods give $y = (\text{constant}) \times e^{-x}$. The names of the constants differ ($A$ vs $C$) but the family of solutions is identical.

---

## Summary of the Recipe

1. Write the DE in standard form: $\frac{dy}{dx} + P(x)y = Q(x)$
2. Compute $\mu = e^{\int P(x)\,dx}$
3. Multiply through by $\mu$
4. The LHS becomes $\frac{d}{dx}(\mu y)$
5. Integrate: $\mu y = \int \mu Q(x)\,dx$
6. Solve for $y$
7. Apply initial condition if given

---

## Practice Problems

**Problem 1**

Solve the differential equation $\displaystyle\frac{dy}{dx} + 4y = 8$. There is no initial condition, so your answer will include an arbitrary constant $C$.

**Problem 2**

Solve the differential equation $\displaystyle\frac{dy}{dx} + \frac{2y}{x} = x$, given the initial condition $y(1) = 3$. Show all steps including the computation of the integrating factor and the application of the initial condition.

**Problem 3**

Solve $\displaystyle\frac{dy}{dx} - y = e^x$, with $y(0) = 2$. Be careful: the equation has a minus sign before $y$, so $P(x) = -1$.

**Problem 4**

Solve the differential equation $\displaystyle x\frac{dy}{dx} + y = \sin x$, subject to the condition $y(\pi) = 0$. You will need to divide by $x$ first to put the equation in standard form.

**Problem 5** (IB-style)

Consider the differential equation $\displaystyle\frac{dy}{dx} + y\cos x = \cos x$ with initial condition $y(0) = 0$.

(a) Write the equation in standard form and identify $P(x)$ and $Q(x)$. [1 mark]

(b) Find the integrating factor $\mu(x)$. [2 marks]

(c) Hence solve the differential equation, giving $y$ explicitly in terms of $x$. [4 marks]

**Problem 6**

An RL electrical circuit has the current $I(t)$ (in amperes) governed by:

$$L\frac{dI}{dt} + RI = V$$

where $L$ (inductance), $R$ (resistance), and $V$ (voltage) are positive constants. The initial current is zero: $I(0) = 0$. Solve this differential equation for $I(t)$. Write your final answer in the form $I(t) = \frac{V}{R}\left(1 - e^{-(R/L)t}\right)$.

---

## Answers

**Answer 1**

The equation is already in standard form with $P(x) = 4$ and $Q(x) = 8$.

Compute the integrating factor: $\mu = e^{\int 4\,dx} = e^{4x}$.

Multiply the DE: $e^{4x}\frac{dy}{dx} + 4e^{4x}y = 8e^{4x}$.

The left side is $\frac{d}{dx}(e^{4x}y) = 8e^{4x}$.

Integrate: $e^{4x}y = \int 8e^{4x}\,dx = 8 \cdot \frac{1}{4}e^{4x} + C = 2e^{4x} + C$.

Divide by $e^{4x}$: $y = 2 + C e^{-4x}$.

(Common pitfall: forgetting the $+C$ after integration. If you do, you only get the particular solution $y = 2$, missing the general solution.)

---

**Answer 2**

Standard form: $P(x) = \frac{2}{x}$, $Q(x) = x$.

Integrating factor: $\mu = e^{\int \frac{2}{x}\,dx} = e^{2\ln|x|} = |x|^2 = x^2$ (for $x > 0$, given $x = 1$ in the initial condition).

Multiply: $x^2\frac{dy}{dx} + 2x y = x^3$.

Left side is $\frac{d}{dx}(x^2 y) = x^3$.

Integrate: $x^2 y = \int x^3\,dx = \frac{x^4}{4} + C$.

Solve: $y = \frac{x^2}{4} + \frac{C}{x^2}$.

Apply $y(1) = 3$: $3 = \frac{1}{4} + C \implies C = \frac{11}{4}$.

Final answer: $y = \frac{x^2}{4} + \frac{11}{4x^2}$.

---

**Answer 3**

Standard form: $\frac{dy}{dx} + (-1)y = e^x$, so $P(x) = -1$, $Q(x) = e^x$.

Integrating factor: $\mu = e^{\int (-1)\,dx} = e^{-x}$.

Multiply: $e^{-x}\frac{dy}{dx} - e^{-x}y = e^{-x} \cdot e^x = 1$.

Left side: $\frac{d}{dx}(e^{-x}y) = 1$.

Integrate: $e^{-x}y = \int 1\,dx = x + C$.

Solve: $y = (x + C)e^x$.

Apply $y(0) = 2$: $2 = (0 + C) \cdot e^0 = C \implies C = 2$.

Final answer: $y = (x + 2)e^x$.

(Common pitfall: when $P(x)$ is negative, the integrating factor $e^{\int P\,dx}$ involves a negative exponent. Students sometimes forget the minus sign and write $\mu = e^x$ instead of $e^{-x}$.)

---

**Answer 4**

First, divide through by $x$ to get standard form: $\frac{dy}{dx} + \frac{y}{x} = \frac{\sin x}{x}$.

So $P(x) = \frac{1}{x}$, $Q(x) = \frac{\sin x}{x}$.

Integrating factor: $\mu = e^{\int \frac{1}{x}\,dx} = e^{\ln|x|} = x$ (for $x > 0$, valid since initial condition is at $x = \pi$).

Multiply by $x$: $x\frac{dy}{dx} + y = \sin x$.

Left side: $\frac{d}{dx}(xy) = \sin x$.

Integrate: $xy = \int \sin x\,dx = -\cos x + C$.

Solve: $y = \frac{-\cos x + C}{x}$.

Apply $y(\pi) = 0$: $0 = \frac{-\cos\pi + C}{\pi} = \frac{-(-1) + C}{\pi} = \frac{1 + C}{\pi}$.

So $1 + C = 0$ and $C = -1$.

Final answer: $y = \frac{-\cos x - 1}{x}$.

---

**Answer 5**

**(a)** The equation $\frac{dy}{dx} + y\cos x = \cos x$ is already in standard form. Identifying against $\frac{dy}{dx} + P(x)y = Q(x)$, we have $P(x) = \cos x$ and $Q(x) = \cos x$.

[1 mark: for correctly identifying both $P(x)$ and $Q(x)$.]

**(b)** The integrating factor is:

$$\mu(x) = e^{\int P(x)\,dx} = e^{\int \cos x\,dx} = e^{\sin x}$$

[2 marks: 1 for the correct integral of $\cos x$, 1 for the correct final expression for $\mu$.]

**(c)** Multiply the DE by $e^{\sin x}$:

$$e^{\sin x}\frac{dy}{dx} + e^{\sin x} y \cos x = e^{\sin x}\cos x$$

The left side is $\frac{d}{dx}(e^{\sin x} y)$, so:

$$\frac{d}{dx}(e^{\sin x} y) = e^{\sin x}\cos x$$

Integrate both sides. For the right side, note that $\int e^{\sin x}\cos x\,dx$ can be evaluated with the substitution $u = \sin x$, $du = \cos x\,dx$:

$$\int e^{\sin x}\cos x\,dx = \int e^u\,du = e^u = e^{\sin x}$$

So: $e^{\sin x} y = e^{\sin x} + C$.

Divide by $e^{\sin x}$: $y = 1 + C e^{-\sin x}$.

Apply $y(0) = 0$: $0 = 1 + C e^{-\sin 0} = 1 + C \cdot e^0 = 1 + C$, so $C = -1$.

Final answer: $y = 1 - e^{-\sin x}$.

[4 marks: 1 for multiplying by $\mu$, 1 for recognizing the LHS as a derivative, 1 for correct integration, 1 for applying the initial condition and obtaining the final answer.]

---

**Answer 6**

The equation is $L\frac{dI}{dt} + RI = V$. First put it in standard form by dividing every term by $L$:

$$\frac{dI}{dt} + \frac{R}{L}I = \frac{V}{L}$$

Now $P(t) = \frac{R}{L}$ (a constant) and $Q(t) = \frac{V}{L}$.

Compute the integrating factor: $\mu = e^{\int \frac{R}{L}\,dt} = e^{(R/L)t}$.

Multiply: $e^{(R/L)t}\frac{dI}{dt} + \frac{R}{L}e^{(R/L)t}I = \frac{V}{L}e^{(R/L)t}$.

Left side: $\frac{d}{dt}\big(e^{(R/L)t} I\big) = \frac{V}{L}e^{(R/L)t}$.

Integrate: $e^{(R/L)t} I = \int \frac{V}{L}e^{(R/L)t}\,dt = \frac{V}{L} \cdot \frac{L}{R} e^{(R/L)t} + C = \frac{V}{R}e^{(R/L)t} + C$.

Divide by $e^{(R/L)t}$: $I = \frac{V}{R} + C e^{-(R/L)t}$.

Apply $I(0) = 0$: $0 = \frac{V}{R} + C \cdot e^0 = \frac{V}{R} + C$, so $C = -\frac{V}{R}$.

Therefore:

$$I(t) = \frac{V}{R} - \frac{V}{R}e^{-(R/L)t} = \frac{V}{R}\left(1 - e^{-(R/L)t}\right)$$

As $t \to \infty$, the exponential term dies away and the current approaches the steady-state value $\frac{V}{R}$ — exactly what Ohm's law predicts for a DC circuit.
