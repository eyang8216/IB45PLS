# Lesson 29: Buffer Solutions — Mechanism and Calculations — IB Chemistry HL

## What You'll Learn
- Explain what a buffer solution is and why it is important in chemistry and biology
- Describe, using chemical equations, the molecular mechanism by which a buffer resists changes in pH when either acid or base is added
- Identify the two components that every buffer solution must contain
- Use the Henderson-Hasselbalch equation to calculate the pH of a buffer solution
- Calculate the new pH of a buffer after a small amount of strong acid or strong base has been added
- Determine how to prepare a buffer solution with a target pH by choosing an appropriate weak acid and calculating the required ratio of conjugate base to acid

---

## 1. What Is a Buffer Solution?

### The problem buffers solve

Imagine you have a litre of pure water at pH 7. If you add just one drop of concentrated hydrochloric acid, the pH plummets to perhaps 3 or 4. Pure water has no defence against added acid or base — its pH changes dramatically with the smallest addition. Many chemical processes cannot tolerate such large swings in pH. Living cells, for example, can only function within a narrow pH range. Your blood must stay between pH 7.35 and 7.45; if it goes outside this range, you become seriously ill.

A **buffer solution** is a solution that resists changes in pH when a small amount of a strong acid or a strong base is added to it. It does not prevent the pH from changing entirely, but it keeps the change very small, often less than 0.1 pH units.

### What a buffer must contain

Every buffer solution contains two essential components. The first component is a weak acid. The second component is the conjugate base of that same weak acid, usually added in the form of a soluble salt. Both components must be present in significant (roughly similar) amounts. You cannot make a buffer by simply dissolving a weak acid in water — that gives you only one of the two components. You also cannot make a buffer from a strong acid and its salt, because a strong acid dissociates completely and cannot establish the equilibrium that a buffer requires.

For example, one of the most common buffers is made from ethanoic acid (CH₃COOH), which is a weak acid, and sodium ethanoate (CH₃COONa), which is a salt that provides the conjugate base CH₃COO⁻. When sodium ethanoate dissolves in water, it dissociates completely into Na⁺ ions and CH₃COO⁻ ions. The Na⁺ ions are spectator ions — they do not participate in the buffer chemistry. The CH₃COO⁻ ions are the active component.

Another type of buffer can be made from a weak base and its conjugate acid. An example is a mixture of ammonia (NH₃), a weak base, and ammonium chloride (NH₄Cl), which provides the conjugate acid NH₄⁺.

### Why a weak acid alone cannot be a buffer

This is a very common misunderstanding. A solution of pure ethanoic acid in water does establish an equilibrium: CH₃COOH (aq) ⇌ H⁺ (aq) + CH₃COO⁻ (aq). However, at equilibrium, the concentration of CH₃COO⁻ is extremely small — only about 1% of the acid concentration. If you add a strong acid (H⁺) to this solution, there are not enough CH₃COO⁻ ions available to react with and neutralise the added H⁺. The pH drops significantly. A buffer needs a substantial reserve of the conjugate base to catch added acid, and a substantial reserve of the weak acid to catch added base. That is why both components must be present from the start.

---

## 2. How a Buffer Works — The Mechanism

### The acid buffer: CH₃COOH and CH₃COO⁻

Consider a buffer solution containing ethanoic acid (CH₃COOH) and ethanoate ions (CH₃COO⁻). In this solution, the following equilibrium exists:

$$\ce{CH3COOH(aq) <=> H+(aq) + CH3COO-(aq)}$$

The key point is that both CH₃COOH and CH₃COO⁻ are present in the solution at high concentrations. They form what you can think of as a "chemical reserve": the weak acid is a reserve of protons that can be released, and the conjugate base is a reserve of "proton-catching capacity."

### What happens when a strong acid is added

Suppose you add a small amount of hydrochloric acid, HCl (aq). Hydrochloric acid dissociates completely, releasing H⁺ ions into the solution. If these H⁺ ions were left free, the pH would drop. However, the ethanoate ions (CH₃COO⁻) that are already present in the buffer immediately react with the added H⁺:

$$\ce{CH3COO-(aq) + H+(aq) -> CH3COOH(aq)}$$

The ethanoate ions act as a Brønsted-Lowry base, accepting the added protons and converting them into undissociated ethanoic acid molecules. The H⁺ ions are removed from the solution. Because the concentration of CH₃COO⁻ is large, it can absorb a significant amount of added acid before running out.

The equilibrium shifts slightly to the left (Le Chatelier's principle), but because both sides of the equilibrium already contain large amounts of their respective species, the shift makes only a tiny difference to the [H⁺] concentration, and therefore only a tiny difference to the pH.

### What happens when a strong base is added

Now suppose you add a small amount of sodium hydroxide, NaOH (aq). Sodium hydroxide dissociates completely, releasing OH⁻ ions. The ethanoic acid molecules (CH₃COOH) present in the buffer react with the added OH⁻:

$$\ce{CH3COOH(aq) + OH-(aq) -> CH3COO-(aq) + H2O(l)}$$

The ethanoic acid acts as a Brønsted-Lowry acid, donating a proton to the hydroxide ion. This reaction produces water (which is neutral) and more ethanoate ions. The OH⁻ ions are removed from the solution. Because the concentration of CH₃COOH is large, it can neutralise a significant amount of added base.

### A visual way to think about buffers

A buffer is like a chemical sponge. The conjugate base soaks up added acid, and the weak acid soaks up added base. As long as you do not exceed the capacity of the sponge — that is, as long as you do not add more acid or base than the buffer components can react with — the pH stays nearly constant.

<div class="worked">
<p><strong>Worked Example 1:</strong> A student has two solutions: Solution A contains only ethanoic acid, CH₃COOH, at a concentration of 0.10 mol dm⁻³. Solution B contains ethanoic acid, CH₃COOH, at a concentration of 0.10 mol dm⁻³ AND sodium ethanoate, CH₃COONa, at a concentration of 0.10 mol dm⁻³. Explain, using chemical equations, which solution can act as a buffer and which cannot.</p>

<p><strong>Strategy:</strong> A buffer must contain both a weak acid and its conjugate base in significant amounts. We need to check which solution meets this requirement.</p>

<p>Solution A contains only CH₃COOH. When this acid partially dissociates (CH₃COOH ⇌ H⁺ + CH₃COO⁻), the concentration of CH₃COO⁻ produced is very small (about 1.34 × 10⁻³ mol dm⁻³ for a 0.10 mol dm⁻³ solution). If H⁺ is added, there are not enough CH₃COO⁻ ions to react with and consume the added protons. Solution A cannot act as a buffer.</p>

<p>Solution B contains CH₃COOH at 0.10 mol dm⁻³ AND CH₃COO⁻ (from dissolved CH₃COONa) at 0.10 mol dm⁻³. Both the weak acid and its conjugate base are present in substantial, equal amounts. When H⁺ is added, the reaction CH₃COO⁻ (aq) + H⁺ (aq) → CH₃COOH (aq) consumes the protons. When OH⁻ is added, the reaction CH₃COOH (aq) + OH⁻ (aq) → CH₃COO⁻ (aq) + H₂O (l) consumes the hydroxide ions. Solution B is an effective buffer.</p>

<p><strong>Why this makes sense:</strong> Having both forms of the conjugate pair in roughly equal amounts is what gives a buffer its ability to resist pH changes in both directions.</p>
</div>

---

## 3. The Henderson-Hasselbalch Equation

### Where the equation comes from

For a buffer made from a weak acid (HA) and its conjugate base (A⁻), we start with the Ka expression:

$$K_a = \frac{[\ce{H+}][\ce{A-}]}{[\ce{HA}]}$$

We can rearrange this equation to solve for [H⁺]:

$$[\ce{H+}] = K_a \times \frac{[\ce{HA}]}{[\ce{A-}]}$$

Now we take the negative logarithm of both sides:

$$-\log[\ce{H+}] = -\log K_a - \log\frac{[\ce{HA}]}{[\ce{A-}]}$$

The left side is pH. The term −log Ka is pKa. And −log([HA]/[A⁻]) = +log([A⁻]/[HA]). So the final result is:

$$\text{pH} = \text{p}K_a + \log\frac{[\ce{A-}]}{[\ce{HA}]}$$

This is the **Henderson-Hasselbalch equation**. It is the single most useful formula for buffer calculations. It tells you that the pH of a buffer depends on two things: the pKa of the weak acid (which is a fixed property of that acid) and the ratio of the concentration of the conjugate base to the concentration of the weak acid.

### What the equation reveals

When [A⁻] = [HA], the ratio [A⁻]/[HA] equals 1. The logarithm of 1 is 0, so pH = pKa. This is a very important result: when the concentrations of the weak acid and its conjugate base are equal, the pH of the buffer equals the pKa of the weak acid. This is the point at which the buffer has its maximum capacity to resist pH changes in both directions.

When [A⁻] is greater than [HA], the ratio is greater than 1, the logarithm is positive, and pH is higher than pKa. This makes sense — more conjugate base means the solution is less acidic.

When [HA] is greater than [A⁻], the ratio is less than 1, the logarithm is negative, and pH is lower than pKa. More weak acid means the solution is more acidic.

A buffer works effectively when the ratio [A⁻]/[HA] is between 0.1 and 10. This corresponds to a pH range of approximately pKa ± 1. Outside this range, one component becomes so depleted that the buffer has very little capacity. This is why, when choosing a weak acid to make a buffer at a particular pH, you should select an acid whose pKa is within 1 unit of the target pH.

<div class="worked">
<p><strong>Worked Example 2:</strong> A buffer solution is prepared by dissolving ethanoic acid, CH₃COOH, and sodium ethanoate, CH₃COONa, in water so that the concentration of ethanoic acid is 0.20 mol dm⁻³ and the concentration of ethanoate ions is 0.10 mol dm⁻³. The pKa of ethanoic acid is 4.74. Calculate the pH of this buffer solution.</p>

<p><strong>Strategy:</strong> Use the Henderson-Hasselbalch equation. Identify [A⁻] as the concentration of the conjugate base (CH₃COO⁻) and [HA] as the concentration of the weak acid (CH₃COOH).</p>

<p>pH = pKa + log([CH₃COO⁻] ÷ [CH₃COOH])</p>
<p>pH = 4.74 + log(0.10 ÷ 0.20)</p>
<p>pH = 4.74 + log(0.50)</p>

<p>Now we need log(0.50). Since 0.50 = 1/2, log(0.50) = log(1) − log(2) = 0 − 0.30 = −0.30.</p>

<p>pH = 4.74 + (−0.30) = 4.44.</p>

<p><strong>Why this makes sense:</strong> The ratio of conjugate base to acid is 0.50, which is less than 1. We expect the pH to be lower than the pKa, and 4.44 is indeed lower than 4.74. The buffer is slightly more acidic than the pKa because there is more acid than conjugate base present.</p>
</div>

<div class="worked">
<p><strong>Worked Example 3:</strong> A chemist needs a buffer with a pH of 5.00. The available weak acid is ethanoic acid, which has a pKa of 4.74. Calculate the ratio of the concentration of ethanoate ions to the concentration of ethanoic acid that is needed.</p>

<p><strong>Strategy:</strong> Rearrange the Henderson-Hasselbalch equation to solve for the ratio [A⁻]/[HA].</p>

<p>pH = pKa + log([A⁻]/[HA])</p>
<p>5.00 = 4.74 + log([A⁻]/[HA])</p>
<p>log([A⁻]/[HA]) = 5.00 − 4.74 = 0.26</p>

<p>Now we need to find the antilog: [A⁻]/[HA] = 10⁰·²⁶.</p>

<p>To calculate 10⁰·²⁶ without a calculator: we know that 10⁰·³⁰ ≈ 2.0, so 10⁰·²⁶ is slightly less than 2.0. A reasonable estimate is 1.8.</p>

<p>So [CH₃COO⁻] ÷ [CH₃COOH] ≈ 1.8. This means the concentration of the conjugate base should be approximately 1.8 times the concentration of the weak acid. For example, if the acid concentration is 0.10 mol dm⁻³, the conjugate base concentration should be about 0.18 mol dm⁻³.</p>

<p><strong>Why this makes sense:</strong> The target pH (5.00) is higher than the pKa (4.74), so the solution needs to be less acidic than the equal-concentration buffer. This requires more conjugate base than acid — hence a ratio greater than 1.</p>
</div>

---

## 4. Calculating pH Changes After Adding Acid or Base to a Buffer

### The step-by-step method

When a strong acid or strong base is added to a buffer, the pH does change, but only by a small amount. To calculate the new pH, follow these steps:

1. Determine the number of moles of each buffer component (the weak acid HA and the conjugate base A⁻) that are present before the addition.

2. Determine the number of moles of H⁺ or OH⁻ being added.

3. Apply the stoichiometry: added H⁺ reacts with A⁻ to form HA. Added OH⁻ reacts with HA to form A⁻.

4. Calculate the new number of moles of HA and A⁻ after the reaction.

5. Use the Henderson-Hasselbalch equation with the new amounts. Since the volume is the same for both components (they are in the same solution), you can use moles directly in the log ratio instead of concentrations — the volumes cancel.

<div class="worked">
<p><strong>Worked Example 4:</strong> A buffer solution is prepared by dissolving 0.50 mol of ethanoic acid, CH₃COOH, and 0.50 mol of sodium ethanoate, CH₃COONa, in enough distilled water to make 1.00 dm³ of solution. The pKa of ethanoic acid is 4.74. A student then adds 0.010 mol of hydrochloric acid, HCl, to this buffer. Assuming the volume does not change upon addition, calculate the new pH of the buffer.</p>

<p><strong>Strategy:</strong> First calculate the initial pH, then determine how the added H⁺ reacts, and finally use the Henderson-Hasselbalch equation with the new amounts.</p>

<p><strong>Initial pH:</strong></p>
<p>pH = pKa + log([CH₃COO⁻]/[CH₃COOH]) = 4.74 + log(0.50/0.50) = 4.74 + log(1) = 4.74 + 0 = 4.74.</p>

<p><strong>Reaction with added H⁺:</strong></p>
<p>The reaction is: CH₃COO⁻ (aq) + H⁺ (aq) → CH₃COOH (aq).</p>

<p>Moles before addition: CH₃COOH = 0.50 mol, CH₃COO⁻ = 0.50 mol.</p>
<p>Moles of H⁺ added: 0.010 mol.</p>

<p>After reaction: CH₃COO⁻ decreases by 0.010 mol (because it reacts with H⁺). CH₃COOH increases by 0.010 mol (because it is produced by the reaction).</p>

<p>New moles of CH₃COO⁻ = 0.50 − 0.010 = 0.49 mol.</p>
<p>New moles of CH₃COOH = 0.50 + 0.010 = 0.51 mol.</p>

<p><strong>New pH:</strong></p>
<p>pH = 4.74 + log(0.49/0.51) = 4.74 + log(0.961).</p>

<p>log(0.961) = −0.017 (since log(1) = 0 and 0.961 is very close to 1).</p>

<p>pH = 4.74 + (−0.017) = 4.72.</p>

<p><strong>Comparison — what would happen without the buffer?</strong></p>
<p>If the same 0.010 mol of HCl were added to 1.00 dm³ of pure water (pH 7.00), the [H⁺] would be 0.010 mol dm⁻³, giving pH = 2.00. That is a change of 5.00 pH units. With the buffer, the change was only 0.02 pH units. The buffer reduced the pH change by a factor of about 250.</p>

<p><strong>Why this makes sense:</strong> Adding acid shifts the equilibrium slightly, but because both components are present in large amounts (0.50 mol each), the 0.010 mol of added H⁺ changes the ratio only from 1.00 to 0.96. This tiny change in the ratio produces only a tiny change in pH.</p>
</div>

---

## 5. Preparing a Buffer — A Practical Guide

### Step 1: Choose the right weak acid

To make a buffer at a target pH, first find a weak acid whose pKa is as close as possible to the target pH. The buffer will work best when the target pH is within ±1 unit of the pKa.

For example, if you need a buffer at pH 4.20, you could use methanoic acid (pKa = 3.74, difference = 0.46) or ethanoic acid (pKa = 4.74, difference = 0.54). Both are within 1 unit. Benzoic acid (pKa = 4.20) would be ideal because its pKa matches the target pH exactly — equal concentrations of acid and conjugate base would give the desired pH.

### Step 2: Calculate the required ratio

Use the Henderson-Hasselbalch equation to find the ratio of [A⁻] to [HA] needed for the target pH.

### Step 3: Calculate the masses or volumes needed

Choose a convenient concentration for one component, calculate the other using the ratio, and then determine the mass of the salt needed.

<div class="worked">
<p><strong>Worked Example 5:</strong> A student needs to prepare 250 cm³ of a buffer solution with pH 4.20. The available chemicals are methanoic acid, HCOOH (pKa = 3.74), and its sodium salt, HCOONa (molar mass = 68.0 g mol⁻¹). The student decides to use a concentration of 0.10 mol dm⁻³ for the methanoic acid. Calculate the mass of sodium methanoate that must be dissolved in the 250 cm³ of acid solution to achieve the desired pH.</p>

<p><strong>Strategy:</strong> Use the Henderson-Hasselbalch equation to find the required ratio, calculate the concentration of methanoate ions needed, then find the number of moles and mass of the salt.</p>

<p>4.20 = 3.74 + log([HCOO⁻]/[HCOOH])</p>
<p>log([HCOO⁻]/[HCOOH]) = 4.20 − 3.74 = 0.46</p>
<p>[HCOO⁻]/[HCOOH] = 10⁰·⁴⁶</p>

<p>Since 10⁰·³⁰ ≈ 2.0 and 10⁰·⁴⁸ ≈ 3.0, the value 10⁰·⁴⁶ is approximately 2.88.</p>

<p>[HCOO⁻] = 2.88 × [HCOOH] = 2.88 × 0.10 = 0.288 mol dm⁻³.</p>

<p>Moles of HCOO⁻ needed in 250 cm³: n = concentration × volume = 0.288 mol dm⁻³ × (250 ÷ 1000) dm³ = 0.288 × 0.250 = 0.0720 mol.</p>

<p>Mass of HCOONa = moles × molar mass = 0.0720 mol × 68.0 g mol⁻¹ = 4.90 g.</p>

<p><strong>Why this makes sense:</strong> The target pH (4.20) is higher than the pKa (3.74), so more conjugate base than acid is needed (ratio > 1). The calculated ratio of 2.88 confirms this, and 4.90 g is a reasonable mass for a typical buffer preparation.</p>
</div>

---

## Practice Problems

**Problem 1:** A buffer solution is prepared by dissolving ethanoic acid, CH₃COOH, and sodium ethanoate, CH₃COONa, in distilled water. The final concentrations are 0.30 mol dm⁻³ for CH₃COOH and 0.20 mol dm⁻³ for CH₃COO⁻. The pKa of ethanoic acid is 4.74 at 298 K. Calculate the pH of this buffer solution.

**Problem 2:** Ammonia, NH₃, is a weak base with Kb = 1.8 × 10⁻⁵ mol dm⁻³ at 298 K. The value of Kw at this temperature is 1.0 × 10⁻¹⁴. A buffer solution is prepared containing ammonia at a concentration of 0.15 mol dm⁻³ and ammonium chloride, NH₄Cl, at a concentration of 0.25 mol dm⁻³. (a) Calculate the Ka of the ammonium ion, NH₄⁺. (b) Calculate the pKa of NH₄⁺. (c) Calculate the pH of this buffer solution. Hint: the buffer contains the conjugate acid (NH₄⁺) and the base (NH₃), so the Henderson-Hasselbalch equation uses pKa of NH₄⁺ and the ratio [NH₃]/[NH₄⁺].

**Problem 3:** A buffer solution with a volume of 1.00 dm³ is prepared containing 0.40 mol of ethanoic acid, CH₃COOH, and 0.40 mol of sodium ethanoate, CH₃COONa. The pKa of ethanoic acid is 4.74 at 298 K. (a) Calculate the initial pH of this buffer. (b) A student adds 0.020 mol of solid sodium hydroxide, NaOH, to the buffer. Assuming the volume does not change, calculate the new pH after the addition. (c) The student resets the buffer and instead adds 0.020 mol of hydrochloric acid, HCl. Calculate the new pH after this addition.

**Problem 4:** A biochemist needs to prepare a buffer solution with a pH of 7.40 for an experiment. The biochemist chooses the dihydrogen phosphate ion, H₂PO₄⁻, as the weak acid component. This species has a pKa of 7.20. The buffer will contain H₂PO₄⁻ (the acid) and HPO₄²⁻ (the conjugate base). Calculate the ratio of the concentration of HPO₄²⁻ to H₂PO₄⁻ needed to achieve the target pH.

**Problem 5 (IB-style):** (a) Define the term "buffer solution" and state the two essential components that every acidic buffer must contain. (b) A student prepares a buffer solution by dissolving 0.050 mol of ethanoic acid, CH₃COOH, and 0.050 mol of sodium ethanoate, CH₃COONa, in enough distilled water to make exactly 500 cm³ of solution. The pKa of ethanoic acid is 4.74 at 298 K. Calculate the pH of the buffer. (c) The student then adds 5.0 cm³ of hydrochloric acid, HCl (aq), with a concentration of 1.0 mol dm⁻³ to the buffer solution. The neutralisation reaction that occurs is: CH₃COO⁻ (aq) + H⁺ (aq) → CH₃COOH (aq). Calculate the new pH of the buffer after this addition, assuming that the volume change is negligible. (d) Compare the pH change you calculated in part (c) with the pH change that would occur if the same amount of HCl were added to 500 cm³ of pure water. Explain why the two pH changes are so different.

---

## Answers

### Answer 1

Using the Henderson-Hasselbalch equation:

pH = pKa + log([CH₃COO⁻] ÷ [CH₃COOH])

pH = 4.74 + log(0.20 ÷ 0.30)

pH = 4.74 + log(0.667)

We need log(0.667). Since 0.667 = 2/3, we can calculate: log(2/3) = log(2) − log(3) = 0.30 − 0.48 = −0.18.

pH = 4.74 + (−0.18) = 4.56.

The ratio of conjugate base to acid is less than 1, so the pH is slightly lower than the pKa, which makes sense.

### Answer 2

**(a)** The Ka of NH₄⁺ is found using Ka × Kb = Kw for the conjugate pair NH₄⁺/NH₃.

Ka(NH₄⁺) = Kw ÷ Kb(NH₃) = (1.0 × 10⁻¹⁴) ÷ (1.8 × 10⁻⁵).

Ka = (1.0 ÷ 1.8) × (10⁻¹⁴ ÷ 10⁻⁵) = 0.556 × 10⁻⁹ = 5.56 × 10⁻¹⁰ mol dm⁻³.

**(b)** pKa = −log(5.56 × 10⁻¹⁰) = −[log(5.56) + log(10⁻¹⁰)] = −[0.745 + (−10.00)] = −(−9.255) = 9.25.

**(c)** For a buffer made from a weak base (NH₃) and its conjugate acid (NH₄⁺), the Henderson-Hasselbalch equation is:

pH = pKa(NH₄⁺) + log([NH₃] ÷ [NH₄⁺])

pH = 9.25 + log(0.15 ÷ 0.25) = 9.25 + log(0.60).

log(0.60) = log(6.0 × 10⁻¹) = log(6.0) + log(10⁻¹) = 0.78 + (−1.00) = −0.22.

pH = 9.25 + (−0.22) = 9.03.

The buffer is basic because it contains more of the weak base (NH₃) than the conjugate acid, and the pKa of NH₄⁺ is itself quite high (9.25), reflecting that NH₄⁺ is a very weak acid.

### Answer 3

**(a)** Initial pH: Since [CH₃COOH] = [CH₃COO⁻] = 0.40 mol dm⁻³, the ratio is 1, and log(1) = 0. So pH = pKa = 4.74.

**(b)** Adding NaOH: OH⁻ reacts with CH₃COOH according to CH₃COOH (aq) + OH⁻ (aq) → CH₃COO⁻ (aq) + H₂O (l).

Before: CH₃COOH = 0.40 mol, CH₃COO⁻ = 0.40 mol. OH⁻ added = 0.020 mol.

After: CH₃COOH = 0.40 − 0.020 = 0.38 mol. CH₃COO⁻ = 0.40 + 0.020 = 0.42 mol.

New pH = 4.74 + log(0.42 ÷ 0.38) = 4.74 + log(1.105).

log(1.105) ≈ 0.043 (since log of a number slightly above 1 is approximately the fractional excess divided by 2.303).

pH = 4.74 + 0.043 = 4.78.

**(c)** Adding HCl: H⁺ reacts with CH₃COO⁻ according to CH₃COO⁻ (aq) + H⁺ (aq) → CH₃COOH (aq).

After: CH₃COO⁻ = 0.40 − 0.020 = 0.38 mol. CH₃COOH = 0.40 + 0.020 = 0.42 mol.

New pH = 4.74 + log(0.38 ÷ 0.42) = 4.74 + log(0.905).

log(0.905) ≈ −0.043. pH = 4.74 + (−0.043) = 4.70.

Notice that the pH shifts are symmetrical: adding base raises pH by 0.04 units, and adding acid lowers pH by 0.04 units. This symmetry occurs because the buffer started with equal amounts of acid and conjugate base.

### Answer 4

Using the Henderson-Hasselbalch equation:

7.40 = 7.20 + log([HPO₄²⁻] ÷ [H₂PO₄⁻])

log([HPO₄²⁻] ÷ [H₂PO₄⁻]) = 7.40 − 7.20 = 0.20

[HPO₄²⁻] ÷ [H₂PO₄⁻] = 10⁰·²⁰

Since 10⁰·³⁰ ≈ 2.0, the value 10⁰·²⁰ is less than 2.0. Using the relationship that 10⁰·²⁰ ≈ 1.58, the ratio is approximately 1.6:1 of HPO₄²⁻ to H₂PO₄⁻.

This means the buffer should contain about 1.6 times as much hydrogen phosphate as dihydrogen phosphate. This makes sense because the target pH (7.40) is higher than the pKa (7.20), so more conjugate base than acid is needed.

### Answer 5

**(a)** A buffer solution is a solution that resists changes in pH when small amounts of a strong acid or a strong base are added to it. Every acidic buffer must contain two essential components: a weak acid and its conjugate base, both present in significant concentrations. The conjugate base is usually provided by dissolving a soluble salt of the weak acid. For example, an ethanoic acid buffer contains CH₃COOH (the weak acid) and CH₃COO⁻ (the conjugate base, provided by dissolving CH₃COONa).

**(b)** First, calculate the concentrations. The total volume is 500 cm³ = 0.500 dm³.

[CH₃COOH] = 0.050 mol ÷ 0.500 dm³ = 0.10 mol dm⁻³.

[CH₃COO⁻] = 0.050 mol ÷ 0.500 dm³ = 0.10 mol dm⁻³.

Since the concentrations are equal, pH = pKa = 4.74.

**(c)** Moles of HCl added = concentration × volume = 1.0 mol dm⁻³ × (5.0 ÷ 1000) dm³ = 0.0050 mol.

The added H⁺ reacts with CH₃COO⁻: CH₃COO⁻ (aq) + H⁺ (aq) → CH₃COOH (aq).

Before addition: CH₃COOH = 0.050 mol, CH₃COO⁻ = 0.050 mol.

After reaction: CH₃COO⁻ = 0.050 − 0.0050 = 0.045 mol. CH₃COOH = 0.050 + 0.0050 = 0.055 mol.

New pH = 4.74 + log(0.045 ÷ 0.055) = 4.74 + log(0.818).

log(0.818) ≈ −0.087.

pH = 4.74 + (−0.087) = 4.65.

The pH changed from 4.74 to 4.65, a decrease of only 0.09 units.

**(d)** If the same 0.0050 mol of HCl were added to 500 cm³ of pure water (pH 7.00):

[H⁺] = 0.0050 mol ÷ 0.500 dm³ = 0.010 mol dm⁻³.

pH = −log(0.010) = 2.00.

The pH of pure water drops from 7.00 to 2.00, a change of 5.00 pH units. With the buffer, the change was only 0.09 pH units.

The two pH changes are so different because the buffer contains the ethanoate ion (CH₃COO⁻), which reacts with and removes the added H⁺ ions from solution. In pure water, there is no such mechanism — the added H⁺ simply accumulates and the pH drops dramatically. The buffer's ability to chemically consume the added acid (converting it into undissociated CH₃COOH molecules) is what makes the change so small.
