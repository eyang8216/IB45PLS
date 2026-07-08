# Lesson 6: Logarithmic Integrals and Trigonometric Integrals

## Part 1: Logarithmic Integrals

### What Is a Logarithmic Integral and Why Does It Matter?

You already know from basic calculus that the derivative of $\ln x$ is $\frac{1}{x}$. Reversing this relationship gives one of the most fundamental integration formulas: $\int \frac{1}{x}\,dx = \ln|x| + C$. The absolute value is necessary because the domain of $\ln x$ is only positive $x$, but $\frac{1}{x}$ is defined for negative $x$ as well.

However, many integrals we encounter have denominators that are not simply $x$ but are linear expressions like $3x + 2$ or $5 - 2x$. Recognizing these as logarithmic forms—and handling the constant factors correctly—is an essential skill for integration. These integrals appear whenever we integrate rational functions after partial fraction decomposition, and they are the building blocks of more advanced techniques.

### The Fundamental Formula for Linear Denominators

When the denominator is a linear expression $ax + b$ (where $a$ and $b$ are constants and $a \neq 0$), the integral follows a straightforward pattern:

$$\int \frac{1}{ax + b}\,dx = \frac{1}{a}\ln|ax + b| + C$$

The factor $\frac{1}{a}$ is the part that students most often forget. Here is why it exists. We can verify the formula by using the substitution $u = ax + b$. Then $du = a\,dx$, which means $dx = \frac{du}{a}$. Substituting:

$$\int \frac{1}{ax + b}\,dx = \int \frac{1}{u} \cdot \frac{du}{a} = \frac{1}{a}\int \frac{1}{u}\,du = \frac{1}{a}\ln|u| + C = \frac{1}{a}\ln|ax + b| + C$$

The factor $\frac{1}{a}$ comes from the $dx = \frac{du}{a}$ step. If you forget it, you are effectively claiming that the derivative of $\ln|ax + b|$ is $\frac{1}{ax + b}$, but the chain rule tells us the derivative is actually $\frac{a}{ax + b}$.

### When the Numerator Is the Derivative of the Denominator

A particularly elegant pattern arises when we recognize that the integral has the form $\int \frac{f'(x)}{f(x)}\,dx$. In this case, the answer is simply $\ln|f(x)| + C$, with no extra constant factor. This is because the substitution $u = f(x)$ gives $du = f'(x)\,dx$ exactly, so the integral becomes $\int \frac{1}{u}\,du = \ln|u| + C$.

For example, in $\int \frac{2x}{x^2 + 1}\,dx$, the numerator $2x$ is exactly the derivative of the denominator $x^2 + 1$. The integral is therefore $\ln|x^2 + 1| + C$. Since $x^2 + 1$ is always positive, the absolute value bars can be dropped: $\ln(x^2 + 1) + C$.

A common misconception: many students see a denominator and automatically apply the $\frac{1}{a}\ln|ax+b|$ formula without checking whether the numerator matches the derivative of the denominator. If the numerator is $2x$ and the denominator is $x^2 + 1$, the answer is not $\frac{1}{2x}\ln|x^2+1|$—that makes no sense because the factor $\frac{1}{a}$ only applies when the denominator is linear and the numerator is a constant.

### Worked Examples for Logarithmic Integrals

**Example 1:** Evaluate $\displaystyle \int \frac{1}{3x + 2}\,dx$.

The denominator is linear with $a = 3$, so the factor is $\frac{1}{3}$:

$$\int \frac{1}{3x + 2}\,dx = \frac{1}{3}\ln|3x + 2| + C$$

**Example 2:** Evaluate $\displaystyle \int \frac{5}{2x - 1}\,dx$.

The constant $5$ can be pulled outside the integral. The denominator is linear with $a = 2$:

$$\int \frac{5}{2x - 1}\,dx = 5\int \frac{1}{2x - 1}\,dx = 5 \cdot \frac{1}{2}\ln|2x - 1| + C = \frac{5}{2}\ln|2x - 1| + C$$

**Example 3:** Evaluate $\displaystyle \int \frac{2x}{x^2 + 1}\,dx$.

The derivative of $x^2 + 1$ is $2x$, which is exactly the numerator. This matches the pattern $\int \frac{f'(x)}{f(x)}\,dx$:

$$\int \frac{2x}{x^2 + 1}\,dx = \ln(x^2 + 1) + C$$

No extra factor is needed because the substitution $u = x^2 + 1$, $du = 2x\,dx$ is exact.

**Example 4:** Evaluate $\displaystyle \int \frac{x}{x^2 + 4}\,dx$.

The derivative of $x^2 + 4$ is $2x$, but the numerator is only $x$. We need to adjust by multiplying and dividing by $2$:

$$\int \frac{x}{x^2 + 4}\,dx = \frac{1}{2}\int \frac{2x}{x^2 + 4}\,dx = \frac{1}{2}\ln(x^2 + 4) + C$$

The factor $\frac{1}{2}$ compensates for the fact that the numerator is half of the derivative of the denominator.

---

## Part 2: Trigonometric Integrals

### Standard Results You Should Know

Derivatives of the six trigonometric functions give six integration formulas. These are the direct reversals of differentiation rules:

$$\int \sin x\,dx = -\cos x + C$$
$$\int \cos x\,dx = \sin x + C$$
$$\int \sec^2 x\,dx = \tan x + C$$
$$\int \csc^2 x\,dx = -\cot x + C$$
$$\int \sec x \tan x\,dx = \sec x + C$$
$$\int \csc x \cot x\,dx = -\csc x + C$$

A common error is forgetting the negative sign in $\int \sin x\,dx = -\cos x$. This happens because the derivative of $\cos x$ is $-\sin x$, so the sign flips when integrating.

### Three Important Integrals That Are Less Obvious

#### The Integral of $\tan x$

The tangent function is defined as $\tan x = \frac{\sin x}{\cos x}$. We can rewrite the integral:

$$\int \tan x\,dx = \int \frac{\sin x}{\cos x}\,dx$$

The derivative of $\cos x$ is $-\sin x$. The numerator $\sin x$ is the negative of the derivative of the denominator. To use the pattern $\int \frac{f'(x)}{f(x)}\,dx$, we need the numerator to exactly match the derivative:

$$\int \frac{\sin x}{\cos x}\,dx = -\int \frac{-\sin x}{\cos x}\,dx = -\ln|\cos x| + C$$

Since $-\ln|\cos x| = \ln|(\cos x)^{-1}| = \ln|\sec x|$, we can also write:

$$\int \tan x\,dx = \ln|\sec x| + C$$

The absolute value bars are necessary because $\sec x$ can be negative.

#### The Integral of $\sec x$

This integral requires a clever algebraic manipulation. Multiply the numerator and denominator by $(\sec x + \tan x)$:

$$\int \sec x\,dx = \int \frac{\sec x(\sec x + \tan x)}{\sec x + \tan x}\,dx = \int \frac{\sec^2 x + \sec x \tan x}{\sec x + \tan x}\,dx$$

Now observe the denominator: its derivative is $\sec x \tan x + \sec^2 x$, which is exactly the numerator. So this fits the pattern $\int \frac{f'(x)}{f(x)}\,dx$:

$$\int \sec x\,dx = \ln|\sec x + \tan x| + C$$

This is a formula worth memorizing because the derivation, while instructive, is not something most people would invent on an exam.

#### The Integral of $\csc x$

A similar trick works for $\csc x$. Multiply numerator and denominator by $(\csc x - \cot x)$:

$$\int \csc x\,dx = \ln|\csc x - \cot x| + C$$

---

## Part 3: Integrating Powers of Sine and Cosine

### The Half-Angle Formulas for $\sin^2 x$ and $\cos^2 x$

You cannot integrate $\sin^2 x$ directly using the basic formulas—the integral of $\sin^2 x$ is not $-\frac{1}{2}\cos^2 x$ or any similarly simple expression. The reason is that the chain rule would produce extra factors. Instead, we use the **half-angle formulas** (also called power-reduction identities), which come from the double-angle formula for cosine:

$$\sin^2 x = \frac{1 - \cos(2x)}{2}$$
$$\cos^2 x = \frac{1 + \cos(2x)}{2}$$

These identities convert a squared trigonometric function into a form we can integrate using basic techniques.

### Worked Example: $\int \sin^2 x\,dx$

**Problem:** Evaluate $\displaystyle \int \sin^2 x\,dx$.

**Approach:** To solve this, we replace $\sin^2 x$ with the half-angle identity $\frac{1 - \cos(2x)}{2}$.

**Step-by-step working:**

$$\int \sin^2 x\,dx = \int \frac{1 - \cos(2x)}{2}\,dx = \frac{1}{2}\int (1 - \cos(2x))\,dx$$
$$= \frac{1}{2}\left(x - \frac{1}{2}\sin(2x)\right) + C$$
$$= \frac{x}{2} - \frac{\sin(2x)}{4} + C$$

**Why this makes sense:** The answer contains an $x$ term, which tells us the integral grows linearly on average. This makes sense because $\sin^2 x$ oscillates between $0$ and $1$, so its accumulated area grows at an average rate of $\frac{1}{2}$ per unit of $x$.

### Worked Example: $\int \cos^2(3x)\,dx$

**Problem:** Evaluate $\displaystyle \int \cos^2(3x)\,dx$.

**Approach:** To solve this, we use $\cos^2(3x) = \frac{1 + \cos(6x)}{2}$, because the argument doubles from $3x$ to $6x$.

**Step-by-step working:**

$$\int \cos^2(3x)\,dx = \int \frac{1 + \cos(6x)}{2}\,dx = \frac{1}{2}\int (1 + \cos(6x))\,dx$$
$$= \frac{1}{2}\left(x + \frac{1}{6}\sin(6x)\right) + C$$
$$= \frac{x}{2} + \frac{\sin(6x)}{12} + C$$

The $\frac{1}{6}$ factor comes from integrating $\cos(6x)$: the integral of $\cos(kx)$ is $\frac{1}{k}\sin(kx)$.

### Worked Example: Integrating an Odd Power of Sine

**Problem:** Evaluate $\displaystyle \int \sin^3 x\,dx$.

**Approach:** To solve this, we cannot use the half-angle formula directly because the power is odd, not even. Instead, we separate one factor of $\sin x$ and convert the remaining $\sin^2 x$ using the Pythagorean identity $\sin^2 x = 1 - \cos^2 x$.

**Step-by-step working:**

$$\int \sin^3 x\,dx = \int \sin^2 x \cdot \sin x\,dx = \int (1 - \cos^2 x)\sin x\,dx$$

Now use the substitution $u = \cos x$, so $du = -\sin x\,dx$, which means $\sin x\,dx = -du$:

$$= \int (1 - u^2)(-du) = \int (u^2 - 1)\,du = \frac{u^3}{3} - u + C$$

Substitute back $u = \cos x$:

$$= \frac{\cos^3 x}{3} - \cos x + C$$

**Why this makes sense:** This technique works for any odd power of $\sin x$ or $\cos x$: peel off one factor to serve as the $du$ part of a substitution, and convert the remaining even power using the Pythagorean identity.

---

## Practice Problems

### Problem 1
Evaluate the indefinite integral $\displaystyle \int \frac{1}{5x - 3}\,dx$.

### Problem 2
Evaluate the indefinite integral $\displaystyle \int \frac{4}{2x + 7}\,dx$.

### Problem 3
Evaluate the indefinite integral $\displaystyle \int \frac{3x^2}{x^3 + 8}\,dx$.

### Problem 4
Evaluate the indefinite integral $\displaystyle \int \tan(2x)\,dx$.

### Problem 5
Evaluate the indefinite integral $\displaystyle \int \sin^2(2x)\,dx$.

### Problem 6
Evaluate the definite integral $\displaystyle \int_0^{\pi} \cos^2 x\,dx$.

---

## Answers

### Answer 1

The denominator is linear with $a = 5$, so the integral is $\frac{1}{5}\ln|5x - 3| + C$. The absolute value is necessary because $5x - 3$ can be negative (when $x < \frac{3}{5}$), and the logarithm is only defined for positive arguments. A common mistake is to forget the $\frac{1}{5}$ factor. You can check your answer by differentiating: the derivative of $\frac{1}{5}\ln|5x - 3|$ is $\frac{1}{5} \cdot \frac{5}{5x - 3} = \frac{1}{5x - 3}$, which is correct.

### Answer 2

Factor out the constant $4$: $\int \frac{4}{2x+7}\,dx = 4\int \frac{1}{2x+7}\,dx$. The denominator is linear with $a = 2$, so the inner integral is $\frac{1}{2}\ln|2x+7|$. Multiplying by $4$: $4 \cdot \frac{1}{2}\ln|2x+7| + C = 2\ln|2x+7| + C$. Notice that the constants combine: $\frac{4}{2} = 2$.

### Answer 3

The derivative of the denominator $x^3 + 8$ is $3x^2$, which is exactly the numerator. This matches the pattern $\int \frac{f'(x)}{f(x)}\,dx$, so the integral is $\ln|x^3 + 8| + C$. No extra constant factor is needed because the numerator and the derivative of the denominator match perfectly. A common error is trying to use the linear denominator formula here; that formula only applies when the denominator is of the form $ax + b$, not a cubic.

### Answer 4

Rewrite $\tan(2x) = \frac{\sin(2x)}{\cos(2x)}$. Let $u = \cos(2x)$, so $du = -2\sin(2x)dx$, meaning $\sin(2x)dx = -\frac{du}{2}$. Then $\int \tan(2x)dx = \int \frac{\sin(2x)}{\cos(2x)}dx = \int \frac{1}{u}\left(-\frac{du}{2}\right) = -\frac{1}{2}\ln|u| + C = -\frac{1}{2}\ln|\cos(2x)| + C = \frac{1}{2}\ln|\sec(2x)| + C$. Note that we can also write the answer directly using the formula $\int \tan(kx)dx = \frac{1}{k}\ln|\sec(kx)| + C$, which generalizes the basic $\tan x$ integral.

### Answer 5

Use the half-angle identity: $\sin^2(2x) = \frac{1 - \cos(4x)}{2}$. Then $\int \sin^2(2x)dx = \frac{1}{2}\int (1 - \cos(4x))dx = \frac{1}{2}\left(x - \frac{1}{4}\sin(4x)\right) + C = \frac{x}{2} - \frac{\sin(4x)}{8} + C$. The $\frac{1}{4}$ factor inside the parentheses comes from integrating $\cos(4x)$, and the $\frac{1}{2}$ outside gives the final coefficient of $\frac{1}{8}$ for the sine term.

### Answer 6

Using the half-angle identity: $\cos^2 x = \frac{1 + \cos(2x)}{2}$. So $\int \cos^2 x\,dx = \frac{1}{2}\int (1 + \cos(2x))dx = \frac{x}{2} + \frac{\sin(2x)}{4} + C$. For the definite integral from $0$ to $\pi$: $\left[\frac{x}{2} + \frac{\sin(2x)}{4}\right]_0^\pi = \left(\frac{\pi}{2} + \frac{\sin(2\pi)}{4}\right) - \left(0 + \frac{\sin(0)}{4}\right) = \frac{\pi}{2} + 0 - 0 = \frac{\pi}{2}$. The sine terms vanish at both limits because $\sin(2\pi) = 0$ and $\sin(0) = 0$. The result $\frac{\pi}{2}$ is the average value of $\cos^2 x$ ($\frac{1}{2}$) multiplied by the length of the interval ($\pi$).

---

## Key Takeaways

1. For $\int \frac{1}{ax + b}\,dx$, the answer is $\frac{1}{a}\ln|ax + b| + C$. The $\frac{1}{a}$ factor comes from the chain rule in reverse. Forgetting it is the most common error in logarithmic integration.
2. When the numerator is exactly the derivative of the denominator, $\int \frac{f'(x)}{f(x)}\,dx = \ln|f(x)| + C$, with no extra factor.
3. Memorize $\int \tan x\,dx = \ln|\sec x| + C$ and $\int \sec x\,dx = \ln|\sec x + \tan x| + C$. These appear regularly in more advanced problems.
4. For $\sin^2 x$ and $\cos^2 x$, always use the half-angle formulas. There is no simpler way to integrate squared trigonometric functions.
5. For odd powers of $\sin x$ or $\cos x$, save one factor for the $du$ of a substitution and convert the remaining even power using $\sin^2 x + \cos^2 x = 1$.

