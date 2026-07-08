# Lesson 18: Geometry — Circles (Arcs, Chords, Sectors)

## What You'll Learn
- Circle fundamentals: circumference, area, radius, diameter
- Arc length and sector area formulas — and when to use each
- The relationship between central angles and arcs
- Inscribed angles and why they're always half the arc they intercept
- Tangent lines and their perpendicular relationship with radii
- The critical distinction between arc measure (degrees) and arc length (distance)

## SAT Context
Circle problems appear in **3–5 questions** across the SAT Math section, typically in the Geometry and Trigonometry domain. The SAT tests a specific set of circle concepts: circumference, area, arc length, sector area, central vs. inscribed angles, and the tangent-radius perpendicular property. Unlike IB AAHL, the SAT does NOT test radian measure for angles — everything is in degrees. The formulas for circumference, area, arc length, and sector area are provided on the SAT reference sheet, but knowing them by heart saves precious seconds. The most subtle trap on the SAT is confusing arc measure (an angle in degrees) with arc length (a physical distance along the circle).

---

## Circle Fundamentals

For a circle with radius $r$ and diameter $d = 2r$:

| Quantity | Formula | What It Measures |
|:---|:---|:---|
| **Diameter** | $d = 2r$ | Distance across the circle through center |
| **Circumference** | $C = 2\pi r = \pi d$ | Distance around the circle |
| **Area** | $A = \pi r^2$ | Space inside the circle |

> **🚨 SAT TRAP ALERT:** The area formula uses $r^2$, and the circumference formula uses $r$ (not squared). A classic SAT distractor: giving you $r = 3$ and offering $9\pi$ (area) as an answer choice when the question asked for circumference ($6\pi$), or vice versa. Always check: are they asking for space inside (area) or distance around (circumference)?

---

## Arc Length

An arc is a portion of the circumference. The arc length is proportional to the central angle.

$$\text{Arc Length} = \frac{\theta}{360°} \times 2\pi r$$

Where $\theta$ is the central angle (in degrees) that subtends the arc.

> **🔍 PATTERN RECOGNITION:** The fraction $\frac{\theta}{360°}$ tells you what fraction of the full circle the arc represents. If $\theta = 90°$, the arc is $\frac{1}{4}$ of the circumference. If $\theta = 60°$, it's $\frac{1}{6}$. Think in fractions — it's faster than plugging into the formula.

### Worked Example 1: Arc Length

**Problem:** A circle has radius 10 cm. What is the length of the arc subtended by a central angle of $72°$?

**Solution:** 
$$\text{Arc Length} = \frac{72}{360} \times 2\pi(10) = \frac{1}{5} \times 20\pi = 4\pi \text{ cm}$$

---

## Sector Area

A sector is the region bounded by two radii and an arc (like a pizza slice). The sector area is proportional to the central angle.

$$\text{Sector Area} = \frac{\theta}{360°} \times \pi r^2$$

> **🔍 PATTERN RECOGNITION:** The sector area formula is the same pattern as arc length — multiply the whole-circle formula by $\frac{\theta}{360°}$. Arc length: fraction × circumference; Sector area: fraction × area. This symmetry makes both formulas easy to remember.

### Worked Example 2: Sector Area

**Problem:** A circle has radius 8. A sector has a central angle of $45°$. What is the area of the sector?

**Solution:**
$$\text{Sector Area} = \frac{45}{360} \times \pi(8)^2 = \frac{1}{8} \times 64\pi = 8\pi$$

---

## Arc Measure vs. Arc Length

This distinction is **the most important circle concept on the SAT**.

| Term | What It Is | Units | Notation |
|:---|:---|:---|:---|
| **Arc Measure** | The angular size of the arc | Degrees | $m\widehat{AB} = 60°$ |
| **Arc Length** | The physical distance along the arc | Linear units (cm, in, etc.) | $\text{length of }\widehat{AB} = \frac{\pi r}{3}$ |

> **🚨 SAT TRAP ALERT:** If a problem asks "what is the length of arc $AB$?" the answer is a distance (something with $\pi$, cm, inches, etc.). If it asks "what is the measure of arc $AB$?" the answer is in degrees. The SAT will include both a degree answer and a distance answer as choices. Read carefully which one they're asking for.

### Worked Example 3: The Distinction

**Problem:** In a circle with radius 6, a central angle of $120°$ subtends arc $PQ$.

(a) What is the measure of arc $PQ$?  
(b) What is the length of arc $PQ$?

**Solution:**
(a) The arc MEASURE equals the central angle: $120°$. That's it — no formula needed.

(b) The arc LENGTH: $\frac{120}{360} \times 2\pi(6) = \frac{1}{3} \times 12\pi = 4\pi$.

---

## Central Angles and Arcs

A **central angle** has its vertex at the center of the circle. Its sides are radii.

**Key fact:** The measure of a central angle **equals** the measure of its intercepted arc.

$$\text{Central angle} = \text{Arc measure}$$

---

## Inscribed Angles

An **inscribed angle** has its vertex ON the circle. Its sides are chords.

**Key fact:** The measure of an inscribed angle is **half** the measure of its intercepted arc.

$$\text{Inscribed angle} = \frac{1}{2} \times \text{Arc measure}$$

> **🔍 PATTERN RECOGNITION:** If a central angle and an inscribed angle intercept the same arc, the inscribed angle is exactly half the central angle. This relationship is tested frequently — it's one of the SAT's favorite circle geometry questions.

### Worked Example 4: Inscribed Angle

**Problem:** In a circle, chord $AB$ and chord $AC$ form an inscribed angle of $35°$ at point $A$ (on the circle). What is the measure of arc $BC$ (the arc not containing $A$)?

**Solution:** The inscribed angle is $35°$. The intercepted arc is twice the inscribed angle:
$$\text{Arc measure} = 2 \times 35° = 70°$$

---

## Inscribed Angle in a Semicircle

If an inscribed angle intercepts a semicircle (an arc of $180°$), the angle is $90°$. In other words:

> **An angle inscribed in a semicircle is always a right angle.**

This is a specific application: $\theta_{\text{inscribed}} = \frac{1}{2} \times 180° = 90°$.

This is Thales' theorem and is a favorite SAT geometry fact.

---

## Tangent Lines

A tangent line touches the circle at exactly one point (the point of tangency).

**Key fact:** The radius drawn to the point of tangency is **perpendicular** to the tangent line.

```
     |
     |  radius
     |
 ----+---- tangent line
     |
   circle
```

> **🚨 SAT TRAP ALERT:** When the SAT shows a tangent line, the radius to the tangency point is ALWAYS perpendicular. This creates a right triangle if you connect the center, the tangency point, and an external point. The SAT expects you to recognize this right triangle and apply the Pythagorean theorem.

### Worked Example 5: Tangent-Radius

**Problem:** From a point $P$ outside a circle, a tangent is drawn touching the circle at point $T$. The center of the circle is $O$. If $OP = 13$ and the radius $OT = 5$, what is the length of tangent segment $PT$?

**Solution:** $OT \perp PT$ (radius perpendicular to tangent). Triangle $OTP$ is a right triangle with right angle at $T$. By the Pythagorean theorem:

$$OT^2 + PT^2 = OP^2$$
$$5^2 + PT^2 = 13^2$$
$$25 + PT^2 = 169$$
$$PT^2 = 144$$
$$PT = 12$$

This is the 5-12-13 Pythagorean triple.

---

## Circles and Proportions

Because arc length and sector area are directly proportional to the central angle, you can set up proportions:

$$\frac{\text{Arc Length}}{\text{Circumference}} = \frac{\text{Sector Area}}{\text{Circle Area}} = \frac{\text{Central Angle}}{360°}$$

If you know three of these, you can find the fourth without going through the full formula.

---

## Practice Problems

### Problem 1
A circle has a circumference of $36\pi$. What is the area of the circle?

(A) $18\pi$  
(B) $36\pi$  
(C) $324\pi$  
(D) $1296\pi$

### Problem 2
In a circle with radius 9, what is the length of the arc subtended by a central angle of $80°$?

(A) $2\pi$  
(B) $4\pi$  
(C) $8\pi$  
(D) $16\pi$

### Problem 3
A sector of a circle has an area of $15\pi$ and a central angle of $60°$. What is the radius of the circle?

### Problem 4
In a circle, an inscribed angle measures $28°$. What is the measure of the central angle that intercepts the same arc?

(A) $14°$  
(B) $28°$  
(C) $56°$  
(D) $152°$

### Problem 5
From a point $P$ outside a circle with center $O$, two tangents $PA$ and $PB$ are drawn (where $A$ and $B$ are points of tangency). If $\angle AOB = 120°$, what is $\angle APB$?

(A) $30°$  
(B) $60°$  
(C) $90°$  
(D) $120°$

### Problem 6
A circle has a diameter of 20. A chord is 12 units long. What is the distance from the center of the circle to this chord?

(A) 6  
(B) 8  
(C) 10  
(D) 16

---

## Answers

### Problem 1 — Answer: (C) $324\pi$

$C = 2\pi r = 36\pi$, so $r = 18$. Area $= \pi r^2 = \pi(18)^2 = 324\pi$.

**Wrong-answer analysis:**
- (A) $18\pi$ — used $r$ instead of $r^2$: $\pi \times 18$
- (B) $36\pi$ — confused area with circumference
- (D) $1296\pi$ — used $2r$ as radius: $\pi(36)^2$

---

### Problem 2 — Answer: (B) $4\pi$

$$\text{Arc Length} = \frac{80}{360} \times 2\pi(9) = \frac{2}{9} \times 18\pi = 4\pi$$

**Wrong-answer analysis:**
- (A) $2\pi$ — used $\frac{80}{360} \times \pi(9)$ (area formula instead of circumference)
- (C) $8\pi$ — used $\frac{80}{360} \times 2\pi(18)$ (doubled radius)
- (D) $16\pi$ — forgot to multiply by $\frac{80}{360}$ (gave full circumference $18\pi$)

---

### Problem 3 — Answer: $r = \sqrt{90} = 3\sqrt{10}$

$$\text{Sector Area} = \frac{60}{360} \times \pi r^2 = \frac{1}{6}\pi r^2 = 15\pi$$
$$\frac{1}{6}\pi r^2 = 15\pi$$
$$\pi r^2 = 90\pi$$
$$r^2 = 90$$
$$r = \sqrt{90} = 3\sqrt{10}$$

---

### Problem 4 — Answer: (C) $56°$

An inscribed angle is half the measure of its intercepted arc, so the arc measures $2 \times 28° = 56°$. The central angle equals the arc measure, so it's $56°$.

**Wrong-answer analysis:**
- (A) $14°$ — halved the inscribed angle instead of doubling it
- (B) $28°$ — confused inscribed angle with central angle (they're only equal if the vertex is at the center)
- (D) $152°$ — used the supplementary arc: $180° - 28° = 152°$ (confused with cyclic quadrilateral)

---

### Problem 5 — Answer: (B) $60°$

In quadrilateral $OAPB$, we have:
- $\angle OAP = 90°$ (radius $\perp$ tangent)
- $\angle OBP = 90°$ (radius $\perp$ tangent)
- $\angle AOB = 120°$ (given)

Sum of interior angles of a quadrilateral: $360°$.
$$\angle APB = 360° - 90° - 90° - 120° = 60°$$

**Wrong-answer analysis:**
- (A) $30°$ — halved $60°$ incorrectly
- (C) $90°$ — assumed tangent-tangent angle is always right
- (D) $120°$ — assumed $\angle APB = \angle AOB$

---

### Problem 6 — Answer: (B) 8

The radius is half the diameter: $r = 10$. Draw the radius to one endpoint of the chord and the perpendicular from the center to the chord. This perpendicular bisects the chord, creating a right triangle with:
- Hypotenuse = radius = $10$
- Half the chord = $12/2 = 6$
- Distance from center to chord = $d$

$$d^2 + 6^2 = 10^2$$
$$d^2 + 36 = 100$$
$$d^2 = 64$$
$$d = 8$$

**Wrong-answer analysis:**
- (A) 6 — used half the chord length as the answer
- (C) 10 — used the radius as the answer
- (D) 16 — used $d = \sqrt{10^2 + 6^2} = \sqrt{136}$ misunderstanding

---

## Key Takeaways

1. **Arc measure (degrees) ≠ Arc length (distance).** Know which one the question asks for.
2. Central angle = arc measure. Inscribed angle = half the arc measure.
3. Any angle inscribed in a semicircle is $90°$ (a right angle).
4. The radius to the point of tangency is always perpendicular to the tangent line.
5. The fraction $\frac{\theta}{360°}$ is the key to both arc length and sector area.
