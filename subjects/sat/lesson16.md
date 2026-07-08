# Lesson 16: Geometry — Lines, Angles & Triangles

## What You'll Learn
- Angle relationships with parallel lines: corresponding, alternate interior, alternate exterior
- Triangle angle sum theorem ($180°$) and the exterior angle theorem
- Similar triangles: the three similarity criteria (AA, SAS, SSS) and proportional reasoning
- Special right triangles: 30-60-90 and 45-45-90 ratios — memorize these
- How to set up proportions from similar triangles efficiently
- The SAT's favorite geometry traps and how to avoid them

## SAT Context
Geometry on the SAT appears in **4–6 questions** across both modules, primarily in the Geometry and Trigonometry domain. The SAT tests a specific, limited set of geometry concepts, and the questions tend to be visual — you'll be shown a diagram and asked to find an angle measure, side length, or relationship. Unlike IB AAHL, which demands rigorous proofs, the SAT asks for quick, accurate calculations. The key distinction: **the SAT provides a reference sheet** with common formulas, but you must know angle relationships and triangle theorems from memory. This lesson covers lines, angles, and triangles — the foundation of all SAT geometry.

---

## Parallel Lines and Transversals

When a **transversal** (a line) crosses two parallel lines, eight angles are formed. These angles have specific relationships:

```
    1 / 2
-----/-----  (parallel line 1)
   3/ 4
    \
   5 \ 6
------\----  (parallel line 2)
     7 \ 8
```

### Angle Pair Relationships

| Angle Pair | Relationship | Example |
|:---|:---|:---|
| Corresponding | Equal | $\angle 1 = \angle 5$, $\angle 2 = \angle 6$, $\angle 3 = \angle 7$, $\angle 4 = \angle 8$ |
| Alternate Interior | Equal | $\angle 3 = \angle 6$, $\angle 4 = \angle 5$ |
| Alternate Exterior | Equal | $\angle 1 = \angle 8$, $\angle 2 = \angle 7$ |
| Consecutive Interior (Same-side) | Supplementary (sum to $180°$) | $\angle 3 + \angle 5 = 180°$, $\angle 4 + \angle 6 = 180°$ |
| Vertical | Equal | $\angle 1 = \angle 3$, $\angle 2 = \angle 4$, $\angle 5 = \angle 7$, $\angle 6 = \angle 8$ |
| Linear Pair | Supplementary | $\angle 1 + \angle 2 = 180°$ (any adjacent angles on a line) |

> **🔍 PATTERN RECOGNITION:** When you see parallel lines on the SAT, immediately look for: (1) a transversal, (2) pairs of equal angles, (3) pairs that sum to $180°$. The SAT rarely asks you to name the relationship — it asks for the angle measure. Identify which angles are equal to which, then solve.

### Worked Example 1: Parallel Lines

**Problem:** In the figure, lines $\ell_1$ and $\ell_2$ are parallel. A transversal intersects them, forming an angle of $65°$ (at the upper left position). What is the measure of the angle at the lower right position?

**Solution:** Let the $65°$ angle be at the upper left. The lower right angle is in the same position relative to the transversal on the bottom line — it's a corresponding angle. Corresponding angles are **equal**. So the answer is $65°$.

**Alternate reasoning:** The lower right angle is also an alternate interior angle with the angle that forms a linear pair with the $65°$ angle. That linear pair angle is $180° - 65° = 115°$. Then alternate interior with the lower right: $115°$? No — let's be more careful. If the $65°$ is at position "1" (upper left of intersection on top line), the lower right would be position "8." Angle 1 and angle 8 are alternate exterior angles — they are equal. **Answer: 65°.**

---

## Triangle Angle Sum

The sum of the interior angles of any triangle is always $180°$:

$$\angle A + \angle B + \angle C = 180°$$

### Exterior Angle Theorem

An exterior angle of a triangle equals the sum of the two remote interior angles:

$$\text{Exterior } \angle = \angle A + \angle B$$

> **🚨 SAT TRAP ALERT:** The exterior angle theorem gives you a shortcut. If a problem shows a triangle with one side extended, the exterior angle equals the sum of the two angles that are NOT adjacent to it. Many students waste time finding the third angle first, then subtracting from $180°$. Use the theorem directly.

### Worked Example 2: Triangle Angles

**Problem:** In triangle $ABC$, $\angle A = 42°$ and $\angle B = 57°$. Side $BC$ is extended past $C$ to point $D$. What is the measure of $\angle ACD$?

**Solution:** $\angle ACD$ is an exterior angle at vertex $C$. By the exterior angle theorem:

$$\angle ACD = \angle A + \angle B = 42° + 57° = 99°$$

---

## Similar Triangles

Two triangles are **similar** if their corresponding angles are equal and their corresponding sides are proportional.

### Three Similarity Criteria

| Criterion | Meaning | What You Need |
|:---|:---|:---|
| **AA** (Angle-Angle) | Two pairs of corresponding angles are equal | Just two angles! (The third automatically matches.) |
| **SAS** (Side-Angle-Side) | Two pairs of corresponding sides are proportional AND the included angle is equal | Two side ratios + one angle |
| **SSS** (Side-Side-Side) | All three pairs of corresponding sides are proportional | Three side ratios |

> **🔍 PATTERN RECOGNITION:** On the SAT, similar triangles are almost always established by AA similarity. Look for shared angles, vertical angles, or parallel lines creating equal corresponding angles. If you can find two pairs of equal angles, the triangles are similar.

### Setting Up Proportions

When triangles are similar, corresponding sides are proportional:

$$\frac{AB}{DE} = \frac{BC}{EF} = \frac{AC}{DF}$$

The scale factor $k = \frac{\text{side in image}}{\text{corresponding side in original}}$.

> **🚨 SAT TRAP ALERT:** When setting up proportions, make sure corresponding sides are in the same position in each ratio. A common error: matching a side of one triangle to a non-corresponding side of the other. Always identify corresponding vertices first (matching angles), THEN set up proportions based on those correspondences.

### Worked Example 3: Similar Triangles

**Problem:** In the figure, $\triangle ABC \sim \triangle DEF$. $AB = 6$, $BC = 8$, $DE = 9$. Find $EF$.

**Solution:** Since the triangles are similar, corresponding sides are proportional. $AB$ corresponds to $DE$, and $BC$ corresponds to $EF$:

$$\frac{AB}{DE} = \frac{BC}{EF}$$
$$\frac{6}{9} = \frac{8}{EF}$$
$$\frac{2}{3} = \frac{8}{EF}$$
Cross-multiply: $2 \cdot EF = 3 \cdot 8 = 24$, so $EF = 12$.

---

## Special Right Triangles (Memorize These!)

These ratios appear constantly on the SAT and are NOT on the reference sheet (except as formulas for special right triangles — actually, the SAT reference sheet does include these now). Still, knowing them cold saves time.

### 45-45-90 Triangle (Isosceles Right Triangle)

The legs are equal. If each leg is $x$, the hypotenuse is $x\sqrt{2}$.

$$x : x : x\sqrt{2}$$

```
    /|
 x√2/ | x
  /   |
/_____|
   x
```

### 30-60-90 Triangle

If the shortest leg (opposite the $30°$ angle) is $x$:
- The hypotenuse is $2x$
- The longer leg (opposite the $60°$ angle) is $x\sqrt{3}$

$$x : x\sqrt{3} : 2x$$

```
      /|
     / |
  2x/  | x√3
   /   |
  /____|
 30°  x
```

> **🚨 SAT TRAP ALERT:** In a 30-60-90 triangle, the side opposite the $30°$ angle is the **shortest** side, and the side opposite the $60°$ angle is the **middle** length. The SAT may give you the longer leg and ask for the hypotenuse — don't accidentally multiply by $\sqrt{3}$ instead of using the ratio correctly.

### Worked Example 4: 30-60-90 Triangle

**Problem:** In a 30-60-90 triangle, the side opposite the $60°$ angle is $5\sqrt{3}$. What is the length of the hypotenuse?

**Solution:** The side opposite $60°$ is the longer leg, which equals $x\sqrt{3}$ where $x$ is the shortest leg. So $x\sqrt{3} = 5\sqrt{3}$, meaning $x = 5$. The hypotenuse is $2x = 2(5) = 10$.

---

## Angle Chasing Strategy

Many SAT geometry problems involve "angle chasing" — starting from a known angle and using theorems to find unknown angles.

### Step-by-Step Angle Chasing:
1. **Mark given angles** on the diagram
2. **Identify parallel lines**, vertical angles, and linear pairs
3. **Fill in supplementary angles** ($180°$ minus known angle)
4. **Use triangle sum** to find missing angles
5. **Use exterior angle theorem** as a shortcut when applicable

### Worked Example 5: Angle Chasing

**Problem:** In the figure, lines $\ell_1 \parallel \ell_2$ are cut by transversal $t$. $\angle 1 = 73°$. Find the measure of the angle that is consecutive interior to $\angle 1$ on the other parallel line.

**Solution:** Consecutive interior angles (same-side interior) are supplementary. If $\angle 1 = 73°$, the consecutive interior angle is $180° - 73° = 107°$.

---

## Proving Similarity from Parallel Lines

If a line is drawn parallel to one side of a triangle, it creates a smaller triangle similar to the original.

```
     A
    /\
   /  \
  /____\
 D      E
/        \
B----------C
```

If $DE \parallel BC$, then $\triangle ADE \sim \triangle ABC$. The ratio of corresponding sides is $\frac{AD}{AB} = \frac{AE}{AC} = \frac{DE}{BC}$.

> **🔍 PATTERN RECOGNITION:** When you see a triangle with a segment drawn parallel to one side, you have similar triangles. The parallel segment creates equal corresponding angles, which is enough for AA similarity.

---

## Practice Problems

### Problem 1
In the figure, two parallel lines are cut by a transversal. One of the acute angles measures $x°$, and an obtuse angle on the other parallel line measures $y°$. If $x + y = 180$, what is the relationship between the two angles?

(A) They are corresponding angles.  
(B) They are alternate interior angles.  
(C) They are consecutive interior (same-side interior) angles.  
(D) They are vertical angles.

### Problem 2
In $\triangle PQR$, $\angle P = 48°$ and $\angle Q = 64°$. Side $QR$ is extended beyond $R$ to point $S$. What is the measure of $\angle PRS$?

### Problem 3
Two triangles are similar. The sides of the smaller triangle are 3, 4, and 5. The longest side of the larger triangle is 15. What is the perimeter of the larger triangle?

(A) 24  
(B) 30  
(C) 36  
(D) 45

### Problem 4
In a 45-45-90 triangle, the hypotenuse is $8\sqrt{2}$. What is the length of each leg?

### Problem 5
In a 30-60-90 triangle, the shortest side is 7. What is the length of the longer leg?

(A) $7\sqrt{3}$  
(B) $14$  
(C) $7\sqrt{2}$  
(D) $\frac{7}{\sqrt{3}}$

### Problem 6
In the figure, $\triangle ABC$ has $DE \parallel BC$, with $D$ on $AB$ and $E$ on $AC$. $AD = 4$, $DB = 6$, and $BC = 15$. What is $DE$?

---

## Answers

### Problem 1 — Answer: (C)

If one angle is acute ($x$) and the other is obtuse ($y$) and they are on different parallel lines with $x + y = 180°$, they are supplementary. The only pair that are supplementary across parallel lines are consecutive interior (same-side interior) angles.

**Wrong-answer analysis:**
- (A) Corresponding angles are equal, not supplementary
- (B) Alternate interior angles are equal, not supplementary
- (D) Vertical angles are equal and share a vertex — these are on different lines

---

### Problem 2 — Answer: $112°$

First, find $\angle R$ using triangle sum:
$$\angle R = 180° - 48° - 64° = 68°$$

$\angle PRS$ is an exterior angle at vertex $R$ (side $QR$ is extended past $R$). By the exterior angle theorem:
$$\angle PRS = \angle P + \angle Q = 48° + 64° = 112°$$

Alternatively: $\angle PRS$ is supplementary to $\angle PRQ = 68°$, so $\angle PRS = 180° - 68° = 112°$. Same answer.

---

### Problem 3 — Answer: (C) 36

Scale factor: the longest side of the larger triangle (15) divided by the longest side of the smaller (5) = $15/5 = 3$. Multiply all sides by 3: $3 \times 3 = 9$, $4 \times 3 = 12$, $5 \times 3 = 15$. Perimeter: $9 + 12 + 15 = 36$.

**Wrong-answer analysis:**
- (A) 24 — might have multiplied original perimeter (12) by 2 instead of 3
- (B) 30 — might have added 10 instead of scaling proportionally
- (D) 45 — might have multiplied original perimeter by 15/4 (using wrong side as reference)

---

### Problem 4 — Answer: 8

In a 45-45-90 triangle, if each leg is $x$, the hypotenuse is $x\sqrt{2}$. Given hypotenuse $= 8\sqrt{2}$:

$$x\sqrt{2} = 8\sqrt{2}$$
$$x = 8$$

Each leg is 8.

---

### Problem 5 — Answer: (A) $7\sqrt{3}$

In a 30-60-90 triangle, the shortest side (opposite $30°$) is $x = 7$. The longer leg (opposite $60°$) is $x\sqrt{3} = 7\sqrt{3}$.

**Wrong-answer analysis:**
- (B) 14 — this is the hypotenuse ($2x = 14$), not the longer leg
- (C) $7\sqrt{2}$ — confused with 45-45-90 ratio
- (D) $\frac{7}{\sqrt{3}}$ — inverted the relationship

---

### Problem 6 — Answer: $DE = 6$

Since $DE \parallel BC$, $\triangle ADE \sim \triangle ABC$. $AB = AD + DB = 4 + 6 = 10$.

$$\frac{DE}{BC} = \frac{AD}{AB}$$
$$\frac{DE}{15} = \frac{4}{10} = \frac{2}{5}$$
$$DE = 15 \cdot \frac{2}{5} = 6$$

---

## Key Takeaways

1. Parallel lines + transversal → equal corresponding/alternate interior angles, supplementary consecutive interior angles.
2. Triangle angle sum is always $180°$. Exterior angle = sum of the two remote interior angles.
3. Similar triangles need only **two** pairs of equal angles (AA). Set up proportions with corresponding sides.
4. Memorize: 45-45-90 = $x:x:x\sqrt{2}$; 30-60-90 = $x:x\sqrt{3}:2x$.
5. Always verify which side corresponds to which when setting up proportions.
