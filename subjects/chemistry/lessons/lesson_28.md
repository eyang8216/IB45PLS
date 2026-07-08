# Lesson 28: Weak Acids, Ka and pKa — IB Chemistry HL

## What You'll Learn
- Explain what makes a weak acid different from a strong acid at the molecular level
- Write the expression for the acid dissociation constant, Ka, for any weak acid
- Convert between Ka and pKa and use these values to compare the relative strength of different weak acids
- Calculate the pH of a solution of a weak acid using the equilibrium (ICE) method
- Recognise when the small-dissociation approximation is valid and when you must solve a quadratic equation instead
- Use the relationship Ka × Kb = Kw to connect a weak acid to the strength of its conjugate base

---

## 1. Weak Acids — Not All Acids Release Their Protons Completely

### The key difference between strong and weak

When a strong acid such as hydrochloric acid (HCl) dissolves in water, every single HCl molecule breaks apart into H⁺ and Cl⁻ ions. There are no HCl molecules left. This is what "strong" means: complete dissociation.

A **weak acid** behaves differently. When a weak acid dissolves in water, only a small fraction of its molecules break apart. Most of the acid molecules remain intact, floating in the solution as whole molecules. Typically, fewer than 5 out of every 100 molecules dissociate.

Consider ethanoic acid, CH₃COOH, which is the acid found in vinegar. When you dissolve 0.10 mol of CH₃COOH in enough water to make 1.00 dm³ of solution, only about 1.3% of the molecules dissociate. The other 98.7% stay as CH₃COOH molecules. The equation for this partial dissociation is written with a double arrow (⇌) to show that both the forward reaction (dissociation) and the reverse reaction (recombination) happen at the same time:

$$\ce{CH3COOH(aq) + H2O(l) <=> CH3COO-(aq) + H3O+(aq)}$$

### A comparison of strong and weak acids

| Property | Strong acid (for example, HCl) | Weak acid (for example, CH₃COOH) |
|----------|-------------------------------|----------------------------------|
| Extent of dissociation | Complete — every molecule breaks apart | Partial — fewer than 5% of molecules dissociate |
| Concentration of H⁺ compared to acid concentration | Equal to the acid concentration | Much smaller than the acid concentration |
| pH of a 0.10 mol dm⁻³ solution | 1.00 | Approximately 2.87 |
| Electrical conductivity | High (many ions to carry current) | Low (fewer ions present) |
| Position of equilibrium | Lies far to the right (products side) | Lies far to the left (reactants side) |
| Arrow used in equation | Single arrow (→) | Double arrow (⇌) |

Many students confuse the word "weak" with "dilute." These words mean different things. "Weak" describes the identity of the acid — how readily it gives away its proton. "Dilute" describes how much acid is present in a given volume of water. You can have a dilute solution of a strong acid (a tiny amount of HCl in a large volume of water) and you can also have a concentrated solution of a weak acid (a large amount of ethanoic acid in a small volume of water).

### Why are some acids weak?

The strength of an acid depends on how easily the bond between the hydrogen atom and the rest of the molecule can break, and how stable the resulting negative ion is after the proton leaves. In ethanoic acid, the O—H bond in the carboxylic acid group (—COOH) does not break as easily as the H—Cl bond in hydrogen chloride. Also, the ethanoate ion (CH₃COO⁻) that forms after the proton leaves is only moderately stable.

---

## 2. Ka — The Acid Dissociation Constant

### What Ka measures

Because weak acids establish an equilibrium, we can write an equilibrium constant for their dissociation. This constant is called the **acid dissociation constant** and is given the symbol **Ka**. The letter "a" stands for "acid."

For any weak acid, which we can represent by the general formula HA (where H is the hydrogen that can come off and A is the rest of the molecule), the dissociation reaction is:

$$\ce{HA(aq) <=> H+(aq) + A-(aq)}$$

The equilibrium constant expression for this reaction is:

$$K_a = \frac{[\ce{H+}][\ce{A-}]}{[\ce{HA}]}$$

In this expression, [H⁺] is the equilibrium concentration of hydrogen ions in mol dm⁻³, [A⁻] is the equilibrium concentration of the conjugate base in mol dm⁻³, and [HA] is the equilibrium concentration of the undissociated weak acid in mol dm⁻³.

Notice that water, H₂O, does not appear in the Ka expression even though it participates in the reaction. This is because water is the solvent and its concentration is effectively constant. In dilute aqueous solutions, the concentration of water is so large (approximately 55 mol dm⁻³) that it does not change measurably during the reaction.

### What Ka tells you about acid strength

The numerical value of Ka is a direct measure of acid strength. A larger value of Ka means that the equilibrium lies further to the right — more of the acid has dissociated. Therefore, a larger Ka means a stronger weak acid.

Because Ka values are often very small numbers (like 1.8 × 10⁻⁵), chemists also use pKa, which is defined in the same way as pH:

$$\text{p}K_a = -\log_{10} K_a$$

Since pKa is the negative logarithm of Ka, a smaller pKa means a larger Ka, which means a stronger acid. This is the same pattern you learned for pH: a smaller number means a larger concentration.

### Ka and pKa values for some common weak acids

| Weak acid | Formula | Ka (mol dm⁻³) | pKa |
|-----------|---------|---------------|-----|
| Methanoic acid | HCOOH | 1.8 × 10⁻⁴ | 3.74 |
| Ethanoic acid | CH₃COOH | 1.8 × 10⁻⁵ | 4.74 |
| Benzoic acid | C₆H₅COOH | 6.3 × 10⁻⁵ | 4.20 |
| Hydrocyanic acid | HCN | 6.2 × 10⁻¹⁰ | 9.21 |

From this table, you can see that methanoic acid (pKa = 3.74) is a stronger acid than ethanoic acid (pKa = 4.74). Hydrocyanic acid (pKa = 9.21) is an extremely weak acid — its Ka of 6.2 × 10⁻¹⁰ means that only a vanishingly small fraction of HCN molecules dissociate in water.

### Ka depends on temperature

Like all equilibrium constants, Ka depends on temperature. The dissociation of a weak acid is usually endothermic (it absorbs heat), so increasing the temperature increases Ka and decreases pKa. When doing calculations, always note the temperature given in the problem. If no temperature is stated, assume 298 K.

<div class="worked">
<span class="worked-label">Worked Example 1</span>

**Question:** Which is the stronger acid: ethanoic acid, CH₃COOH, with Ka = 1.8 × 10⁻⁵, or methanoic acid, HCOOH, with Ka = 1.8 × 10⁻⁴?

**Strategy:** Compare the Ka values directly. The acid with the larger Ka is stronger because a larger Ka means more dissociation.

Ka of methanoic acid = 1.8 × 10⁻⁴. Ka of ethanoic acid = 1.8 × 10⁻⁵.

Since 1.8 × 10⁻⁴ is ten times larger than 1.8 × 10⁻⁵ (because 10⁻⁴ = 10 × 10⁻⁵), methanoic acid has the larger Ka.

We can also compare pKa values: pKa(HCOOH) = −log(1.8 × 10⁻⁴) = 3.74. pKa(CH₃COOH) = −log(1.8 × 10⁻⁵) = 4.74. Since 3.74 is smaller than 4.74, methanoic acid is confirmed as the stronger acid.

**Why this makes sense:** A Ka value that is 10 times larger means the acid dissociates about 10 times more. Methanoic acid has one fewer CH₂ group than ethanoic acid, which affects how well the negative charge on the conjugate base is stabilised.
</div>

---

## 3. Calculating the pH of a Weak Acid Solution

### Setting up an ICE table

When a weak acid HA dissolves in water, the following equilibrium is established: HA (aq) ⇌ H⁺ (aq) + A⁻ (aq). To find the pH, we need to find the equilibrium concentration of H⁺, which we will call x.

We use a systematic approach called an **ICE table**. ICE stands for Initial, Change, and Equilibrium. Here is how to set it up:

| | HA | H⁺ | A⁻ |
|---|-----|------|------|
| **I** (Initial concentration) | C₀ | 0 | 0 |
| **C** (Change) | −x | +x | +x |
| **E** (Equilibrium concentration) | C₀ − x | x | x |

In this table, C₀ (read as "C-nought" or "C-zero") is the initial concentration of the weak acid before any dissociation has happened. The symbol x represents the amount of acid that dissociates, which is also the concentration of H⁺ and A⁻ produced at equilibrium.

Now we substitute the equilibrium concentrations into the Ka expression:

$$K_a = \frac{[\ce{H+}][\ce{A-}]}{[\ce{HA}]} = \frac{x \times x}{C_0 - x} = \frac{x^2}{C_0 - x}$$

### The small-dissociation approximation

For most weak acids at reasonable concentrations, x (the amount that dissociates) is very small compared to C₀. If we assume that C₀ − x is approximately equal to C₀, the equation simplifies dramatically:

$$K_a \approx \frac{x^2}{C_0}$$

Solving for x gives:

$$x = \sqrt{K_a \times C_0}$$

Once we have x, which equals [H⁺], we calculate pH = −log(x).

### Checking whether the approximation is valid

After you calculate x, you must check whether it was reasonable to assume that C₀ − x ≈ C₀. The rule is: calculate the percentage dissociation, which is (x ÷ C₀) × 100%. If this percentage is less than 5%, the approximation is valid and your answer is reliable. If it is 5% or greater, you must use the more accurate quadratic method.

<div class="worked">
**Worked Example 2**

**Question:** Calculate the pH of a solution of ethanoic acid, CH₃COOH, with a concentration of 0.10 mol dm⁻³ at 298 K. The Ka of ethanoic acid is 1.8 × 10⁻⁵ mol dm⁻³.

**Strategy:** Set up the ICE table and use the approximation, then check if it is valid.

The equilibrium is: CH₃COOH (aq) ⇌ H⁺ (aq) + CH₃COO⁻ (aq).

| | CH₃COOH | H⁺ | CH₃COO⁻ |
|---|---------|------|----------|
| I | 0.10 | 0 | 0 |
| C | −x | +x | +x |
| E | 0.10 − x | x | x |

Using the approximation: x = √(Ka × C₀) = √(1.8 × 10⁻⁵ × 0.10).

Inside the square root: 1.8 × 10⁻⁵ × 0.10 = 1.8 × 10⁻⁶.

x = √(1.8 × 10⁻⁶) = √1.8 × √10⁻⁶ = 1.34 × 10⁻³ mol dm⁻³.

Therefore [H⁺] = 1.34 × 10⁻³ mol dm⁻³.

pH = −log(1.34 × 10⁻³) = −[log(1.34) + log(10⁻³)] = −[0.127 + (−3.00)] = −(−2.873) = 2.87.

Check the approximation: percentage dissociation = (1.34 × 10⁻³ ÷ 0.10) × 100% = 1.34%. This is less than 5%, so the approximation is valid.

**Why this makes sense:** A weak acid of concentration 0.10 mol dm⁻³ should have a pH between 2 and 3 if it is moderately weak. A strong acid at this concentration would have pH 1.00, and ethanoic acid at 2.87 is indeed much less acidic.
</div>

---

## 4. When You Cannot Use the Approximation — Solving the Quadratic

### Why the approximation sometimes fails

The approximation C₀ − x ≈ C₀ works well when x is tiny compared to C₀. But what if the acid is relatively strong (large Ka) or the solution is very dilute (small C₀)? In these cases, x might be a significant fraction of C₀, and replacing C₀ − x with just C₀ would introduce a large error.

### The full quadratic equation

When the approximation is not valid (percentage dissociation ≥ 5%), you must solve the exact equation:

$$K_a = \frac{x^2}{C_0 - x}$$

Multiplying both sides by (C₀ − x):

$$K_a(C_0 - x) = x^2$$

Expanding:

$$K_a C_0 - K_a x = x^2$$

Rearranging into standard quadratic form ax² + bx + c = 0:

$$x^2 + K_a x - K_a C_0 = 0$$

This quadratic equation can be solved using the quadratic formula:

$$x = \frac{-K_a + \sqrt{K_a^2 + 4K_a C_0}}{2}$$

We use only the positive root (adding the square root, not subtracting it) because x, a concentration, cannot be negative.

<div class="worked">
**Worked Example 3**

**Question:** Calculate the pH of a solution of methanoic acid, HCOOH, with a concentration of 0.010 mol dm⁻³. The Ka of methanoic acid is 1.8 × 10⁻⁴ mol dm⁻³.

**Strategy:** First attempt the approximation, then check it. If it fails, use the quadratic formula.

Try the approximation: x = √(Ka × C₀) = √(1.8 × 10⁻⁴ × 0.010) = √(1.8 × 10⁻⁶).

x = 1.34 × 10⁻³ mol dm⁻³.

Check: percentage dissociation = (1.34 × 10⁻³ ÷ 0.010) × 100% = 13.4%. This is greater than 5%, so the approximation is NOT valid. We must solve the quadratic.

Set up the quadratic: x² + Ka·x − Ka·C₀ = 0.

x² + (1.8 × 10⁻⁴)x − (1.8 × 10⁻⁴ × 0.010) = 0.

x² + 1.8×10⁻⁴x − 1.8×10⁻⁶ = 0.

Apply the quadratic formula. First, calculate the discriminant:

Discriminant = Ka² + 4·Ka·C₀ = (1.8 × 10⁻⁴)² + 4 × (1.8 × 10⁻⁴) × 0.010.

(1.8 × 10⁻⁴)² = 3.24 × 10⁻⁸.

4 × 1.8 × 10⁻⁴ × 0.010 = 7.2 × 10⁻⁶.

Discriminant = 3.24 × 10⁻⁸ + 7.2 × 10⁻⁶ = 7.2324 × 10⁻⁶.

Now: x = [−Ka + √(discriminant)] ÷ 2 = [−1.8 × 10⁻⁴ + √(7.2324 × 10⁻⁶)] ÷ 2.

√(7.2324 × 10⁻⁶) = √7.2324 × √10⁻⁶ = 2.689 × 10⁻³.

−1.8 × 10⁻⁴ + 2.689 × 10⁻³ = (2.689 − 0.180) × 10⁻³ = 2.509 × 10⁻³.

x = 2.509 × 10⁻³ ÷ 2 = 1.25 × 10⁻³ mol dm⁻³.

[H⁺] = 1.25 × 10⁻³ mol dm⁻³.

pH = −log(1.25 × 10⁻³) = −[log(1.25) + log(10⁻³)] = −[0.097 + (−3.00)] = −(−2.90) = 2.90.

**Why this makes sense:** The approximation gave 1.34 × 10⁻³, while the exact value is 1.25 × 10⁻³. The approximation overestimates [H⁺] because it ignores the fact that some of the acid is used up, reducing the amount available for further dissociation. The true pH of 2.90 is slightly higher (less acidic) than the approximate pH of 2.87.
</div>

---

## 5. Finding Ka from pH — Working Backwards

### Using measured pH to determine Ka

Sometimes you know the pH of a weak acid solution and you need to find Ka. This is a common experimental problem. The strategy is: convert pH to [H⁺] (which is x), then substitute into the Ka expression.

<div class="worked">
**Worked Example 4**

**Question:** A solution of a weak monoprotic acid, HA, has a concentration of 0.20 mol dm⁻³. The pH of this solution is measured as 3.00 at 298 K. Calculate the Ka and pKa of this acid.

**Strategy:** First find [H⁺] from pH, then use the Ka expression.

[H⁺] = 10⁻³·⁰⁰ = 1.0 × 10⁻³ mol dm⁻³. This is x.

At equilibrium: [HA] = 0.20 − 1.0 × 10⁻³ = 0.199 mol dm⁻³ (note that we should not approximate here — use the exact value since the percentage dissociation is only 0.5%, but it is good practice to be precise).

Ka = [H⁺][A⁻] ÷ [HA] = (1.0 × 10⁻³)² ÷ 0.199 = 1.0 × 10⁻⁶ ÷ 0.199 = 5.03 × 10⁻⁶ mol dm⁻³.

pKa = −log(5.03 × 10⁻⁶) = 5.30.

**Why this makes sense:** A pH of 3.00 from a 0.20 mol dm⁻³ acid is only moderately acidic — only 0.5% of the acid dissociated. This gives a Ka of about 5 × 10⁻⁶, which is a typical value for a weak acid.
</div>

---

## 6. The Ka-Kb Relationship for Conjugate Pairs

### How a weak acid and its conjugate base are connected

Consider a weak acid, HA, and its conjugate base, A⁻. The conjugate base can act as a weak base in water:

$$\ce{A-(aq) + H2O(l) <=> HA(aq) + OH-(aq)}$$

This reaction has its own equilibrium constant, called Kb (the base dissociation constant):

$$K_b = \frac{[\ce{HA}][\ce{OH-}]}{[\ce{A-}]}$$

There is a deep connection between Ka for HA and Kb for A⁻. If you multiply Ka and Kb:

$$K_a \times K_b = \frac{[\ce{H+}][\ce{A-}]}{[\ce{HA}]} \times \frac{[\ce{HA}][\ce{OH-}]}{[\ce{A-}]} = [\ce{H+}][\ce{OH-}] = K_w$$

All the concentration terms cancel except [H⁺] and [OH⁻], whose product is Kw. Therefore:

$$K_a \times K_b = K_w = 1.0 \times 10^{-14} \ \text{at 298 K}$$

Taking negative logarithms of both sides gives:

$$\text{p}K_a + \text{p}K_b = 14.00 \ \text{at 298 K}$$

This relationship has a powerful implication: the stronger the acid (larger Ka, smaller pKa), the weaker its conjugate base (smaller Kb, larger pKb). If an acid gives away its proton very easily, the conjugate base that remains has very little tendency to take a proton back.

<div class="worked">
**Worked Example 5**

**Question:** The Ka of ethanoic acid, CH₃COOH, is 1.8 × 10⁻⁵ at 298 K. Calculate Kb and pKb for the ethanoate ion, CH₃COO⁻.

**Strategy:** Use Ka × Kb = Kw.

Kb(CH₃COO⁻) = Kw ÷ Ka = (1.0 × 10⁻¹⁴) ÷ (1.8 × 10⁻⁵).

Kb = (1.0 ÷ 1.8) × (10⁻¹⁴ ÷ 10⁻⁵) = 0.556 × 10⁻⁹ = 5.6 × 10⁻¹⁰ mol dm⁻³.

pKb = −log(5.6 × 10⁻¹⁰) = 9.25.

Alternatively, using pKa + pKb = 14.00: pKa = 4.74, so pKb = 14.00 − 4.74 = 9.26. (The small difference is due to rounding.)

**Why this makes sense:** Ethanoic acid is a moderately weak acid (pKa 4.74), so its conjugate base should be a very weak base. Indeed, Kb = 5.6 × 10⁻¹⁰ is extremely small, confirming that the ethanoate ion has very little tendency to accept a proton from water.
</div>

---

## Practice Problems

**Problem 1:** A student prepares a solution of a weak monoprotic acid, HA, by dissolving 0.050 mol of HA in enough distilled water to make 1.00 dm³ of solution. The student measures the pH of this solution and finds it is 4.00 at 298 K. (a) Calculate the hydrogen ion concentration, [H⁺], in this solution. (b) Calculate the acid dissociation constant, Ka, for this acid. (c) Calculate pKa. (d) Determine whether this acid is stronger or weaker than ethanoic acid (Ka = 1.8 × 10⁻⁵) and explain your reasoning.

**Problem 2:** Calculate the pH of a solution of benzoic acid, C₆H₅COOH, with a concentration of 0.050 mol dm⁻³ at 298 K. The Ka of benzoic acid is 6.3 × 10⁻⁵ mol dm⁻³. After calculating x, check whether the small-dissociation approximation was valid for this problem.

**Problem 3:** The pKa of methanoic acid, HCOOH, is 3.74 at 298 K. (a) Calculate the Ka of methanoic acid. (b) A student prepares a solution of methanoic acid with a concentration of 0.20 mol dm⁻³. Using the approximation method, calculate the pH of this solution. (c) Check whether the approximation was valid.

**Problem 4:** Four different weak acids are listed in the table below. Arrange these acids in order of increasing acid strength from weakest to strongest. Explain your reasoning.

| Acid | Property given | Value |
|------|---------------|-------|
| Acid W | pKa | 9.20 |
| Acid X | Ka | 2.0 × 10⁻⁴ mol dm⁻³ |
| Acid Y | pKa | 3.50 |
| Acid Z | Ka | 5.0 × 10⁻¹⁰ mol dm⁻³ |

**Problem 5 (IB-style):** (a) Explain, at the molecular level, why hydrochloric acid, HCl (aq), is classified as a strong acid but ethanoic acid, CH₃COOH (aq), is classified as a weak acid. Your explanation should refer to what happens when each acid is added to water. (b) A student prepares a solution of ethanoic acid, CH₃COOH, with a concentration of 0.50 mol dm⁻³ and measures the pH as 2.52 at 298 K. Calculate the Ka and pKa of ethanoic acid from these data. (c) Using the Kw value of 1.0 × 10⁻¹⁴ at 298 K, calculate Kb for the ethanoate ion, CH₃COO⁻. (d) Ammonia, NH₃, has Kb = 1.8 × 10⁻⁵ mol dm⁻³ at 298 K. Determine whether the ethanoate ion is a stronger base or a weaker base than ammonia. Explain your conclusion by comparing the relevant Kb values.

---

## Answers

### Answer 1

**(a)** The hydrogen ion concentration is found from the pH: [H⁺] = 10⁻⁴·⁰⁰ = 1.0 × 10⁻⁴ mol dm⁻³. This is the value of x, the amount of acid that dissociated.

**(b)** At equilibrium, the weak acid HA has dissociated slightly. The equilibrium concentrations are: [H⁺] = 1.0 × 10⁻⁴ mol dm⁻³, [A⁻] = 1.0 × 10⁻⁴ mol dm⁻³ (because each HA that dissociates produces one H⁺ and one A⁻), and [HA] = 0.050 − 1.0 × 10⁻⁴ = 0.0499 mol dm⁻³ (which is very close to 0.050 because only a tiny amount dissociated).

Ka = [H⁺][A⁻] ÷ [HA] = (1.0 × 10⁻⁴)² ÷ 0.0499 = 1.0 × 10⁻⁸ ÷ 0.0499 ≈ 2.00 × 10⁻⁷ mol dm⁻³.

**(c)** pKa = −log(2.0 × 10⁻⁷) = 6.70.

**(d)** This acid has Ka = 2.0 × 10⁻⁷, which is smaller than Ka of ethanoic acid (1.8 × 10⁻⁵). A smaller Ka means less dissociation, so this acid is weaker than ethanoic acid. Alternatively, pKa of this acid (6.70) is larger than pKa of ethanoic acid (4.74), and a larger pKa means a weaker acid.

### Answer 2

Ka = 6.3 × 10⁻⁵, C₀ = 0.050 mol dm⁻³.

Using the approximation: x = √(Ka × C₀) = √(6.3 × 10⁻⁵ × 0.050).

Inside the square root: 6.3 × 10⁻⁵ × 0.050 = 6.3 × 10⁻⁵ × 5.0 × 10⁻² = 31.5 × 10⁻⁷ = 3.15 × 10⁻⁶.

x = √(3.15 × 10⁻⁶) = √3.15 × √10⁻⁶ = 1.775 × 10⁻³ mol dm⁻³.

Check the approximation: percentage dissociation = (1.775 × 10⁻³ ÷ 0.050) × 100% = 3.55%. This is less than 5%, so the approximation is valid.

pH = −log(1.775 × 10⁻³) = −[log(1.775) + log(10⁻³)] = −[0.249 + (−3.00)] = −(−2.751) = 2.75.

### Answer 3

**(a)** Ka = 10⁻ᵖᴷᵃ = 10⁻³·⁷⁴ = 1.8 × 10⁻⁴ mol dm⁻³.

**(b)** C₀ = 0.20 mol dm⁻³, Ka = 1.8 × 10⁻⁴.

x = √(1.8 × 10⁻⁴ × 0.20) = √(3.6 × 10⁻⁵) = √(36 × 10⁻⁶) = √36 × √10⁻⁶ = 6.0 × 10⁻³ mol dm⁻³.

pH = −log(6.0 × 10⁻³) = −[log(6.0) + log(10⁻³)] = −[0.778 + (−3.00)] = −(−2.222) = 2.22.

**(c)** Check: percentage dissociation = (6.0 × 10⁻³ ÷ 0.20) × 100% = 3.0%. This is less than 5%, so the approximation is valid.

### Answer 4

To compare acid strengths, convert all values to the same scale. I will convert everything to pKa because smaller pKa means stronger acid — this makes ordering easiest.

Acid W: pKa = 9.20 (already given).

Acid X: pKa = −log(2.0 × 10⁻⁴) = −[log(2.0) + log(10⁻⁴)] = −[0.30 + (−4.00)] = −(−3.70) = 3.70.

Acid Y: pKa = 3.50 (already given).

Acid Z: pKa = −log(5.0 × 10⁻¹⁰) = −[log(5.0) + log(10⁻¹⁰)] = −[0.70 + (−10.00)] = −(−9.30) = 9.30.

Now order from weakest (largest pKa) to strongest (smallest pKa): Z (pKa 9.30) → W (pKa 9.20) → X (pKa 3.70) → Y (pKa 3.50).

So, increasing acid strength: Acid Z < Acid W < Acid X < Acid Y.

Notice that Acids Z and W are very close in strength (pKa values differ by only 0.10). Acids X and Y are both much stronger — their Ka values are about 10⁵ to 10⁶ times larger than those of Z and W.

### Answer 5

**(a)** When hydrogen chloride gas dissolves in water, every HCl molecule breaks apart. The H—Cl bond is highly polarised and water molecules can easily pull the hydrogen away as H⁺. The reaction HCl (aq) → H⁺ (aq) + Cl⁻ (aq) goes to completion, and no intact HCl molecules remain. This is complete dissociation, which defines a strong acid.

When ethanoic acid dissolves in water, only a tiny fraction (about 1% in a 0.1 mol dm⁻³ solution) of the CH₃COOH molecules break apart. The O—H bond in the carboxylic acid group is stronger and less easily broken by water. The reaction CH₃COOH (aq) ⇌ H⁺ (aq) + CH₃COO⁻ (aq) establishes an equilibrium that lies heavily to the left — most molecules stay intact. The double arrow shows that both forward and reverse reactions occur. This partial dissociation defines a weak acid.

**(b)** From pH = 2.52: [H⁺] = 10⁻²·⁵².

We can split this: 10⁻²·⁵² = 10⁻⁰·⁵² × 10⁻².

10⁻⁰·⁵² = 1 ÷ 10⁰·⁵² ≈ 1 ÷ 3.31 ≈ 0.302.

[H⁺] = 0.302 × 10⁻² = 3.02 × 10⁻³ mol dm⁻³.

Now: Ka = [H⁺]² ÷ ([CH₃COOH] − [H⁺]). Using the exact expression:

Ka = (3.02 × 10⁻³)² ÷ (0.50 − 3.02 × 10⁻³).

(3.02 × 10⁻³)² = 9.12 × 10⁻⁶.

0.50 − 0.00302 = 0.49698 ≈ 0.497.

Ka = 9.12 × 10⁻⁶ ÷ 0.497 = 1.84 × 10⁻⁵ mol dm⁻³.

pKa = −log(1.84 × 10⁻⁵) ≈ 4.74.

**(c)** Kb(CH₃COO⁻) = Kw ÷ Ka = (1.0 × 10⁻¹⁴) ÷ (1.84 × 10⁻⁵) = 5.4 × 10⁻¹⁰ mol dm⁻³.

**(d)** Comparing Kb values: the ethanoate ion has Kb = 5.4 × 10⁻¹⁰, and ammonia has Kb = 1.8 × 10⁻⁵. Since 5.4 × 10⁻¹⁰ is much smaller than 1.8 × 10⁻⁵ (by a factor of about 33,000), the ethanoate ion is a much weaker base than ammonia. This makes sense because ethanoic acid is a stronger acid than the ammonium ion (NH₄⁺, which has Ka = 5.6 × 10⁻¹⁰), and the stronger the acid, the weaker its conjugate base.
