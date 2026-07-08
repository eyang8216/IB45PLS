# Lesson 19: Complex Numbers — Cartesian Form and Basic Operations

## WHAT Are Complex Numbers?

You already know how to solve equations like \(x^2 - 4 = 0\). You factor it to \((x-2)(x+2) = 0\), giving you \(x = 2\) or \(x = -2\). Both are ordinary real numbers.

Now try solving this equation:

\[
x^2 + 1 = 0
\]

Subtract 1 from both sides: \(x^2 = -1\). A number squared is negative one? That is impossible with the numbers you have used so far. The square of any real number is always zero or positive. For example, \(3^2 = 9\), \((-3)^2 = 9\), and \(0^2 = 0\). None of these equal \(-1\).

So mathematicians invented a new number. They called it the **imaginary unit**, written as \(i\), and defined it by one simple rule:

\[
\boxed{i^2 = -1}
\]

The letter \(i\) is not a variable you solve for. It is a constant — a new kind of number that lives outside the real number line. With \(i\) in your toolkit, you can now solve every quadratic equation, not just the ones that happen to have real answers.

A **complex number** is any number you can write as \(a + bi\), where \(a\) and \(b\) are ordinary real numbers. The set of all complex numbers is called \(\mathbb{C}\).

## WHY Do Complex Numbers Matter?

Complex numbers are not just an abstract curiosity. They are used every day by electrical engineers to analyze alternating current circuits. They appear in quantum mechanics, where the fundamental equation of physics (the Schrödinger equation) has \(i\) built into it. They are used in signal processing, control systems, and fluid dynamics. Understanding complex numbers opens the door to a huge range of advanced mathematics and real-world applications.

---

## 1. Cartesian Form

The **Cartesian form** (also called rectangular form) of a complex number is simply writing it as \(a + bi\). For example, \(3 + 4i\) and \(-2 - i\) are both complex numbers in Cartesian form.

When you look at \(a + bi\):

- \(a\) is called the **real part**, written as \(\operatorname{Re}(z)\). It is the number sitting by itself.
- \(b\) is called the **imaginary part**, written as \(\operatorname{Im}(z)\). It is just the coefficient in front of \(i\). The imaginary part is \(b\) itself, not \(bi\).

**Common misconception:** Many students think the imaginary part of \(3 + 4i\) is \(4i\). It is not — the imaginary part is just \(4\). The \(i\) is the imaginary unit, and the imaginary part is the real number that multiplies it.

Here are some examples to make this clear:

- For \(z = 3 + 4i\): the real part is \(3\) and the imaginary part is \(4\).
- For \(z = -2 - i\): the real part is \(-2\) and the imaginary part is \(-1\) (because \(-i\) means \(-1 \cdot i\)).
- For \(z = 7\): the real part is \(7\) and the imaginary part is \(0\). A real number is a special case of a complex number — one where the imaginary part happens to be zero.
- For \(z = 5i\): the real part is \(0\) and the imaginary part is \(5\). This is called a **purely imaginary** number.

---

## 2. Equality of Complex Numbers

Two complex numbers are equal exactly when both their real parts match and their imaginary parts match. In symbols:

\[
\boxed{a + bi = c + di \quad\text{means}\quad a = c \;\text{and}\; b = d}
\]

This rule is very useful. Whenever a problem tells you that two complex numbers are equal, you can split it into two separate real-number equations.

### Worked Example: Finding Unknown Values from Equality

**Problem:** Find the real numbers \(x\) and \(y\) such that \((x + y) + (x - y)i = 5 + i\).

**Approach:** Since the two complex numbers are equal, their real parts must be equal and their imaginary parts must be equal. Write two equations and solve them as a system.

**Step 1 — Equate real parts:**
The real part on the left is \(x + y\). The real part on the right is \(5\).
\[
x + y = 5
\]

**Step 2 — Equate imaginary parts:**
The imaginary part on the left is \(x - y\). The imaginary part on the right is \(1\).
\[
x - y = 1
\]

**Step 3 — Solve the system:**
Add the two equations: \((x + y) + (x - y) = 5 + 1\), which gives \(2x = 6\), so \(x = 3\).
Substitute back: \(3 + y = 5\), so \(y = 2\).

**Answer:** \(x = 3\), \(y = 2\).

**Why this makes sense:** Check by plugging back: \((3 + 2) + (3 - 2)i = 5 + 1i = 5 + i\). It matches perfectly.

---

## 3. Adding and Subtracting Complex Numbers

Adding and subtracting complex numbers is simple: you treat the real parts and imaginary parts separately, just like you treat "like terms" when combining algebraic expressions.

\[
\boxed{(a + bi) + (c + di) = (a + c) + (b + d)i}
\]
\[
\boxed{(a + bi) - (c + di) = (a - c) + (b - d)i}
\]

### Worked Example 1 — Addition

**Problem:** Simplify \((3 + 2i) + (5 - 4i)\).

**Approach:** Group the real numbers together and the \(i\)-terms together.

**Step 1:** Real parts: \(3 + 5 = 8\).
**Step 2:** Imaginary parts: \(2 + (-4) = -2\).
**Step 3:** Put them together: \(8 - 2i\).

**Answer:** \(8 - 2i\).

### Worked Example 2 — Subtraction

**Problem:** Simplify \((6 + i) - (2 - 3i)\).

**Approach:** Be careful with the minus sign — it applies to both parts of the second number. Think of it as \((6 + i) + (-2 + 3i)\).

**Step 1:** Real parts: \(6 - 2 = 4\).
**Step 2:** Imaginary parts: \(1 - (-3)\). Subtracting negative three is the same as adding three: \(1 + 3 = 4\).
**Step 3:** Put them together: \(4 + 4i\).

**Answer:** \(4 + 4i\).

**Common misconception:** Many students subtract only the real part and forget to distribute the minus sign to the imaginary part. Always write the subtraction as adding the negative: \(a + bi - (c + di) = a + bi - c - di\).

---

## 4. Multiplying Complex Numbers

To multiply two complex numbers, expand them exactly like you expand two binomials — use the distributive property (often called FOIL: First, Outer, Inner, Last). Then, wherever you see \(i^2\), replace it with \(-1\).

\[
\boxed{(a + bi)(c + di) = ac + adi + bci + bdi^2 = (ac - bd) + (ad + bc)i}
\]

You do not need to memorize that formula. Just expand and simplify \(i^2 = -1\).

### Worked Example 1 — Basic Multiplication

**Problem:** Multiply \((2 + 3i)(1 - 4i)\).

**Approach:** Expand step by step using the distributive property, then replace \(i^2\) with \(-1\) and combine like terms.

**Step 1 — Expand:**
Multiply \(2\) by \(1\): \(2\)
Multiply \(2\) by \(-4i\): \(-8i\)
Multiply \(3i\) by \(1\): \(+3i\)
Multiply \(3i\) by \(-4i\): \(-12i^2\)

So we have: \(2 - 8i + 3i - 12i^2\)

**Step 2 — Combine the \(i\)-terms:** \(-8i + 3i = -5i\). We now have \(2 - 5i - 12i^2\).

**Step 3 — Replace \(i^2\) with \(-1\):** \(-12i^2 = -12(-1) = +12\).

**Step 4 — Add the real numbers:** \(2 + 12 = 14\).

**Answer:** \(14 - 5i\).

### Worked Example 2 — Squaring a Complex Number

**Problem:** Evaluate \((1 + i)^2\).

**Approach:** Squaring means multiplying the number by itself. Expand and simplify.

**Step 1 — Expand:**
\((1 + i)(1 + i) = 1 + i + i + i^2 = 1 + 2i + i^2\)

**Step 2 — Replace \(i^2\) with \(-1\):** \(1 + 2i + (-1) = 1 + 2i - 1\).

**Step 3 — Simplify:** The \(1\) and \(-1\) cancel, leaving \(2i\).

**Answer:** \(2i\).

**Why this makes sense:** \(1 + i\) squared gives \(2i\), which is purely imaginary. This may feel surprising, but it follows directly from \(i^2 = -1\).

### Worked Example 3 — The Conjugate Product

**Problem:** Multiply \((3 - i)(3 + i)\).

**Approach:** Expand as usual. Notice that these two numbers have the same real part and opposite imaginary parts — they are **conjugates** of each other (you will study conjugates in depth in Lesson 20).

**Step 1 — Expand:**
\((3 - i)(3 + i) = 9 + 3i - 3i - i^2\).

**Step 2 — The middle terms cancel:** \(3i - 3i = 0\).

**Step 3 — Replace \(i^2\):** \(-i^2 = -(-1) = +1\).

**Step 4 — Add:** \(9 + 1 = 10\).

**Answer:** \(10\), which is a real number. Multiplying a complex number by its conjugate always gives a real number — this fact becomes extremely useful when you divide complex numbers.

---

## 5. Powers of \(i\)

The powers of \(i\) follow a repeating cycle of length 4. Once you know the first four powers, you can find any power of \(i\).

Let us compute them one at a time:

\[
\begin{aligned}
i^1 &= i \\[4pt]
i^2 &= -1 \\[4pt]
i^3 &= i^2 \cdot i = (-1) \cdot i = -i \\[4pt]
i^4 &= i^2 \cdot i^2 = (-1) \cdot (-1) = 1
\end{aligned}
\]

Now what about \(i^5\)? Since \(i^4 = 1\), we have \(i^5 = i^4 \cdot i = 1 \cdot i = i\). The cycle starts over.

The pattern is: \(i, -1, -i, 1, i, -1, -i, 1, \dots\)

**Key rule:** To find \(i^n\), divide the exponent \(n\) by 4 and look at the remainder.
- If the remainder is 0, \(i^n = 1\).
- If the remainder is 1, \(i^n = i\).
- If the remainder is 2, \(i^n = -1\).
- If the remainder is 3, \(i^n = -i\).

### Worked Example: A Large Power of \(i\)

**Problem:** Evaluate \(i^{2023}\).

**Approach:** Divide 2023 by 4 to find the remainder. The remainder determines which value in the cycle we land on.

**Step 1:** Divide: \(2023 \div 4\). Since \(4 \times 505 = 2020\), the remainder is \(2023 - 2020 = 3\).

**Step 2:** A remainder of 3 means \(i^{2023} = i^3 = -i\).

**Answer:** \(-i\).

**Common misconception:** Some students think \(i^0 = 0\). But any number (except 0 itself) raised to the power 0 is 1. So \(i^0 = 1\), which matches the remainder-0 case.

---

## Practice Problems

**Problem 1:** For the complex number \(z = -4 + 7i\), state the real part \(\operatorname{Re}(z)\) and the imaginary part \(\operatorname{Im}(z)\).

**Problem 2:** Simplify \((5 - 2i) + (-3 + 6i) - (4 + i)\). Give your answer in Cartesian form \(a + bi\).

**Problem 3:** Multiply \((2 + i)(3 - 5i)\) and express your answer in the form \(a + bi\).

**Problem 4:** Evaluate \((2 - i)^2\) and give your answer in Cartesian form \(a + bi\).

**Problem 5 (IB Exam Style):** The complex numbers \(z\) and \(w\) are given by \(z = 3 + 2i\) and \(w = 1 - 4i\).
(a) Find \(z + w\) and \(z - w\), giving each answer in the form \(a + bi\). [2 marks]
(b) Find \(zw\), giving your answer in the form \(a + bi\). [2 marks]
(c) Verify that \(\operatorname{Re}(zw)\) equals \(\operatorname{Re}(z)\operatorname{Re}(w) - \operatorname{Im}(z)\operatorname{Im}(w)\). [2 marks]

**Problem 6:** Evaluate \(i^{50} + i^{51} + i^{52} + i^{53}\).

**Problem 7:** Simplify \((1 + i)(1 - i)(2 + 3i)\) and express your answer in the form \(a + bi\).

---

## Answers

**Answer 1:** The complex number \(z = -4 + 7i\) is in Cartesian form \(a + bi\) with \(a = -4\) and \(b = 7\). Therefore \(\operatorname{Re}(z) = -4\) and \(\operatorname{Im}(z) = 7\). Remember: the imaginary part is the coefficient 7, not \(7i\).

**Answer 2:** We group the real parts and imaginary parts separately, being careful to distribute the minus sign in the subtraction.

Real parts: \(5 + (-3) - 4 = 5 - 3 - 4 = -2\).

Imaginary parts: \(-2 + 6 - 1 = 3\).

So the result is \(-2 + 3i\).

**Answer 3:** Expand \((2 + i)(3 - 5i)\) using the distributive property:

\(2 \cdot 3 = 6\)
\(2 \cdot (-5i) = -10i\)
\(i \cdot 3 = 3i\)
\(i \cdot (-5i) = -5i^2\)

Combine: \(6 - 10i + 3i - 5i^2 = 6 - 7i - 5i^2\).

Replace \(i^2\) with \(-1\): \(-5(-1) = +5\).

So we have \(6 - 7i + 5 = 11 - 7i\).

**Answer 4:** \((2 - i)^2\) means \((2 - i)(2 - i)\). Expand:

\(2 \cdot 2 = 4\)
\(2 \cdot (-i) = -2i\)
\((-i) \cdot 2 = -2i\)
\((-i) \cdot (-i) = i^2\)

Combine: \(4 - 2i - 2i + i^2 = 4 - 4i + i^2\).

Replace \(i^2\) with \(-1\): \(4 - 4i - 1 = 3 - 4i\).

**Answer 5:**

(a) \(z + w = (3 + 2i) + (1 - 4i) = (3 + 1) + (2 - 4)i = 4 - 2i\).

\(z - w = (3 + 2i) - (1 - 4i) = (3 - 1) + (2 - (-4))i = 2 + 6i\).

(b) \(zw = (3 + 2i)(1 - 4i) = 3(1) + 3(-4i) + 2i(1) + 2i(-4i) = 3 - 12i + 2i - 8i^2\).

Combine: \(3 - 10i - 8i^2\). Replace \(i^2 = -1\): \(-8(-1) = 8\). So \(3 - 10i + 8 = 11 - 10i\).

(c) Left-hand side: \(\operatorname{Re}(zw) = \operatorname{Re}(11 - 10i) = 11\).

Right-hand side: \(\operatorname{Re}(z)\operatorname{Re}(w) - \operatorname{Im}(z)\operatorname{Im}(w) = (3)(1) - (2)(-4) = 3 - (-8) = 3 + 8 = 11\).

Both sides equal 11, so the verification is successful. This formula is actually the general pattern for the real part of a product of two complex numbers.

**Pitfall:** In part (b), many students forget that the imaginary part of \(w\) is \(-4\) (not \(4\)). Keep the sign with the number.

**Answer 6:** Find each power by dividing the exponent by 4 and checking the remainder.

- \(50 \div 4 = 12\) remainder \(2\), so \(i^{50} = i^2 = -1\).
- \(51 \div 4 = 12\) remainder \(3\), so \(i^{51} = i^3 = -i\).
- \(52 \div 4 = 13\) remainder \(0\), so \(i^{52} = i^0 = 1\).
- \(53 \div 4 = 13\) remainder \(1\), so \(i^{53} = i^1 = i\).

Now add them: \((-1) + (-i) + 1 + i\).

The \(-1\) and \(1\) cancel to \(0\). The \(-i\) and \(i\) cancel to \(0\). The total sum is \(0\).

**Why this makes sense:** Adding four consecutive powers of \(i\) always gives zero because the cycle \(i, -1, -i, 1\) sums to zero. This is a useful shortcut to remember.

**Answer 7:** First multiply \((1 + i)(1 - i)\). These are conjugates, so their product is real:

\((1 + i)(1 - i) = 1 - i + i - i^2 = 1 - i^2 = 1 - (-1) = 2\).

Now multiply this result by \((2 + 3i)\): \(2(2 + 3i) = 4 + 6i\).

The final answer is \(4 + 6i\).
