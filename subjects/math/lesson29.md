# Lesson 29: Row Reduction and Solving Linear Systems

## WHAT Is Row Reduction?

A **linear system** is a collection of equations where each equation is a straight line (in two dimensions) or a flat plane (in three dimensions). For example, here is a system of three equations with three unknown variables \(x\), \(y\), and \(z\):

\[
\begin{cases}
x + 2y + z = 9 \\
2x + y - z = 3 \\
3x - y + 2z = 8
\end{cases}
\]

Solving this by hand using substitution or elimination would involve many messy steps. **Row reduction** (also called **Gaussian elimination**) is an organized method that turns any linear system into a form where you can read off the answers directly.

The core idea is to write the system as a grid of numbers (a **matrix**), then perform simple, legal operations on the rows until the grid has a staircase pattern. At that point, solving is easy.

## WHY Learn Row Reduction?

Row reduction is systematic. It works on systems with 2 equations, 3 equations, or 50 equations. It never requires clever guesswork — you just follow the algorithm. It also tells you whether a system has one solution, no solution, or infinitely many solutions, which is information you cannot always get just by looking at the equations. This method is foundational for linear algebra, computer graphics, economic modeling, and any field that deals with large sets of linear constraints.

---

## 1. Writing a Linear System as a Matrix

A **matrix** (plural: matrices) is a rectangular array of numbers. To convert a linear system into a matrix, you drop the variables and the equals signs and keep only the coefficients and the right-hand-side numbers.

The system:

\[
\begin{cases}
a_{11}x + a_{12}y + a_{13}z = b_1 \\
a_{21}x + a_{22}y + a_{23}z = b_2 \\
a_{31}x + a_{32}y + a_{33}z = b_3
\end{cases}
\]

can be written compactly as \(A\mathbf{x} = \mathbf{b}\), where \(A\) is called the **coefficient matrix** and \(\mathbf{x}\) and \(\mathbf{b}\) are column vectors.

For row reduction, it is even more useful to write the **augmented matrix**, which attaches the right-hand-side column to the coefficient matrix with a vertical bar:

\[
\left(\begin{array}{ccc|c}
a_{11} & a_{12} & a_{13} & b_1 \\
a_{21} & a_{22} & a_{23} & b_2 \\
a_{31} & a_{32} & a_{33} & b_3
\end{array}\right)
\]

Each row corresponds to one equation. The numbers before the bar are the coefficients of \(x\), \(y\), and \(z\). The number after the bar is the right-hand side of the equation.

**Example:** The system at the top of this lesson becomes this augmented matrix:

\[
\left(\begin{array}{ccc|c}
1 & 2 & 1 & 9 \\
2 & 1 & -1 & 3 \\
3 & -1 & 2 & 8
\end{array}\right)
\]

---

## 2. The Three Elementary Row Operations

There are exactly three operations you are allowed to perform on the rows of an augmented matrix. They are called **elementary row operations**, and they all have one crucial property: they do not change the solution of the system.

**Operation 1 — Swap two rows.** You can exchange any two rows. Notation: \(R_i \leftrightarrow R_j\). This just changes the order of the equations, which does not affect the solutions.

**Operation 2 — Multiply a row by a non-zero number.** You can multiply every entry in a row by the same non-zero constant. Notation: \(R_i \to kR_i\) where \(k \neq 0\). This is like multiplying both sides of an equation by \(k\), which preserves equality as long as \(k\) is not zero.

**Operation 3 — Add a multiple of one row to another.** You can replace a row by itself plus a multiple of another row. Notation: \(R_i \to R_i + kR_j\). This is the workhorse of the method — it lets you create zeros.

**Common misconception:** Students sometimes try to replace a row by a multiple of itself AND add another row in one combined step that is not one of the three legal operations. Stick to the three allowed operations one at a time.

---

## 3. What the Goal Looks Like: Row Echelon Form (REF)

The goal of row reduction is to reach **row echelon form (REF)**. A matrix is in REF when:

1. All rows that contain only zeros are at the bottom.
2. The first non-zero entry in each row (called the **pivot** or **leading coefficient**) is farther to the right than the pivot in the row above it.
3. All entries below each pivot are zero.

Visually, the non-zero entries form a staircase going down and to the right:

\[
\begin{pmatrix}
\boxed{2} & 1 & 3 & 4 \\
0 & \boxed{5} & -1 & 2 \\
0 & 0 & \boxed{3} & 6
\end{pmatrix}
\]

The boxed numbers (2, 5, 3) are the pivots. Notice how everything below each pivot is zero.

There is also a stricter version called **reduced row echelon form (RREF)**, where each pivot is exactly 1 and is the only non-zero entry in its column. RREF lets you read solutions directly without back-substitution. For now, REF is enough.

---

## 4. The Gaussian Elimination Algorithm

Here is the step-by-step process you follow every time:

1. Write the augmented matrix.
2. Working from left to right, make each pivot position a 1 (optional but helpful) and then create zeros below it using operation 3 (\(R_i \to R_i + kR_j\)).
3. Once the matrix is in REF, read the equations from bottom to top to find the solution (this is called **back-substitution**).

---

## 5. Worked Example: A System with a Unique Solution

**Problem:** Solve this system using Gaussian elimination:

\[
\begin{cases}
x + 2y + z = 9 \\
2x + y - z = 3 \\
3x - y + 2z = 8
\end{cases}
\]

**Approach:** Write the augmented matrix. Use row operations to create zeros below the first pivot, then below the second pivot. Then back-substitute.

**Step 1 — Write the augmented matrix:**
\[
\left(\begin{array}{ccc|c}
1 & 2 & 1 & 9 \\
2 & 1 & -1 & 3 \\
3 & -1 & 2 & 8
\end{array}\right)
\]

**Step 2 — Create zeros below the first pivot (the 1 in row 1, column 1):**

For row 2: \(R_2 \to R_2 - 2R_1\). This means: new row 2 = old row 2 minus 2 times row 1.
\[
\begin{array}{c}
R_2: (2, 1, -1, 3) - 2(1, 2, 1, 9) = (2-2, 1-4, -1-2, 3-18) = (0, -3, -3, -15)
\end{array}
\]

For row 3: \(R_3 \to R_3 - 3R_1\).
\[
\begin{array}{c}
R_3: (3, -1, 2, 8) - 3(1, 2, 1, 9) = (3-3, -1-6, 2-3, 8-27) = (0, -7, -1, -19)
\end{array}
\]

The matrix now looks like:
\[
\left(\begin{array}{ccc|c}
1 & 2 & 1 & 9 \\
0 & -3 & -3 & -15 \\
0 & -7 & -1 & -19
\end{array}\right)
\]

**Step 3 — Make the second pivot nicer (optional but helpful).** Divide row 2 by \(-3\): \(R_2 \to -\frac{1}{3}R_2\).

\[
\left(\begin{array}{ccc|c}
1 & 2 & 1 & 9 \\
0 & 1 & 1 & 5 \\
0 & -7 & -1 & -19
\end{array}\right)
\]

**Step 4 — Create a zero below the second pivot:** \(R_3 \to R_3 + 7R_2\).
\[
\begin{array}{c}
R_3: (0, -7, -1, -19) + 7(0, 1, 1, 5) = (0, -7+7, -1+7, -19+35) = (0, 0, 6, 16)
\end{array}
\]

\[
\left(\begin{array}{ccc|c}
1 & 2 & 1 & 9 \\
0 & 1 & 1 & 5 \\
0 & 0 & 6 & 16
\end{array}\right)
\]

**Step 5 — Make the third pivot 1:** \(R_3 \to \frac{1}{6}R_3\).

\[
\left(\begin{array}{ccc|c}
1 & 2 & 1 & 9 \\
0 & 1 & 1 & 5 \\
0 & 0 & 1 & \frac{8}{3}
\end{array}\right)
\]

**Step 6 — Back-substitute (read from bottom to top):**

The third row means \(z = \frac{8}{3}\).

The second row means \(y + z = 5\). Substitute \(z = \frac{8}{3}\): \(y + \frac{8}{3} = 5\), so \(y = 5 - \frac{8}{3} = \frac{15-8}{3} = \frac{7}{3}\).

The first row means \(x + 2y + z = 9\). Substitute: \(x + 2(\frac{7}{3}) + \frac{8}{3} = 9\), so \(x + \frac{14}{3} + \frac{8}{3} = 9\), so \(x + \frac{22}{3} = 9\), and \(x = 9 - \frac{22}{3} = \frac{27-22}{3} = \frac{5}{3}\).

**Answer:** \(x = \frac{5}{3}\), \(y = \frac{7}{3}\), \(z = \frac{8}{3}\).

**Why this makes sense:** Plug these values into the original first equation: \(\frac{5}{3} + 2(\frac{7}{3}) + \frac{8}{3} = \frac{5+14+8}{3} = \frac{27}{3} = 9\). It checks out.

---

## 6. Worked Example: A System with No Solution

**Problem:** Solve this system:

\[
\begin{cases}
x + y + z = 3 \\
2x - y + z = 2 \\
4x + y + 3z = 5
\end{cases}
\]

**Approach:** Row reduce and watch for a contradiction.

**Step 1 — Augmented matrix:**
\[
\left(\begin{array}{ccc|c}
1 & 1 & 1 & 3 \\
2 & -1 & 1 & 2 \\
4 & 1 & 3 & 5
\end{array}\right)
\]

**Step 2 — Zeros below first pivot:**
\(R_2 \to R_2 - 2R_1\): \((2, -1, 1, 2) - 2(1, 1, 1, 3) = (0, -3, -1, -4)\).
\(R_3 \to R_3 - 4R_1\): \((4, 1, 3, 5) - 4(1, 1, 1, 3) = (0, -3, -1, -7)\).

\[
\left(\begin{array}{ccc|c}
1 & 1 & 1 & 3 \\
0 & -3 & -1 & -4 \\
0 & -3 & -1 & -7
\end{array}\right)
\]

**Step 3 — Zero below second pivot:** \(R_3 \to R_3 - R_2\).
\((0, -3, -1, -7) - (0, -3, -1, -4) = (0, 0, 0, -3)\).

\[
\left(\begin{array}{ccc|c}
1 & 1 & 1 & 3 \\
0 & -3 & -1 & -4 \\
0 & 0 & 0 & -3
\end{array}\right)
\]

**Step 4 — Interpret:** The last row means \(0x + 0y + 0z = -3\), or simply \(0 = -3\). This is impossible.

**Answer:** The system has **no solution**. It is called an **inconsistent** system.

---

## 7. Worked Example: A System with Infinitely Many Solutions

**Problem:** Solve this system:

\[
\begin{cases}
x + 2y - z = 4 \\
2x + 4y - 2z = 8 \\
x - y + z = 1
\end{cases}
\]

**Approach:** Row reduce and watch for a row of zeros or a free variable.

**Step 1 — Augmented matrix:**
\[
\left(\begin{array}{ccc|c}
1 & 2 & -1 & 4 \\
2 & 4 & -2 & 8 \\
1 & -1 & 1 & 1
\end{array}\right)
\]

**Step 2 — Zero below first pivot:**
\(R_2 \to R_2 - 2R_1\): \((2, 4, -2, 8) - 2(1, 2, -1, 4) = (0, 0, 0, 0)\).

Row 2 becomes all zeros. This means the second equation was just a multiple of the first — it adds no new information.

**Step 3 — Continue with row 3:**
\(R_3 \to R_3 - R_1\): \((1, -1, 1, 1) - (1, 2, -1, 4) = (0, -3, 2, -3)\).

\[
\left(\begin{array}{ccc|c}
1 & 2 & -1 & 4 \\
0 & -3 & 2 & -3 \\
0 & 0 & 0 & 0
\end{array}\right)
\]

**Step 4 — Make the second pivot 1:** \(R_2 \to -\frac{1}{3}R_2\).

\[
\left(\begin{array}{ccc|c}
1 & 2 & -1 & 4 \\
0 & 1 & -\frac{2}{3} & 1 \\
0 & 0 & 0 & 0
\end{array}\right)
\]

**Step 5 — Create a zero above the second pivot (optional, toward RREF):**
\(R_1 \to R_1 - 2R_2\): \((1, 2, -1, 4) - 2(0, 1, -\frac{2}{3}, 1) = (1, 0, \frac{1}{3}, 2)\).

\[
\left(\begin{array}{ccc|c}
1 & 0 & \frac{1}{3} & 2 \\
0 & 1 & -\frac{2}{3} & 1 \\
0 & 0 & 0 & 0
\end{array}\right)
\]

**Step 6 — Interpret:** The matrix gives us:
- \(x + \frac{1}{3}z = 2\), so \(x = 2 - \frac{1}{3}z\).
- \(y - \frac{2}{3}z = 1\), so \(y = 1 + \frac{2}{3}z\).
- The third row is \(0 = 0\) (always true, so no restriction).

The variable \(z\) is **free** — it can be any real number. We express \(x\) and \(y\) in terms of \(z\).

Let \(z = t\), where \(t\) is any real number. Then:
\[
x = 2 - \frac{1}{3}t, \qquad y = 1 + \frac{2}{3}t, \qquad z = t
\]

**Answer:** Infinitely many solutions. The solution set is a line (a one-parameter family) in three-dimensional space.

---

## 8. How to Classify a Linear System

After reducing to REF, look at the augmented matrix:

- **Unique solution:** Every variable column has a pivot, and there is no row of the form \((0\;0\;0\;|\;k)\) with \(k \neq 0\). There are as many non-zero rows as variables.
- **No solution:** There is at least one row of the form \((0\;0\;0\;|\;k)\) where \(k \neq 0\). This is a contradiction.
- **Infinitely many solutions:** There are fewer pivots than variables, and there is no contradictory row. At least one variable is free.

---

## 9. Solving Using the Inverse Matrix (Alternative Method)

If the coefficient matrix \(A\) is square (same number of equations as variables) and its determinant is not zero, the system \(A\mathbf{x} = \mathbf{b}\) has exactly one solution, given by:

\[
\boxed{\mathbf{x} = A^{-1}\mathbf{b}}
\]

This method is fast for small systems (like \(2 \times 2\)) but less practical for large systems than row reduction.

### Worked Example: Inverse Matrix Method

**Problem:** Solve this \(2 \times 2\) system using the inverse matrix:

\[
\begin{cases}
2x + y = 5 \\
x + 3y = 7
\end{cases}
\]

**Approach:** Write \(A\), \(\mathbf{x}\), and \(\mathbf{b}\). Compute \(A^{-1}\). Multiply.

**Step 1:** \(A = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix}\), \(\mathbf{b} = \begin{pmatrix} 5 \\ 7 \end{pmatrix}\).

**Step 2 — Determinant:** \(\det A = (2)(3) - (1)(1) = 6 - 1 = 5\). Since it is not zero, \(A^{-1}\) exists.

**Step 3 — Inverse:** For a \(2 \times 2\) matrix \(\begin{pmatrix} a & b \\ c & d \end{pmatrix}\), the inverse is \(\frac{1}{ad-bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}\).

So \(A^{-1} = \frac{1}{5}\begin{pmatrix} 3 & -1 \\ -1 & 2 \end{pmatrix}\).

**Step 4 — Multiply:** \(\mathbf{x} = A^{-1}\mathbf{b} = \frac{1}{5}\begin{pmatrix} 3 & -1 \\ -1 & 2 \end{pmatrix}\begin{pmatrix} 5 \\ 7 \end{pmatrix}\).

Compute the product: \(\begin{pmatrix} 3(5) + (-1)(7) \\ (-1)(5) + 2(7) \end{pmatrix} = \begin{pmatrix} 15 - 7 \\ -5 + 14 \end{pmatrix} = \begin{pmatrix} 8 \\ 9 \end{pmatrix}\).

Then multiply by \(\frac{1}{5}\): \(\begin{pmatrix} 8/5 \\ 9/5 \end{pmatrix}\).

**Answer:** \(x = \frac{8}{5}\), \(y = \frac{9}{5}\).

---

## Practice Problems

**Problem 1:** Solve this system using Gaussian elimination:

\[
\begin{cases}
x + y + z = 6 \\
2x - y + 3z = 14 \\
3x + y - z = 2
\end{cases}
\]

**Problem 2:** Solve this system using Gaussian elimination:

\[
\begin{cases}
x + 2y - z = 4 \\
3x + 6y - 3z = 12 \\
2x - y + z = 5
\end{cases}
\]

**Problem 3:** Set up the augmented matrix for this system and row reduce enough to determine whether it has a unique solution, no solution, or infinitely many solutions:

\[
\begin{cases}
x + y + z = 3 \\
x - y + 2z = 1 \\
2x + 3z = 5
\end{cases}
\]

**Problem 4:** Solve this system using the inverse matrix method:

\[
\begin{cases}
3x + 2y = 11 \\
2x - y = 5
\end{cases}
\]

**Problem 5 (IB Exam Style):** Consider the system:

\[
\begin{cases}
x + y + z = 2 \\
2x + 3y + 2z = 5 \\
2x + 3y + (k^2 - 1)z = k + 1
\end{cases}
\]

(a) Write down the augmented matrix for this system. [1 mark]
(b) Use row operations to reduce the matrix to row echelon form. [3 marks]
(c) Determine the values of \(k\) for which the system has a unique solution. [2 marks]
(d) Determine the values of \(k\) for which the system has no solution. Explain why there are no values of \(k\) for which the system has infinitely many solutions. [2 marks]

**Problem 6:** A system has been reduced to this augmented matrix:

\[
\left(\begin{array}{ccc|c}
1 & 2 & 0 & 5 \\
0 & 0 & 1 & -3 \\
0 & 0 & 0 & 0
\end{array}\right)
\]

Write the solution set in parametric form, using a parameter \(t\) for any free variable.

---

## Answers

**Answer 1:** Augmented matrix: \(\left(\begin{array}{ccc|c} 1 & 1 & 1 & 6 \\ 2 & -1 & 3 & 14 \\ 3 & 1 & -1 & 2 \end{array}\right)\).

\(R_2 \to R_2 - 2R_1\): \((2, -1, 3, 14) - 2(1, 1, 1, 6) = (0, -3, 1, 2)\).

\(R_3 \to R_3 - 3R_1\): \((3, 1, -1, 2) - 3(1, 1, 1, 6) = (0, -2, -4, -16)\).

Matrix: \(\left(\begin{array}{ccc|c} 1 & 1 & 1 & 6 \\ 0 & -3 & 1 & 2 \\ 0 & -2 & -4 & -16 \end{array}\right)\).

Simplify row 3: \(R_3 \to -\frac{1}{2}R_3\) gives \((0, 1, 2, 8)\). Swap \(R_2 \leftrightarrow R_3\) for convenience:

\(\left(\begin{array}{ccc|c} 1 & 1 & 1 & 6 \\ 0 & 1 & 2 & 8 \\ 0 & -3 & 1 & 2 \end{array}\right)\).

\(R_3 \to R_3 + 3R_2\): \((0, -3, 1, 2) + 3(0, 1, 2, 8) = (0, 0, 7, 26)\).

\(\left(\begin{array}{ccc|c} 1 & 1 & 1 & 6 \\ 0 & 1 & 2 & 8 \\ 0 & 0 & 7 & 26 \end{array}\right)\).

Back-substitute: \(7z = 26 \Rightarrow z = \frac{26}{7}\).

\(y + 2z = 8 \Rightarrow y + \frac{52}{7} = 8 \Rightarrow y = \frac{56-52}{7} = \frac{4}{7}\).

\(x + y + z = 6 \Rightarrow x + \frac{4}{7} + \frac{26}{7} = 6 \Rightarrow x + \frac{30}{7} = \frac{42}{7} \Rightarrow x = \frac{12}{7}\).

**Answer 2:** Augmented matrix: \(\left(\begin{array}{ccc|c} 1 & 2 & -1 & 4 \\ 3 & 6 & -3 & 12 \\ 2 & -1 & 1 & 5 \end{array}\right)\).

\(R_2 \to R_2 - 3R_1\): \((3, 6, -3, 12) - 3(1, 2, -1, 4) = (0, 0, 0, 0)\). Row 2 is all zeros, so the second equation was just a multiple of the first.

\(R_3 \to R_3 - 2R_1\): \((2, -1, 1, 5) - 2(1, 2, -1, 4) = (0, -5, 3, -3)\).

Matrix: \(\left(\begin{array}{ccc|c} 1 & 2 & -1 & 4 \\ 0 & -5 & 3 & -3 \\ 0 & 0 & 0 & 0 \end{array}\right)\).

\(R_2 \to -\frac{1}{5}R_2\): \((0, 1, -\frac{3}{5}, \frac{3}{5})\).

\(R_1 \to R_1 - 2R_2\): \((1, 2, -1, 4) - 2(0, 1, -\frac{3}{5}, \frac{3}{5}) = (1, 0, \frac{1}{5}, \frac{14}{5})\).

\(\left(\begin{array}{ccc|c} 1 & 0 & \frac{1}{5} & \frac{14}{5} \\ 0 & 1 & -\frac{3}{5} & \frac{3}{5} \\ 0 & 0 & 0 & 0 \end{array}\right)\).

Let \(z = t\) (free). Then \(x = \frac{14}{5} - \frac{1}{5}t\) and \(y = \frac{3}{5} + \frac{3}{5}t\).

The system has **infinitely many solutions**.

**Answer 3:** Augmented matrix: \(\left(\begin{array}{ccc|c} 1 & 1 & 1 & 3 \\ 1 & -1 & 2 & 1 \\ 2 & 0 & 3 & 5 \end{array}\right)\).

\(R_2 \to R_2 - R_1\): \((1, -1, 2, 1) - (1, 1, 1, 3) = (0, -2, 1, -2)\).

\(R_3 \to R_3 - 2R_1\): \((2, 0, 3, 5) - 2(1, 1, 1, 3) = (0, -2, 1, -1)\).

\(\left(\begin{array}{ccc|c} 1 & 1 & 1 & 3 \\ 0 & -2 & 1 & -2 \\ 0 & -2 & 1 & -1 \end{array}\right)\).

\(R_3 \to R_3 - R_2\): \((0, -2, 1, -1) - (0, -2, 1, -2) = (0, 0, 0, 1)\).

\(\left(\begin{array}{ccc|c} 1 & 1 & 1 & 3 \\ 0 & -2 & 1 & -2 \\ 0 & 0 & 0 & 1 \end{array}\right)\).

Row 3 reads \(0 = 1\), which is a contradiction. The system has **no solution** (it is inconsistent).

**Answer 4:** \(A = \begin{pmatrix} 3 & 2 \\ 2 & -1 \end{pmatrix}\), \(\mathbf{b} = \begin{pmatrix} 11 \\ 5 \end{pmatrix}\).

\(\det A = (3)(-1) - (2)(2) = -3 - 4 = -7\). Since \(\det A \neq 0\), the inverse exists.

\(A^{-1} = \frac{1}{-7}\begin{pmatrix} -1 & -2 \\ -2 & 3 \end{pmatrix} = \begin{pmatrix} \frac{1}{7} & \frac{2}{7} \\[4pt] \frac{2}{7} & -\frac{3}{7} \end{pmatrix}\).

\(\mathbf{x} = A^{-1}\mathbf{b} = \begin{pmatrix} \frac{1}{7} & \frac{2}{7} \\[4pt] \frac{2}{7} & -\frac{3}{7} \end{pmatrix}\begin{pmatrix} 11 \\ 5 \end{pmatrix} = \begin{pmatrix} \frac{11+10}{7} \\[4pt] \frac{22-15}{7} \end{pmatrix} = \begin{pmatrix} \frac{21}{7} \\[4pt] \frac{7}{7} \end{pmatrix} = \begin{pmatrix} 3 \\ 1 \end{pmatrix}\).

So \(x = 3\) and \(y = 1\).

**Why this makes sense:** Plug into the first equation: \(3(3) + 2(1) = 9 + 2 = 11\). Into the second: \(2(3) - 1 = 6 - 1 = 5\). Both check out.

**Answer 5:**

(a) \(\left(\begin{array}{ccc|c} 1 & 1 & 1 & 2 \\ 2 & 3 & 2 & 5 \\ 2 & 3 & k^2-1 & k+1 \end{array}\right)\).

(b) \(R_2 \to R_2 - 2R_1\): \((2, 3, 2, 5) - 2(1, 1, 1, 2) = (0, 1, 0, 1)\).

\(R_3 \to R_3 - 2R_1\): \((2, 3, k^2-1, k+1) - 2(1, 1, 1, 2) = (0, 1, k^2-3, k-3)\).

Matrix: \(\left(\begin{array}{ccc|c} 1 & 1 & 1 & 2 \\ 0 & 1 & 0 & 1 \\ 0 & 1 & k^2-3 & k-3 \end{array}\right)\).

\(R_3 \to R_3 - R_2\): \((0, 1, k^2-3, k-3) - (0, 1, 0, 1) = (0, 0, k^2-3, k-4)\).

REF: \(\left(\begin{array}{ccc|c} 1 & 1 & 1 & 2 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & k^2-3 & k-4 \end{array}\right)\).

(c) For a unique solution, every variable needs a pivot and there must be no contradiction. The third row gives the equation \((k^2-3)z = k-4\). For there to be a pivot in the \(z\) column, we need \(k^2 - 3 \neq 0\), meaning \(k \neq \pm\sqrt{3}\). When \(k \neq \pm\sqrt{3}\), we can solve for \(z\) uniquely, and then back-substitute for \(y\) and \(x\). So the system has a unique solution when \(k \neq \sqrt{3}\) and \(k \neq -\sqrt{3}\).

(d) When \(k^2 - 3 = 0\) (i.e., \(k = \sqrt{3}\) or \(k = -\sqrt{3}\)), the third row becomes \((0, 0, 0, k-4)\). Since \(k = \pm\sqrt{3}\) means \(k-4 \neq 0\) (because \(\sqrt{3} \approx 1.732\), so \(\sqrt{3} - 4 \neq 0\)), the row reads \(0 = k-4 \neq 0\), which is a contradiction. So for \(k = \pm\sqrt{3}\), the system has **no solution**.

Why no infinite solutions? For infinite solutions we would need both \(k^2 - 3 = 0\) AND \(k - 4 = 0\) simultaneously. But \(k^2 = 3\) and \(k = 4\) cannot both be true — no number satisfies both conditions. Therefore there is never a row of zeros at the bottom, so there are never infinite solutions.

**Answer 6:** The matrix gives two equations: \(x + 2y = 5\) and \(z = -3\).

The variable \(y\) does not have a pivot, so \(y\) is free. Let \(y = t\), where \(t\) can be any real number.

Then \(x + 2t = 5\), so \(x = 5 - 2t\).

The variable \(z\) is fixed: \(z = -3\).

Solution in parametric form: \((x, y, z) = (5 - 2t,\; t,\; -3)\), where \(t \in \mathbb{R}\).
