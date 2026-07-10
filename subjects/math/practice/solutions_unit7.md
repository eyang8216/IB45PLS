# IB AAHL Unit 7: Number, Functions & Graphs — Full Solutions

---

## Problem 1 — Optimization (Fencing)

**Approach**: Use the fencing constraint to relate \(x\) and \(y\), substitute into the area formula, then differentiate to find the maximum.

**(a)** The fencing covers two sides perpendicular to the wall and one side parallel to the wall. The stone wall itself does not require fencing. Therefore:

\[
2y + x = 200 \quad\Rightarrow\quad y = \frac{200 - x}{2} = 100 - \frac{x}{2}.
\]

**(b)** The area is \(A = x \cdot y = x\left(100 - \frac{x}{2}\right) = 100x - \frac{1}{2}x^{2}\).

**(c)** To maximize \(A\), differentiate:

\[
\frac{dA}{dx} = 100 - x.
\]

Set \(\frac{dA}{dx} = 0\): \(100 - x = 0 \Rightarrow x = 100\).

Second derivative: \(\frac{d^{2}A}{dx^{2}} = -1 < 0\), confirming a maximum.

When \(x = 100\), \(y = 100 - \frac{100}{2} = 50\).

Maximum area: \(A = 100(100) - \frac{1}{2}(100)^{2} = 10000 - 5000 = 5000\text{ m}^{2}\).

**Answer**: Dimensions: \(100\text{ m}\) (parallel to wall) by \(50\text{ m}\) (perpendicular). Maximum area: \(5000\text{ m}^{2}\).

**Pitfalls**: Forgetting that only three sides need fencing, or confusing which variable is which. Always verify the second derivative sign.

---

## Problem 2 — Optimization (Open Box)

**Approach**: Express volume as a function of the cutout size \(x\), differentiate, and find the critical point within the feasible domain \((0, 25)\).

**(a)** After cutting out squares of side \(x\):
- Length of box = \(80 - 2x\)
- Width of box = \(50 - 2x\)
- Height = \(x\)

Volume: \(V = x(80 - 2x)(50 - 2x) = x(4000 - 160x - 100x + 4x^{2})\)
\(= x(4000 - 260x + 4x^{2}) = 4x^{3} - 260x^{2} + 4000x\).

**(b)** \(\frac{dV}{dx} = 12x^{2} - 520x + 4000\).

Set \(\frac{dV}{dx} = 0\): \(12x^{2} - 520x + 4000 = 0\).

Divide by 4: \(3x^{2} - 130x + 1000 = 0\).

Using the quadratic formula:

\[
x = \frac{130 \pm \sqrt{130^{2} - 4(3)(1000)}}{2(3)} = \frac{130 \pm \sqrt{16900 - 12000}}{6} = \frac{130 \pm \sqrt{4900}}{6} = \frac{130 \pm 70}{6}.
\]

\(x = \frac{200}{6} \approx 33.33\) or \(x = \frac{60}{6} = 10\).

Since \(x\) must be less than \(\frac{50}{2} = 25\), only \(x = 10\) is feasible.

\(\frac{d^{2}V}{dx^{2}} = 24x - 520\). At \(x = 10\): \(240 - 520 = -280 < 0\), so maximum.

**(c)** \(V_{\max} = 4(10)^{3} - 260(10)^{2} + 4000(10) = 4000 - 26000 + 40000 = 18000\text{ cm}^{3}\).

**Answer**: \(x = 10.00\text{ cm}\); maximum volume \(= 18000\text{ cm}^{3}\).

**Pitfalls**: The domain is \((0, 25)\) because both \(80 - 2x > 0\) and \(50 - 2x > 0\). Always check that the critical point lies within the feasible interval. The root \(x \approx 33.33\) is outside the domain.

---

## Problem 3 — Optimization (Cylinder)

**Approach**: Use volume constraint to express \(h\) in terms of \(r\), write cost as a function of \(r\), then differentiate.

**(a)** Volume: \(\pi r^{2} h = 1000 \Rightarrow h = \frac{1000}{\pi r^{2}}\).

**(b)** Surface areas:
- Curved surface: \(2\pi r h\), cost = \(0.05 \times 2\pi r h = 0.10\pi r h\)
- Two circular ends: \(2\pi r^{2}\), cost = \(0.08 \times 2\pi r^{2} = 0.16\pi r^{2}\)

Substituting \(h\):

\[
\text{Curved cost} = 0.10\pi r \cdot \frac{1000}{\pi r^{2}} = \frac{100}{r}.
\]

\[
C = 0.16\pi r^{2} + \frac{100}{r}.
\]

**(c)** \(\frac{dC}{dr} = 0.32\pi r - \frac{100}{r^{2}}\).

Set to zero: \(0.32\pi r = \frac{100}{r^{2}} \Rightarrow 0.32\pi r^{3} = 100 \Rightarrow r^{3} = \frac{100}{0.32\pi} = \frac{100}{0.32 \times 3.14159...}\)

\(r^{3} \approx \frac{100}{1.0053} \approx 99.47 \Rightarrow r \approx \sqrt[3]{99.47} \approx 4.63\text{ cm}\).

Second derivative: \(\frac{d^{2}C}{dr^{2}} = 0.32\pi + \frac{200}{r^{3}} > 0\), so minimum.

Minimum cost: \(C = 0.16\pi(4.63)^{2} + \frac{100}{4.63} \approx 0.16\pi(21.44) + 21.60 \approx 10.78 + 21.60 = 32.38\).

More precisely: \(r = \sqrt[3]{\frac{100}{0.32\pi}} \approx 4.629...\)

\(C_{\min} = 0.16\pi(4.629)^{2} + \frac{100}{4.629} \approx 10.77 + 21.60 \approx 32.37\).

**Answer**: Radius \(\approx 4.63\text{ cm}\); minimum cost \(\approx \$32.37\).

**Pitfalls**: Distinguishing between surface areas (curved vs. ends) and their respective costs. Ensuring the volume constraint is correctly applied.

---

## Problem 4 — Binomial Expansion (Specific Coefficient)

**Approach**: Use the general term formula \((a+b)^{n} = \sum \binom{n}{r} a^{n-r}b^{r}\), find \(r\) such that the power of \(x\) is zero.

**(a)** Let \(a = 2x^{3}\) and \(b = -\frac{1}{x} = -x^{-1}\).

\[
T_{r+1} = \binom{8}{r} (2x^{3})^{8-r} \left(-x^{-1}\right)^{r} = \binom{8}{r} 2^{8-r} (-1)^{r} x^{3(8-r)} \cdot x^{-r}.
\]

\[
T_{r+1} = \binom{8}{r} 2^{8-r} (-1)^{r} x^{24 - 3r - r} = \binom{8}{r} 2^{8-r} (-1)^{r} x^{24 - 4r}.
\]

**(b)** For the term to be independent of \(x\), the exponent of \(x\) must be zero:

\[
24 - 4r = 0 \Rightarrow r = 6.
\]

**(c)** Substituting \(r = 6\):

\[
T_{7} = \binom{8}{6} 2^{8-6} (-1)^{6} x^{0} = \binom{8}{6} \cdot 2^{2} \cdot 1.
\]

\[
\binom{8}{6} = \binom{8}{2} = 28.
\]

Constant term = \(28 \times 4 = 112\).

**Answer**: \(r = 6\); constant term = \(112\).

**Pitfalls**: Sign from \((-1)^{r}\) — for \(r = 6\) (even), the sign is positive. Also ensuring the power of \(x\) inside \((2x^{3})^{8-r}\) is correctly computed as \(3(8-r)\).

---

## Problem 5 — Binomial Expansion (Rational \(n\))

**Approach**: Write as \((1 + 2x)^{-1/2}\) and use the binomial series for rational index.

\[
\frac{1}{\sqrt{1 + 2x}} = (1 + 2x)^{-1/2}.
\]

The binomial series for \((1 + u)^{n}\) with rational \(n\):

\[
(1 + u)^{n} = 1 + n u + \frac{n(n-1)}{2!}u^{2} + \frac{n(n-1)(n-2)}{3!}u^{3} + \cdots, \quad |u| < 1.
\]

Here \(n = -\frac{1}{2}\) and \(u = 2x\).

\[
(1 + 2x)^{-1/2} = 1 + \left(-\frac{1}{2}\right)(2x) + \frac{(-\frac{1}{2})(-\frac{3}{2})}{2!}(2x)^{2} + \frac{(-\frac{1}{2})(-\frac{3}{2})(-\frac{5}{2})}{3!}(2x)^{3} + \cdots
\]

Term 1: \(1\).

Term 2: \(-\frac{1}{2} \cdot 2x = -x\).

Term 3: \(\frac{(-\frac{1}{2})(-\frac{3}{2})}{2} \cdot 4x^{2} = \frac{\frac{3}{4}}{2} \cdot 4x^{2} = \frac{3}{8} \cdot 4x^{2} = \frac{3}{2}x^{2}\).

Term 4: \(\frac{(-\frac{1}{2})(-\frac{3}{2})(-\frac{5}{2})}{6} \cdot 8x^{3} = \frac{-\frac{15}{8}}{6} \cdot 8x^{3} = -\frac{15}{48} \cdot 8x^{3} = -\frac{15}{6}x^{3} = -\frac{5}{2}x^{3}\).

\[
\frac{1}{\sqrt{1 + 2x}} = 1 - x + \frac{3}{2}x^{2} - \frac{5}{2}x^{3} + \cdots
\]

Validity: \(|2x| < 1 \Rightarrow |x| < \frac{1}{2}\), i.e., \(-\frac{1}{2} < x < \frac{1}{2}\).

**Answer**: \(1 - x + \frac{3}{2}x^{2} - \frac{5}{2}x^{3} + \cdots\), valid for \(|x| < \frac{1}{2}\).

**Pitfalls**: The binomial coefficient signs for negative \(n\). Carefully track the product \((-\frac{1}{2})(-\frac{3}{2})(-\frac{5}{2})\) — note the negative sign. Also the factor \((2x)^{k}\) multiplies each term.

---

## Problem 6 — Binomial Expansion (Coefficient)

**Approach**: Expand both factors up to \(x^{5}\) and find combinations of terms that yield \(x^{5}\).

\[
(1 + x)^{3} = 1 + 3x + 3x^{2} + x^{3}.
\]

\[
(1 + 2x)^{6} = \sum_{k=0}^{6} \binom{6}{k} (2x)^{k} = \sum_{k=0}^{6} \binom{6}{k} 2^{k} x^{k}.
\]

We need the coefficient of \(x^{5}\) in the product \((1 + 3x + 3x^{2} + x^{3}) \times \sum_{k=0}^{6} \binom{6}{k} 2^{k} x^{k}\).

The ways to get \(x^{5}\):

| From \((1+x)^{3}\) | From \((1+2x)^{6}\) | Contribution |
|---|---|---|
| \(1\) | \(x^{5}\) | \(1 \times \binom{6}{5}2^{5} = 1 \times 6 \times 32 = 192\) |
| \(3x\) | \(x^{4}\) | \(3 \times \binom{6}{4}2^{4} = 3 \times 15 \times 16 = 720\) |
| \(3x^{2}\) | \(x^{3}\) | \(3 \times \binom{6}{3}2^{3} = 3 \times 20 \times 8 = 480\) |
| \(x^{3}\) | \(x^{2}\) | \(1 \times \binom{6}{2}2^{2} = 1 \times 15 \times 4 = 60\) |

Total coefficient = \(192 + 720 + 480 + 60 = 1452\).

**Answer**: Coefficient of \(x^{5}\) is \(1452\).

**Pitfalls**: Forgetting that \((1+x)^{3}\) stops at \(x^{3}\), so terms beyond \(x^{3}\) from the first factor don't exist. Double-check combinatorics and powers of 2.

---

## Problem 7 — Counting (Permutations)

**Approach**: "MISSISSIPPI" has repeated letters; use the formula for permutations with repetitions.

Letters: M (1), I (4), S (4), P (2). Total 11 letters.

\[
\text{Number of arrangements} = \frac{11!}{1! \times 4! \times 4! \times 2!}.
\]

\[
11! = 39916800.
\]

\[
4! = 24, \quad 2! = 2.
\]

\[
\frac{39916800}{24 \times 24 \times 2} = \frac{39916800}{1152} = 34650.
\]

**Answer**: \(34650\) distinct arrangements.

**Pitfalls**: Identifying the correct frequencies — M (1), I (4), S (4), P (2). Not just the letter count but the repetition count matters.

---

## Problem 8 — Counting (Permutations with Constraints)

**Approach**: For (b), treat the group of girls as a single "block." For (c), consider the two possible alternating patterns.

**(a)** No restrictions: \(9! = 362880\).

**(b)** Treat the 4 girls as one block. Then we have 5 boys + 1 block = 6 objects. Arrange these 6 objects in \(6!\) ways. Within the block, the 4 girls can be arranged in \(4!\) ways.

Total = \(6! \times 4! = 720 \times 24 = 17280\).

**(c)** Alternating means either BGBGBGBGB or GBGBGBGBG. Since there are 5 boys and 4 girls, only the pattern starting and ending with a boy (BGBGBGBGB) is possible.

Arrange 5 boys in 5! ways and 4 girls in 4! ways: \(5! \times 4! = 120 \times 24 = 2880\).

**Answer**: (a) \(362880\); (b) \(17280\); (c) \(2880\).

**Pitfalls**: In (c), check whether both alternating patterns are possible. With unequal numbers (5 boys, 4 girls), only BGBGBGBGB works because there are more boys.

---

## Problem 9 — Counting (Combinations)

**Approach**: Use \(\binom{n}{r}\) and sum over valid cases, or use complementary counting.

**(a)** No restrictions: choose 6 from 15.

\[
\binom{15}{6} = 5005.
\]

**(b)** At least 3 women: sum over 3, 4, 5, 6 women (maximum women is 7, but committee size is 6, so up to 6 women).

\[
\text{3W, 3M}: \binom{7}{3}\binom{8}{3} = 35 \times 56 = 1960.
\]
\[
\text{4W, 2M}: \binom{7}{4}\binom{8}{2} = 35 \times 28 = 980.
\]
\[
\text{5W, 1M}: \binom{7}{5}\binom{8}{1} = 21 \times 8 = 168.
\]
\[
\text{6W, 0M}: \binom{7}{6}\binom{8}{0} = 7 \times 1 = 7.
\]

Total = \(1960 + 980 + 168 + 7 = 3115\).

**(c)** More men than women: the valid splits are 4M/2W, 5M/1W, 6M/0W.

\[
\text{4M, 2W}: \binom{8}{4}\binom{7}{2} = 70 \times 21 = 1470.
\]
\[
\text{5M, 1W}: \binom{8}{5}\binom{7}{1} = 56 \times 7 = 392.
\]
\[
\text{6M, 0W}: \binom{8}{6}\binom{7}{0} = 28 \times 1 = 28.
\]

Total = \(1470 + 392 + 28 = 1890\).

**Answer**: (a) \(5005\); (b) \(3115\); (c) \(1890\).

**Pitfalls**: In (b), note the constraint is "at least 3 women," not "exactly 3 women." Summing all qualifying cases is the safest approach.

---

## Problem 10 — Counting (Repeated Arrangements)

**Approach**: "PARALLEL" — letters: P(1), A(2), R(1), L(3), E(1). Total 8 letters.

**(a)** No restrictions:

\[
\frac{8!}{1! \times 2! \times 1! \times 3! \times 1!} = \frac{40320}{2 \times 6} = \frac{40320}{12} = 3360.
\]

**(b)** Begin and end with L: fix the first and last positions as L. The remaining 6 positions are filled with P, A, A, R, L, E (one L used in the middle, plus the other letters).

Remaining letters: P(1), A(2), R(1), L(1), E(1) — total 6.

\[
\frac{6!}{1! \times 2! \times 1! \times 1! \times 1!} = \frac{720}{2} = 360.
\]

However, we must ensure the two fixed L's are chosen from the 3 L's. Since the L's are identical, fixing two of them at the ends is just one way, and the remaining L is placed among the other positions. So the above count is correct.

**(c)** All L's together: treat the three L's as one "super-letter" [LLL]. Now we have: P(1), A(2), R(1), [LLL](1), E(1) — 6 objects.

\[
\frac{6!}{1! \times 2! \times 1! \times 1! \times 1!} = \frac{720}{2} = 360.
\]

**Answer**: (a) \(3360\); (b) \(360\); (c) \(360\).

**Pitfalls**: When fixing identical letters at specific positions, those letters are "used up" from the pool. The remaining count adjusts accordingly.

---

## Problem 11 — Polynomial (Remainder Theorem)

**Approach**: By the Remainder Theorem, \(P(c)\) is the remainder when \(P(x)\) is divided by \((x - c)\).

Given \(P(x) = 2x^{3} + ax^{2} + bx - 6\).

Remainder when divided by \((x + 1)\): \(P(-1) = -14\).

\[
P(-1) = 2(-1)^{3} + a(-1)^{2} + b(-1) - 6 = -2 + a - b - 6 = a - b - 8.
\]

\[
a - b - 8 = -14 \Rightarrow a - b = -6 \quad (1)
\]

Remainder when divided by \((x - 2)\): \(P(2) = 18\).

\[
P(2) = 2(2)^{3} + a(2)^{2} + b(2) - 6 = 16 + 4a + 2b - 6 = 4a + 2b + 10.
\]

\[
4a + 2b + 10 = 18 \Rightarrow 4a + 2b = 8 \Rightarrow 2a + b = 4 \quad (2)
\]

Solve (1) and (2):
From (1): \(b = a + 6\).
Substitute into (2): \(2a + (a + 6) = 4 \Rightarrow 3a + 6 = 4 \Rightarrow 3a = -2 \Rightarrow a = -\frac{2}{3}\).

Then \(b = -\frac{2}{3} + 6 = \frac{16}{3}\).

**Answer**: \(a = -\frac{2}{3}\), \(b = \frac{16}{3}\).

**Pitfalls**: Sign when evaluating \(P(-1)\) — remember \((-1)^{3} = -1\). Also, \((x+1)\) corresponds to evaluating at \(x = -1\), not \(x = 1\).

---

## Problem 12 — Polynomial (Factor Theorem)

**Approach**: Since \(x = 2\) is a root, \(P(2) = 0\). Use this to find \(k\), then factorize.

\[
P(x) = x^{3} - 7x^{2} + kx - 8.
\]

\[
P(2) = (2)^{3} - 7(2)^{2} + k(2) - 8 = 8 - 28 + 2k - 8 = 2k - 28 = 0.
\]

\[
2k = 28 \Rightarrow k = 14.
\]

So \(P(x) = x^{3} - 7x^{2} + 14x - 8\).

Since \(x = 2\) is a root, \((x - 2)\) is a factor. Divide:

\[
(x^{3} - 7x^{2} + 14x - 8) \div (x - 2).
\]

Using synthetic division with root 2:

\[
\begin{array}{c|ccc}
2 & 1 & -7 & 14 & -8 \\
  &   & 2  & -10 & 8 \\
\hline
  & 1 & -5 & 4   & 0 \\
\end{array}
\]

Quotient: \(x^{2} - 5x + 4\).

Factorize: \(x^{2} - 5x + 4 = (x - 1)(x - 4)\).

\[
P(x) = (x - 2)(x - 1)(x - 4).
\]

**Answer**: \(k = 14\); \(P(x) = (x - 2)(x - 1)(x - 4)\).

**Pitfalls**: After synthetic division, ensure the quotient is correct — the coefficients [1, -5, 4] correspond to \(x^{2} - 5x + 4\). Verify by expanding: \((x-2)(x^{2} - 5x + 4) = x^{3} - 5x^{2} + 4x - 2x^{2} + 10x - 8 = x^{3} - 7x^{2} + 14x - 8\). Correct.

---

## Problem 13 — Polynomial (Complex Conjugate Roots)

**Approach**: Real-coefficient polynomials have complex roots in conjugate pairs. So \(x = 1 - 2i\) is also a root. Use the three roots and \(P(0) = -10\) to find the leading coefficient.

Roots: \(r_{1} = 1 + 2i\), \(r_{2} = 1 - 2i\), \(r_{3} = -1\).

The quadratic factor for the complex pair:

\[
(x - (1+2i))(x - (1-2i)) = (x - 1 - 2i)(x - 1 + 2i) = (x-1)^{2} - (2i)^{2} = (x-1)^{2} + 4 = x^{2} - 2x + 1 + 4 = x^{2} - 2x + 5.
\]

So \(P(x) = a(x + 1)(x^{2} - 2x + 5)\) for some constant \(a\).

Given \(P(0) = -10\):

\[
P(0) = a(0 + 1)(0^{2} - 0 + 5) = a(1)(5) = 5a = -10 \Rightarrow a = -2.
\]

\[
P(x) = -2(x + 1)(x^{2} - 2x + 5) = -2(x^{3} - 2x^{2} + 5x + x^{2} - 2x + 5) = -2(x^{3} - x^{2} + 3x + 5).
\]

\[
P(x) = -2x^{3} + 2x^{2} - 6x - 10.
\]

**Answer**: \(P(x) = -2x^{3} + 2x^{2} - 6x - 10\).

**Pitfalls**: The conjugate root theorem only applies when coefficients are real. Always check that the product of the complex factors yields a polynomial with real coefficients — \((x-1)^{2} + 4\) is indeed real.

---

## Problem 14 — Functions (Domain, Range & Inverse)

**Approach**: For a rational function \(f(x) = \frac{ax+b}{cx+d}\), the horizontal asymptote is \(y = \frac{a}{c}\) and gives the excluded value from the range.

**(a)** \(f(x) = \frac{2x+1}{x-3}\).

Domain: \(x \in \mathbb{R},\; x \neq 3\).

Range: Since the horizontal asymptote is \(y = \frac{2}{1} = 2\), the value \(y = 2\) is excluded. Range: \(y \in \mathbb{R},\; y \neq 2\).

**(b)** To find \(f^{-1}\): let \(y = \frac{2x+1}{x-3}\).

\[
y(x-3) = 2x + 1 \Rightarrow yx - 3y = 2x + 1 \Rightarrow yx - 2x = 3y + 1 \Rightarrow x(y - 2) = 3y + 1.
\]

\[
x = \frac{3y + 1}{y - 2}.
\]

\[
f^{-1}(x) = \frac{3x + 1}{x - 2}.
\]

Domain of \(f^{-1}\): \(x \neq 2\) (which matches the range of \(f\)). Range of \(f^{-1}\): \(y \neq 3\) (domain of \(f\)).

**(c)** Verify:

\[
f(f^{-1}(x)) = f\left(\frac{3x+1}{x-2}\right) = \frac{2\left(\frac{3x+1}{x-2}\right) + 1}{\frac{3x+1}{x-2} - 3} = \frac{\frac{6x+2}{x-2} + \frac{x-2}{x-2}}{\frac{3x+1 - 3x + 6}{x-2}} = \frac{\frac{7x}{x-2}}{\frac{7}{x-2}} = x.
\]

**Answer**: (a) Domain: \(\mathbb{R}\setminus\{3\}\), Range: \(\mathbb{R}\setminus\{2\}\); (b) \(f^{-1}(x) = \frac{3x+1}{x-2}\), Domain: \(\mathbb{R}\setminus\{2\}\), Range: \(\mathbb{R}\setminus\{3\}\); (c) Verified.

**Pitfalls**: The domain of the inverse is the range of the original function. The horizontal asymptote of a rational function \(\frac{ax+b}{cx+d}\) is \(y = \frac{a}{c}\), not \(\frac{a}{d}\).

---

## Problem 15 — Functions (Composite)

**Approach**: Compose functions by substituting carefully, and determine domains by considering where each function is defined.

**(a)** \(g(x) = \ln(x - 2)\) requires \(x - 2 > 0\), so \(x > 2\). Domain of \(g\): \((2, \infty)\).

**(b)** \((f \circ g)(x) = f(g(x)) = f(\ln(x-2)) = e^{\ln(x-2)} = x - 2\), for \(x > 2\).

**(c)** \((g \circ f)(x) = g(f(x)) = g(e^{x}) = \ln(e^{x} - 2)\).

Domain: \(e^{x} - 2 > 0 \Rightarrow e^{x} > 2 \Rightarrow x > \ln 2\).

So \((g \circ f)(x) = \ln(e^{x} - 2)\), domain: \((\ln 2, \infty)\).

**(d)** \((g \circ f)(\ln 5) = \ln(e^{\ln 5} - 2) = \ln(5 - 2) = \ln 3\).

**Answer**: (a) \((2, \infty)\); (b) \((f \circ g)(x) = x - 2\) for \(x > 2\); (c) \((g \circ f)(x) = \ln(e^{x} - 2)\), domain \((\ln 2, \infty)\); (d) \(\ln 3\).

**Pitfalls**: The domain of a composite function is not necessarily the intersection of the domains — the output of the inner function must lie in the domain of the outer function. For \((g \circ f)\), \(e^{x}\) must be \(> 2\), not just \(e^{x} > 0\).

---

## Problem 16 — Functions (Inverse & Domain Restriction)

**Approach**: Complete the square to find the minimum and range, then restrict the domain to make the function one-to-one.

**(a)** \(f(x) = x^{2} - 4x + 7\).

Complete the square: \(x^{2} - 4x = (x - 2)^{2} - 4\).

\[
f(x) = (x - 2)^{2} - 4 + 7 = (x - 2)^{2} + 3.
\]

**(b)** The minimum occurs at \(x = 2\) and is \(f(2) = 3\).

**(c)** \(f\) is a quadratic opening upward. It is not one-to-one on \(\mathbb{R}\) because \(f(a) = f(b)\) for \(a \neq b\) (e.g., \(f(1) = f(3) = 4\)). To make it invertible, restrict the domain to \(x \geq 2\) (or \(x \leq 2\)).

Choose the maximal domain \([2, \infty)\). On this domain, \(f(x) \geq 3\).

To find \(f^{-1}\): let \(y = (x - 2)^{2} + 3\).

\[
y - 3 = (x - 2)^{2} \Rightarrow x - 2 = \pm\sqrt{y - 3}.
\]

Since \(x \geq 2\), we take the positive root: \(x = 2 + \sqrt{y - 3}\).

\[
f^{-1}(x) = 2 + \sqrt{x - 3}, \quad \text{domain: } x \geq 3.
\]

**Answer**: (a) \(f(x) = (x - 2)^{2} + 3\); (b) Minimum value 3 at \(x = 2\); (c) Not one-to-one on \(\mathbb{R}\); restrict to \([2, \infty)\); \(f^{-1}(x) = 2 + \sqrt{x - 3}\), \(x \geq 3\).

**Pitfalls**: After restricting the domain, the inverse must correspond to that branch. If \(x \geq 2\), then \(x - 2 \geq 0\), so take the positive square root.

---

## Problem 17 — Transformations (Sequence)

**Approach**: Apply transformations in the given order to the equation \(y = f(x)\).

Starting with \(y = f(x)\):

1. **Horizontal stretch by factor 3**: Replace \(x\) by \(\frac{x}{3}\): \(y = f\left(\frac{x}{3}\right)\).

2. **Reflection in the \(y\)-axis**: Replace \(x\) by \(-x\): \(y = f\left(\frac{-x}{3}\right) = f\left(-\frac{x}{3}\right)\).

3. **Translation by \(\begin{pmatrix}1 \\ -2\end{pmatrix}\)**: Replace \(x\) by \(x - 1\) (shift right 1) and \(y\) by \(y + 2\) (shift down 2):

\[
y + 2 = f\left(-\frac{x-1}{3}\right).
\]

\[
y = f\left(-\frac{x-1}{3}\right) - 2.
\]

**Answer**: \(y = f\left(\frac{1-x}{3}\right) - 2\).

**Pitfalls**: The order of transformations matters. A horizontal stretch "by factor 3" means replacing \(x\) with \(x/3\). A reflection in the \(y\)-axis means \(x \to -x\). The translation \((1, -2)\) means \(x \to x - 1\) and \(y \to y + 2\).

---

## Problem 18 — Transformations (Image of a Point)

**Approach**: Apply transformations to the equation and track the point through each transformation.

Original curve: \(y = \sqrt{x + 4}\).

**(a)** Reflection in \(x\)-axis: \(y \to -y\): \(-y = \sqrt{x + 4} \Rightarrow y = -\sqrt{x + 4}\).

Translation by \((2, 5)\): \(x \to x - 2\), \(y \to y - 5\):

\[
y - 5 = -\sqrt{(x - 2) + 4} = -\sqrt{x + 2}.
\]

\[
y = 5 - \sqrt{x + 2}.
\]

**(b)** Point \(P(0, 2)\): check — \(\sqrt{0 + 4} = 2\). Correct.

Apply reflection in \(x\)-axis: \((0, 2) \to (0, -2)\).

Apply translation \((2, 5)\): \((0 + 2, -2 + 5) = (2, 3)\).

Verify on the transformed curve: \(y = 5 - \sqrt{2 + 2} = 5 - 2 = 3\). Correct.

**Answer**: (a) \(y = 5 - \sqrt{x + 2}\); (b) \((2, 3)\).

**Pitfalls**: Reflection in the \(x\)-axis changes the sign of \(y\) only. The translation vector \(\begin{pmatrix}2 \\ 5\end{pmatrix}\) means "right 2, up 5."

---

## Problem 19 — Modulus (Equation)

**Approach**: Consider cases based on where the expression inside the absolute value changes sign.

\[
|2x - 1| = x + 4.
\]

The critical point is \(x = \frac{1}{2}\).

**Case 1**: \(x \geq \frac{1}{2}\). Then \(|2x - 1| = 2x - 1\).

\[
2x - 1 = x + 4 \Rightarrow x = 5.
\]

Check: \(5 \geq \frac{1}{2}\) ✓. Also check in original: \(|2(5)-1| = |9| = 9\) and \(5+4 = 9\) ✓.

**Case 2**: \(x < \frac{1}{2}\). Then \(|2x - 1| = -(2x - 1) = 1 - 2x\).

\[
1 - 2x = x + 4 \Rightarrow 1 - 4 = 3x \Rightarrow -3 = 3x \Rightarrow x = -1.
\]

Check: \(-1 < \frac{1}{2}\) ✓. Original: \(|2(-1)-1| = |-3| = 3\) and \(-1+4 = 3\) ✓.

**Answer**: \(x = -1\) or \(x = 5\).

**Pitfalls**: Always verify solutions against the case condition and in the original equation. Extraneous solutions can arise if the case algebra produces a value that violates the case condition.

---

## Problem 20 — Modulus (Inequality)

**Approach**: \(|3x + 2| \leq 5\) means \(-5 \leq 3x + 2 \leq 5\).

\[
-5 \leq 3x + 2 \leq 5.
\]

Subtract 2 throughout: \(-7 \leq 3x \leq 3\).

Divide by 3: \(-\frac{7}{3} \leq x \leq 1\).

**Answer**: \(x \in \left[-\frac{7}{3},\; 1\right]\).

**Pitfalls**: The inequality \(|A| \leq B\) (with \(B \geq 0\)) translates to \(-B \leq A \leq B\). For strict inequalities, use the same pattern with strict inequality signs.

---

## Problem 21 — Modulus (Combined Inequality)

**Approach**: \(|x - 1| + |x - 3| < 5\). Break into intervals defined by the critical points \(x = 1\) and \(x = 3\).

**Interval 1**: \(x < 1\). Then \(|x-1| = 1 - x\) and \(|x-3| = 3 - x\).

\[
(1 - x) + (3 - x) < 5 \Rightarrow 4 - 2x < 5 \Rightarrow -2x < 1 \Rightarrow x > -\frac{1}{2}.
\]

Intersection with \(x < 1\): \(-\frac{1}{2} < x < 1\).

**Interval 2**: \(1 \leq x < 3\). Then \(|x-1| = x - 1\) and \(|x-3| = 3 - x\).

\[
(x - 1) + (3 - x) < 5 \Rightarrow 2 < 5.
\]

This is always true. Intersection with \(1 \leq x < 3\): \(1 \leq x < 3\).

**Interval 3**: \(x \geq 3\). Then \(|x-1| = x - 1\) and \(|x-3| = x - 3\).

\[
(x - 1) + (x - 3) < 5 \Rightarrow 2x - 4 < 5 \Rightarrow 2x < 9 \Rightarrow x < \frac{9}{2}.
\]

Intersection with \(x \geq 3\): \(3 \leq x < \frac{9}{2}\).

Union of all three: \(-\frac{1}{2} < x < \frac{9}{2}\).

**Answer**: \(x \in \left(-\frac{1}{2},\; \frac{9}{2}\right)\).

**Pitfalls**: Carefully manage the split at each critical point. The middle interval gave a tautology (2 < 5), meaning the entire interval satisfies the inequality — double-check the algebra. The union of all valid sub-intervals gives the final solution.

---

## Problem 22 — Rational Functions (Asymptotes & Sketching)

**Approach**: For \(f(x) = \frac{3x - 2}{x + 1}\), find vertical asymptote (denominator = 0), horizontal asymptote (limit as \(x \to \pm\infty\)), and intercepts.

**(a)** Vertical asymptote: \(x + 1 = 0 \Rightarrow x = -1\).

Horizontal asymptote: \(\lim_{x\to\pm\infty} \frac{3x-2}{x+1} = 3\). So \(y = 3\) is the horizontal asymptote.

**(b)** \(y\)-intercept: set \(x = 0\): \(f(0) = \frac{-2}{1} = -2\). Point: \((0, -2)\).

\(x\)-intercept: set \(f(x) = 0\): \(3x - 2 = 0 \Rightarrow x = \frac{2}{3}\). Point: \((\frac{2}{3}, 0)\).

**(c)** Sketch description:

The graph is a rectangular hyperbola with:
- Vertical asymptote: \(x = -1\) (dashed line)
- Horizontal asymptote: \(y = 3\) (dashed line)
- \(y\)-intercept at \((0, -2)\)
- \(x\)-intercept at \((\frac{2}{3}, 0)\)

For \(x < -1\): \(x+1 < 0\), both numerator and denominator are negative (for \(x\) sufficiently negative, \(3x - 2 < 0\)), so \(f(x) > 3\). As \(x \to -\infty\), \(f(x) \to 3^{+}\). As \(x \to (-1)^{-}\), \(f(x) \to +\infty\).

For \(x > -1\): As \(x \to (-1)^{+}\), \(f(x) \to -\infty\). The function crosses the \(x\)-axis at \((\frac{2}{3}, 0)\) and the \(y\)-axis at \((0, -2)\), then approaches \(y = 3\) from below as \(x \to +\infty\).

**Answer**: (a) \(x = -1\) (vertical), \(y = 3\) (horizontal); (b) \(y\)-intercept \((0, -2)\), \(x\)-intercept \((\frac{2}{3}, 0)\); (c) see description.

**Pitfalls**: The horizontal asymptote is the ratio of leading coefficients \(\frac{3}{1} = 3\). Do not confuse with \(\frac{-2}{1} = -2\) (which is the \(y\)-intercept).

---

## Problem 23 — Rational Inequality

**Approach**: Solve \(\frac{x - 2}{x + 1} \geq 0\) by sign analysis. Critical points: numerator zero (\(x = 2\)) and denominator zero (\(x = -1\)).

Create a sign table:

| Interval | \(x < -1\) | \(-1 < x < 2\) | \(x > 2\) |
|---|---|---|---|
| \(x - 2\) | \(-\) | \(-\) | \(+\) |
| \(x + 1\) | \(-\) | \(+\) | \(+\) |
| \(\frac{x-2}{x+1}\) | \(+\) | \(-\) | \(+\) |

We want \(\frac{x-2}{x+1} \geq 0\).

- \(x < -1\): positive ✓ (but note \(x = -1\) is excluded).
- \(x = 2\): numerator is zero, so expression = 0, included ✓.
- \(x > 2\): positive ✓.

Solution: \(x < -1\) or \(x \geq 2\).

**Answer**: \(x \in (-\infty, -1) \cup [2, \infty)\).

**Pitfalls**: The denominator cannot be zero, so \(x = -1\) is always excluded, even if the inequality is non-strict (\(\geq\)). At \(x = 2\), the numerator is zero making the whole fraction zero, which satisfies \(\geq 0\), so include \(x = 2\).

---

## Problem 24 — Rational Inequality (Advanced)

**Approach**: Rearrange \(\frac{2x + 1}{x - 3} \leq 1\) to get a single fraction compared to zero.

\[
\frac{2x + 1}{x - 3} - 1 \leq 0 \Rightarrow \frac{2x + 1 - (x - 3)}{x - 3} \leq 0 \Rightarrow \frac{x + 4}{x - 3} \leq 0.
\]

Critical points: numerator zero at \(x = -4\), denominator zero at \(x = 3\).

Sign table:

| Interval | \(x < -4\) | \(-4 < x < 3\) | \(x > 3\) |
|---|---|---|---|
| \(x + 4\) | \(-\) | \(+\) | \(+\) |
| \(x - 3\) | \(-\) | \(-\) | \(+\) |
| \(\frac{x+4}{x-3}\) | \(+\) | \(-\) | \(+\) |

We want \(\frac{x+4}{x-3} \leq 0\):

- \(-4 \leq x < 3\): negative or zero ✓. At \(x = -4\), fraction = 0, included. At \(x = 3\), undefined, excluded.

**Answer**: \(x \in [-4, 3)\).

**Pitfalls**: Always bring all terms to one side to get \(\frac{P(x)}{Q(x)} \leq 0\) form. Do not multiply both sides by \((x-3)\) without considering the sign of the denominator — that can flip the inequality direction.

---

## Problem 25 — Multi-part (Functions, Modulus & Transformations)

**(a)** \(f(x) = |x^{2} - 4|\).

The underlying quadratic \(y = x^{2} - 4\) is a parabola opening upward with roots at \(x = \pm 2\) and vertex at \((0, -4)\).

Taking the absolute value flips the portion below the \(x\)-axis upward. So:
- For \(|x| \geq 2\): \(x^{2} - 4 \geq 0\), so \(f(x) = x^{2} - 4\).
- For \(|x| < 2\): \(x^{2} - 4 < 0\), so \(f(x) = -(x^{2} - 4) = 4 - x^{2}\).

Key points:
- \(x\)-intercepts: \(x = -2\) and \(x = 2\).
- \(y\)-intercept: \(f(0) = |0 - 4| = 4\), point \((0, 4)\).
- The portion for \(|x| < 2\) is an inverted parabola \(y = 4 - x^{2}\) with maximum at \((0, 4)\).
- For \(|x| \geq 2\), the graph is \(y = x^{2} - 4\) with minimum at \((\pm 2, 0)\).
- The points \((\pm 2, 0)\) are turning points (cusps) of the absolute value function.

**(b)** Solve \(f(x) = 5\):

Case 1: \(x^{2} - 4 = 5\) (when \(|x| \geq 2\)): \(x^{2} = 9 \Rightarrow x = \pm 3\). Both satisfy \(|x| \geq 2\).

Case 2: \(4 - x^{2} = 5\) (when \(|x| < 2\)): \(-x^{2} = 1 \Rightarrow x^{2} = -1\), no real solutions.

Solutions: \(x = -3\) or \(x = 3\).

**(c)** Translation by \((-1, 3)\): \(x \to x + 1\), \(y \to y - 3\).

Original: \(y = |x^{2} - 4|\). Transformed: \(y - 3 = |(x + 1)^{2} - 4| \Rightarrow y = |(x + 1)^{2} - 4| + 3\).

\(y\)-intercept: set \(x = 0\): \(y = |(0+1)^{2} - 4| + 3 = |1 - 4| + 3 = |-3| + 3 = 3 + 3 = 6\). Point: \((0, 6)\).

**Answer**: (a) See description; (b) \(x = -3\) or \(x = 3\); (c) \(y = |(x+1)^{2} - 4| + 3\); \(y\)-intercept \((0, 6)\).

**Pitfalls**: Graphing \(|x^{2} - 4|\) — identify where the quadratic is negative and flip it. When translating left by 1, replace \(x\) by \(x + 1\), not \(x - 1\).

---
