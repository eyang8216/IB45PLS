# Lesson 18: Homogeneous Differential Equations and Applications

## What Is a Homogeneous Differential Equation and Why Does It Matter?

In Lesson 17 we learned how to solve linear differential equations using an integrating factor. But not all differential equations are linear. Some have $y^2$ terms, or products like $xy$, or fractions with both $x$ and $y$ in the numerator and denominator. Many of these are **homogeneous**, and they have their own special method of solution.

A first-order differential equation is called **homogeneous** (in the sense used in the IB syllabus) if it can be rewritten so that the right-hand side depends only on the **ratio** of $y$ to $x$. In other words, it can be expressed as:

$$\boxed{\frac{dy}{dx} = f\!\left(\frac{y}{x}\right)}$$

Think of it this way: if you scale both $x$ and $y$ by the same factor, the value of $\frac{dy}{dx}$ does not change. The only thing that matters is the proportion between $y$ and $x$, not their individual sizes.

Why does this matter? Many real-world relationships — especially in geometry and physics — depend on proportions rather than absolute quantities. And mathematically, the homogeneity property unlocks a powerful substitution that turns the DE into a separable equation, which we already know how to solve.

---

## How to Recognise a Homogeneous DE

To test whether a differential equation is homogeneous, replace $x$ with $kx$ and $y$ with $ky$ everywhere on the right-hand side. If every factor of $k$ cancels out completely, the equation is homogeneous.

**Example:** Test $\displaystyle\frac{dy}{dx} = \frac{x^2 + y^2}{xy}$.

Replace $x \to kx$ and $y \to ky$:

$$\frac{(kx)^2 + (ky)^2}{(kx)(ky)} = \frac{k^2 x^2 + k^2 y^2}{k^2 xy} = \frac{k^2(x^2 + y^2)}{k^2(xy)} = \frac{x^2 + y^2}{xy}$$

The $k^2$ cancels. The right-hand side is unchanged. This DE is homogeneous.

Furthermore, we can actually rewrite the right-hand side as a function of $y/x$ alone:

$$\frac{x^2 + y^2}{xy} = \frac{x}{y} + \frac{y}{x} = \frac{1}{(y/x)} + \frac{y}{x}$$

This confirms the form $f(y/x)$.

---

## The Substitution: $v = \frac{y}{x}$

The standard method for solving a homogeneous DE $\frac{dy}{dx} = f(y/x)$ is to introduce a new variable $v$ defined by:

$$\boxed{v = \frac{y}{x}}$$

This can also be written as $y = vx$.

Now we need to express $\frac{dy}{dx}$ in terms of $v$ and $x$. Since $y = vx$, we use the **product rule** (because both $v$ and $x$ depend on $x$):

$$\boxed{\frac{dy}{dx} = v + x\frac{dv}{dx}}$$

This is the crucial step. The derivative of $vx$ with respect to $x$ is $v \cdot 1 + x \cdot \frac{dv}{dx}$.

When we substitute $y = vx$ and $\frac{dy}{dx} = v + x\frac{dv}{dx}$ into the original DE, the $v$ terms often simplify, and we are left with an equation that is **separable** — meaning all the $v$ terms can go on one side and all the $x$ terms on the other.

---

## The Step-by-Step Recipe

1. **Verify** the DE is homogeneous: rewrite the right-hand side as a function of $y/x$ (or confirm via the $kx$, $ky$ test).
2. **Substitute** $v = y/x$, which means $y = vx$ and $\frac{dy}{dx} = v + x\frac{dv}{dx}$.
3. **Replace** in the DE: $v + x\frac{dv}{dx} = f(v)$.
4. **Rearrange** to isolate the derivative: $x\frac{dv}{dx} = f(v) - v$.
5. **Separate** the variables: $\frac{dv}{f(v) - v} = \frac{dx}{x}$.
6. **Integrate** both sides.
7. **Back-substitute** $v = y/x$ to get the solution in terms of $x$ and $y$.
8. If an **initial condition** is given, apply it to find the constant.

---

## Worked Examples

### Worked Example 1: A Simple Homogeneous DE

**Solve $\displaystyle\frac{dy}{dx} = \frac{x + y}{x}$.**

**Approach:** The right side can be split: $\frac{x+y}{x} = 1 + \frac{y}{x}$. This is clearly a function of $y/x$ alone, so the DE is homogeneous. Use the substitution $v = y/x$.

**Step 1:** Verify homogeneity. The right-hand side is $1 + \frac{y}{x} = f(v)$ with $v = y/x$. Confirmed.

**Step 2:** Substitute $y = vx$ and $\frac{dy}{dx} = v + x\frac{dv}{dx}$:

$$v + x\frac{dv}{dx} = 1 + v$$

**Step 3:** The $v$ terms cancel on both sides:

$$x\frac{dv}{dx} = 1$$

**Step 4:** Separate:

$$dv = \frac{dx}{x}$$

**Step 5:** Integrate both sides:

$$\int dv = \int \frac{dx}{x} \quad\Longrightarrow\quad v = \ln|x| + C$$

**Step 6:** Back-substitute $v = \frac{y}{x}$:

$$\frac{y}{x} = \ln|x| + C$$

**Step 7:** Multiply by $x$:

$$y = x\ln|x| + Cx$$

**Answer: $y = x\ln|x| + Cx$**

---

### Worked Example 2: A DE with Quadratic Terms

**Solve $\displaystyle\frac{dy}{dx} = \frac{x^2 + y^2}{2xy}$.**

**Approach:** Divide the numerator and denominator by $x^2$ to express the right-hand side as a function of $y/x$:

$$\frac{x^2 + y^2}{2xy} = \frac{1 + (y/x)^2}{2(y/x)} = \frac{1 + v^2}{2v}$$

**Step 1:** Homogeneous confirmed. The right side is $f(v) = \frac{1+v^2}{2v}$.

**Step 2:** Substitute:

$$v + x\frac{dv}{dx} = \frac{1 + v^2}{2v}$$

**Step 3:** Isolate $x\frac{dv}{dx}$:

$$x\frac{dv}{dx} = \frac{1 + v^2}{2v} - v = \frac{1 + v^2 - 2v^2}{2v} = \frac{1 - v^2}{2v}$$

**Step 4:** Separate:

$$\frac{2v}{1 - v^2}\,dv = \frac{dx}{x}$$

**Step 5:** Integrate. For the left side, use the substitution $u = 1 - v^2$, so $du = -2v\,dv$:

$$\int \frac{2v}{1 - v^2}\,dv = -\int \frac{1}{u}\,du = -\ln|u| = -\ln|1 - v^2|$$

The right side: $\int \frac{dx}{x} = \ln|x| + C$.

So: $-\ln|1 - v^2| = \ln|x| + C$.

Multiply by $-1$: $\ln|1 - v^2| = -\ln|x| - C$.

Let $C' = -C$. Then:

$$\ln|1 - v^2| = -\ln|x| + C'$$

Exponentiate: $|1 - v^2| = e^{C'} \cdot \frac{1}{|x|} = \frac{A}{|x|}$, where $A = e^{C'}$ is a positive constant. We can absorb the sign by letting $A$ be any nonzero constant and write:

$$1 - v^2 = \frac{A}{x}$$

**Step 6:** Back-substitute $v = y/x$:

$$1 - \frac{y^2}{x^2} = \frac{A}{x}$$

Multiply through by $x^2$:

$$x^2 - y^2 = Ax$$

**Answer: $x^2 - y^2 = Ax$, or equivalently $y^2 = x^2 - Ax$**

---

### Worked Example 3: Homogeneous DE with an Initial Condition

**Solve $\displaystyle\frac{dy}{dx} = \frac{y}{x} + \frac{x}{y}$, given that $y(1) = 2$.**

**Approach:** The right side is already expressed as a function of $v = y/x$: $f(v) = v + \frac{1}{v}$.

**Step 1:** Homogeneous confirmed.

**Step 2:** Substitute:

$$v + x\frac{dv}{dx} = v + \frac{1}{v}$$

**Step 3:** The $v$ terms cancel:

$$x\frac{dv}{dx} = \frac{1}{v}$$

**Step 4:** Separate:

$$v\,dv = \frac{dx}{x}$$

**Step 5:** Integrate:

$$\int v\,dv = \int \frac{dx}{x} \quad\Longrightarrow\quad \frac{v^2}{2} = \ln|x| + C$$

**Step 6:** Back-substitute $v = y/x$:

$$\frac{y^2}{2x^2} = \ln|x| + C$$

Multiply by $2x^2$:

$$y^2 = 2x^2(\ln|x| + C)$$

**Step 7:** Apply $y(1) = 2$. Substitute $x = 1$, $y = 2$:

$$4 = 2(1)^2(\ln 1 + C) = 2(0 + C) = 2C \quad\Longrightarrow\quad C = 2$$

Therefore:

$$y^2 = 2x^2(\ln|x| + 2)$$

Since $y(1) = 2$ is positive, we take the positive square root:

$$y = x\sqrt{2\ln|x| + 4}$$

**Why this makes sense:** At $x = 1$, $\ln 1 = 0$, so $y = 1 \times \sqrt{4} = 2$, which satisfies the initial condition.

---

## Choosing the Right Method: A Decision Guide

When you see a first-order differential equation, ask these questions in order:

1. **Is it separable?** Can you write it as $\frac{dy}{dx} = g(x) \cdot h(y)$? If yes, separate variables and integrate (covered in Lesson 15).

2. **Is it linear?** Can you write it as $\frac{dy}{dx} + P(x)y = Q(x)$? If yes, use the integrating factor method (Lesson 17).

3. **Is it homogeneous?** Can you write it as $\frac{dy}{dx} = f(y/x)$? If yes, use the substitution $v = y/x$ (this lesson).

4. **If none of the above apply**, you may need to use Euler's method for numerical approximation (Lesson 16), or try to rewrite the equation into one of the above forms.

Some equations are **both** linear and separable. In that case, either method works — pick the one that seems easier.

---

## Applications of Differential Equations

Differential equations are not just abstract puzzles. They model real systems. Here are two important applications.

### Application 1: Newton's Law of Cooling

Newton's Law of Cooling describes how a warm object cools down in a cooler environment. The rate at which the temperature drops is proportional to the difference between the object's temperature $T$ and the ambient (room) temperature $T_a$.

$$\boxed{\frac{dT}{dt} = -k(T - T_a)}$$

Here $k > 0$ is a constant (the cooling constant) that depends on the object and its surroundings. The minus sign means that when $T > T_a$, the temperature decreases.

This equation is both linear and separable. Let us solve it using the integrating factor method as a review.

Rewrite in standard form: $\frac{dT}{dt} + kT = kT_a$.

Here $P(t) = k$ (a constant) and $Q(t) = kT_a$. The integrating factor is $\mu = e^{\int k\,dt} = e^{kt}$.

Multiply: $e^{kt}\frac{dT}{dt} + k e^{kt}T = kT_a e^{kt}$.

Left side: $\frac{d}{dt}(e^{kt}T) = kT_a e^{kt}$.

Integrate: $e^{kt}T = kT_a \int e^{kt}\,dt = kT_a \cdot \frac{1}{k}e^{kt} + C = T_a e^{kt} + C$.

Divide by $e^{kt}$: $T = T_a + C e^{-kt}$.

If the initial temperature is $T(0) = T_0$, then $T_0 = T_a + C$, so $C = T_0 - T_a$. The full solution is:

$$\boxed{T(t) = T_a + (T_0 - T_a)e^{-kt}}$$

This formula tells you the temperature at any time $t$. As $t \to \infty$, the exponential dies away, and the temperature approaches $T_a$ — the object eventually reaches room temperature.

---

#### Worked Application: Cooling Coffee

A cup of coffee at 90°C is placed in a room at 20°C. After 5 minutes, its temperature has dropped to 60°C. Find the temperature after 15 minutes.

**Step 1:** Write the general solution. $T_a = 20$, $T_0 = 90$, so:

$$T(t) = 20 + (90 - 20)e^{-kt} = 20 + 70e^{-kt}$$

**Step 2:** Use the data point to find $k$. At $t = 5$, $T = 60$:

$$60 = 20 + 70e^{-5k} \quad\Longrightarrow\quad 40 = 70e^{-5k} \quad\Longrightarrow\quad e^{-5k} = \frac{40}{70} = \frac{4}{7}$$

**Step 3:** Find the temperature at $t = 15$. There is a clever trick: $e^{-15k} = (e^{-5k})^3$, so:

$$T(15) = 20 + 70 \times \left(\frac{4}{7}\right)^3 = 20 + 70 \times \frac{64}{343}$$

Compute $70 \times \frac{64}{343} = \frac{4480}{343} \approx 13.06$.

$$T(15) \approx 20 + 13.06 = 33.06$$

**Answer: Approximately 33.1°C**

---

### Application 2: Mixing Problems

Consider a tank that initially holds 100 litres of water with 10 kg of salt dissolved in it. A salt-water solution with a concentration of 0.2 kg per litre flows into the tank at a rate of 5 litres per minute. The mixture is kept well stirred and flows out at the same rate of 5 litres per minute. How much salt is in the tank at time $t$?

The key idea: the rate of change of salt equals the rate salt enters minus the rate salt leaves.

**Rate in:** (concentration of inflow) × (flow rate) = $0.2 \times 5 = 1$ kg/min.

**Rate out:** At time $t$, let $S(t)$ be the amount of salt in the tank (in kg). The volume stays constant at 100 L (because inflow equals outflow). The concentration in the tank is $\frac{S(t)}{100}$ kg/L. Salt leaves at: $\frac{S}{100} \times 5 = \frac{S}{20}$ kg/min.

Therefore the differential equation is:

$$\frac{dS}{dt} = 1 - \frac{S}{20}$$

Rewrite in standard form: $\frac{dS}{dt} + \frac{1}{20}S = 1$.

Now solve: $P(t) = \frac{1}{20}$, so $\mu = e^{\int (1/20)\,dt} = e^{t/20}$.

Multiply: $e^{t/20}\frac{dS}{dt} + \frac{1}{20}e^{t/20}S = e^{t/20}$.

Left side: $\frac{d}{dt}(e^{t/20}S) = e^{t/20}$.

Integrate: $e^{t/20}S = \int e^{t/20}\,dt = 20e^{t/20} + C$.

Divide: $S = 20 + C e^{-t/20}$.

Initial condition: $S(0) = 10$. So $10 = 20 + C$, which gives $C = -10$.

$$\boxed{S(t) = 20 - 10e^{-t/20}}$$

As time goes on ($t \to \infty$), the exponential term vanishes, and the amount of salt approaches $20$ kg. This matches the inflow concentration times the tank volume: $0.2 \times 100 = 20$ kg.

---

## Summary

| Type of DE | Form | Method |
|---|---|---|
| **Separable** | $\frac{dy}{dx} = g(x)h(y)$ | Separate variables and integrate |
| **Linear** | $\frac{dy}{dx} + P(x)y = Q(x)$ | Integrating factor $\mu = e^{\int P\,dx}$ |
| **Homogeneous** | $\frac{dy}{dx} = f(y/x)$ | Substitute $v = y/x$ |
| **Applications** | Real-world models | Identify the type, then apply its method |

---

## Practice Problems

**Problem 1**

Solve the homogeneous differential equation $\displaystyle\frac{dy}{dx} = \frac{y}{x} + \frac{x}{y}$. Write your answer as a relationship between $y$ and $x$ (you do not need to solve for $y$ explicitly).

**Problem 2**

Solve the homogeneous differential equation $\displaystyle\frac{dy}{dx} = \frac{2xy}{x^2 - y^2}$. Start by dividing the numerator and denominator by $x^2$ to express the right-hand side as a function of $v = y/x$.

**Problem 3**

Identify the type of the differential equation $\displaystyle\frac{dy}{dx} = \frac{x}{y}$ and solve it using the most appropriate method. (Hint: try separation of variables.)

**Problem 4**

Identify the type of the differential equation $\displaystyle\frac{dy}{dx} + 2y = e^{-x}$, with $y(0) = 1$, and solve it using the most appropriate method.

**Problem 5** (IB-style — Newton's Law of Cooling)

A body at 100°C is placed in a room maintained at a constant temperature of 25°C. After exactly 10 minutes, the body has cooled to 70°C.

(a) Write down the differential equation that models this situation, and give its general solution. State clearly what each symbol represents. [2 marks]

(b) Show that the cooling constant $k$ satisfies $e^{-10k} = 0.6$, and hence find the value of $k$ correct to four decimal places. [3 marks]

(c) Find the temperature of the body after 20 minutes. [2 marks]

(d) Determine how many minutes (to the nearest minute) it takes for the body to cool to 30°C. [2 marks]

**Problem 6** (Mixing Application)

A tank initially contains 50 litres of pure water (so the initial amount of salt is 0 kg). A salt solution with a concentration of 0.1 kg per litre flows into the tank at a rate of 2 litres per minute. The mixture is kept well stirred and flows out at the same rate of 2 litres per minute. Let $S(t)$ be the amount of salt (in kg) in the tank at time $t$ minutes.

(a) Write a differential equation for $S(t)$ by considering the rates at which salt enters and leaves the tank. [2 marks]

(b) Solve the differential equation to find $S(t)$. [4 marks]

(c) What amount of salt does the tank approach after a very long time? Explain why this value makes physical sense. [2 marks]

---

## Answers

**Answer 1**

The right side is $\frac{y}{x} + \frac{x}{y} = v + \frac{1}{v}$ with $v = y/x$. The DE is homogeneous.

Substitute: $v + x\frac{dv}{dx} = v + \frac{1}{v}$.

The $v$ terms cancel: $x\frac{dv}{dx} = \frac{1}{v}$.

Separate: $v\,dv = \frac{dx}{x}$.

Integrate: $\frac{v^2}{2} = \ln|x| + C$.

Back-substitute $v = y/x$: $\frac{y^2}{2x^2} = \ln|x| + C$.

Multiply by $2x^2$: $y^2 = 2x^2(\ln|x| + C)$.

(Common pitfall: forgetting to back-substitute $v = y/x$ at the end and leaving the answer in terms of $v$.)

---

**Answer 2**

Divide numerator and denominator by $x^2$:

$$\frac{dy}{dx} = \frac{2(y/x)}{1 - (y/x)^2} = \frac{2v}{1 - v^2}$$

where $v = y/x$. The DE is homogeneous.

Substitute: $v + x\frac{dv}{dx} = \frac{2v}{1 - v^2}$.

Isolate: $x\frac{dv}{dx} = \frac{2v}{1 - v^2} - v = \frac{2v - v(1 - v^2)}{1 - v^2} = \frac{2v - v + v^3}{1 - v^2} = \frac{v + v^3}{1 - v^2} = \frac{v(1 + v^2)}{1 - v^2}$.

Separate: $\frac{1 - v^2}{v(1 + v^2)}\,dv = \frac{dx}{x}$.

Use partial fractions on the left side: $\frac{1 - v^2}{v(1 + v^2)} = \frac{1}{v} - \frac{2v}{1 + v^2}$.

Integrate: $\int \frac{1}{v}\,dv - \int \frac{2v}{1 + v^2}\,dv = \int \frac{dx}{x}$.

The first integral is $\ln|v|$. For the second, use $u = 1+v^2$, $du = 2v\,dv$, so $\int \frac{2v}{1+v^2}\,dv = \ln(1+v^2)$.

Thus: $\ln|v| - \ln(1 + v^2) = \ln|x| + \ln C$, where we write the constant as $\ln C$ for convenience.

Combine logs: $\ln\left|\frac{v}{1 + v^2}\right| = \ln|Cx|$.

Remove logs: $\frac{v}{1 + v^2} = Cx$.

Back-substitute $v = y/x$:

$$\frac{y/x}{1 + y^2/x^2} = Cx \quad\Longrightarrow\quad \frac{y}{x} \cdot \frac{x^2}{x^2 + y^2} = Cx \quad\Longrightarrow\quad \frac{xy}{x^2 + y^2} = Cx$$

Cancel $x$ (assuming $x \neq 0$): $\frac{y}{x^2 + y^2} = C$.

So: $y = C(x^2 + y^2)$, or equivalently $x^2 + y^2 = \frac{y}{C}$.

---

**Answer 3**

The equation $\frac{dy}{dx} = \frac{x}{y}$ can be solved by separation of variables (it is also homogeneous, but separation is quicker).

Separate: $y\,dy = x\,dx$.

Integrate: $\frac{y^2}{2} = \frac{x^2}{2} + C$.

Multiply by $2$: $y^2 = x^2 + 2C$. Since $2C$ is just another constant, we can write:

$$y^2 = x^2 + C$$

(where the $C$ here is $2C$ from the previous line — the exact name of the constant does not matter).

---

**Answer 4**

The equation $\frac{dy}{dx} + 2y = e^{-x}$ is linear, with $P(x) = 2$ and $Q(x) = e^{-x}$.

Integrating factor: $\mu = e^{\int 2\,dx} = e^{2x}$.

Multiply: $e^{2x}\frac{dy}{dx} + 2e^{2x}y = e^{2x} \cdot e^{-x} = e^x$.

Left side: $\frac{d}{dx}(e^{2x}y) = e^x$.

Integrate: $e^{2x}y = \int e^x\,dx = e^x + C$.

Divide: $y = e^{-x} + C e^{-2x}$.

Apply $y(0) = 1$: $1 = e^0 + C \cdot e^0 = 1 + C$, so $C = 0$.

Final answer: $y = e^{-x}$.

(Interesting: the solution simplifies to just $e^{-x}$, with no arbitrary constant term surviving.)

---

**Answer 5**

**(a)** Let $T(t)$ be the temperature of the body at time $t$ minutes. Let $T_a = 25$ be the ambient temperature. Newton's Law of Cooling states:

$$\frac{dT}{dt} = -k(T - 25)$$

where $k > 0$ is the cooling constant. The general solution (derived in the lesson) is:

$$T(t) = 25 + (T_0 - 25)e^{-kt}$$

where $T_0 = T(0) = 100$ is the initial temperature.

[2 marks: 1 for the correct differential equation, 1 for the general solution with symbols explained.]

**(b)** Substitute $T_0 = 100$: $T(t) = 25 + 75e^{-kt}$.

At $t = 10$, $T = 70$: $70 = 25 + 75e^{-10k}$.

$45 = 75e^{-10k}$, so $e^{-10k} = \frac{45}{75} = 0.6$.

Taking natural logs: $-10k = \ln(0.6)$, so $k = -\frac{\ln(0.6)}{10}$.

Compute: $k \approx \frac{0.5108}{10} = 0.0511$ (to four decimal places: $0.0511$).

[3 marks: 1 for setting up $T(10) = 70$, 1 for solving to get $e^{-10k} = 0.6$, 1 for the correct value of $k$.]

**(c)** At $t = 20$: $T(20) = 25 + 75e^{-20k} = 25 + 75(e^{-10k})^2 = 25 + 75(0.6)^2 = 25 + 75 \times 0.36 = 25 + 27 = 52$.

So the temperature after 20 minutes is 52°C.

[2 marks: 1 for using $e^{-20k} = (e^{-10k})^2$, 1 for the correct temperature.]

**(d)** Set $T(t) = 30$: $30 = 25 + 75e^{-kt}$, so $5 = 75e^{-kt}$ and $e^{-kt} = \frac{5}{75} = \frac{1}{15}$.

Take natural logs: $-kt = \ln(1/15) = -\ln 15$, so $t = \frac{\ln 15}{k}$.

Using $k \approx 0.05108$: $t \approx \frac{2.7081}{0.05108} \approx 53.0$.

To the nearest minute, it takes 53 minutes.

[2 marks: 1 for setting up the equation correctly, 1 for the correct time.]

---

**Answer 6**

**(a)** The volume stays constant at 50 L because the inflow rate equals the outflow rate.

Rate of salt entering: (concentration in) × (flow rate in) = $0.1 \times 2 = 0.2$ kg/min.

Rate of salt leaving: at time $t$, the concentration in the tank is $\frac{S}{50}$ kg/L. Salt leaves at rate $\frac{S}{50} \times 2 = \frac{S}{25}$ kg/min.

Therefore: $\frac{dS}{dt} = 0.2 - \frac{S}{25}$.

[2 marks: 1 for the correct "rate in", 1 for the correct "rate out" and the differential equation.]

**(b)** Write in standard form: $\frac{dS}{dt} + \frac{1}{25}S = 0.2$.

Integrating factor: $\mu = e^{\int (1/25)\,dt} = e^{t/25}$.

Multiply: $e^{t/25}\frac{dS}{dt} + \frac{1}{25}e^{t/25}S = 0.2e^{t/25}$.

Left side: $\frac{d}{dt}(e^{t/25}S) = 0.2e^{t/25}$.

Integrate: $e^{t/25}S = \int 0.2e^{t/25}\,dt = 0.2 \times 25e^{t/25} + C = 5e^{t/25} + C$.

Divide: $S = 5 + C e^{-t/25}$.

Apply $S(0) = 0$: $0 = 5 + C$, so $C = -5$.

Final answer: $S(t) = 5(1 - e^{-t/25})$.

[4 marks: 1 for standard form, 1 for the integrating factor, 1 for integration, 1 for applying initial condition.]

**(c)** As $t \to \infty$, the exponential $e^{-t/25} \to 0$, so $S(t) \to 5$ kg.

This makes physical sense because the inflow has a concentration of $0.1$ kg/L and the tank volume is $50$ L. Over a long time, the water in the tank is completely replaced by the incoming solution, so the amount of salt should be $0.1 \times 50 = 5$ kg.

[2 marks: 1 for identifying the limit, 1 for the physical explanation.]
