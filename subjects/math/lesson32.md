# Lesson 32: Proof by Induction — Cross-Topic Proofs

## What is Proof by Induction and Why Learn It?

Proof by mathematical induction is a method for proving that a statement is true for all positive integers. You cannot verify infinitely many cases one by one. Instead, induction gives you a two-step logical shortcut: prove the first case, then prove that if any case is true, the next case must also be true. Together, these two steps guarantee the statement holds for every positive integer.

In IB AAHL, induction problems go far beyond simple sums. You will be asked to prove statements about matrices, complex numbers, derivatives, and sequences defined by recurrence relations. This lesson covers each of these cross-topic applications.

## 1. What is a Statement in Induction?

A **statement**, often written as $P(n)$, is a sentence that depends on a positive integer $n$ and is either true or false for each value of $n$. For example, $P(n)$ might be "the $n$th power of a certain matrix has a particular form." The goal of induction is to prove that $P(n)$ is true for every $n \in \mathbb{N}$ (where $\mathbb{N}$ denotes the set of positive integers $\{1, 2, 3, \ldots\}$).

## 2. The Two Steps of Induction

Every induction proof has the same structure:

**Base case:** Prove that the statement is true for the first value of $n$, which is almost always $n = 1$. This is the foundation.

**Inductive step:** Assume the statement is true for some arbitrary value $n = k$. This assumption is called the **inductive hypothesis**. Then, using this hypothesis, prove that the statement must also be true for $n = k + 1$.

If both steps succeed, then $P(1)$ is true, which forces $P(2)$ to be true, which forces $P(3)$ to be true, and so on forever. This chain reaction is the essence of induction.

Many students think the inductive hypothesis is "cheating" because we assume what we want to prove. But we only assume it for $n = k$, and we prove it for $n = k + 1$. We never assume the conclusion for the very case we are trying to prove.

## 3. Matrix Induction

### Worked Example 1

**Problem:** Prove that for all positive integers $n$, the following matrix power formula holds:

$$\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}^n = \begin{pmatrix} 1 & n \\ 0 & 1 \end{pmatrix}$$

**Approach:** We need to verify the base case at $n = 1$, then assume the formula for $n = k$ and prove it for $n = k + 1$ by multiplying the $k$th power by the original matrix.

**Base case ($n = 1$):**

The left side is the matrix raised to the power 1, which is just the matrix itself:

$$\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}^1 = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$$

The right side with $n = 1$ is:

$$\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$$

Both sides match, so $P(1)$ is true.

**Inductive hypothesis:** Assume the statement is true for $n = k$. That is:

$$\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}^k = \begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix}$$

**Inductive step ($n = k + 1$):**

We start with the left side for $n = k + 1$ and rewrite it using the property of exponents:

$$\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}^{k+1} = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}^k \cdot \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$$

Now we replace the $k$th power using the inductive hypothesis:

$$= \begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix} \cdot \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$$

Next we perform the matrix multiplication. The entry in row 1, column 1 is $(1)(1) + (k)(0) = 1$. The entry in row 1, column 2 is $(1)(1) + (k)(1) = 1 + k$. The entry in row 2, column 1 is $(0)(1) + (1)(0) = 0$. The entry in row 2, column 2 is $(0)(1) + (1)(1) = 1$.

$$= \begin{pmatrix} 1 & 1 + k \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & k+1 \\ 0 & 1 \end{pmatrix}$$

This is exactly the formula with $n = k+1$, so $P(k+1)$ is true.

**Why this makes sense:** Each time you multiply by $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, you add the top-left entry to the top-right entry. The top-left stays 1, so the top-right increases by exactly 1 with each multiplication.

---

## 4. Complex Number Induction — De Moivre's Theorem

### Worked Example 2

**Problem:** Prove De Moivre's theorem: $(\cos\theta + i\sin\theta)^n = \cos(n\theta) + i\sin(n\theta)$ for all positive integers $n$.

**Approach:** The base case $n = 1$ is immediate. For the inductive step, we assume the formula holds for $n = k$ and multiply by $(\cos\theta + i\sin\theta)$ once more. Then we use the trigonometric addition formulas to combine arguments.

**Base case ($n = 1$):**

$$(\cos\theta + i\sin\theta)^1 = \cos\theta + i\sin\theta = \cos(1\cdot\theta) + i\sin(1\cdot\theta)$$

The statement holds for $n = 1$.

**Inductive hypothesis:** Assume $(\cos\theta + i\sin\theta)^k = \cos(k\theta) + i\sin(k\theta)$.

**Inductive step ($n = k+1$):**

$$(\cos\theta + i\sin\theta)^{k+1} = (\cos\theta + i\sin\theta)^k \cdot (\cos\theta + i\sin\theta)$$

Substitute the inductive hypothesis:

$$= [\cos(k\theta) + i\sin(k\theta)] \cdot [\cos\theta + i\sin\theta]$$

Now expand the product. Multiply each term in the first bracket by each term in the second:

$$= \cos(k\theta)\cos\theta + i\cos(k\theta)\sin\theta + i\sin(k\theta)\cos\theta + i^2\sin(k\theta)\sin\theta$$

Since $i^2 = -1$, the last term becomes $-\sin(k\theta)\sin\theta$. Group the real terms together and the imaginary terms together:

Real part: $\cos(k\theta)\cos\theta - \sin(k\theta)\sin\theta$

Imaginary part: $i[\cos(k\theta)\sin\theta + \sin(k\theta)\cos\theta]$

The real part is the cosine addition formula: $\cos(A+B) = \cos A \cos B - \sin A \sin B$, with $A = k\theta$ and $B = \theta$.

The imaginary part is the sine addition formula: $\sin(A+B) = \sin A \cos B + \cos A \sin B$, with $A = k\theta$ and $B = \theta$.

Therefore:

$$= \cos(k\theta + \theta) + i\sin(k\theta + \theta) = \cos((k+1)\theta) + i\sin((k+1)\theta)$$

This proves $P(k+1)$.

**Why this makes sense:** Multiplying two complex numbers on the unit circle adds their angles. Starting at angle $\theta$, each additional multiplication adds another $\theta$, so after $n$ multiplications the angle is $n\theta$. The inductive proof formalizes this geometric intuition.

---

## 5. Derivative Induction

### Worked Example 3

**Problem:** Prove that the $n$th derivative of $f(x) = x e^x$ is given by $f^{(n)}(x) = (x + n)e^x$ for all positive integers $n$.

**Approach:** We compute the first derivative to check the base case. Then we assume the formula for the $k$th derivative and differentiate once more to get the $(k+1)$th derivative.

**Base case ($n = 1$):**

Using the product rule, the derivative of $x e^x$ is:

$$f'(x) = (1)e^x + x(e^x) = e^x + x e^x = (x + 1)e^x$$

This matches the formula with $n = 1$, since $(x + 1)e^x = (x + 1)e^x$.

**Inductive hypothesis:** Assume $f^{(k)}(x) = (x + k)e^x$.

**Inductive step ($n = k+1$):**

The $(k+1)$th derivative is the derivative of the $k$th derivative:

$$f^{(k+1)}(x) = \frac{d}{dx}\left[f^{(k)}(x)\right] = \frac{d}{dx}\left[(x + k)e^x\right]$$

Apply the product rule. The derivative of $(x+k)$ is $1$, and the derivative of $e^x$ is $e^x$:

$$= (1)e^x + (x+k)e^x = e^x + (x+k)e^x = (x + k + 1)e^x = (x + (k+1))e^x$$

This matches the formula for $n = k+1$.

**Why this makes sense:** Each derivative of $x e^x$ adds one more $e^x$ term. Starting with $(x+0)e^x$ at the zeroth derivative, each differentiation increments the coefficient of $e^x$ by 1.

---

## 6. Induction with Recurrence Relations

### Worked Example 4

**Problem:** A sequence is defined by $u_1 = 1$ and $u_{n+1} = 2u_n + 1$ for $n \geq 1$. Prove that the closed form is $u_n = 2^n - 1$ for all positive integers $n$.

**Approach:** The base case checks $n=1$. The inductive step uses the recurrence relation: we express $u_{k+1}$ in terms of $u_k$, substitute the closed form for $u_k$, and simplify.

**Base case ($n = 1$):**

$$u_1 = 1 \quad\text{and}\quad 2^1 - 1 = 2 - 1 = 1$$

The closed form matches the given initial value.

**Inductive hypothesis:** Assume $u_k = 2^k - 1$.

**Inductive step ($n = k+1$):**

Using the recurrence relation:

$$u_{k+1} = 2u_k + 1$$

Substitute the inductive hypothesis for $u_k$:

$$u_{k+1} = 2(2^k - 1) + 1$$

Expand:

$$= 2 \cdot 2^k - 2 + 1 = 2^{k+1} - 1$$

This is exactly the closed form with $n = k+1$.

**Why this makes sense:** The recurrence says "double and add 1." If you start at 1, then double and add 1 repeatedly, you generate $1, 3, 7, 15, 31, \ldots$, which are all one less than powers of 2.

---

## Practice Problems

### Problem 1
Prove by induction that for all positive integers $n$:

$$\begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}^n = \begin{pmatrix} 2^n & 0 \\ 0 & 2^n \end{pmatrix}$$

(a) State the base case $n = 1$ and verify it.
(b) Write the inductive hypothesis for $n = k$.
(c) Prove the inductive step from $n = k$ to $n = k+1$.

### Problem 2
A sequence is defined by $a_1 = 3$ and $a_{n+1} = 5a_n - 8$ for $n \geq 1$.

(a) Calculate $a_2$ and $a_3$ using the recurrence.
(b) A proposed closed form is $a_n = 5^{n-1} + 2$. Prove this by induction.

### Problem 3
Prove by induction that the $n$th derivative of $f(x) = e^{3x}$ is given by $f^{(n)}(x) = 3^n e^{3x}$ for all positive integers $n$.

### Problem 4
Prove by induction that for all positive integers $n$:

$$(\cos\theta - i\sin\theta)^n = \cos(n\theta) - i\sin(n\theta)$$

### Problem 5 (IB Exam Style)
Consider the matrix $M = \begin{pmatrix} 1 & a \\ 0 & 1 \end{pmatrix}$ where $a$ is a real constant.

(a) Find $M^2$ and $M^3$. **[2 marks]**

(b) Conjecture a formula for $M^n$ for $n \in \mathbb{N}$. **[1 mark]**

(c) Prove your conjecture by mathematical induction. **[5 marks]**

---

## Answers

### Problem 1

(a) **Base case $n=1$:** The left side is $\begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}^1 = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}$. The right side is $\begin{pmatrix} 2^1 & 0 \\ 0 & 2^1 \end{pmatrix} = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}$. They match.

(b) **Inductive hypothesis:** Assume $\begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}^k = \begin{pmatrix} 2^k & 0 \\ 0 & 2^k \end{pmatrix}$.

(c) **Inductive step:** Starting with $n = k+1$, we write the $(k+1)$th power as the $k$th power times the original matrix:

$$\begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}^{k+1} = \begin{pmatrix} 2^k & 0 \\ 0 & 2^k \end{pmatrix} \cdot \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}$$

Multiplying gives $\begin{pmatrix} 2^k \cdot 2 + 0 \cdot 0 & 2^k \cdot 0 + 0 \cdot 2 \\ 0 \cdot 2 + 2^k \cdot 0 & 0 \cdot 0 + 2^k \cdot 2 \end{pmatrix} = \begin{pmatrix} 2^{k+1} & 0 \\ 0 & 2^{k+1} \end{pmatrix}$.

This matches the formula with $n = k+1$, completing the inductive step. A common pitfall is forgetting that multiplying a scalar matrix by itself simply multiplies the diagonal entries.

### Problem 2

(a) Using $a_1 = 3$:
$a_2 = 5(3) - 8 = 15 - 8 = 7$
$a_3 = 5(7) - 8 = 35 - 8 = 27$

(b) **Base case $n=1$:** $a_1 = 3$ and $5^{1-1} + 2 = 5^0 + 2 = 1 + 2 = 3$. They match.

**Inductive hypothesis:** Assume $a_k = 5^{k-1} + 2$.

**Inductive step:** $a_{k+1} = 5a_k - 8 = 5(5^{k-1} + 2) - 8 = 5^k + 10 - 8 = 5^k + 2 = 5^{(k+1)-1} + 2$. This is exactly the closed form for $n = k+1$.

### Problem 3

**Base case $n=1$:** $f'(x) = 3e^{3x} = 3^1 e^{3x}$. True.

**Inductive hypothesis:** Assume $f^{(k)}(x) = 3^k e^{3x}$.

**Inductive step:** $f^{(k+1)}(x) = \frac{d}{dx}[3^k e^{3x}] = 3^k \cdot 3e^{3x} = 3^{k+1} e^{3x}$. True.

The reason this works is that each derivative pulls down another factor of 3 from the chain rule applied to $e^{3x}$.

### Problem 4

**Base case $n=1$:** $(\cos\theta - i\sin\theta)^1 = \cos\theta - i\sin\theta = \cos(1\cdot\theta) - i\sin(1\cdot\theta)$. True.

**Inductive hypothesis:** Assume $(\cos\theta - i\sin\theta)^k = \cos(k\theta) - i\sin(k\theta)$.

**Inductive step:** $(\cos\theta - i\sin\theta)^{k+1} = [\cos(k\theta) - i\sin(k\theta)] \cdot [\cos\theta - i\sin\theta]$.

Expand: $\cos(k\theta)\cos\theta - i\cos(k\theta)\sin\theta - i\sin(k\theta)\cos\theta + i^2\sin(k\theta)\sin\theta$.

Since $i^2 = -1$, the last term is $-\sin(k\theta)\sin\theta$. Real part: $\cos(k\theta)\cos\theta - \sin(k\theta)\sin\theta = \cos(k\theta + \theta)$. Imaginary part: $-[\cos(k\theta)\sin\theta + \sin(k\theta)\cos\theta]i = -i\sin(k\theta + \theta)$. Result: $\cos((k+1)\theta) - i\sin((k+1)\theta)$.

### Problem 5

(a) $M^2 = \begin{pmatrix} 1 & a \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 1 & a \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 2a \\ 0 & 1 \end{pmatrix}$

$M^3 = M^2 \cdot M = \begin{pmatrix} 1 & 2a \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 1 & a \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 3a \\ 0 & 1 \end{pmatrix}$

(b) The pattern is $M^n = \begin{pmatrix} 1 & na \\ 0 & 1 \end{pmatrix}$.

(c) **Proof by induction:**

- **Base case $n = 1$:** $M^1 = \begin{pmatrix} 1 & 1\cdot a \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & a \\ 0 & 1 \end{pmatrix}$, which is indeed $M$.

- **Inductive hypothesis:** Assume $M^k = \begin{pmatrix} 1 & ka \\ 0 & 1 \end{pmatrix}$ for some positive integer $k$.

- **Inductive step:** $M^{k+1} = M^k \cdot M = \begin{pmatrix} 1 & ka \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 1 & a \\ 0 & 1 \end{pmatrix}$.

Multiply: row 1 col 1 = $(1)(1) + (ka)(0) = 1$; row 1 col 2 = $(1)(a) + (ka)(1) = a + ka = (k+1)a$; row 2 col 1 = $(0)(1) + (1)(0) = 0$; row 2 col 2 = $(0)(a) + (1)(1) = 1$.

So $M^{k+1} = \begin{pmatrix} 1 & (k+1)a \\ 0 & 1 \end{pmatrix}$, which matches the conjectured formula for $n = k+1$. By induction, the formula holds for all $n \in \mathbb{N}$.
