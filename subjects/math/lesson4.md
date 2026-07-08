# Lesson 4: Integration by Parts (Basic)

## What Is Integration by Parts and Why Does It Matter?

Differentiation has a set of straightforward rules: the product rule, the chain rule, the quotient rule. Integration, however, has no direct analog of the product rule. You cannot integrate a product of two functions by integrating each factor separately and multiplying. The integral of $x \cdot e^x$ is not $\frac{x^2}{2} \cdot e^x$. The integral of $x \cdot \sin x$ is not $\frac{x^2}{2} \cdot (-\cos x)$.

We need a technique that handles products of functions during integration. **Integration by parts** is the technique that fills this gap. It is the integration counterpart of the product rule for differentiation, and it converts the integral of a product into a different integral that may be easier to evaluate.

This technique is essential for integrating expressions like $x e^x$, $x \sin x$, $\ln x$, $\arctan x$, and many others that appear throughout calculus, physics, and engineering.

## Where the Formula Comes From

We begin with the **product rule** for differentiation. Suppose $u$ and $v$ are two functions of $x$. The product rule states:

$$\frac{d}{dx}(u \cdot v) = u \frac{dv}{dx} + v \frac{du}{dx}$$

In a more compact notation using differentials, we write $u' = \frac{du}{dx}$ and $v' = \frac{dv}{dx}$. Then the product rule is:

$$\frac{d}{dx}(uv) = u v' + v u'$$

Now rearrange this equation. Move the second term to the left side:

$$u v' = \frac{d}{dx}(uv) - v u'$$

The next step is to integrate both sides with respect to $x$. The integral of a derivative $\frac{d}{dx}(uv)$ is simply $uv$, by the Fundamental Theorem of Calculus:

$$\int u v' \, dx = uv - \int v u' \, dx$$

This is the integration by parts formula in its "function" form. In practice, we use the cleaner differential notation. Let $du = u'\,dx$ and $dv = v'\,dx$. Then the formula becomes:

$$\int u \, dv = uv - \int v \, du$$

This is what we call the **integration by parts formula**. It trades the original integral $\int u\,dv$ for a new integral $\int v\,du$. The art of using this technique is choosing $u$ and $dv$ so that the new integral is simpler than the original.

## The LIATE Rule: How to Choose $u$

A common question from students is: "How do I know what to pick as $u$ and what to pick as $dv$?" The answer is the **LIATE rule**, which is a priority list for selecting $u$ when the integrand is a product of two functions from different families. The letter $u$ should come from the type that appears higher in this list:

| Priority | Letter | Function Type | Examples |
|---|---|---|---|
| Highest | **L** | Logarithmic | $\ln x$, $\ln(2x + 1)$, $\ln(3x)$ |
| | **I** | Inverse trigonometric | $\arcsin x$, $\arctan x$, $\arccos x$ |
| | **A** | Algebraic (polynomials, roots) | $x$, $x^2$, $\sqrt{x}$, $x^5 + 2$ |
| | **T** | Trigonometric | $\sin x$, $\cos x$, $\tan x$, $\sec x$ |
| Lowest | **E** | Exponential | $e^x$, $e^{2x}$, $3^x$ |

The reasoning behind this order is that differentiating a logarithmic or inverse trigonometric function produces a simpler algebraic expression (for example, the derivative of $\ln x$ is $\frac{1}{x}$). Differentiating a polynomial lowers its degree, which is progress. But differentiating a trigonometric or exponential function does not fundamentally change its type—$\sin x$ becomes $\cos x$, and $e^x$ stays $e^x$.

Whatever is not chosen as $u$ becomes $dv$, and you must be able to integrate $dv$ to get $v$.

Here are three quick illustrations of the LIATE rule:

- In $\int x e^x \, dx$, $x$ is Algebraic and $e^x$ is Exponential. Since A comes before E, we choose $u = x$ and $dv = e^x\,dx$.
- In $\int x \sin x \, dx$, $x$ is Algebraic and $\sin x$ is Trigonometric. Since A comes before T, we choose $u = x$ and $dv = \sin x\,dx$.
- In $\int \ln x \, dx$, we have only one visible function. The trick is to write it as $\ln x \cdot 1$. Now $\ln x$ is Logarithmic and $1$ is Algebraic. L comes before A, so $u = \ln x$ and $dv = 1 \cdot dx$.

## A Common Misconception

Many students believe that the function that is "harder" to integrate should be chosen as $u$. This is backwards. You should choose $u$ as the function that becomes **simpler when differentiated**. The function you pick as $dv$ must be one you **can integrate**. The LIATE rule formalizes this insight.

## Step-by-Step Method

1. **Identify the two types** of functions in the product and use LIATE to select $u$.
2. **Set $dv$** to be everything else in the integrand, including the $dx$.
3. **Differentiate $u$** to get $du = u'\,dx$.
4. **Integrate $dv$** to get $v$ (no need for $+C$ at this stage—we will add it at the end).
5. **Apply the formula** $\int u\,dv = uv - \int v\,du$.
6. **Evaluate the new integral** $\int v\,du$, which should be simpler than the original.
7. **Add $+C$** to the final result.

---

## Worked Examples

### Example 1: A Polynomial Times an Exponential

**Problem:** Evaluate $\displaystyle \int x e^x \, dx$.

**Approach:** To solve this, we need to identify the types of functions. Here $x$ is Algebraic and $e^x$ is Exponential. The LIATE rule says A comes before E, so we choose $u = x$ and $dv = e^x\,dx$.

**Step-by-step working:**

$$u = x \quad \implies \quad du = 1 \cdot dx$$
$$dv = e^x\,dx \quad \implies \quad v = e^x$$

Now substitute into the integration by parts formula $\int u\,dv = uv - \int v\,du$:

$$\int x e^x \, dx = x \cdot e^x - \int e^x \cdot 1\,dx$$

The new integral is simply $\int e^x\,dx = e^x$. So:

$$\int x e^x \, dx = x e^x - e^x + C$$

Factor out $e^x$:

$$\int x e^x \, dx = e^x(x - 1) + C$$

**Why this makes sense:** We can check by differentiating the answer. Using the product rule: $\frac{d}{dx}[e^x(x-1)] = e^x(x-1) + e^x(1) = e^x(x-1+1) = x e^x$, which matches the original integrand. The check confirms the result is correct.

---

### Example 2: A Polynomial Times a Trigonometric Function

**Problem:** Evaluate $\displaystyle \int x \sin x \, dx$.

**Approach:** To solve this, we note that $x$ is Algebraic and $\sin x$ is Trigonometric. LIATE says A before T, so $u = x$ and $dv = \sin x\,dx$.

**Step-by-step working:**

$$u = x \quad \implies \quad du = dx$$
$$dv = \sin x\,dx \quad \implies \quad v = -\cos x$$

Apply the formula:

$$\int x \sin x \, dx = x(-\cos x) - \int (-\cos x)\,dx$$

The double negative becomes a positive:

$$= -x\cos x + \int \cos x\,dx$$

The integral of $\cos x$ is $\sin x$:

$$= -x\cos x + \sin x + C$$

**Why this makes sense:** Differentiating $ -x\cos x + \sin x$ using the product rule on the first term: $\frac{d}{dx}(-x\cos x) = -(1 \cdot \cos x + x \cdot (-\sin x)) = -\cos x + x\sin x$. Adding the derivative of $\sin x$ which is $\cos x$ gives $x\sin x$. The answer checks out.

---

### Example 3: The Natural Logarithm (A Special Case)

**Problem:** Evaluate $\displaystyle \int \ln x \, dx$.

**Approach:** To solve this, we notice there is only one function. The technique is to rewrite the integrand as $\ln x \cdot 1$, so we have a product of a Logarithmic function ($\ln x$) and an Algebraic function ($1$). LIATE says L before A, so $u = \ln x$ and $dv = 1 \cdot dx$.

**Step-by-step working:**

$$u = \ln x \quad \implies \quad du = \frac{1}{x}\,dx$$
$$dv = dx \quad \implies \quad v = x$$

Apply the formula:

$$\int \ln x \, dx = (\ln x)(x) - \int x \cdot \frac{1}{x}\,dx$$

The $x$ in the numerator and denominator cancel:

$$= x\ln x - \int 1\,dx$$
$$= x\ln x - x + C$$

**Why this makes sense:** Differentiating $x\ln x - x$: by the product rule, $\frac{d}{dx}(x\ln x) = 1 \cdot \ln x + x \cdot \frac{1}{x} = \ln x + 1$. The derivative of $-x$ is $-1$. Adding: $\ln x + 1 - 1 = \ln x$. The result is correct. This is a classic formula worth remembering: $\int \ln x\,dx = x\ln x - x + C$.

---

### Example 4: A Polynomial Times Cosine with a Constant Multiple

**Problem:** Evaluate $\displaystyle \int x \cos(3x) \, dx$.

**Approach:** To solve this, we identify $x$ as Algebraic and $\cos(3x)$ as Trigonometric. LIATE says A before T, so $u = x$ and $dv = \cos(3x)\,dx$. When integrating $\cos(3x)$, we need the chain rule in reverse: the integral of $\cos(kx)$ is $\frac{1}{k}\sin(kx)$.

**Step-by-step working:**

$$u = x \quad \implies \quad du = dx$$
$$dv = \cos(3x)\,dx \quad \implies \quad v = \frac{1}{3}\sin(3x)$$

Apply the formula:

$$\int x \cos(3x)\,dx = x \cdot \frac{1}{3}\sin(3x) - \int \frac{1}{3}\sin(3x)\,dx$$

Factor out the constant $\frac{1}{3}$ from the remaining integral:

$$= \frac{1}{3}x\sin(3x) - \frac{1}{3}\int \sin(3x)\,dx$$

The integral of $\sin(3x)$ is $-\frac{1}{3}\cos(3x)$, because when we differentiate $-\frac{1}{3}\cos(3x)$, we get $-\frac{1}{3} \cdot (-\sin(3x) \cdot 3) = \sin(3x)$:

$$= \frac{1}{3}x\sin(3x) - \frac{1}{3}\left(-\frac{1}{3}\cos(3x)\right) + C$$
$$= \frac{1}{3}x\sin(3x) + \frac{1}{9}\cos(3x) + C$$

**Why this makes sense:** The answer contains both a sine term (from the $x$ interacting with the integral of $\cos$) and a cosine term (from the second round of integration). The coefficients $\frac{1}{3}$ and $\frac{1}{9}$ come from the chain-rule constants when integrating trig functions with arguments like $3x$. This structure is typical for integration by parts with trigonometric functions.

---

## Practice Problems

### Problem 1
Evaluate the indefinite integral $\displaystyle \int x e^{2x} \, dx$.

### Problem 2
Evaluate the indefinite integral $\displaystyle \int x \cos x \, dx$.

### Problem 3
Evaluate the indefinite integral $\displaystyle \int \ln(2x) \, dx$. (Hint: First rewrite $\ln(2x)$ as $\ln 2 + \ln x$, or treat it as a single logarithmic function using $u = \ln(2x)$.)

### Problem 4
Evaluate the indefinite integral $\displaystyle \int x \sin(2x) \, dx$.

### Problem 5
Evaluate the indefinite integral $\displaystyle \int \arctan x \, dx$. (Hint: Write the integrand as $\arctan x \cdot 1$. The function $\arctan x$ is an inverse trigonometric function, so it takes priority over the algebraic $1$ in LIATE. You will need a substitution for the resulting integral.)

### Problem 6
Evaluate the indefinite integral $\displaystyle \int x^2 \ln x \, dx$. (Hint: LIATE says Logarithmic comes before Algebraic, even when the algebraic part is $x^2$. So $u = \ln x$ and $dv = x^2\,dx$.)

---

## Answers

### Answer 1

We identify $x$ as Algebraic and $e^{2x}$ as Exponential. By LIATE, $u = x$ and $dv = e^{2x}\,dx$. Then $du = dx$ and $v = \frac{1}{2}e^{2x}$. Applying the formula: $\int x e^{2x}\,dx = x \cdot \frac{1}{2}e^{2x} - \int \frac{1}{2}e^{2x}\,dx = \frac{1}{2}x e^{2x} - \frac{1}{2} \cdot \frac{1}{2}e^{2x} + C = \frac{1}{2}x e^{2x} - \frac{1}{4}e^{2x} + C$. This can also be written as $\frac{e^{2x}}{4}(2x - 1) + C$. A common mistake is forgetting the $\frac{1}{2}$ factor when integrating $e^{2x}$ to get $v$.

### Answer 2

We identify $x$ as Algebraic and $\cos x$ as Trigonometric. By LIATE, $u = x$ and $dv = \cos x\,dx$. Then $du = dx$ and $v = \sin x$. Applying the formula: $\int x \cos x\,dx = x\sin x - \int \sin x\,dx = x\sin x - (-\cos x) + C = x\sin x + \cos x + C$. A common error is getting the sign wrong: the integral of $\cos x$ is $+\sin x$, and the integral of $\sin x$ is $-\cos x$. Watch the double negative carefully.

### Answer 3

We can use the property $\ln(2x) = \ln 2 + \ln x$. The integral splits as $\int \ln 2\,dx + \int \ln x\,dx$. The first part is $(\ln 2)x$. The second part, as shown in Example 3, is $x\ln x - x$. Combined: $\int \ln(2x)\,dx = x\ln 2 + x\ln x - x + C = x(\ln 2 + \ln x) - x + C = x\ln(2x) - x + C$. Alternatively, use $u = \ln(2x)$ directly with $dv = dx$. Then $du = \frac{1}{2x} \cdot 2\,dx = \frac{1}{x}\,dx$ and $v = x$. The formula gives $x\ln(2x) - \int x \cdot \frac{1}{x}\,dx = x\ln(2x) - x + C$, the same result.

### Answer 4

We identify $x$ as Algebraic and $\sin(2x)$ as Trigonometric. By LIATE, $u = x$ and $dv = \sin(2x)\,dx$. Then $du = dx$. To find $v$, we integrate $\sin(2x)$: the integral of $\sin(kx)$ is $-\frac{1}{k}\cos(kx)$, so $v = -\frac{1}{2}\cos(2x)$. Applying the formula: $\int x\sin(2x)\,dx = x\left(-\frac{1}{2}\cos(2x)\right) - \int \left(-\frac{1}{2}\cos(2x)\right)dx = -\frac{1}{2}x\cos(2x) + \frac{1}{2}\int \cos(2x)\,dx$. The integral of $\cos(2x)$ is $\frac{1}{2}\sin(2x)$, so: $-\frac{1}{2}x\cos(2x) + \frac{1}{2} \cdot \frac{1}{2}\sin(2x) + C = -\frac{1}{2}x\cos(2x) + \frac{1}{4}\sin(2x) + C$.

### Answer 5

The function $\arctan x$ is inverse trigonometric (I in LIATE). We write it as $\arctan x \cdot 1$, so the Algebraic $1$ becomes $dv$. Set $u = \arctan x$ and $dv = dx$. Then $du = \frac{1}{1 + x^2}\,dx$ and $v = x$. Applying the formula: $\int \arctan x\,dx = x\arctan x - \int x \cdot \frac{1}{1+x^2}\,dx = x\arctan x - \int \frac{x}{1+x^2}\,dx$. For the remaining integral, use the substitution $w = 1 + x^2$, so $dw = 2x\,dx$ and $x\,dx = \frac{1}{2}dw$. Then $\int \frac{x}{1+x^2}\,dx = \frac{1}{2}\int \frac{1}{w}\,dw = \frac{1}{2}\ln|w| = \frac{1}{2}\ln(1+x^2)$. Since $1+x^2$ is always positive, we can drop the absolute value. Final answer: $\int \arctan x\,dx = x\arctan x - \frac{1}{2}\ln(1+x^2) + C$. A common pitfall is not recognizing that the remaining integral $\int \frac{x}{1+x^2}\,dx$ is a $\ln$ form through substitution.

### Answer 6

We have $\ln x$ (Logarithmic) and $x^2$ (Algebraic). LIATE says L before A, so $u = \ln x$ even though differentiating $x^2$ seems tempting. Set $u = \ln x$ and $dv = x^2\,dx$. Then $du = \frac{1}{x}\,dx$ and $v = \frac{1}{3}x^3$. Applying the formula: $\int x^2 \ln x\,dx = \frac{1}{3}x^3 \ln x - \int \frac{1}{3}x^3 \cdot \frac{1}{x}\,dx = \frac{1}{3}x^3 \ln x - \frac{1}{3}\int x^2\,dx = \frac{1}{3}x^3 \ln x - \frac{1}{3} \cdot \frac{x^3}{3} + C = \frac{1}{3}x^3 \ln x - \frac{1}{9}x^3 + C$. This can be factored as $\frac{x^3}{9}(3\ln x - 1) + C$. Many students make the mistake of choosing $u = x^2$ here, which makes the integral more complicated rather than simpler. The LIATE rule exists precisely to prevent this error.

---

## Key Takeaways

1. Integration by parts is the integration counterpart of the product rule. It converts $\int u\,dv$ into $uv - \int v\,du$.
2. The LIATE rule tells you what to choose as $u$: Logarithmic, Inverse trig, Algebraic, Trigonometric, Exponential, in that order of priority.
3. The function $dv$ must be something you can integrate. It always includes the $dx$ factor.
4. When you see a lone logarithm or inverse trig function, write it as the function times $1$ and use $dv = dx$.
5. Always check your answer by differentiating. This catches errors in signs, constants, and missing terms.

