# Lesson 22: Pattern Recognition & Common SAT Traps

## What You'll Learn
- The 10 most common SAT Math traps, categorized and explained
- How to spot each trap **before** falling for it
- Answer choice distractor patterns — how wrong answers are engineered
- Sign errors, unit mismatches, solving for wrong variable, and more
- "NOT" and "EXCEPT" questions — a reading comprehension trap
- Extraneous solutions from squaring and domain restrictions
- A systematic pre-submission checklist to catch these traps

## SAT Context
The SAT Math section is as much a test of attention to detail as it is of mathematical ability. The test designers deliberately construct wrong answer choices to match the results of common mistakes. Approximately **20-30% of incorrect answers** on the SAT come not from not knowing the math, but from falling into a trap. Your IB AAHL training has given you strong mathematical instincts — but the SAT exploits the gap between knowing math and carefully reading a standardized test question. This lesson catalogs every major trap category so you can recognize them in real time.

---

## Trap 1: Sign Errors (Negative × Negative)

**The Trap:** Rushing through arithmetic and getting a sign wrong — especially when dealing with subtraction of negative numbers or multiplying negatives.

**Classic Example:**
Simplify: $3x - 2(x - 5)$

- **Correct:** $3x - 2x + 10 = x + 10$
- **Trap answer:** $3x - 2x - 10 = x - 10$ (forgetting that $-2 \times -5 = +10$)

**How to Spot It:** When you see a negative sign outside parentheses, slow down. Distribute carefully. Most SAT answer choices include the sign-error version.

> **🚨 SAT TRAP ALERT:** Double negatives are the most common sign trap. $-(-4) = +4$, not $-4$. When subtracting an expression like $-(x-3)$, the result is $-x+3$, not $-x-3$.

---

## Trap 2: Unit Mismatches

**The Trap:** The problem gives information in one unit but asks for the answer in another.

**Classic Example:**
"A car travels at 60 miles per hour. How many feet does it travel in 1 second?"

- You need: 60 miles/hour → feet/second
- 60 miles = $60 \times 5280 = 316,800$ feet
- 1 hour = 3600 seconds
- Speed = $316,800 / 3600 = 88$ feet/second

**The trap:** Answering 60 (just using the given number without conversion) or 316,800 (converting miles to feet but not hours to seconds).

**How to Spot It:** Scan for different units in the question vs. the answer. "Miles" and "feet," "hours" and "minutes," "feet" and "inches" — these pairings are red flags.

> **🔍 PATTERN RECOGNITION:** Rate problems (miles per hour, feet per second, gallons per minute) are the #1 unit-trap vehicle. Always check: do the time units match? Do the distance units match?

---

## Trap 3: Solving for the Wrong Variable

**The Trap:** The question asks for $2x$ (or $x+5$, or some expression), but you solve for $x$ and stop there.

**Classic Example:**
"If $3x - 7 = 14$, what is the value of $6x + 2$?"

- Solve: $3x = 21$, so $x = 7$
- But they want $6x + 2 = 6(7) + 2 = 44$
- **Trap answer:** 7 (the value of $x$, not the expression asked for)

> **🚨 SAT TRAP ALERT:** The SAT frequently includes the intermediate answer ($x = 7$) as a choice, knowing that students will solve for $x$ and immediately select that answer without reading what was actually asked.

**How to Spot It:** After solving, re-read the question. Are they asking for $x$, $2x$, $x+3$, $f(x)$, or something else? Circle what the question is actually asking for.

---

## Trap 4: Answer Choice Distractor Patterns

The SAT engineers wrong answers to match common mistakes. Here are the main distractor types:

| Distractor Type | How It's Made | Example |
|:---|:---|:---|
| **Intermediate value** | The result of step 1, before finishing | Solving for $x$ when they want $2x$ |
| **Sign error** | Right magnitude, wrong sign | $-5$ instead of $5$ |
| **Reciprocal** | $a/b$ instead of $b/a$ | $3/4$ instead of $4/3$ |
| **Right operation, wrong operand** | Used perimeter instead of area | $4s$ instead of $s^2$ |
| **Off by factor** | Forgot to square, halve, double, etc. | $r$ instead of $r^2$ |
| **Partial solution** | Solved one case but not all | One root of a quadratic |
| **No-domain-check** | Ignores domain restrictions | Including $x=1$ when denominator is $x-1$ |

---

## Trap 5: "NOT" and "EXCEPT" Questions

**The Trap:** The question asks "which of the following is NOT..." or "all of the following EXCEPT..." and you select the one that IS true.

**Classic Example:**
"Which of the following is NOT a solution to $x^2 - 5x + 6 = 0$?"

The solutions are $x = 2$ and $x = 3$. If the choices include 2, 3, and 4, the answer is 4 — but many students select 2 or 3 because they match the solutions.

> **🚨 SAT TRAP ALERT:** When you see "NOT," "EXCEPT," "CANNOT," or "LEAST likely," underline or circle the word. Then mentally reframe: "I'm looking for the answer that DOESN'T fit." This small habit prevents the most frustrating type of wrong answer.

---

## Trap 6: Extraneous Solutions from Squaring

**The Trap:** Solving an equation with radicals by squaring both sides introduces extraneous solutions that don't satisfy the original equation.

**Classic Example:**
Solve: $\sqrt{x+3} = x-3$

Square both sides: $x+3 = (x-3)^2 = x^2 - 6x + 9$
$$0 = x^2 - 7x + 6 = (x-1)(x-6)$$
$x = 1$ or $x = 6$

Check $x = 1$: $\sqrt{4} = 2$, but $1-3 = -2$. $2 \neq -2$. ❌ Extraneous!
Check $x = 6$: $\sqrt{9} = 3$, and $6-3 = 3$. ✓

**Answer: $x = 6$ only.**

> **🔍 PATTERN RECOGNITION:** When a question involves squaring both sides, the answer is always "check your solutions." At least one solution from the squared equation will often be extraneous. The SAT includes the extraneous solution as a distractor.

---

## Trap 7: Domain Restrictions

**The Trap:** Forgetting that denominators can't be zero, or that even-root radicands must be non-negative.

**Classic Example:**
"The function $f(x) = \frac{x-2}{x^2-4}$ is undefined for which value of $x$?"

Simplify: $\frac{x-2}{(x-2)(x+2)} = \frac{1}{x+2}$ (for $x \neq 2$)

The function is undefined when the denominator is zero: $x = 2$ or $x = -2$. Even though the expression simplifies, the original function is undefined at $x=2$.

**The trap:** Answering $x = -2$ only, forgetting that $x=2$ also makes the original denominator zero.

> **🚨 SAT TRAP ALERT:** Simplifying an expression can hide domain restrictions. Always check the ORIGINAL form for domain issues, not the simplified form.

---

## Trap 8: Assuming Diagrams Are to Scale

**The Trap:** On the SAT, figures are drawn to scale **unless stated otherwise** — but some are labeled "Note: Figure not drawn to scale." Over-relying on visual appearance when the problem says "not drawn to scale."

**How to Spot It:** If the problem says "Note: Figure not drawn to scale," trust the given numbers, NOT how the figure looks. A line that looks shorter might actually be longer.

---

## Trap 9: Distribution Errors with Fractions

**The Trap:** Incorrectly distributing when fractions are involved.

**Example:**
$$\frac{1}{2}(x + 4) = 3$$

- **Correct:** Multiply both sides by 2: $x+4 = 6$, $x = 2$
- **Trap:** $\frac{x}{2} + 4 = 3$, then $x/2 = -1$, $x = -2$ (forgot to distribute to the 4)

---

## Trap 10: Missing Multiple Solutions

**The Trap:** When solving equations with even powers or absolute values, there are often two solutions. The SAT includes only one as a distractor.

**Example:** $x^2 = 25$ → $x = 5$ or $x = -5$. Answering only $5$ is incomplete.

Similarly, $|x-2| = 5$ → $x-2 = 5$ or $x-2 = -5$ → $x = 7$ or $x = -3$.

> **🔍 PATTERN RECOGNITION:** Whenever you see $x^2$, $|x|$, or any even power = constant, there are TWO solutions (unless the context restricts it). Check whether the answer expects both.

---

## The Pre-Submission Checklist

Before selecting an answer, run through this 10-second mental checklist:

1. **Did I answer what was asked?** (Not an intermediate value)
2. **Are the units correct?** (Matching what's asked)
3. **Did I check for ±?** (Even powers, absolute values)
4. **Are there domain restrictions?** (Denominators, radicals)
5. **Did I check for extraneous solutions?** (After squaring)
6. **Did I read NOT/EXCEPT?** (If present)
7. **Is my sign correct?** (Especially with double negatives)
8. **Did I consider all cases?** (Multiple solutions, if any)

---

## Practice Problems

### Problem 1
If $2x - 5 = 7$, what is the value of $4x + 3$?

(A) 6  
(B) 12  
(C) 27  
(D) 31

### Problem 2
Which of the following is NOT a solution to $(x-1)(x+4)(x-3) = 0$?

(A) $-4$  
(B) $-1$  
(C) $1$  
(D) $3$

### Problem 3
Solve for $x$: $\sqrt{2x+3} = x$

(A) $x = -1$ only  
(B) $x = 3$ only  
(C) $x = -1$ and $x = 3$  
(D) No solution

### Problem 4
The function $f(x) = \frac{x+2}{x^2-4}$ is undefined at how many values of $x$?

(A) 0  
(B) 1  
(C) 2  
(D) Infinitely many

### Problem 5
A rectangle has an area of 48 square feet. What is its area in square inches? (1 foot = 12 inches)

(A) 4  
(B) 576  
(C) 6,912  
(D) 48

### Problem 6
Solve: $|2x - 1| = 7$

(A) $x = 4$ only  
(B) $x = -3$ only  
(C) $x = 4$ and $x = -3$  
(D) No solution

### Problem 7
Simplify: $\frac{1}{3}(6x - 9) + 2$

(A) $2x - 1$  
(B) $2x - 3$  
(C) $2x + 5$  
(D) $2x - 5$

### Problem 8
The expression $\frac{x}{x-3}$ is undefined when $x =$ ?

(A) $-3$  
(B) $0$  
(C) $3$  
(D) $0$ and $3$

---

## Answers

### Problem 1 — Answer: (C) 27

$2x - 5 = 7$ → $2x = 12$ → $x = 6$. Then $4x + 3 = 4(6) + 3 = 24 + 3 = 27$.

- **(A) 6:** The value of $x$ — classic "solved for wrong variable" trap
- **(B) 12:** The value of $2x$ — another intermediate value
- **(D) 31:** $4(7) + 3$, using the right-hand-side (7) as $x$

---

### Problem 2 — Answer: (B) $-1$

Solutions to $(x-1)(x+4)(x-3) = 0$ are $x = 1$, $x = -4$, and $x = 3$. The value $-1$ is NOT a solution.

- **(A) $-4$:** IS a solution — selected if you missed "NOT"
- **(C) $1$:** IS a solution — selected if you missed "NOT"
- **(D) $3$:** IS a solution — selected if you missed "NOT"

---

### Problem 3 — Answer: (B) $x = 3$ only

Square both sides: $2x+3 = x^2$ → $x^2 - 2x - 3 = 0$ → $(x-3)(x+1) = 0$. Candidates: $x = 3$, $x = -1$.

Check $x = -1$: $\sqrt{2(-1)+3} = \sqrt{1} = 1$, but $x = -1$. $1 \neq -1$. ❌

Check $x = 3$: $\sqrt{2(3)+3} = \sqrt{9} = 3$. ✓

- **(A) $x=-1$ only:** Both candidates found, wrong one kept
- **(C) Both:** Failed to check for extraneous solutions
- **(D) No solution:** Gave up after finding the extraneous issue

---

### Problem 4 — Answer: (C) 2

Denominator: $x^2 - 4 = 0$ → $(x-2)(x+2) = 0$ → $x = 2$ or $x = -2$.

Even though $f(x) = \frac{x+2}{(x-2)(x+2)} = \frac{1}{x-2}$ simplifies, the original function is undefined at BOTH $x=2$ and $x=-2$. The simplification hides the domain restriction at $x=-2$ (the cancellation is only valid when $x \neq -2$).

- **(A) 0:** Thought the function is always defined
- **(B) 1:** Only caught one zero of the denominator ($x=2$ or $x=-2$)

---

### Problem 5 — Answer: (C) 6,912

48 square feet = $48 \times (12 \times 12) = 48 \times 144 = 6,912$ square inches.

- **(A) 4:** Divided 48 by 12 (used linear conversion for area — wrong!)
- **(B) 576:** Multiplied by 12 ($48 \times 12$) — used linear conversion
- **(D) 48:** Ignored unit conversion entirely

---

### Problem 6 — Answer: (C) $x = 4$ and $x = -3$

$|2x-1| = 7$ means:
- $2x-1 = 7$ → $2x = 8$ → $x = 4$
- $2x-1 = -7$ → $2x = -6$ → $x = -3$

- **(A) $x=4$ only:** Only solved the positive case
- **(B) $x=-3$ only:** Only solved the negative case
- **(D) No solution:** Absolute value equations always have solutions when the RHS is positive

---

### Problem 7 — Answer: (A) $2x - 1$

$\frac{1}{3}(6x - 9) + 2 = \frac{6x}{3} - \frac{9}{3} + 2 = 2x - 3 + 2 = 2x - 1$

- **(B) $2x-3$:** Forgot to add the $+2$ at the end
- **(C) $2x+5$:** $-3+2$ computed as $+5$ (sign error)
- **(D) $2x-5$:** $-3+2$ computed as $-5$ (sign error)

---

### Problem 8 — Answer: (C) 3

$\frac{x}{x-3}$ is undefined when the denominator $x-3 = 0$, so $x = 3$.

- **(A) $-3$:** Sign error — solved $x+3=0$ instead of $x-3=0$
- **(B) $0$:** Confused with numerator being zero (which makes the expression 0, not undefined)
- **(D) $0$ and $3$:** Combined both errors above

---

## Key Takeaways

1. The SAT deliberately includes wrong answers that match the result of common mistakes. Recognize the distractor patterns.
2. Always re-read the question after solving: are they asking for $x$, $2x$, or something else?
3. "NOT" and "EXCEPT" — underline these words and reframe the question.
4. Squaring both sides? Check for extraneous solutions.
5. Unit mismatches: square the conversion factor for area, cube it for volume.
6. Even powers and absolute values: there are usually two solutions.
7. Domain restrictions: denominators $\neq 0$, even-root radicands $\geq 0$.
