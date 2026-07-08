# Lesson 2: Implicit Differentiation

## What Is Implicit Differentiation and Why Does It Matter?

In mathematics, we often encounter equations that describe a relationship between two variables, typically written as $x$ and $y$. When we can express $y$ entirely in terms of $x$—for example, $y = x^2 + 3x$—we say that $y$ is an **explicit function** of $x$. The word "explicit" means the relationship is stated directly: you can read off the value of $y$ for any given $x$ without solving anything.

However, many important equations in mathematics and science do not isolate $y$ on one side. An equation such as $x^2 + y^2 = 25$ describes a circle of radius 5 centered at the origin. This equation relates $x$ and $y$, but it does not tell us $y$ as a single formula in $x$. We say $y$ is an **implicit function** of $x$ because the relationship is hidden inside the equation rather than displayed openly.

We need a method to find the slope of a curve—the derivative $\frac{dy}{dx}$—even when we cannot solve for $y$ explicitly. The reason this matters is that many curves in geometry (circles, ellipses, hyperbolas, the Folium of Descartes) and in applied problems (thermodynamic relations, economic indifference curves) are naturally expressed in implicit form. Without implicit differentiation, we would be unable to compute rates of change, find tangent lines, or locate critical points on these curves.

**Implicit differentiation** is the technique that lets us differentiate both sides of an equation directly with respect to $x$, treating $y$ as a function of $x$ even when we do not have an explicit formula for it.

## The Core Idea: Treat $y$ as $y(x)$

The central insight of implicit differentiation is to imagine that $y$ is a function of $x$, which we can write as $y(x)$, even though we do not know its formula. Whenever we differentiate an expression that contains $y$, we apply the **chain rule**. The chain rule is the differentiation rule that tells us how to differentiate a composition of functions: if $f$ depends on $y$, and $y$ depends on $x$, then $\frac{d}{dx}[f(y)] = f'(y) \cdot \frac{dy}{dx}$.

Here is what the chain rule produces for common expressions involving $y$ when we differentiate with respect to $x$:

- The derivative of $y$ is $1 \cdot \frac{dy}{dx}$, because $\frac{d}{dy}(y) = 1$.
- The derivative of $y^2$ is $2y \cdot \frac{dy}{dx}$, because $\frac{d}{dy}(y^2) = 2y$.
- The derivative of $y^3$ is $3y^2 \cdot \frac{dy}{dx}$, following the same pattern.
- The derivative of $\sin y$ is $\cos y \cdot \frac{dy}{dx}$.
- The derivative of $e^y$ is $e^y \cdot \frac{dy}{dx}$.

Every $y$-term generates an extra factor of $\frac{dy}{dx}$ when differentiated with respect to $x$. This factor is what we eventually isolate to obtain the derivative.

Expressions that mix $x$ and $y$ in a product, such as $xy$ or $x^2y$, require the **product rule** in addition to the chain rule. The product rule states that $\frac{d}{dx}(uv) = u'v + uv'$, where $u$ and $v$ are both functions of $x$. For $xy$, we treat this as the product of the function $x$ and the function $y(x)$.

## A Common Misconception: The Product Rule with Mixed Terms

Many students forget to apply the product rule when differentiating terms like $xy$ or $2xy$. Here is the precise breakdown:

When we differentiate $2xy$ with respect to $x$, we are differentiating the product of two functions: the function $2x$ and the function $y(x)$. The product rule gives:

$$\frac{d}{dx}(2x \cdot y) = \frac{d}{dx}(2x) \cdot y + (2x) \cdot \frac{d}{dx}(y) = 2 \cdot y + 2x \cdot \frac{dy}{dx}$$

The most common error is writing the derivative as simply $2y$ and omitting the $2x\frac{dy}{dx}$ term. Another common error is writing only $2\frac{dy}{dx}$ and forgetting the $2y$ term. Both parts are necessary.

## Step-by-Step Method for Implicit Differentiation

When you encounter an implicit equation, follow these steps:

1. **Differentiate both sides** of the equation with respect to $x$, term by term.
2. **Apply the chain rule** to every term containing $y$: multiply by $\frac{dy}{dx}$.
3. **Apply the product rule** to any term that is a product of an $x$-expression and a $y$-expression.
4. **Collect all terms containing $\frac{dy}{dx}$** on one side of the equation.
5. **Move all terms without $\frac{dy}{dx}$** to the other side.
6. **Factor out $\frac{dy}{dx}$** from the side where you collected it.
7. **Divide** to isolate $\frac{dy}{dx}$.

---

## Worked Examples

### Example 1: The Circle

**Problem:** Find $\frac{dy}{dx}$ for the equation $x^2 + y^2 = 25$.

**Approach:** To solve this, we need to differentiate every term with respect to $x$, remembering that $y$ is a function of $x$, so $y^2$ requires the chain rule.

**Step-by-step working:**

$$\frac{d}{dx}(x^2) + \frac{d}{dx}(y^2) = \frac{d}{dx}(25)$$

The derivative of $x^2$ is $2x$. The derivative of a constant like $25$ is $0$. For $y^2$, the chain rule gives $2y \cdot \frac{dy}{dx}$:

$$2x + 2y\frac{dy}{dx} = 0$$

Now collect the $\frac{dy}{dx}$ term and move everything else to the other side:

$$2y\frac{dy}{dx} = -2x$$

Divide both sides by $2y$:

$$\frac{dy}{dx} = -\frac{x}{y}$$

**Why this makes sense:** The slope of a circle is negative when $x$ and $y$ have the same sign (first and third quadrants) and positive when they have opposite signs, which matches the geometry of a circle.

---

### Example 2: An Equation with a Mixed Product

**Problem:** Find $\frac{dy}{dx}$ for the equation $x^2 + y^2 = 2xy + 4$.

**Approach:** To solve this, we differentiate both sides. The left side is straightforward. The right side contains $2xy$, which is a product of $2x$ and $y$, so we must use the product rule there.

**Step-by-step working:**

Differentiate the left side:

$$\frac{d}{dx}(x^2) + \frac{d}{dx}(y^2) = 2x + 2y\frac{dy}{dx}$$

Differentiate the right side. The constant $4$ gives $0$. For $2xy$, we apply the product rule to $2x$ and $y$:

$$\frac{d}{dx}(2xy) = \frac{d}{dx}(2x) \cdot y + 2x \cdot \frac{d}{dx}(y) = 2 \cdot y + 2x \cdot \frac{dy}{dx}$$

So the full differentiated equation is:

$$2x + 2y\frac{dy}{dx} = 2y + 2x\frac{dy}{dx}$$

Now collect all terms with $\frac{dy}{dx}$ on the left and all other terms on the right:

$$2y\frac{dy}{dx} - 2x\frac{dy}{dx} = 2y - 2x$$

Factor out $\frac{dy}{dx}$ from the left side:

$$\frac{dy}{dx}(2y - 2x) = 2y - 2x$$

Factor $2$ from both sides:

$$\frac{dy}{dx} \cdot 2(y - x) = 2(y - x)$$

For $y \neq x$, we can divide both sides by $2(y - x)$, giving:

$$\frac{dy}{dx} = 1$$

**Why this makes sense:** The equation $x^2 + y^2 = 2xy + 4$ can be rewritten as $(x - y)^2 = 4$, which means $x - y = \pm 2$. This is the equation of two parallel lines, each with slope $1$. The derivative being $1$ everywhere (except where $x = y$, which never occurs on these lines) confirms this geometry.

**A common mistake:** Many students get $\frac{dy}{dx} = \frac{y - x}{y}$ for this problem because they mishandle the product rule on $2xy$. If you obtained that answer, check that you wrote both the $2y$ term and the $2x\frac{dy}{dx}$ term when differentiating $2xy$.

---

### Example 3: A Trigonometric Implicit Equation

**Problem:** Find $\frac{dy}{dx}$ for the equation $\sin(x + y) = x$.

**Approach:** To solve this, we differentiate $\sin(x + y)$ using the chain rule. The outer function is sine, and the inner function is $x + y$, whose derivative is $1 + \frac{dy}{dx}$.

**Step-by-step working:**

Differentiate both sides:

$$\frac{d}{dx}[\sin(x + y)] = \frac{d}{dx}(x)$$

Apply the chain rule to the left side: the derivative of $\sin(\text{something})$ is $\cos(\text{something})$ times the derivative of the something:

$$\cos(x + y) \cdot \left(1 + \frac{dy}{dx}\right) = 1$$

Divide both sides by $\cos(x + y)$:

$$1 + \frac{dy}{dx} = \frac{1}{\cos(x + y)}$$

The expression $\frac{1}{\cos(x + y)}$ is the definition of $\sec(x + y)$. Subtract $1$ from both sides:

$$\frac{dy}{dx} = \sec(x + y) - 1$$

**Why this makes sense:** When $x + y$ is near $0$, $\sec(x+y)$ is near $1$, so $\frac{dy}{dx}$ is near $0$. As $x + y$ approaches $\frac{\pi}{2}$, $\sec(x+y)$ grows large, so $\frac{dy}{dx}$ becomes large. This matches the behavior of the implicit curve.

---

### Example 4: The Folium of Descartes

**Problem:** Find $\frac{dy}{dx}$ for the equation $x^3 + y^3 = 6xy$.

**Approach:** To solve this, we need the chain rule for $y^3$ and the product rule for $6xy$ on the right side.

**Step-by-step working:**

$$\frac{d}{dx}(x^3) + \frac{d}{dx}(y^3) = \frac{d}{dx}(6xy)$$

The derivative of $x^3$ is $3x^2$. For $y^3$, the chain rule gives $3y^2\frac{dy}{dx}$. For $6xy$, the product rule gives $6y + 6x\frac{dy}{dx}$:

$$3x^2 + 3y^2\frac{dy}{dx} = 6y + 6x\frac{dy}{dx}$$

Collect $\frac{dy}{dx}$ terms on the left and other terms on the right:

$$3y^2\frac{dy}{dx} - 6x\frac{dy}{dx} = 6y - 3x^2$$

Factor out $\frac{dy}{dx}$:

$$\frac{dy}{dx}(3y^2 - 6x) = 6y - 3x^2$$

Divide both sides by $(3y^2 - 6x)$:

$$\frac{dy}{dx} = \frac{6y - 3x^2}{3y^2 - 6x}$$

Factor $3$ from numerator and denominator:

$$\frac{dy}{dx} = \frac{3(2y - x^2)}{3(y^2 - 2x)} = \frac{2y - x^2}{y^2 - 2x}$$

**Why this makes sense:** The Folium of Descartes has a loop in the first quadrant. At the origin $(0,0)$, the curve crosses itself, and the derivative formula gives $\frac{0}{0}$, indicating two different tangent lines—which matches the geometry.

---

## Practice Problems

### Problem 1
Find $\frac{dy}{dx}$ for the equation $x^2 + y^2 = 2xy + 4$. Give your final answer in its simplest form.

### Problem 2
Find $\frac{dy}{dx}$ for the equation $x^3 + y^3 = 6xy$, which describes the Folium of Descartes. Simplify your answer.

### Problem 3
Find $\frac{dy}{dx}$ for the equation $\sin(x + y) = x$.

### Problem 4
Find $\frac{dy}{dx}$ for the equation $e^{xy} = x + y$, where $e$ is the base of the natural logarithm.

### Problem 5
A curve has equation $x^2 + 3xy + y^2 = 7$.
(a) Find an expression for $\frac{dy}{dx}$ in terms of $x$ and $y$. [4 marks]
(b) Hence find the equation of the tangent line to the curve at the point $(1, 2)$. [3 marks]

---

## Answers

### Answer 1

To find $\frac{dy}{dx}$ for $x^2 + y^2 = 2xy + 4$, we differentiate both sides with respect to $x$. The left side gives $2x + 2y\frac{dy}{dx}$. The right side requires the product rule on $2xy$: the derivative is $2y + 2x\frac{dy}{dx}$, and the derivative of the constant $4$ is $0$. Setting these equal gives $2x + 2y\frac{dy}{dx} = 2y + 2x\frac{dy}{dx}$. We collect all terms containing $\frac{dy}{dx}$ on one side: $2y\frac{dy}{dx} - 2x\frac{dy}{dx} = 2y - 2x$. Factoring gives $\frac{dy}{dx}(2y - 2x) = 2y - 2x$. Dividing both sides by $2(y-x)$ yields $\frac{dy}{dx} = 1$, provided $y \neq x$. A common mistake is to mishandle the product rule on $2xy$ and lose the $2x\frac{dy}{dx}$ term, which leads to an incorrect answer like $\frac{y-x}{y}$. The correct answer is simply $\frac{dy}{dx} = 1$.

### Answer 2

For $x^3 + y^3 = 6xy$, we differentiate term by term. The derivative of $x^3$ is $3x^2$. The derivative of $y^3$ is $3y^2\frac{dy}{dx}$ by the chain rule. On the right side, $6xy$ is a product, so its derivative is $6y + 6x\frac{dy}{dx}$ by the product rule. This gives the equation $3x^2 + 3y^2\frac{dy}{dx} = 6y + 6x\frac{dy}{dx}$. We bring $\frac{dy}{dx}$ terms to the left: $3y^2\frac{dy}{dx} - 6x\frac{dy}{dx} = 6y - 3x^2$. Factoring gives $\frac{dy}{dx}(3y^2 - 6x) = 6y - 3x^2$. Dividing and factoring a $3$ from numerator and denominator yields $\frac{dy}{dx} = \frac{2y - x^2}{y^2 - 2x}$. A common pitfall is forgetting the product rule on $6xy$. The right side must produce two terms, not just one.

### Answer 3

To differentiate $\sin(x+y) = x$, we apply the chain rule to the left side. The derivative of $\sin$ of something is $\cos$ of that something, multiplied by the derivative of the inside. The derivative of the inside $(x+y)$ is $1 + \frac{dy}{dx}$. So the left side becomes $\cos(x+y) \cdot (1 + \frac{dy}{dx})$. The right side derivative is simply $1$. We have $\cos(x+y)(1 + \frac{dy}{dx}) = 1$. Dividing both sides by $\cos(x+y)$ gives $1 + \frac{dy}{dx} = \frac{1}{\cos(x+y)}$, which is $\sec(x+y)$. Subtracting $1$ yields $\frac{dy}{dx} = \sec(x+y) - 1$. A common error is forgetting to differentiate the inside $x+y$ and writing only $\cos(x+y)$ instead of $\cos(x+y)(1 + \frac{dy}{dx})$.

### Answer 4

For $e^{xy} = x + y$, the left side is an exponential with $xy$ as the exponent. The chain rule says: differentiate $e^{\text{inside}}$ to get $e^{\text{inside}}$ times the derivative of the inside. The inside is $xy$, which is a product requiring the product rule: $\frac{d}{dx}(xy) = 1 \cdot y + x \cdot \frac{dy}{dx} = y + x\frac{dy}{dx}$. So the derivative of the left side is $e^{xy}(y + x\frac{dy}{dx})$. The right side derivative is $1 + \frac{dy}{dx}$. Setting them equal: $e^{xy}(y + x\frac{dy}{dx}) = 1 + \frac{dy}{dx}$. Expanding the left: $y e^{xy} + x e^{xy}\frac{dy}{dx} = 1 + \frac{dy}{dx}$. Collect $\frac{dy}{dx}$ terms: $x e^{xy}\frac{dy}{dx} - \frac{dy}{dx} = 1 - y e^{xy}$. Factor: $\frac{dy}{dx}(x e^{xy} - 1) = 1 - y e^{xy}$. Therefore $\frac{dy}{dx} = \frac{1 - y e^{xy}}{x e^{xy} - 1}$. The most common mistake here is mishandling the derivative of $e^{xy}$ by forgetting the product rule on the exponent $xy$.

### Answer 5

(a) Differentiating $x^2 + 3xy + y^2 = 7$ term by term: the derivative of $x^2$ is $2x$. The term $3xy$ requires the product rule: $\frac{d}{dx}(3xy) = 3y + 3x\frac{dy}{dx}$. The derivative of $y^2$ is $2y\frac{dy}{dx}$ by the chain rule. The constant $7$ differentiates to $0$. This gives $2x + 3y + 3x\frac{dy}{dx} + 2y\frac{dy}{dx} = 0$. Collecting $\frac{dy}{dx}$ terms: $3x\frac{dy}{dx} + 2y\frac{dy}{dx} = -2x - 3y$. Factor: $\frac{dy}{dx}(3x + 2y) = -(2x + 3y)$. Therefore $\frac{dy}{dx} = -\frac{2x + 3y}{3x + 2y}$.

(b) At the point $(1, 2)$, we substitute $x = 1$ and $y = 2$ into the derivative: $\frac{dy}{dx} = -\frac{2(1) + 3(2)}{3(1) + 2(2)} = -\frac{2 + 6}{3 + 4} = -\frac{8}{7}$. The slope of the tangent line at $(1, 2)$ is $-\frac{8}{7}$. Using point-slope form $y - y_1 = m(x - x_1)$: $y - 2 = -\frac{8}{7}(x - 1)$. Simplifying: $y = -\frac{8}{7}x + \frac{8}{7} + 2 = -\frac{8}{7}x + \frac{22}{7}$. The equation of the tangent line is $y = -\frac{8}{7}x + \frac{22}{7}$, or equivalently $8x + 7y = 22$.

A common mistake in part (a) is to write the derivative of $3xy$ as $3y$ or $3\frac{dy}{dx}$ instead of the full product rule result $3y + 3x\frac{dy}{dx}$. Another common error is forgetting to substitute both $x$ and $y$ values when evaluating $\frac{dy}{dx}$ at the point.

---

## Key Takeaways

1. Every term containing $y$ generates a $\frac{dy}{dx}$ factor when differentiated with respect to $x$, because of the chain rule.
2. Products that mix $x$ and $y$ require the product rule. The derivative of $xy$ is $1 \cdot y + x \cdot \frac{dy}{dx}$, not just $y$ or just $\frac{dy}{dx}$.
3. After differentiating, collect all terms with $\frac{dy}{dx}$ on one side, factor it out, and solve.
4. Simplify the final expression. Some answers reduce dramatically—as in Example 2, where the derivative simplifies to $1$.

