# Lesson 21: Complex Numbers (SAT Level — Quick Review)

## What You'll Learn
- The imaginary unit $i = \sqrt{-1}$ and the cycle of powers: $i$, $i^2 = -1$, $i^3 = -i$, $i^4 = 1$
- Addition and subtraction of complex numbers: combine real parts and imaginary parts
- Multiplication: use FOIL, then replace $i^2$ with $-1$
- The complex conjugate and how to use it for division
- What is (and is NOT) on the SAT for complex numbers
- The most common SAT trap: forgetting $i^2 = -1$ midway through multiplication

## SAT Context
Complex numbers appear in **1–3 questions** on the SAT, typically in the Advanced Math domain. This is one of the most limited topics — the SAT tests only basic arithmetic with complex numbers in the form $a+bi$. There is **no polar form, no De Moivre's theorem, no Argand diagrams, no complex roots of unity, no Euler's formula** — all of those are IB AAHL territory. If you've completed AAHL, you've gone far beyond what the SAT requires. The SAT's complex number questions are quick arithmetic checks: can you add $(3+2i)+(1-5i)$, multiply $(2+i)(3-4i)$, or simplify $\frac{1}{1+i}$? Treat this as a rapid review — you already know everything conceptually, and this lesson is about avoiding careless errors.

---

## What is $i$?

$$i = \sqrt{-1}$$
$$i^2 = -1$$

$i$ is **not** a real number. Complex numbers have the form $a + bi$, where $a$ and $b$ are real numbers.

| Term | Meaning | Example |
|:---|:---|:---|
| Real part | $a$ in $a+bi$ | In $3-2i$, real part is $3$ |
| Imaginary part | $b$ in $a+bi$ (the coefficient, not including $i$) | In $3-2i$, imaginary part is $-2$ |
| Pure real | $b = 0$ | $5 = 5 + 0i$ |
| Pure imaginary | $a = 0$ | $4i = 0 + 4i$ |

---

## The Cycle of Powers of $i$

Powers of $i$ repeat in a 4-cycle:

$$i^1 = i$$
$$i^2 = -1$$
$$i^3 = i^2 \cdot i = -1 \cdot i = -i$$
$$i^4 = i^3 \cdot i = -i \cdot i = -i^2 = -(-1) = 1$$
$$i^5 = i^4 \cdot i = 1 \cdot i = i \quad \text{(pattern repeats)}$$

> **🔍 PATTERN RECOGNITION:** To simplify $i^n$ for large $n$, divide $n$ by 4 and use the remainder:
> - Remainder 0: $i^n = 1$
> - Remainder 1: $i^n = i$
> - Remainder 2: $i^n = -1$
> - Remainder 3: $i^n = -i$

### Worked Example 1: Powers of $i$

**Problem:** Simplify $i^{27}$.

**Solution:** $27 \div 4 = 6$ with remainder $3$. So $i^{27} = i^3 = -i$.

---

## Addition and Subtraction

Combine real parts with real parts, and imaginary parts with imaginary parts:

$$(a + bi) + (c + di) = (a + c) + (b + d)i$$
$$(a + bi) - (c + di) = (a - c) + (b - d)i$$

### Worked Example 2: Addition

**Problem:** Simplify $(5 + 3i) + (2 - 7i)$.

**Solution:** Real: $5 + 2 = 7$. Imaginary: $3i + (-7i) = -4i$. **Answer:** $7 - 4i$.

---

## Multiplication

Use FOIL (First, Outer, Inner, Last), then replace $i^2$ with $-1$:

$$(a + bi)(c + di) = ac + adi + bci + bdi^2$$
$$= ac + (ad + bc)i + bd(-1)$$
$$= (ac - bd) + (ad + bc)i$$

> **🚨 SAT TRAP ALERT:** The most common error in complex multiplication is **forgetting that $i^2 = -1$.** Students FOIL correctly but leave the $i^2$ term as-is (with a plus sign). Example: $(2+i)(3+2i) = 6 + 4i + 3i + 2i^2$. If you leave this as $6 + 7i + 2i^2$, that's wrong. You must replace $i^2$ with $-1$: $6 + 7i + 2(-1) = 6 + 7i - 2 = 4 + 7i$.

### Worked Example 3: Multiplication

**Problem:** Simplify $(3 + 2i)(1 - 4i)$.

**Solution:**
$$(3)(1) + (3)(-4i) + (2i)(1) + (2i)(-4i)$$
$$= 3 - 12i + 2i - 8i^2$$
$$= 3 - 10i - 8(-1)$$
$$= 3 - 10i + 8$$
$$= 11 - 10i$$

**Common wrong answer:** $3 - 10i - 8i^2$ (forgetting to replace $i^2$ with $-1$).

---

## Complex Conjugate

The **complex conjugate** of $a + bi$ is $a - bi$ (flip the sign of the imaginary part).

**Key property:** The product of a complex number and its conjugate is always a **real** number:

$$(a + bi)(a - bi) = a^2 - (bi)^2 = a^2 - b^2i^2 = a^2 - b^2(-1) = a^2 + b^2$$

> **🔍 PATTERN RECOGNITION:** $(a+bi)(a-bi) = a^2 + b^2$. Always real, always positive (unless both $a$ and $b$ are 0). The SAT often asks: "What is the product of $2+3i$ and its conjugate?" Answer: $2^2 + 3^2 = 4 + 9 = 13$.

### Worked Example 4: Conjugate Product

**Problem:** What is $(4 - 5i)(4 + 5i)$?

**Solution:** This is a number multiplied by its conjugate. The result is $4^2 + 5^2 = 16 + 25 = 41$.

---

## Division with Complex Numbers

To divide by a complex number, multiply numerator and denominator by the **conjugate** of the denominator:

$$\frac{a+bi}{c+di} = \frac{a+bi}{c+di} \cdot \frac{c-di}{c-di}$$

The denominator becomes real: $(c+di)(c-di) = c^2 + d^2$.

### Worked Example 5: Division

**Problem:** Simplify $\frac{5}{2+i}$ into the form $a+bi$.

**Solution:**
$$\frac{5}{2+i} \cdot \frac{2-i}{2-i} = \frac{5(2-i)}{(2+i)(2-i)} = \frac{10 - 5i}{4 + 1} = \frac{10 - 5i}{5} = 2 - i$$

---

## SAT vs. AAHL: What's NOT Tested

The SAT does NOT test:
- $\text{Arg}(z)$ or $\arg(z)$ — argument of a complex number
- $|z|$ — modulus (though you can compute $\sqrt{a^2+b^2}$ implicitly via conjugate)
- Polar form: $r(\cos\theta + i\sin\theta)$
- De Moivre's theorem: $(\cos\theta + i\sin\theta)^n = \cos(n\theta) + i\sin(n\theta)$
- Euler's formula: $e^{i\theta} = \cos\theta + i\sin\theta$
- Roots of unity
- Loci in the complex plane (circles, perpendicular bisectors, etc.)
- Complex polynomials beyond basic factoring

> **🚨 SAT TRAP ALERT:** If you find yourself drawing an Argand diagram or using polar coordinates, STOP. You have left the SAT's scope. The SAT complex number questions can all be solved with the four basic operations and the conjugate.

---

## Solving Equations with $i$

Occasionally, the SAT asks you to solve an equation where the variable is a complex number.

### Worked Example 6: Solving for Complex Numbers

**Problem:** If $(x + yi) + (3 - 2i) = 7 + 4i$, find $x$ and $y$ (where $x$ and $y$ are real).

**Solution:**
$$(x + 3) + (y - 2)i = 7 + 4i$$

For two complex numbers to be equal, their real parts must be equal AND their imaginary parts must be equal:
$$x + 3 = 7 \implies x = 4$$
$$y - 2 = 4 \implies y = 6$$

**Answer:** $x = 4$, $y = 6$, so the number is $4 + 6i$.

---

## Practice Problems

### Problem 1
Simplify $(7 - 2i) - (3 + 5i)$.

(A) $4 + 3i$  
(B) $4 - 7i$  
(C) $10 + 3i$  
(D) $10 - 7i$

### Problem 2
Simplify $(2 + i)(3 - 2i)$.

(A) $8 - i$  
(B) $4 - i$  
(C) $8 + i$  
(D) $6 - i$

### Problem 3
What is $i^{42}$?

(A) $i$  
(B) $-1$  
(C) $-i$  
(D) $1$

### Problem 4
If $a$ and $b$ are real numbers and $(a + bi)(2 - i) = 7 - i$, what is the value of $a + b$?

(A) 2  
(B) 3  
(C) 4  
(D) 5

### Problem 5
Simplify $\frac{3 + i}{1 - i}$ into the form $a + bi$.

(A) $2 + i$  
(B) $1 + 2i$  
(C) $2 - i$  
(D) $1 - 2i$

---

## Answers

### Problem 1 — Answer: (B) $4 - 7i$

$$(7 - 2i) - (3 + 5i) = 7 - 2i - 3 - 5i = (7-3) + (-2-5)i = 4 - 7i$$

**Wrong-answer analysis:**
- (A) $4 + 3i$ — added the imaginary parts instead of subtracting: $-2i - 5i$ computed as $+3i$
- (C) $10 + 3i$ — added both instead of subtracting
- (D) $10 - 7i$ — added real parts ($7+3$) but correctly subtracted imaginary

---

### Problem 2 — Answer: (A) $8 - i$

$$(2+i)(3-2i) = 6 - 4i + 3i - 2i^2 = 6 - i - 2(-1) = 6 - i + 2 = 8 - i$$

**Wrong-answer analysis:**
- (B) $4 - i$ — forgot to change the sign on $i^2$: $6 - i + 2i^2$ left as $6 - i - 2 = 4 - i$ (but actually used $i^2 = +1$)
- (C) $8 + i$ — sign error on the $i$ term
- (D) $6 - i$ — forgot the $i^2$ term entirely

---

### Problem 3 — Answer: (B) $-1$

$42 \div 4 = 10$ with remainder $2$. $i^{42} = i^2 = -1$.

**Wrong-answer analysis:**
- (A) $i$ — confused remainder 2 with remainder 1
- (C) $-i$ — remainder 3
- (D) $1$ — remainder 0 (divided evenly, which it doesn't: $42/4 = 10.5$)

---

### Problem 4 — Answer: (C) 4

Let $(a+bi)(2-i) = 7-i$. Expand:
$$(a+bi)(2-i) = 2a - ai + 2bi - bi^2 = 2a + (-a+2b)i + b = (2a+b) + (-a+2b)i$$

Set equal to $7 - i$:
$$2a + b = 7$$
$$-a + 2b = -1$$

Solve the system. From the second: $a = 2b + 1$. Substitute into the first: $2(2b+1) + b = 7$ → $4b + 2 + b = 7$ → $5b = 5$ → $b = 1$. Then $a = 2(1) + 1 = 3$. So $a + b = 4$.

**Wrong-answer analysis:**
- (A) 2 — various arithmetic errors
- (B) 3 — might have found only $a$ or only $b$
- (D) 5 — might have added incorrectly at the end

---

### Problem 5 — Answer: (B) $1 + 2i$

$$\frac{3+i}{1-i} \cdot \frac{1+i}{1+i} = \frac{(3+i)(1+i)}{(1-i)(1+i)} = \frac{3 + 3i + i + i^2}{1 + 1} = \frac{3 + 4i - 1}{2} = \frac{2 + 4i}{2} = 1 + 2i$$

**Wrong-answer analysis:**
- (A) $2 + i$ — forgot to divide by 2 at the end, or multiplied by wrong conjugate
- (C) $2 - i$ — sign errors in the imaginary part
- (D) $1 - 2i$ — sign error: used $(3+i)(1+i)$ but made an error in the $i^2$ sign

---

## Key Takeaways

1. $i^2 = -1$ is the only fact you need to remember. Everything else follows.
2. Powers of $i$ cycle: $i$, $-1$, $-i$, $1$ (repeat). Divide the exponent by 4.
3. Multiplication: FOIL, then replace $i^2$ with $-1$. Don't forget this step!
4. The conjugate of $a+bi$ is $a-bi$. Their product is always the real number $a^2 + b^2$.
5. For division, multiply numerator and denominator by the conjugate of the denominator.
6. The SAT tests only arithmetic with $a+bi$ — no polar form, no De Moivre, no advanced topics.
