# Lesson 5: Integration by Parts (Advanced)

## When One Round of Integration by Parts Is Not Enough

In Lesson 4, we learned how integration by parts converts the integral of a product into a simpler integral that can be evaluated immediately. However, not every product yields to a single application of the formula. There are two important scenarios where the technique must be extended.

The first scenario occurs when the integrand contains a polynomial multiplied by an exponential or trigonometric function, and the polynomial has degree greater than 1—for example, $x^2 e^x$ or $x^3 \sin x$. Each round of integration by parts reduces the degree of the polynomial by one, so we need to apply the technique repeatedly until the polynomial disappears.

The second scenario occurs when both functions in the product are "cyclical" under differentiation and integration—the classic example is $e^x \sin x$. After two rounds of integration by parts, the original integral reappears on the right-hand side. Instead of going in circles forever, we treat this as an algebraic equation and solve for the original integral.

The reason these advanced techniques matter is that integrals like $\int x^3 e^x dx$ and $\int e^x \sin x\,dx$ appear frequently in applications: Laplace transforms, Fourier analysis, damped oscillations, and quantum mechanics all involve such integrals.

## Scenario 1: Repeated Integration by Parts

When the integrand is a polynomial $x^n$ multiplied by $e^{kx}$, $\sin(kx)$, or $\cos(kx)$, the LIATE rule tells us to set $u$ equal to the polynomial term. After one round of integration by parts, the new integral contains $x^{n-1}$ instead of $x^n$. The polynomial degree drops by one. We apply integration by parts again, and again, until the polynomial term becomes a constant and then vanishes.

### Worked Example: Repeated IBP

**Problem:** Evaluate $\displaystyle \int x^2 e^x \, dx$.

**Approach:** To solve this, we set $u = x^2$ (Algebraic) and $dv = e^x dx$ (Exponential), following LIATE. After the first round, we will have an integral with $x e^x$, which requires a second round of integration by parts.

**Step-by-step working:**

**Round 1:** $u = x^2$, $dv = e^x dx$. Then $du = 2x\,dx$, $v = e^x$.

$$\int x^2 e^x dx = x^2 e^x - \int 2x e^x dx$$

The remaining integral is $\int 2x e^x dx$. We factor out the constant $2$: this equals $2\int x e^x dx$. Now we apply integration by parts a second time.

**Round 2:** For $\int x e^x dx$, set $u = x$, $dv = e^x dx$. Then $du = dx$, $v = e^x$.

$$\int x e^x dx = x e^x - \int e^x dx = x e^x - e^x$$

Now substitute this back into the expression from Round 1:

$$\int x^2 e^x dx = x^2 e^x - 2(x e^x - e^x) + C$$
$$= x^2 e^x - 2x e^x + 2e^x + C$$
$$= e^x(x^2 - 2x + 2) + C$$

**Why this makes sense:** We can verify by differentiating. Using the product rule on $e^x(x^2 - 2x + 2)$: the derivative of $e^x$ times the polynomial is $e^x(x^2 - 2x + 2)$. The derivative of the polynomial times $e^x$ is $e^x(2x - 2)$. Adding these: $e^x(x^2 - 2x + 2 + 2x - 2) = e^x(x^2) = x^2 e^x$. The answer is correct. Notice the pattern: the coefficients alternate in sign and the polynomial inside the parentheses is related to the derivatives of $x^2$.

---

## Scenario 2: The Loop Trick (Integration by Parts with Cyclical Functions)

When the integrand is the product of an exponential and a trigonometric function—for example, $e^x \sin x$ or $e^{2x} \cos(3x)$—something remarkable happens. Neither function changes its type under differentiation or integration: $e^x$ stays $e^x$, and $\sin x$ cycles between $\sin x$ and $\cos x$. After two rounds of integration by parts, the original integral reappears on the right-hand side, creating an equation that we can solve algebraically.

Many students panic when they see the original integral reappear and think they have made a mistake. This is actually the sign that the loop trick is working correctly.

### Worked Example: The Loop Trick

**Problem:** Evaluate $\displaystyle \int e^x \sin x \, dx$.

**Approach:** To solve this, we apply integration by parts twice. LIATE does not give a decisive preference here (both Trigonometric and Exponential are in the list), but a useful strategy is to let $u$ be the trigonometric function in both rounds so that the pattern stays consistent.

**Step-by-step working:**

Let $I = \int e^x \sin x\,dx$. This name $I$ is just notation to make the algebra cleaner.

**Round 1:** Set $u = \sin x$, $dv = e^x dx$. Then $du = \cos x\,dx$, $v = e^x$.

$$I = e^x \sin x - \int e^x \cos x\,dx \quad \text{(Equation 1)}$$

**Round 2:** Now evaluate $\int e^x \cos x\,dx$. Set $u = \cos x$, $dv = e^x dx$. Then $du = -\sin x\,dx$, $v = e^x$.

$$\int e^x \cos x\,dx = e^x \cos x - \int e^x (-\sin x)\,dx = e^x \cos x + \int e^x \sin x\,dx$$

But $\int e^x \sin x\,dx$ is exactly our original $I$! So:

$$\int e^x \cos x\,dx = e^x \cos x + I \quad \text{(Equation 2)}$$

Now substitute Equation 2 into Equation 1:

$$I = e^x \sin x - (e^x \cos x + I)$$
$$I = e^x \sin x - e^x \cos x - I$$

Add $I$ to both sides:

$$2I = e^x \sin x - e^x \cos x$$
$$2I = e^x(\sin x - \cos x)$$

Divide by 2:

$$I = \frac{1}{2}e^x(\sin x - \cos x) + C$$

**Why this makes sense:** The answer is a combination of $\sin x$ and $\cos x$ multiplied by $e^x$, which is exactly what we would expect—integrating a product of $e^x$ and $\sin x$ should produce something of the same form. The factor $\frac{1}{2}$ comes from solving the algebraic equation.

**A common mistake:** Students often forget to add the constant $C$ at the end. Even though we manipulated the equation with $I$ on both sides, $I$ represents an indefinite integral, so the final answer must include $+C$. Another common mistake is forgetting to divide by the coefficient (2 in this case) after adding $I$ to both sides.

---

## Scenario 3: The Tabular Method (A Shortcut)

For integrals of the form $\int (\text{polynomial}) \times (\text{exponential or trigonometric})\,dx$, the tabular method organizes repeated integration by parts into a compact table. This method is much faster than writing out each round of integration by parts separately.

Here is how to construct the table:

1. Create three columns: Sign, $u$ (differentiate), and $dv$ (integrate).
2. Put the polynomial in the $u$ column and differentiate it repeatedly until you reach $0$.
3. Put the exponential or trigonometric function in the $dv$ column and integrate it repeatedly the same number of times.
4. The signs alternate: $+$, $-$, $+$, $-$, starting with $+$.
5. Multiply diagonally (sign × $u$ term × $dv$ term directly to the right and down one row) and add all the products.

### Worked Example: Tabular Method

**Problem:** Evaluate $\displaystyle \int x^3 \sin x \, dx$.

**Approach:** To solve this, we use the tabular method. The polynomial $x^3$ goes in the differentiate column, and $\sin x$ goes in the integrate column.

**Step-by-step working:**

| Sign | $u$ (differentiate) | $dv$ (integrate) |
|:---|:---|:---|
| $+$ | $x^3$ | $\sin x$ |
| $-$ | $3x^2$ | $-\cos x$ |
| $+$ | $6x$ | $-\sin x$ |
| $-$ | $6$ | $\cos x$ |
| $+$ | $0$ | $\sin x$ |

Now multiply along the diagonals (sign × $u$ row × $dv$ from the row below):

The first diagonal: $(+)(x^3)(-\cos x) = -x^3\cos x$
The second diagonal: $(-)(3x^2)(-\sin x) = +3x^2\sin x$
The third diagonal: $(+)(6x)(\cos x) = +6x\cos x$
The fourth diagonal: $(-)(6)(\sin x) = -6\sin x$

The fifth row has $u = 0$, so it contributes nothing.

Adding all these:

$$\int x^3 \sin x\,dx = -x^3\cos x + 3x^2\sin x + 6x\cos x - 6\sin x + C$$

**Why this makes sense:** The highest power term is $x^3$ attached to $\cos x$, and the signs alternate with each row. This pattern is typical: when you differentiate a cubic polynomial, you get three nonzero derivatives followed by zero.

---

## Practice Problems

### Problem 1
Evaluate the indefinite integral $\displaystyle \int x^2 \sin x \, dx$ using repeated integration by parts.

### Problem 2
Evaluate the indefinite integral $\displaystyle \int e^{2x} \cos x \, dx$ using the loop trick.

### Problem 3
Evaluate the indefinite integral $\displaystyle \int e^x \cos(3x) \, dx$ using the loop trick.

### Problem 4
Evaluate the indefinite integral $\displaystyle \int x^3 e^{-x} \, dx$ using the tabular method.

### Problem 5
Evaluate the indefinite integral $\displaystyle \int e^{-x} \sin(2x) \, dx$ using the loop trick.

---

## Answers

### Answer 1

We apply repeated integration by parts. Round 1: $u = x^2$, $dv = \sin x\,dx$, so $du = 2x\,dx$, $v = -\cos x$. This gives $\int x^2\sin x\,dx = -x^2\cos x + \int 2x\cos x\,dx$. Round 2 for $\int 2x\cos x\,dx$: $u = 2x$, $dv = \cos x\,dx$, so $du = 2\,dx$, $v = \sin x$. This gives $\int 2x\cos x\,dx = 2x\sin x - \int 2\sin x\,dx = 2x\sin x + 2\cos x$. Combining: $\int x^2\sin x\,dx = -x^2\cos x + 2x\sin x + 2\cos x + C$. A common mistake is getting the signs wrong on the trigonometric integrals: $\int \sin x\,dx = -\cos x$ (negative) and $\int \cos x\,dx = \sin x$ (positive).

### Answer 2

Let $I = \int e^{2x}\cos x\,dx$. Round 1: $u = \cos x$, $dv = e^{2x}dx$, so $du = -\sin x\,dx$, $v = \frac{1}{2}e^{2x}$. Then $I = \frac{1}{2}e^{2x}\cos x - \int \frac{1}{2}e^{2x}(-\sin x)dx = \frac{1}{2}e^{2x}\cos x + \frac{1}{2}\int e^{2x}\sin x\,dx$. Round 2 for $\int e^{2x}\sin x\,dx$: $u = \sin x$, $dv = e^{2x}dx$, so $du = \cos x\,dx$, $v = \frac{1}{2}e^{2x}$. Then $\int e^{2x}\sin x\,dx = \frac{1}{2}e^{2x}\sin x - \frac{1}{2}\int e^{2x}\cos x\,dx = \frac{1}{2}e^{2x}\sin x - \frac{1}{2}I$. Substitute back: $I = \frac{1}{2}e^{2x}\cos x + \frac{1}{2}\left(\frac{1}{2}e^{2x}\sin x - \frac{1}{2}I\right) = \frac{1}{2}e^{2x}\cos x + \frac{1}{4}e^{2x}\sin x - \frac{1}{4}I$. Bring $\frac{1}{4}I$ to the left: $I + \frac{1}{4}I = \frac{5}{4}I = \frac{1}{2}e^{2x}\cos x + \frac{1}{4}e^{2x}\sin x$. Multiply by $\frac{4}{5}$: $I = \frac{e^{2x}}{5}(2\cos x + \sin x) + C$. A common pitfall is mishandling the fractions when solving for $I$. Be systematic: collect all $I$ terms on one side first.

### Answer 3

Let $I = \int e^x\cos(3x)dx$. Round 1: $u = \cos(3x)$, $dv = e^x dx$, so $du = -3\sin(3x)dx$, $v = e^x$. Then $I = e^x\cos(3x) + 3\int e^x\sin(3x)dx$. Round 2 for $\int e^x\sin(3x)dx$: $u = \sin(3x)$, $dv = e^x dx$, so $du = 3\cos(3x)dx$, $v = e^x$. Then $\int e^x\sin(3x)dx = e^x\sin(3x) - 3\int e^x\cos(3x)dx = e^x\sin(3x) - 3I$. Substitute: $I = e^x\cos(3x) + 3(e^x\sin(3x) - 3I) = e^x\cos(3x) + 3e^x\sin(3x) - 9I$. So $I + 9I = 10I = e^x(\cos(3x) + 3\sin(3x))$. Therefore $I = \frac{e^x}{10}(\cos(3x) + 3\sin(3x)) + C$.

### Answer 4

Using the tabular method:

| Sign | Differentiate | Integrate |
|:---|:---|:---|
| $+$ | $x^3$ | $e^{-x}$ |
| $-$ | $3x^2$ | $-e^{-x}$ |
| $+$ | $6x$ | $e^{-x}$ |
| $-$ | $6$ | $-e^{-x}$ |
| $+$ | $0$ | $e^{-x}$ |

Diagonal products: $(+)(x^3)(-e^{-x}) = -x^3e^{-x}$, $(-)(3x^2)(e^{-x}) = -3x^2e^{-x}$, $(+)(6x)(-e^{-x}) = -6xe^{-x}$, $(-)(6)(e^{-x}) = -6e^{-x}$. Adding: $\int x^3 e^{-x}dx = -x^3e^{-x} - 3x^2e^{-x} - 6xe^{-x} - 6e^{-x} + C = -e^{-x}(x^3 + 3x^2 + 6x + 6) + C$. All signs are negative because the sign column and the integrate column both contribute sign information. Check carefully row by row.

### Answer 5

Let $I = \int e^{-x}\sin(2x)dx$. Round 1: $u = \sin(2x)$, $dv = e^{-x}dx$, so $du = 2\cos(2x)dx$, $v = -e^{-x}$. Then $I = -e^{-x}\sin(2x) + 2\int e^{-x}\cos(2x)dx$. Round 2 for $\int e^{-x}\cos(2x)dx$: $u = \cos(2x)$, $dv = e^{-x}dx$, so $du = -2\sin(2x)dx$, $v = -e^{-x}$. Then $\int e^{-x}\cos(2x)dx = -e^{-x}\cos(2x) - 2\int e^{-x}\sin(2x)dx = -e^{-x}\cos(2x) - 2I$. Substitute: $I = -e^{-x}\sin(2x) + 2(-e^{-x}\cos(2x) - 2I) = -e^{-x}\sin(2x) - 2e^{-x}\cos(2x) - 4I$. So $I + 4I = 5I = -e^{-x}(\sin(2x) + 2\cos(2x))$. Therefore $I = -\frac{e^{-x}}{5}(\sin(2x) + 2\cos(2x)) + C$. Note the overall negative sign: this comes from the fact that the integral of $e^{-x}$ is $-e^{-x}$, which flips signs compared to the $e^x$ case.

---

## Key Takeaways

1. When the polynomial has degree $n > 1$, repeated integration by parts reduces the degree by one each round. Stop when the polynomial vanishes.
2. The loop trick works when the original integral reappears after two rounds. Do not panic when you see the same integral again—isolate it algebraically and solve.
3. The tabular method is a fast, organized way to handle $\int (\text{polynomial}) \times (\text{exponential or trig})\,dx$. Differentiate the polynomial until zero, integrate the other function, and multiply diagonally with alternating signs.
4. Never forget $+C$. Even in the loop trick, where the algebra involves the integral on both sides, the final answer must include the constant of integration.
5. Double-check your signs. Alternating signs in the tabular method and sign flips from integrating trigonometric functions are the most common sources of error.

