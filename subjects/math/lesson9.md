# Lesson 9: Infinite Series and Geometric Series

## What Is an Infinite Series and Why Does It Matter?

Imagine you start walking toward a wall. Each step covers half the remaining distance. You take a step of 1 metre, then half a metre, then a quarter metre, and so on forever. Will you ever reach the wall?

An **infinite series** answers questions like this. An infinite series is what happens when you add up all the terms of a sequence that never ends. We write it using sigma notation:

$$\sum_{n=1}^{\infty} a_n = a_1 + a_2 + a_3 + a_4 + \cdots$$

The symbol $\sum$ (the Greek letter sigma) means "add up." The subscript $n=1$ tells you to start at the first term, and $\infty$ means you never stop.

Why does this matter? Infinite series appear everywhere in mathematics and science. They let us represent numbers exactly (like writing $0.333\ldots$ as a fraction), compute values of functions like sine and cosine, and model things like cooling objects and electrical circuits. The central question is: can adding infinitely many numbers ever give a finite answer?

---

## The Key Idea: Partial Sums

Since you cannot literally add infinitely many numbers, mathematicians use a clever trick. Instead of adding all terms at once, you add them one at a time and watch what happens.

A **partial sum** is the total after you have added a certain number of terms. The $N$-th partial sum, written $S_N$, is the sum of the first $N$ terms:

$$S_1 = a_1$$
$$S_2 = a_1 + a_2$$
$$S_3 = a_1 + a_2 + a_3$$
$$\vdots$$
$$S_N = a_1 + a_2 + \cdots + a_N$$

Now we look at what happens to the sequence of partial sums $S_1, S_2, S_3, \ldots$ as $N$ gets larger and larger.

Suppose the partial sums creep closer and closer to some fixed number $S$. Perhaps $S_1 = 0.5$, then $S_2 = 0.75$, then $S_3 = 0.875$, and so on, clearly heading toward $1$. In that case, we say the series **converges** to $S$, and we write:

$$\sum_{n=1}^{\infty} a_n = S$$

If the partial sums do not approach any particular number — maybe they grow bigger and bigger without bound, or they bounce around forever — then we say the series **diverges**.

Many students think that as long as the terms $a_n$ themselves get smaller the series must converge. But that is not true. The terms getting smaller is necessary for convergence, but it is not enough by itself. The classic counterexample is the harmonic series, which we will see later in this course.

---

## A First Look: A Series That Diverges

Consider the simplest possible infinite series — just adding the number $1$ over and over forever:

$$\sum_{n=1}^{\infty} 1 = 1 + 1 + 1 + 1 + \cdots$$

After $N$ terms, the partial sum is $S_N = N$. As $N$ goes to infinity, $S_N$ also goes to infinity. There is no fixed number the sum approaches. Therefore this series diverges. This is not surprising since the terms themselves do not get smaller — they stay at $1$ forever.

---

## A Series That Converges: Telescoping

There is a special type of series called a **telescoping series**, where most of the terms cancel out when you write the partial sum. Think of it like a collapsible telescope: only the ends remain.

Consider this series:

$$\sum_{n=1}^{\infty} \frac{1}{n(n+1)}$$

Let us write out the first few terms. But first we need a useful trick from algebra. The fraction $\frac{1}{n(n+1)}$ can be split into two simpler fractions using **partial fractions**:

$$\frac{1}{n(n+1)} = \frac{1}{n} - \frac{1}{n+1}$$

Now write out the first few terms of the series using this split:

$$n=1: \quad \frac{1}{1} - \frac{1}{2}$$
$$n=2: \quad \frac{1}{2} - \frac{1}{3}$$
$$n=3: \quad \frac{1}{3} - \frac{1}{4}$$
$$n=4: \quad \frac{1}{4} - \frac{1}{5}$$

When you add these, something beautiful happens. The $-\frac{1}{2}$ from the first term cancels with the $+\frac{1}{2}$ from the second. The $-\frac{1}{3}$ from the second cancels with the $+\frac{1}{3}$ from the third. Almost everything cancels.

The $N$-th partial sum, after all the cancellations, leaves only:

$$S_N = 1 - \frac{1}{N+1}$$

Now let $N$ go to infinity. The fraction $\frac{1}{N+1}$ approaches $0$. Therefore:

$$\lim_{N\to\infty} S_N = 1 - 0 = 1$$

The series converges, and its sum is exactly $1$.

---

## The Geometric Series: The Most Important Series in This Course

A **geometric series** is formed by starting with a first term and then multiplying by the same number (called the **common ratio**) to get each next term. The pattern is:

$$\sum_{n=1}^{\infty} ar^{n-1} = a + ar + ar^2 + ar^3 + \cdots$$

Here $a$ is the first term and $r$ is the common ratio. The exponent $n-1$ just makes the first term nice: when $n=1$, $ar^{1-1} = ar^0 = a$.

Every term is $r$ times the previous one. For example, the series $4 + 2 + 1 + \frac{1}{2} + \cdots$ is geometric because each term is $\frac{1}{2}$ times the one before it.

---

### Deriving the Sum Formula

Let us find a formula for the $N$-th partial sum of a geometric series. Write it out:

$$S_N = a + ar + ar^2 + \cdots + ar^{N-1}$$

Now multiply both sides by $r$:

$$rS_N = ar + ar^2 + ar^3 + \cdots + ar^N$$

Notice that both $S_N$ and $rS_N$ share many of the same terms. Subtract the second equation from the first:

$$S_N - rS_N = (a + ar + ar^2 + \cdots + ar^{N-1}) - (ar + ar^2 + \cdots + ar^N)$$

Almost everything on the right cancels. Only $a$ from the first bracket and $-ar^N$ from the second bracket survive:

$$S_N - rS_N = a - ar^N$$

Factor out $S_N$ on the left:

$$S_N(1 - r) = a(1 - r^N)$$

Divide both sides by $(1 - r)$, as long as $r \neq 1$:

$$S_N = \frac{a(1 - r^N)}{1 - r}$$

This is the formula for the $N$-th partial sum of a geometric series.

Now the critical question: what happens when $N$ goes to infinity? The only part that depends on $N$ is $r^N$.

If $|r| < 1$ (that is, $r$ is strictly between $-1$ and $1$), then raising $r$ to larger and larger powers makes $r^N$ shrink toward $0$. For example, $(0.5)^{10} \approx 0.001$, and $(0.5)^{100}$ is tiny beyond imagination. So $r^N \to 0$ as $N \to \infty$, and:

$$\sum_{n=1}^{\infty} ar^{n-1} = \frac{a}{1 - r} \qquad \text{whenever } |r| < 1$$

If $|r| \geq 1$, then $r^N$ does not shrink to $0$. For example, if $r = 2$, then $2^N$ grows without bound. If $r = 1$, every term is just $a$, and we are adding $a$ infinitely many times. In all such cases the series diverges.

The condition $|r| < 1$ is what determines convergence. Always check it first.

---

## Worked Examples

### Worked Example 1

Find the sum of the series $4 + 2 + 1 + \dfrac{1}{2} + \cdots$.

**Approach:** This looks like a geometric series because each term appears to be half of the previous one. We need to identify the first term $a$ and the common ratio $r$, verify that $|r| < 1$, and then use the formula.

**Step 1:** Identify the first term. The first term is $a = 4$.

**Step 2:** Find the common ratio. Divide the second term by the first: $r = \frac{2}{4} = \frac{1}{2}$.

**Step 3:** Check the condition. $|r| = \frac{1}{2} < 1$, so the series converges.

**Step 4:** Apply the sum formula:

$$\text{Sum} = \frac{a}{1 - r} = \frac{4}{1 - \frac{1}{2}} = \frac{4}{\frac{1}{2}} = 8$$

**Why this makes sense:** The first term is $4$, and each subsequent term is half the previous one. The sum should be larger than $4$ but not enormous because the terms quickly become tiny. After $4$ terms the sum is $4 + 2 + 1 + 0.5 = 7.5$. After $5$ it is $7.75$. After $6$ it is $7.875$. The partial sums are clearly approaching $8$, which confirms our formula.

**Answer: $8$**

---

### Worked Example 2

Find the sum of the series $3 - 1 + \dfrac{1}{3} - \dfrac{1}{9} + \cdots$.

**Approach:** The signs alternate, but the pattern of multiplying by the same number each time still holds. We find $a$ and $r$, check $|r|$, and apply the formula.

**Step 1:** First term: $a = 3$.

**Step 2:** Common ratio: divide the second term by the first: $r = \frac{-1}{3} = -\frac{1}{3}$.

**Step 3:** Check: $|r| = \frac{1}{3} < 1$, so the series converges.

**Step 4:** Apply the formula:

$$\text{Sum} = \frac{3}{1 - \left(-\frac{1}{3}\right)} = \frac{3}{1 + \frac{1}{3}} = \frac{3}{\frac{4}{3}} = 3 \times \frac{3}{4} = \frac{9}{4}$$

**Why this makes sense:** The terms alternate between positive and negative, with shrinking magnitudes. The sum should settle somewhere between $3$ and $3 - 1 = 2$. Indeed, $\frac{9}{4} = 2.25$ is right in that range.

**Answer: $\frac{9}{4}$**

---

### Worked Example 3

Find the sum of the series written in sigma notation: $\displaystyle\sum_{n=1}^{\infty} 5 \cdot \left(\frac{2}{3}\right)^{n-1}$.

**Approach:** This is already in the standard geometric series form $\sum ar^{n-1}$. We can read $a$ and $r$ directly.

**Step 1:** Comparing to $ar^{n-1}$, we see $a = 5$ and $r = \frac{2}{3}$.

**Step 2:** Check: $|r| = \frac{2}{3} < 1$. Converges.

**Step 3:** Sum formula:

$$\text{Sum} = \frac{5}{1 - \frac{2}{3}} = \frac{5}{\frac{1}{3}} = 15$$

**Why this makes sense:** Each term is $\frac{2}{3}$ of the previous one, so the sum should be larger than the first term ($5$) but smaller than infinite growth. Dividing by $1 - \frac{2}{3} = \frac{1}{3}$ effectively multiplies by $3$, giving $15$.

**Answer: $15$**

---

### Worked Example 4: Index Shift

Find the sum of $\displaystyle\sum_{n=2}^{\infty} \left(\frac{1}{2}\right)^n$.

**Approach:** The standard formula works when the sum starts at $n=1$ with $ar^{n-1}$ or at $n=0$ with $ar^n$. Here the sum starts at $n=2$, so the first term is $(\frac{1}{2})^2 = \frac{1}{4}$. We can think of this as a geometric series starting at a later term.

**Step 1:** Factor out the first term. Write the series as:

$$\sum_{n=2}^{\infty} \left(\frac{1}{2}\right)^n = \left(\frac{1}{2}\right)^2 + \left(\frac{1}{2}\right)^3 + \left(\frac{1}{2}\right)^4 + \cdots$$

**Step 2:** Factor out $(\frac{1}{2})^2 = \frac{1}{4}$:

$$= \frac{1}{4}\left(1 + \frac{1}{2} + \left(\frac{1}{2}\right)^2 + \cdots\right)$$

**Step 3:** The bracket is a standard geometric series with $a = 1$ and $r = \frac{1}{2}$. Its sum is $\frac{1}{1 - \frac{1}{2}} = 2$.

**Step 4:** Multiply: $\frac{1}{4} \times 2 = \frac{1}{2}$.

**Why this makes sense:** Another way: the full series starting from $n=0$ sums to $\frac{1}{1 - 1/2} = 2$, which is $1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \cdots$. Our series starts at $\frac{1}{4}$, so it is the full sum minus the first two terms: $2 - 1 - \frac{1}{2} = \frac{1}{2}$. Both methods agree.

**Answer: $\frac{1}{2}$**

---

### Worked Example 5: Repeating Decimal as a Geometric Series

Express the repeating decimal $0.7777\ldots$ as a fraction in lowest terms.

**Approach:** A repeating decimal can be thought of as an infinite geometric series. Each digit position represents a power of one-tenth.

**Step 1:** Write the decimal as a sum of fractions:

$$0.7777\ldots = \frac{7}{10} + \frac{7}{100} + \frac{7}{1000} + \frac{7}{10000} + \cdots$$

**Step 2:** Identify the geometric series. Each term is $\frac{1}{10}$ times the previous term. So $a = \frac{7}{10}$ and $r = \frac{1}{10}$.

**Step 3:** Check: $|r| = \frac{1}{10} < 1$. Converges.

**Step 4:** Apply the sum formula:

$$\text{Sum} = \frac{\frac{7}{10}}{1 - \frac{1}{10}} = \frac{\frac{7}{10}}{\frac{9}{10}} = \frac{7}{9}$$

**Why this makes sense:** Many students already know that $0.333\ldots = \frac{1}{3}$ and $0.666\ldots = \frac{2}{3}$. Following the pattern, $0.777\ldots$ should be $\frac{7}{9}$, which matches our calculation.

**Answer: $\frac{7}{9}$**

---

## A Quick Check for Divergence: The $n$-th Term Test

Sometimes you can tell immediately that a series diverges without doing any complicated calculations.

**The $n$-th Term Test (Divergence Test):** If the individual terms $a_n$ do not approach $0$ as $n$ goes to infinity, then the series $\sum a_n$ must diverge.

Think about it: if you are adding numbers and the numbers are not getting closer and closer to $0$, the sum cannot settle down to a finite value. It will either grow without bound or oscillate forever.

**Important warning:** The reverse is NOT true. If the terms do approach $0$, the series might converge OR diverge. The $n$-th term test cannot prove convergence — it can only prove divergence.

**Example:** Consider $\displaystyle\sum_{n=1}^{\infty} \frac{n}{2n+1}$.

Look at the general term: $a_n = \frac{n}{2n+1}$.

As $n$ gets very large, the $+1$ in the denominator matters less and less. The ratio $\frac{n}{2n+1}$ approaches $\frac{1}{2}$.

Since $\frac{1}{2} \neq 0$, the terms do not approach $0$, and by the $n$-th term test the series diverges.

---

## Summary

| Series Type | Form | Converges When | Sum Formula |
|---|---|---|---|
| Geometric | $\sum ar^{n-1}$ | $|r| < 1$ | $\dfrac{a}{1 - r}$ |
| Telescoping | $\sum (b_n - b_{n+1})$ | $\lim b_n$ exists | $b_1 - \lim b_n$ |

The geometric series is the one you will use most often. The condition $|r| < 1$ must be burned into memory: if the absolute value of the common ratio is less than $1$, the series converges, and the sum is the first term divided by $(1 - r)$.

---

## Practice Problems

**Problem 1**

Find the sum of the following infinite geometric series: $2 + \dfrac{2}{3} + \dfrac{2}{9} + \dfrac{2}{27} + \cdots$. Show all your working.

**Problem 2**

Find the sum of the series $5 - \dfrac{5}{2} + \dfrac{5}{4} - \dfrac{5}{8} + \cdots$. Identify the first term, the common ratio, and confirm that the series converges before computing the sum.

**Problem 3**

Determine whether the following series converges. If it does, find the sum: $\displaystyle\sum_{n=1}^{\infty} 6 \cdot (0.4)^{n-1}$.

**Problem 4**

Find the sum of $\displaystyle\sum_{n=3}^{\infty} \left(\dfrac{1}{3}\right)^n$. Note that the sum starts at $n=3$, not at $n=1$.

**Problem 5** (IB-style)

An infinite geometric series has a first term of $20$ and a sum of $50$.

(a) Find the common ratio $r$. [3 marks]

(b) Hence, or otherwise, find the sum of the series starting from the third term (that is, the sum $a_3 + a_4 + a_5 + \cdots$). [3 marks]

**Problem 6**

Does the series $\displaystyle\sum_{n=1}^{\infty} \dfrac{3n^2}{n^2 + 4}$ converge or diverge? Justify your answer using an appropriate test. If it diverges, explain why.

---

## Answers

**Answer 1**

We need to identify the first term and the common ratio. The first term is $a = 2$. To find the common ratio, divide the second term by the first: $r = \frac{2/3}{2} = \frac{1}{3}$. Since $|r| = \frac{1}{3} < 1$, the series converges. Now apply the geometric series sum formula:

$$\text{Sum} = \frac{a}{1 - r} = \frac{2}{1 - \frac{1}{3}} = \frac{2}{\frac{2}{3}} = 2 \times \frac{3}{2} = 3$$

So the sum of the infinite series is $3$.

(Common pitfall: forgetting to check $|r| < 1$ first. Always check convergence before using the formula.)

---

**Answer 2**

The first term is $a = 5$. The common ratio is $r = \frac{-5/2}{5} = -\frac{1}{2}$. Because $|r| = \frac{1}{2} < 1$, the series converges. Using the sum formula:

$$\text{Sum} = \frac{a}{1 - r} = \frac{5}{1 - \left(-\frac{1}{2}\right)} = \frac{5}{1 + \frac{1}{2}} = \frac{5}{\frac{3}{2}} = 5 \times \frac{2}{3} = \frac{10}{3}$$

So the sum is $\frac{10}{3}$.

(Common pitfall: when $r$ is negative, the denominator becomes $1 - (-\frac{1}{2}) = 1 + \frac{1}{2} = \frac{3}{2}$. Students often write $1 - \frac{1}{2}$ by mistake.)

---

**Answer 3**

The series is in standard form $\sum ar^{n-1}$. Reading off, we have $a = 6$ and $r = 0.4$. Since $|r| = 0.4 < 1$, the series converges. The sum is:

$$\text{Sum} = \frac{a}{1 - r} = \frac{6}{1 - 0.4} = \frac{6}{0.6} = 10$$

So the series converges to $10$.

---

**Answer 4**

The sum starts at $n = 3$, so the first term is $\left(\frac{1}{3}\right)^3 = \frac{1}{27}$. This is a geometric series with first term $a = \frac{1}{27}$ and common ratio $r = \frac{1}{3}$.

Alternatively, we can factor: the series $\sum_{n=3}^{\infty} \left(\frac{1}{3}\right)^n = \left(\frac{1}{3}\right)^3 \sum_{k=0}^{\infty} \left(\frac{1}{3}\right)^k = \frac{1}{27} \cdot \frac{1}{1 - \frac{1}{3}}$.

Now compute:

$$\frac{1}{27} \times \frac{1}{\frac{2}{3}} = \frac{1}{27} \times \frac{3}{2} = \frac{3}{54} = \frac{1}{18}$$

So the sum is $\frac{1}{18}$.

(Common pitfall: using the formula $\frac{a}{1-r}$ with $a = 1$ instead of $a = (\frac{1}{3})^3$. The formula requires the actual first term of the series you are summing.)

---

**Answer 5**

**(a)** For a geometric series with first term $a = 20$ and sum $S = 50$, we use $S = \frac{a}{1 - r}$. Substitute the known values:

$$50 = \frac{20}{1 - r}$$

Multiply both sides by $(1 - r)$: $50(1 - r) = 20$.

Divide by $50$: $1 - r = \frac{20}{50} = \frac{2}{5}$.

So $r = 1 - \frac{2}{5} = \frac{3}{5}$.

[3 marks: 1 for setting up the equation, 1 for correct algebra, 1 for the correct ratio.]

**(b)** The sum from the third term onward is the total sum minus the first two terms. The total sum is $50$. The first term is $20$. The second term is $ar = 20 \times \frac{3}{5} = 12$. Therefore:

Sum from $n=3$ onward $= 50 - 20 - 12 = 18$.

Alternatively, the series starting at $n=3$ is geometric with first term $ar^2 = 20 \times (\frac{3}{5})^2 = 20 \times \frac{9}{25} = \frac{36}{5} = 7.2$ and common ratio $\frac{3}{5}$. The sum is $\frac{7.2}{1 - 3/5} = 7.2 \times \frac{5}{2} = 18$. Both methods give the same answer.

[3 marks: 1 for finding the second term, 1 for subtracting the first two terms from the total, 1 for the correct answer.]

---

**Answer 6**

We use the $n$-th term test. Look at the general term $a_n = \frac{3n^2}{n^2 + 4}$.

To find the limit as $n \to \infty$, divide the numerator and denominator by the highest power of $n$, which is $n^2$:

$$\lim_{n\to\infty} \frac{3n^2}{n^2 + 4} = \lim_{n\to\infty} \frac{3}{1 + \frac{4}{n^2}} = \frac{3}{1 + 0} = 3$$

The limit of the terms is $3$, which is not $0$. By the $n$-th term test, if the terms do not approach $0$, the series cannot converge. Therefore the series diverges.

(Common pitfall: many students see the $n^2$ in both numerator and denominator and guess the series behaves like $\frac{1}{n^2}$, which would converge. But the numerator has a coefficient of $3$, and the terms approach $3$, not $0$. Always compute the limit of the terms first.)
