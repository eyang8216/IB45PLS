# Lesson 17: Geometry — Right Triangles & Trigonometry (SAT)

## What You'll Learn
- Pythagorean theorem and its applications in SAT geometry problems
- SOHCAHTOA: sine, cosine, and tangent definitions for right triangles
- How to use special right triangle ratios (30-60-90, 45-45-90) with trig
- The cofunction identity: $\sin(x) = \cos(90° - x)$
- How SAT trigonometry differs from IB AAHL trigonometry (much simpler!)
- Common mix-up traps between sine/cosine and opposite/adjacent

## SAT Context
Trigonometry on the SAT is deliberately limited. The SAT tests only **right triangle trigonometry** — SOHCAHTOA and the complementary angle relationship. There is **no Law of Sines, no Law of Cosines, no identities** beyond $\sin(x) = \cos(90°-x)$, no radians, no unit circle beyond the first quadrant, no compound angle formulas, and no trigonometric equations. If you've completed IB AAHL, you have vastly more trigonometry knowledge than the SAT requires. The challenge is not the math — it's avoiding careless errors on straightforward problems. Expect **2–4 trigonometry questions** across both modules.

---

## Pythagorean Theorem

For any right triangle with legs $a$ and $b$ and hypotenuse $c$:

$$a^2 + b^2 = c^2$$

> **🔍 PATTERN RECOGNITION:** The SAT almost always uses Pythagorean triples (3-4-5, 5-12-13, 8-15-17, 7-24-25) or their multiples. If you recognize these, you can skip the calculation entirely. The most common triple on the SAT is 3-4-5 and its multiples (6-8-10, 9-12-15, etc.).

### Worked Example 1: Pythagorean Triple

**Problem:** In right triangle $ABC$ with right angle at $C$, $AC = 9$ and $BC = 12$. Find $AB$.

**Solution:** Recognize the 3-4-5 triple scaled by 3: $9 = 3 \times 3$, $12 = 4 \times 3$, so the hypotenuse is $5 \times 3 = 15$.

**Using the formula:** $AB^2 = 9^2 + 12^2 = 81 + 144 = 225$, $AB = \sqrt{225} = 15$.

---

## SOHCAHTOA

For a right triangle with angle $\theta$:

$$\sin\theta = \frac{\text{Opposite}}{\text{Hypotenuse}} \quad \text{(SOH)}$$

$$\cos\theta = \frac{\text{Adjacent}}{\text{Hypotenuse}} \quad \text{(CAH)}$$

$$\tan\theta = \frac{\text{Opposite}}{\text{Adjacent}} \quad \text{(TOA)}$$

> **🚨 SAT TRAP ALERT:** "Opposite" and "adjacent" are relative to the angle you're using. The side opposite angle $A$ is adjacent to angle $B$, and vice versa. When a right triangle problem gives you two angles, make sure you know which angle you're working with before labeling sides.

### Identifying Sides Relative to an Angle

```
     A
     |\
     | \
  opp|  \ hyp
     |   \
     |____\
       adj   B
```

- **Hypotenuse:** Always the longest side, opposite the right angle.
- **Opposite:** The side across from the angle in question.
- **Adjacent:** The side next to the angle (that is NOT the hypotenuse).

> **🚨 SAT TRAP ALERT:** The most common SAT trig error is mixing up $\sin$ and $\cos$. Remember: **S**ine uses the **O**pposite side (S-OH), **C**osine uses the **A**djacent side (C-AH). Students who rush often pick $\cos$ when the problem calls for $\sin$, and vice versa.

---

## Finding Missing Sides with Trig

When you know one angle (other than the right angle) and one side, you can find any other side using SOHCAHTOA.

### Worked Example 2: Using Sine to Find a Side

**Problem:** In right triangle $ABC$ with right angle at $C$, $\angle A = 35°$ and the hypotenuse $AB = 20$. Find $BC$, the side opposite angle $A$.

**Solution:** $\sin(35°) = \frac{BC}{AB} = \frac{BC}{20}$, so $BC = 20 \cdot \sin(35°) \approx 20 \times 0.5736 \approx 11.47$.

---

## Finding Missing Angles with Inverse Trig

When you know two sides and need to find an angle, use inverse trig:

- $\theta = \sin^{-1}\left(\frac{\text{opp}}{\text{hyp}}\right)$
- $\theta = \cos^{-1}\left(\frac{\text{adj}}{\text{hyp}}\right)$
- $\theta = \tan^{-1}\left(\frac{\text{opp}}{\text{adj}}\right)$

> **🔍 PATTERN RECOGNITION:** On the SAT, a question that requires inverse trig will typically have answer choices that are easy to distinguish. You don't need exact decimal values — the SAT provides a calculator (Desmos) for the math modules, and you can compute these directly. But often, the answer is a recognizable angle (30°, 45°, 60°) that you can identify from the side ratios.

---

## Special Right Triangles and Trig Values

You should know (or be able to derive quickly) these exact values:

| $\theta$ | $\sin\theta$ | $\cos\theta$ | $\tan\theta$ |
|:---:|:---:|:---:|:---:|
| $30°$ | $\frac{1}{2}$ | $\frac{\sqrt{3}}{2}$ | $\frac{1}{\sqrt{3}} = \frac{\sqrt{3}}{3}$ |
| $45°$ | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{2}}{2}$ | $1$ |
| $60°$ | $\frac{\sqrt{3}}{2}$ | $\frac{1}{2}$ | $\sqrt{3}$ |

### Deriving from the Triangles

**For 30° and 60°:** Use the 30-60-90 triangle with sides $1 : \sqrt{3} : 2$.

- $\sin(30°) = \frac{\text{opp}}{\text{hyp}} = \frac{1}{2}$
- $\cos(30°) = \frac{\text{adj}}{\text{hyp}} = \frac{\sqrt{3}}{2}$
- $\tan(30°) = \frac{\text{opp}}{\text{adj}} = \frac{1}{\sqrt{3}}$

- $\sin(60°) = \frac{\sqrt{3}}{2}$, $\cos(60°) = \frac{1}{2}$, $\tan(60°) = \sqrt{3}$

**For 45°:** Use the 45-45-90 triangle with sides $1 : 1 : \sqrt{2}$.

- $\sin(45°) = \frac{1}{\sqrt{2}} = \frac{\sqrt{2}}{2}$
- $\cos(45°) = \frac{1}{\sqrt{2}} = \frac{\sqrt{2}}{2}$
- $\tan(45°) = 1$

---

## The Cofunction Identity

For complementary angles (angles that sum to $90°$):

$$\sin(x) = \cos(90° - x)$$
$$\cos(x) = \sin(90° - x)$$

> **🔍 PATTERN RECOGNITION:** This is the ONLY trigonometric identity tested on the SAT (beyond SOHCAHTOA). If you see $\sin(20°) = \cos(k°)$, the answer is $k = 70°$ because $20° + 70° = 90°$. This pattern is so predictable that you can answer without computing any values.

### Worked Example 3: Cofunction

**Problem:** In right triangle $PQR$ with right angle at $Q$, $\sin(P) = \frac{5}{13}$. What is $\cos(R)$?

**Solution:** In a right triangle, angles $P$ and $R$ are complementary ($P + R = 90°$). By the cofunction identity: $\cos(R) = \sin(90° - R) = \sin(P)$. Since $\sin(P) = \frac{5}{13}$, we have $\cos(R) = \frac{5}{13}$.

**Alternatively:** In the right triangle, the side opposite $P$ is the side adjacent to $R$. So $\sin(P) = \frac{\text{opp}_P}{\text{hyp}} = \frac{\text{adj}_R}{\text{hyp}} = \cos(R)$. They must be equal.

---

## SAT vs. AAHL Trigonometry

| Feature | IB AAHL | SAT |
|:---|:---|:---|
| Trigonometric Identities | Many (Pythagorean, double-angle, sum/difference, etc.) | Only $\sin(x) = \cos(90°-x)$ |
| Radians | Heavy use | Not tested |
| Unit Circle | Full circle, all quadrants | Only first quadrant implied |
| Law of Sines/Cosines | Yes | **No** |
| Solving Trig Equations | Yes, with general solutions | **No** |
| Compound Angles | $\sin(A \pm B)$, $\tan(2A)$, etc. | **No** |
| Reciprocal Functions | $\csc$, $\sec$, $\cot$ | **No** (only $\sin$, $\cos$, $\tan$) |
| Inverse Trig | $\arcsin$, $\arccos$, $\arctan$ | $\sin^{-1}$, $\cos^{-1}$, $\tan^{-1}$ on calculator |

> **🚨 SAT TRAP ALERT:** If you find yourself reaching for an AAHL trig technique (double-angle formula, law of sines, etc.), STOP. You're overcomplicating it. The SAT trig question can ALWAYS be solved with just SOHCAHTOA and the Pythagorean theorem. The hard part is not the math — it's reading the diagram correctly.

---

## Right Triangle Word Problems

### Angle of Elevation / Depression

These are just right triangles in disguise:
- **Angle of elevation:** Angle measured upward from horizontal
- **Angle of depression:** Angle measured downward from horizontal

```
    *  (object)
   /|
  / |
 /  | height
/θ  |
----+
eye  horizontal
```

> **🔍 PATTERN RECOGNITION:** SAT word problems with "angle of elevation" or "angle of depression" are always right triangle trig problems. Draw the triangle, label the known side and angle, identify which side you need, and use the appropriate trig ratio.

### Worked Example 4: Word Problem

**Problem:** A ladder 25 feet long leans against a wall. The ladder makes a $60°$ angle with the ground. How high up the wall does the ladder reach?

**Solution:** The ladder is the hypotenuse (25 ft). The height is opposite the $60°$ angle.

$$\sin(60°) = \frac{\text{height}}{25}$$
$$\frac{\sqrt{3}}{2} = \frac{h}{25}$$
$$h = 25 \cdot \frac{\sqrt{3}}{2} = \frac{25\sqrt{3}}{2} \approx 21.65 \text{ feet}$$

---

## Practice Problems

### Problem 1
In right triangle $ABC$ with right angle at $C$, $AB = 17$ and $BC = 8$. What is $AC$?

(A) 9  
(B) 15  
(C) $\sqrt{353}$  
(D) 25

### Problem 2
In right triangle $DEF$ with right angle at $E$, $\angle D = 40°$ and $DE = 10$. Which expression gives $DF$ (the hypotenuse)?

(A) $10 \sin(40°)$  
(B) $10 \cos(40°)$  
(C) $\frac{10}{\sin(40°)}$  
(D) $\frac{10}{\cos(40°)}$

### Problem 3
In a 30-60-90 right triangle, the hypotenuse is 12. What is the area of the triangle?

(A) $18\sqrt{3}$  
(B) $36\sqrt{3}$  
(C) $72$  
(D) $18$

### Problem 4
In right triangle $XYZ$ with right angle at $Y$, $\sin(X) = \frac{12}{13}$. What is $\tan(X)$?

(A) $\frac{5}{12}$  
(B) $\frac{12}{5}$  
(C) $\frac{5}{13}$  
(D) $\frac{13}{5}$

### Problem 5
In right triangle $PQR$ with right angle at $Q$, $\cos(P) = 0.6$. What is $\sin(R)$?

### Problem 6
A 30-foot ramp makes a $10°$ angle with the ground. To the nearest tenth of a foot, what horizontal distance does the ramp cover?

---

## Answers

### Problem 1 — Answer: (B) 15

$AB$ is the hypotenuse = 17, $BC$ is a leg = 8. Using Pythagorean theorem:

$$AC^2 + 8^2 = 17^2$$
$$AC^2 + 64 = 289$$
$$AC^2 = 225$$
$$AC = 15$$

This is the 8-15-17 Pythagorean triple.

**Wrong-answer analysis:**
- (A) 9 — might have subtracted: $17 - 8 = 9$ (not how the theorem works)
- (C) $\sqrt{353}$ — might have added squares incorrectly: $17^2 + 8^2 = 289 + 64 = 353$
- (D) 25 — might have added: $17 + 8 = 25$

---

### Problem 2 — Answer: (D) $\frac{10}{\cos(40°)}$

From angle $D$: $DE$ is the adjacent side (next to $D$, not the hypotenuse). $DF$ is the hypotenuse.

$$\cos(40°) = \frac{\text{adj}}{\text{hyp}} = \frac{DE}{DF} = \frac{10}{DF}$$
$$DF = \frac{10}{\cos(40°)}$$

**Wrong-answer analysis:**
- (A) $10\sin(40°)$ — would give the opposite side, not the hypotenuse
- (B) $10\cos(40°)$ — would give the adjacent side if DF were known and you were solving for DE
- (C) $\frac{10}{\sin(40°)}$ — uses sine instead of cosine; would be correct if 10 were the opposite side

---

### Problem 3 — Answer: (A) $18\sqrt{3}$

In a 30-60-90 triangle with hypotenuse 12: $2x = 12$, so $x = 6$ (shortest leg). The longer leg is $x\sqrt{3} = 6\sqrt{3}$. Area = $\frac{1}{2} \times \text{base} \times \text{height} = \frac{1}{2} \times 6 \times 6\sqrt{3} = 18\sqrt{3}$.

**Wrong-answer analysis:**
- (B) $36\sqrt{3}$ — doubled the area (forgot the $\frac{1}{2}$)
- (C) 72 — used $6 \times 12$ (leg × hypotenuse)
- (D) 18 — used the legs without $\sqrt{3}$

---

### Problem 4 — Answer: (B) $\frac{12}{5}$

$\sin(X) = \frac{\text{opp}}{\text{hyp}} = \frac{12}{13}$. In a right triangle at $Y$, the side opposite $X$ is $YZ$, and the hypotenuse is $XZ$. So $YZ = 12$ and $XZ = 13$. Using Pythagorean theorem: $XY^2 + 12^2 = 13^2$, so $XY^2 = 169 - 144 = 25$, $XY = 5$. Then $\tan(X) = \frac{\text{opp}}{\text{adj}} = \frac{YZ}{XY} = \frac{12}{5}$.

**Wrong-answer analysis:**
- (A) $\frac{5}{12}$ — this is $\cot(X)$, the reciprocal of tangent
- (C) $\frac{5}{13}$ — this is $\cos(X)$, mixing up trig ratios
- (D) $\frac{13}{5}$ — this is $\csc(X)$, not tested on the SAT but a distractor

---

### Problem 5 — Answer: $\sin(R) = 0.6$

In a right triangle at $Q$, angles $P$ and $R$ are complementary: $P + R = 90°$. By the cofunction identity, $\sin(R) = \cos(90° - R) = \cos(P) = 0.6$.

---

### Problem 6 — Answer: Approximately 29.5 feet

The ramp is the hypotenuse (30 ft). The horizontal distance is adjacent to the $10°$ angle.

$$\cos(10°) = \frac{\text{horizontal}}{30}$$
$$\text{horizontal} = 30 \cdot \cos(10°) \approx 30 \times 0.9848 \approx 29.5 \text{ feet}$$

---

## Key Takeaways

1. The SAT only tests right triangle trig: SOHCAHTOA and $\sin(x) = \cos(90°-x)$. Nothing more.
2. Recognize Pythagorean triples (especially 3-4-5, 5-12-13, 8-15-17) to save time.
3. The cofunction identity is the most predictable trig question on the SAT — complementary angles swap sine and cosine.
4. Always identify which angle you're working with before labeling opposite/adjacent.
5. Don't overcomplicate — if you're using AAHL techniques, you're doing too much.
