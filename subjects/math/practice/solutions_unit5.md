# Unit 5: Vectors & Matrices — Solutions

---

## Problem 1

**Approach:** Use the dot product formula \(\mathbf{a}\cdot\mathbf{b} = a_1b_1 + a_2b_2 + a_3b_3\) and the angle formula \(\cos\theta = \frac{\mathbf{a}\cdot\mathbf{b}}{|\mathbf{a}||\mathbf{b}|}\).

**(a)** With \(\mathbf{a} = (3,-2,1)\) and \(\mathbf{b} = (-1,4,2)\):

\[
\mathbf{a}\cdot\mathbf{b} = 3(-1) + (-2)(4) + 1(2) = -3 - 8 + 2 = -9
\]

**(b)** Magnitudes:

\[
|\mathbf{a}| = \sqrt{3^2 + (-2)^2 + 1^2} = \sqrt{9+4+1} = \sqrt{14}
\]
\[
|\mathbf{b}| = \sqrt{(-1)^2 + 4^2 + 2^2} = \sqrt{1+16+4} = \sqrt{21}
\]

Then

\[
\cos\theta = \frac{-9}{\sqrt{14}\sqrt{21}} = \frac{-9}{\sqrt{294}} = \frac{-9}{7\sqrt{6}}
\]

\[
\theta = \arccos\!\left(\frac{-9}{7\sqrt{6}}\right) \approx 121.66^\circ
\]

**Answer:** (a) \(\mathbf{a}\cdot\mathbf{b} = -9\); (b) \(\theta \approx 121.7^\circ\)

---

## Problem 2

**Approach:** Compute the cross product using the determinant formula, verify orthogonality via dot products, then normalize.

**(a)** \(\mathbf{u} = (2,1,-3)\), \(\mathbf{v} = (1,-2,4)\).

\[
\mathbf{u}\times\mathbf{v} =
\begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
2 & 1 & -3 \\
1 & -2 & 4
\end{vmatrix}
\]

\[
= \mathbf{i}\bigl(1\cdot 4 - (-3)(-2)\bigr) - \mathbf{j}\bigl(2\cdot 4 - (-3)(1)\bigr) + \mathbf{k}\bigl(2(-2) - 1\cdot 1\bigr)
\]
\[
= \mathbf{i}(4-6) - \mathbf{j}(8+3) + \mathbf{k}(-4-1) = -2\mathbf{i} - 11\mathbf{j} - 5\mathbf{k}
\]

So \(\mathbf{u}\times\mathbf{v} = (-2,-11,-5)\).

**(b)** Verify orthogonality:

\[
\mathbf{u}\cdot(\mathbf{u}\times\mathbf{v}) = 2(-2) + 1(-11) + (-3)(-5) = -4 - 11 + 15 = 0 \;\checkmark
\]
\[
\mathbf{v}\cdot(\mathbf{u}\times\mathbf{v}) = 1(-2) + (-2)(-11) + 4(-5) = -2 + 22 - 20 = 0 \;\checkmark
\]

Both dot products are zero, confirming \(\mathbf{u}\times\mathbf{v}\) is orthogonal to both \(\mathbf{u}\) and \(\mathbf{v}\).

**(c)** Magnitude of the cross product:

\[
|\mathbf{u}\times\mathbf{v}| = \sqrt{(-2)^2 + (-11)^2 + (-5)^2} = \sqrt{4+121+25} = \sqrt{150} = 5\sqrt{6}
\]

A unit vector is:

\[
\frac{\mathbf{u}\times\mathbf{v}}{|\mathbf{u}\times\mathbf{v}|} = \left(\frac{-2}{5\sqrt{6}},\; \frac{-11}{5\sqrt{6}},\; \frac{-5}{5\sqrt{6}}\right)
\]

**Answer:** (a) \(\mathbf{u}\times\mathbf{v} = -2\mathbf{i} - 11\mathbf{j} - 5\mathbf{k}\); (b) Verified; (c) \(\displaystyle\frac{1}{5\sqrt{6}}(-2,-11,-5)\)

---

## Problem 3

**Approach:** The area of triangle \(ABC\) is half the magnitude of the cross product of two side vectors.

\[
\overrightarrow{AB} = B - A = (4-1,\;0-2,\;-1-3) = (3,-2,-4)
\]
\[
\overrightarrow{AC} = C - A = (2-1,\;5-2,\;1-3) = (1,3,-2)
\]

\[
\overrightarrow{AB}\times\overrightarrow{AC} =
\begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
3 & -2 & -4 \\
1 & 3 & -2
\end{vmatrix}
\]

\[
= \mathbf{i}\bigl((-2)(-2)-(-4)(3)\bigr) - \mathbf{j}\bigl(3(-2)-(-4)(1)\bigr) + \mathbf{k}\bigl(3\cdot 3 - (-2)(1)\bigr)
\]
\[
= \mathbf{i}(4+12) - \mathbf{j}(-6+4) + \mathbf{k}(9+2) = 16\mathbf{i} + 2\mathbf{j} + 11\mathbf{k}
\]

\[
|\overrightarrow{AB}\times\overrightarrow{AC}| = \sqrt{16^2 + 2^2 + 11^2} = \sqrt{256+4+121} = \sqrt{381}
\]

\[
\text{Area} = \frac{1}{2}\sqrt{381}
\]

**Answer:** \(\displaystyle\frac{\sqrt{381}}{2}\) square units

---

## Problem 4

**Approach:** Use the point \(P\) and direction vector \(\mathbf{d}\) to write the line in vector, parametric, and Cartesian forms.

**(a)** Vector equation: \(\mathbf{r} = (2,-1,5) + t(3,-1,2),\; t \in \mathbb{R}\).

**(b)** Parametric equations:
\[
x = 2 + 3t,\quad y = -1 - t,\quad z = 5 + 2t
\]

**(c)** Solve each parametric equation for \(t\) and equate:
\[
t = \frac{x-2}{3} = \frac{y+1}{-1} = \frac{z-5}{2}
\]

**Answer:** (a) \(\mathbf{r} = (2,-1,5) + t(3,-1,2)\); (b) \(x=2+3t,\; y=-1-t,\; z=5+2t\); (c) \(\displaystyle\frac{x-2}{3} = \frac{y+1}{-1} = \frac{z-5}{2}\)

---

## Problem 5

**Approach:** Find the direction vector from \(A\) to \(B\), then write parametric and Cartesian forms.

**(a)** Direction vector:
\[
\overrightarrow{AB} = B - A = (5-1,\;-1-3,\;4-(-2)) = (4,-4,6)
\]
This can be simplified by dividing by 2: \(\mathbf{d} = (2,-2,3)\).

**(b)** Parametric equations (using \(A\) and simplified \(\mathbf{d}\)):
\[
x = 1 + 2t,\quad y = 3 - 2t,\quad z = -2 + 3t,\quad t \in \mathbb{R}
\]

**(c)** Cartesian form:
\[
\frac{x-1}{2} = \frac{y-3}{-2} = \frac{z+2}{3}
\]

**Answer:** (a) \(\overrightarrow{AB} = (4,-4,6)\); (b) \(x=1+2t,\;y=3-2t,\;z=-2+3t\); (c) \(\displaystyle\frac{x-1}{2} = \frac{y-3}{-2} = \frac{z+2}{3}\)

---

## Problem 6

**Approach:** Compare direction vectors; if parallel, check whether a point on one line lies on the other.

Direction vectors: \(\mathbf{d}_1 = (2,-1,3)\) for \(L_1\), \(\mathbf{d}_2 = (-4,2,-6)\) for \(L_2\).

Observe that \(\mathbf{d}_2 = -2\mathbf{d}_1\), so the lines are parallel (or coincident).

Now check whether the point \((1,0,2)\) on \(L_1\) lies on \(L_2\). Set:

\[
(1,0,2) = (3,-1,5) + \mu(-4,2,-6)
\]

This gives three equations:
\[
\begin{aligned}
1 &= 3 - 4\mu \;\Rightarrow\; \mu = \tfrac{1}{2} \\
0 &= -1 + 2\mu \;\Rightarrow\; \mu = \tfrac{1}{2} \\
2 &= 5 - 6\mu \;\Rightarrow\; \mu = \tfrac{1}{2}
\end{aligned}
\]

All three equations give \(\mu = \frac{1}{2}\), which is consistent. Hence \((1,0,2)\) lies on \(L_2\), and the lines are identical.

**Answer:** The lines are the same line (coincident).

---

## Problem 7

**Approach:** Convert each line to parametric form; compare direction vectors to check parallelism; then attempt to solve for an intersection point.

**(a)** Direction vectors: \(\mathbf{d}_1 = (2,-1,4)\) for \(L_1\), \(\mathbf{d}_2 = (-1,2,2)\) for \(L_2\).

For parallelism we need \(\mathbf{d}_2 = k\mathbf{d}_1\). Check:
\[
(-1,2,2) = k(2,-1,4) \;\Rightarrow\; k = -\tfrac{1}{2},\; k = -2,\; k = \tfrac{1}{2}
\]
These are inconsistent, so \(L_1\) and \(L_2\) are **not parallel**.

**(b)** Parametric forms:
\[
L_1:\; x = 1+2\lambda,\; y = -3-\lambda,\; z = 2+4\lambda
\]
\[
L_2:\; x = 4-\mu,\; y = 1+2\mu,\; z = -1+2\mu
\]

Set coordinates equal:
\[
\begin{aligned}
1+2\lambda &= 4-\mu \quad &\Rightarrow&\quad 2\lambda + \mu = 3 \quad &\text{(1)}\\
-3-\lambda &= 1+2\mu \quad &\Rightarrow&\quad -\lambda - 2\mu = 4 \quad &\text{(2)}\\
2+4\lambda &= -1+2\mu \quad &\Rightarrow&\quad 4\lambda - 2\mu = -3 \quad &\text{(3)}
\end{aligned}
\]

From (1) and (3):
\[
\begin{cases}
2\lambda + \mu = 3 \\
4\lambda - 2\mu = -3
\end{cases}
\]

Multiply (1) by 2: \(4\lambda + 2\mu = 6\). Add to (3): \(8\lambda = 3 \;\Rightarrow\; \lambda = \frac{3}{8}\).

Then \(\mu = 3 - 2(\frac{3}{8}) = 3 - \frac{3}{4} = \frac{9}{4}\).

Check in equation (2):
\[
\lambda + 2\mu = \frac{3}{8} + 2\!\left(\frac{9}{4}\right) = \frac{3}{8} + \frac{18}{4} = \frac{3}{8} + \frac{36}{8} = \frac{39}{8}
\]
But equation (2) requires \(\lambda + 2\mu = -4 = -\frac{32}{8}\), and \(\frac{39}{8} \neq -\frac{32}{8}\).

The system is inconsistent. The lines do **not** intersect; they are skew.

**Answer:** (a) Not parallel (direction vectors are not scalar multiples). (b) The lines do not intersect — they are skew.

---

## Problem 8

**Approach:** Substitute the parametric equations of the line into the Cartesian equation of the plane and solve for the parameter.

Line: \(x = 2+t,\; y = -1+2t,\; z = 3-t\).

Plane: \(2x - y + 3z = 10\).

Substitute:
\[
2(2+t) - (-1+2t) + 3(3-t) = 10
\]
\[
4 + 2t + 1 - 2t + 9 - 3t = 10
\]
\[
14 - 3t = 10 \;\Rightarrow\; -3t = -4 \;\Rightarrow\; t = \frac{4}{3}
\]

Intersection point:
\[
x = 2 + \tfrac{4}{3} = \tfrac{10}{3},\quad y = -1 + 2\!\left(\tfrac{4}{3}\right) = \tfrac{5}{3},\quad z = 3 - \tfrac{4}{3} = \tfrac{5}{3}
\]

**Answer:** \(\displaystyle\left(\frac{10}{3},\; \frac{5}{3},\; \frac{5}{3}\right)\)

---

## Problem 9

**Approach:** The direction of the intersection line is \(\mathbf{n}_1 \times \mathbf{n}_2\). Find a point by setting one variable to zero and solving the resulting system.

**(a)** Normals: \(\mathbf{n}_1 = (1,2,-1)\), \(\mathbf{n}_2 = (2,-1,3)\).

\[
\mathbf{n}_1 \times \mathbf{n}_2 =
\begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
1 & 2 & -1 \\
2 & -1 & 3
\end{vmatrix}
\]

\[
= \mathbf{i}(2\cdot 3 - (-1)(-1)) - \mathbf{j}(1\cdot 3 - (-1)(2)) + \mathbf{k}(1(-1) - 2\cdot 2)
\]
\[
= \mathbf{i}(6-1) - \mathbf{j}(3+2) + \mathbf{k}(-1-4) = 5\mathbf{i} - 5\mathbf{j} - 5\mathbf{k}
\]

Direction vector: \((5,-5,-5)\), which simplifies to \((1,-1,-1)\).

**(b)** Set \(z = 0\) in both plane equations:
\[
\begin{cases}
x + 2y = 4 \\
2x - y = 1
\end{cases}
\]

From the second: \(y = 2x - 1\). Substitute into the first:
\[
x + 2(2x-1) = 4 \;\Rightarrow\; x + 4x - 2 = 4 \;\Rightarrow\; 5x = 6 \;\Rightarrow\; x = \tfrac{6}{5}
\]
\[
y = 2\!\left(\tfrac{6}{5}\right) - 1 = \tfrac{12}{5} - 1 = \tfrac{7}{5}
\]

Point on intersection line: \(\left(\frac{6}{5},\;\frac{7}{5},\;0\right)\).

**(c)** Vector equation:
\[
\mathbf{r} = \left(\frac{6}{5},\;\frac{7}{5},\;0\right) + t(1,-1,-1),\quad t \in \mathbb{R}
\]

**Answer:** (a) \((1,-1,-1)\); (b) \(\left(\frac{6}{5},\frac{7}{5},0\right)\); (c) \(\mathbf{r} = \left(\frac{6}{5},\frac{7}{5},0\right) + t(1,-1,-1)\)

---

## Problem 10

**Approach:** Use the point-to-plane distance formula \(d = \frac{|ax_0 + by_0 + cz_0 - d|}{\sqrt{a^2+b^2+c^2}}\) for plane \(ax+by+cz = d\).

Plane: \(2x + y - 2z = 8\), so \(a=2,\;b=1,\;c=-2,\;d=8\).

Point \(P(3,-2,4)\):

\[
\text{Distance} = \frac{|2(3) + 1(-2) + (-2)(4) - 8|}{\sqrt{2^2 + 1^2 + (-2)^2}} = \frac{|6 - 2 - 8 - 8|}{\sqrt{4+1+4}} = \frac{|-12|}{3} = 4
\]

**Answer:** \(4\) units

---

## Problem 11

**Approach:** Perform matrix addition and multiplication directly.

\(A = \begin{pmatrix}2 & -1 \\ 3 & 4\end{pmatrix},\; B = \begin{pmatrix}1 & 5 \\ -2 & 0\end{pmatrix}\).

**(a)** \(A + B = \begin{pmatrix}2+1 & -1+5 \\ 3+(-2) & 4+0\end{pmatrix} = \begin{pmatrix}3 & 4 \\ 1 & 4\end{pmatrix}\)

**(b)** \(AB = \begin{pmatrix}2(1)+(-1)(-2) & 2(5)+(-1)(0) \\ 3(1)+4(-2) & 3(5)+4(0)\end{pmatrix} = \begin{pmatrix}2+2 & 10+0 \\ 3-8 & 15+0\end{pmatrix} = \begin{pmatrix}4 & 10 \\ -5 & 15\end{pmatrix}\)

**(c)** \(BA = \begin{pmatrix}1(2)+5(3) & 1(-1)+5(4) \\ -2(2)+0(3) & -2(-1)+0(4)\end{pmatrix} = \begin{pmatrix}2+15 & -1+20 \\ -4+0 & 2+0\end{pmatrix} = \begin{pmatrix}17 & 19 \\ -4 & 2\end{pmatrix}\)

**(d)** \(AB = \begin{pmatrix}4 & 10 \\ -5 & 15\end{pmatrix}\) while \(BA = \begin{pmatrix}17 & 19 \\ -4 & 2\end{pmatrix}\). They are clearly different, confirming that matrix multiplication is not commutative in general.

**Answer:** (a) \(\begin{pmatrix}3 & 4 \\ 1 & 4\end{pmatrix}\); (b) \(\begin{pmatrix}4 & 10 \\ -5 & 15\end{pmatrix}\); (c) \(\begin{pmatrix}17 & 19 \\ -4 & 2\end{pmatrix}\); (d) \(AB \neq BA\)

---

## Problem 12

**Approach:** Multiply the matrices using the row-by-column rule; state dimensions.

\(C\) is \(2 \times 3\), \(D\) is \(3 \times 2\).

**(a)** \(CD\) is \(2 \times 2\):
\[
CD = \begin{pmatrix}1 & 0 & 2 \\ -1 & 3 & 1\end{pmatrix}
     \begin{pmatrix}2 & -1 \\ 0 & 3 \\ 4 & 1\end{pmatrix}
   = \begin{pmatrix}
     1(2)+0(0)+2(4) & 1(-1)+0(3)+2(1) \\
     -1(2)+3(0)+1(4) & -1(-1)+3(3)+1(1)
     \end{pmatrix}
   = \begin{pmatrix}2+0+8 & -1+0+2 \\ -2+0+4 & 1+9+1\end{pmatrix}
   = \begin{pmatrix}10 & 1 \\ 2 & 11\end{pmatrix}
\]

**(b)** \(DC\) is \(3 \times 3\):
\[
DC = \begin{pmatrix}2 & -1 \\ 0 & 3 \\ 4 & 1\end{pmatrix}
     \begin{pmatrix}1 & 0 & 2 \\ -1 & 3 & 1\end{pmatrix}
   = \begin{pmatrix}
     2(1)+(-1)(-1) & 2(0)+(-1)(3) & 2(2)+(-1)(1) \\
     0(1)+3(-1)    & 0(0)+3(3)    & 0(2)+3(1) \\
     4(1)+1(-1)    & 4(0)+1(3)    & 4(2)+1(1)
     \end{pmatrix}
   = \begin{pmatrix}2+1 & 0-3 & 4-1 \\ 0-3 & 0+9 & 0+3 \\ 4-1 & 0+3 & 8+1\end{pmatrix}
   = \begin{pmatrix}3 & -3 & 3 \\ -3 & 9 & 3 \\ 3 & 3 & 9\end{pmatrix}
\]

**(c)** Dimensions: \(CD\) is \(2 \times 2\); \(DC\) is \(3 \times 3\).

**Answer:** (a) \(CD = \begin{pmatrix}10 & 1 \\ 2 & 11\end{pmatrix}\); (b) \(DC = \begin{pmatrix}3 & -3 & 3 \\ -3 & 9 & 3 \\ 3 & 3 & 9\end{pmatrix}\); (c) \(CD\): \(2 \times 2\), \(DC\): \(3 \times 3\)

---

## Problem 13

**Approach:** Use \(\det\begin{pmatrix}a & b \\ c & d\end{pmatrix} = ad - bc\).

\[
\det(A) = 4(5) - (-3)(2) = 20 + 6 = 26
\]
\[
\det(B) = (-1)(-2) - 6(3) = 2 - 18 = -16
\]

**Answer:** \(\det(A) = 26\); \(\det(B) = -16\)

---

## Problem 14

**Approach:** Expand the \(3\times 3\) determinant along the first row.

\[
M = \begin{pmatrix}2 & -1 & 3 \\ 0 & 4 & 1 \\ -2 & 3 & 5\end{pmatrix}
\]

\[
\begin{aligned}
\det(M) &= 2\begin{vmatrix}4 & 1 \\ 3 & 5\end{vmatrix} - (-1)\begin{vmatrix}0 & 1 \\ -2 & 5\end{vmatrix} + 3\begin{vmatrix}0 & 4 \\ -2 & 3\end{vmatrix} \\[4pt]
&= 2(4\cdot 5 - 1\cdot 3) + 1(0\cdot 5 - 1\cdot(-2)) + 3(0\cdot 3 - 4\cdot(-2)) \\[4pt]
&= 2(20 - 3) + (0 + 2) + 3(0 + 8) \\[4pt]
&= 2(17) + 2 + 3(8) = 34 + 2 + 24 = 60
\end{aligned}
\]

**Answer:** \(\det(M) = 60\)

---

## Problem 15

**Approach:** For \(A = \begin{pmatrix}a & b \\ c & d\end{pmatrix}\), \(A^{-1} = \frac{1}{ad-bc}\begin{pmatrix}d & -b \\ -c & a\end{pmatrix}\).

**(a)** \(A = \begin{pmatrix}3 & 2 \\ 4 & 5\end{pmatrix}\), \(\det(A) = 3(5) - 2(4) = 15 - 8 = 7\).

\[
A^{-1} = \frac{1}{7}\begin{pmatrix}5 & -2 \\ -4 & 3\end{pmatrix}
\]

**(b)** Verify:
\[
AA^{-1} = \frac{1}{7}\begin{pmatrix}3 & 2 \\ 4 & 5\end{pmatrix}\begin{pmatrix}5 & -2 \\ -4 & 3\end{pmatrix}
       = \frac{1}{7}\begin{pmatrix}3(5)+2(-4) & 3(-2)+2(3) \\ 4(5)+5(-4) & 4(-2)+5(3)\end{pmatrix}
\]
\[
= \frac{1}{7}\begin{pmatrix}15-8 & -6+6 \\ 20-20 & -8+15\end{pmatrix}
= \frac{1}{7}\begin{pmatrix}7 & 0 \\ 0 & 7\end{pmatrix}
= \begin{pmatrix}1 & 0 \\ 0 & 1\end{pmatrix} \;\checkmark
\]

**Answer:** (a) \(A^{-1} = \frac{1}{7}\begin{pmatrix}5 & -2 \\ -4 & 3\end{pmatrix}\); (b) Verified.

---

## Problem 16

**Approach:** Compute \(\det(B)\), the cofactor matrix, then the adjugate (transpose of cofactors), and divide by \(\det(B)\).

\[
B = \begin{pmatrix}1 & 2 & 1 \\ 2 & 5 & 2 \\ 1 & 3 & 4\end{pmatrix}
\]

**Step 1 — Determinant** (expanding along row 1):
\[
\begin{aligned}
\det(B) &= 1\begin{vmatrix}5 & 2 \\ 3 & 4\end{vmatrix} - 2\begin{vmatrix}2 & 2 \\ 1 & 4\end{vmatrix} + 1\begin{vmatrix}2 & 5 \\ 1 & 3\end{vmatrix} \\[4pt]
&= 1(20-6) - 2(8-2) + 1(6-5) \\[4pt]
&= 14 - 12 + 1 = 3
\end{aligned}
\]

**Step 2 — Cofactor matrix:**
\[
\begin{aligned}
C_{11} &= +\begin{vmatrix}5 & 2 \\ 3 & 4\end{vmatrix} = 20-6 = 14 &
C_{12} &= -\begin{vmatrix}2 & 2 \\ 1 & 4\end{vmatrix} = -(8-2) = -6 &
C_{13} &= +\begin{vmatrix}2 & 5 \\ 1 & 3\end{vmatrix} = 6-5 = 1 \\[6pt]
C_{21} &= -\begin{vmatrix}2 & 1 \\ 3 & 4\end{vmatrix} = -(8-3) = -5 &
C_{22} &= +\begin{vmatrix}1 & 1 \\ 1 & 4\end{vmatrix} = 4-1 = 3 &
C_{23} &= -\begin{vmatrix}1 & 2 \\ 1 & 3\end{vmatrix} = -(3-2) = -1 \\[6pt]
C_{31} &= +\begin{vmatrix}2 & 1 \\ 5 & 2\end{vmatrix} = 4-5 = -1 &
C_{32} &= -\begin{vmatrix}1 & 1 \\ 2 & 2\end{vmatrix} = -(2-2) = 0 &
C_{33} &= +\begin{vmatrix}1 & 2 \\ 2 & 5\end{vmatrix} = 5-4 = 1
\end{aligned}
\]

Cofactor matrix: \(\begin{pmatrix}14 & -6 & 1 \\ -5 & 3 & -1 \\ -1 & 0 & 1\end{pmatrix}\)

**Step 3 — Adjugate** (transpose of cofactors):
\[
\operatorname{adj}(B) = \begin{pmatrix}14 & -5 & -1 \\ -6 & 3 & 0 \\ 1 & -1 & 1\end{pmatrix}
\]

**Step 4 — Inverse:**
\[
B^{-1} = \frac{1}{3}\begin{pmatrix}14 & -5 & -1 \\ -6 & 3 & 0 \\ 1 & -1 & 1\end{pmatrix}
\]

**Answer:** \(B^{-1} = \dfrac{1}{3}\begin{pmatrix}14 & -5 & -1 \\ -6 & 3 & 0 \\ 1 & -1 & 1\end{pmatrix}\)

---

## Problem 17

**Approach:** Write the augmented matrix and perform Gaussian elimination.

System:
\[
\begin{cases}
x + 2y + z = 5 \\
2x - y + 3z = 1 \\
-x + 4y - z = 7
\end{cases}
\]

Augmented matrix:
\[
\begin{pmatrix}[1 & 2 & 1 & | & 5] \\
[2 & -1 & 3 & | & 1] \\
[-1 & 4 & -1 & | & 7]
\end{pmatrix}
\]

\(R_2 \to R_2 - 2R_1\): \(\begin{pmatrix}0 & -5 & 1 & | & -9\end{pmatrix}\)

\(R_3 \to R_3 + R_1\): \(\begin{pmatrix}0 & 6 & 0 & | & 12\end{pmatrix}\)

\[
\begin{pmatrix}[1 & 2 & 1 & | & 5] \\
[0 & -5 & 1 & | & -9] \\
[0 & 6 & 0 & | & 12]
\end{pmatrix}
\]

From \(R_3\): \(6y = 12 \;\Rightarrow\; y = 2\).

From \(R_2\): \(-5(2) + z = -9 \;\Rightarrow\; -10 + z = -9 \;\Rightarrow\; z = 1\).

From \(R_1\): \(x + 2(2) + 1 = 5 \;\Rightarrow\; x + 5 = 5 \;\Rightarrow\; x = 0\).

**Answer:** \(x = 0,\; y = 2,\; z = 1\)

---

## Problem 18

**Approach:** Write the augmented matrix, reduce to row-echelon form, and classify.

System:
\[
\begin{cases}
x + y + z = 2 \\
2x - y + 3z = 5 \\
3x + 0y + 4z = 7
\end{cases}
\]

Augmented matrix:
\[
\begin{pmatrix}[1 & 1 & 1 & | & 2] \\
[2 & -1 & 3 & | & 5] \\
[3 & 0 & 4 & | & 7]
\end{pmatrix}
\]

\(R_2 \to R_2 - 2R_1\): \(\begin{pmatrix}0 & -3 & 1 & | & 1\end{pmatrix}\)

\(R_3 \to R_3 - 3R_1\): \(\begin{pmatrix}0 & -3 & 1 & | & 1\end{pmatrix}\)

\[
\begin{pmatrix}[1 & 1 & 1 & | & 2] \\
[0 & -3 & 1 & | & 1] \\
[0 & -3 & 1 & | & 1]
\end{pmatrix}
\]

\(R_3 \to R_3 - R_2\): \(\begin{pmatrix}0 & 0 & 0 & | & 0\end{pmatrix}\)

The system reduces to two independent equations in three unknowns, so there are **infinitely many solutions**.

From \(R_2\): \(-3y + z = 1 \;\Rightarrow\; z = 3y + 1\).

From \(R_1\): \(x + y + (3y+1) = 2 \;\Rightarrow\; x + 4y = 1 \;\Rightarrow\; x = 1 - 4y\).

Let \(y = t\) (free parameter). Then:
\[
x = 1 - 4t,\quad y = t,\quad z = 3t + 1,\quad t \in \mathbb{R}
\]

**Answer:** Infinitely many solutions: \((x,y,z) = (1-4t,\;t,\;3t+1),\; t \in \mathbb{R}\)

---

## Problem 19

**Approach:** Write the augmented matrix and perform row reduction.

System:
\[
\begin{cases}
x + 2y - z = 3 \\
2x + 4y - 2z = 7 \\
-x - 2y + z = 1
\end{cases}
\]

Augmented matrix:
\[
\begin{pmatrix}[1 & 2 & -1 & | & 3] \\
[2 & 4 & -2 & | & 7] \\
[-1 & -2 & 1 & | & 1]
\end{pmatrix}
\]

\(R_2 \to R_2 - 2R_1\): \(\begin{pmatrix}0 & 0 & 0 & | & 1\end{pmatrix}\)

\(R_3 \to R_3 + R_1\): \(\begin{pmatrix}0 & 0 & 0 & | & 4\end{pmatrix}\)

\[
\begin{pmatrix}[1 & 2 & -1 & | & 3] \\
[0 & 0 & 0 & | & 1] \\
[0 & 0 & 0 & | & 4]
\end{pmatrix}
\]

Row 2 states \(0 = 1\) and row 3 states \(0 = 4\). Both are contradictions. The system is **inconsistent** and has **no solution**.

**Answer:** No solution (inconsistent system).

---

## Problem 20

**Approach:** Orthogonal vectors have zero dot product. Solve for \(k\), compute the cross product, and interpret geometrically.

**(a)** \(\mathbf{a} = (1,k,2)\), \(\mathbf{b} = (k,3,-1)\). Orthogonal means \(\mathbf{a}\cdot\mathbf{b} = 0\):

\[
1(k) + k(3) + 2(-1) = 0 \;\Rightarrow\; k + 3k - 2 = 0 \;\Rightarrow\; 4k = 2 \;\Rightarrow\; k = \tfrac{1}{2}
\]

**(b)** With \(k = \frac{1}{2}\), \(\mathbf{a} = (1,\frac{1}{2},2)\) and \(\mathbf{b} = (\frac{1}{2},3,-1)\).

\[
\mathbf{a}\times\mathbf{b} =
\begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
1 & \frac{1}{2} & 2 \\
\frac{1}{2} & 3 & -1
\end{vmatrix}
\]

\[
= \mathbf{i}\!\left(\tfrac{1}{2}(-1) - 2\cdot 3\right)
  - \mathbf{j}\!\left(1(-1) - 2\cdot \tfrac{1}{2}\right)
  + \mathbf{k}\!\left(1\cdot 3 - \tfrac{1}{2}\cdot \tfrac{1}{2}\right)
\]
\[
= \mathbf{i}\!\left(-\tfrac{1}{2} - 6\right) - \mathbf{j}(-1 - 1) + \mathbf{k}\!\left(3 - \tfrac{1}{4}\right)
\]
\[
= -\tfrac{13}{2}\,\mathbf{i} + 2\,\mathbf{j} + \tfrac{11}{4}\,\mathbf{k}
\]

**(c)** When two vectors are orthogonal, \(\theta = 90^\circ\), so \(|\mathbf{a}\times\mathbf{b}| = |\mathbf{a}||\mathbf{b}|\sin 90^\circ = |\mathbf{a}||\mathbf{b}|\). The magnitude of the cross product equals the product of the magnitudes — it is maximized for given lengths (since \(\sin\theta \le 1\) with equality only at \(90^\circ\)). This represents the area of the rectangle spanned by the two vectors.

**Answer:** (a) \(k = \frac{1}{2}\); (b) \(\mathbf{a}\times\mathbf{b} = -\frac{13}{2}\mathbf{i} + 2\mathbf{j} + \frac{11}{4}\mathbf{k}\); (c) \(|\mathbf{a}\times\mathbf{b}| = |\mathbf{a}||\mathbf{b}|\) — the cross product magnitude is maximized, giving the area of the rectangle defined by the two vectors.

---

## Problem 21

**Approach:** Compute \(\det(M)\) symbolically, find when it is zero, then compute \(M^{-1}\) for a specific \(a\).

**(a)** \(M = \begin{pmatrix}a & 2 \\ 3 & a\end{pmatrix}\).
\[
\det(M) = a\cdot a - 2\cdot 3 = a^2 - 6
\]

**(b)** Singular when \(\det(M) = 0\):
\[
a^2 - 6 = 0 \;\Rightarrow\; a = \pm\sqrt{6}
\]

**(c)** For \(a = 1\): \(M = \begin{pmatrix}1 & 2 \\ 3 & 1\end{pmatrix}\), \(\det(M) = 1 - 6 = -5\).

\[
M^{-1} = \frac{1}{-5}\begin{pmatrix}1 & -2 \\ -3 & 1\end{pmatrix} = \begin{pmatrix}-\frac{1}{5} & \frac{2}{5} \\[4pt] \frac{3}{5} & -\frac{1}{5}\end{pmatrix}
\]

Verify:
\[
MM^{-1} = \begin{pmatrix}1 & 2 \\ 3 & 1\end{pmatrix}
         \begin{pmatrix}-\frac{1}{5} & \frac{2}{5} \\[4pt] \frac{3}{5} & -\frac{1}{5}\end{pmatrix}
       = \begin{pmatrix}
         1\!\left(-\frac{1}{5}\right) + 2\!\left(\frac{3}{5}\right) &
         1\!\left(\frac{2}{5}\right) + 2\!\left(-\frac{1}{5}\right) \\[4pt]
         3\!\left(-\frac{1}{5}\right) + 1\!\left(\frac{3}{5}\right) &
         3\!\left(\frac{2}{5}\right) + 1\!\left(-\frac{1}{5}\right)
         \end{pmatrix}
\]
\[
= \begin{pmatrix}-\frac{1}{5}+\frac{6}{5} & \frac{2}{5}-\frac{2}{5} \\[4pt] -\frac{3}{5}+\frac{3}{5} & \frac{6}{5}-\frac{1}{5}\end{pmatrix}
= \begin{pmatrix}1 & 0 \\ 0 & 1\end{pmatrix} \;\checkmark
\]

**Answer:** (a) \(\det(M) = a^2 - 6\); (b) \(a = \pm\sqrt{6}\); (c) \(M^{-1} = \begin{pmatrix}-1/5 & 2/5 \\ 3/5 & -1/5\end{pmatrix}\)

---

## Problem 22

**Approach:** Find two direction vectors from the three points, take their cross product for a normal, then derive the Cartesian equation and distance from the origin.

Points: \(A(1,0,2)\), \(B(3,-1,4)\), \(C(0,2,-1)\).

**(a)** Direction vectors in the plane:
\[
\overrightarrow{AB} = B - A = (2,-1,2),\qquad \overrightarrow{AC} = C - A = (-1,2,-3)
\]

**(b)** Normal vector \(\mathbf{n} = \overrightarrow{AB} \times \overrightarrow{AC}\):
\[
\mathbf{n} =
\begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
2 & -1 & 2 \\
-1 & 2 & -3
\end{vmatrix}
\]
\[
= \mathbf{i}\bigl((-1)(-3) - 2\cdot 2\bigr) - \mathbf{j}\bigl(2(-3) - 2(-1)\bigr) + \mathbf{k}\bigl(2\cdot 2 - (-1)(-1)\bigr)
\]
\[
= \mathbf{i}(3-4) - \mathbf{j}(-6+2) + \mathbf{k}(4-1) = -\mathbf{i} + 4\mathbf{j} + 3\mathbf{k}
\]

Normal: \(\mathbf{n} = (-1,4,3)\).

**(c)** Cartesian equation using point \(A(1,0,2)\) and normal \((-1,4,3)\):
\[
-1(x-1) + 4(y-0) + 3(z-2) = 0
\]
\[
-x + 1 + 4y + 3z - 6 = 0 \;\Rightarrow\; -x + 4y + 3z - 5 = 0
\]
Multiply by \(-1\) for cleaner form:
\[
x - 4y - 3z + 5 = 0 \quad \text{or} \quad x - 4y - 3z = -5
\]

**(d)** Distance from origin \((0,0,0)\) to plane \(x - 4y - 3z + 5 = 0\):
\[
d = \frac{|1(0) - 4(0) - 3(0) + 5|}{\sqrt{1^2 + (-4)^2 + (-3)^2}} = \frac{|5|}{\sqrt{1+16+9}} = \frac{5}{\sqrt{26}}
\]

**Answer:** (a) \(\overrightarrow{AB} = (2,-1,2)\), \(\overrightarrow{AC} = (-1,2,-3)\); (b) \(\mathbf{n} = (-1,4,3)\); (c) \(x - 4y - 3z = -5\); (d) \(\displaystyle\frac{5}{\sqrt{26}}\)

---

## Problem 23

**Approach:** Compute the scalar triple product \((\mathbf{p}\times\mathbf{q})\cdot\mathbf{r}\), take its absolute value for volume, and interpret the zero case.

**(a)** \(\mathbf{p} = (2,1,-1)\), \(\mathbf{q} = (1,-3,2)\), \(\mathbf{r} = (4,-1,3)\).

\[
\mathbf{p}\times\mathbf{q} =
\begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
2 & 1 & -1 \\
1 & -3 & 2
\end{vmatrix}
\]
\[
= \mathbf{i}(1\cdot 2 - (-1)(-3)) - \mathbf{j}(2\cdot 2 - (-1)(1)) + \mathbf{k}(2(-3) - 1\cdot 1)
\]
\[
= \mathbf{i}(2 - 3) - \mathbf{j}(4 + 1) + \mathbf{k}(-6 - 1) = -\mathbf{i} - 5\mathbf{j} - 7\mathbf{k}
\]

\[
(\mathbf{p}\times\mathbf{q})\cdot\mathbf{r} = (-1)(4) + (-5)(-1) + (-7)(3) = -4 + 5 - 21 = -20
\]

**(b)** Volume of parallelepiped \(= |(\mathbf{p}\times\mathbf{q})\cdot\mathbf{r}| = |-20| = 20\) cubic units.

**(c)** If the scalar triple product is zero, the three vectors are **coplanar** — they lie in the same plane. The parallelepiped collapses, giving zero volume.

**Answer:** (a) \(-20\); (b) \(20\) cubic units; (c) The vectors are coplanar (they lie in the same plane).

---

## Problem 24

**Approach:** Row-reduce the augmented matrix and analyze the last row for consistency.

\[
\begin{pmatrix}[1 & -1 & 2 & | & 4] \\
[2 & 1 & -1 & | & 1] \\
[1 & -4 & 7 & | & k]
\end{pmatrix}
\]

**(a)** Row reduction:
\[
\begin{aligned}
R_2 &\to R_2 - 2R_1: & (0 &\; 3 &\; -5 &|& -7) \\
R_3 &\to R_3 - R_1:  & (0 &\; -3 &\; 5 &|& k-4)
\end{aligned}
\]

\[
\begin{pmatrix}[1 & -1 & 2 & | & 4] \\
[0 & 3 & -5 & | & -7] \\
[0 & -3 & 5 & | & k-4]
\end{pmatrix}
\]

\(R_3 \to R_3 + R_2\): \(\begin{pmatrix}0 & 0 & 0 & | & k-11\end{pmatrix}\)

Row-echelon form:
\[
\begin{pmatrix}[1 & -1 & 2 & | & 4] \\
[0 & 3 & -5 & | & -7] \\
[0 & 0 & 0 & | & k-11]
\end{pmatrix}
\]

**(b)** Infinitely many solutions occur when the last row is \(0 = 0\), i.e., \(k - 11 = 0\):
\[
k = 11
\]

**(c)** No solution when the last row is \(0 = \text{nonzero}\), i.e., \(k - 11 \neq 0\):
\[
k \neq 11
\]

**Answer:** (a) Row-echelon form as shown; (b) \(k = 11\); (c) \(k \neq 11\)

---

## Problem 25

**Approach:** Compare the direction vector of the line with the normal of the plane; substitute parametric equations to find intersection; use the angle formula.

**(a)** Direction of \(L\): \(\mathbf{d} = (2,-3,1)\). Normal of \(\Pi\): \(\mathbf{n} = (1,-2,1)\).

\[
\mathbf{d}\cdot\mathbf{n} = 2(1) + (-3)(-2) + 1(1) = 2 + 6 + 1 = 9 \neq 0
\]

Since \(\mathbf{d}\cdot\mathbf{n} \neq 0\), \(L\) is **not parallel** to \(\Pi\).

**(b)** Parametric form of \(L\): \(x = 1 + 2t,\; y = -1 - 3t,\; z = 4 + t\).

Substitute into plane \(x - 2y + z = 6\):
\[
(1+2t) - 2(-1-3t) + (4+t) = 6
\]
\[
1 + 2t + 2 + 6t + 4 + t = 6
\]
\[
7 + 9t = 6 \;\Rightarrow\; 9t = -1 \;\Rightarrow\; t = -\frac{1}{9}
\]

Intersection point:
\[
x = 1 + 2\!\left(-\tfrac{1}{9}\right) = 1 - \tfrac{2}{9} = \tfrac{7}{9}
\]
\[
y = -1 - 3\!\left(-\tfrac{1}{9}\right) = -1 + \tfrac{3}{9} = -1 + \tfrac{1}{3} = -\tfrac{2}{3}
\]
\[
z = 4 - \tfrac{1}{9} = \tfrac{36}{9} - \tfrac{1}{9} = \tfrac{35}{9}
\]

**(c)** The acute angle \(\theta\) between line and plane satisfies:
\[
\sin\theta = \frac{|\mathbf{d}\cdot\mathbf{n}|}{|\mathbf{d}||\mathbf{n}|}
\]

\[
|\mathbf{d}| = \sqrt{2^2 + (-3)^2 + 1^2} = \sqrt{4+9+1} = \sqrt{14}
\]
\[
|\mathbf{n}| = \sqrt{1^2 + (-2)^2 + 1^2} = \sqrt{1+4+1} = \sqrt{6}
\]
\[
\sin\theta = \frac{9}{\sqrt{14}\sqrt{6}} = \frac{9}{\sqrt{84}} = \frac{9}{2\sqrt{21}}
\]

\[
\theta = \arcsin\!\left(\frac{9}{2\sqrt{21}}\right) \approx 79.1^\circ
\]

**Answer:** (a) \(\mathbf{d}\cdot\mathbf{n} = 9 \neq 0\), so not parallel; (b) \(\left(\frac{7}{9},\;-\frac{2}{3},\;\frac{35}{9}\right)\); (c) \(\theta \approx 79.1^\circ\)
