# Lesson 19: Circle Equations & Coordinate Geometry

## What You'll Learn
- The standard form of a circle equation: $(x-h)^2 + (y-k)^2 = r^2$
- How to identify the center $(h, k)$ and radius $r$ from the equation
- Completing the square to convert expanded form to standard form
- The distance formula and how it relates to the circle equation
- The midpoint formula and its applications
- The SAT trap: $r^2$ on the right side, NOT $r$

## SAT Context
Circle equations appear in **2–3 questions** across the SAT Math modules, primarily in the Advanced Math domain. These questions test your ability to recognize and manipulate the standard form of a circle equation. The most common format: the SAT gives an expanded equation like $x^2 + y^2 - 6x + 8y = 0$ and asks for the center and radius. Completing the square is the essential skill here. The distance and midpoint formulas also appear in coordinate geometry questions, often combined with circles. Unlike IB AAHL, which dives into conic sections in detail, the SAT limits itself to circles only — no ellipses, no hyperbolas, no parabolas in non-function form.

---

## Standard Form of a Circle

The equation of a circle with center $(h, k)$ and radius $r$:

$$(x - h)^2 + (y - k)^2 = r^2$$

> **🚨 SAT TRAP ALERT (CRITICAL):** The right side of the equation is $r^2$, NOT $r$. If an equation says $(x-3)^2 + (y+2)^2 = 25$, the radius is $\sqrt{25} = 5$, not 25. The SAT will include 25 as an answer choice to catch students who forget this. This is one of the most reliable SAT circle traps.

### Reading the Center from the Equation

- $(x - h)^2$ → center's $x$-coordinate is $h$
- $(y - k)^2$ → center's $y$-coordinate is $k$

> **🚨 SAT TRAP ALERT:** $(x + 4)^2$ means $(x - (-4))^2$, so $h = -4$, not $+4$. Similarly, $(y - 2)^2$ means $k = 2$. The sign in the equation is the OPPOSITE of the coordinate. This is the same trap as function transformations.

### Worked Example 1: Reading the Equation

**Problem:** Find the center and radius of the circle $(x+5)^2 + (y-1)^2 = 49$.

**Solution:**
- $x+5 = x - (-5)$, so $h = -5$
- $y-1$ → $k = 1$
- $r^2 = 49$, so $r = 7$

**Center:** $(-5, 1)$, **Radius:** $7$

**Common wrong answer:** Center $(5, -1)$ (both signs flipped) and radius 49.

---

## Completing the Square for Circles

When the circle equation is given in expanded form, you must complete the square for both $x$ and $y$ terms.

### Steps:
1. Group $x$ terms and $y$ terms
2. Move the constant to the right side
3. Complete the square for $x$: take half of the $x$-coefficient, square it, add to both sides
4. Complete the square for $y$: take half of the $y$-coefficient, square it, add to both sides
5. Rewrite as $(x-h)^2 + (y-k)^2 = r^2$

### Worked Example 2: Completing the Square

**Problem:** Find the center and radius of the circle $x^2 + y^2 - 8x + 6y = 0$.

**Solution:**
1. Group: $(x^2 - 8x) + (y^2 + 6y) = 0$
2. Complete square for $x$: half of $-8$ is $-4$, square is $16$. Add 16 to both sides.
3. Complete square for $y$: half of $6$ is $3$, square is $9$. Add 9 to both sides.
4. $(x^2 - 8x + 16) + (y^2 + 6y + 9) = 0 + 16 + 9$
5. $(x - 4)^2 + (y + 3)^2 = 25$

**Center:** $(4, -3)$, **Radius:** $\sqrt{25} = 5$

> **🔍 PATTERN RECOGNITION:** The completed-square constants you add are always $(\frac{\text{coefficient}}{2})^2$. For $x^2 + bx$, add $(\frac{b}{2})^2$. For $x^2$ with a coefficient other than 1 (like $2x^2$), factor it out first.

### Worked Example 3: With Coefficients

**Problem:** Find the center and radius of $2x^2 + 2y^2 - 12x + 8y = 24$.

**Solution:** First divide everything by 2:
$$x^2 + y^2 - 6x + 4y = 12$$

Group: $(x^2 - 6x) + (y^2 + 4y) = 12$

Complete squares:
- $x$: half of $-6$ is $-3$, square is $9$
- $y$: half of $4$ is $2$, square is $4$

$$(x^2 - 6x + 9) + (y^2 + 4y + 4) = 12 + 9 + 4$$
$$(x-3)^2 + (y+2)^2 = 25$$

**Center:** $(3, -2)$, **Radius:** $5$

---

## The Distance Formula

The distance between points $(x_1, y_1)$ and $(x_2, y_2)$:

$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

This is simply the Pythagorean theorem in coordinate form.

> **🔍 PATTERN RECOGNITION:** The distance formula IS the circle equation rewritten. For a circle centered at $(h, k)$, the distance from any point $(x, y)$ on the circle to the center is exactly $r$. That's why: $\sqrt{(x-h)^2 + (y-k)^2} = r$, which squares to $(x-h)^2 + (y-k)^2 = r^2$.

### Worked Example 4: Distance Formula

**Problem:** What is the distance between points $A(2, -1)$ and $B(5, 3)$?

**Solution:**
$$d = \sqrt{(5-2)^2 + (3-(-1))^2} = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5$$

This is a 3-4-5 right triangle.

---

## The Midpoint Formula

The midpoint of the segment joining $(x_1, y_1)$ and $(x_2, y_2)$:

$$\text{Midpoint} = \left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)$$

This gives the **average** of the $x$-coordinates and the average of the $y$-coordinates.

### Applications:
1. Finding the midpoint of a segment
2. Finding an endpoint when given the midpoint and one endpoint
3. Finding the center of a circle when given the endpoints of a diameter

### Worked Example 5: Midpoint

**Problem:** The endpoints of a diameter of a circle are $(-2, 4)$ and $(6, -2)$. What is the center of the circle?

**Solution:** The center is the midpoint of any diameter:
$$\left(\frac{-2 + 6}{2}, \frac{4 + (-2)}{2}\right) = \left(\frac{4}{2}, \frac{2}{2}\right) = (2, 1)$$

---

## Equation of a Circle from Diameter Endpoints

If you know the endpoints of a diameter:
1. Find the center (midpoint of the diameter endpoints)
2. Find the radius (half the distance between endpoints, OR distance from center to either endpoint)

### Worked Example 6: Circle from Diameter

**Problem:** Points $P(1, 2)$ and $Q(7, 10)$ are endpoints of a diameter. Find the equation of the circle.

**Solution:**
1. Center = midpoint: $\left(\frac{1+7}{2}, \frac{2+10}{2}\right) = (4, 6)$
2. Radius = distance from center $(4, 6)$ to endpoint $(1, 2)$:
   $$r = \sqrt{(4-1)^2 + (6-2)^2} = \sqrt{3^2 + 4^2} = \sqrt{25} = 5$$
3. Equation: $(x-4)^2 + (y-6)^2 = 25$

---

## Determining if a Point Lies on a Circle

Plug the point's coordinates into the equation. If the equation holds true (both sides equal), the point is on the circle.

### Worked Example 7: Point on Circle

**Problem:** Does the point $(5, 1)$ lie on the circle $(x-2)^2 + (y+3)^2 = 25$?

**Solution:**
Plug in: $(5-2)^2 + (1+3)^2 = 3^2 + 4^2 = 9 + 16 = 25$. Since $25 = 25$, the point is on the circle.

---

## Practice Problems

### Problem 1
What are the center and radius of the circle $(x+3)^2 + (y-7)^2 = 16$?

(A) Center $(3, -7)$, radius 4  
(B) Center $(-3, 7)$, radius 4  
(C) Center $(3, -7)$, radius 16  
(D) Center $(-3, 7)$, radius 16

### Problem 2
Find the center and radius of $x^2 + y^2 - 4x + 10y + 20 = 0$.

### Problem 3
What is the distance between the points $(-3, 5)$ and $(1, 2)$?

### Problem 4
The midpoint of segment $AB$ is $(4, -1)$. If $A$ is $(1, 2)$, what are the coordinates of $B$?

(A) $(2.5, 0.5)$  
(B) $(7, -4)$  
(C) $(7, 0)$  
(D) $(5.5, 1.5)$

### Problem 5
A circle has center $(2, -1)$ and passes through the point $(5, 3)$. What is the equation of the circle?

(A) $(x-2)^2 + (y+1)^2 = 5$  
(B) $(x-2)^2 + (y+1)^2 = 25$  
(C) $(x+2)^2 + (y-1)^2 = 25$  
(D) $(x-5)^2 + (y-3)^2 = 25$

---

## Answers

### Problem 1 — Answer: (B) Center $(-3, 7)$, radius 4

$(x+3)^2 = (x-(-3))^2$ → $h = -3$. $(y-7)^2$ → $k = 7$. $r^2 = 16$ → $r = 4$.

**Wrong-answer analysis:**
- (A) Center $(3, -7)$ — flipped both signs
- (C) Center $(3, -7)$, radius 16 — flipped signs AND forgot to take square root
- (D) Center $(-3, 7)$, radius 16 — correct center but forgot to take square root of 16

---

### Problem 2 — Answer: Center $(2, -5)$, radius $3$

$$x^2 + y^2 - 4x + 10y + 20 = 0$$
$$(x^2 - 4x) + (y^2 + 10y) = -20$$

Complete squares:
- $x$: $(\frac{-4}{2})^2 = 4$
- $y$: $(\frac{10}{2})^2 = 25$

$$(x^2 - 4x + 4) + (y^2 + 10y + 25) = -20 + 4 + 25$$
$$(x-2)^2 + (y+5)^2 = 9$$

Center $(2, -5)$, $r = \sqrt{9} = 3$.

---

### Problem 3 — Answer: 5

$$d = \sqrt{(1-(-3))^2 + (2-5)^2} = \sqrt{4^2 + (-3)^2} = \sqrt{16 + 9} = \sqrt{25} = 5$$

---

### Problem 4 — Answer: (B) $(7, -4)$

If midpoint $M(4, -1) = \left(\frac{1+x_B}{2}, \frac{2+y_B}{2}\right)$:

$\frac{1+x_B}{2} = 4$ → $1+x_B = 8$ → $x_B = 7$
$\frac{2+y_B}{2} = -1$ → $2+y_B = -2$ → $y_B = -4$

$B$ is $(7, -4)$.

**Wrong-answer analysis:**
- (A) $(2.5, 0.5)$ — found the midpoint of $A$ and the given midpoint
- (C) $(7, 0)$ — correct $x$ but wrong $y$ calculation
- (D) $(5.5, 1.5)$ — various arithmetic errors

---

### Problem 5 — Answer: (B) $(x-2)^2 + (y+1)^2 = 25$

The radius is the distance from center $(2, -1)$ to point $(5, 3)$:

$$r = \sqrt{(5-2)^2 + (3-(-1))^2} = \sqrt{3^2 + 4^2} = \sqrt{25} = 5$$

So $r^2 = 25$. Using center $(h, k) = (2, -1)$: $(x-2)^2 + (y+1)^2 = 25$.

**Wrong-answer analysis:**
- (A) $= 5$ — forgot to square the radius ($r^2$ not $r$)
- (C) $(x+2)^2 + (y-1)^2$ — flipped center signs
- (D) Uses the point $(5, 3)$ as the center — completely misread the problem

---

## Key Takeaways

1. Standard form: $(x-h)^2 + (y-k)^2 = r^2$. The right side is $r^2$, NEVER $r$.
2. The center $(h, k)$ has signs OPPOSITE to what appears in $(x-h)^2$ and $(y-k)^2$.
3. Completing the square is the bridge from expanded form to standard form.
4. The distance formula IS the Pythagorean theorem in coordinates.
5. For a diameter, the center is the midpoint of the endpoints; the radius is half the diameter length.
