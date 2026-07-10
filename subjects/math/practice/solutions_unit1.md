# Unit 1: Calculus Foundations — Solutions

## Problem 1
A function $f$ is defined by
$$
f(x) = \begin{cases}
\dfrac{\sin(3x)}{x}, & x \neq 0,\\[6pt]
k, & x = 0,
\end{cases}
$$
where $k$ is a real constant.

**(a) Evaluate $\displaystyle\lim_{x \to 0} f(x)$.**

**Approach:** Rewrite the limit to exploit the standard result $\displaystyle\lim_{u \to 0}\frac{\sin u}{u}=1$.

Multiply numerator and denominator by $3$:
$$
\lim_{x \to 0} \frac{\sin(3x)}{x}
= \lim_{x \to 0} 3 \cdot \frac{\sin(3x)}{3x}
= 3 \cdot \lim_{x \to 0} \frac{\sin(3x)}{3x}.
$$
As $x \to 0$, $3x \to 0$, so $\displaystyle\lim_{x \to 0}\frac{\sin(3x)}{3x} = 1$. Hence
$$
\lim_{x \to 0} f(x) = 3 \times 1 = 3.
$$

**Answer:** $\displaystyle\lim_{x \to 0} f(x) = 3$.

---

**(b) Hence determine the value of $k$ for which $f$ is continuous at $x = 0$.**

**Approach:** For continuity at $x=0$, the limit as $x \to 0$ must equal the function value $f(0)=k$.

From part (a), $\displaystyle\lim_{x \to 0} f(x) = 3$. For $f$ to be continuous at $x = 0$,
$$
f(0) = \lim_{x \to 0} f(x) \quad\Longrightarrow\quad k = 3.
$$

**Answer:** $k = 3$.

---

**(c) For the value of $k$ found in part (b), state whether $f$ is differentiable at $x = 0$. Justify your answer.**

**Approach:** Use the limit definition of the derivative at $x=0$. With $k=3$, $f(0)=3$.

The derivative from first principles:
$$
f'(0) = \lim_{h \to 0} \frac{f(h) - f(0)}{h}
= \lim_{h \to 0} \frac{\frac{\sin(3h)}{h} - 3}{h}
= \lim_{h \to 0} \frac{\sin(3h) - 3h}{h^{2}}.
$$

Substituting $h=0$ gives the indeterminate form $\frac{0}{0}$. Apply L'Hôpital's rule:
$$
f'(0) = \lim_{h \to 0} \frac{3\cos(3h) - 3}{2h}.
$$
This is still $\frac{0}{0}$. Apply L'Hôpital's rule a second time:
$$
f'(0) = \lim_{h \to 0} \frac{-9\sin(3h)}{2} = \frac{-9 \cdot 0}{2} = 0.
$$
Since the limit exists (and equals $0$), $f$ **is differentiable** at $x = 0$, with $f'(0) = 0$.

**Answer:** Yes, $f$ is differentiable at $x = 0$; $f'(0) = 0$.

*Pitfall:* Do not assume differentiability follows automatically from continuity — always check the derivative from first principles.

---

## Problem 2
Consider the limit
$$
L = \lim_{x \to 0} \frac{e^{2x} - 1 - 2x}{x^{2}}.
$$

**(a) Explain why direct substitution yields an indeterminate form, and state the type.**

**Approach:** Substitute $x = 0$ directly into numerator and denominator.

- Numerator: $e^{0} - 1 - 0 = 1 - 1 - 0 = 0$.
- Denominator: $0^{2} = 0$.

Both numerator and denominator approach $0$, so the limit is of the **indeterminate form $\frac{0}{0}$**.

**Answer:** Indeterminate form $\frac{0}{0}$.

---

**(b) Use L'Hôpital's rule to evaluate $L$.**

**Approach:** Differentiate numerator and denominator separately.

First application of L'Hôpital:
$$
L = \lim_{x \to 0} \frac{2e^{2x} - 2}{2x}.
$$
This is still $\frac{0}{0}$ (numerator: $2 - 2 = 0$, denominator: $0$). Apply L'Hôpital again:
$$
L = \lim_{x \to 0} \frac{4e^{2x}}{2} = \lim_{x \to 0} 2e^{2x} = 2 \cdot 1 = 2.
$$

**Answer:** $L = 2$.

---

**(c) Verify your result by using the Maclaurin series for $e^{2x}$ up to and including the term in $x^{2}$.**

**Approach:** Write the series expansion of $e^{2x}$ and substitute.

The Maclaurin series is $e^{u} = 1 + u + \frac{u^{2}}{2!} + \frac{u^{3}}{3!} + \cdots$. With $u = 2x$:
$$
e^{2x} = 1 + 2x + \frac{(2x)^{2}}{2} + \frac{(2x)^{3}}{6} + \cdots
= 1 + 2x + 2x^{2} + \frac{4}{3}x^{3} + \cdots
$$

Substitute into the numerator:
$$
e^{2x} - 1 - 2x = \bigl(1 + 2x + 2x^{2} + \cdots\bigr) - 1 - 2x = 2x^{2} + O(x^{3}).
$$
Hence
$$
L = \lim_{x \to 0} \frac{2x^{2} + O(x^{3})}{x^{2}}
= \lim_{x \to 0} \bigl(2 + O(x)\bigr) = 2.
$$
Both methods agree.

**Answer:** $L = 2$, verified by Maclaurin series.

---

## Problem 3
A curve is defined implicitly by $x^{3} + y^{3} = 6xy$.

**(a) Find an expression for $\dfrac{dy}{dx}$ in terms of $x$ and $y$.**

**Approach:** Differentiate both sides with respect to $x$, using the chain rule for terms involving $y$.

$$
\frac{d}{dx}\bigl(x^{3}\bigr) + \frac{d}{dx}\bigl(y^{3}\bigr) = \frac{d}{dx}(6xy).
$$

- $\frac{d}{dx}(x^{3}) = 3x^{2}$.
- $\frac{d}{dx}(y^{3}) = 3y^{2}\frac{dy}{dx}$ (chain rule).
- $\frac{d}{dx}(6xy) = 6y + 6x\frac{dy}{dx}$ (product rule).

Thus
$$
3x^{2} + 3y^{2}\frac{dy}{dx} = 6y + 6x\frac{dy}{dx}.
$$
Collect terms containing $\frac{dy}{dx}$:
$$
3y^{2}\frac{dy}{dx} - 6x\frac{dy}{dx} = 6y - 3x^{2},
$$
$$
\frac{dy}{dx}\bigl(3y^{2} - 6x\bigr) = 6y - 3x^{2}.
$$
Solve for $\frac{dy}{dx}$:
$$
\frac{dy}{dx} = \frac{6y - 3x^{2}}{3y^{2} - 6x}
= \frac{2y - x^{2}}{y^{2} - 2x}.
$$

**Answer:** $\displaystyle\frac{dy}{dx} = \frac{2y - x^{2}}{y^{2} - 2x}$.

---

**(b) Find the coordinates of all points on the curve at which the tangent is horizontal.**

**Approach:** A horizontal tangent occurs when $\frac{dy}{dx} = 0$, i.e. when the numerator is zero (provided the denominator is not also zero).

Set $2y - x^{2} = 0$, giving $x^{2} = 2y$, or $y = \frac{x^{2}}{2}$.

Substitute into the original equation $x^{3} + y^{3} = 6xy$:
$$
x^{3} + \left(\frac{x^{2}}{2}\right)^{3} = 6x\!\left(\frac{x^{2}}{2}\right),
$$
$$
x^{3} + \frac{x^{6}}{8} = 3x^{3},
$$
$$
\frac{x^{6}}{8} = 2x^{3},
$$
$$
x^{6} = 16x^{3},
$$
$$
x^{3}(x^{3} - 16) = 0.
$$

Hence $x^{3} = 0$ or $x^{3} = 16$.

- $x = 0$: then $y = \frac{0^{2}}{2} = 0$. The point is $(0, 0)$. Check denominator: $y^{2} - 2x = 0$, so $\frac{dy}{dx}$ is indeterminate at $(0,0)$. The point $(0,0)$ is a self-intersection (node) of the folium of Descartes; the tangent is not well-defined.

- $x^{3} = 16 \;\Longrightarrow\; x = \sqrt[3]{16} = 2\sqrt[3]{2}$. Then $y = \frac{x^{2}}{2} = \frac{(2\sqrt[3]{2})^{2}}{2} = \frac{4 \cdot 2^{2/3}}{2} = 2 \cdot 2^{2/3} = 2^{5/3}$.

Check denominator: $y^{2} - 2x = (2^{5/3})^{2} - 2(2\sqrt[3]{2}) = 2^{10/3} - 4\sqrt[3]{2} \neq 0$, so the tangent is genuinely horizontal at this point.

**Answer:** The tangent is horizontal at $\bigl(2\sqrt[3]{2},\; 2^{5/3}\bigr)$. (The origin $(0,0)$ gives $\frac{dy}{dx}$ of the form $\frac{0}{0}$ and is a node, not a point with a horizontal tangent.)

*Pitfall:* Always check that the denominator of $\frac{dy}{dx}$ is non-zero when the numerator is zero; otherwise the point may be singular.

---

## Problem 4
Evaluate $\displaystyle\int x^{2} e^{x}\,dx$ using integration by parts. Give your answer in simplest factored form.

**Approach:** Apply integration by parts twice. Recall $\int u\,dv = uv - \int v\,du$.

**First application:** Let $u = x^{2}$, $dv = e^{x}\,dx$. Then $du = 2x\,dx$, $v = e^{x}$.
$$
\int x^{2} e^{x}\,dx = x^{2}e^{x} - \int 2x\,e^{x}\,dx
= x^{2}e^{x} - 2\int x e^{x}\,dx.
$$

**Second application** (on $\int x e^{x}\,dx$): Let $u = x$, $dv = e^{x}\,dx$. Then $du = dx$, $v = e^{x}$.
$$
\int x e^{x}\,dx = x e^{x} - \int e^{x}\,dx = x e^{x} - e^{x}.
$$

Substitute back:
$$
\int x^{2} e^{x}\,dx = x^{2}e^{x} - 2\bigl(x e^{x} - e^{x}\bigr) + C
= x^{2}e^{x} - 2x e^{x} + 2e^{x} + C.
$$

Factor $e^{x}$:
$$
\int x^{2} e^{x}\,dx = e^{x}\bigl(x^{2} - 2x + 2\bigr) + C.
$$

**Answer:** $\displaystyle\int x^{2} e^{x}\,dx = e^{x}(x^{2} - 2x + 2) + C$.

*Pitfall:* Don't forget to apply integration by parts twice. The polynomial degree reduces each time until the $x$-term is gone.

---

## Problem 5
Evaluate $\displaystyle\int \ln(x^{2} + 1)\,dx$. You may use $\displaystyle\int \frac{1}{x^{2}+1}\,dx = \arctan x + C$.

**Approach:** Use integration by parts with $u = \ln(x^{2}+1)$ and $dv = dx$.

Let $u = \ln(x^{2} + 1)$, $dv = dx$.

Then $du = \frac{2x}{x^{2} + 1}\,dx$, $v = x$.

Apply the formula $\int u\,dv = uv - \int v\,du$:
$$
\int \ln(x^{2}+1)\,dx = x\ln(x^{2}+1) - \int x \cdot \frac{2x}{x^{2}+1}\,dx
= x\ln(x^{2}+1) - 2\int \frac{x^{2}}{x^{2}+1}\,dx.
$$

Rewrite the remaining integrand by adding and subtracting $1$ in the numerator:
$$
\frac{x^{2}}{x^{2}+1} = \frac{(x^{2}+1) - 1}{x^{2}+1} = 1 - \frac{1}{x^{2}+1}.
$$

Thus
$$
\int \ln(x^{2}+1)\,dx = x\ln(x^{2}+1) - 2\int\!\left(1 - \frac{1}{x^{2}+1}\right)dx
= x\ln(x^{2}+1) - 2\int\!dx + 2\int\frac{1}{x^{2}+1}\,dx.
$$

Integrate each term:
$$
= x\ln(x^{2}+1) - 2x + 2\arctan x + C.
$$

**Answer:** $\displaystyle\int \ln(x^{2} + 1)\,dx = x\ln(x^{2}+1) - 2x + 2\arctan x + C$.

---

## Problem 6
Use the method of partial fractions to show that
$$
\int \frac{3x^{2} + 5x + 2}{x^{3} + x^{2} + x + 1}\,dx = \ln\!\left|(x+1)^{2}\sqrt{x^{2}+1}\right| + C.
$$
Begin by factorising the denominator completely.

**Approach:** Factor the denominator, set up partial fractions, solve for constants, then integrate.

**Step 1 — Factorise the denominator:**
$$
x^{3} + x^{2} + x + 1 = x^{2}(x+1) + 1(x+1) = (x+1)(x^{2}+1).
$$
The factor $x^{2}+1$ is irreducible over the reals.

**Step 2 — Set up partial fractions:**
$$
\frac{3x^{2}+5x+2}{(x+1)(x^{2}+1)} = \frac{A}{x+1} + \frac{Bx + C}{x^{2}+1}.
$$

Multiply through by $(x+1)(x^{2}+1)$:
$$
3x^{2} + 5x + 2 = A(x^{2}+1) + (Bx + C)(x+1).
$$

**Step 3 — Solve for constants:**
Expand the right-hand side:
$$
A(x^{2}+1) + (Bx+C)(x+1) = Ax^{2} + A + Bx^{2} + Bx + Cx + C = (A+B)x^{2} + (B+C)x + (A+C).
$$

Equate coefficients with $3x^{2} + 5x + 2$:
- $x^{2}$: $A + B = 3$
- $x^{1}$: $B + C = 5$
- $x^{0}$: $A + C = 2$

From the first equation, $B = 3 - A$. From the third, $C = 2 - A$. Substitute into the second:
$$
(3 - A) + (2 - A) = 5 \;\Longrightarrow\; 5 - 2A = 5 \;\Longrightarrow\; A = 0.
$$
Then $B = 3 - 0 = 3$ and $C = 2 - 0 = 2$.

Thus
$$
\frac{3x^{2}+5x+2}{(x+1)(x^{2}+1)} = \frac{3x + 2}{x^{2}+1}.
$$

**Step 4 — Integrate:**
$$
\int \frac{3x+2}{x^{2}+1}\,dx = 3\int\frac{x}{x^{2}+1}\,dx + 2\int\frac{1}{x^{2}+1}\,dx.
$$

For the first integral, let $u = x^{2}+1$, $du = 2x\,dx$, so $\int\frac{x}{x^{2}+1}\,dx = \frac{1}{2}\ln|x^{2}+1|$.

The second integral is $2\arctan x$.

Hence
$$
\int \frac{3x^{2}+5x+2}{x^{3}+x^{2}+x+1}\,dx = \frac{3}{2}\ln|x^{2}+1| + 2\arctan x + C.
$$

**Note:** The result obtained does not match the claimed answer $\ln|(x+1)^{2}\sqrt{x^{2}+1}| + C$. Differentiating the claimed answer gives $\frac{3x^{2}+x+2}{(x+1)(x^{2}+1)}$, suggesting a typo in the problem statement (the numerator should likely be $3x^{2} + x + 2$ rather than $3x^{2} + 5x + 2$). With the corrected numerator $3x^{2}+x+2$, the partial fractions become $\frac{2}{x+1} + \frac{x}{x^{2}+1}$, which integrates to $2\ln|x+1| + \frac{1}{2}\ln(x^{2}+1) + C = \ln\!\left|(x+1)^{2}\sqrt{x^{2}+1}\right| + C$.

**Answer:** $\displaystyle\int \frac{3x^{2}+5x+2}{x^{3}+x^{2}+x+1}\,dx = \frac{3}{2}\ln|x^{2}+1| + 2\arctan x + C$. (See note above regarding the discrepancy with the claimed answer.)

---

## Problem 7
A spherical balloon is being inflated at a rate of $100\,\text{cm}^{3}\,\text{s}^{-1}$.

**(a) Write down an expression for the volume $V$ of the balloon in terms of its radius $r$.**

**Approach:** Recall the formula for the volume of a sphere.

**Answer:** $V = \frac{4}{3}\pi r^{3}$.

---

**(b) Find the rate at which the radius is increasing when the radius is $10\,\text{cm}$.**

**Approach:** Use related rates. Differentiate $V$ with respect to $t$, then solve for $\frac{dr}{dt}$.

Given $\frac{dV}{dt} = 100$. Differentiate $V = \frac{4}{3}\pi r^{3}$ with respect to $t$:
$$
\frac{dV}{dt} = 4\pi r^{2}\,\frac{dr}{dt}.
$$

Substitute $\frac{dV}{dt} = 100$ and $r = 10$:
$$
100 = 4\pi (10)^{2}\,\frac{dr}{dt}
= 4\pi \cdot 100\,\frac{dr}{dt}
= 400\pi\,\frac{dr}{dt}.
$$

Solve for $\frac{dr}{dt}$:
$$
\frac{dr}{dt} = \frac{100}{400\pi} = \frac{1}{4\pi}\;\text{cm}\,\text{s}^{-1}.
$$

**Answer:** $\displaystyle\frac{dr}{dt} = \frac{1}{4\pi}\;\text{cm}\,\text{s}^{-1}$ (approximately $0.0796\;\text{cm}\,\text{s}^{-1}$).

---

**(c) Find the rate at which the surface area is increasing at the instant when the radius is $10\,\text{cm}$.**

**Approach:** The surface area of a sphere is $S = 4\pi r^{2}$. Differentiate with respect to $t$ and use $\frac{dr}{dt}$ from part (b).

$$
S = 4\pi r^{2} \;\Longrightarrow\; \frac{dS}{dt} = 8\pi r\,\frac{dr}{dt}.
$$

At $r = 10$, $\frac{dr}{dt} = \frac{1}{4\pi}$:
$$
\frac{dS}{dt} = 8\pi (10)\!\left(\frac{1}{4\pi}\right)
= \frac{80\pi}{4\pi} = 20\;\text{cm}^{2}\,\text{s}^{-1}.
$$

**Answer:** $\displaystyle\frac{dS}{dt} = 20\;\text{cm}^{2}\,\text{s}^{-1}$.

---

## Problem 8
Consider the limit $\displaystyle\lim_{x \to \infty} \frac{\ln x}{\sqrt{x}}$.

**(a) State the type of indeterminate form.**

**Approach:** As $x \to \infty$, $\ln x \to \infty$ and $\sqrt{x} \to \infty$.

**Answer:** Indeterminate form $\frac{\infty}{\infty}$.

---

**(b) Use L'Hôpital's rule to evaluate the limit.**

**Approach:** Differentiate numerator and denominator.

$$
\lim_{x \to \infty} \frac{\ln x}{\sqrt{x}}
= \lim_{x \to \infty} \frac{\frac{1}{x}}{\frac{1}{2\sqrt{x}}}
= \lim_{x \to \infty} \frac{1}{x} \cdot \frac{2\sqrt{x}}{1}
= \lim_{x \to \infty} \frac{2}{\sqrt{x}} = 0.
$$

**Answer:** The limit equals $0$.

---

**(c) Comment on what this limit tells you about the relative growth rates of $\ln x$ and $\sqrt{x}$ as $x \to \infty$.**

**Approach:** A limit of $0$ means the numerator grows more slowly than the denominator.

Since $\displaystyle\lim_{x \to \infty} \frac{\ln x}{\sqrt{x}} = 0$, the function $\ln x$ grows much more slowly than $\sqrt{x}$ as $x \to \infty$. In terms of asymptotic growth rates, any power function $x^{a}$ (with $a > 0$) eventually dominates $\ln x$, no matter how small $a$ is.

**Answer:** $\ln x$ grows asymptotically slower than $\sqrt{x}$; as $x \to \infty$, $\sqrt{x}$ dominates $\ln x$.

---

## Problem 9
A curve is defined by the parametric equations
$$
x = t^{2} + 2t,\qquad y = t^{3} - 3t,
$$
where $t \in \mathbb{R}$.

**(a) Find $\dfrac{dy}{dx}$ in terms of $t$.**

**Approach:** Use the chain rule: $\displaystyle\frac{dy}{dx} = \frac{dy/dt}{dx/dt}$.

$$
\frac{dx}{dt} = 2t + 2,\qquad \frac{dy}{dt} = 3t^{2} - 3.
$$

Hence
$$
\frac{dy}{dx} = \frac{3t^{2} - 3}{2t + 2}
= \frac{3(t^{2} - 1)}{2(t + 1)}
= \frac{3(t-1)(t+1)}{2(t+1)}.
$$

For $t \neq -1$, cancel $(t+1)$:
$$
\frac{dy}{dx} = \frac{3(t-1)}{2}.
$$

**Answer:** $\displaystyle\frac{dy}{dx} = \frac{3(t-1)}{2}$ (for $t \neq -1$).

---

**(b) Determine the coordinates of the points on the curve where the tangent is parallel to the $x$-axis.**

**Approach:** A tangent parallel to the $x$-axis has $\frac{dy}{dx} = 0$.

Set $\frac{dy}{dx} = \frac{3(t-1)}{2} = 0$, giving $t = 1$.

At $t = 1$:
$$
x = 1^{2} + 2(1) = 3,\qquad y = 1^{3} - 3(1) = -2.
$$

**Answer:** The tangent is horizontal at the point $(3, -2)$.

---

**(c) Find the equation of the tangent to the curve at the point where $t = 1$, giving your answer in the form $ax + by + c = 0$.**

**Approach:** At $t = 1$, we already know the point $(3, -2)$ and the gradient $\frac{dy}{dx} = 0$ (horizontal). The tangent is the horizontal line through $(3, -2)$.

A horizontal line has equation $y = -2$, which can be written as:
$$
0\cdot x + 1\cdot y + 2 = 0.
$$

**Answer:** $y + 2 = 0$ (or $0x + y + 2 = 0$).

---

## Problem 10
Evaluate $\displaystyle\int_{0}^{\pi/2} e^{x} \cos x\,dx$. Use integration by parts twice and solve for the original integral.

**Approach:** Let $I = \int_{0}^{\pi/2} e^{x}\cos x\,dx$. Apply integration by parts twice; the original integral reappears, allowing us to solve for $I$ algebraically.

**First integration by parts:** Let $u = \cos x$, $dv = e^{x}\,dx$. Then $du = -\sin x\,dx$, $v = e^{x}$.
$$
I = \Bigl[e^{x}\cos x\Bigr]_{0}^{\pi/2} - \int_{0}^{\pi/2} e^{x}(-\sin x)\,dx
= \Bigl[e^{x}\cos x\Bigr]_{0}^{\pi/2} + \int_{0}^{\pi/2} e^{x}\sin x\,dx.
$$

Evaluate the boundary term:
$$
\Bigl[e^{x}\cos x\Bigr]_{0}^{\pi/2} = e^{\pi/2}\cos\!\left(\tfrac{\pi}{2}\right) - e^{0}\cos(0) = e^{\pi/2}\cdot 0 - 1\cdot 1 = -1.
$$

Thus $I = -1 + \int_{0}^{\pi/2} e^{x}\sin x\,dx$.

**Second integration by parts** (on $\int e^{x}\sin x\,dx$): Let $u = \sin x$, $dv = e^{x}\,dx$. Then $du = \cos x\,dx$, $v = e^{x}$.
$$
\int_{0}^{\pi/2} e^{x}\sin x\,dx = \Bigl[e^{x}\sin x\Bigr]_{0}^{\pi/2} - \int_{0}^{\pi/2} e^{x}\cos x\,dx.
$$

Evaluate the boundary term:
$$
\Bigl[e^{x}\sin x\Bigr]_{0}^{\pi/2} = e^{\pi/2}\sin\!\left(\tfrac{\pi}{2}\right) - e^{0}\sin(0) = e^{\pi/2}\cdot 1 - 0 = e^{\pi/2}.
$$

So $\int_{0}^{\pi/2} e^{x}\sin x\,dx = e^{\pi/2} - I$.

Substitute back into the expression for $I$:
$$
I = -1 + \bigl(e^{\pi/2} - I\bigr).
$$

Solve for $I$:
$$
I = -1 + e^{\pi/2} - I \;\Longrightarrow\; 2I = e^{\pi/2} - 1 \;\Longrightarrow\; I = \frac{e^{\pi/2} - 1}{2}.
$$

**Answer:** $\displaystyle\int_{0}^{\pi/2} e^{x} \cos x\,dx = \frac{e^{\pi/2} - 1}{2}$.

*Pitfall:* When using this "boomerang" technique, be careful with signs — the original integral must reappear with the **same sign** to solve for it.

---

## Problem 11
A function $g$ is defined by
$$
g(x) = \begin{cases}
\dfrac{x^{2} - 4}{x - 2}, & x < 2,\\[6pt]
ax + b, & 2 \leq x \leq 3,\\[6pt]
\dfrac{\sqrt{x} - \sqrt{3}}{x - 3}, & x > 3,
\end{cases}
$$
where $a$ and $b$ are real constants.

**(a) Find $\displaystyle\lim_{x \to 2^{-}} g(x)$.**

**Approach:** For $x < 2$, $g(x) = \frac{x^{2}-4}{x-2}$. Factor the numerator.

$$
\frac{x^{2} - 4}{x - 2} = \frac{(x-2)(x+2)}{x-2}.
$$
For $x < 2$ (so $x \neq 2$), this simplifies to $x + 2$. Hence
$$
\lim_{x \to 2^{-}} g(x) = \lim_{x \to 2^{-}} (x + 2) = 2 + 2 = 4.
$$

**Answer:** $\displaystyle\lim_{x \to 2^{-}} g(x) = 4$.

---

**(b) Find $\displaystyle\lim_{x \to 3^{+}} g(x)$.**

**Approach:** For $x > 3$, $g(x) = \frac{\sqrt{x} - \sqrt{3}}{x - 3}$. Rationalise the numerator.

Multiply numerator and denominator by $\sqrt{x} + \sqrt{3}$:
$$
\frac{\sqrt{x} - \sqrt{3}}{x - 3} \cdot \frac{\sqrt{x} + \sqrt{3}}{\sqrt{x} + \sqrt{3}}
= \frac{x - 3}{(x-3)(\sqrt{x} + \sqrt{3})}
= \frac{1}{\sqrt{x} + \sqrt{3}}.
$$

For $x > 3$ (so $x \neq 3$), this simplification is valid. Hence
$$
\lim_{x \to 3^{+}} g(x) = \lim_{x \to 3^{+}} \frac{1}{\sqrt{x} + \sqrt{3}}
= \frac{1}{\sqrt{3} + \sqrt{3}} = \frac{1}{2\sqrt{3}}.
$$

**Answer:** $\displaystyle\lim_{x \to 3^{+}} g(x) = \frac{1}{2\sqrt{3}}$.

---

**(c) Determine the values of $a$ and $b$ such that $g$ is continuous on $\mathbb{R}$.**

**Approach:** For continuity, the function value must match the limits at the boundary points $x=2$ and $x=3$.

At $x = 2$, the middle piece applies: $g(2) = a(2) + b = 2a + b$. For continuity,
$$
2a + b = \lim_{x \to 2^{-}} g(x) = 4. \tag{1}
$$

At $x = 3$, the middle piece applies: $g(3) = a(3) + b = 3a + b$. For continuity,
$$
3a + b = \lim_{x \to 3^{+}} g(x) = \frac{1}{2\sqrt{3}}. \tag{2}
$$

Subtract (1) from (2):
$$
(3a + b) - (2a + b) = \frac{1}{2\sqrt{3}} - 4 \;\Longrightarrow\; a = \frac{1}{2\sqrt{3}} - 4.
$$

Substitute into (1):
$$
2\!\left(\frac{1}{2\sqrt{3}} - 4\right) + b = 4 \;\Longrightarrow\; \frac{1}{\sqrt{3}} - 8 + b = 4 \;\Longrightarrow\; b = 12 - \frac{1}{\sqrt{3}}.
$$

**Answer:** $a = \frac{1}{2\sqrt{3}} - 4,\quad b = 12 - \frac{1}{\sqrt{3}}$.

---

## Problem 12
Use the substitution $x = \sin\theta$, where $-\frac{\pi}{2} \leq \theta \leq \frac{\pi}{2}$, to evaluate
$$
\int_{0}^{1/2} \frac{x^{2}}{\sqrt{1 - x^{2}}}\,dx.
$$

**Approach:** Substitute $x = \sin\theta$, which implies $dx = \cos\theta\,d\theta$ and $\sqrt{1-x^{2}} = \cos\theta$ (since $\cos\theta \geq 0$ on $[-\frac{\pi}{2}, \frac{\pi}{2}]$).

Change the limits:
- $x = 0$: $\sin\theta = 0 \;\Longrightarrow\; \theta = 0$.
- $x = \frac{1}{2}$: $\sin\theta = \frac{1}{2} \;\Longrightarrow\; \theta = \frac{\pi}{6}$.

Substitute into the integral:
$$
\int_{0}^{1/2} \frac{x^{2}}{\sqrt{1-x^{2}}}\,dx
= \int_{0}^{\pi/6} \frac{\sin^{2}\theta}{\cos\theta} \cdot \cos\theta\,d\theta
= \int_{0}^{\pi/6} \sin^{2}\theta\,d\theta.
$$

Use the identity $\sin^{2}\theta = \frac{1 - \cos(2\theta)}{2}$:
$$
\int_{0}^{\pi/6} \sin^{2}\theta\,d\theta
= \int_{0}^{\pi/6} \frac{1 - \cos(2\theta)}{2}\,d\theta
= \frac{1}{2}\int_{0}^{\pi/6} \bigl(1 - \cos(2\theta)\bigr)\,d\theta.
$$

Integrate:
$$
= \frac{1}{2}\Bigl[\theta - \frac{1}{2}\sin(2\theta)\Bigr]_{0}^{\pi/6}
= \frac{1}{2}\!\left(\frac{\pi}{6} - \frac{1}{2}\sin\!\left(\frac{\pi}{3}\right) - 0\right)
= \frac{1}{2}\!\left(\frac{\pi}{6} - \frac{1}{2}\cdot\frac{\sqrt{3}}{2}\right)
= \frac{1}{2}\!\left(\frac{\pi}{6} - \frac{\sqrt{3}}{4}\right)
= \frac{\pi}{12} - \frac{\sqrt{3}}{8}.
$$

**Answer:** $\displaystyle\int_{0}^{1/2} \frac{x^{2}}{\sqrt{1 - x^{2}}}\,dx = \frac{\pi}{12} - \frac{\sqrt{3}}{8}$.

---

## Problem 13
A water tank has the shape of an inverted right circular cone with height $4\,\text{m}$ and base radius $2\,\text{m}$. Water is being pumped into the tank at a constant rate of $0.5\,\text{m}^{3}\,\text{min}^{-1}$.

**(a) Express the volume $V$ of water in the tank in terms of the height $h$ of the water level.**

**Approach:** Use similar triangles to relate the water's radius $r$ to its height $h$.

The full cone has height $H = 4$ and base radius $R = 2$. By similar triangles,
$$
\frac{r}{h} = \frac{R}{H} = \frac{2}{4} = \frac{1}{2} \;\Longrightarrow\; r = \frac{h}{2}.
$$

The volume of a cone is $V = \frac{1}{3}\pi r^{2}h$. Substitute $r = \frac{h}{2}$:
$$
V = \frac{1}{3}\pi\left(\frac{h}{2}\right)^{2}h
= \frac{1}{3}\pi \cdot \frac{h^{2}}{4} \cdot h
= \frac{\pi}{12}h^{3}.
$$

**Answer:** $V = \frac{\pi}{12}h^{3}$.

---

**(b) Find the rate at which the water level is rising when the water is $1\,\text{m}$ deep.**

**Approach:** Differentiate $V$ with respect to $t$ and use $\frac{dV}{dt} = 0.5$.

$$
\frac{dV}{dt} = \frac{\pi}{12} \cdot 3h^{2}\,\frac{dh}{dt} = \frac{\pi}{4}h^{2}\,\frac{dh}{dt}.
$$

Set $\frac{dV}{dt} = 0.5$ and $h = 1$:
$$
0.5 = \frac{\pi}{4}(1)^{2}\,\frac{dh}{dt} \;\Longrightarrow\; \frac{dh}{dt} = \frac{0.5 \times 4}{\pi} = \frac{2}{\pi}\;\text{m}\,\text{min}^{-1}.
$$

**Answer:** $\displaystyle\frac{dh}{dt} = \frac{2}{\pi}\;\text{m}\,\text{min}^{-1}$ (approximately $0.637\;\text{m}\,\text{min}^{-1}$).

---

**(c) If the tank is initially empty, how long will it take to fill the tank completely? Give your answer in minutes, correct to one decimal place.**

**Approach:** Find the total volume of the tank when $h = 4$, then divide by the constant fill rate.

When full, $h = 4$:
$$
V_{\text{full}} = \frac{\pi}{12}(4)^{3} = \frac{\pi}{12} \cdot 64 = \frac{16\pi}{3}\;\text{m}^{3}.
$$

At a rate of $0.5\;\text{m}^{3}\,\text{min}^{-1}$:
$$
t = \frac{V_{\text{full}}}{0.5} = \frac{16\pi/3}{0.5} = \frac{16\pi}{1.5} = \frac{32\pi}{3} \approx 33.5\;\text{min}.
$$

**Answer:** $33.5$ minutes (to one decimal place).

---

## Problem 14
Evaluate the following integrals:

**(a) $\displaystyle\int \tan^{3} x\,dx$**

**Approach:** Write $\tan^{3}x = \tan x \cdot \tan^{2}x = \tan x(\sec^{2}x - 1)$.

$$
\int \tan^{3}x\,dx = \int \tan x\,(\sec^{2}x - 1)\,dx
= \int \tan x \sec^{2}x\,dx - \int \tan x\,dx.
$$

For the first term, let $u = \tan x$, $du = \sec^{2}x\,dx$:
$$
\int \tan x \sec^{2}x\,dx = \int u\,du = \frac{u^{2}}{2} = \frac{\tan^{2}x}{2}.
$$

The second term is a standard integral: $\int \tan x\,dx = \ln|\sec x| + C$ (or $-\ln|\cos x| + C$).

Thus
$$
\int \tan^{3}x\,dx = \frac{\tan^{2}x}{2} - \ln|\sec x| + C.
$$

**Answer:** $\displaystyle\int \tan^{3}x\,dx = \frac{1}{2}\tan^{2}x - \ln|\sec x| + C$.

---

**(b) $\displaystyle\int \frac{\sin x}{\cos^{2} x}\,dx$**

**Approach:** Let $u = \cos x$, then $du = -\sin x\,dx$, so $\sin x\,dx = -du$.

$$
\int \frac{\sin x}{\cos^{2}x}\,dx = \int \frac{-du}{u^{2}} = -\int u^{-2}\,du = -(-u^{-1}) + C = \frac{1}{u} + C = \frac{1}{\cos x} + C = \sec x + C.
$$

**Answer:** $\displaystyle\int \frac{\sin x}{\cos^{2}x}\,dx = \sec x + C$.

---

**(c) $\displaystyle\int_{0}^{\pi/4} \sec^{4} x\,dx$**

**Approach:** Write $\sec^{4}x = \sec^{2}x \cdot \sec^{2}x = \sec^{2}x\,(1 + \tan^{2}x)$.

Let $u = \tan x$, $du = \sec^{2}x\,dx$. Change limits: $x = 0 \Rightarrow u = 0$; $x = \frac{\pi}{4} \Rightarrow u = 1$.

$$
\int_{0}^{\pi/4} \sec^{4}x\,dx = \int_{0}^{\pi/4} \sec^{2}x\,(1 + \tan^{2}x)\,dx
= \int_{0}^{1} (1 + u^{2})\,du.
$$

Integrate:
$$
= \Bigl[u + \frac{u^{3}}{3}\Bigr]_{0}^{1}
= \left(1 + \frac{1}{3}\right) - 0 = \frac{4}{3}.
$$

**Answer:** $\displaystyle\int_{0}^{\pi/4} \sec^{4}x\,dx = \frac{4}{3}$.

---

## Problem 15
Consider the limit $\displaystyle\lim_{x \to 0} \left(\frac{1}{\sin x} - \frac{1}{x}\right)$.

**(a) Show that this limit can be rewritten as a single fraction whose numerator and denominator both approach $0$ as $x \to 0$.**

**Approach:** Combine the two fractions over a common denominator.

$$
\frac{1}{\sin x} - \frac{1}{x} = \frac{x - \sin x}{x\sin x}.
$$

As $x \to 0$:
- Numerator: $x - \sin x \to 0 - 0 = 0$.
- Denominator: $x\sin x \to 0 \cdot 0 = 0$.

Thus the limit is of the indeterminate form $\frac{0}{0}$.

**Answer:** $\displaystyle\lim_{x \to 0} \frac{x - \sin x}{x\sin x}$, which is of the form $\frac{0}{0}$.

---

**(b) Use L'Hôpital's rule to evaluate the limit. You may need to apply the rule more than once.**

**Approach:** Apply L'Hôpital's rule to $\displaystyle\lim_{x \to 0} \frac{x - \sin x}{x\sin x}$.

**First application:**
Numerator derivative: $\frac{d}{dx}(x - \sin x) = 1 - \cos x$.
Denominator derivative: $\frac{d}{dx}(x\sin x) = \sin x + x\cos x$ (product rule).

$$
\lim_{x \to 0} \frac{x - \sin x}{x\sin x}
= \lim_{x \to 0} \frac{1 - \cos x}{\sin x + x\cos x}.
$$

At $x = 0$, numerator: $1 - 1 = 0$; denominator: $0 + 0 = 0$. Still $\frac{0}{0}$.

**Second application:**
Numerator derivative: $\frac{d}{dx}(1 - \cos x) = \sin x$.
Denominator derivative: $\frac{d}{dx}(\sin x + x\cos x) = \cos x + \cos x - x\sin x = 2\cos x - x\sin x$.

$$
\lim_{x \to 0} \frac{1 - \cos x}{\sin x + x\cos x}
= \lim_{x \to 0} \frac{\sin x}{2\cos x - x\sin x}.
$$

Now substitute $x = 0$:
Numerator: $\sin 0 = 0$. Denominator: $2\cos 0 - 0 = 2$.

Thus the limit is $\frac{0}{2} = 0$.

**Answer:** $\displaystyle\lim_{x \to 0} \left(\frac{1}{\sin x} - \frac{1}{x}\right) = 0$.

*Pitfall:* The original expression is of the form $\infty - \infty$, which is indeterminate. Rewriting as a single fraction is essential before applying L'Hôpital.

---

## Problem 16
A ladder of length $5\,\text{m}$ leans against a vertical wall. The bottom slides away at $0.3\,\text{m}\,\text{s}^{-1}$. At $t = 0$, the bottom is $3\,\text{m}$ from the wall.

**(a) Express the height $y$ of the top of the ladder in terms of the distance $x$ of the bottom from the wall.**

**Approach:** Use Pythagoras' theorem. The ladder, wall, and ground form a right-angled triangle.

The ladder is the hypotenuse of length $5$. Hence
$$
x^{2} + y^{2} = 5^{2} = 25 \;\Longrightarrow\; y = \sqrt{25 - x^{2}},
$$
where $y \geq 0$ (the ladder touches the wall above ground).

**Answer:** $y = \sqrt{25 - x^{2}}$.

---

**(b) Find the rate at which the top of the ladder is sliding down the wall when the bottom is $3\,\text{m}$ from the wall.**

**Approach:** Differentiate $x^{2} + y^{2} = 25$ with respect to $t$.

$$
2x\frac{dx}{dt} + 2y\frac{dy}{dt} = 0 \;\Longrightarrow\; \frac{dy}{dt} = -\frac{x}{y}\,\frac{dx}{dt}.
$$

Given $\frac{dx}{dt} = 0.3$ (positive because the bottom moves away). At $x = 3$, $y = \sqrt{25 - 3^{2}} = \sqrt{16} = 4$.

$$
\frac{dy}{dt} = -\frac{3}{4} \cdot 0.3 = -0.225\;\text{m}\,\text{s}^{-1}.
$$

The negative sign indicates the top is sliding **down**.

**Answer:** $\displaystyle\frac{dy}{dt} = -0.225\;\text{m}\,\text{s}^{-1}$ (sliding down at $0.225\;\text{m}\,\text{s}^{-1}$).

---

**(c) Determine whether the top of the ladder is accelerating or decelerating at this instant. Justify your answer.**

**Approach:** Find $\frac{d^{2}y}{dt^{2}}$ and evaluate its sign. Since $\frac{dy}{dt}$ is negative, "accelerating" means $\frac{d^{2}y}{dt^{2}} < 0$ (becoming more negative, i.e. sliding down faster).

From part (b), $\frac{dy}{dt} = -\frac{x}{y} \cdot 0.3$. Differentiate with respect to $t$ using the quotient rule:
$$
\frac{d^{2}y}{dt^{2}} = -0.3 \cdot \frac{y\frac{dx}{dt} - x\frac{dy}{dt}}{y^{2}}.
$$

At $x = 3$, $y = 4$, $\frac{dx}{dt} = 0.3$, $\frac{dy}{dt} = -0.225$:
$$
\frac{d^{2}y}{dt^{2}} = -0.3 \cdot \frac{4(0.3) - 3(-0.225)}{4^{2}}
= -0.3 \cdot \frac{1.2 + 0.675}{16}
= -0.3 \cdot \frac{1.875}{16}
= -0.3 \cdot 0.1171875
\approx -0.0352\;\text{m}\,\text{s}^{-2}.
$$

Since $\frac{dy}{dt} < 0$ and $\frac{d^{2}y}{dt^{2}} < 0$, the velocity is becoming more negative, i.e. the magnitude of the downward velocity is **increasing**. The top of the ladder is **accelerating** downward.

**Answer:** The top is accelerating (downward); $\frac{d^{2}y}{dt^{2}} \approx -0.0352\;\text{m}\,\text{s}^{-2}$, so the downward speed is increasing.

---

## Problem 17
Prove that $\displaystyle\int x^{n} \ln x\,dx = \frac{x^{n+1}}{(n+1)^{2}}\bigl((n+1)\ln x - 1\bigr) + C$ for positive integers $n$, using integration by parts.

**Approach:** Choose $u = \ln x$ and $dv = x^{n}\,dx$.

Let $u = \ln x$, $dv = x^{n}\,dx$. Then $du = \frac{1}{x}\,dx$, $v = \frac{x^{n+1}}{n+1}$.

Apply $\int u\,dv = uv - \int v\,du$:
$$
\int x^{n}\ln x\,dx = \frac{x^{n+1}}{n+1}\ln x - \int \frac{x^{n+1}}{n+1} \cdot \frac{1}{x}\,dx
= \frac{x^{n+1}\ln x}{n+1} - \frac{1}{n+1}\int x^{n}\,dx.
$$

Integrate the remaining term:
$$
\int x^{n}\,dx = \frac{x^{n+1}}{n+1}.
$$

Thus
$$
\int x^{n}\ln x\,dx = \frac{x^{n+1}\ln x}{n+1} - \frac{1}{n+1} \cdot \frac{x^{n+1}}{n+1} + C
= \frac{x^{n+1}\ln x}{n+1} - \frac{x^{n+1}}{(n+1)^{2}} + C.
$$

Factor $\frac{x^{n+1}}{(n+1)^{2}}$:
$$
= \frac{x^{n+1}}{(n+1)^{2}}\bigl((n+1)\ln x - 1\bigr) + C.
$$

This matches the required formula.

**Answer:** The formula is proved. $\square$

*Pitfall:* The choice $u = \ln x$ is strategic — it eliminates the logarithm upon differentiation, while $x^{n}$ is easy to integrate.

---

## Problem 18
Decompose $f(x) = \dfrac{5x^{2} + 2x + 1}{(x-1)(x^{2}+x+1)}$ into partial fractions of the form $\dfrac{A}{x-1} + \dfrac{Bx+C}{x^{2}+x+1}$. Hence evaluate $\displaystyle\int f(x)\,dx$.

**Step 1 — Set up the decomposition:**
$$
\frac{5x^{2}+2x+1}{(x-1)(x^{2}+x+1)} = \frac{A}{x-1} + \frac{Bx+C}{x^{2}+x+1}.
$$

Multiply through by $(x-1)(x^{2}+x+1)$:
$$
5x^{2}+2x+1 = A(x^{2}+x+1) + (Bx+C)(x-1).
$$

**Step 2 — Solve for $A$, $B$, $C$.**

Expand the right-hand side:
$$
A(x^{2}+x+1) + (Bx+C)(x-1) = Ax^{2} + Ax + A + Bx^{2} - Bx + Cx - C
$$
$$
= (A+B)x^{2} + (A - B + C)x + (A - C).
$$

Equate coefficients with $5x^{2}+2x+1$:
- $x^{2}$: $A + B = 5$
- $x^{1}$: $A - B + C = 2$
- $x^{0}$: $A - C = 1$

From the third, $C = A - 1$. From the first, $B = 5 - A$. Substitute into the second:
$$
A - (5 - A) + (A - 1) = 2 \;\Longrightarrow\; A - 5 + A + A - 1 = 2 \;\Longrightarrow\; 3A - 6 = 2 \;\Longrightarrow\; 3A = 8 \;\Longrightarrow\; A = \frac{8}{3}.
$$

Then $B = 5 - \frac{8}{3} = \frac{7}{3}$, and $C = \frac{8}{3} - 1 = \frac{5}{3}$.

Thus
$$
\frac{5x^{2}+2x+1}{(x-1)(x^{2}+x+1)} = \frac{8/3}{x-1} + \frac{\frac{7}{3}x + \frac{5}{3}}{x^{2}+x+1}.
$$

**Step 3 — Integrate.**

$$
\int f(x)\,dx = \frac{8}{3}\int\frac{1}{x-1}\,dx + \frac{1}{3}\int\frac{7x+5}{x^{2}+x+1}\,dx.
$$

The first term: $\frac{8}{3}\ln|x-1|$.

For the second term, complete the square in the denominator: $x^{2}+x+1 = (x+\frac{1}{2})^{2} + \frac{3}{4}$.

Rewrite the numerator to split off the derivative of the denominator ($2x+1$):
$$
7x+5 = \frac{7}{2}(2x+1) + \left(5 - \frac{7}{2}\right) = \frac{7}{2}(2x+1) + \frac{3}{2}.
$$

Thus
$$
\frac{1}{3}\int\frac{7x+5}{x^{2}+x+1}\,dx
= \frac{1}{3}\cdot\frac{7}{2}\int\frac{2x+1}{x^{2}+x+1}\,dx \;+\; \frac{1}{3}\cdot\frac{3}{2}\int\frac{1}{x^{2}+x+1}\,dx
$$
$$
= \frac{7}{6}\ln|x^{2}+x+1| + \frac{1}{2}\int\frac{1}{(x+\frac{1}{2})^{2} + \frac{3}{4}}\,dx.
$$

For the remaining integral, use the arctan form $\int\frac{1}{u^{2}+a^{2}}\,du = \frac{1}{a}\arctan\frac{u}{a}$ with $u = x+\frac{1}{2}$, $a = \frac{\sqrt{3}}{2}$:
$$
\int\frac{1}{(x+\frac{1}{2})^{2} + \frac{3}{4}}\,dx
= \frac{1}{\sqrt{3}/2}\arctan\!\left(\frac{x+\frac{1}{2}}{\sqrt{3}/2}\right)
= \frac{2}{\sqrt{3}}\arctan\!\left(\frac{2x+1}{\sqrt{3}}\right).
$$

Multiplying by $\frac{1}{2}$ gives $\frac{1}{\sqrt{3}}\arctan\!\left(\frac{2x+1}{\sqrt{3}}\right)$.

Putting everything together:
$$
\int f(x)\,dx = \frac{8}{3}\ln|x-1| + \frac{7}{6}\ln|x^{2}+x+1| + \frac{1}{\sqrt{3}}\arctan\!\left(\frac{2x+1}{\sqrt{3}}\right) + C.
$$

**Answer:** $\displaystyle\int f(x)\,dx = \frac{8}{3}\ln|x-1| + \frac{7}{6}\ln(x^{2}+x+1) + \frac{1}{\sqrt{3}}\arctan\!\left(\frac{2x+1}{\sqrt{3}}\right) + C$.

---

## Problem 19
Consider the limit $\displaystyle\lim_{x \to 0} (1 + \sin x)^{1/x}$.

**(a) By taking the natural logarithm, show that evaluating this limit is equivalent to finding $\displaystyle\exp\!\left(\lim_{x \to 0} \frac{\ln(1+\sin x)}{x}\right)$.**

**Approach:** Let $L = \lim_{x \to 0} (1+\sin x)^{1/x}$. Take $\ln$ of both sides.

Since the exponential function is continuous,
$$
\ln L = \ln\!\left(\lim_{x \to 0} (1+\sin x)^{1/x}\right)
= \lim_{x \to 0} \ln\!\left((1+\sin x)^{1/x}\right)
= \lim_{x \to 0} \frac{\ln(1+\sin x)}{x}.
$$

Exponentiating both sides gives $L = \exp\!\left(\lim_{x \to 0} \frac{\ln(1+\sin x)}{x}\right)$.

**Answer:** The equivalence is shown: $L = \exp\!\left(\displaystyle\lim_{x \to 0} \frac{\ln(1+\sin x)}{x}\right)$.

---

**(b) Use L'Hôpital's rule to evaluate the inner limit.**

**Approach:** Set $M = \lim_{x \to 0} \frac{\ln(1+\sin x)}{x}$. Direct substitution gives $\frac{0}{0}$.

Apply L'Hôpital: differentiate numerator and denominator.
- $\frac{d}{dx}\ln(1+\sin x) = \frac{\cos x}{1+\sin x}$.
- $\frac{d}{dx}(x) = 1$.

Thus
$$
M = \lim_{x \to 0} \frac{\cos x}{1+\sin x} = \frac{\cos 0}{1 + \sin 0} = \frac{1}{1} = 1.
$$

**Answer:** $M = 1$.

---

**(c) Hence state the value of the original limit.**

**Approach:** $L = e^{M} = e^{1}$.

**Answer:** $\displaystyle\lim_{x \to 0} (1 + \sin x)^{1/x} = e$.

---

## Problem 20
A curve is defined implicitly by $e^{xy} + x^{2} - y^{2} = 0$.

**(a) Show that $\dfrac{dy}{dx} = \dfrac{2x + ye^{xy}}{2y - xe^{xy}}$.**

**Approach:** Differentiate implicitly with respect to $x$.

Differentiate each term:
- $\frac{d}{dx}\bigl(e^{xy}\bigr) = e^{xy} \cdot \frac{d}{dx}(xy) = e^{xy}\!\left(y + x\frac{dy}{dx}\right)$ (product rule).
- $\frac{d}{dx}(x^{2}) = 2x$.
- $\frac{d}{dx}(-y^{2}) = -2y\frac{dy}{dx}$.

Thus:
$$
e^{xy}\!\left(y + x\frac{dy}{dx}\right) + 2x - 2y\frac{dy}{dx} = 0.
$$

Expand and collect $\frac{dy}{dx}$ terms:
$$
y e^{xy} + x e^{xy}\frac{dy}{dx} + 2x - 2y\frac{dy}{dx} = 0,
$$
$$
x e^{xy}\frac{dy}{dx} - 2y\frac{dy}{dx} = -2x - y e^{xy},
$$
$$
\frac{dy}{dx}\bigl(x e^{xy} - 2y\bigr) = -2x - y e^{xy}.
$$

Thus
$$
\frac{dy}{dx} = \frac{-2x - y e^{xy}}{x e^{xy} - 2y}
= \frac{2x + y e^{xy}}{2y - x e^{xy}}.
$$

This matches the required expression.

**Answer:** Shown. $\square$

---

**(b) Find the gradient of the curve at the point $(0, 1)$.**

**Approach:** Substitute $x = 0$, $y = 1$ into $\frac{dy}{dx}$.

At $(0, 1)$: $e^{0\cdot 1} = e^{0} = 1$.

$$
\frac{dy}{dx}\Bigr|_{(0,1)} = \frac{2(0) + 1 \cdot 1}{2(1) - 0 \cdot 1} = \frac{0 + 1}{2 - 0} = \frac{1}{2}.
$$

**Answer:** The gradient at $(0, 1)$ is $\frac{1}{2}$.

---

**(c) Determine the equation of the tangent to the curve at $(0, 1)$.**

**Approach:** Use point-slope form $y - y_{1} = m(x - x_{1})$.

With $m = \frac{1}{2}$ and point $(0, 1)$:
$$
y - 1 = \frac{1}{2}(x - 0) \;\Longrightarrow\; y = \frac{1}{2}x + 1.
$$

In general form:
$$
x - 2y + 2 = 0.
$$

**Answer:** $x - 2y + 2 = 0$.

---

## Problem 21
Evaluate the following integrals using integration by parts:

**(a) $\displaystyle\int \arctan x\,dx$**

**Approach:** Let $u = \arctan x$, $dv = dx$. Then $du = \frac{1}{1+x^{2}}\,dx$, $v = x$.

$$
\int \arctan x\,dx = x\arctan x - \int \frac{x}{1+x^{2}}\,dx.
$$

For the remaining integral, substitute $w = 1+x^{2}$, $dw = 2x\,dx$, so $x\,dx = \frac{dw}{2}$:
$$
\int \frac{x}{1+x^{2}}\,dx = \frac{1}{2}\int\frac{1}{w}\,dw = \frac{1}{2}\ln|w| + C = \frac{1}{2}\ln(1+x^{2}) + C.
$$

Thus
$$
\int \arctan x\,dx = x\arctan x - \frac{1}{2}\ln(1+x^{2}) + C.
$$

**Answer:** $\displaystyle\int \arctan x\,dx = x\arctan x - \frac{1}{2}\ln(1+x^{2}) + C$.

---

**(b) $\displaystyle\int x\sec^{2}x\,dx$**

**Approach:** Let $u = x$, $dv = \sec^{2}x\,dx$. Then $du = dx$, $v = \tan x$.

$$
\int x\sec^{2}x\,dx = x\tan x - \int \tan x\,dx.
$$

Recall $\int \tan x\,dx = \ln|\sec x| + C$ (or $-\ln|\cos x| + C$). Thus
$$
\int x\sec^{2}x\,dx = x\tan x - \ln|\sec x| + C.
$$

**Answer:** $\displaystyle\int x\sec^{2}x\,dx = x\tan x - \ln|\sec x| + C$.

*Alternative form:* $x\tan x + \ln|\cos x| + C$.

---

**(c) $\displaystyle\int (\ln x)^{2}\,dx$**

**Approach:** Let $u = (\ln x)^{2}$, $dv = dx$. Then $du = 2\ln x \cdot \frac{1}{x}\,dx = \frac{2\ln x}{x}\,dx$, $v = x$.

$$
\int (\ln x)^{2}\,dx = x(\ln x)^{2} - \int x \cdot \frac{2\ln x}{x}\,dx
= x(\ln x)^{2} - 2\int \ln x\,dx.
$$

Now $\int \ln x\,dx$ requires another integration by parts. Let $u = \ln x$, $dv = dx$; then $du = \frac{1}{x}\,dx$, $v = x$:
$$
\int \ln x\,dx = x\ln x - \int x \cdot \frac{1}{x}\,dx = x\ln x - x + C.
$$

Substitute back:
$$
\int (\ln x)^{2}\,dx = x(\ln x)^{2} - 2(x\ln x - x) + C
= x(\ln x)^{2} - 2x\ln x + 2x + C.
$$

**Answer:** $\displaystyle\int (\ln x)^{2}\,dx = x\bigl((\ln x)^{2} - 2\ln x + 2\bigr) + C$.

---

## Problem 22
A function $f$ is defined by $f(x) = \dfrac{x^{2}+1}{x^{2}-1}$, except where the denominator vanishes.

**(a) Find all values of $x$ for which $f$ is discontinuous.**

**Approach:** The denominator $x^{2}-1 = 0$ when $x = \pm 1$. These are the only potential discontinuities since the numerator and denominator are polynomials (continuous everywhere else).

**Answer:** $f$ is discontinuous at $x = 1$ and $x = -1$.

---

**(b) For each point of discontinuity, evaluate the left-hand and right-hand limits and classify the type of discontinuity.**

**Approach:** Factor the denominator: $x^{2}-1 = (x-1)(x+1)$. The numerator does not share these factors, so these are vertical asymptotes.

**At $x = 1$:**
- As $x \to 1^{-}$ (from below): denominator $\to 0^{-}$ (since $x-1 < 0$, $x+1 > 0$), numerator $\to 2$. So $f(x) \to -\infty$.
- As $x \to 1^{+}$ (from above): denominator $\to 0^{+}$, numerator $\to 2$. So $f(x) \to +\infty$.

This is an **infinite discontinuity** (vertical asymptote).

**At $x = -1$:**
- As $x \to -1^{-}$ (from below): $x-1 < 0$, $x+1 < 0$ (small negative), so denominator $\to$ (negative)$\times$(negative) $\to 0^{+}$. Numerator $\to 2$. So $f(x) \to +\infty$.
- As $x \to -1^{+}$ (from above): $x-1 < 0$, $x+1 > 0$ (small positive), so denominator $\to 0^{-}$. Numerator $\to 2$. So $f(x) \to -\infty$.

This is also an **infinite discontinuity** (vertical asymptote).

**Answer:** Both $x=1$ and $x=-1$ are infinite discontinuities (vertical asymptotes).

---

**(c) Determine the equations of all vertical and horizontal asymptotes.**

**Approach:**
- **Vertical asymptotes** occur where the denominator is zero and the numerator is non-zero: $x = 1$ and $x = -1$.
- **Horizontal asymptote:** Evaluate $\lim_{x \to \pm\infty} f(x)$.

$$
\lim_{x \to \pm\infty} \frac{x^{2}+1}{x^{2}-1}
= \lim_{x \to \pm\infty} \frac{1 + \frac{1}{x^{2}}}{1 - \frac{1}{x^{2}}}
= \frac{1+0}{1-0} = 1.
$$

Thus $y = 1$ is a horizontal asymptote in both directions.

**Answer:** Vertical asymptotes: $x = -1$ and $x = 1$. Horizontal asymptote: $y = 1$.

---

## Problem 23
Use partial fractions to evaluate $\displaystyle\int \frac{x^{3} + 2x^{2} + 2x + 1}{(x^{2}+1)^{2}}\,dx$. Write the integrand as $\dfrac{Ax+B}{x^{2}+1} + \dfrac{Cx+D}{(x^{2}+1)^{2}}$.

**Step 1 — Set up the decomposition:**
$$
\frac{x^{3}+2x^{2}+2x+1}{(x^{2}+1)^{2}} = \frac{Ax+B}{x^{2}+1} + \frac{Cx+D}{(x^{2}+1)^{2}}.
$$

Multiply through by $(x^{2}+1)^{2}$:
$$
x^{3}+2x^{2}+2x+1 = (Ax+B)(x^{2}+1) + (Cx+D).
$$

**Step 2 — Expand and equate coefficients:**
$$
(Ax+B)(x^{2}+1) + Cx + D = Ax^{3} + Ax + Bx^{2} + B + Cx + D
$$
$$
= Ax^{3} + Bx^{2} + (A+C)x + (B+D).
$$

Equate with $x^{3} + 2x^{2} + 2x + 1$:
- $x^{3}$: $A = 1$
- $x^{2}$: $B = 2$
- $x^{1}$: $A + C = 2 \;\Longrightarrow\; 1 + C = 2 \;\Longrightarrow\; C = 1$
- $x^{0}$: $B + D = 1 \;\Longrightarrow\; 2 + D = 1 \;\Longrightarrow\; D = -1$

Thus
$$
\frac{x^{3}+2x^{2}+2x+1}{(x^{2}+1)^{2}} = \frac{x+2}{x^{2}+1} + \frac{x-1}{(x^{2}+1)^{2}}.
$$

**Step 3 — Integrate each term.**

**Term 1:** $\displaystyle\int\frac{x+2}{x^{2}+1}\,dx = \int\frac{x}{x^{2}+1}\,dx + 2\int\frac{1}{x^{2}+1}\,dx$.

- $\int\frac{x}{x^{2}+1}\,dx$: let $u = x^{2}+1$, $du = 2x\,dx$, so this is $\frac{1}{2}\ln(x^{2}+1)$.
- $2\int\frac{1}{x^{2}+1}\,dx = 2\arctan x$.

**Term 2:** $\displaystyle\int\frac{x-1}{(x^{2}+1)^{2}}\,dx = \int\frac{x}{(x^{2}+1)^{2}}\,dx - \int\frac{1}{(x^{2}+1)^{2}}\,dx$.

- $\int\frac{x}{(x^{2}+1)^{2}}\,dx$: let $u = x^{2}+1$, $du = 2x\,dx$, so $\int x(x^{2}+1)^{-2}\,dx = \frac{1}{2}\int u^{-2}\,du = \frac{1}{2}(-u^{-1}) = -\frac{1}{2(x^{2}+1)}$.

- $\int\frac{1}{(x^{2}+1)^{2}}\,dx$: use the reduction formula or the substitution $x = \tan\theta$. With $x = \tan\theta$, $dx = \sec^{2}\theta\,d\theta$, and $(x^{2}+1)^{2} = \sec^{4}\theta$. Then $\int\frac{1}{(x^{2}+1)^{2}}\,dx = \int\frac{\sec^{2}\theta}{\sec^{4}\theta}\,d\theta = \int\cos^{2}\theta\,d\theta = \int\frac{1+\cos(2\theta)}{2}\,d\theta = \frac{\theta}{2} + \frac{\sin(2\theta)}{4} = \frac{\theta}{2} + \frac{\sin\theta\cos\theta}{2}$.

Now $\theta = \arctan x$, $\sin\theta = \frac{x}{\sqrt{1+x^{2}}}$, $\cos\theta = \frac{1}{\sqrt{1+x^{2}}}$. So $\sin\theta\cos\theta = \frac{x}{1+x^{2}}$. Thus
$$
\int\frac{1}{(x^{2}+1)^{2}}\,dx = \frac{1}{2}\arctan x + \frac{x}{2(1+x^{2})} + C.
$$

**Step 4 — Combine all parts:**
$$
\int f(x)\,dx = \frac{1}{2}\ln(x^{2}+1) + 2\arctan x + \left(-\frac{1}{2(x^{2}+1)}\right) - \left(\frac{1}{2}\arctan x + \frac{x}{2(x^{2}+1)}\right) + C
$$
$$
= \frac{1}{2}\ln(x^{2}+1) + \left(2 - \frac{1}{2}\right)\arctan x - \frac{1+x}{2(x^{2}+1)} + C
$$
$$
= \frac{1}{2}\ln(x^{2}+1) + \frac{3}{2}\arctan x - \frac{x+1}{2(x^{2}+1)} + C.
$$

**Answer:** $\displaystyle\int \frac{x^{3}+2x^{2}+2x+1}{(x^{2}+1)^{2}}\,dx = \frac{1}{2}\ln(x^{2}+1) + \frac{3}{2}\arctan x - \frac{x+1}{2(x^{2}+1)} + C$.

---

## Problem 24
A particle moves along a curve defined implicitly by $\sin(xy) = x + y$, where $(x, y)$ depend on time $t$.

**(a) Find $\dfrac{dy}{dx}$ in terms of $x$ and $y$.**

**Approach:** Differentiate implicitly with respect to $x$.

$$
\frac{d}{dx}\bigl(\sin(xy)\bigr) = \frac{d}{dx}(x + y).
$$

Left side: $\cos(xy) \cdot \frac{d}{dx}(xy) = \cos(xy)\!\left(y + x\frac{dy}{dx}\right)$.

Right side: $1 + \frac{dy}{dx}$.

Thus:
$$
\cos(xy)\!\left(y + x\frac{dy}{dx}\right) = 1 + \frac{dy}{dx}.
$$

Expand:
$$
y\cos(xy) + x\cos(xy)\frac{dy}{dx} = 1 + \frac{dy}{dx}.
$$

Collect $\frac{dy}{dx}$ terms:
$$
x\cos(xy)\frac{dy}{dx} - \frac{dy}{dx} = 1 - y\cos(xy),
$$
$$
\frac{dy}{dx}\bigl(x\cos(xy) - 1\bigr) = 1 - y\cos(xy),
$$
$$
\frac{dy}{dx} = \frac{1 - y\cos(xy)}{x\cos(xy) - 1}.
$$

**Answer:** $\displaystyle\frac{dy}{dx} = \frac{1 - y\cos(xy)}{x\cos(xy) - 1}$.

---

**(b) At the instant when $x=0$ and $y=0$, the $x$-coordinate is increasing at $2$ units per second. Find the rate at which the $y$-coordinate is changing.**

**Approach:** Use the chain rule $\frac{dy}{dt} = \frac{dy}{dx} \cdot \frac{dx}{dt}$. First evaluate $\frac{dy}{dx}$ at $(0,0)$.

At $(0,0)$: $\cos(0\cdot 0) = \cos(0) = 1$.
$$
\frac{dy}{dx}\Bigr|_{(0,0)} = \frac{1 - 0\cdot 1}{0\cdot 1 - 1} = \frac{1}{-1} = -1.
$$

Given $\frac{dx}{dt} = 2$:
$$
\frac{dy}{dt} = \frac{dy}{dx} \cdot \frac{dx}{dt} = (-1) \cdot 2 = -2.
$$

**Answer:** The $y$-coordinate is decreasing at $2$ units per second ($\frac{dy}{dt} = -2$).

---

## Problem 25
Prove the reduction formula $\displaystyle\int \cos^{n}x\,dx = \frac{1}{n}\cos^{n-1}x\sin x + \frac{n-1}{n}\int \cos^{n-2}x\,dx$ for integers $n \geq 2$. Hence evaluate $\displaystyle\int_{0}^{\pi/2} \cos^{4}x\,dx$.

**(a) Prove the reduction formula.**

**Approach:** Write $\cos^{n}x = \cos^{n-1}x \cdot \cos x$ and apply integration by parts.

Let $I_{n} = \int \cos^{n}x\,dx$. Write $I_{n} = \int \cos^{n-1}x \cdot \cos x\,dx$.

Set $u = \cos^{n-1}x$, $dv = \cos x\,dx$.

Then $du = (n-1)\cos^{n-2}x \cdot (-\sin x)\,dx = -(n-1)\cos^{n-2}x\sin x\,dx$, and $v = \sin x$.

Apply integration by parts:
$$
I_{n} = \cos^{n-1}x\sin x - \int \sin x \cdot \bigl(-(n-1)\cos^{n-2}x\sin x\bigr)\,dx
$$
$$
= \cos^{n-1}x\sin x + (n-1)\int \cos^{n-2}x\sin^{2}x\,dx.
$$

Replace $\sin^{2}x$ with $1 - \cos^{2}x$:
$$
I_{n} = \cos^{n-1}x\sin x + (n-1)\int \cos^{n-2}x\,(1 - \cos^{2}x)\,dx
$$
$$
= \cos^{n-1}x\sin x + (n-1)\int \cos^{n-2}x\,dx - (n-1)\int \cos^{n}x\,dx.
$$

The first remaining integral is $I_{n-2}$ and the last is $I_{n}$:
$$
I_{n} = \cos^{n-1}x\sin x + (n-1)I_{n-2} - (n-1)I_{n}.
$$

Bring $(n-1)I_{n}$ to the left:
$$
I_{n} + (n-1)I_{n} = \cos^{n-1}x\sin x + (n-1)I_{n-2},
$$
$$
nI_{n} = \cos^{n-1}x\sin x + (n-1)I_{n-2},
$$
$$
I_{n} = \frac{1}{n}\cos^{n-1}x\sin x + \frac{n-1}{n}I_{n-2}.
$$

This proves the reduction formula. $\square$

---

**(b) Evaluate $\displaystyle\int_{0}^{\pi/2} \cos^{4}x\,dx$.**

**Approach:** Apply the reduction formula repeatedly.

Let $J_{n} = \int_{0}^{\pi/2} \cos^{n}x\,dx$. Using the reduction formula with definite limits:

For $n \geq 2$:
$$
J_{n} = \Bigl[\frac{1}{n}\cos^{n-1}x\sin x\Bigr]_{0}^{\pi/2} + \frac{n-1}{n}J_{n-2}.
$$

At $x = \frac{\pi}{2}$, $\cos\frac{\pi}{2} = 0$, so the boundary term vanishes. At $x = 0$, $\sin 0 = 0$, so it also vanishes. Thus for all $n \geq 2$:
$$
J_{n} = \frac{n-1}{n}\,J_{n-2}.
$$

Now compute $J_{4}$:
$$
J_{4} = \frac{3}{4}J_{2}.
$$

$$
J_{2} = \frac{1}{2}J_{0}.
$$

$$
J_{0} = \int_{0}^{\pi/2} \cos^{0}x\,dx = \int_{0}^{\pi/2} 1\,dx = \frac{\pi}{2}.
$$

Working backwards:
$$
J_{2} = \frac{1}{2} \cdot \frac{\pi}{2} = \frac{\pi}{4},
$$
$$
J_{4} = \frac{3}{4} \cdot \frac{\pi}{4} = \frac{3\pi}{16}.
$$

**Answer:** $\displaystyle\int_{0}^{\pi/2} \cos^{4}x\,dx = \frac{3\pi}{16}$.

*Pitfall:* The boundary term $\frac{1}{n}\cos^{n-1}x\sin x$ vanishes at both $0$ and $\frac{\pi}{2}$ for all $n \geq 2$, which greatly simplifies definite integrals on $[0, \frac{\pi}{2}]$.
