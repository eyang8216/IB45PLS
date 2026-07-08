# Lesson 25: Circuits II — Series and Parallel

## What You'll Learn

By the end of this lesson, you will be able to:
- Identify whether resistors are connected in series or in parallel
- Calculate equivalent resistance for series and parallel combinations
- Determine current through and voltage across each resistor in any series-parallel circuit
- Never again add parallel resistances directly

---

## ⚠️ READ THIS FIRST — The Most Important Paragraph in This Lesson

On your diagnostic test, you were given a 6.0 Ω resistor and a 3.0 Ω resistor connected in parallel. You added them directly and wrote "equivalent resistance is 9 Ω." That is the series rule. For parallel, the correct answer is 2.0 Ω. This is not a small mistake — it is the single most common error in all of circuit analysis, and it leads to every subsequent calculation being wrong. By the end of this lesson, you will understand WHY parallel is different, you will be able to calculate it correctly every time, and you will have a physical intuition that catches this error before it reaches the page.

---

## 1. What Is a Circuit?

### 1.1 Why This Matters

A circuit is a closed conducting path through which electric charge can flow. The word "circuit" shares a root with "circle" — the path must be complete. If the path is broken anywhere, no current flows anywhere in that loop. Every circuit analysis problem begins with identifying the paths that charge can take from the positive terminal of the battery, through the circuit, and back to the negative terminal.

### 1.2 The Two Fundamental Ways to Connect Components

There are exactly two ways to connect two components together: series and parallel. Every complex circuit you will ever see is just a combination of these two patterns repeated at different scales. If you master series and parallel, you can analyze any circuit.

- **Series:** Components are connected end to end, one after another, forming a single continuous path. The same current must flow through each component because there is only one path.
- **Parallel:** Components are connected to the same two nodes. Each component provides an independent path for current. The voltage across each component is the same because they share the same two connection points.

---

## 2. Series Circuits

### 2.1 What Series Means Physically

Imagine a single-lane road with three toll booths placed one after another. Every car must pass through every toll booth. The traffic flow (current) through each booth is identical because there is only one road. The total delay (voltage drop) is the sum of the delays at each booth.

This is exactly how series circuits work. Charge flows through each resistor in turn. There is no junction where charge can choose an alternative path, so the same current passes through every resistor.

### 2.2 The Three Rules for Series Circuits

**Rule 1 — Current is the same everywhere:**
$$I = I_1 = I_2 = I_3 = \dots$$

This is not an approximation. It is a direct consequence of charge conservation: charge cannot appear or disappear, so whatever flows into a series of components must flow out of each one at the same rate. If the current were different at different points, charge would be piling up somewhere, which does not happen in steady-state circuits.

**Rule 2 — Voltages add:**
$$V_{\text{total}} = V_1 + V_2 + V_3 + \dots$$

As charge flows through each resistor, it loses electrical potential energy. The total energy lost per unit charge (total voltage drop) is the sum of the losses across each resistor. Think of it like water flowing downhill through a series of waterfalls: the total drop in height equals the sum of the drops at each waterfall.

**Rule 3 — Resistances add directly:**
$$R_{\text{total}} = R_1 + R_2 + R_3 + \dots$$

Because the same current flows through each resistor, and the total voltage is the sum of individual voltages, we can write:
$$V_{\text{total}} = V_1 + V_2 = IR_1 + IR_2 = I(R_1 + R_2)$$
Dividing by $I$: $R_{\text{total}} = R_1 + R_2$.

The total resistance in series is always LARGER than any individual resistance. Adding more resistors in series makes it harder for current to flow.

### 2.3 The Voltage Divider Rule

In a series circuit, the total voltage divides across the resistors in proportion to their resistance. If you have two resistors $R_1$ and $R_2$ in series across a total voltage $V$:

$$V_1 = \frac{R_1}{R_1 + R_2} \times V$$
$$V_2 = \frac{R_2}{R_1 + R_2} \times V$$

The larger resistor gets a larger share of the voltage. If $R_1 = 2R_2$, then $V_1 = 2V_2$. This rule is NOT in the IB Data Booklet — you should memorise it. It appears constantly in sensor circuits, potentiometer problems, and practical electronics.

---

## 3. Parallel Circuits

### 3.1 What Parallel Means Physically

Now imagine a multi-lane highway. Cars approach a junction and can choose any lane. Each lane provides an independent path to the destination. Adding more lanes reduces overall resistance to traffic flow — more cars can get through in the same time.

This is exactly how parallel circuits work. Charge arrives at a junction and splits among multiple paths, then recombines. Each path provides an independent route for current. Adding a resistor in parallel provides an ADDITIONAL path, which makes it EASIER for current to flow — so the total resistance DECREASES.

### 3.2 The Three Rules for Parallel Circuits

**Rule 1 — Voltage is the same across all branches:**
$$V = V_1 = V_2 = V_3 = \dots$$

All components in parallel share the same two nodes. The potential difference between those two nodes is a single value. Every path between those nodes experiences that same potential difference. This is the defining feature of a parallel connection.

**Rule 2 — Currents add:**
$$I_{\text{total}} = I_1 + I_2 + I_3 + \dots$$

Charge conserves at the junction. The total current entering the junction equals the sum of currents leaving it through each branch. This is Kirchhoff's junction rule, which we study formally in Lesson 26.

**Rule 3 — Reciprocals of resistance add:**
$$\frac{1}{R_{\text{total}}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} + \dots$$

THIS is the rule you must never confuse with the series rule. It comes from applying Rules 1 and 2 together with Ohm's Law:

In each branch: $I_1 = V/R_1$, $I_2 = V/R_2$, and so on.
Total current: $I = I_1 + I_2 = V/R_1 + V/R_2 = V(1/R_1 + 1/R_2)$.
But $I = V/R_{\text{total}}$, so $1/R_{\text{total}} = 1/R_1 + 1/R_2$.

### 3.3 WHY Parallel Reduces Total Resistance — Physical Intuition

This is so important it deserves its own section. Many students memorise the reciprocal formula without understanding WHY the total resistance decreases. Here is the physical reason:

Resistance is opposition to current flow. In a parallel circuit, adding another resistor provides another pathway for charge to flow through. The battery now has multiple routes to push charge around the circuit. More routes means less overall opposition. The total current from the battery increases (because $I = V/R$, and $R$ has decreased), even though $V$ is unchanged.

If you have two identical resistors $R$ in parallel, the total resistance is $R/2$, not $2R$. If you have ten in parallel, it is $R/10$. This is the opposite of what happens in series.

### 3.4 The Product-Over-Sum Shortcut (Two Resistors Only)

For exactly two resistors in parallel, the formula simplifies:

$$R_{\text{total}} = \frac{R_1 R_2}{R_1 + R_2}$$

This is derived from the reciprocal rule and is valid ONLY for two resistors. For three or more, you must use the reciprocal method or reduce in pairs.

Worked: $R_1 = 6.0\text{ Ω}$, $R_2 = 3.0\text{ Ω}$:
$$R_{\text{total}} = \frac{6.0 \times 3.0}{6.0 + 3.0} = \frac{18}{9.0} = 2.0\text{ Ω}$$

This is the answer you should have gotten on your diagnostic.

### 3.5 Special Case — Identical Resistors in Parallel

If you have $n$ identical resistors, each of resistance $R$, connected in parallel:

$$R_{\text{total}} = \frac{R}{n}$$

Three 6 Ω resistors in parallel give $6/3 = 2\text{ Ω}$. Ten 100 Ω resistors in parallel give $100/10 = 10\text{ Ω}$. This is the fastest check — if you ever calculate a parallel total that is LARGER than any individual resistor, you have made a mistake.

### 3.6 Common Misconceptions — Addressed Directly

**Misconception 1:** "Parallel resistors add the same way as series resistors." They emphatically do not. In series, you add resistances directly; in parallel, you add reciprocals. The total resistance in parallel is always LESS than the smallest individual resistance.

**Misconception 2:** "Two paths must have twice the resistance of one." Consider two identical doors side by side. Do two doors make it harder to leave the room? No — they make it easier. Two parallel paths reduce the overall obstruction, they do not increase it.

**Misconception 3:** "I should always use the product-over-sum formula." Product-over-sum works only for exactly two resistors. For three resistors, you cannot simply multiply all three and divide by their sum. Learn the reciprocal method — it works for any number.

**Misconception 4:** "Current splits equally in parallel." Current splits in inverse proportion to resistance. The path with lower resistance gets MORE current. If one branch is 3 Ω and another is 6 Ω in parallel across 12 V, the currents are 4 A and 2 A respectively — not 3 A each.

---

## 4. Series vs. Parallel — Direct Comparison

This table is worth studying until you can reproduce it from memory:

| Property | Series | Parallel |
|----------|--------|----------|
| Connection | End-to-end, one path | Same two nodes, multiple paths |
| Current | Same through all: $I = I_1 = I_2$ | Splits, then adds: $I = I_1 + I_2$ |
| Voltage | Divides: $V = V_1 + V_2$ | Same across all: $V = V_1 = V_2$ |
| Resistance | Adds directly: $R = R_1 + R_2$ | Reciprocals add: $\frac{1}{R} = \frac{1}{R_1} + \frac{1}{R_2}$ |
| Total $R$ compared to individuals | Total is LARGER than any one | Total is SMALLER than any one |
| Adding another resistor... | Increases total $R$ | Decreases total $R$ |
| If one resistor fails (open)... | All current stops | Current continues in other branches |

---

## 5. Combined Series-Parallel Circuits

### 5.1 The Reduction Method

Real circuits contain both series and parallel combinations. The method for solving them is called "circuit reduction." You replace small groups of resistors with their equivalent single resistance, working from the innermost part outward, until the entire circuit is a single equivalent resistance. Then you work backward, finding currents and voltages at each stage.

**The method step by step:**

1. Identify any resistors that are clearly in series (same current, no junctions between them) or clearly in parallel (share both ends). Start with the innermost group.
2. Replace that group with its equivalent resistance.
3. Redraw the simplified circuit.
4. Repeat until only one equivalent resistance remains.
5. Use Ohm's Law with the battery voltage and total resistance to find the total current.
6. Work backward through each simplification, finding voltage across and current through each original resistor.

### 5.2 How to Tell Series from Parallel at a Glance

This is a skill that comes with practice. Here is a reliable test:

- **Series test:** Do the two resistors share exactly one node, with nothing else connected to that node? If current has no choice but to flow through one then the other, they are in series.
- **Parallel test:** Do the two resistors share BOTH nodes? If you can trace a path from one end of resistor A to one end of resistor B without passing through any other component, AND the same is true for their other ends, they are in parallel.

If neither test passes, the resistors are in a more complex arrangement that requires Kirchhoff's Laws (Lesson 26).

---

## Worked Examples

### Worked Example 25.1 — Simple Series Circuit

**Problem:** A 9.0 V battery is connected to two resistors in series: 4.0 Ω and 8.0 Ω. Calculate the total resistance, the current in the circuit, and the voltage across each resistor.

**Approach:** For series, we add resistances directly, then use Ohm's Law to find the current. The voltage across each resistor follows from $V = IR$.

**Solution:**

Total resistance:
$$R_{\text{total}} = 4.0 + 8.0 = 12.0\text{ Ω}$$

Current (same through both):
$$I = \frac{V}{R_{\text{total}}} = \frac{9.0}{12.0} = 0.75\text{ A}$$

Voltage across 4.0 Ω:
$$V_1 = IR_1 = (0.75)(4.0) = 3.0\text{ V}$$

Voltage across 8.0 Ω:
$$V_2 = IR_2 = (0.75)(8.0) = 6.0\text{ V}$$

Check: $V_1 + V_2 = 3.0 + 6.0 = 9.0\text{ V} = V_{\text{battery}}$ ✓

**Why this makes sense:** The larger resistor (8 Ω) gets twice the voltage of the smaller one (4 Ω) because $V = IR$ and $I$ is the same. The voltages sum to the battery voltage, confirming the loop rule.

---

### Worked Example 25.2 — Simple Parallel Circuit

**Problem:** A 12 V battery is connected to two resistors in parallel: 6.0 Ω and 3.0 Ω. Calculate the total resistance, the total current drawn from the battery, and the current through each resistor.

**Approach:** For parallel, we use the reciprocal rule for resistance. The voltage across each branch is the full battery voltage. We can find branch currents directly using Ohm's Law, then sum them to get the total.

**Solution:**

Total resistance:
$$\frac{1}{R_{\text{total}}} = \frac{1}{6.0} + \frac{1}{3.0} = \frac{1}{6.0} + \frac{2}{6.0} = \frac{3}{6.0}$$
$$R_{\text{total}} = \frac{6.0}{3} = 2.0\text{ Ω}$$

Or using the product-over-sum shortcut:
$$R_{\text{total}} = \frac{6.0 \times 3.0}{6.0 + 3.0} = \frac{18}{9.0} = 2.0\text{ Ω}$$

Total current from battery:
$$I_{\text{total}} = \frac{V}{R_{\text{total}}} = \frac{12}{2.0} = 6.0\text{ A}$$

Current through 6.0 Ω:
$$I_1 = \frac{V}{R_1} = \frac{12}{6.0} = 2.0\text{ A}$$

Current through 3.0 Ω:
$$I_2 = \frac{V}{R_2} = \frac{12}{3.0} = 4.0\text{ A}$$

Check: $I_1 + I_2 = 2.0 + 4.0 = 6.0\text{ A} = I_{\text{total}}$ ✓

**Why this makes sense:** The 3 Ω resistor draws twice the current of the 6 Ω resistor because it has half the resistance. The total current (6.0 A) is larger than either branch current, because the paths are independent. The total resistance (2.0 Ω) is smaller than either individual resistance, which is the hallmark of a parallel combination.

---

### Worked Example 25.3 — Series vs. Parallel: Same Resistors, Different Results

**Problem:** Two resistors, 4.0 Ω and 12 Ω, are connected to a 16 V battery. Calculate the total current drawn when the resistors are connected (a) in series and (b) in parallel. Explain why the currents are different.

**Approach:** Apply the appropriate rule for each case, then compare the results. This side-by-side comparison reinforces why you cannot use the series rule for parallel circuits.

**Solution (a) — Series:**
$$R_{\text{total}} = 4.0 + 12 = 16\text{ Ω}$$
$$I = \frac{16}{16} = 1.0\text{ A}$$

**Solution (b) — Parallel:**
$$\frac{1}{R_{\text{total}}} = \frac{1}{4.0} + \frac{1}{12} = \frac{3}{12} + \frac{1}{12} = \frac{4}{12}$$
$$R_{\text{total}} = \frac{12}{4} = 3.0\text{ Ω}$$
$$I = \frac{16}{3.0} = 5.33\text{ A}$$

**Why the difference:** In series, the single path forces current through both resistors, so the total resistance is high (16 Ω) and current is low (1.0 A). In parallel, the battery has two independent paths, so the effective resistance is much lower (3.0 Ω) and the total current is more than five times larger (5.33 A). The same two resistors, the same battery — completely different behavior depending on how they are connected.

---

### Worked Example 25.4 — Combined Series-Parallel Circuit

**Problem:** A 24 V battery is connected to a circuit with three resistors. Resistor A (8.0 Ω) is in series with a parallel combination of resistor B (6.0 Ω) and resistor C (3.0 Ω). Calculate the total current from the battery and the voltage across resistor A.

**Approach:** Use the reduction method. First, find the equivalent resistance of the parallel pair (B and C). Then add that to the series resistor (A) to get the total resistance. Then work backward to find individual quantities.

**Solution:**

**Step 1 — Reduce the parallel pair:**
$$\frac{1}{R_{BC}} = \frac{1}{6.0} + \frac{1}{3.0} = \frac{1}{6.0} + \frac{2}{6.0} = \frac{3}{6.0}$$
$$R_{BC} = 2.0\text{ Ω}$$

**Step 2 — Total resistance (A is in series with the parallel pair):**
$$R_{\text{total}} = R_A + R_{BC} = 8.0 + 2.0 = 10.0\text{ Ω}$$

**Step 3 — Total current:**
$$I = \frac{V}{R_{\text{total}}} = \frac{24}{10.0} = 2.4\text{ A}$$

**Step 4 — Voltage across resistor A:**
$$V_A = IR_A = (2.4)(8.0) = 19.2\text{ V}$$

**Check:** The remaining voltage across the parallel pair is $24 - 19.2 = 4.8\text{ V}$. Current through B: $4.8/6.0 = 0.8\text{ A}$. Current through C: $4.8/3.0 = 1.6\text{ A}$. Sum: $0.8 + 1.6 = 2.4\text{ A}$ — matches the total current. ✓

**Why this makes sense:** The 8 Ω series resistor takes most of the voltage (19.2 V out of 24 V) because it has the largest resistance in the circuit. The parallel pair has a low equivalent resistance (2.0 Ω), so it gets only a small voltage.

---

### Worked Example 25.5 — IB-Style Complex Combination

**Problem:** A circuit consists of a 12 V battery with negligible internal resistance connected to four resistors. A 10 Ω resistor is in series with a parallel combination. The parallel combination consists of a 15 Ω resistor in one branch, and a series combination of a 5.0 Ω resistor and a 10 Ω resistor in the other branch. Calculate: (a) the total resistance of the circuit, (b) the total current drawn from the battery, and (c) the current through the 5.0 Ω resistor.

**Approach:** This circuit has a series-parallel arrangement nested inside another parallel branch. Reduce from the innermost part outward, then work back.

**Solution:**

Label the circuit for clarity:
- $R_1 = 10\text{ Ω}$ (series, at the start)
- Branch 1 of the parallel section: $R_2 = 15\text{ Ω}$
- Branch 2 of the parallel section: $R_3 = 5.0\text{ Ω}$ in series with $R_4 = 10\text{ Ω}$

**(a) Total resistance:**

Reduce Branch 2 (series): $R_{34} = 5.0 + 10 = 15\text{ Ω}$.

Now the parallel section has two 15 Ω resistors:
$$\frac{1}{R_{\text{parallel}}} = \frac{1}{15} + \frac{1}{15} = \frac{2}{15}$$
$$R_{\text{parallel}} = 7.5\text{ Ω}$$

Total with $R_1$ in series: $R_{\text{total}} = 10 + 7.5 = 17.5\text{ Ω}$.

**(b) Total current:**
$$I = \frac{12}{17.5} = 0.686\text{ A}$$

**(c) Current through the 5.0 Ω resistor:**

First, find the voltage across the parallel section:
$$V_{\text{parallel}} = I \times R_{\text{parallel}} = (0.686)(7.5) = 5.14\text{ V}$$

This 5.14 V is across each branch of the parallel section. In Branch 2, the 5.0 Ω and 10 Ω resistors form a series pair across 5.14 V. Their total is 15 Ω, so:
$$I_{\text{branch 2}} = \frac{5.14}{15} = 0.343\text{ A}$$

Since $R_3$ (5.0 Ω) and $R_4$ (10 Ω) are in series, the current is the same through both: 0.343 A.

**Why this makes sense:** The two parallel branches are identical (15 Ω each), so they split the total current equally — 0.343 A in each, summing to 0.686 A. The 5.0 Ω resistor has the same current as the 10 Ω resistor in series with it.

---

## Practice Problems

### Problem 1 — Simple Series
A 6.0 V battery is connected to three resistors in series: 3.0 Ω, 6.0 Ω, and 9.0 Ω. Calculate the total resistance, the current in the circuit, and the voltage across the 9.0 Ω resistor.

### Problem 2 — Simple Parallel (Read Carefully Before Starting)
A 12 V battery is connected to three resistors in parallel: 4.0 Ω, 6.0 Ω, and 12 Ω. Calculate the total resistance and the current through each resistor. Check that your branch currents sum to the total current. Remember: do NOT add the resistances directly.

### Problem 3 — Spot the Mistake
A student calculates the equivalent resistance of a 4.0 Ω resistor and a 12 Ω resistor in parallel as follows: $R = 4.0 + 12 = 16\text{ Ω}$. Explain what the student did wrong. Calculate the correct equivalent resistance. Then explain why the correct answer must be smaller than 4.0 Ω (the smallest individual resistance).

### Problem 4 — Series-Parallel Combination
A 24 V battery is connected to a 6.0 Ω resistor in series with a parallel combination of a 12 Ω resistor and an 8.0 Ω resistor. Calculate: (a) the total equivalent resistance of the circuit, (b) the current drawn from the battery, (c) the voltage across the 6.0 Ω resistor, and (d) the current through the 8.0 Ω resistor.

### Problem 5 — Three Parallel Resistors
Three resistors of 2.0 Ω, 3.0 Ω, and 6.0 Ω are connected in parallel across a 6.0 V battery. (a) Calculate the equivalent resistance of the three resistors. (b) Calculate the total current from the battery. (c) Determine the current through each resistor and show that they sum to the total current. (d) Explain why the current through the 2.0 Ω resistor is the largest.

### Problem 6 — IB-Style Examination Question
A student is investigating how the total resistance of a parallel combination changes as more resistors are added. She has a collection of identical 12 Ω resistors.

(a) Calculate the total resistance when two 12 Ω resistors are connected in parallel. (1 mark)

(b) Calculate the total resistance when three 12 Ω resistors are connected in parallel. (1 mark)

(c) The student connects four 12 Ω resistors in parallel and measures a total current of 3.0 A from a battery with negligible internal resistance. Determine the battery voltage. (2 marks)

(d) The student now connects the same four 12 Ω resistors in series instead of in parallel. She uses the same battery as in part (c). Calculate the current that flows. (2 marks)

(e) Compare the total power dissipated by the four resistors when connected in parallel with the power dissipated when connected in series. Account for the difference in terms of the physical arrangement of the resistors. (3 marks)

---

## Answers

### Answer 1
$$R_{\text{total}} = 3.0 + 6.0 + 9.0 = 18.0\text{ Ω}$$
$$I = \frac{6.0}{18.0} = 0.333\text{ A}$$
$$V_{9\text{ Ω}} = IR = (0.333)(9.0) = 3.0\text{ V}$$

The 9.0 Ω resistor, being the largest, gets the largest voltage share (3.0 V out of 6.0 V total). The 3.0 Ω gets 1.0 V and the 6.0 Ω gets 2.0 V, summing to 6.0 V.

---

### Answer 2

Total resistance using the reciprocal method:
$$\frac{1}{R} = \frac{1}{4.0} + \frac{1}{6.0} + \frac{1}{12} = \frac{3}{12} + \frac{2}{12} + \frac{1}{12} = \frac{6}{12}$$
$$R = 2.0\text{ Ω}$$

Total current: $I = 12/2.0 = 6.0\text{ A}$.

Branch currents (voltage is 12 V across each):
- Through 4.0 Ω: $I = 12/4.0 = 3.0\text{ A}$
- Through 6.0 Ω: $I = 12/6.0 = 2.0\text{ A}$
- Through 12 Ω: $I = 12/12 = 1.0\text{ A}$

Sum: $3.0 + 2.0 + 1.0 = 6.0\text{ A}$ ✓

The total resistance (2.0 Ω) is smaller than the smallest individual resistance (4.0 Ω), which is always the case for parallel combinations.

---

### Answer 3

The student added the resistances directly as if they were in series. For parallel resistors, the correct method is to add reciprocals:

$$\frac{1}{R} = \frac{1}{4.0} + \frac{1}{12} = \frac{3}{12} + \frac{1}{12} = \frac{4}{12}$$
$$R = 3.0\text{ Ω}$$

The correct answer (3.0 Ω) must be smaller than 4.0 Ω because adding a parallel path always REDUCES the total resistance. The 12 Ω resistor provides an additional path for current, so the overall opposition is less than that of the 4.0 Ω resistor alone. If the student's answer of 16 Ω were correct, connecting a second resistor would have made it HARDER for current to flow — which contradicts the physical reality that adding more paths makes it easier.

---

### Answer 4

**(a)** Equivalent resistance of the parallel pair:
$$\frac{1}{R_p} = \frac{1}{12} + \frac{1}{8.0} = \frac{1}{12} + \frac{1.5}{12} = \frac{2.5}{12}$$
$$R_p = \frac{12}{2.5} = 4.8\text{ Ω}$$

Total: $R_{\text{total}} = 6.0 + 4.8 = 10.8\text{ Ω}$.

**(b)** Current from battery: $I = 24/10.8 = 2.22\text{ A}$.

**(c)** Voltage across 6.0 Ω: $V = (2.22)(6.0) = 13.3\text{ V}$.

Check: voltage across parallel pair = $24 - 13.3 = 10.7\text{ V}$. Current through 12 Ω: $10.7/12 = 0.89\text{ A}$. Current through 8.0 Ω: $10.7/8.0 = 1.33\text{ A}$. Sum: $0.89 + 1.33 = 2.22\text{ A}$ ✓.

**(d)** Current through 8.0 Ω: $1.33\text{ A}$ (calculated above).

---

### Answer 5

**(a)** $\frac{1}{R} = \frac{1}{2.0} + \frac{1}{3.0} + \frac{1}{6.0} = \frac{3}{6.0} + \frac{2}{6.0} + \frac{1}{6.0} = \frac{6}{6.0}$, so $R = 1.0\text{ Ω}$.

**(b)** $I = 6.0/1.0 = 6.0\text{ A}$.

**(c)** Through 2.0 Ω: $6.0/2.0 = 3.0\text{ A}$. Through 3.0 Ω: $6.0/3.0 = 2.0\text{ A}$. Through 6.0 Ω: $6.0/6.0 = 1.0\text{ A}$. Sum: $3.0 + 2.0 + 1.0 = 6.0\text{ A}$ ✓.

**(d)** The 2.0 Ω resistor has the smallest resistance, so it presents the least opposition to current flow. In a parallel circuit where all branches share the same voltage (6.0 V), the current through each branch is inversely proportional to its resistance ($I = V/R$). The smallest resistance therefore draws the largest current.

---

### Answer 6 — IB-Style Full Solution with Mark Scheme

**(a)** (1 mark)
$$R = \frac{12}{2} = 6.0\text{ Ω}$$
Or: $1/R = 1/12 + 1/12 = 2/12$, so $R = 6.0\text{ Ω}$. 1 mark for correct answer. Award the mark for either method.

**(b)** (1 mark)
$$R = \frac{12}{3} = 4.0\text{ Ω}$$
1 mark for correct answer.

**(c)** (2 marks)
Four 12 Ω resistors in parallel: $R = 12/4 = 3.0\text{ Ω}$. (1 mark for the equivalent resistance.)
Battery voltage: $V = IR = (3.0)(3.0) = 9.0\text{ V}$. (1 mark for correct voltage with unit.)

**(d)** (2 marks)
Four 12 Ω resistors in series: $R = 12 \times 4 = 48\text{ Ω}$. (1 mark)
Current: $I = V/R = 9.0/48 = 0.1875\text{ A} \approx 0.19\text{ A}$. (1 mark)

**(e)** (3 marks)
Power in parallel: $P = IV = (3.0)(9.0) = 27\text{ W}$, or $P = V^2/R = 9.0^2/3.0 = 27\text{ W}$.
Power in series: $P = V^2/R = 9.0^2/48 = 81/48 = 1.69\text{ W}$.

The power dissipated in parallel (27 W) is 16 times larger than in series (1.69 W). (1 mark for calculating both powers.)

In parallel, each resistor experiences the full battery voltage (9.0 V), so each dissipates $P = V^2/R = 81/12 = 6.75\text{ W}$. Four such resistors give $4 \times 6.75 = 27\text{ W}$. (1 mark for explanation.)

In series, the voltage is divided among the four resistors (2.25 V each), and the total resistance is much larger (48 Ω vs. 3.0 Ω), so the current is much smaller (0.19 A vs. 3.0 A). The power dissipated depends on $I^2 R$ or $V^2/R$; the 16× smaller effective voltage per resistor combined with the 16× larger total resistance accounts for the factor of 16 in power. (1 mark for linking physical arrangement to power difference.)

---

## Key Takeaways

1. **Series: same current, voltages add, resistances add directly.** Total resistance is always larger than any individual resistance.

2. **Parallel: same voltage, currents add, reciprocals of resistance add.** Total resistance is always smaller than the smallest individual resistance.

3. **The physical reason parallel reduces resistance:** adding a parallel path gives current an additional route, making it easier for charge to flow. More paths = less overall opposition.

4. **The product-over-sum shortcut** ($R_1R_2/(R_1+R_2)$) works ONLY for two resistors. For three or more, use the reciprocal method.

5. **For $n$ identical resistors in parallel:** $R_{\text{total}} = R/n$. This is the fastest check — if your calculated parallel total is larger than any individual, you used the wrong formula.

6. **Check your work:** In series, $I$ is the same everywhere and $V$ sums to the battery. In parallel, $V$ is the same across branches and $I$ sums to the total. These checks will catch most errors.
