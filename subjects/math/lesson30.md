# Lesson 30: Proof by Induction — Summation Formulas

## WHAT Is Mathematical Induction?

Imagine someone tells you a formula and claims it works for every positive whole number \(n = 1, 2, 3, \dots\) forever. You could test \(n = 1\) — it works. Then \(n = 2\) — it works too. Then \(n = 3\) — still works. But how can you be sure it works for \(n = 1000\), or \(n = 1000000\), without checking every single case? You cannot check infinitely many numbers one by one.

**Mathematical induction** is a method of proof that solves this problem. It lets you prove that a statement is true for all positive whole numbers using just two steps. The method is like setting up a chain of dominoes where knocking over the first one guarantees that every domino in the line will fall.

## WHY Learn Induction?

Induction is one of the most important proof techniques in mathematics. It appears throughout the IB AAHL syllabus — summation formulas, divisibility, inequalities, matrix powers, and more. It also teaches you a way of thinking: if you can prove that "true for \(k\)" forces "true for \(k+1\)," and you already know it is true for the starting value, then it must be true everywhere. This logical structure shows up in computer science (proving algorithms are correct), in engineering, and in any field that uses discrete mathematics.

---

## 1. The Domino Analogy

Picture a long row of dominoes standing on end. Two things need to happen for all the dominoes to fall:

1. **You knock over the first domino.** If the first one never falls, the chain never starts.
2. **Each domino is close enough to knock over the next one.** When domino \(k\) falls, it hits domino \(k+1\) and makes it fall too.

If both conditions are met, every domino in the row will fall — the first falls, which knocks over the second, which knocks over the third, and so on forever.

Mathematical induction uses exactly this logic:

1. **Base case:** Prove the statement is true for \(n = 1\) (or whatever the first value is). This is knocking over the first domino.
2. **Inductive step:** Prove that if the statement is true for \(n = k\) (where \(k\) is any positive whole number), then it must also be true for \(n = k+1\). This is showing that each domino knocks over the next one.

Once both steps are done, the statement is guaranteed true for \(n = 1, 2, 3, \dots\) forever. No further checking is needed.

---

## 2. The Three-Part Structure of an Induction Proof

Every induction proof follows the same structure. Learning this structure is half the battle.

| Part | What You Do | How to Write It |
|------|-------------|-----------------|
| **1. Statement** | Name the claim you are proving and call it \(P(n)\) | "Let \(P(n)\) be the statement that ..." |
| **2. Base case** | Verify \(P(1)\) is true by direct calculation | "When \(n = 1\): LHS = ..., RHS = ..., so \(P(1)\) is true." |
| **3. Inductive hypothesis** | Assume \(P(k)\) is true for some arbitrary \(k\) | "Assume \(P(k)\) is true for some \(k \in \mathbb{N}\). That is: ..." |
| **4. Inductive step** | Starting from \(P(k)\), prove \(P(k+1)\) | "We must show that \(P(k+1)\) is true. Starting from the LHS of \(P(k+1)\): ..." |
| **5. Conclusion** | State that induction is complete | "By the principle of mathematical induction, \(P(n)\) is true for all \(n \in \mathbb{N}\)." |

**Common misconception:** Some students think the inductive hypothesis means "assume the statement is true for all \(n\)." That would be assuming exactly what you are trying to prove! You only assume it for one arbitrary value \(k\), and then prove that this forces it to be true for the next value \(k+1\).

---

## 3. The Core Strategy for Summation Induction

When the statement \(P(n)\) involves a sum (sigma notation), the inductive step almost always follows the same pattern:

1. **Split the sum:** Write the sum up to \(k+1\) as the sum up to \(k\), plus the \((k+1)\)-th term.
2. **Apply the hypothesis:** Replace the sum up to \(k\) with the formula from \(P(k)\).
3. **Algebraically combine:** Get a common denominator if needed, factor, and simplify until the expression matches the right-hand side of \(P(k+1)\).

---

## 4. Worked Example 1: Sum of the First \(n\) Natural Numbers

**Problem:** Prove that for all positive whole numbers \(n\):

\[
1 + 2 + 3 + \dots + n = \frac{n(n+1)}{2}
\]

**Approach:** Let \(P(n)\) name this statement. Check the base case \(n=1\). Then assume \(P(k)\) and try to prove \(P(k+1)\) by splitting the sum and using the hypothesis.

**Step 1 — Define the statement:**
Let \(P(n)\) be the statement: \(\displaystyle\sum_{r=1}^{n} r = \frac{n(n+1)}{2}\).

This sigma notation \(\sum_{r=1}^{n} r\) just means "add up \(r\) for every whole number \(r\) from 1 to \(n\)."

**Step 2 — Base case (\(n = 1\)):**

Left-hand side (LHS): \(\sum_{r=1}^{1} r = 1\).

Right-hand side (RHS): \(\frac{1(1+1)}{2} = \frac{1 \cdot 2}{2} = 1\).

LHS = RHS, so \(P(1)\) is true. The first domino has fallen.

**Step 3 — Inductive hypothesis:**
Assume \(P(k)\) is true for some \(k \in \mathbb{N}\). That is, assume:

\[
\sum_{r=1}^{k} r = \frac{k(k+1)}{2}
\]

This is your tool — you get to use it in the next step.

**Step 4 — Inductive step (prove \(P(k+1)\)):**
We need to show that \(P(k+1)\) is true:

\[
\sum_{r=1}^{k+1} r = \frac{(k+1)(k+2)}{2}
\]

Start from the left-hand side of \(P(k+1)\) and try to reach the right-hand side:

\[
\begin{aligned}
\sum_{r=1}^{k+1} r &= \underbrace{\sum_{r=1}^{k} r}_{\text{this is the hypothesis!}} + \;(k+1) \\[6pt]
&= \frac{k(k+1)}{2} + (k+1) \qquad \text{(substituting the hypothesis)} \\[6pt]
&= \frac{k(k+1)}{2} + \frac{2(k+1)}{2} \qquad \text{(common denominator 2)} \\[6pt]
&= \frac{k(k+1) + 2(k+1)}{2} \\[6pt]
&= \frac{(k+1)(k + 2)}{2} \qquad \text{(factor out }k+1\text{)} \\[6pt]
&= \frac{(k+1)((k+1)+1)}{2}
\end{aligned}
\]

This is exactly the right-hand side of \(P(k+1)\). So \(P(k+1)\) is true whenever \(P(k)\) is true.

**Step 5 — Conclusion:**
By the principle of mathematical induction, \(P(n)\) is true for all \(n \in \mathbb{N}\).

**Why this makes sense:** The formula \(\frac{n(n+1)}{2}\) is often called the "triangular number" formula. For \(n = 5\), it gives \(\frac{5 \cdot 6}{2} = 15\), and indeed \(1+2+3+4+5 = 15\). The induction proof guarantees that this formula works for every \(n\), not just the ones you check by hand.

---

## 5. Worked Example 2: Sum of Squares

**Problem:** Prove that for all positive whole numbers \(n\):

\[
1^2 + 2^2 + 3^2 + \dots + n^2 = \frac{n(n+1)(2n+1)}{6}
\]

**Approach:** Same structure. The algebra in the inductive step will be slightly longer because the target expression has more factors.

**Step 1:** Let \(P(n)\) be: \(\displaystyle\sum_{r=1}^{n} r^2 = \frac{n(n+1)(2n+1)}{6}\).

**Step 2 — Base case (\(n = 1\)):**
LHS: \(1^2 = 1\).
RHS: \(\frac{1(1+1)(2\cdot1+1)}{6} = \frac{1 \cdot 2 \cdot 3}{6} = \frac{6}{6} = 1\).
LHS = RHS, so \(P(1)\) is true.

**Step 3 — Inductive hypothesis:**
Assume \(P(k)\): \(\displaystyle\sum_{r=1}^{k} r^2 = \frac{k(k+1)(2k+1)}{6}\).

**Step 4 — Inductive step:**
We need to prove \(P(k+1)\): \(\displaystyle\sum_{r=1}^{k+1} r^2 = \frac{(k+1)(k+2)(2k+3)}{6}\).

Starting from the LHS:

\[
\begin{aligned}
\sum_{r=1}^{k+1} r^2 &= \underbrace{\sum_{r=1}^{k} r^2}_{\text{use hypothesis}} + \;(k+1)^2 \\[6pt]
&= \frac{k(k+1)(2k+1)}{6} + (k+1)^2 \\[6pt]
&= \frac{k(k+1)(2k+1)}{6} + \frac{6(k+1)^2}{6} \qquad \text{(common denominator 6)} \\[6pt]
&= \frac{k(k+1)(2k+1) + 6(k+1)^2}{6} \\[6pt]
&= \frac{(k+1)\big[k(2k+1) + 6(k+1)\big]}{6} \qquad \text{(factor out }k+1\text{)} \\[6pt]
&= \frac{(k+1)(2k^2 + k + 6k + 6)}{6} \\[6pt]
&= \frac{(k+1)(2k^2 + 7k + 6)}{6}
\end{aligned}
\]

Now factor the quadratic \(2k^2 + 7k + 6\). Look for two numbers that multiply to \(2 \times 6 = 12\) and add to \(7\). Those numbers are \(3\) and \(4\). So:

\[
2k^2 + 7k + 6 = 2k^2 + 3k + 4k + 6 = k(2k+3) + 2(2k+3) = (2k+3)(k+2)
\]

Substitute back:

\[
\frac{(k+1)(2k+3)(k+2)}{6} = \frac{(k+1)(k+2)(2k+3)}{6} = \frac{(k+1)((k+1)+1)(2(k+1)+1)}{6}
\]

This is exactly \(P(k+1)\).

**Step 5:** By induction, \(P(n)\) is true for all \(n \in \mathbb{N}\).

**Pitfall:** When factoring, double-check that your factored expression expands back to the original. A sign error in factoring is a common place where induction proofs go wrong.

---

## 6. Worked Example 3: Sum of Cubes

**Problem:** Prove that for all positive whole numbers \(n\):

\[
1^3 + 2^3 + 3^3 + \dots + n^3 = \left[\frac{n(n+1)}{2}\right]^2
\]

**Approach:** Notice the right-hand side is the square of the formula for \(1+2+\dots+n\) from Example 1. This is a beautiful result: the sum of the first \(n\) cubes equals the square of the sum of the first \(n\) natural numbers.

**Step 1:** Let \(P(n)\) be: \(\displaystyle\sum_{r=1}^{n} r^3 = \left[\frac{n(n+1)}{2}\right]^2\).

**Step 2 — Base case (\(n = 1\)):**
LHS: \(1^3 = 1\).
RHS: \(\left[\frac{1 \cdot 2}{2}\right]^2 = 1^2 = 1\).
\(P(1)\) is true.

**Step 3 — Inductive hypothesis:**
Assume \(P(k)\): \(\displaystyle\sum_{r=1}^{k} r^3 = \left[\frac{k(k+1)}{2}\right]^2\).

**Step 4 — Inductive step:**
Prove \(P(k+1)\): \(\displaystyle\sum_{r=1}^{k+1} r^3 = \left[\frac{(k+1)(k+2)}{2}\right]^2\).

\[
\begin{aligned}
\sum_{r=1}^{k+1} r^3 &= \sum_{r=1}^{k} r^3 + (k+1)^3 \\[6pt]
&= \left[\frac{k(k+1)}{2}\right]^2 + (k+1)^3 \qquad \text{(by hypothesis)} \\[6pt]
&= \frac{k^2(k+1)^2}{4} + (k+1)^3 \\[6pt]
&= \frac{k^2(k+1)^2}{4} + \frac{4(k+1)^3}{4} \qquad \text{(common denominator 4)} \\[6pt]
&= \frac{k^2(k+1)^2 + 4(k+1)^3}{4} \\[6pt]
&= \frac{(k+1)^2\big[k^2 + 4(k+1)\big]}{4} \qquad \text{(factor out }(k+1)^2\text{)} \\[6pt]
&= \frac{(k+1)^2(k^2 + 4k + 4)}{4} \\[6pt]
&= \frac{(k+1)^2(k+2)^2}{4} \\[6pt]
&= \left[\frac{(k+1)(k+2)}{2}\right]^2
\end{aligned}
\]

This is \(P(k+1)\).

**Step 5:** By induction, \(P(n)\) is true for all \(n \in \mathbb{N}\).

**Why this makes sense:** For \(n = 3\), the formula gives \(\left[\frac{3 \cdot 4}{2}\right]^2 = 6^2 = 36\). And indeed \(1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36\). The fact that this always works — that the sum of cubes is always a perfect square — is a surprising and elegant result that induction lets us prove with confidence.

---

## 7. Key Strategy Summary for Summation Induction

When you prove \(P(k+1)\) from \(P(k)\) for a summation formula, always follow these four sub-steps:

1. **Split the sum** at the \((k+1)\)-th term: \(\sum_{r=1}^{k+1} = \sum_{r=1}^{k} + \text{term}_{k+1}\).
2. **Substitute** the inductive hypothesis for the sum up to \(k\).
3. **Manipulate algebraically** — common denominator, factor, expand, simplify.
4. **Match the target** — your final expression must look exactly like the RHS of \(P(k+1)\), with every \(k\) replaced by \(k+1\).

**Common misconception:** Some students try to prove \(P(k+1)\) by starting from the RHS and working backward, or by manipulating both sides at once. The cleanest approach is to start from the LHS of \(P(k+1)\) and work forward until you reach the RHS.

---

## Practice Problems

**Problem 1:** Prove by mathematical induction that for all positive whole numbers \(n\):

\[
1 + 3 + 5 + \dots + (2n-1) = n^2
\]

In other words, the sum of the first \(n\) odd numbers equals \(n^2\).

**Problem 2:** Prove by mathematical induction that for all positive whole numbers \(n\):

\[
2 + 4 + 6 + \dots + 2n = n(n+1)
\]

This is the sum of the first \(n\) even numbers.

**Problem 3:** Prove by mathematical induction that for all \(n \in \mathbb{N}\):

\[
\sum_{r=1}^{n} r(r+1) = \frac{n(n+1)(n+2)}{3}
\]

**Problem 4:** Prove by mathematical induction that for all \(n \in \mathbb{N}\):

\[
\sum_{r=1}^{n} (2r-1)^2 = \frac{n(2n-1)(2n+1)}{3}
\]

This formula gives the sum of the squares of the first \(n\) odd numbers.

**Problem 5 (IB Exam Style):** Consider the statement \(P(n)\): \(\displaystyle\sum_{r=1}^{n} \frac{1}{r(r+1)} = \frac{n}{n+1}\) for all \(n \in \mathbb{N}\).

(a) Show that \(P(1)\) is true. [1 mark]
(b) Assume \(P(k)\) is true and use this to prove that \(P(k+1)\) is true. [4 marks]
(c) State the conclusion of the induction argument. [1 mark]

(You may use the fact that \(\frac{1}{r(r+1)} = \frac{1}{r} - \frac{1}{r+1}\). This is called a partial fraction decomposition.)

**Problem 6:** Prove by mathematical induction that for all \(n \in \mathbb{N}\):

\[
\sum_{r=1}^{n} r(r!) = (n+1)! - 1
\]

Recall: \(r!\) (read "\(r\) factorial") means \(r \times (r-1) \times (r-2) \times \dots \times 1\). Also, \((r+1)! = (r+1) \times r!\).

---

## Answers

**Answer 1:**

Let \(P(n)\) be: \(\displaystyle\sum_{r=1}^{n} (2r-1) = n^2\).

**Base case (\(n=1\)):** LHS: \(2(1)-1 = 1\). RHS: \(1^2 = 1\). \(P(1)\) is true.

**Inductive hypothesis:** Assume \(P(k)\): \(\displaystyle\sum_{r=1}^{k} (2r-1) = k^2\).

**Inductive step:** Prove \(P(k+1)\): \(\displaystyle\sum_{r=1}^{k+1} (2r-1) = (k+1)^2\).

\[
\begin{aligned}
\sum_{r=1}^{k+1} (2r-1) &= \sum_{r=1}^{k} (2r-1) + (2(k+1)-1) \\
&= k^2 + (2k+2-1) \qquad \text{(using the hypothesis)} \\
&= k^2 + 2k + 1 \\
&= (k+1)^2
\end{aligned}
\]

So \(P(k+1)\) is true. By induction, \(P(n)\) is true for all \(n \in \mathbb{N}\).

**Interpretation:** This proves that the sum of the first \(n\) odd numbers is always a perfect square — the square of \(n\). For example, \(1+3+5+7 = 16 = 4^2\).

---

**Answer 2:**

Let \(P(n)\) be: \(\displaystyle\sum_{r=1}^{n} 2r = n(n+1)\).

**Base case (\(n=1\)):** LHS: \(2(1) = 2\). RHS: \(1(2) = 2\). \(P(1)\) is true.

**Inductive hypothesis:** Assume \(P(k)\): \(\displaystyle\sum_{r=1}^{k} 2r = k(k+1)\).

**Inductive step:** Prove \(P(k+1)\): \(\displaystyle\sum_{r=1}^{k+1} 2r = (k+1)(k+2)\).

\[
\begin{aligned}
\sum_{r=1}^{k+1} 2r &= \sum_{r=1}^{k} 2r + 2(k+1) \\
&= k(k+1) + 2(k+1) \qquad \text{(using the hypothesis)} \\
&= (k+1)(k+2) \qquad \text{(factor out }k+1\text{)}
\end{aligned}
\]

So \(P(k+1)\) is true. By induction, \(P(n)\) is true for all \(n \in \mathbb{N}\).

**Interpretation:** The sum of the first \(n\) even numbers is \(n(n+1)\). For \(n=4\), \(2+4+6+8 = 20\) and \(4 \times 5 = 20\).

---

**Answer 3:**

Let \(P(n)\) be: \(\displaystyle\sum_{r=1}^{n} r(r+1) = \frac{n(n+1)(n+2)}{3}\).

**Base case (\(n=1\)):** LHS: \(1 \cdot 2 = 2\). RHS: \(\frac{1 \cdot 2 \cdot 3}{3} = \frac{6}{3} = 2\). \(P(1)\) is true.

**Inductive hypothesis:** Assume \(P(k)\): \(\displaystyle\sum_{r=1}^{k} r(r+1) = \frac{k(k+1)(k+2)}{3}\).

**Inductive step:** Prove \(P(k+1)\): \(\displaystyle\sum_{r=1}^{k+1} r(r+1) = \frac{(k+1)(k+2)(k+3)}{3}\).

\[
\begin{aligned}
\sum_{r=1}^{k+1} r(r+1) &= \sum_{r=1}^{k} r(r+1) + (k+1)(k+2) \\
&= \frac{k(k+1)(k+2)}{3} + (k+1)(k+2) \qquad \text{(by hypothesis)} \\
&= \frac{k(k+1)(k+2) + 3(k+1)(k+2)}{3} \\
&= \frac{(k+1)(k+2)(k+3)}{3} \qquad \text{(factor out }(k+1)(k+2)\text{)}
\end{aligned}
\]

So \(P(k+1)\) is true. By induction, \(P(n)\) is true for all \(n \in \mathbb{N}\).

---

**Answer 4:**

Let \(P(n)\) be: \(\displaystyle\sum_{r=1}^{n} (2r-1)^2 = \frac{n(2n-1)(2n+1)}{3}\).

**Base case (\(n=1\)):** LHS: \((2(1)-1)^2 = 1^2 = 1\). RHS: \(\frac{1(2\cdot1-1)(2\cdot1+1)}{3} = \frac{1 \cdot 1 \cdot 3}{3} = 1\). \(P(1)\) is true.

**Inductive hypothesis:** Assume \(P(k)\): \(\displaystyle\sum_{r=1}^{k} (2r-1)^2 = \frac{k(2k-1)(2k+1)}{3}\).

**Inductive step:** Prove \(P(k+1)\): \(\displaystyle\sum_{r=1}^{k+1} (2r-1)^2 = \frac{(k+1)(2k+1)(2k+3)}{3}\).

\[
\begin{aligned}
\sum_{r=1}^{k+1} (2r-1)^2 &= \sum_{r=1}^{k} (2r-1)^2 + (2(k+1)-1)^2 \\
&= \frac{k(2k-1)(2k+1)}{3} + (2k+1)^2 \qquad \text{(by hypothesis)} \\
&= \frac{k(2k-1)(2k+1) + 3(2k+1)^2}{3} \\
&= \frac{(2k+1)\big[k(2k-1) + 3(2k+1)\big]}{3} \qquad \text{(factor out }2k+1\text{)} \\
&= \frac{(2k+1)(2k^2 - k + 6k + 3)}{3} \\
&= \frac{(2k+1)(2k^2 + 5k + 3)}{3}
\end{aligned}
\]

Factor \(2k^2 + 5k + 3\): find two numbers that multiply to \(2 \times 3 = 6\) and add to \(5\). Those are \(2\) and \(3\). So \(2k^2 + 5k + 3 = 2k^2 + 2k + 3k + 3 = 2k(k+1) + 3(k+1) = (k+1)(2k+3)\).

\[
\frac{(2k+1)(k+1)(2k+3)}{3} = \frac{(k+1)(2k+1)(2(k+1)+1)}{3}
\]

This is \(P(k+1)\). By induction, \(P(n)\) is true for all \(n \in \mathbb{N}\).

---

**Answer 5:**

(a) \(P(1)\): LHS = \(\frac{1}{1 \cdot 2} = \frac{1}{2}\). RHS = \(\frac{1}{1+1} = \frac{1}{2}\). LHS = RHS, so \(P(1)\) is true.

(b) Assume \(P(k)\): \(\displaystyle\sum_{r=1}^{k} \frac{1}{r(r+1)} = \frac{k}{k+1}\).

We must prove \(P(k+1)\): \(\displaystyle\sum_{r=1}^{k+1} \frac{1}{r(r+1)} = \frac{k+1}{k+2}\).

\[
\begin{aligned}
\sum_{r=1}^{k+1} \frac{1}{r(r+1)} &= \sum_{r=1}^{k} \frac{1}{r(r+1)} + \frac{1}{(k+1)(k+2)} \\[6pt]
&= \frac{k}{k+1} + \frac{1}{(k+1)(k+2)} \qquad \text{(by hypothesis)} \\[6pt]
&= \frac{k(k+2)}{(k+1)(k+2)} + \frac{1}{(k+1)(k+2)} \qquad \text{(common denominator)} \\[6pt]
&= \frac{k(k+2) + 1}{(k+1)(k+2)} \\[6pt]
&= \frac{k^2 + 2k + 1}{(k+1)(k+2)} \\[6pt]
&= \frac{(k+1)^2}{(k+1)(k+2)} \\[6pt]
&= \frac{k+1}{k+2} \qquad \text{(cancel }k+1\text{)}
\end{aligned}
\]

This is exactly the RHS of \(P(k+1)\), so \(P(k+1)\) is true.

(c) By the principle of mathematical induction, \(P(n)\) is true for all \(n \in \mathbb{N}\). That is, \(\displaystyle\sum_{r=1}^{n} \frac{1}{r(r+1)} = \frac{n}{n+1}\) for every positive whole number \(n\).

**Why this makes sense:** The formula shows that as \(n\) gets large, the sum approaches 1 (since \(\frac{n}{n+1} \to 1\)). The sum "telescopes" — each term cancels with part of the next term when written in partial fraction form, which is why the formula is so simple.

---

**Answer 6:**

Let \(P(n)\) be: \(\displaystyle\sum_{r=1}^{n} r(r!) = (n+1)! - 1\).

**Base case (\(n=1\)):** LHS: \(1 \cdot 1! = 1 \cdot 1 = 1\). RHS: \(2! - 1 = 2 - 1 = 1\). \(P(1)\) is true.

**Inductive hypothesis:** Assume \(P(k)\): \(\displaystyle\sum_{r=1}^{k} r(r!) = (k+1)! - 1\).

**Inductive step:** Prove \(P(k+1)\): \(\displaystyle\sum_{r=1}^{k+1} r(r!) = (k+2)! - 1\).

\[
\begin{aligned}
\sum_{r=1}^{k+1} r(r!) &= \sum_{r=1}^{k} r(r!) + (k+1)(k+1)! \\[6pt]
&= (k+1)! - 1 + (k+1)(k+1)! \qquad \text{(by hypothesis)} \\[6pt]
&= (k+1)!\big[1 + (k+1)\big] - 1 \qquad \text{(factor out }(k+1)!\text{)} \\[6pt]
&= (k+1)!(k+2) - 1 \\[6pt]
&= (k+2)! - 1 \qquad \text{(since }(k+2)! = (k+2)(k+1)!\text{)}
\end{aligned}
\]

This is \(P(k+1)\). By induction, \(P(n)\) is true for all \(n \in \mathbb{N}\).

**Pitfall:** The step where you go from \((k+1)!(k+2)\) to \((k+2)!\) relies on understanding the definition of factorial: \((k+2)! = (k+2) \times (k+1) \times k \times \dots \times 1 = (k+2) \times (k+1)!\). If this is unfamiliar, review the definition of factorial before attempting this proof.
