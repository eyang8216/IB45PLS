# Lesson 7: Partial Fractions

## What Are Partial Fractions and Why Do They Matter?

A **rational function** is a fraction whose numerator and denominator are both polynomials. For example, $\frac{1}{x^2 - 1}$ and $\frac{2x+1}{(x-1)(x+2)}$ are rational functions. We often need to integrate rational functions, but most of them cannot be integrated using a single simple rule.

The technique of **partial fractions** breaks a complicated rational function into a sum of simpler fractions that we already know how to integrate—typically fractions with linear denominators that integrate to logarithms. The name "partial fractions" comes from the idea of decomposing a single fraction into its partial (component) fractions.

For instance, instead of trying to integrate $\frac{1}{x^2 - 1}$ directly, we can discover that:

$$\frac{1}{x^2 - 1} = \frac{1/2}{x - 1} - \frac{1/2}{x + 1}$$

Each of these two smaller fractions integrates to a natural logarithm. The integral of the original rational function is then simply a sum of logarithms.

This technique is essential because rational functions appear throughout calculus: in integration, in solving differential equations, in Laplace transforms, and in analyzing the behavior of systems. Without partial fractions, many of these problems would be intractable.

## When to Use Partial Fractions

The method applies when three conditions are met:

1. The integrand is a rational function—a fraction of polynomials.
2. The denominator can be factored into linear factors (like $x - a$) or irreducible quadratic factors (like $x^2 + 1$, which has no real roots).
3. The degree of the numerator is strictly less than the degree of the denominator. If it is not, we must perform polynomial long division first.

## The Core Case: Distinct Linear Factors

The simplest and most common case is when the denominator factors into distinct linear factors—factors of the form $(x - a)$ where each root $a$ is different. In this case, the decomposition takes the form:

$$\frac{P(x)}{(x - a)(x - b)(x - c)} = \frac{A}{x - a} + \frac{B}{x - b} + \frac{C}{x - c}$$

Here $A$, $B$, and $C$ are constants (numbers) that we must determine. The numerator $P(x)$ is a polynomial whose degree is less than the number of linear factors.

Finding the constants $A$, $B$, $C$ is the main task. There are two methods, and the substitution method (plugging in the roots) is usually much faster than equating coefficients.

## Step-by-Step Method

1. **Check the degrees.** If the numerator degree is greater than or equal to the denominator degree, perform polynomial long division first and apply partial fractions to the remainder term.
2. **Factor the denominator** completely into linear and irreducible quadratic factors.
3. **Write the decomposition form** with an unknown constant over each factor.
4. **Multiply both sides** by the original denominator to clear all fractions. This leaves a polynomial equation.
5. **Solve for the constants.** The fastest approach: substitute each root of the denominator (the values of $x$ that make each factor zero) into the polynomial equation. Each substitution makes all but one constant vanish. For any remaining constants, expand and equate coefficients.
6. **Integrate each partial fraction.** For linear denominators, each term integrates to a logarithm.

---

## Worked Examples

### Example 1: Two Distinct Linear Factors

**Problem:** Evaluate $\displaystyle \int \frac{1}{x^2 - 1}\,dx$.

**Approach:** To solve this, we first factor the denominator as $(x-1)(x+1)$. Since the numerator has degree $0$ and the denominator has degree $2$, the degree condition is satisfied. We set up the decomposition with unknown constants and solve.

**Step-by-step working:**

The denominator factors: $x^2 - 1 = (x-1)(x+1)$. Write:

$$\frac{1}{(x-1)(x+1)} = \frac{A}{x-1} + \frac{B}{x+1}$$

Multiply both sides by $(x-1)(x+1)$ to clear denominators:

$$1 = A(x+1) + B(x-1)$$

This equation must be true for all values of $x$. The clever move is to choose values of $x$ that make one of the terms vanish. When $x = 1$, the term $B(x-1)$ becomes $B(0) = 0$, so only $A$ remains:

$$x = 1: \quad 1 = A(1+1) = 2A \implies A = \frac{1}{2}$$

When $x = -1$, the term $A(x+1)$ becomes $A(0) = 0$, so only $B$ remains:

$$x = -1: \quad 1 = B(-1-1) = B(-2) \implies B = -\frac{1}{2}$$

Now substitute $A$ and $B$ back and integrate:

$$\int \frac{1}{x^2 - 1}\,dx = \int \left(\frac{1/2}{x-1} - \frac{1/2}{x+1}\right)dx$$
$$= \frac{1}{2}\ln|x-1| - \frac{1}{2}\ln|x+1| + C$$
$$= \frac{1}{2}\ln\left|\frac{x-1}{x+1}\right| + C$$

**Why this makes sense:** The two logarithms combine into a single logarithm of a quotient by the property $\ln a - \ln b = \ln(a/b)$. The absolute values are essential because the argument of a logarithm must be positive, but $x-1$ and $x+1$ can be negative for different ranges of $x$.

---

### Example 2: Three Distinct Linear Factors

**Problem:** Evaluate $\displaystyle \int \frac{2x+1}{(x-1)(x+2)(x-3)}\,dx$.

**Approach:** To solve this, we set up the decomposition with three constants—one for each linear factor—and use the substitution method.

**Step-by-step working:**

Write the decomposition:

$$\frac{2x+1}{(x-1)(x+2)(x-3)} = \frac{A}{x-1} + \frac{B}{x+2} + \frac{C}{x-3}$$

Multiply by the denominator:

$$2x+1 = A(x+2)(x-3) + B(x-1)(x-3) + C(x-1)(x+2)$$

Substitute each root:

$x = 1$: $2(1)+1 = A(1+2)(1-3) \implies 3 = A(3)(-2) = -6A \implies A = -\frac{1}{2}$

$x = -2$: $2(-2)+1 = B(-2-1)(-2-3) \implies -3 = B(-3)(-5) = 15B \implies B = -\frac{1}{5}$

$x = 3$: $2(3)+1 = C(3-1)(3+2) \implies 7 = C(2)(5) = 10C \implies C = \frac{7}{10}$

Now integrate:

$$\int \frac{2x+1}{(x-1)(x+2)(x-3)}\,dx = \int \left(-\frac{1/2}{x-1} - \frac{1/5}{x+2} + \frac{7/10}{x-3}\right)dx$$
$$= -\frac{1}{2}\ln|x-1| - \frac{1}{5}\ln|x+2| + \frac{7}{10}\ln|x-3| + C$$

**Why this makes sense:** The constants $A$, $B$, $C$ sum to $-\frac{1}{2} + (-\frac{1}{5}) + \frac{7}{10} = -\frac{5}{10} - \frac{2}{10} + \frac{7}{10} = 0$. This reflects the fact that the numerator $2x+1$ has lower degree than the denominator, which imposes constraints on the partial fraction constants.

---

### Example 3: A Repeated Linear Factor

**Problem:** Evaluate $\displaystyle \int \frac{x}{(x-1)^2}\,dx$.

**Approach:** To solve this, we note that the factor $(x-1)$ appears twice (it has multiplicity 2). When a linear factor is repeated, the decomposition must include all lower powers of that factor.

**Step-by-step working:**

For a repeated factor $(x-1)^2$, the decomposition is:

$$\frac{x}{(x-1)^2} = \frac{A}{x-1} + \frac{B}{(x-1)^2}$$

Multiply by $(x-1)^2$:

$$x = A(x-1) + B$$

Substitute $x = 1$: $1 = A(0) + B \implies B = 1$.

To find $A$, we can either substitute another value (say $x = 0$: $0 = A(-1) + 1 \implies A = 1$) or expand and equate coefficients: $x = Ax + (B - A)$. Comparing coefficients of $x$: $1 = A$, so $A = 1$.

Now integrate. The first term is a logarithm; the second is a power:

$$\int \frac{x}{(x-1)^2}\,dx = \int \left(\frac{1}{x-1} + \frac{1}{(x-1)^2}\right)dx$$
$$= \ln|x-1| + \int (x-1)^{-2}\,dx$$
$$= \ln|x-1| - (x-1)^{-1} + C$$
$$= \ln|x-1| - \frac{1}{x-1} + C$$

**Why this makes sense:** The integral contains both a logarithmic term (from the $\frac{A}{x-1}$ part) and an algebraic term (from the $\frac{B}{(x-1)^2}$ part). This mixture is characteristic of repeated factors.

---

### Example 4: Numerator Degree Too High

**Problem:** Evaluate $\displaystyle \int \frac{x^2}{x-2}\,dx$.

**Approach:** To solve this, we first check degrees. The numerator has degree $2$ and the denominator has degree $1$. Since the numerator degree is not less than the denominator degree, we must perform polynomial long division before applying partial fractions.

**Step-by-step working:**

Divide $x^2$ by $x-2$:

$$x^2 \div (x-2) = x + 2 + \frac{4}{x-2}$$

To see why this is correct: $(x-2)(x+2) = x^2 - 4$, and we need to add $4$ to get $x^2$. So $\frac{x^2}{x-2} = \frac{x^2 - 4 + 4}{x-2} = \frac{(x-2)(x+2)}{x-2} + \frac{4}{x-2} = x + 2 + \frac{4}{x-2}$.

Now integrate:

$$\int \frac{x^2}{x-2}\,dx = \int \left(x + 2 + \frac{4}{x-2}\right)dx$$
$$= \frac{x^2}{2} + 2x + 4\ln|x-2| + C$$

**Why this makes sense:** The result has a polynomial part $\frac{x^2}{2} + 2x$ from the quotient of the division, and a logarithmic part $4\ln|x-2|$ from the remainder. This is the general pattern when the numerator degree is too high.

---

## Practice Problems

### Problem 1
Evaluate the indefinite integral $\displaystyle \int \frac{1}{x^2 - 4}\,dx$.

### Problem 2
Evaluate the indefinite integral $\displaystyle \int \frac{1}{x^2 + 5x + 6}\,dx$.

### Problem 3
Evaluate the indefinite integral $\displaystyle \int \frac{x+3}{x^2 - x - 2}\,dx$.

### Problem 4
Evaluate the indefinite integral $\displaystyle \int \frac{2x-1}{(x+1)(x-2)(x+3)}\,dx$.

### Problem 5
Evaluate the indefinite integral $\displaystyle \int \frac{x^2 + 1}{x^2 - 1}\,dx$. (Check the degrees carefully before setting up the decomposition.)

---

## Answers

### Answer 1

The denominator factors as $(x-2)(x+2)$. Set up: $\frac{1}{(x-2)(x+2)} = \frac{A}{x-2} + \frac{B}{x+2}$. Multiply: $1 = A(x+2) + B(x-2)$. Substitute $x=2$: $1 = 4A \implies A = \frac{1}{4}$. Substitute $x=-2$: $1 = B(-4) \implies B = -\frac{1}{4}$. The integral is $\int \left(\frac{1/4}{x-2} - \frac{1/4}{x+2}\right)dx = \frac{1}{4}\ln|x-2| - \frac{1}{4}\ln|x+2| + C = \frac{1}{4}\ln\left|\frac{x-2}{x+2}\right| + C$. A common mistake is to factor $x^2-4$ as $(x-4)(x+1)$ instead of the difference of squares $(x-2)(x+2)$.

### Answer 2

Factor: $x^2 + 5x + 6 = (x+2)(x+3)$. Set up: $\frac{1}{(x+2)(x+3)} = \frac{A}{x+2} + \frac{B}{x+3}$. Multiply: $1 = A(x+3) + B(x+2)$. Substitute $x=-2$: $1 = A(1) \implies A = 1$. Substitute $x=-3$: $1 = B(-1) \implies B = -1$. The integral is $\int \left(\frac{1}{x+2} - \frac{1}{x+3}\right)dx = \ln|x+2| - \ln|x+3| + C = \ln\left|\frac{x+2}{x+3}\right| + C$.

### Answer 3

Factor: $x^2 - x - 2 = (x-2)(x+1)$. Set up: $\frac{x+3}{(x-2)(x+1)} = \frac{A}{x-2} + \frac{B}{x+1}$. Multiply: $x+3 = A(x+1) + B(x-2)$. Substitute $x=2$: $5 = 3A \implies A = \frac{5}{3}$. Substitute $x=-1$: $2 = B(-3) \implies B = -\frac{2}{3}$. The integral is $\int \left(\frac{5/3}{x-2} - \frac{2/3}{x+1}\right)dx = \frac{5}{3}\ln|x-2| - \frac{2}{3}\ln|x+1| + C$.

### Answer 4

Set up: $\frac{2x-1}{(x+1)(x-2)(x+3)} = \frac{A}{x+1} + \frac{B}{x-2} + \frac{C}{x+3}$. Multiply: $2x-1 = A(x-2)(x+3) + B(x+1)(x+3) + C(x+1)(x-2)$. Substitute $x=-1$: $-3 = A(-3)(2) = -6A \implies A = \frac{1}{2}$. Substitute $x=2$: $3 = B(3)(5) = 15B \implies B = \frac{1}{5}$. Substitute $x=-3$: $-7 = C(-2)(-5) = 10C \implies C = -\frac{7}{10}$. The integral is $\int \left(\frac{1/2}{x+1} + \frac{1/5}{x-2} - \frac{7/10}{x+3}\right)dx = \frac{1}{2}\ln|x+1| + \frac{1}{5}\ln|x-2| - \frac{7}{10}\ln|x+3| + C$. A common error is mixing up which factor each constant corresponds to; double-check by tracing each substitution back to the decomposition.

### Answer 5

The numerator and denominator both have degree $2$. Since the numerator degree is not less than the denominator degree, we perform long division first: $\frac{x^2+1}{x^2-1} = 1 + \frac{2}{x^2-1}$. Now decompose $\frac{2}{x^2-1} = \frac{2}{(x-1)(x+1)} = \frac{A}{x-1} + \frac{B}{x+1}$. Multiply: $2 = A(x+1) + B(x-1)$. Substitute $x=1$: $2 = 2A \implies A = 1$. Substitute $x=-1$: $2 = B(-2) \implies B = -1$. So $\frac{x^2+1}{x^2-1} = 1 + \frac{1}{x-1} - \frac{1}{x+1}$. Integrating: $\int \frac{x^2+1}{x^2-1}\,dx = \int \left(1 + \frac{1}{x-1} - \frac{1}{x+1}\right)dx = x + \ln|x-1| - \ln|x+1| + C = x + \ln\left|\frac{x-1}{x+1}\right| + C$. Many students skip the long division step and try to decompose $\frac{x^2+1}{x^2-1}$ directly, which does not work because the decomposition form assumes the numerator degree is lower.

---

## Key Takeaways

1. Partial fractions decomposes a rational function into simpler fractions that integrate to logarithms (for linear factors).
2. Always check that the numerator degree is less than the denominator degree. If it is not, do polynomial long division first.
3. The substitution method—plugging in the roots of the denominator—is almost always faster than equating coefficients.
4. For repeated linear factors like $(x-a)^n$, include all lower powers: $\frac{A_1}{x-a} + \frac{A_2}{(x-a)^2} + \cdots + \frac{A_n}{(x-a)^n}$.
5. Every partial fraction integral reduces to logarithms and possibly power terms. This is the power of the technique: it turns an intimidating rational function into a sum of simple, familiar integrals.

