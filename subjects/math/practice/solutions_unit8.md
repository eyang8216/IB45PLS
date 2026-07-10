# IB AAHL Unit 8: Trigonometry & Geometry — Full Solutions

---

## Problem 1 — Compound Angle (Exact Value)

**Approach**: Express \(75^{\circ}\) as \(45^{\circ} + 30^{\circ}\) and use \(\cos(A + B) = \cos A \cos B - \sin A \sin B\).

\[
\cos 75^{\circ} = \cos(45^{\circ} + 30^{\circ}) = \cos 45^{\circ}\cos 30^{\circ} - \sin 45^{\circ}\sin 30^{\circ}.
\]

\[
\cos 45^{\circ} = \frac{\sqrt{2}}{2}, \quad \cos 30^{\circ} = \frac{\sqrt{3}}{2}, \quad \sin 45^{\circ} = \frac{\sqrt{2}}{2}, \quad \sin 30^{\circ} = \frac{1}{2}.
\]

\[
\cos 75^{\circ} = \frac{\sqrt{2}}{2} \cdot \frac{\sqrt{3}}{2} - \frac{\sqrt{2}}{2} \cdot \frac{1}{2} = \frac{\sqrt{6}}{4} - \frac{\sqrt{2}}{4} = \frac{\sqrt{6} - \sqrt{2}}{4}.
\]

**Answer**: \(\cos 75^{\circ} = \dfrac{\sqrt{6} - \sqrt{2}}{4}\).

**Pitfalls**: Choosing the right compound formula — \(\cos(A+B)\) uses \(\cos A \cos B - \sin A \sin B\). Alternatively, one could use \(\cos(90^{\circ} - 15^{\circ}) = \sin 15^{\circ}\), but the compound approach is more direct.

---

## Problem 2 — Double Angle (Exact Value)

**Approach**: Given \(\sin\theta = \frac{3}{5}\) in Q1, find \(\cos\theta\) using \(\sin^{2}\theta + \cos^{2}\theta = 1\), then apply double-angle formulas.

\[
\cos\theta = \sqrt{1 - \sin^{2}\theta} = \sqrt{1 - \frac{9}{25}} = \sqrt{\frac{16}{25}} = \frac{4}{5} \quad (\text{positive in Q1}).
\]

**(a)** \(\sin 2\theta = 2\sin\theta\cos\theta = 2 \cdot \frac{3}{5} \cdot \frac{4}{5} = \frac{24}{25}\).

**(b)** \(\cos 2\theta = \cos^{2}\theta - \sin^{2}\theta = \left(\frac{4}{5}\right)^{2} - \left(\frac{3}{5}\right)^{2} = \frac{16}{25} - \frac{9}{25} = \frac{7}{25}\).

Alternatively: \(\cos 2\theta = 1 - 2\sin^{2}\theta = 1 - 2\left(\frac{9}{25}\right) = 1 - \frac{18}{25} = \frac{7}{25}\).

**(c)** \(\tan 2\theta = \frac{\sin 2\theta}{\cos 2\theta} = \frac{24/25}{7/25} = \frac{24}{7}\).

**Answer**: (a) \(\sin 2\theta = \frac{24}{25}\); (b) \(\cos 2\theta = \frac{7}{25}\); (c) \(\tan 2\theta = \frac{24}{7}\).

**Pitfalls**: The sign of \(\cos\theta\) — since \(0 < \theta < \frac{\pi}{2}\), both sine and cosine are positive. For other quadrants, the sign matters.

---

## Problem 3 — Compound Angle (Simplification)

**Approach**: Recognize the expression matches the sine difference formula.

\[
\sin(A + B)\cos B - \cos(A + B)\sin B = \sin((A + B) - B) = \sin A.
\]

This is directly the identity \(\sin(P - Q) = \sin P \cos Q - \cos P \sin Q\) with \(P = A + B\) and \(Q = B\).

**Answer**: \(\sin A\).

**Pitfalls**: Recognizing the pattern. The expression \(\sin P\cos Q - \cos P\sin Q\) is \(\sin(P - Q)\). Make sure to identify \(P\) and \(Q\) correctly.

---

## Problem 4 — Proving Identity

**Approach**: Use double-angle identities \(\cos 2\theta = 1 - 2\sin^{2}\theta\) and \(\sin 2\theta = 2\sin\theta\cos\theta\).

\[
\frac{1 - \cos 2\theta}{\sin 2\theta} = \frac{1 - (1 - 2\sin^{2}\theta)}{2\sin\theta\cos\theta} = \frac{2\sin^{2}\theta}{2\sin\theta\cos\theta} = \frac{\sin\theta}{\cos\theta} = \tan\theta.
\]

Restrictions: \(\sin 2\theta \neq 0 \Rightarrow \theta \neq n\frac{\pi}{2}\) for integer \(n\). Also \(\cos\theta \neq 0\) for the final form \(\tan\theta\).

**Answer**: Identity proved. Restrictions: \(\theta \neq n\frac{\pi}{2},\; n \in \mathbb{Z}\).

**Pitfalls**: Choosing the right form of \(\cos 2\theta\). Using \(\cos 2\theta = 1 - 2\sin^{2}\theta\) makes the numerator simplify nicely. Using \(\cos 2\theta = \cos^{2}\theta - \sin^{2}\theta\) would also work but is less direct.

---

## Problem 5 — Proving Identity

**Approach**: Express \(\sin 3x\) and \(\cos 3x\) using triple-angle formulas, or use compound angle methods.

\[
\sin 3x = \sin(2x + x) = \sin 2x\cos x + \cos 2x\sin x = (2\sin x\cos x)\cos x + (\cos^{2}x - \sin^{2}x)\sin x.
\]
\[
\sin 3x = 2\sin x\cos^{2}x + \sin x\cos^{2}x - \sin^{3}x = 3\sin x\cos^{2}x - \sin^{3}x = \sin x(3\cos^{2}x - \sin^{2}x).
\]

\[
\cos 3x = \cos(2x + x) = \cos 2x\cos x - \sin 2x\sin x = (\cos^{2}x - \sin^{2}x)\cos x - (2\sin x\cos x)\sin x.
\]
\[
\cos 3x = \cos^{3}x - \sin^{2}x\cos x - 2\sin^{2}x\cos x = \cos^{3}x - 3\sin^{2}x\cos x = \cos x(\cos^{2}x - 3\sin^{2}x).
\]

Now compute:

\[
\frac{\sin 3x}{\sin x} = \frac{\sin x(3\cos^{2}x - \sin^{2}x)}{\sin x} = 3\cos^{2}x - \sin^{2}x.
\]

\[
\frac{\cos 3x}{\cos x} = \frac{\cos x(\cos^{2}x - 3\sin^{2}x)}{\cos x} = \cos^{2}x - 3\sin^{2}x.
\]

\[
\frac{\sin 3x}{\sin x} - \frac{\cos 3x}{\cos x} = (3\cos^{2}x - \sin^{2}x) - (\cos^{2}x - 3\sin^{2}x) = 2\cos^{2}x + 2\sin^{2}x = 2(\cos^{2}x + \sin^{2}x) = 2.
\]

**Answer**: Identity proved.

**Pitfalls**: The triple-angle formulas \(\sin 3x = 3\sin x - 4\sin^{3}x\) and \(\cos 3x = 4\cos^{3}x - 3\cos x\) could also be used, leading to a slightly different but equally valid simplification. Ensure division by \(\sin x\) and \(\cos x\) is valid by stating restrictions: \(x \neq n\pi\) and \(x \neq \frac{\pi}{2} + n\pi\).

---

## Problem 6 — Solving (Basic)

**Approach**: Isolate \(\sin x\) and find principal values, then use symmetry.

\[
2\sin x = 1 \Rightarrow \sin x = \frac{1}{2}.
\]

In \([0, 2\pi]\): \(\sin x = \frac{1}{2}\) at \(x = \frac{\pi}{6}\) (Q1) and \(x = \pi - \frac{\pi}{6} = \frac{5\pi}{6}\) (Q2).

**Answer**: \(x = \frac{\pi}{6},\; \frac{5\pi}{6}\).

**Pitfalls**: Remember that \(\sin x\) is positive in Q1 and Q2. The second solution is \(\pi - \alpha\), not \(2\pi - \alpha\).

---

## Problem 7 — Solving (Quadratic in \(\sin\))

**Approach**: Treat as a quadratic in \(\sin x\).

\[
2\sin^{2} x - 3\sin x + 1 = 0.
\]

Let \(u = \sin x\): \(2u^{2} - 3u + 1 = 0\).

Factor: \((2u - 1)(u - 1) = 0\).

\(u = \frac{1}{2}\) or \(u = 1\).

\(\sin x = \frac{1}{2}\): \(x = \frac{\pi}{6},\; \frac{5\pi}{6}\).

\(\sin x = 1\): \(x = \frac{\pi}{2}\).

**Answer**: \(x = \frac{\pi}{6},\; \frac{\pi}{2},\; \frac{5\pi}{6}\).

**Pitfalls**: Always check that each solution satisfies the original domain. \(\sin x = 1\) has only one solution in \([0, 2\pi]\).

---

## Problem 8 — Solving (Quadratic in \(\cos\))

**Approach**: Factor the quadratic in \(\cos x\).

\[
2\cos^{2} x + 3\cos x - 2 = 0.
\]

Let \(u = \cos x\): \(2u^{2} + 3u - 2 = 0\).

\[
u = \frac{-3 \pm \sqrt{9 - 4(2)(-2)}}{2(2)} = \frac{-3 \pm \sqrt{9 + 16}}{4} = \frac{-3 \pm 5}{4}.
\]

\(u = \frac{2}{4} = \frac{1}{2}\) or \(u = \frac{-8}{4} = -2\).

\(\cos x = -2\) has no real solutions (since \(-1 \leq \cos x \leq 1\)).

\(\cos x = \frac{1}{2}\): \(x = \frac{\pi}{3},\; \frac{5\pi}{3}\) (Q1 and Q4).

**Answer**: \(x = \frac{\pi}{3},\; \frac{5\pi}{3}\).

**Pitfalls**: Reject solutions outside \([-1, 1]\) for sine and cosine. Here \(\cos x = -2\) is invalid.

---

## Problem 9 — Solving (Using Identity)

**Approach**: Use \(\cos 2x = 1 - 2\sin^{2} x\) to get everything in terms of \(\sin x\).

\[
\cos 2x = \sin x \Rightarrow 1 - 2\sin^{2} x = \sin x \Rightarrow 2\sin^{2} x + \sin x - 1 = 0.
\]

Factor: \((2\sin x - 1)(\sin x + 1) = 0\).

\(\sin x = \frac{1}{2}\): \(x = \frac{\pi}{6},\; \frac{5\pi}{6}\).

\(\sin x = -1\): \(x = \frac{3\pi}{2}\).

**Answer**: \(x = \frac{\pi}{6},\; \frac{5\pi}{6},\; \frac{3\pi}{2}\).

**Pitfalls**: There are three forms for \(\cos 2x\). Here \(1 - 2\sin^{2}x\) is most convenient because the RHS is \(\sin x\). Using \(\cos 2x = 2\cos^{2}x - 1\) would give a quadratic in \(\cos x\) with an extra step to convert.

---

## Problem 10 — Solving (Multiple Angles)

**Approach**: Solve for \(3x\) first, then divide by 3 and find all solutions in the given range for \(x\).

\[
\sin 3x = \frac{\sqrt{3}}{2}.
\]

\(\sin \alpha = \frac{\sqrt{3}}{2}\) when \(\alpha = \frac{\pi}{3} + 2k\pi\) or \(\alpha = \frac{2\pi}{3} + 2k\pi\), for integer \(k\).

So \(3x = \frac{\pi}{3} + 2k\pi\) or \(3x = \frac{2\pi}{3} + 2k\pi\).

\[
x = \frac{\pi}{9} + \frac{2k\pi}{3} \quad \text{or} \quad x = \frac{2\pi}{9} + \frac{2k\pi}{3}.
\]

Now find all \(x \in [0, 2\pi]\).

For \(x = \frac{\pi}{9} + \frac{2k\pi}{3}\):
- \(k = 0\): \(x = \frac{\pi}{9}\)
- \(k = 1\): \(x = \frac{\pi}{9} + \frac{2\pi}{3} = \frac{\pi}{9} + \frac{6\pi}{9} = \frac{7\pi}{9}\)
- \(k = 2\): \(x = \frac{\pi}{9} + \frac{4\pi}{3} = \frac{\pi}{9} + \frac{12\pi}{9} = \frac{13\pi}{9}\)
- \(k = 3\): \(x = \frac{\pi}{9} + 2\pi = \frac{19\pi}{9} > 2\pi\) (excluded)

For \(x = \frac{2\pi}{9} + \frac{2k\pi}{3}\):
- \(k = 0\): \(x = \frac{2\pi}{9}\)
- \(k = 1\): \(x = \frac{2\pi}{9} + \frac{2\pi}{3} = \frac{2\pi}{9} + \frac{6\pi}{9} = \frac{8\pi}{9}\)
- \(k = 2\): \(x = \frac{2\pi}{9} + \frac{4\pi}{3} = \frac{2\pi}{9} + \frac{12\pi}{9} = \frac{14\pi}{9}\)
- \(k = 3\): \(x = \frac{2\pi}{9} + 2\pi = \frac{20\pi}{9} > 2\pi\) (excluded)

**Answer**: \(x = \frac{\pi}{9},\; \frac{2\pi}{9},\; \frac{7\pi}{9},\; \frac{8\pi}{9},\; \frac{13\pi}{9},\; \frac{14\pi}{9}\).

**Pitfalls**: When solving \(\sin(nx) = k\), add \(2k\pi/n\) (not \(2k\pi\)) to the principal solutions after dividing by \(n\). Also check that all generated values lie within the required range.

---

## Problem 11 — Solving (Multiple Angles)

**Approach**: Similar to Problem 10, but with tangent which has period \(\pi\).

\[
\tan 2x = -\sqrt{3}.
\]

\(\tan \alpha = -\sqrt{3}\) when \(\alpha = -\frac{\pi}{3} + k\pi\) (or \(\alpha = \frac{2\pi}{3} + k\pi\)), for integer \(k\).

So \(2x = -\frac{\pi}{3} + k\pi\) or equivalently \(2x = \frac{2\pi}{3} + k\pi\).

\[
x = -\frac{\pi}{6} + \frac{k\pi}{2} \quad \text{or} \quad x = \frac{\pi}{3} + \frac{k\pi}{2}.
\]

Using \(x = \frac{2\pi/3 + k\pi}{2} = \frac{\pi}{3} + \frac{k\pi}{2}\):

- \(k = 0\): \(x = \frac{\pi}{3}\)
- \(k = 1\): \(x = \frac{\pi}{3} + \frac{\pi}{2} = \frac{5\pi}{6}\)
- \(k = 2\): \(x = \frac{\pi}{3} + \pi = \frac{4\pi}{3}\)
- \(k = 3\): \(x = \frac{\pi}{3} + \frac{3\pi}{2} = \frac{11\pi}{6}\)
- \(k = 4\): \(x = \frac{\pi}{3} + 2\pi > 2\pi\) (excluded)

Checking \(x = -\frac{\pi}{6} + \frac{k\pi}{2}\):
- \(k = 1\): \(x = -\frac{\pi}{6} + \frac{\pi}{2} = \frac{\pi}{3}\) (duplicate)
- \(k = 2\): \(x = -\frac{\pi}{6} + \pi = \frac{5\pi}{6}\) (duplicate)
- etc. These produce the same set.

**Answer**: \(x = \frac{\pi}{3},\; \frac{5\pi}{6},\; \frac{4\pi}{3},\; \frac{11\pi}{6}\).

**Pitfalls**: Tangent has period \(\pi\), so the general solution for \(\tan \theta = k\) is \(\theta = \alpha + n\pi\). When solving \(\tan(nx) = k\), the solutions become \(x = \frac{\alpha}{n} + \frac{m\pi}{n}\).

---

## Problem 12 — Solving (Using Compound Identity)

**Approach**: Express \(\sin x + \cos x\) as \(R\sin(x + \alpha)\).

\[
R\sin(x + \alpha) = R(\sin x\cos\alpha + \cos x\sin\alpha) = (R\cos\alpha)\sin x + (R\sin\alpha)\cos x.
\]

Compare with \(\sin x + \cos x\):
- \(R\cos\alpha = 1\)
- \(R\sin\alpha = 1\)

\[
R = \sqrt{1^{2} + 1^{2}} = \sqrt{2}.
\]

\[
\cos\alpha = \frac{1}{\sqrt{2}},\; \sin\alpha = \frac{1}{\sqrt{2}} \Rightarrow \alpha = \frac{\pi}{4}.
\]

So \(\sin x + \cos x = \sqrt{2}\sin\left(x + \frac{\pi}{4}\right)\).

Equation: \(\sqrt{2}\sin\left(x + \frac{\pi}{4}\right) = 1 \Rightarrow \sin\left(x + \frac{\pi}{4}\right) = \frac{1}{\sqrt{2}}\).

\[
x + \frac{\pi}{4} = \frac{\pi}{4} + 2k\pi \quad \text{or} \quad x + \frac{\pi}{4} = \frac{3\pi}{4} + 2k\pi.
\]

Case 1: \(x + \frac{\pi}{4} = \frac{\pi}{4} + 2k\pi \Rightarrow x = 2k\pi\).
- In \([0, 2\pi]\): \(x = 0\) and \(x = 2\pi\).

Case 2: \(x + \frac{\pi}{4} = \frac{3\pi}{4} + 2k\pi \Rightarrow x = \frac{\pi}{2} + 2k\pi\).
- In \([0, 2\pi]\): \(x = \frac{\pi}{2}\).

**Answer**: \(x = 0,\; \frac{\pi}{2},\; 2\pi\).

**Pitfalls**: Both \(x = 0\) and \(x = 2\pi\) are valid in the closed interval \([0, 2\pi]\). The harmonic form \(R\sin(x + \alpha)\) is a powerful technique for solving \(\sin x + \cos x = c\).

---

## Problem 13 — Reciprocal Trig (Equation with \(\sec\))

**Approach**: Let \(u = \sec x\) and solve the quadratic, then convert to \(\cos x\).

\[
\sec^{2} x - 3\sec x + 2 = 0.
\]

Let \(u = \sec x\): \(u^{2} - 3u + 2 = 0 \Rightarrow (u - 1)(u - 2) = 0\).

\(u = 1\) or \(u = 2\).

\(\sec x = 1 \Rightarrow \cos x = 1\): \(x = 0,\; 2\pi\).

\(\sec x = 2 \Rightarrow \cos x = \frac{1}{2}\): \(x = \frac{\pi}{3},\; \frac{5\pi}{3}\).

**Answer**: \(x = 0,\; \frac{\pi}{3},\; \frac{5\pi}{3},\; 2\pi\).

**Pitfalls**: \(\sec x = \frac{1}{\cos x}\), so \(\sec x = 2\) gives \(\cos x = \frac{1}{2}\). Always convert to sine/cosine to solve.

---

## Problem 14 — Reciprocal Trig (Equation with \(\csc\) and \(\cot\))

**Approach**: Express in terms of sine and cosine.

\[
\csc x = 2\cot x.
\]

\[
\frac{1}{\sin x} = 2 \cdot \frac{\cos x}{\sin x}.
\]

Multiply both sides by \(\sin x\) (noting \(\sin x \neq 0\)):

\[
1 = 2\cos x \Rightarrow \cos x = \frac{1}{2}.
\]

In \([0, 2\pi]\): \(x = \frac{\pi}{3},\; \frac{5\pi}{3}\).

Check: For both, \(\sin x \neq 0\) ✓.

**Answer**: \(x = \frac{\pi}{3},\; \frac{5\pi}{3}\).

**Pitfalls**: Multiplying by \(\sin x\) assumes \(\sin x \neq 0\). Check that no solutions with \(\sin x = 0\) were lost — \(\csc x\) is undefined at those points anyway, so they cannot be solutions.

---

## Problem 15 — Inverse Trig (Evaluation)

**(a)** \(\arcsin\left(\frac{1}{2}\right)\): The angle in \(\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]\) whose sine is \(\frac{1}{2}\). That is \(\frac{\pi}{6}\).

**(b)** \(\arccos\left(-\frac{\sqrt{3}}{2}\right)\): The angle in \([0, \pi]\) whose cosine is \(-\frac{\sqrt{3}}{2}\). \(\cos \frac{5\pi}{6} = -\frac{\sqrt{3}}{2}\). Answer: \(\frac{5\pi}{6}\).

**(c)** \(\arctan(-1)\): The angle in \(\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)\) whose tangent is \(-1\). That is \(-\frac{\pi}{4}\).

**(d)** \(\cos(\arcsin(\frac{3}{5}))\): Let \(\theta = \arcsin(\frac{3}{5})\), so \(\sin\theta = \frac{3}{5}\) and \(\theta \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right]\). In this range, \(\cos\theta \geq 0\).

\[
\cos\theta = \sqrt{1 - \sin^{2}\theta} = \sqrt{1 - \frac{9}{25}} = \sqrt{\frac{16}{25}} = \frac{4}{5}.
\]

**Answer**: (a) \(\frac{\pi}{6}\); (b) \(\frac{5\pi}{6}\); (c) \(-\frac{\pi}{4}\); (d) \(\frac{4}{5}\).

**Pitfalls**: The range of \(\arcsin\) is \(\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]\), of \(\arccos\) is \([0, \pi]\), and of \(\arctan\) is \(\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)\). These principal ranges determine the sign of compositions.

---

## Problem 16 — Inverse Trig (Composition)

**Approach**: Let \(A = \arcsin(\frac{2}{3})\) and \(B = \arccos(\frac{1}{4})\). Find \(\tan(A + B)\).

We need \(\tan(A + B) = \frac{\tan A + \tan B}{1 - \tan A \tan B}\).

For \(A = \arcsin(\frac{2}{3})\): \(\sin A = \frac{2}{3}\). Using a right triangle with opposite 2, hypotenuse 3, adjacent = \(\sqrt{3^{2} - 2^{2}} = \sqrt{5}\).

Since \(\arcsin\) range is \(\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]\) and \(\sin A > 0\), \(A\) is in Q1, so \(\tan A = \frac{2}{\sqrt{5}}\).

For \(B = \arccos(\frac{1}{4})\): \(\cos B = \frac{1}{4}\). Using a right triangle with adjacent 1, hypotenuse 4, opposite = \(\sqrt{4^{2} - 1^{2}} = \sqrt{15}\).

\(\arccos\) range is \([0, \pi]\) and \(\cos B > 0\), so \(B\) is in Q1, \(\tan B = \frac{\sqrt{15}}{1} = \sqrt{15}\).

Now:

\[
\tan(A + B) = \frac{\frac{2}{\sqrt{5}} + \sqrt{15}}{1 - \frac{2}{\sqrt{5}} \cdot \sqrt{15}} = \frac{\frac{2}{\sqrt{5}} + \sqrt{15}}{1 - \frac{2\sqrt{15}}{\sqrt{5}}} = \frac{\frac{2}{\sqrt{5}} + \sqrt{15}}{1 - 2\sqrt{3}}.
\]

Simplify numerator: \(\frac{2}{\sqrt{5}} + \sqrt{15} = \frac{2 + \sqrt{75}}{\sqrt{5}} = \frac{2 + 5\sqrt{3}}{\sqrt{5}}\).

Denominator: \(1 - 2\sqrt{3}\).

\[
\tan(A + B) = \frac{2 + 5\sqrt{3}}{\sqrt{5}(1 - 2\sqrt{3})}.
\]

Rationalize: multiply numerator and denominator by \((1 + 2\sqrt{3})\):

\[
= \frac{(2 + 5\sqrt{3})(1 + 2\sqrt{3})}{\sqrt{5}(1 - 12)} = \frac{(2 + 5\sqrt{3})(1 + 2\sqrt{3})}{-11\sqrt{5}}.
\]

Expand numerator: \((2 + 5\sqrt{3})(1 + 2\sqrt{3}) = 2 + 4\sqrt{3} + 5\sqrt{3} + 10 \cdot 3 = 2 + 9\sqrt{3} + 30 = 32 + 9\sqrt{3}\).

\[
\tan(A + B) = -\frac{32 + 9\sqrt{3}}{11\sqrt{5}} = -\frac{(32 + 9\sqrt{3})\sqrt{5}}{55}.
\]

**Answer**: \(\tan\left(\arcsin(\frac{2}{3}) + \arccos(\frac{1}{4})\right) = -\dfrac{(32 + 9\sqrt{3})\sqrt{5}}{55}\).

**Pitfalls**: Carefully determine the sign of \(\tan A\) and \(\tan B\) based on the principal ranges. Both are positive here because the arguments are positive and within Q1. The rationalization step requires care with signs.

---

## Problem 17 — Radians (Arc Length, Sector & Segment Area)

**Approach**: Use the formulas \(s = r\theta\), \(A_{\text{sector}} = \frac{1}{2}r^{2}\theta\), and \(A_{\text{segment}} = A_{\text{sector}} - A_{\text{triangle}}\).

Given: \(r = 12\text{ cm}\), \(\theta = \frac{2\pi}{3}\).

**(a)** Arc length: \(s = r\theta = 12 \times \frac{2\pi}{3} = 8\pi\text{ cm}\).

**(b)** Sector area: \(A_{\text{sector}} = \frac{1}{2}r^{2}\theta = \frac{1}{2} \times 144 \times \frac{2\pi}{3} = 144 \times \frac{\pi}{3} = 48\pi\text{ cm}^{2}\).

**(c)** Segment area: The triangle formed by two radii and the chord has area \(\frac{1}{2}r^{2}\sin\theta\).

\[
A_{\text{triangle}} = \frac{1}{2} \times 144 \times \sin\left(\frac{2\pi}{3}\right) = 72 \times \frac{\sqrt{3}}{2} = 36\sqrt{3}.
\]

\[
A_{\text{segment}} = A_{\text{sector}} - A_{\text{triangle}} = 48\pi - 36\sqrt{3}\text{ cm}^{2}.
\]

**Answer**: (a) \(8\pi\text{ cm}\); (b) \(48\pi\text{ cm}^{2}\); (c) \((48\pi - 36\sqrt{3})\text{ cm}^{2}\).

**Pitfalls**: The formula for triangle area using two sides and included angle is \(\frac{1}{2}ab\sin C\). The segment is the sector minus the triangle — not the other way around.

---

## Problem 18 — Radians (Arc Length — Pendulum)

**Approach**: Convert degrees to radians, then use \(s = r\theta\).

\[
\theta = 18^{\circ} = 18 \times \frac{\pi}{180} = \frac{\pi}{10}\text{ radians}.
\]

Arc length: \(s = r\theta = 40 \times \frac{\pi}{10} = 4\pi \approx 12.57\text{ cm}\).

**Answer**: \(4\pi \approx 12.57\text{ cm}\).

**Pitfalls**: The arc length formula \(s = r\theta\) requires \(\theta\) in radians. Always convert degrees to radians first.

---

## Problem 19 — Radians (Segment Area)

**Approach**: Sector area minus triangle area.

Given: \(r = 10\text{ cm}\), \(\theta = \frac{\pi}{3}\).

Sector area: \(A_{\text{sector}} = \frac{1}{2}r^{2}\theta = \frac{1}{2} \times 100 \times \frac{\pi}{3} = \frac{50\pi}{3}\).

Triangle area: \(A_{\text{triangle}} = \frac{1}{2}r^{2}\sin\theta = \frac{1}{2} \times 100 \times \sin\left(\frac{\pi}{3}\right) = 50 \times \frac{\sqrt{3}}{2} = 25\sqrt{3}\).

Segment area: \(A_{\text{segment}} = \frac{50\pi}{3} - 25\sqrt{3}\text{ cm}^{2}\).

**Answer**: \(\left(\dfrac{50\pi}{3} - 25\sqrt{3}\right)\text{ cm}^{2}\).

**Pitfalls**: With \(\theta = \frac{\pi}{3}\), the triangle is equilateral, and its area could also be found using \(\frac{\sqrt{3}}{4}a^{2}\). Both approaches give the same result.

---

## Problem 20 — Volume of Revolution (Disk Method, \(x\)-axis)

**Approach**: Use \(V = \pi \int_{a}^{b} y^{2}\,dx\) for rotation about the \(x\)-axis.

\[
y = \sqrt{x}, \quad y^{2} = x.
\]

\[
V = \pi \int_{1}^{4} x\,dx = \pi \left[\frac{x^{2}}{2}\right]_{1}^{4} = \pi \left(\frac{16}{2} - \frac{1}{2}\right) = \pi \left(8 - \frac{1}{2}\right) = \frac{15\pi}{2}.
\]

**Answer**: \(\dfrac{15\pi}{2}\text{ cubic units}\).

**Pitfalls**: The formula is \(\pi \int y^{2}\,dx\), not \(\pi \int y\,dx\). For rotation about the \(x\)-axis, the integrand is the square of the function.

---

## Problem 21 — Volume of Revolution (Disk Method, \(y\)-axis)

**Approach**: For rotation about the \(y\)-axis, express \(x\) in terms of \(y\) and use \(V = \pi \int x^{2}\,dy\).

Given: \(y = x^{2}\), so \(x = \sqrt{y}\) (positive since \(x \geq 0\) in the region). Limits: from \(y = 0\) to \(y = 4\).

\[
V = \pi \int_{0}^{4} x^{2}\,dy = \pi \int_{0}^{4} y\,dy = \pi \left[\frac{y^{2}}{2}\right]_{0}^{4} = \pi \times \frac{16}{2} = 8\pi.
\]

**Answer**: \(8\pi\text{ cubic units}\).

**Pitfalls**: When rotating about the \(y\)-axis, the integrand is \(x^{2}\) (as a function of \(y\)), not \(y^{2}\). The limits are \(y\)-values, not \(x\)-values.

---

## Problem 22 — Volume of Revolution (Washer Method)

**Approach**: Find the intersection points, then use the washer formula \(V = \pi \int (R^{2} - r^{2})\,dx\).

Intersection of \(y = x^{2}\) and \(y = 2x\):
\[
x^{2} = 2x \Rightarrow x^{2} - 2x = 0 \Rightarrow x(x - 2) = 0 \Rightarrow x = 0 \text{ or } x = 2.
\]

On \([0, 2]\), which curve is above? At \(x = 1\): \(x^{2} = 1\), \(2x = 2\). So \(y = 2x\) is above \(y = x^{2}\).

Outer radius: \(R = 2x\). Inner radius: \(r = x^{2}\).

\[
V = \pi \int_{0}^{2} \left[(2x)^{2} - (x^{2})^{2}\right]\,dx = \pi \int_{0}^{2} (4x^{2} - x^{4})\,dx.
\]

\[
V = \pi \left[\frac{4x^{3}}{3} - \frac{x^{5}}{5}\right]_{0}^{2} = \pi \left(\frac{4 \times 8}{3} - \frac{32}{5}\right) = \pi \left(\frac{32}{3} - \frac{32}{5}\right).
\]

\[
\frac{32}{3} - \frac{32}{5} = 32\left(\frac{1}{3} - \frac{1}{5}\right) = 32 \times \frac{5 - 3}{15} = 32 \times \frac{2}{15} = \frac{64}{15}.
\]

\[
V = \frac{64\pi}{15}.
\]

**Answer**: \(\dfrac{64\pi}{15}\text{ cubic units}\).

**Pitfalls**: Determining which function is the outer curve. On \([0, 2]\), \(2x \geq x^{2}\), so \(R = 2x\) and \(r = x^{2}\). If you swap them, you get a negative volume (or take absolute value).

---

## Problem 23 — Trig + Calculus (Connected)

**Approach**: For \(y = \sin x\), \(0 \leq x \leq \pi\), rotated about the \(x\)-axis.

**(a)** \(V = \pi \int_{0}^{\pi} \sin^{2} x\,dx\).

**(b)** Use \(\sin^{2} x = \frac{1 - \cos 2x}{2}\):

\[
V = \pi \int_{0}^{\pi} \frac{1 - \cos 2x}{2}\,dx = \frac{\pi}{2} \int_{0}^{\pi} (1 - \cos 2x)\,dx.
\]

**(c)** \[
V = \frac{\pi}{2} \left[x - \frac{\sin 2x}{2}\right]_{0}^{\pi} = \frac{\pi}{2} \left[\left(\pi - \frac{\sin 2\pi}{2}\right) - \left(0 - \frac{\sin 0}{2}\right)\right].
\]

\(\sin 2\pi = 0\), \(\sin 0 = 0\).

\[
V = \frac{\pi}{2} \times \pi = \frac{\pi^{2}}{2}.
\]

**Answer**: \(\dfrac{\pi^{2}}{2}\text{ cubic units}\).

**Pitfalls**: The integral of \(\sin^{2} x\) is not \(-\cos^{2} x\) or similar. Always use the double-angle identity \(\sin^{2} x = \frac{1 - \cos 2x}{2}\) to integrate.

---

## Problem 24 — Trig + Calculus (Connected)

**Approach**: Product rule for differentiation, then tangent line and volume setup.

**(a)** \(f(x) = x\cos x\).

\[
f'(x) = 1 \cdot \cos x + x \cdot (-\sin x) = \cos x - x\sin x.
\]

**(b)** At \(x = \frac{\pi}{3}\):

\[
f\left(\frac{\pi}{3}\right) = \frac{\pi}{3} \cos\frac{\pi}{3} = \frac{\pi}{3} \cdot \frac{1}{2} = \frac{\pi}{6}.
\]

\[
f'\left(\frac{\pi}{3}\right) = \cos\frac{\pi}{3} - \frac{\pi}{3}\sin\frac{\pi}{3} = \frac{1}{2} - \frac{\pi}{3} \cdot \frac{\sqrt{3}}{2} = \frac{1}{2} - \frac{\pi\sqrt{3}}{6}.
\]

Tangent line: \(y - y_{0} = m(x - x_{0})\):

\[
y - \frac{\pi}{6} = \left(\frac{1}{2} - \frac{\pi\sqrt{3}}{6}\right)\left(x - \frac{\pi}{3}\right).
\]

\[
y = \frac{\pi}{6} + \left(\frac{1}{2} - \frac{\pi\sqrt{3}}{6}\right)\left(x - \frac{\pi}{3}\right).
\]

**(c)** Volume integral for rotation about the \(x\)-axis:

\[
V = \pi \int_{0}^{\frac{\pi}{2}} [f(x)]^{2}\,dx = \pi \int_{0}^{\frac{\pi}{2}} x^{2}\cos^{2} x\,dx.
\]

**Answer**: (a) \(f'(x) = \cos x - x\sin x\); (b) \(y = \frac{\pi}{6} + \left(\frac{1}{2} - \frac{\pi\sqrt{3}}{6}\right)\left(x - \frac{\pi}{3}\right)\); (c) \(V = \pi \int_{0}^{\frac{\pi}{2}} x^{2}\cos^{2} x\,dx\).

**Pitfalls**: The product rule: \(\frac{d}{dx}(x\cos x) = \cos x - x\sin x\). Common error: forgetting the negative sign from the derivative of \(\cos x\).

---

## Problem 25 — Multi-part (Trig Equations, Radians & Transformations)

**Approach**: Analyze the sinusoidal function, solve the equation, and determine the translation to move the minimum to the origin.

\(f(x) = 3\sin\left(2x - \frac{\pi}{3}\right) + 1\).

**(a)** Write as \(f(x) = 3\sin\left(2\left[x - \frac{\pi}{6}\right]\right) + 1\).

- Amplitude: \(A = 3\).
- Period: \(\frac{2\pi}{2} = \pi\).
- Phase shift: \(\frac{\pi}{6}\) to the right (from \(2x - \frac{\pi}{3} = 2(x - \frac{\pi}{6})\)).
- Vertical shift: up by 1. Range: \([-2, 4]\).

**(b)** Solve \(3\sin\left(2x - \frac{\pi}{3}\right) + 1 = 2.5\):

\[
3\sin\left(2x - \frac{\pi}{3}\right) = 1.5 \Rightarrow \sin\left(2x - \frac{\pi}{3}\right) = 0.5.
\]

\[
2x - \frac{\pi}{3} = \arcsin(0.5) = \frac{\pi}{6} + 2k\pi \quad \text{or} \quad 2x - \frac{\pi}{3} = \pi - \frac{\pi}{6} + 2k\pi = \frac{5\pi}{6} + 2k\pi.
\]

Case 1: \(2x - \frac{\pi}{3} = \frac{\pi}{6} + 2k\pi \Rightarrow 2x = \frac{\pi}{6} + \frac{\pi}{3} + 2k\pi = \frac{\pi}{2} + 2k\pi \Rightarrow x = \frac{\pi}{4} + k\pi\).

For \(x \in [0, 2\pi]\): \(k = 0 \Rightarrow x = \frac{\pi}{4} \approx 0.785\); \(k = 1 \Rightarrow x = \frac{5\pi}{4} \approx 3.93\).

Case 2: \(2x - \frac{\pi}{3} = \frac{5\pi}{6} + 2k\pi \Rightarrow 2x = \frac{5\pi}{6} + \frac{\pi}{3} + 2k\pi = \frac{5\pi}{6} + \frac{2\pi}{6} + 2k\pi = \frac{7\pi}{6} + 2k\pi \Rightarrow x = \frac{7\pi}{12} + k\pi\).

For \(x \in [0, 2\pi]\): \(k = 0 \Rightarrow x = \frac{7\pi}{12} \approx 1.83\); \(k = 1 \Rightarrow x = \frac{19\pi}{12} \approx 4.97\).

To 3 s.f.: \(x = 0.785,\; 1.83,\; 3.93,\; 4.97\).

**(c)** The minimum value of \(f\) is \(1 - 3 = -2\), occurring when \(\sin(2x - \frac{\pi}{3}) = -1\):

\[
2x - \frac{\pi}{3} = \frac{3\pi}{2} + 2k\pi \Rightarrow 2x = \frac{3\pi}{2} + \frac{\pi}{3} + 2k\pi = \frac{9\pi + 2\pi}{6} + 2k\pi = \frac{11\pi}{6} + 2k\pi.
\]

For the principal minimum (smallest positive \(x\)): \(k = 0 \Rightarrow x = \frac{11\pi}{12}\). The minimum point is \(\left(\frac{11\pi}{12}, -2\right)\).

To map the minimum to the origin, translate left by \(\frac{11\pi}{12}\) and up by 2 (vector \(\begin{pmatrix}-\frac{11\pi}{12} \\ 2\end{pmatrix}\)).

Transformed equation: \(y - 2 = 3\sin\left(2(x + \frac{11\pi}{12}) - \frac{\pi}{3}\right) + 1\).

Simplify the argument: \(2x + \frac{11\pi}{6} - \frac{\pi}{3} = 2x + \frac{11\pi}{6} - \frac{2\pi}{6} = 2x + \frac{9\pi}{6} = 2x + \frac{3\pi}{2}\).

Transformed: \(y - 2 = 3\sin(2x + \frac{3\pi}{2}) + 1 \Rightarrow y = 3\sin(2x + \frac{3\pi}{2}) + 3\).

Since \(\sin(\theta + \frac{3\pi}{2}) = -\cos\theta\), this is \(y = -3\cos(2x) + 3\).

**Answer**: (a) Amplitude = 3, Period = \(\pi\), Phase shift = \(\frac{\pi}{6}\) right; (b) \(x \approx 0.785,\; 1.83,\; 3.93,\; 4.97\); (c) Translation: vector \(\begin{pmatrix}-\frac{11\pi}{12} \\ 2\end{pmatrix}\); equation: \(y = 3\sin(2x + \frac{3\pi}{2}) + 3\) or equivalently \(y = 3 - 3\cos(2x)\).

**Pitfalls**: When solving \(\sin(2x - \frac{\pi}{3}) = 0.5\), the general solution includes all solutions within the period. After finding \(2x - \frac{\pi}{3}\), remember to divide by 2 and add \(\frac{\pi}{3}\) correctly. For the translation, identify the coordinates of the minimum precisely.

---
