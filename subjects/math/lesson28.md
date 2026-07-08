# Lesson 28 — Matrices: Operations, Determinants, and Inverses

## What Are Matrices?

### The "What"

A **matrix** (plural: **matrices**) is a rectangular array of numbers arranged in rows and columns. Each number in the matrix is called an **entry** or **element**. The **order** (or **dimension**) of a matrix is described as $m \times n$, meaning $m$ rows and $n$ columns.

For example, this is a $2 \times 3$ matrix:

$$A = \begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \end{pmatrix}$$

The entry $a_{ij}$ sits in row $i$ and column $j$. The first subscript gives the row number. The second gives the column number.

### The "Why"

Matrices are a compact way to represent and solve systems of linear equations. They are used to describe transformations (rotations, reflections, scaling) in geometry. They appear in computer graphics, economics, statistics, and quantum mechanics. Understanding matrix operations — addition, multiplication, determinants, and inverses — is essential for solving linear systems efficiently.

---

## 1. Matrix Addition and Subtraction

Two matrices can be added or subtracted only when they have exactly the same order (same number of rows and same number of columns). The operation is performed entry by entry:

$$\begin{pmatrix} a & b \\ c & d \end{pmatrix} + \begin{pmatrix} e & f \\ g & h \end{pmatrix} = \begin{pmatrix} a+e & b+f \\ c+g & d+h \end{pmatrix}$$

**A common misconception:** Students sometimes try to add matrices of different sizes. This is not defined. A $2 \times 3$ matrix cannot be added to a $3 \times 2$ matrix.

### Scalar Multiplication

To multiply a matrix by a scalar (a single number), multiply every entry by that scalar:

$$k\begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} ka & kb \\ kc & kd \end{pmatrix}$$

---

## 2. Matrix Multiplication

Matrix multiplication is more complex than addition. Two matrices $A$ and $B$ can be multiplied (in the order $AB$) only if the number of columns of $A$ equals the number of rows of $B$.

If $A$ is $m \times n$ and $B$ is $n \times p$, then the product $AB$ is $m \times p$.

The entry in row $i$ and column $j$ of the product is computed as the **dot product** of row $i$ of $A$ with column $j$ of $B$:

$$\boxed{c_{ij} = \sum_{k=1}^{n} a_{ik}\,b_{kj}}$$

This means: multiply the first entry of the row by the first entry of the column, the second by the second, and so on, then add all the products.

### Key Properties

- Matrix multiplication is **not commutative**: in general, $AB \neq BA$. The order matters.
- Matrix multiplication **is associative**: $(AB)C = A(BC)$. You can group them either way.
- Matrix multiplication **is distributive**: $A(B + C) = AB + AC$.

---

## Worked Example 1: Matrix Multiplication

**Problem:** Compute the product $AB$ where

$$A = \begin{pmatrix} 2 & 1 & 3 \\ -1 & 0 & 4 \end{pmatrix},\quad B = \begin{pmatrix} 1 & 2 \\ 3 & -1 \\ 0 & 5 \end{pmatrix}$$

**Approach:** $A$ is $2 \times 3$ and $B$ is $3 \times 2$, so $AB$ will be $2 \times 2$. Compute each entry using row-from-$A$ dotted with column-from-$B$.

**Step 1 — Entry $(1,1)$:** Row 1 of $A$ = $(2, 1, 3)$, Column 1 of $B$ = $(1, 3, 0)$.
$$c_{11} = 2(1) + 1(3) + 3(0) = 2 + 3 + 0 = 5$$

**Step 2 — Entry $(1,2)$:** Row 1 of $A$ = $(2, 1, 3)$, Column 2 of $B$ = $(2, -1, 5)$.
$$c_{12} = 2(2) + 1(-1) + 3(5) = 4 - 1 + 15 = 18$$

**Step 3 — Entry $(2,1)$:** Row 2 of $A$ = $(-1, 0, 4)$, Column 1 of $B$ = $(1, 3, 0)$.
$$c_{21} = -1(1) + 0(3) + 4(0) = -1 + 0 + 0 = -1$$

**Step 4 — Entry $(2,2)$:** Row 2 of $A$ = $(-1, 0, 4)$, Column 2 of $B$ = $(2, -1, 5)$.
$$c_{22} = -1(2) + 0(-1) + 4(5) = -2 + 0 + 20 = 18$$

**Answer:**
$$AB = \begin{pmatrix} 5 & 18 \\ -1 & 18 \end{pmatrix}$$

---

## 3. The Determinant

The **determinant** is a special scalar value associated with a square matrix. It provides critical information about the matrix: whether it is invertible, how it scales areas or volumes, and properties of the linear transformation it represents.

### Determinant of a $2 \times 2$ Matrix

$$\boxed{\det\begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{vmatrix} a & b \\ c & d \end{vmatrix} = ad - bc}$$

The determinant is the product of the main diagonal minus the product of the off-diagonal.

- If $\det A \neq 0$, the matrix is **invertible** (also called **non-singular**).
- If $\det A = 0$, the matrix is **singular** (not invertible). Geometrically, this means the transformation collapses the plane into a line or a point.

---

### Determinant of a $3 \times 3$ Matrix

For a $3 \times 3$ matrix $A = \begin{pmatrix} a & b & c \\ d & e & f \\ g & h & i \end{pmatrix}$, the determinant is computed by **expansion along the first row**:

$$\boxed{\det A = a\begin{vmatrix}e&f\\h&i\end{vmatrix} - b\begin{vmatrix}d&f\\g&i\end{vmatrix} + c\begin{vmatrix}d&e\\g&h\end{vmatrix}}$$

Notice the alternating signs: $+$, $-$, $+$. The $2 \times 2$ determinants inside are called **minors**. Specifically:

$$\det A = a(ei - fh) - b(di - fg) + c(dh - eg)$$

---

## Worked Example 2: $3 \times 3$ Determinant

**Problem:** Find the determinant of $A = \begin{pmatrix} 2 & 1 & 3 \\ 4 & -1 & 0 \\ 1 & 2 & 5 \end{pmatrix}$.

**Approach:** Expand along the first row using the formula with alternating signs.

**Step 1 — Set up the expansion:**
$$\det A = 2\begin{vmatrix}-1&0\\2&5\end{vmatrix} - 1\begin{vmatrix}4&0\\1&5\end{vmatrix} + 3\begin{vmatrix}4&-1\\1&2\end{vmatrix}$$

**Step 2 — Compute each $2 \times 2$ determinant:**
First: $(-1)(5) - (0)(2) = -5 - 0 = -5$.
Second: $(4)(5) - (0)(1) = 20 - 0 = 20$.
Third: $(4)(2) - (-1)(1) = 8 + 1 = 9$.

**Step 3 — Combine with signs:**
$$\det A = 2(-5) - 1(20) + 3(9) = -10 - 20 + 27 = -3$$

**Answer:** $\det A = -3$.

**Why this makes sense:** The determinant is non-zero ($-3$), so the matrix is invertible.

---

## 4. Inverse of a $2 \times 2$ Matrix

The **inverse** of a square matrix $A$, written $A^{-1}$, is the matrix that satisfies $AA^{-1} = A^{-1}A = I$, where $I$ is the **identity matrix** (ones on the diagonal, zeros elsewhere).

For a $2 \times 2$ matrix $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ with $\det A = ad - bc \neq 0$:

$$\boxed{A^{-1} = \frac{1}{\det A}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}}$$

The pattern: swap $a$ and $d$, change the signs of $b$ and $c$, then divide everything by the determinant.

---

## Worked Example 3: Inverse of a $2 \times 2$ Matrix

**Problem:** Find the inverse of $A = \begin{pmatrix} 3 & 2 \\ 5 & 4 \end{pmatrix}$.

**Approach:** Compute the determinant. If it is non-zero, apply the formula.

**Step 1 — Determinant:**
$$\det A = 3(4) - 2(5) = 12 - 10 = 2$$

**Step 2 — Apply the formula:**
$$A^{-1} = \frac{1}{2}\begin{pmatrix} 4 & -2 \\ -5 & 3 \end{pmatrix} = \begin{pmatrix} 2 & -1 \\ -2.5 & 1.5 \end{pmatrix}$$

**Step 3 — Verify:**
$\begin{pmatrix}3&2\\5&4\end{pmatrix}\begin{pmatrix}2&-1\\-2.5&1.5\end{pmatrix} = \begin{pmatrix}6-5&-3+3\\10-10&-5+6\end{pmatrix} = \begin{pmatrix}1&0\\0&1\end{pmatrix} = I$. Confirmed.

**Answer:** $A^{-1} = \begin{pmatrix} 2 & -1 \\ -2.5 & 1.5 \end{pmatrix}$

---

## 5. Inverse of a $3 \times 3$ Matrix (Using Cofactors)

For a $3 \times 3$ matrix, the inverse is computed using the **adjugate method**:

$$A^{-1} = \frac{1}{\det A}\,(\text{adj }A)$$

The **adjugate** (adj $A$) is the transpose of the **cofactor matrix**. Each cofactor is computed as:

$$C_{ij} = (-1)^{i+j} \cdot M_{ij}$$

where $M_{ij}$ is the **minor** — the determinant of the $2 \times 2$ matrix obtained by deleting row $i$ and column $j$ from $A$. The sign $(-1)^{i+j}$ creates a checkerboard pattern: positions where $i + j$ is even get $+$, odd get $-$.

---

## Worked Example 4: Inverse of a $3 \times 3$ Matrix

**Problem:** Find the inverse of $A = \begin{pmatrix} 1 & 2 & 0 \\ 3 & 1 & 2 \\ 0 & 1 & 1 \end{pmatrix}$.

**Approach:** Compute $\det A$, then find all nine cofactors, form the cofactor matrix, transpose to get the adjugate, and multiply by $\frac{1}{\det A}$.

**Step 1 — Determinant (expand along first row):**
$\det A = 1\begin{vmatrix}1&2\\1&1\end{vmatrix} - 2\begin{vmatrix}3&2\\0&1\end{vmatrix} + 0 = 1(1-2) - 2(3-0) = -1 - 6 = -7$.

**Step 2 — Cofactors (using checkerboard signs):**

$C_{11} = +\begin{vmatrix}1&2\\1&1\end{vmatrix} = 1 - 2 = -1$.

$C_{12} = -\begin{vmatrix}3&2\\0&1\end{vmatrix} = -(3 - 0) = -3$.

$C_{13} = +\begin{vmatrix}3&1\\0&1\end{vmatrix} = 3 - 0 = 3$.

$C_{21} = -\begin{vmatrix}2&0\\1&1\end{vmatrix} = -(2 - 0) = -2$.

$C_{22} = +\begin{vmatrix}1&0\\0&1\end{vmatrix} = 1 - 0 = 1$.

$C_{23} = -\begin{vmatrix}1&2\\0&1\end{vmatrix} = -(1 - 0) = -1$.

$C_{31} = +\begin{vmatrix}2&0\\1&2\end{vmatrix} = 4 - 0 = 4$.

$C_{32} = -\begin{vmatrix}1&0\\3&2\end{vmatrix} = -(2 - 0) = -2$.

$C_{33} = +\begin{vmatrix}1&2\\3&1\end{vmatrix} = 1 - 6 = -5$.

Cofactor matrix: $\begin{pmatrix}-1 & -3 & 3 \\ -2 & 1 & -1 \\ 4 & -2 & -5\end{pmatrix}$.

**Step 3 — Adjugate (transpose the cofactor matrix):**
$\text{adj }A = \begin{pmatrix}-1 & -2 & 4 \\ -3 & 1 & -2 \\ 3 & -1 & -5\end{pmatrix}$.

**Step 4 — Multiply by $\frac{1}{\det A}$:**
$A^{-1} = \frac{1}{-7}\begin{pmatrix}-1 & -2 & 4 \\ -3 & 1 & -2 \\ 3 & -1 & -5\end{pmatrix} = \begin{pmatrix}\frac{1}{7} & \frac{2}{7} & -\frac{4}{7} \\ \frac{3}{7} & -\frac{1}{7} & \frac{2}{7} \\ -\frac{3}{7} & \frac{1}{7} & \frac{5}{7}\end{pmatrix}$.

---

## 6. Important Properties of Determinants

- $\det(AB) = (\det A)(\det B)$ — the determinant of a product is the product of determinants.
- $\det(A^{-1}) = \frac{1}{\det A}$ — the determinant of the inverse is the reciprocal.
- $\det(A^T) = \det A$ — transposing does not change the determinant.
- Swapping two rows changes the sign of the determinant.
- If any row (or column) is all zeros, the determinant is zero.
- If two rows (or columns) are identical, the determinant is zero.

---

## Summary Table

| Operation | Rule |
|-----------|------|
| Addition | Entry-wise (same order required) |
| Multiplication | Row $\times$ Column dot products |
| $\det(2 \times 2)$ | $ad - bc$ |
| $\det(3 \times 3)$ | Expansion by minors (first row) |
| $A^{-1}$ ($2 \times 2$) | $\frac{1}{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$ |
| $A^{-1}$ ($3 \times 3$) | $\frac{1}{\det A}(\text{adj }A)$ |

---

## Practice Problems

**Problem 1:** Let $A = \begin{pmatrix}2&1&3\\0&-1&4\end{pmatrix}$ and $B = \begin{pmatrix}1&0\\-1&2\\3&1\end{pmatrix}$. Compute the product $AB$.

**Problem 2:** Compute the determinant of $\begin{pmatrix}5&2\\3&-1\end{pmatrix}$.

**Problem 3:** Compute the determinant of $\begin{pmatrix}1&0&2\\3&1&4\\2&-1&1\end{pmatrix}$.

**Problem 4:** Find the inverse of $A = \begin{pmatrix}4&3\\2&1\end{pmatrix}$.

**Problem 5 (IB-style):** Let $A = \begin{pmatrix}2&1\\0&3\end{pmatrix}$ and $B = \begin{pmatrix}4&-1\\2&5\end{pmatrix}$.
(a) Compute the product $AB$. [2 marks]
(b) Find $\det A$ and $\det B$. [1 mark]
(c) Verify that $\det(AB) = \det A \cdot \det B$. [2 marks]

**Problem 6:** Find the inverse of $B = \begin{pmatrix}1&2&1\\0&1&2\\1&0&1\end{pmatrix}$ using the cofactor method. Show all steps.

---

## Answers

**Answer 1:**

$A$ is $2 \times 3$, $B$ is $3 \times 2$, so $AB$ is $2 \times 2$.

$c_{11} = 2(1) + 1(-1) + 3(3) = 2 - 1 + 9 = 10$.

$c_{12} = 2(0) + 1(2) + 3(1) = 0 + 2 + 3 = 5$.

$c_{21} = 0(1) + (-1)(-1) + 4(3) = 0 + 1 + 12 = 13$.

$c_{22} = 0(0) + (-1)(2) + 4(1) = 0 - 2 + 4 = 2$.

$AB = \begin{pmatrix}10&5\\13&2\end{pmatrix}$.

---

**Answer 2:**

$\det = 5(-1) - 2(3) = -5 - 6 = -11$.

---

**Answer 3:**

Expand along the first row:

$\det = 1\begin{vmatrix}1&4\\-1&1\end{vmatrix} - 0 + 2\begin{vmatrix}3&1\\2&-1\end{vmatrix}$.

First minor: $1(1) - 4(-1) = 1 + 4 = 5$.

Second minor: $3(-1) - 1(2) = -3 - 2 = -5$.

$\det = 1(5) + 2(-5) = 5 - 10 = -5$.

---

**Answer 4:**

$\det A = 4(1) - 3(2) = 4 - 6 = -2$.

$A^{-1} = \frac{1}{-2}\begin{pmatrix}1&-3\\-2&4\end{pmatrix} = \begin{pmatrix}-\frac{1}{2}&\frac{3}{2}\\1&-2\end{pmatrix}$.

---

**Answer 5:**

**(a)** $AB = \begin{pmatrix}2(4)+1(2) & 2(-1)+1(5)\\0(4)+3(2) & 0(-1)+3(5)\end{pmatrix} = \begin{pmatrix}8+2 & -2+5\\0+6 & 0+15\end{pmatrix} = \begin{pmatrix}10&3\\6&15\end{pmatrix}$.

**(b)** $\det A = 2(3) - 1(0) = 6$. $\det B = 4(5) - (-1)(2) = 20 + 2 = 22$.

**(c)** $\det(AB) = 10(15) - 3(6) = 150 - 18 = 132$.

$\det A \cdot \det B = 6 \times 22 = 132$. They match. ✓

---

**Answer 6:**

$\det B = 1\begin{vmatrix}1&2\\0&1\end{vmatrix} - 2\begin{vmatrix}0&2\\1&1\end{vmatrix} + 1\begin{vmatrix}0&1\\1&0\end{vmatrix} = 1(1) - 2(-2) + 1(-1) = 1 + 4 - 1 = 4$.

Cofactors:

$C_{11} = +\begin{vmatrix}1&2\\0&1\end{vmatrix} = 1$.

$C_{12} = -\begin{vmatrix}0&2\\1&1\end{vmatrix} = -(-2) = 2$.

$C_{13} = +\begin{vmatrix}0&1\\1&0\end{vmatrix} = -1$.

$C_{21} = -\begin{vmatrix}2&1\\0&1\end{vmatrix} = -2$.

$C_{22} = +\begin{vmatrix}1&1\\1&1\end{vmatrix} = 0$.

$C_{23} = -\begin{vmatrix}1&2\\1&0\end{vmatrix} = -(-2) = 2$.

$C_{31} = +\begin{vmatrix}2&1\\1&2\end{vmatrix} = 3$.

$C_{32} = -\begin{vmatrix}1&1\\0&2\end{vmatrix} = -2$.

$C_{33} = +\begin{vmatrix}1&2\\0&1\end{vmatrix} = 1$.

Cofactor matrix: $\begin{pmatrix}1&2&-1\\-2&0&2\\3&-2&1\end{pmatrix}$.

Adjugate (transpose): $\begin{pmatrix}1&-2&3\\2&0&-2\\-1&2&1\end{pmatrix}$.

$B^{-1} = \frac{1}{4}\begin{pmatrix}1&-2&3\\2&0&-2\\-1&2&1\end{pmatrix} = \begin{pmatrix}\frac{1}{4}&-\frac{1}{2}&\frac{3}{4}\\\frac{1}{2}&0&-\frac{1}{2}\\-\frac{1}{4}&\frac{1}{2}&\frac{1}{4}\end{pmatrix}$.
