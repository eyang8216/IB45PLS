# Lesson 20: Complex Conjugates, Modulus, and Division

## WHAT Are Conjugates and the Modulus?

In Lesson 19 you learned how to add, subtract, and multiply complex numbers. But there is one operation missing: division. How do you divide by a complex number? The answer involves two new concepts: the **complex conjugate** and the **modulus**.

The conjugate gives you a way to turn the denominator of a fraction into a plain real number. The modulus tells you the "size" of a complex number — how far it is from zero. Together, these ideas make complex division possible.

## WHY These Ideas Matter

Without conjugates, you cannot divide complex numbers. Without the modulus, you cannot measure distances between complex numbers or draw them on a diagram (which is the topic of Lesson 21). Conjugates also appear throughout physics and engineering — for example, the complex conjugate is used to compute the power in an AC electrical circuit.

---

## 1. The Complex Conjugate

The **complex conjugate** of a complex number \(z = a + bi\) is written as \(\overline{z}\) (pronounced "z bar"). To find the conjugate, you keep the real part exactly the same and flip the sign of the imaginary part:

\[
\boxed{\overline{z} = a - bi}
\]

Here are some examples to make this concrete:

- If \(z = 3 + 4i\), then \(\overline{z} = 3 - 4i\).
- If \(z = -2 - 5i\), then \(\overline{z} = -2 + 5i\).
- If \(z = 7\) (a real number), then \(\overline{z} = 7\). A real number is its own conjugate because flipping the sign of zero does nothing.
- If \(z = 6i\) (purely imaginary), then \(\overline{z} = -6i\).

**Common misconception:** Some students think the conjugate changes the sign of the real part too. It does not. Only the imaginary part changes sign.

---

## 2. Key Properties of the Conjugate

### Property 1: Multiplying a Number by Its Conjugate Gives a Real Number

This is the most important property. Watch what happens:

\[
z \cdot \overline{z} = (a + bi)(a - bi) = a^2 - (bi)^2 = a^2 - b^2 i^2 = a^2 - b^2(-1) = a^2 + b^2
\]

The answer, \(a^2 + b^2\), is always a real number. It is always zero or positive. It can never be negative because both \(a^2\) and \(b^2\) are non-negative.

**Example:** For \(z = 3 + 4i\), we have \(z \cdot \overline{z} = 3^2 + 4^2 = 9 + 16 = 25\).

### Property 2: Adding a Number and Its Conjugate Gives Twice the Real Part

\[
z + \overline{z} = (a + bi) + (a - bi) = 2a = 2\operatorname{Re}(z)
\]

The imaginary parts cancel out completely.

### Property 3: Subtracting the Conjugate Gives Twice the Imaginary Part (Times \(i\))

\[
z - \overline{z} = (a + bi) - (a - bi) = 2bi = 2i \cdot \operatorname{Im}(z)
\]

### Property 4: Conjugates Play Nicely with Operations

- The conjugate of a sum is the sum of the conjugates: \(\overline{z + w} = \overline{z} + \overline{w}\).
- The conjugate of a product is the product of the conjugates: \(\overline{z \cdot w} = \overline{z} \cdot \overline{w}\).
- The conjugate of a quotient is the quotient of the conjugates: \(\overline{\left(\frac{z}{w}\right)} = \frac{\overline{z}}{\overline{w}}\).
- Taking the conjugate twice returns you to the original number: \(\overline{(\overline{z})} = z\).

These properties mean you can often simplify complicated expressions by taking conjugates at the start or at the end — the result is the same.

---

## 3. The Modulus

The **modulus** of a complex number \(z = a + bi\) is written as \(|z|\) (the same notation as absolute value). It is defined as:

\[
\boxed{|z| = \sqrt{a^2 + b^2}}
\]

You can think of the modulus as the distance from the complex number to zero. (In Lesson 21, you will see this distance drawn on a diagram.)

Notice that \(|z| = \sqrt{z \cdot \overline{z}}\), because we just showed that \(z \cdot \overline{z} = a^2 + b^2\).

**Examples:**

- \(|3 + 4i| = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5\)
- \(|-5 + 12i| = \sqrt{(-5)^2 + 12^2} = \sqrt{25 + 144} = \sqrt{169} = 13\)
- \(|1 + i| = \sqrt{1^2 + 1^2} = \sqrt{2}\)
- \(|6| = \sqrt{6^2 + 0^2} = \sqrt{36} = 6\) — the modulus of a real number is just its absolute value.
- \(|2i| = \sqrt{0^2 + 2^2} = \sqrt{4} = 2\)

**Common misconception:** The modulus is always a real number, and it is always non-negative. It is never a complex number and it never has an \(i\) in it.

---

## 4. Dividing Complex Numbers

You now have all the tools to divide complex numbers. The strategy is:

**Multiply the numerator and denominator by the conjugate of the denominator.**

This works because multiplying the denominator by its conjugate gives a real number (\(c^2 + d^2\)). Once the denominator is real, you can split the fraction into real and imaginary parts.

\[
\boxed{\frac{a + bi}{c + di} = \frac{(a + bi)(c - di)}{(c + di)(c - di)} = \frac{(a + bi)(c - di)}{c^2 + d^2}}
\]

### Worked Example 1 — Standard Division

**Problem:** Evaluate \(\displaystyle \frac{3 + 2i}{1 - i}\). Give your answer in Cartesian form.

**Approach:** The denominator is \(1 - i\). Its conjugate is \(1 + i\). Multiply top and bottom by \(1 + i\).

**Step 1 — Multiply numerator and denominator:**
\[
\frac{3 + 2i}{1 - i} \cdot \frac{1 + i}{1 + i} = \frac{(3 + 2i)(1 + i)}{(1 - i)(1 + i)}
\]

**Step 2 — Simplify the denominator:**
\((1 - i)(1 + i) = 1^2 + 1^2 = 1 + 1 = 2\). The denominator is now a real number: 2.

**Step 3 — Expand the numerator:**
\((3 + 2i)(1 + i) = 3(1) + 3(i) + 2i(1) + 2i(i) = 3 + 3i + 2i + 2i^2 = 3 + 5i + 2(-1) = 3 + 5i - 2 = 1 + 5i\).

**Step 4 — Divide each part by the denominator:**
\[
\frac{1 + 5i}{2} = \frac{1}{2} + \frac{5}{2}i
\]

**Answer:** \(\displaystyle \frac{1}{2} + \frac{5}{2}i\).

**Why this makes sense:** We can check by multiplying back. \((\frac{1}{2} + \frac{5}{2}i)(1 - i)\) should equal \(3 + 2i\). Let us verify: \(\frac{1}{2}(1 - i) + \frac{5}{2}i(1 - i) = \frac{1}{2} - \frac{1}{2}i + \frac{5}{2}i - \frac{5}{2}i^2 = \frac{1}{2} + 2i - \frac{5}{2}(-1) = \frac{1}{2} + 2i + \frac{5}{2} = 3 + 2i\). It works.

### Worked Example 2 — Another Division

**Problem:** Evaluate \(\displaystyle \frac{4 - i}{2 + 3i}\). Give your answer in Cartesian form.

**Approach:** The conjugate of \(2 + 3i\) is \(2 - 3i\). Multiply top and bottom by \(2 - 3i\).

**Step 1 — Set up:**
\[
\frac{4 - i}{2 + 3i} \cdot \frac{2 - 3i}{2 - 3i} = \frac{(4 - i)(2 - 3i)}{(2 + 3i)(2 - 3i)}
\]

**Step 2 — Denominator:**
\((2 + 3i)(2 - 3i) = 2^2 + 3^2 = 4 + 9 = 13\).

**Step 3 — Numerator:**
\((4 - i)(2 - 3i) = 4(2) + 4(-3i) + (-i)(2) + (-i)(-3i) = 8 - 12i - 2i + 3i^2 = 8 - 14i + 3(-1) = 8 - 14i - 3 = 5 - 14i\).

**Step 4 — Divide:**
\[
\frac{5 - 14i}{13} = \frac{5}{13} - \frac{14}{13}i
\]

**Answer:** \(\displaystyle \frac{5}{13} - \frac{14}{13}i\).

### Worked Example 3 — Combining Fractions

**Problem:** Evaluate \(\displaystyle \frac{5}{2 + i} - \frac{5}{2 - i}\).

**Approach:** You could find a common denominator or handle each fraction separately and then subtract. Using a common denominator is cleaner here.

**Step 1 — Common denominator:**
The common denominator is \((2 + i)(2 - i) = 4 + 1 = 5\).

**Step 2 — Combine numerators:**
\[
\frac{5(2 - i) - 5(2 + i)}{(2 + i)(2 - i)} = \frac{10 - 5i - 10 - 5i}{5} = \frac{-10i}{5} = -2i
\]

**Answer:** \(-2i\), which is purely imaginary.

### Worked Example 4 — A Ratio Involving a Number and Its Conjugate

**Problem:** If \(z = 2 + i\), evaluate \(\displaystyle \frac{z}{\overline{z}} + \frac{\overline{z}}{z}\).

**Approach:** First identify \(\overline{z} = 2 - i\). Then compute each fraction and add.

**Step 1:** \(\displaystyle \frac{z}{\overline{z}} = \frac{2 + i}{2 - i}\). Multiply top and bottom by \(2 + i\):
\[
\frac{(2 + i)(2 + i)}{(2 - i)(2 + i)} = \frac{4 + 4i + i^2}{4 + 1} = \frac{4 + 4i - 1}{5} = \frac{3 + 4i}{5}
\]

**Step 2:** \(\displaystyle \frac{\overline{z}}{z} = \frac{2 - i}{2 + i}\). Multiply top and bottom by \(2 - i\):
\[
\frac{(2 - i)(2 - i)}{(2 + i)(2 - i)} = \frac{4 - 4i + i^2}{4 + 1} = \frac{4 - 4i - 1}{5} = \frac{3 - 4i}{5}
\]

**Step 3 — Add:**
\[
\frac{3 + 4i}{5} + \frac{3 - 4i}{5} = \frac{3 + 4i + 3 - 4i}{5} = \frac{6}{5}
\]

**Answer:** \(\displaystyle \frac{6}{5}\). The imaginary parts cancel, leaving a real number.

**Why this makes sense:** The expression \(\frac{z}{\overline{z}} + \frac{\overline{z}}{z}\) is always real for any non-zero complex number \(z\), because the two terms are conjugates of each other and their sum is twice the real part.

---

## Practice Problems

**Problem 1:** For \(z = -3 + 4i\), find the conjugate \(\overline{z}\) and the modulus \(|z|\).

**Problem 2:** Let \(z = 1 + 2i\) and \(w = 3 - i\). Compute \(\overline{z + w}\) and then verify that it equals \(\overline{z} + \overline{w}\).

**Problem 3:** Divide and simplify: \(\displaystyle \frac{2 + i}{3 - 2i}\). Give your answer in the form \(a + bi\).

**Problem 4:** Evaluate \(\displaystyle \frac{1 + i}{1 - i}\). What do you notice about the result? Explain why this happens.

**Problem 5 (IB Exam Style):** Let \(z = \dfrac{2 + i}{1 - i}\).
(a) Express \(z\) in Cartesian form \(a + bi\). [3 marks]
(b) Hence find the modulus \(|z|\). [2 marks]
(c) Verify your answer for \(|z|\) by using the property \(\left|\dfrac{z_1}{z_2}\right| = \dfrac{|z_1|}{|z_2|}\). [1 mark]

**Problem 6:** Simplify \(\displaystyle \frac{3}{1 + i\sqrt{3}}\) and express your answer in Cartesian form.

---

## Answers

**Answer 1:** The conjugate of \(z = -3 + 4i\) is \(\overline{z} = -3 - 4i\). Only the sign of the imaginary part flips; the real part stays at \(-3\).

The modulus is \(|z| = \sqrt{(-3)^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5\).

**Pitfall:** When squaring \(-3\), remember that \((-3)^2 = 9\) (positive), not \(-9\). The square of any real number is non-negative.

**Answer 2:** First, \(z + w = (1 + 2i) + (3 - i) = 4 + i\). So \(\overline{z + w} = 4 - i\).

Now compute \(\overline{z} = 1 - 2i\) and \(\overline{w} = 3 + i\). Their sum is \((1 - 2i) + (3 + i) = 4 - i\).

Both methods give \(4 - i\), confirming the property \(\overline{z + w} = \overline{z} + \overline{w}\).

**Answer 3:** Multiply numerator and denominator by the conjugate of \(3 - 2i\), which is \(3 + 2i\):

\[
\frac{2 + i}{3 - 2i} \cdot \frac{3 + 2i}{3 + 2i} = \frac{(2 + i)(3 + 2i)}{3^2 + 2^2} = \frac{(2 + i)(3 + 2i)}{9 + 4} = \frac{(2 + i)(3 + 2i)}{13}
\]

Expand the numerator: \(2(3) + 2(2i) + i(3) + i(2i) = 6 + 4i + 3i + 2i^2 = 6 + 7i + 2(-1) = 6 + 7i - 2 = 4 + 7i\).

So the result is \(\displaystyle \frac{4 + 7i}{13} = \frac{4}{13} + \frac{7}{13}i\).

**Answer 4:** Multiply numerator and denominator by the conjugate of \(1 - i\), which is \(1 + i\):

\[
\frac{1 + i}{1 - i} \cdot \frac{1 + i}{1 + i} = \frac{(1 + i)^2}{1^2 + 1^2} = \frac{(1 + i)^2}{2}
\]

Now \((1 + i)^2 = 1 + 2i + i^2 = 1 + 2i - 1 = 2i\).

So \(\displaystyle \frac{2i}{2} = i\).

The result is \(i\), which is the imaginary unit itself. This happens because \(\frac{1 + i}{1 - i} = i\) is a special ratio. More generally, for any non-zero complex number \(z\), the ratio \(\frac{z}{\overline{z}}\) always has modulus 1 — it lies on the unit circle (a concept you will explore in later lessons).

**Answer 5:**

(a) First compute \(z = \frac{2 + i}{1 - i}\). Multiply by the conjugate \(1 + i\):

\[
z = \frac{(2 + i)(1 + i)}{(1 - i)(1 + i)} = \frac{(2 + i)(1 + i)}{1^2 + 1^2} = \frac{(2 + i)(1 + i)}{2}
\]

Expand the numerator: \(2(1) + 2(i) + i(1) + i(i) = 2 + 2i + i + i^2 = 2 + 3i - 1 = 1 + 3i\).

So \(z = \frac{1 + 3i}{2} = \frac{1}{2} + \frac{3}{2}i\).

(b) The modulus is \(|z| = \sqrt{\left(\frac{1}{2}\right)^2 + \left(\frac{3}{2}\right)^2} = \sqrt{\frac{1}{4} + \frac{9}{4}} = \sqrt{\frac{10}{4}} = \frac{\sqrt{10}}{2}\).

(c) Check using the property: \(\left|\frac{2 + i}{1 - i}\right| = \frac{|2 + i|}{|1 - i|} = \frac{\sqrt{2^2 + 1^2}}{\sqrt{1^2 + (-1)^2}} = \frac{\sqrt{5}}{\sqrt{2}} = \sqrt{\frac{5}{2}}\).

And \(\sqrt{\frac{5}{2}} = \frac{\sqrt{10}}{2}\), matching the result from part (b). The property holds.

**Pitfall:** When squaring fractions, square both the numerator and denominator: \(\left(\frac{1}{2}\right)^2 = \frac{1}{4}\), not \(\frac{1}{2}\).

**Answer 6:** Multiply numerator and denominator by the conjugate of \(1 + i\sqrt{3}\), which is \(1 - i\sqrt{3}\):

\[
\frac{3}{1 + i\sqrt{3}} \cdot \frac{1 - i\sqrt{3}}{1 - i\sqrt{3}} = \frac{3(1 - i\sqrt{3})}{1^2 + (\sqrt{3})^2} = \frac{3(1 - i\sqrt{3})}{1 + 3} = \frac{3(1 - i\sqrt{3})}{4}
\]

Distribute the 3: \(\displaystyle \frac{3 - 3i\sqrt{3}}{4} = \frac{3}{4} - \frac{3\sqrt{3}}{4}i\).
