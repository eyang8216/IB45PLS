# Lesson 23: De Moivre's Theorem and Powers of Complex Numbers

## What Is De Moivre's Theorem?

### The "What"

De Moivre's theorem is a rule for raising a complex number to any integer power. If a complex number is written in polar form with modulus $r$ and argument $\theta$, then the $n$th power of that number has modulus $r^n$ and argument $n\theta$.

The theorem is named after Abraham de Moivre (1667–1754), a French mathematician who spent most of his career in England. In its most common form, the theorem states:

$$(\cos\theta + i\sin\theta)^n = \cos(n\theta) + i\sin(n\theta)$$

This holds for any integer $n$: positive, negative, or zero.

In exponential form, the same idea is even more transparent:

$$(re^{i\theta})^n = r^n e^{in\theta}$$

### The "Why" — Avoiding Enormous Expansions

Without De Moivre's theorem, computing something like $(1 + i)^8$ would require expanding $(1 + i)^8$ using the binomial theorem, which produces nine terms involving powers of $i$, which then must be simplified using $i^2 = -1$, $i^3 = -i$, $i^4 = 1$, and so on. That is tedious and error-prone.

With De Moivre's theorem, the computation reduces to three simple steps: convert to polar form, apply the power to the modulus and argument, and convert back if needed.

---

## 1. The Theorem in Detail

Let $z = r(\cos\theta + i\sin\theta) = re^{i\theta}$. For any integer $n$:

$$z^n = r^n \bigl(\cos(n\theta) + i\sin(n\theta)\bigr) = r^n e^{in\theta}$$

**The modulus gets raised to the power $n$.** For example, if $r = 2$ and $n = 3$, the new modulus is $2^3 = 8$.

**The argument gets multiplied by $n$.** For example, if $\theta = \frac{\pi}{4}$ and $n = 3$, the new argument is $\frac{3\pi}{4}$.

After computing $n\theta$, you may need to adjust the argument to keep it in the principal range $(-\pi, \pi]$. You do this by adding or subtracting multiples of $2\pi$.

**A common misconception:** Some students think De Moivre's theorem works for any exponent, including fractions like $\frac{1}{2}$ (square roots). It does not work directly for non-integer exponents without careful handling. Fractional exponents produce multiple values — those are the roots of complex numbers, which are treated in a separate lesson.

---

## Worked Example 1: A Simple Power

**Problem:** Compute $(1 + i)^8$ and give the answer in Cartesian form.

**Approach:** We could expand $(1 + i)^8$ using the binomial theorem, but that would be very long. Instead, we convert $1 + i$ to polar form, apply De Moivre's theorem with $n = 8$, and then convert back to Cartesian form.

**Step 1 — Convert $1 + i$ to polar form:**
$$|1 + i| = \sqrt{1^2 + 1^2} = \sqrt{2}$$
$$\arg(1 + i) = \arctan\left(\frac{1}{1}\right) = \frac{\pi}{4}$$

So $1 + i = \sqrt{2}\left(\cos\frac{\pi}{4} + i\sin\frac{\pi}{4}\right) = \sqrt{2}\,e^{i\pi/4}$.

**Step 2 — Apply De Moivre with $n = 8$:**
$$(1 + i)^8 = (\sqrt{2})^8 \left(\cos\left(8 \cdot \frac{\pi}{4}\right) + i\sin\left(8 \cdot \frac{\pi}{4}\right)\right)$$

Compute the modulus: $(\sqrt{2})^8 = (2^{1/2})^8 = 2^4 = 16$.

Compute the argument: $8 \cdot \frac{\pi}{4} = 2\pi$.

**Step 3 — Evaluate the trigonometric functions:**
$$\cos(2\pi) = 1,\quad \sin(2\pi) = 0$$

So $(1 + i)^8 = 16(1 + 0i) = 16$.

**Answer:** $16$

**Why this makes sense:** The answer is a positive real number with no imaginary part. The argument $2\pi$ means the result lands on the positive real axis. The modulus $16$ is large because we raised the original modulus $\sqrt{2} \approx 1.414$ to the 8th power.

---

## Worked Example 2: Argument Adjustment Required

**Problem:** Compute $(\sqrt{3} - i)^6$ and give the answer in Cartesian form.

**Approach:** Convert to polar form, apply De Moivre, adjust the argument to the principal range, and convert back.

**Step 1 — Find modulus and argument:**
$$|\sqrt{3} - i| = \sqrt{(\sqrt{3})^2 + (-1)^2} = \sqrt{3 + 1} = \sqrt{4} = 2$$

For the argument: $\tan\theta = \frac{-1}{\sqrt{3}}$. The reference angle is $\frac{\pi}{6}$. Since $a = \sqrt{3} > 0$ and $b = -1 < 0$, the point is in Quadrant IV, so $\theta = -\frac{\pi}{6}$.

So $\sqrt{3} - i = 2e^{-i\pi/6}$.

**Step 2 — Apply De Moivre with $n = 6$:**
$$(\sqrt{3} - i)^6 = 2^6 e^{i \cdot 6 \cdot (-\pi/6)} = 64 e^{-i\pi}$$

**Step 3 — Convert to Cartesian:**
$$64 e^{-i\pi} = 64(\cos(-\pi) + i\sin(-\pi)) = 64(-1 + 0i) = -64$$

**Answer:** $-64$

**Why this makes sense:** The argument $-\pi$ places the result on the negative real axis. The modulus $64$ equals $2^6$, as expected. The result is purely real because $\sin(-\pi) = 0$.

---

## Worked Example 3: Negative Exponent

**Problem:** Compute $(1 + i)^{-4}$.

**Approach:** De Moivre's theorem works for negative integers exactly as it does for positive ones. The only difference is that $r^n$ with a negative $n$ produces a fraction.

**Step 1 — Polar form of $1 + i$:**
$$1 + i = \sqrt{2}\,e^{i\pi/4}$$

**Step 2 — Apply De Moivre with $n = -4$:**
$$(1 + i)^{-4} = (\sqrt{2})^{-4} e^{i \cdot (-4) \cdot (\pi/4)} = (\sqrt{2})^{-4} e^{-i\pi}$$

Compute the modulus: $(\sqrt{2})^{-4} = (2^{1/2})^{-4} = 2^{-2} = \frac{1}{4}$.

**Step 3 — Convert to Cartesian:**
$$\frac{1}{4} e^{-i\pi} = \frac{1}{4}(\cos(-\pi) + i\sin(-\pi)) = \frac{1}{4}(-1 + 0i) = -\frac{1}{4}$$

**Answer:** $-\frac{1}{4}$

---

## Worked Example 4: A Fraction with Powers

**Problem:** Simplify $\displaystyle \frac{(1 + i)^6}{(\sqrt{3} + i)^4}$. Give the answer in exponential form.

**Approach:** Convert both the numerator and the denominator to exponential form, apply De Moivre to each, then use the division rule for complex numbers (divide moduli, subtract arguments).

**Step 1 — Polar form of $1 + i$:**
Modulus: $\sqrt{2}$. Argument: $\frac{\pi}{4}$. So $1 + i = \sqrt{2}\,e^{i\pi/4}$.

**Step 2 — Polar form of $\sqrt{3} + i$:**
Modulus: $|\sqrt{3} + i| = \sqrt{3 + 1} = 2$.
Argument: $\tan\theta = \frac{1}{\sqrt{3}}$, reference angle $\frac{\pi}{6}$. Since both components are positive (Quadrant I), $\theta = \frac{\pi}{6}$.
So $\sqrt{3} + i = 2e^{i\pi/6}$.

**Step 3 — Apply powers:**
$$(1 + i)^6 = (\sqrt{2})^6 e^{i \cdot 6 \cdot \pi/4} = 8 e^{i3\pi/2} = 8e^{-i\pi/2}$$

(We replaced $3\pi/2$ with $-\pi/2$ by subtracting $2\pi$, since both represent the same angle but $-\pi/2$ is in the principal range.)

$$(\sqrt{3} + i)^4 = 2^4 e^{i \cdot 4 \cdot \pi/6} = 16 e^{i2\pi/3}$$

**Step 4 — Divide:**
$$\frac{8e^{-i\pi/2}}{16e^{i2\pi/3}} = \frac{8}{16} e^{-i\pi/2 - i2\pi/3} = \frac{1}{2} e^{-i7\pi/6}$$

**Step 5 — Adjust argument to principal range:**
$-\frac{7\pi}{6} + 2\pi = \frac{5\pi}{6}$.

**Answer:** $\frac{1}{2} e^{i5\pi/6}$

---

## 2. Deriving Trigonometric Identities with De Moivre

De Moivre's theorem provides an elegant way to derive formulas for $\cos(n\theta)$ and $\sin(n\theta)$ in terms of powers of $\cos\theta$ and $\sin\theta$. The technique is:

1. Write $(\cos\theta + i\sin\theta)^n = \cos(n\theta) + i\sin(n\theta)$ (De Moivre).
2. Expand the left side using the binomial theorem.
3. Equate the real parts to get $\cos(n\theta)$.
4. Equate the imaginary parts to get $\sin(n\theta)$.

---

## Worked Example 5: Deriving $\cos(3\theta)$ and $\sin(3\theta)$

**Problem:** Use De Moivre's theorem to express $\cos(3\theta)$ in terms of $\cos\theta$ only, and $\sin(3\theta)$ in terms of $\sin\theta$ only.

**Approach:** Apply De Moivre with $n = 3$, expand the left side using the binomial theorem, then separate real and imaginary parts.

**Step 1 — Apply De Moivre:**
$$(\cos\theta + i\sin\theta)^3 = \cos(3\theta) + i\sin(3\theta)$$

**Step 2 — Expand the left side using the binomial theorem:**

The binomial theorem says $(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3$. Here $a = \cos\theta$ and $b = i\sin\theta$.

$$(\cos\theta + i\sin\theta)^3 = \cos^3\theta + 3\cos^2\theta(i\sin\theta) + 3\cos\theta(i\sin\theta)^2 + (i\sin\theta)^3$$

**Step 3 — Simplify using powers of $i$:**

We know $i^2 = -1$ and $i^3 = i^2 \cdot i = -i$.

The expansion becomes:
$$= \cos^3\theta + 3i\cos^2\theta\sin\theta + 3\cos\theta(-\sin^2\theta) + (-i\sin^3\theta)$$
$$= (\cos^3\theta - 3\cos\theta\sin^2\theta) + i(3\cos^2\theta\sin\theta - \sin^3\theta)$$

**Step 4 — Equate real and imaginary parts:**

Real part: $\cos(3\theta) = \cos^3\theta - 3\cos\theta\sin^2\theta$.

Imaginary part: $\sin(3\theta) = 3\cos^2\theta\sin\theta - \sin^3\theta$.

**Step 5 — Express in terms of a single function:**

For $\cos(3\theta)$: Replace $\sin^2\theta$ with $1 - \cos^2\theta$:
$$\cos(3\theta) = \cos^3\theta - 3\cos\theta(1 - \cos^2\theta) = \cos^3\theta - 3\cos\theta + 3\cos^3\theta = 4\cos^3\theta - 3\cos\theta$$

For $\sin(3\theta)$: Replace $\cos^2\theta$ with $1 - \sin^2\theta$:
$$\sin(3\theta) = 3(1 - \sin^2\theta)\sin\theta - \sin^3\theta = 3\sin\theta - 3\sin^3\theta - \sin^3\theta = 3\sin\theta - 4\sin^3\theta$$

**Answer:**
$$\cos(3\theta) = 4\cos^3\theta - 3\cos\theta$$
$$\sin(3\theta) = 3\sin\theta - 4\sin^3\theta$$

**Why this makes sense:** If we test with $\theta = 0$, both formulas give $\cos(0) = 1$ and $\sin(0) = 0$, which matches $\cos(0) = 1$ and $\sin(0) = 0$. If we test with $\theta = \frac{\pi}{2}$, we get $\cos(\frac{3\pi}{2}) = 0$ and $\sin(\frac{3\pi}{2}) = -1$, which is correct.

---

## 3. Key Strategy for Powers of Complex Numbers

When you need to compute a power of a complex number, follow this sequence:

1. **Convert to polar or exponential form.** Find $r = \sqrt{a^2 + b^2}$ and $\theta = \arg(z)$ with the correct quadrant.
2. **Apply De Moivre's theorem.** Raise $r$ to the power $n$. Multiply $\theta$ by $n$.
3. **Adjust the argument** to the principal range $(-\pi, \pi]$ by adding or subtracting multiples of $2\pi$.
4. **Convert back to Cartesian form** if the question asks for $a + bi$ form.

---

## Practice Problems

**Problem 1:** Evaluate $(1 - i)^6$ and give your answer in Cartesian form $a + bi$.

**Problem 2:** Compute $(-1 + i\sqrt{3})^5$ using De Moivre's theorem. Give the answer in Cartesian form.

**Problem 3:** Simplify the expression $\displaystyle \frac{(1 + i\sqrt{3})^4}{(1 - i)^3}$. Give your answer in the form $r(\cos\theta + i\sin\theta)$.

**Problem 4:** Use De Moivre's theorem with $n = 2$ to derive an expression for $\cos(2\theta)$ in terms of $\cos\theta$ only.

**Problem 5 (IB-style):** Let $z = \cos\theta + i\sin\theta$ where $\theta$ is a real number.
(a) Show that $z^n + \frac{1}{z^n} = 2\cos(n\theta)$ for any integer $n$. [3 marks]
(b) Hence, express $\cos^3\theta$ in terms of $\cos\theta$ and $\cos(3\theta)$. [3 marks]

**Problem 6:** Evaluate $\left(\frac{\sqrt{2}}{2} - i\frac{\sqrt{2}}{2}\right)^{-10}$.

---

## Answers

**Answer 1:**

The number $1 - i$ has modulus $|1 - i| = \sqrt{1^2 + (-1)^2} = \sqrt{2}$.

The argument: $\tan\theta = \frac{-1}{1} = -1$. Since $a > 0$ and $b < 0$ (Quadrant IV), $\theta = -\frac{\pi}{4}$.

So $1 - i = \sqrt{2}\,e^{-i\pi/4}$.

Apply De Moivre with $n = 6$: $(1 - i)^6 = (\sqrt{2})^6 e^{i \cdot 6 \cdot (-\pi/4)} = 8 e^{-i3\pi/2}$.

Adjust the argument: $-\frac{3\pi}{2} + 2\pi = \frac{\pi}{2}$.

So $8e^{i\pi/2} = 8(\cos\frac{\pi}{2} + i\sin\frac{\pi}{2}) = 8(0 + i) = 8i$.

**Answer:** $8i$

---

**Answer 2:**

Modulus: $|-1 + i\sqrt{3}| = \sqrt{(-1)^2 + (\sqrt{3})^2} = \sqrt{1 + 3} = 2$.

Argument: $\tan\theta = \frac{\sqrt{3}}{-1} = -\sqrt{3}$. Reference angle $\frac{\pi}{3}$. Since $a < 0$ and $b > 0$ (Quadrant II), $\theta = \pi - \frac{\pi}{3} = \frac{2\pi}{3}$.

So $-1 + i\sqrt{3} = 2e^{i2\pi/3}$.

Apply De Moivre with $n = 5$: $(-1 + i\sqrt{3})^5 = 2^5 e^{i \cdot 5 \cdot 2\pi/3} = 32 e^{i10\pi/3}$.

Adjust: $\frac{10\pi}{3} - 2\pi = \frac{10\pi}{3} - \frac{6\pi}{3} = \frac{4\pi}{3}$.

Convert to Cartesian: $32(\cos\frac{4\pi}{3} + i\sin\frac{4\pi}{3}) = 32\left(-\frac{1}{2} - i\frac{\sqrt{3}}{2}\right) = -16 - 16\sqrt{3}i$.

**Answer:** $-16 - 16\sqrt{3}i$

---

**Answer 3:**

Numerator: $1 + i\sqrt{3}$ has modulus $\sqrt{1 + 3} = 2$. Argument: $\tan\theta = \frac{\sqrt{3}}{1} = \sqrt{3}$, so $\theta = \frac{\pi}{3}$ (Quadrant I). Thus $(1 + i\sqrt{3})^4 = 2^4 e^{i \cdot 4 \cdot \pi/3} = 16e^{i4\pi/3}$.

Denominator: $1 - i$ has modulus $\sqrt{2}$. Argument: $-\frac{\pi}{4}$ (Quadrant IV). Thus $(1 - i)^3 = (\sqrt{2})^3 e^{i \cdot 3 \cdot (-\pi/4)} = 2\sqrt{2}\, e^{-i3\pi/4}$.

Division: $\frac{16e^{i4\pi/3}}{2\sqrt{2}\,e^{-i3\pi/4}} = \frac{16}{2\sqrt{2}} e^{i(4\pi/3 + 3\pi/4)}$.

Simplify the modulus: $\frac{16}{2\sqrt{2}} = \frac{8}{\sqrt{2}} = 4\sqrt{2}$.

Simplify the argument: $\frac{4\pi}{3} + \frac{3\pi}{4} = \frac{16\pi}{12} + \frac{9\pi}{12} = \frac{25\pi}{12}$.

Adjust: $\frac{25\pi}{12} - 2\pi = \frac{25\pi}{12} - \frac{24\pi}{12} = \frac{\pi}{12}$.

**Answer:** $4\sqrt{2}\left(\cos\frac{\pi}{12} + i\sin\frac{\pi}{12}\right)$

---

**Answer 4:**

De Moivre with $n = 2$: $(\cos\theta + i\sin\theta)^2 = \cos(2\theta) + i\sin(2\theta)$.

Expand the left side: $\cos^2\theta + 2i\cos\theta\sin\theta + i^2\sin^2\theta = (\cos^2\theta - \sin^2\theta) + i(2\cos\theta\sin\theta)$.

Equating real parts: $\cos(2\theta) = \cos^2\theta - \sin^2\theta$.

Replace $\sin^2\theta$ with $1 - \cos^2\theta$: $\cos(2\theta) = \cos^2\theta - (1 - \cos^2\theta) = 2\cos^2\theta - 1$.

**Answer:** $\cos(2\theta) = 2\cos^2\theta - 1$

---

**Answer 5:**

**(a)** Since $z = \cos\theta + i\sin\theta = e^{i\theta}$, we have $z^n = e^{in\theta} = \cos(n\theta) + i\sin(n\theta)$.

Also $\frac{1}{z^n} = z^{-n} = e^{-in\theta} = \cos(n\theta) - i\sin(n\theta)$.

Adding these: $z^n + \frac{1}{z^n} = [\cos(n\theta) + i\sin(n\theta)] + [\cos(n\theta) - i\sin(n\theta)] = 2\cos(n\theta)$.

**(b)** For $n = 1$: $z + \frac{1}{z} = 2\cos\theta$.

Cube both sides: $(z + \frac{1}{z})^3 = 8\cos^3\theta$.

Expand the left side: $z^3 + 3z + \frac{3}{z} + \frac{1}{z^3} = (z^3 + \frac{1}{z^3}) + 3(z + \frac{1}{z})$.

Using the result from (a): $z^3 + \frac{1}{z^3} = 2\cos(3\theta)$ and $z + \frac{1}{z} = 2\cos\theta$.

So $(z^3 + \frac{1}{z^3}) + 3(z + \frac{1}{z}) = 2\cos(3\theta) + 3(2\cos\theta) = 2\cos(3\theta) + 6\cos\theta$.

Thus $8\cos^3\theta = 2\cos(3\theta) + 6\cos\theta$, which gives $\cos^3\theta = \frac{1}{4}\cos(3\theta) + \frac{3}{4}\cos\theta$.

---

**Answer 6:**

The number $\frac{\sqrt{2}}{2} - i\frac{\sqrt{2}}{2}$ has modulus $\sqrt{\left(\frac{\sqrt{2}}{2}\right)^2 + \left(-\frac{\sqrt{2}}{2}\right)^2} = \sqrt{\frac{1}{2} + \frac{1}{2}} = \sqrt{1} = 1$.

Argument: $\tan\theta = \frac{-\sqrt{2}/2}{\sqrt{2}/2} = -1$. Since $a > 0$ and $b < 0$ (Quadrant IV), $\theta = -\frac{\pi}{4}$.

So the number is $1 \cdot e^{-i\pi/4} = e^{-i\pi/4}$.

Apply De Moivre with $n = -10$: $(e^{-i\pi/4})^{-10} = e^{i \cdot (-10) \cdot (-\pi/4)} = e^{i10\pi/4} = e^{i5\pi/2}$.

Adjust: $\frac{5\pi}{2} - 2\pi = \frac{\pi}{2}$. So the result is $e^{i\pi/2} = i$.

**Answer:** $i$
