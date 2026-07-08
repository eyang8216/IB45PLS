# Lesson 8: Sequences — Convergence and Divergence

## What Is a Sequence and Why Does It Matter?

A **sequence** is an ordered list of numbers. We write a sequence as $\{a_n\}_{n=1}^{\infty}$, which means "the list of numbers $a_1, a_2, a_3, a_4, \dots$ where the pattern continues forever." The letter $n$ is called the **index**, and it tells us which position we are at in the list. The expression $a_n$ is called the **$n$-th term** or the **general term** of the sequence. It is a formula that tells us how to compute any term from its position number.

For example, the sequence defined by $a_n = \frac{1}{n}$ produces the terms $1, \frac{1}{2}, \frac{1}{3}, \frac{1}{4}, \dots$. The sequence defined by $a_n = 2^n$ produces $2, 4, 8, 16, \dots$. The sequence defined by $a_n = (-1)^n$ produces $-1, 1, -1, 1, \dots$, oscillating between two values.

Sequences matter because they are the foundation of infinite series, which we will study in later lessons. Every infinite series is built from a sequence of terms, and understanding whether a sequence converges or diverges is the first step toward understanding the behavior of series. Sequences also model discrete processes in science and economics: population growth from year to year, compound interest computed at regular intervals, and iterative algorithms in computer science all involve sequences.

A useful way to think about a sequence is as a function whose domain is the set of natural numbers $\{1, 2, 3, \dots\}$. Just as we can ask about the limit of a function $f(x)$ as $x \to \infty$, we can ask about the limit of a sequence $a_n$ as $n \to \infty$.

## Convergence: The Central Definition

A sequence $\{a_n\}$ **converges** if its terms approach a specific finite number $L$ as $n$ becomes larger and larger. We write:

$$\lim_{n \to \infty} a_n = L$$

This means that no matter how small a tolerance we choose, eventually all terms of the sequence will be within that tolerance of $L$. The number $L$ is called the **limit** of the sequence.

For a sequence to converge, the limit $L$ must be a finite real number. It is not enough for the terms to just "get big" or "stay bounded." The terms must actually settle down and approach one specific value.

A simple example is $a_n = \frac{1}{n}$. As $n$ increases, $\frac{1}{n}$ gets smaller and smaller, approaching $0$. We say this sequence converges to $0$.

## Divergence: When a Sequence Does Not Converge

A sequence **diverges** if it does not converge to any finite limit. Divergence can happen in several distinct ways:

- **Growing without bound:** The terms become larger and larger without approaching any ceiling. Example: $a_n = n^2$ produces $1, 4, 9, 16, \dots$ and grows toward infinity.
- **Decreasing without bound (negative):** The terms become more and more negative. Example: $a_n = -2^n$ produces $-2, -4, -8, -16, \dots$.
- **Oscillating without settling:** The terms bounce between values and never approach a single number. Example: $a_n = (-1)^n$ produces $-1, 1, -1, 1, \dots$. The sequence never decides where to go.
- **Oscillating with growing amplitude:** The terms bounce between values that get farther apart. Example: $a_n = (-1)^n \cdot n$ produces $-1, 2, -3, 4, \dots$.

A crucial point: saying that a sequence "goes to infinity" (like $a_n = n^2$) is still called divergence. Convergence requires the limit to be a finite number. This is a common point of confusion for students.

---

## Techniques for Finding Limits of Sequences

### Technique 1: Dominant Terms for Rational Expressions

When the general term $a_n$ is a fraction of polynomials in $n$, the behavior as $n \to \infty$ is determined by the highest powers of $n$ in the numerator and denominator. The standard method is to divide every term in both numerator and denominator by the highest power of $n$ that appears in the denominator. Each term of the form $\frac{\text{constant}}{n^k}$ then approaches $0$ as $n \to \infty$.

**Worked Example 1:** Determine whether $a_n = \dfrac{2n+1}{3n-4}$ converges.

Divide numerator and denominator by $n$ (the highest power in the denominator):

$$\lim_{n\to\infty} \frac{2n+1}{3n-4} = \lim_{n\to\infty} \frac{2 + \frac{1}{n}}{3 - \frac{4}{n}} = \frac{2+0}{3-0} = \frac{2}{3}$$

Since the limit is a finite number, the sequence **converges to $\frac{2}{3}$**.

**Worked Example 2:** Determine whether $a_n = \dfrac{n^2 + 5}{2n^3 - n}$ converges.

Divide numerator and denominator by $n^3$ (the highest power in the denominator):

$$\lim_{n\to\infty} \frac{n^2+5}{2n^3-n} = \lim_{n\to\infty} \frac{\frac{1}{n} + \frac{5}{n^3}}{2 - \frac{1}{n^2}} = \frac{0+0}{2-0} = 0$$

**Converges to $0$.**

**Worked Example 3:** Determine whether $a_n = \dfrac{4n^3 - n}{n^2 + 7}$ converges.

Divide numerator and denominator by $n^2$:

$$\lim_{n\to\infty} \frac{4n - \frac{1}{n}}{1 + \frac{7}{n^2}} = \frac{\infty - 0}{1+0} = \infty$$

**Diverges to $\infty$.**

From these examples, a pattern emerges for rational sequences:

- If the degree of the numerator is less than the degree of the denominator, the limit is $0$.
- If the degrees are equal, the limit is the ratio of the leading coefficients.
- If the degree of the numerator is greater, the sequence diverges (to $\infty$ or $-\infty$ depending on signs).

---

### Technique 2: L'Hôpital's Rule via the Continuous Analog

If the general term $a_n$ can be written as $f(n)$ where $f(x)$ is a differentiable function of a real variable, and if the limit is of the indeterminate form $\frac{\infty}{\infty}$ or $\frac{0}{0}$, we can apply L'Hôpital's Rule to $f(x)$ and then transfer the result back to the sequence.

**Worked Example 4:** Determine whether $a_n = \dfrac{\ln n}{n}$ converges.

Consider $f(x) = \frac{\ln x}{x}$. As $x \to \infty$, both numerator and denominator go to $\infty$, giving the indeterminate form $\frac{\infty}{\infty}$. Apply L'Hôpital's Rule: differentiate numerator and denominator separately:

$$\lim_{x\to\infty} \frac{\ln x}{x} = \lim_{x\to\infty} \frac{1/x}{1} = \lim_{x\to\infty} \frac{1}{x} = 0$$

Therefore $\lim_{n\to\infty} \frac{\ln n}{n} = 0$. The sequence **converges to $0$**.

**Worked Example 5:** Determine whether $a_n = n e^{-n} = \dfrac{n}{e^n}$ converges.

Consider $f(x) = \frac{x}{e^x}$. This is $\frac{\infty}{\infty}$. Apply L'Hôpital:

$$\lim_{x\to\infty} \frac{x}{e^x} = \lim_{x\to\infty} \frac{1}{e^x} = 0$$

**Converges to $0$.** The exponential function grows much faster than any polynomial, so $\frac{n}{e^n} \to 0$ for any power of $n$.

---

### Technique 3: The Squeeze Theorem

The Squeeze Theorem (also called the Sandwich Theorem) says: if we can trap a sequence between two simpler sequences that both approach the same limit, then the trapped sequence must approach that limit as well. Formally, if $b_n \leq a_n \leq c_n$ for all sufficiently large $n$, and $\lim b_n = \lim c_n = L$, then $\lim a_n = L$.

**Worked Example 6:** Determine whether $a_n = \dfrac{\sin n}{n}$ converges.

The sine function always gives values between $-1$ and $1$: $-1 \leq \sin n \leq 1$ for every $n$. Dividing all parts of this inequality by $n$ (which is positive for $n \geq 1$):

$$-\frac{1}{n} \leq \frac{\sin n}{n} \leq \frac{1}{n}$$

Both $-\frac{1}{n}$ and $\frac{1}{n}$ approach $0$ as $n \to \infty$. By the Squeeze Theorem, the sequence in the middle must also approach $0$. **Converges to $0$.**

---

### Technique 4: Famous Limits Worth Memorizing

Some sequences have limits that are not obvious from the techniques above but appear frequently enough to be worth memorizing:

- $\displaystyle\lim_{n\to\infty} \left(1 + \frac{1}{n}\right)^n = e$ (this is actually a definition of the number $e$).
- $\displaystyle\lim_{n\to\infty} \frac{\ln n}{n^p} = 0$ for any $p > 0$ (logarithms grow slower than any power function).
- $\displaystyle\lim_{n\to\infty} \frac{n^p}{e^n} = 0$ for any $p > 0$ (exponentials grow faster than any power function).
- $\displaystyle\lim_{n\to\infty} \sqrt[n]{n} = n^{1/n} \to 1$.
- $\displaystyle\lim_{n\to\infty} r^n = 0$ if $|r| < 1$. If $|r| > 1$, the sequence diverges. If $r = 1$, the limit is $1$. If $r = -1$, the sequence oscillates and diverges.

---

### Technique 5: Handling Oscillation from $(-1)^n$

When a sequence contains the factor $(-1)^n$ or $(-1)^{n-1}$, the sign alternates with each term. Whether the sequence converges depends on what the alternating factor is multiplied by:

- If the non-alternating part approaches $0$, the sequence converges to $0$ (the oscillations get smaller and smaller).
- If the non-alternating part approaches a nonzero number $L$, the sequence oscillates between values approaching $L$ and $-L$, and diverges.
- If the non-alternating part grows without bound, the sequence oscillates with increasing amplitude and diverges.

For example, $a_n = \frac{(-1)^n}{n}$ converges to $0$ because the amplitude $\frac{1}{n} \to 0$. But $a_n = (-1)^n \cdot \frac{n}{n+1}$ diverges because the amplitude $\frac{n}{n+1} \to 1$, so the sequence oscillates between values approaching $1$ and $-1$.

---

## Practice Problems

For each sequence, determine whether it converges or diverges. If it converges, state the limit.

### Problem 1
A sequence is defined by $a_n = \dfrac{5n - 3}{2n + 7}$ for $n \geq 1$. Determine whether this sequence converges, and if so, find its limit.

### Problem 2
A sequence is defined by $a_n = \dfrac{n^2 + 1}{n^3 - n}$ for $n \geq 2$. Determine whether this sequence converges, and if so, find its limit.

### Problem 3
A sequence is defined by $a_n = \dfrac{3n^3 - 2n}{n^2 + 5}$ for $n \geq 1$. Determine whether this sequence converges, and if so, find its limit.

### Problem 4
A sequence is defined by $a_n = \dfrac{(-1)^n}{n^2}$ for $n \geq 1$. Determine whether this sequence converges, and if so, find its limit.

### Problem 5
A sequence is defined by $a_n = (-1)^n \cdot \dfrac{n^2}{n^2 + 1}$ for $n \geq 1$.
(a) State whether the sequence converges or diverges. [2 marks]
(b) Justify your answer by analyzing the behavior of the non-alternating factor. [3 marks]

### Problem 6
A sequence is defined by $a_n = \dfrac{\cos(3n)}{\sqrt{n}}$ for $n \geq 1$. Use the Squeeze Theorem to determine whether this sequence converges, and if so, find its limit.

### Problem 7
A sequence is defined by $a_n = \left(1 + \dfrac{2}{n}\right)^n$ for $n \geq 1$. Determine whether this sequence converges, and if so, find its limit.

---

## Answers

### Answer 1

To find the limit, we divide numerator and denominator by the highest power of $n$ in the denominator, which is $n$: $\lim_{n\to\infty} \frac{5n-3}{2n+7} = \lim_{n\to\infty} \frac{5 - \frac{3}{n}}{2 + \frac{7}{n}}$. As $n \to \infty$, the fractions $\frac{3}{n}$ and $\frac{7}{n}$ both approach $0$. The limit is therefore $\frac{5}{2}$. The sequence converges to $\frac{5}{2}$.

### Answer 2

Divide numerator and denominator by $n^3$, the highest power in the denominator: $\lim_{n\to\infty} \frac{n^2+1}{n^3-n} = \lim_{n\to\infty} \frac{\frac{1}{n} + \frac{1}{n^3}}{1 - \frac{1}{n^2}}$. Both $\frac{1}{n}$ and $\frac{1}{n^3}$ approach $0$, and $\frac{1}{n^2}$ approaches $0$. The limit is $\frac{0}{1} = 0$. The sequence converges to $0$. A common error is to only look at the leading terms and conclude the limit is $\frac{n^2}{n^3} = \frac{1}{n} \to 0$, which happens to give the right answer here, but the proper method of dividing through by $n^3$ is more reliable.

### Answer 3

Divide by $n^2$, the highest power in the denominator: $\lim_{n\to\infty} \frac{3n^3-2n}{n^2+5} = \lim_{n\to\infty} \frac{3n - \frac{2}{n}}{1 + \frac{5}{n^2}}$. As $n \to \infty$, $3n \to \infty$ while $\frac{2}{n} \to 0$, so the numerator approaches $\infty$. The denominator approaches $1$. The limit is therefore $\infty$. The sequence diverges to $\infty$.

### Answer 4

The factor $(-1)^n$ causes alternating signs, but the amplitude is $\frac{1}{n^2}$, which approaches $0$. Using the Squeeze Theorem: $-\frac{1}{n^2} \leq \frac{(-1)^n}{n^2} \leq \frac{1}{n^2}$. Both bounds approach $0$, so the sequence converges to $0$. The oscillations become smaller and smaller, eventually indistinguishable from $0$.

### Answer 5

(a) The sequence diverges.

(b) The non-alternating factor is $\frac{n^2}{n^2+1}$. As $n \to \infty$, this factor approaches $1$ (divide numerator and denominator by $n^2$: $\frac{1}{1 + 1/n^2} \to \frac{1}{1+0} = 1$). Because $(-1)^n$ oscillates between $1$ and $-1$, the sequence as a whole oscillates between values that approach $1$ and $-1$, never settling on a single limit. A common mistake is to think that any sequence containing $(-1)^n$ diverges, but if the non-alternating factor goes to $0$, the sequence converges to $0$. Here the non-alternating factor does not go to $0$, so the sequence diverges.

### Answer 6

The cosine function satisfies $-1 \leq \cos(3n) \leq 1$ for every $n$. Since $\sqrt{n} > 0$ for $n \geq 1$, dividing by $\sqrt{n}$ preserves the inequality direction: $-\frac{1}{\sqrt{n}} \leq \frac{\cos(3n)}{\sqrt{n}} \leq \frac{1}{\sqrt{n}}$. Both $-\frac{1}{\sqrt{n}}$ and $\frac{1}{\sqrt{n}}$ converge to $0$ as $n \to \infty$. By the Squeeze Theorem, the sequence $\frac{\cos(3n)}{\sqrt{n}}$ also converges to $0$.

### Answer 7

This is a variation of the famous limit $\lim_{n\to\infty} (1 + \frac{k}{n})^n = e^k$. Here $k = 2$, so the limit is $e^2$. Alternatively, we can rewrite: $(1 + \frac{2}{n})^n = [(1 + \frac{2}{n})^{n/2}]^2$. The inner expression $(1 + \frac{2}{n})^{n/2}$ approaches $e$ as $n \to \infty$ (this is the definition of $e$ with a substitution $m = n/2$). Squaring gives $e^2$. The sequence converges to $e^2$.

---

## Key Takeaways

1. A sequence converges if its terms approach a finite limit as $n \to \infty$. It diverges if the terms grow without bound, oscillate without settling, or approach no finite number.
2. For rational expressions in $n$, divide by the highest power in the denominator. The limit is $0$ if numerator degree is less, the ratio of leading coefficients if degrees are equal, and $\pm\infty$ if numerator degree is greater.
3. L'Hôpital's Rule applied to the continuous analog works for indeterminate forms like $\frac{\infty}{\infty}$ and $\frac{0}{0}$.
4. The Squeeze Theorem is powerful for sequences involving $\sin n$, $\cos n$, or $(-1)^n$ divided by something that grows.
5. The alternating factor $(-1)^n$ alone does not determine convergence. What matters is whether the amplitude approaches $0$.

