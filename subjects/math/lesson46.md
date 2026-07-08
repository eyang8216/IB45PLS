# Lesson 46: Trigonometry — Compound and Double Angle Identities

## What You Will Learn and Why It Matters

When you add two angles together and take the sine, the result is **not** $\sin A + \sin B$. Instead, sine and cosine follow specific expansion formulas called the **compound angle identities**. From these, you can derive the **double angle identities** (when both angles are the same) and the half-angle identities. These formulas are among the most heavily used tools in the entire IB AAHL course. You need them to find exact values of trigonometric expressions without a calculator, to prove other identities, to solve trigonometric equations, to differentiate and integrate trigonometric functions, and to work with complex numbers in polar form. If you invest time in memorizing and practicing these now, you will save yourself enormous effort later.

---

## 1. The Compound Angle Formulas

For any angles $A$ and $B$ (measured in radians or degrees, the formulas work the same):

$$\sin(A + B) = \sin A \cos B + \cos A \sin B$$

$$\sin(A - B) = \sin A \cos B - \cos A \sin B$$

$$\cos(A + B) = \cos A \cos B - \sin A \sin B$$

$$\cos(A - B) = \cos A \cos B + \sin A \sin B$$

$$\tan(A + B) = \frac{\tan A + \tan B}{1 - \tan A \tan B}$$

$$\tan(A - B) = \frac{\tan A - \tan B}{1 + \tan A \tan B}$$

**How to remember the patterns:** For sine, the sign between the terms matches the sign between the angles: $\sin(A + B)$ has a plus between $\sin A \cos B$ and $\cos A \sin B$. For cosine, the sign is opposite: $\cos(A + B)$ has a minus between the terms. For tangent, the numerator has the same sign and the denominator has the opposite sign.

---

## 2. Using Compound Angle Formulas to Find Exact Values

The compound angle formulas allow you to compute the sine, cosine, or tangent of angles that are sums or differences of the standard angles you have memorized ($30^\circ$, $45^\circ$, $60^\circ$, and their radian equivalents).

### Worked Example 1

**Problem:** Find the exact value of $\sin 75^\circ$ without using a calculator.

**Approach:** Write $75^\circ$ as the sum of two standard angles: $75^\circ = 45^\circ + 30^\circ$. Then apply the sine addition formula.

**Step-by-step working:**
1. $\sin 75^\circ = \sin(45^\circ + 30^\circ)$.
2. Apply the formula: $\sin(45^\circ + 30^\circ) = \sin 45^\circ \cos 30^\circ + \cos 45^\circ \sin 30^\circ$.
3. Substitute the known exact values: $\sin 45^\circ = \frac{\sqrt{2}}{2}$, $\cos 30^\circ = \frac{\sqrt{3}}{2}$, $\cos 45^\circ = \frac{\sqrt{2}}{2}$, $\sin 30^\circ = \frac{1}{2}$.
4. Compute: $\frac{\sqrt{2}}{2} \cdot \frac{\sqrt{3}}{2} + \frac{\sqrt{2}}{2} \cdot \frac{1}{2} = \frac{\sqrt{6}}{4} + \frac{\sqrt{2}}{4}$.
5. Combine: $\frac{\sqrt{6} + \sqrt{2}}{4}$.

The exact value of $\sin 75^\circ$ is $\dfrac{\sqrt{6} + \sqrt{2}}{4}$.

**Why this makes sense:** You can approximate this: $\sqrt{6} \approx 2.449$ and $\sqrt{2} \approx 1.414$, so the numerator is about $3.863$, giving approximately $0.966$. The sine of $75^\circ$ should indeed be close to $1$.

---

### Worked Example 2

**Problem:** Find the exact value of $\cos 15^\circ$ without a calculator.

**Approach:** Write $15^\circ$ as a difference: $15^\circ = 45^\circ - 30^\circ$. Apply the cosine subtraction formula.

**Step-by-step working:**
1. $\cos 15^\circ = \cos(45^\circ - 30^\circ)$.
2. Apply the formula: $\cos(45^\circ - 30^\circ) = \cos 45^\circ \cos 30^\circ + \sin 45^\circ \sin 30^\circ$. (Notice the plus sign — the formula for $\cos(A - B)$ has a plus.)
3. Substitute: $\frac{\sqrt{2}}{2} \cdot \frac{\sqrt{3}}{2} + \frac{\sqrt{2}}{2} \cdot \frac{1}{2} = \frac{\sqrt{6}}{4} + \frac{\sqrt{2}}{4}$.
4. Combine: $\frac{\sqrt{6} + \sqrt{2}}{4}$.

The exact value of $\cos 15^\circ$ is also $\dfrac{\sqrt{6} + \sqrt{2}}{4}$.

**Why this makes sense:** Since $\sin 75^\circ = \cos 15^\circ$ (because $\sin\theta = \cos(90^\circ - \theta)$), the two worked examples should give the same answer. They do.

---

## 3. Double Angle Formulas

Set $B = A$ in the compound angle formulas. This gives the double angle identities:

$$\sin(2A) = 2\sin A \cos A$$

$$\cos(2A) = \cos^2 A - \sin^2 A = 2\cos^2 A - 1 = 1 - 2\sin^2 A$$

$$\tan(2A) = \frac{2\tan A}{1 - \tan^2 A}$$

The three forms of $\cos(2A)$ are all algebraically equivalent. You can prove this by substituting $\sin^2 A = 1 - \cos^2 A$ or $\cos^2 A = 1 - \sin^2 A$ into the first form. Choose the form that best matches the problem you are solving.

### Worked Example 3

**Problem:** Given that $\sin A = \dfrac{3}{5}$ and $A$ is an acute angle (between $0$ and $90^\circ$), find $\sin(2A)$.

**Approach:** First find $\cos A$ using the identity $\sin^2 A + \cos^2 A = 1$. Then apply $\sin(2A) = 2\sin A \cos A$.

**Step-by-step working:**
1. $\sin^2 A = \left(\frac{3}{5}\right)^2 = \frac{9}{25}$.
2. From $\sin^2 A + \cos^2 A = 1$: $\frac{9}{25} + \cos^2 A = 1$, so $\cos^2 A = \frac{16}{25}$.
3. Since $A$ is acute, $\cos A$ is positive: $\cos A = \sqrt{\frac{16}{25}} = \frac{4}{5}$.
4. $\sin(2A) = 2\sin A \cos A = 2 \cdot \frac{3}{5} \cdot \frac{4}{5} = \frac{24}{25}$.

**Why this makes sense:** Since $\sin A = 0.6$ and $A$ is acute, $A$ is approximately $36.87^\circ$. Double that is about $73.74^\circ$, whose sine should be close to $0.96$ ($\frac{24}{25} = 0.96$). The answer is reasonable.

---

### Worked Example 4

**Problem:** Express $\sin(3A)$ in terms of $\sin A$ only.

**Approach:** Write $3A$ as $2A + A$ and apply the compound angle formula. Then replace $\sin(2A)$ and $\cos(2A)$ with the double angle formulas. Finally, replace any $\cos^2 A$ with $1 - \sin^2 A$.

**Step-by-step working:**
1. $\sin(3A) = \sin(2A + A) = \sin(2A)\cos A + \cos(2A)\sin A$.
2. Substitute $\sin(2A) = 2\sin A \cos A$: the first term becomes $(2\sin A \cos A)\cos A = 2\sin A \cos^2 A$.
3. Substitute $\cos(2A) = 1 - 2\sin^2 A$ (choosing the form that uses only $\sin A$): the second term becomes $(1 - 2\sin^2 A)\sin A = \sin A - 2\sin^3 A$.
4. Combine: $2\sin A \cos^2 A + \sin A - 2\sin^3 A$.
5. Replace $\cos^2 A$ with $1 - \sin^2 A$: $2\sin A(1 - \sin^2 A) + \sin A - 2\sin^3 A = 2\sin A - 2\sin^3 A + \sin A - 2\sin^3 A = 3\sin A - 4\sin^3 A$.

The result is $\sin(3A) = 3\sin A - 4\sin^3 A$.

**Why this makes sense:** When $A = 30^\circ$, $\sin A = \frac{1}{2}$. The formula gives $3 \cdot \frac{1}{2} - 4 \cdot \frac{1}{8} = \frac{3}{2} - \frac{1}{2} = 1 = \sin 90^\circ = \sin(3 \times 30^\circ)$. It checks out.

---

## 4. Half-Angle Formulas

From the double angle formulas, you can derive expressions for $\sin^2 A$ and $\cos^2 A$ in terms of $\cos(2A)$:

$$\sin^2 A = \frac{1 - \cos(2A)}{2}$$

$$\cos^2 A = \frac{1 + \cos(2A)}{2}$$

These are called the **half-angle formulas** (or power-reducing formulas). They are essential in calculus when you need to integrate $\sin^2 x$ or $\cos^2 x$.

---

## 5. Proving Trigonometric Identities

Proving identities means showing that one trigonometric expression can be transformed into another using known identities. There is no single algorithm. The strategy is to start from the more complicated side and simplify, or to express everything in terms of sine and cosine, or to recognize a pattern that matches a known identity.

### Worked Example 5

**Problem:** Prove the identity $(\sin A + \cos A)^2 = 1 + \sin(2A)$.

**Approach:** Expand the left-hand side and then recognize the double angle pattern.

**Step-by-step working:**
1. Expand the left side: $(\sin A + \cos A)^2 = \sin^2 A + 2\sin A \cos A + \cos^2 A$.
2. Group $\sin^2 A + \cos^2 A = 1$.
3. Recognize that $2\sin A \cos A = \sin(2A)$.
4. So the left side equals $1 + \sin(2A)$, which is the right side. The identity is proved.

---

### Worked Example 6

**Problem:** Prove the identity $\tan A + \cot A = \dfrac{2}{\sin(2A)}$.

**Approach:** Write $\tan A$ and $\cot A$ in terms of sine and cosine. Combine into a single fraction. Recognize the double angle form.

**Step-by-step working:**
1. $\tan A = \dfrac{\sin A}{\cos A}$ and $\cot A = \dfrac{\cos A}{\sin A}$.
2. Find a common denominator: $\dfrac{\sin^2 A + \cos^2 A}{\sin A \cos A}$.
3. The numerator $\sin^2 A + \cos^2 A = 1$.
4. The denominator $\sin A \cos A = \frac{1}{2}\sin(2A)$.
5. So the left side equals $\dfrac{1}{\frac{1}{2}\sin(2A)} = \dfrac{2}{\sin(2A)}$. The identity is proved.

---

## Practice Problems

**1.** Find the exact value of $\sin 105^\circ$ without using a calculator.

**2.** Find the exact value of $\tan 15^\circ$ without using a calculator.

**3.** Given that $\sin A = \dfrac{5}{13}$ and $A$ is an acute angle, find the exact value of $\cos(2A)$.

**4.** Prove the identity $\dfrac{1 - \cos(2A)}{1 + \cos(2A)} = \tan^2 A$.

**5.** (IB Exam Style)

(a) Use the compound angle formula to express $\cos(4A)$ in terms of $\cos(2A)$ only. [2 marks]

(b) Hence express $\cos(4A)$ in terms of $\cos A$ only, simplifying your answer. [3 marks]

(c) Verify your formula by evaluating both sides when $A = \dfrac{\pi}{6}$. [1 mark]

**6.** Prove the identity $\sin(A + B)\sin(A - B) = \sin^2 A - \sin^2 B$.

---

## Answers

**1.** Write $105^\circ$ as $60^\circ + 45^\circ$. Then $\sin 105^\circ = \sin(60^\circ + 45^\circ) = \sin 60^\circ \cos 45^\circ + \cos 60^\circ \sin 45^\circ = \frac{\sqrt{3}}{2} \cdot \frac{\sqrt{2}}{2} + \frac{1}{2} \cdot \frac{\sqrt{2}}{2} = \frac{\sqrt{6}}{4} + \frac{\sqrt{2}}{4} = \frac{\sqrt{6} + \sqrt{2}}{4}$. This is the same as $\sin 75^\circ$ from Worked Example 1, which makes sense because $\sin(105^\circ) = \sin(180^\circ - 105^\circ) = \sin 75^\circ$.

**2.** Write $15^\circ$ as $45^\circ - 30^\circ$. Then $\tan 15^\circ = \tan(45^\circ - 30^\circ) = \frac{\tan 45^\circ - \tan 30^\circ}{1 + \tan 45^\circ \tan 30^\circ} = \frac{1 - \frac{1}{\sqrt{3}}}{1 + 1 \cdot \frac{1}{\sqrt{3}}} = \frac{\frac{\sqrt{3} - 1}{\sqrt{3}}}{\frac{\sqrt{3} + 1}{\sqrt{3}}} = \frac{\sqrt{3} - 1}{\sqrt{3} + 1}$. To rationalize, multiply numerator and denominator by $(\sqrt{3} - 1)$: $\frac{(\sqrt{3} - 1)^2}{(\sqrt{3} + 1)(\sqrt{3} - 1)} = \frac{3 - 2\sqrt{3} + 1}{3 - 1} = \frac{4 - 2\sqrt{3}}{2} = 2 - \sqrt{3}$. A common error is to forget to rationalize or to mishandle the fraction algebra.

**3.** From $\sin A = \frac{5}{13}$, use $\sin^2 A + \cos^2 A = 1$: $\frac{25}{169} + \cos^2 A = 1$, so $\cos^2 A = \frac{144}{169}$. Since $A$ is acute, $\cos A = \frac{12}{13}$. Then $\cos(2A) = 2\cos^2 A - 1 = 2 \cdot \frac{144}{169} - 1 = \frac{288}{169} - \frac{169}{169} = \frac{119}{169}$. Alternatively, using the form $1 - 2\sin^2 A$: $1 - 2 \cdot \frac{25}{169} = 1 - \frac{50}{169} = \frac{119}{169}$. Both forms agree.

**4.** Use the half-angle forms of $\cos(2A)$. The numerator $1 - \cos(2A) = 1 - (1 - 2\sin^2 A) = 2\sin^2 A$. The denominator $1 + \cos(2A) = 1 + (2\cos^2 A - 1) = 2\cos^2 A$. So the left side becomes $\frac{2\sin^2 A}{2\cos^2 A} = \frac{\sin^2 A}{\cos^2 A} = \tan^2 A$. The identity is proved. This is a classic result that connects double-angle trig to the square of tangent.

**5.** (a) Using $\cos(2\theta) = 2\cos^2\theta - 1$ with $\theta = 2A$: $\cos(4A) = 2\cos^2(2A) - 1$. [2 marks]

(b) Substitute $\cos(2A) = 2\cos^2 A - 1$: $\cos(4A) = 2(2\cos^2 A - 1)^2 - 1$. Expand the square: $(2\cos^2 A - 1)^2 = 4\cos^4 A - 4\cos^2 A + 1$. Then $\cos(4A) = 2(4\cos^4 A - 4\cos^2 A + 1) - 1 = 8\cos^4 A - 8\cos^2 A + 2 - 1 = 8\cos^4 A - 8\cos^2 A + 1$. [3 marks]

(c) When $A = \frac{\pi}{6}$: $\cos A = \frac{\sqrt{3}}{2}$. Then $\cos^2 A = \frac{3}{4}$ and $\cos^4 A = \frac{9}{16}$. The formula gives $8 \cdot \frac{9}{16} - 8 \cdot \frac{3}{4} + 1 = \frac{72}{16} - 6 + 1 = \frac{9}{2} - 5 = \frac{9}{2} - \frac{10}{2} = -\frac{1}{2}$. Directly: $4A = 4 \cdot \frac{\pi}{6} = \frac{2\pi}{3}$, and $\cos\frac{2\pi}{3} = -\frac{1}{2}$. The formula is verified. [1 mark]

**6.** Expand the left side using the compound angle formulas: $\sin(A + B) = \sin A \cos B + \cos A \sin B$ and $\sin(A - B) = \sin A \cos B - \cos A \sin B$. Their product is $(\sin A \cos B)^2 - (\cos A \sin B)^2 = \sin^2 A \cos^2 B - \cos^2 A \sin^2 B$. Replace $\cos^2 B$ with $1 - \sin^2 B$ and $\cos^2 A$ with $1 - \sin^2 A$: this becomes $\sin^2 A(1 - \sin^2 B) - (1 - \sin^2 A)\sin^2 B = \sin^2 A - \sin^2 A \sin^2 B - \sin^2 B + \sin^2 A \sin^2 B = \sin^2 A - \sin^2 B$. The $\sin^2 A \sin^2 B$ terms cancel. The identity is proved.
