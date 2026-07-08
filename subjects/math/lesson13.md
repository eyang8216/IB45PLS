# Lesson 13: Taylor Series and Maclaurin Series

## 1. The Central Question

Suppose you have a function, such as the exponential $e^x$ or the sine function $\sin x$. These functions are not polynomials—they involve transcendental operations that make them hard to compute by hand. Yet in many applications, from engineering to physics, we need to evaluate these functions numerically. The central question of this lesson is: can we represent a complicated function as an infinite polynomial—a power series—that we can evaluate term by term?

The answer is yes, for a large class of functions. The resulting power series is called a **Taylor series**, and it is one of the most powerful ideas in calculus. The Taylor series gives us a way to approximate any sufficiently smooth function near a chosen point, with accuracy that improves as we include more terms.

---

## 2. What Is a Taylor Series?

Given a function $f(x)$ that can be differentiated infinitely many times at a point $x = a$, the **Taylor series** of $f$ centered at $a$ is:

$$f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!} (x-a)^n$$

Let us unpack this notation. The symbol $f^{(n)}(a)$ means "the $n$-th derivative of $f$, evaluated at $x = a$." So $f^{(0)}(a)$ is just $f(a)$, the value of the function itself. $f^{(1)}(a)$ is the first derivative $f'(a)$. $f^{(2)}(a)$ is the second derivative $f''(a)$. The symbol $n!$ (read "$n$ factorial") is the product of all positive integers from $1$ to $n$; for example, $3! = 3 \times 2 \times 1 = 6$. By convention, $0! = 1$.

When the center is chosen to be $a = 0$, the series receives a special name: the **Maclaurin series**.

$$f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(0)}{n!} x^n$$

Many students confuse Taylor and Maclaurin series, thinking they are different concepts. In fact, a Maclaurin series is simply a Taylor series with the center set to zero. This is the most common special case because calculations at zero are typically the easiest.

---

## 3. Where the Formula Comes From

To understand why the Taylor series takes this form, imagine we want to write the function $f(x)$ as a power series with unknown coefficients:

$$f(x) = c_0 + c_1(x-a) + c_2(x-a)^2 + c_3(x-a)^3 + \cdots$$

Our goal is to determine the coefficients $c_0, c_1, c_2, \ldots$ in terms of the derivatives of $f$ at $a$.

First, plug in $x = a$. All the $(x-a)$ terms become zero, leaving only $f(a) = c_0$. This tells us that $c_0$ is simply the value of the function at the center.

Next, differentiate the series term by term:

$$f'(x) = c_1 + 2c_2(x-a) + 3c_3(x-a)^2 + 4c_4(x-a)^3 + \cdots$$

Now plug in $x = a$ again. All terms with $(x-a)$ vanish, and we get $f'(a) = c_1$. So $c_1$ is the first derivative at the center.

Differentiate a second time:

$$f''(x) = 2c_2 + 6c_3(x-a) + 12c_4(x-a)^2 + \cdots$$

Plug in $x = a$: $f''(a) = 2c_2$, so $c_2 = \frac{f''(a)}{2}$.

Notice that the number multiplying $c_2$ after two differentiations is $2 = 2!$. After three differentiations we would get $6 = 3!$. The pattern continues: $c_n = \frac{f^{(n)}(a)}{n!}$. This is exactly the Taylor series formula.

---

## 4. The Maclaurin Series You Must Memorize

These five series are essential for IB AAHL. You should know their forms, their first few terms, and their intervals of convergence.

### 4.1 The Exponential Function: $e^x$

$$e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \cdots$$

**Why this works:** Every derivative of $e^x$ is $e^x$ itself. At $x = 0$, every derivative equals $1$. So $f^{(n)}(0) = 1$ for all $n$, giving $c_n = \frac{1}{n!}$.

The radius of convergence is $R = \infty$, meaning this series converges for every real number $x$.

Many students think the series for $e^x$ "looks like" it should converge only for small $x$ because factorials grow fast. But factorials are in the denominator, which means they help the series converge, not hinder it. The terms shrink to zero for any fixed $x$, no matter how large.

### 4.2 The Sine Function: $\sin x$

$$\sin x = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{(2n+1)!} = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots$$

**Why this works:** The derivatives of $\sin x$ cycle: $\sin x$, $\cos x$, $-\sin x$, $-\cos x$, and then repeat. Evaluated at $0$, this cycle gives $0, 1, 0, -1, 0, 1, 0, -1, \ldots$. Only the odd-order derivatives (first, third, fifth, ...) are nonzero, and they alternate in sign. That is why only odd powers appear.

The radius of convergence is $R = \infty$.

### 4.3 The Cosine Function: $\cos x$

$$\cos x = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n}}{(2n)!} = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \cdots$$

**Why this works:** The derivatives of $\cos x$ cycle: $\cos x$, $-\sin x$, $-\cos x$, $\sin x$, and then repeat. Evaluated at $0$, this gives $1, 0, -1, 0, 1, 0, -1, 0, \ldots$. Only the even-order derivatives are nonzero, and they alternate in sign. That is why only even powers appear.

The radius of convergence is $R = \infty$.

### 4.4 The Natural Logarithm: $\ln(1+x)$

$$\ln(1+x) = \sum_{n=1}^{\infty} \frac{(-1)^{n-1} x^n}{n} = x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \cdots$$

**Why this works:** The function evaluated at zero is $\ln(1) = 0$, so $c_0 = 0$. The first derivative is $\frac{1}{1+x}$, which at $x=0$ equals $1$. Higher derivatives follow the pattern $f^{(n)}(0) = (-1)^{n-1}(n-1)!$ for $n \geq 1$. Dividing by $n!$ gives $c_n = \frac{(-1)^{n-1}}{n}$.

The radius of convergence is $R = 1$. The interval includes $x = 1$ (giving the alternating harmonic series, which converges) but excludes $x = -1$ (where the logarithm is undefined).

A common misunderstanding is to think $\ln(1+x)$ converges for all $x$ like $e^x$ does. It does not—the series only works for $-1 < x \leq 1$. At $x = -1$, the logarithm itself is undefined, and at $x < -1$ or $x > 1$, the series diverges.

### 4.5 The Binomial Series: $(1+x)^k$

$$(1+x)^k = \sum_{n=0}^{\infty} \binom{k}{n} x^n = 1 + kx + \frac{k(k-1)}{2!}x^2 + \frac{k(k-1)(k-2)}{3!}x^3 + \cdots$$

Here $\binom{k}{n}$ is the **generalized binomial coefficient**, defined for any real number $k$ and nonnegative integer $n$ by:

$$\binom{k}{n} = \frac{k(k-1)(k-2)\cdots(k-n+1)}{n!}$$

The radius of convergence is $R = 1$ (when $k$ is not a nonnegative integer). A useful special case is the geometric series, obtained by setting $k = -1$:

$$\frac{1}{1+x} = \sum_{n=0}^{\infty} (-1)^n x^n = 1 - x + x^2 - x^3 + \cdots$$

---

## 5. Worked Examples — Building Series by Substitution

One of the most powerful techniques for finding Maclaurin series is substitution: if you know the series for a basic function, you can replace $x$ with a new expression to get the series for a related function. This is always legitimate within the radius of convergence.

### Worked Example 1

**Problem:** Find the Maclaurin series for $f(x) = e^{2x}$. Write the first four nonzero terms and the general term.

**Approach:** We know the series for $e^x$. Replace every $x$ in that series with $2x$, then simplify each term.

**Step 1:** Start with $e^u = \sum_{n=0}^{\infty} \frac{u^n}{n!}$ and substitute $u = 2x$:

$$e^{2x} = \sum_{n=0}^{\infty} \frac{(2x)^n}{n!} = \sum_{n=0}^{\infty} \frac{2^n x^n}{n!}$$

**Step 2:** Write the first four nonzero terms ($n = 0, 1, 2, 3$):

$$e^{2x} = 1 + 2x + \frac{4x^2}{2!} + \frac{8x^3}{3!} + \cdots = 1 + 2x + 2x^2 + \frac{4x^3}{3} + \cdots$$

The general term is $\frac{2^n x^n}{n!}$.

**Why this makes sense:** The derivative of $e^{2x}$ is $2e^{2x}$, so at $x=0$ the first derivative is $2$, giving the coefficient $2$. The second derivative at $0$ is $4$, giving $\frac{4}{2!} = 2$. Our series matches this pattern.

---

### Worked Example 2

**Problem:** Find the Maclaurin series for $f(x) = \sin(x^2)$. Write the first four nonzero terms.

**Approach:** Substitute $u = x^2$ into the known series for $\sin u$.

**Step 1:** The series for sine is $\sin u = u - \frac{u^3}{3!} + \frac{u^5}{5!} - \frac{u^7}{7!} + \cdots$.

**Step 2:** Replace $u$ with $x^2$:

$$\sin(x^2) = x^2 - \frac{(x^2)^3}{3!} + \frac{(x^2)^5}{5!} - \frac{(x^2)^7}{7!} + \cdots$$

**Step 3:** Simplify the exponents:

$$\sin(x^2) = x^2 - \frac{x^6}{6} + \frac{x^{10}}{120} - \frac{x^{14}}{5040} + \cdots$$

The general term is $\frac{(-1)^n x^{4n+2}}{(2n+1)!}$.

**Why this makes sense:** When $x$ is small, $x^2$ is even smaller, so $\sin(x^2)$ should behave like $x^2$ (its leading term). Our series confirms this: the first term is $x^2$.

---

### Worked Example 3

**Problem:** Find the Maclaurin series for $f(x) = \frac{1}{1+3x}$. Write the first four nonzero terms.

**Approach:** Recognize this as a geometric series. Use the identity $\frac{1}{1 - r} = \sum_{n=0}^{\infty} r^n$ with $r = -3x$.

**Step 1:** Rewrite the function to match the geometric series form:

$$\frac{1}{1+3x} = \frac{1}{1 - (-3x)}$$

**Step 2:** Substitute $r = -3x$ into $\sum_{n=0}^{\infty} r^n$:

$$\frac{1}{1+3x} = \sum_{n=0}^{\infty} (-3x)^n = \sum_{n=0}^{\infty} (-3)^n x^n$$

**Step 3:** First four nonzero terms: $1 - 3x + 9x^2 - 27x^3$.

**Why this makes sense:** This is a geometric series that converges when $|-3x| < 1$, meaning $|x| < \frac{1}{3}$. For values of $x$ inside this interval, the infinite sum adds up to exactly $\frac{1}{1+3x}$.

---

### Worked Example 4

**Problem:** Find the Taylor series for $f(x) = \ln x$ centered at $a = 1$. Write the first four nonzero terms.

**Approach:** Compute derivatives of $\ln x$, evaluate them at $x = 1$, and plug into the Taylor series formula with $a = 1$.

**Step 1:** Compute derivatives:

$f(x) = \ln x$, so $f(1) = \ln(1) = 0$.

$f'(x) = \frac{1}{x} = x^{-1}$, so $f'(1) = 1$.

$f''(x) = -x^{-2}$, so $f''(1) = -1$.

$f'''(x) = 2x^{-3}$, so $f'''(1) = 2$.

$f^{(4)}(x) = -6x^{-4}$, so $f^{(4)}(1) = -6$.

**Step 2:** The pattern: $f^{(n)}(1) = (-1)^{n-1}(n-1)!$ for $n \geq 1$.

**Step 3:** Form the Taylor series with $a = 1$:

$$\ln x = \sum_{n=1}^{\infty} \frac{(-1)^{n-1}(n-1)!}{n!}(x-1)^n = \sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{n}(x-1)^n$$

**Step 4:** First four nonzero terms:

$$\ln x = (x-1) - \frac{(x-1)^2}{2} + \frac{(x-1)^3}{3} - \frac{(x-1)^4}{4} + \cdots$$

**Why this makes sense:** If we set $x = 1 + u$, this becomes the standard $\ln(1+u)$ series we already know.

---

### Worked Example 5

**Problem:** Find the first four nonzero terms of the Maclaurin series for $f(x) = x \cos x$.

**Approach:** Start with the known series for $\cos x$ and multiply every term by $x$.

**Step 1:** Write the cosine series:

$$\cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \cdots$$

**Step 2:** Multiply each term by $x$:

$$x\cos x = x \cdot 1 - x \cdot \frac{x^2}{2!} + x \cdot \frac{x^4}{4!} - x \cdot \frac{x^6}{6!} + \cdots$$

**Step 3:** Simplify:

$$x\cos x = x - \frac{x^3}{2} + \frac{x^5}{24} - \frac{x^7}{720} + \cdots$$

**Why this makes sense:** The function $x\cos x$ is an odd function (it satisfies $f(-x) = -f(x)$), and indeed only odd powers appear in the series.

---

## 6. Summary Table

| Function | Maclaurin Series | First Few Terms | $R$ |
|---|---|---|---|
| $e^x$ | $\sum_{n=0}^{\infty} \frac{x^n}{n!}$ | $1 + x + \frac{x^2}{2} + \frac{x^3}{6} + \cdots$ | $\infty$ |
| $\sin x$ | $\sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{(2n+1)!}$ | $x - \frac{x^3}{6} + \frac{x^5}{120} - \cdots$ | $\infty$ |
| $\cos x$ | $\sum_{n=0}^{\infty} \frac{(-1)^n x^{2n}}{(2n)!}$ | $1 - \frac{x^2}{2} + \frac{x^4}{24} - \cdots$ | $\infty$ |
| $\ln(1+x)$ | $\sum_{n=1}^{\infty} \frac{(-1)^{n-1}x^n}{n}$ | $x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots$ | $1$ |
| $\frac{1}{1-x}$ | $\sum_{n=0}^{\infty} x^n$ | $1 + x + x^2 + x^3 + \cdots$ | $1$ |
| $(1+x)^k$ | $\sum_{n=0}^{\infty} \binom{k}{n}x^n$ | $1 + kx + \frac{k(k-1)}{2}x^2 + \cdots$ | $1$ |

---

## Practice Problems

**Problem 1**
Find the Maclaurin series for $f(x) = e^{-x}$ by substituting $-x$ into the series for $e^x$. Write the first four nonzero terms and the general term.

**Problem 2**
Find the Maclaurin series for $f(x) = \cos(2x)$ by substituting $2x$ into the series for $\cos x$. Write the first four nonzero terms.

**Problem 3**
Find the Maclaurin series for $f(x) = \ln(1 - x)$ by substituting $-x$ into the series for $\ln(1+x)$. Write the first four nonzero terms.

**Problem 4**
Find the Taylor series for $f(x) = e^x$ centered at $a = 1$. Write the first four nonzero terms and the general term.

**Problem 5 (IB-style)**
The function $f$ is defined by $f(x) = x^2 e^x$.

(a) Using the Maclaurin series for $e^x$, find the Maclaurin series for $f(x)$ up to and including the term in $x^5$. [3 marks]

(b) Hence find the value of $f^{(4)}(0)$, the fourth derivative of $f$ evaluated at $x = 0$. [2 marks]

---

## Answers

**Answer 1**
Substitute $u = -x$ into $e^u = \sum_{n=0}^{\infty} \frac{u^n}{n!}$. This gives $e^{-x} = \sum_{n=0}^{\infty} \frac{(-x)^n}{n!} = \sum_{n=0}^{\infty} \frac{(-1)^n x^n}{n!}$.

The first four nonzero terms (for $n = 0, 1, 2, 3$) are: $1 - x + \frac{x^2}{2!} - \frac{x^3}{3!}$, which simplifies to $1 - x + \frac{x^2}{2} - \frac{x^3}{6}$.

The general term is $\frac{(-1)^n x^n}{n!}$.

**Answer 2**
Substitute $u = 2x$ into $\cos u = \sum_{n=0}^{\infty} \frac{(-1)^n u^{2n}}{(2n)!}$. This gives $\cos(2x) = \sum_{n=0}^{\infty} \frac{(-1)^n (2x)^{2n}}{(2n)!} = \sum_{n=0}^{\infty} \frac{(-1)^n 4^n x^{2n}}{(2n)!}$.

The first four nonzero terms are:
$n=0$: $1$
$n=1$: $-\frac{4x^2}{2!} = -2x^2$
$n=2$: $\frac{16x^4}{4!} = \frac{16x^4}{24} = \frac{2x^4}{3}$
$n=3$: $-\frac{64x^6}{6!} = -\frac{64x^6}{720} = -\frac{4x^6}{45}$

So: $1 - 2x^2 + \frac{2}{3}x^4 - \frac{4}{45}x^6$.

**Answer 3**
Substitute $u = -x$ into $\ln(1+u) = u - \frac{u^2}{2} + \frac{u^3}{3} - \frac{u^4}{4} + \cdots$.

$\ln(1-x) = (-x) - \frac{(-x)^2}{2} + \frac{(-x)^3}{3} - \frac{(-x)^4}{4} + \cdots = -x - \frac{x^2}{2} - \frac{x^3}{3} - \frac{x^4}{4} - \cdots$

The first four nonzero terms are: $-x - \frac{x^2}{2} - \frac{x^3}{3} - \frac{x^4}{4}$.

All signs are negative, unlike the alternating signs in $\ln(1+x)$. The general term is $-\frac{x^n}{n}$ for $n \geq 1$.

**Answer 4**
For $f(x) = e^x$, every derivative is $e^x$, so $f^{(n)}(1) = e^1 = e$ for all $n$. Plugging into the Taylor series formula with $a = 1$:

$e^x = \sum_{n=0}^{\infty} \frac{e}{n!}(x-1)^n = e + e(x-1) + \frac{e}{2}(x-1)^2 + \frac{e}{6}(x-1)^3 + \cdots$

The first four nonzero terms are: $e + e(x-1) + \frac{e}{2}(x-1)^2 + \frac{e}{6}(x-1)^3$. The general term is $\frac{e}{n!}(x-1)^n$.

**Answer 5 (IB-style)**
**(a)** The Maclaurin series for $e^x$ is $e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \frac{x^5}{5!} + \cdots$. Multiply by $x^2$:

$f(x) = x^2 e^x = x^2\left(1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots\right) = x^2 + x^3 + \frac{x^4}{2!} + \frac{x^5}{3!} + \cdots$

The Maclaurin series up to $x^5$ is: $x^2 + x^3 + \frac{x^4}{2} + \frac{x^5}{6}$. [3 marks]

**(b)** The coefficient of $x^4$ in the Maclaurin series is $\frac{f^{(4)}(0)}{4!}$. From part (a), the $x^4$ term is $\frac{x^4}{2}$, so $\frac{f^{(4)}(0)}{4!} = \frac{1}{2}$.

Therefore $f^{(4)}(0) = \frac{1}{2} \cdot 4! = \frac{1}{2} \cdot 24 = 12$. [2 marks]

A common pitfall is to forget to multiply by the factorial when extracting derivatives from series coefficients. The coefficient gives you $\frac{f^{(n)}(0)}{n!}$, not $f^{(n)}(0)$ directly.
