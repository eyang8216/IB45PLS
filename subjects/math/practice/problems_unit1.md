# Unit 1: Calculus Foundations — Practice Problems

## Problem 1
A function $f$ is defined by

$$
f(x) = \begin{cases}
\dfrac{\sin(3x)}{x}, & x \neq 0,\\[6pt]
k, & x = 0,
\end{cases}
$$

where $k$ is a real constant.

(a) Evaluate $\displaystyle\lim_{x \to 0} f(x)$.

(b) Hence determine the value of $k$ for which $f$ is continuous at $x = 0$.

(c) For the value of $k$ found in part (b), state whether $f$ is differentiable at $x = 0$. Justify your answer.

## Problem 2
Consider the limit

$$
L = \lim_{x \to 0} \frac{e^{2x} - 1 - 2x}{x^2}.
$$

(a) Explain why direct substitution yields an indeterminate form, and state the type of indeterminate form.

(b) Use L'Hôpital's rule to evaluate $L$.

(c) Verify your result by using the Maclaurin series for $e^{2x}$ up to and including the term in $x^2$.

## Problem 3
A curve is defined implicitly by the equation

$$
x^3 + y^3 = 6xy.
$$

(a) Find an expression for $\dfrac{dy}{dx}$ in terms of $x$ and $y$.

(b) Find the coordinates of all points on the curve at which the tangent is horizontal.

## Problem 4
Use integration by parts to evaluate

$$
\int x^2 e^x\,dx.
$$

Give your answer in its simplest factored form.

## Problem 5
Evaluate

$$
\int \ln(x^2 + 1)\,dx.
$$

You may use the standard integral $\displaystyle\int \frac{1}{x^2 + 1}\,dx = \arctan x + C$.

## Problem 6
Use the method of partial fractions to show that

$$
\int \frac{3x^2 + 5x + 2}{x^3 + x^2 + x + 1}\,dx = \ln\left|(x + 1)^2\sqrt{x^2 + 1}\right| + C.
$$

You should begin by factorising the denominator completely.

## Problem 7
A spherical balloon is being inflated at a rate of $100\,\text{cm}^3\,\text{s}^{-1}$.

(a) Write down an expression for the volume $V$ of the balloon in terms of its radius $r$.

(b) Find the rate at which the radius is increasing when the radius is $10\,\text{cm}$.

(c) Find the rate at which the surface area is increasing at the instant when the radius is $10\,\text{cm}$.

## Problem 8
Consider the limit

$$
\lim_{x \to \infty} \frac{\ln x}{\sqrt{x}}.
$$

(a) State the type of indeterminate form.

(b) Use L'Hôpital's rule to evaluate the limit.

(c) Comment on what this limit tells you about the relative growth rates of $\ln x$ and $\sqrt{x}$ as $x \to \infty$.

## Problem 9
A curve is defined by the parametric equations

$$
x = t^2 + 2t,\qquad y = t^3 - 3t,
$$

where $t \in \mathbb{R}$.

(a) Find $\dfrac{dy}{dx}$ in terms of $t$.

(b) Determine the coordinates of the points on the curve where the tangent is parallel to the $x$-axis.

(c) Find the equation of the tangent to the curve at the point where $t = 1$, giving your answer in the form $ax + by + c = 0$.

## Problem 10
Evaluate

$$
\int_{0}^{\pi/2} e^x \cos x\,dx.
$$

Use integration by parts twice and solve for the original integral.

## Problem 11
A function $g$ is defined by

$$
g(x) = \begin{cases}
\dfrac{x^2 - 4}{x - 2}, & x < 2,\\[6pt]
ax + b, & 2 \leq x \leq 3,\\[6pt]
\dfrac{\sqrt{x} - \sqrt{3}}{x - 3}, & x > 3,
\end{cases}
$$

where $a$ and $b$ are real constants.

(a) Find $\displaystyle\lim_{x \to 2^{-}} g(x)$.

(b) Find $\displaystyle\lim_{x \to 3^{+}} g(x)$.

(c) Determine the values of $a$ and $b$ such that $g$ is continuous on $\mathbb{R}$.

## Problem 12
Use the substitution $x = \sin\theta$, where $-\frac{\pi}{2} \leq \theta \leq \frac{\pi}{2}$, to evaluate

$$
\int_{0}^{1/2} \frac{x^2}{\sqrt{1 - x^2}}\,dx.
$$

## Problem 13
A water tank has the shape of an inverted right circular cone with height $4\,\text{m}$ and base radius $2\,\text{m}$. Water is being pumped into the tank at a constant rate of $0.5\,\text{m}^3\,\text{min}^{-1}$.

(a) Express the volume $V$ of water in the tank in terms of the height $h$ of the water level.

(b) Find the rate at which the water level is rising when the water is $1\,\text{m}$ deep.

(c) If the tank is initially empty, how long will it take to fill the tank completely? Give your answer in minutes, correct to one decimal place.

## Problem 14
Evaluate the following integrals:

(a) $\displaystyle\int \tan^3 x\,dx$

(b) $\displaystyle\int \frac{\sin x}{\cos^2 x}\,dx$

(c) $\displaystyle\int_{0}^{\pi/4} \sec^4 x\,dx$

## Problem 15
Consider the limit

$$
\lim_{x \to 0} \left(\frac{1}{\sin x} - \frac{1}{x}\right).
$$

(a) Show that this limit can be rewritten as a single fraction whose numerator and denominator both approach $0$ as $x \to 0$.

(b) Use L'Hôpital's rule to evaluate the limit. You may need to apply the rule more than once.

## Problem 16
A ladder of length $5\,\text{m}$ leans against a vertical wall. The bottom of the ladder slides away from the wall along horizontal ground at a constant speed of $0.3\,\text{m}\,\text{s}^{-1}$. At time $t = 0$, the bottom of the ladder is $3\,\text{m}$ from the wall.

(a) Express the height $y$ (in metres) of the top of the ladder above the ground in terms of the distance $x$ (in metres) of the bottom from the wall.

(b) Find the rate at which the top of the ladder is sliding down the wall when the bottom is $3\,\text{m}$ from the wall.

(c) Determine whether the top of the ladder is accelerating or decelerating at this instant. Justify your answer.

## Problem 17
Prove that

$$
\int x^n \ln x\,dx = \frac{x^{n+1}}{(n+1)^2}\Big((n+1)\ln x - 1\Big) + C,
$$

where $n$ is a positive integer, using integration by parts.

## Problem 18
Decompose the rational function

$$
f(x) = \frac{5x^2 + 2x + 1}{(x - 1)(x^2 + x + 1)}
$$

into partial fractions of the form

$$
\frac{A}{x - 1} + \frac{Bx + C}{x^2 + x + 1}.
$$

Hence evaluate $\displaystyle\int f(x)\,dx$.

## Problem 19
Consider the limit

$$
\lim_{x \to 0} (1 + \sin x)^{1/x}.
$$

(a) By taking the natural logarithm of the expression, show that evaluating this limit is equivalent to finding $\displaystyle\exp\left(\lim_{x \to 0} \frac{\ln(1 + \sin x)}{x}\right)$.

(b) Use L'Hôpital's rule to evaluate the inner limit.

(c) Hence state the value of the original limit.

## Problem 20
A curve is defined implicitly by

$$
e^{xy} + x^2 - y^2 = 0.
$$

(a) Show that $\dfrac{dy}{dx} = \dfrac{2x + ye^{xy}}{2y - xe^{xy}}$.

(b) Find the gradient of the curve at the point $(0, 1)$.

(c) Determine the equation of the tangent to the curve at the point $(0, 1)$.

## Problem 21
Evaluate the following integrals using integration by parts:

(a) $\displaystyle\int \arctan x\,dx$

(b) $\displaystyle\int x \sec^2 x\,dx$

(c) $\displaystyle\int (\ln x)^2\,dx$

## Problem 22
A function $f$ is defined for all real $x$ by $f(x) = \dfrac{x^2 + 1}{x^2 - 1}$, except where the denominator vanishes.

(a) Find all values of $x$ for which $f$ is discontinuous.

(b) For each point of discontinuity, evaluate the left-hand and right-hand limits and classify the type of discontinuity.

(c) Determine the equations of all vertical and horizontal asymptotes of the graph of $y = f(x)$.

## Problem 23
Use the method of partial fractions to evaluate

$$
\int \frac{x^3 + 2x^2 + 2x + 1}{(x^2 + 1)^2}\,dx.
$$

Begin by writing the integrand in the form $\dfrac{Ax + B}{x^2 + 1} + \dfrac{Cx + D}{(x^2 + 1)^2}$.

## Problem 24
A particle moves along a curve defined implicitly by the equation

$$
\sin(xy) = x + y,
$$

where the coordinates $(x, y)$ depend on time $t$.

(a) Find $\dfrac{dy}{dx}$ in terms of $x$ and $y$.

(b) At the instant when $x = 0$ and $y = 0$, the $x$-coordinate is increasing at a rate of $2$ units per second. Find the rate at which the $y$-coordinate is changing at this instant.

## Problem 25
Prove the reduction formula

$$
\int \cos^n x\,dx = \frac{1}{n}\cos^{n-1}x\sin x + \frac{n-1}{n}\int \cos^{n-2}x\,dx
$$

for integers $n \geq 2$, using integration by parts.

Hence evaluate $\displaystyle\int_{0}^{\pi/2} \cos^4 x\,dx$.
