# Lesson 24: The Equilibrium Constant Kc — Expression, Magnitude, and Reaction Quotient Q

## What You'll Learn
- Write the equilibrium constant expression Kc for any homogeneous or heterogeneous equilibrium
- Interpret the magnitude of Kc to determine whether reactants or products are favoured
- Explain why Kc depends only on temperature and not on concentration or pressure
- Calculate the reaction quotient Q and use it to predict the direction a reaction will proceed
- Perform simple Kc calculations from equilibrium concentration data

---

## 1. The Kc Expression

### What This Concept Is and Why It Matters

When a reversible reaction reaches equilibrium, the concentrations of reactants and products stop changing. But there is a deeper mathematical regularity: for any given reaction at a fixed temperature, the ratio of product concentrations to reactant concentrations — each raised to the power of its stoichiometric coefficient — always has the same numerical value. This value is called the **equilibrium constant**, given the symbol Kc (the "c" stands for concentration).

The Kc expression lets you calculate the equilibrium constant from measured concentrations, or predict equilibrium concentrations if you know Kc. It is one of the most powerful quantitative tools in chemistry.

### How to Write the Kc Expression

Consider a general reversible reaction:

\[
a\text{A} + b\text{B} \rightleftharpoons c\text{C} + d\text{D}
\]

The equilibrium constant Kc is defined as:

\[
K_c = \frac{[\text{C}]^c [\text{D}]^d}{[\text{A}]^a [\text{B}]^b}
\]

Here is what each part means:

- **[A], [B], [C], [D]** are the equilibrium concentrations of the reactants and products, measured in mol dm⁻³.
- **The exponents a, b, c, d** are the stoichiometric coefficients from the balanced equation. The coefficient in front of A becomes the exponent for [A] in the denominator. The coefficient in front of C becomes the exponent for [C] in the numerator.
- **Products go in the numerator** (top of the fraction), and **reactants go in the denominator** (bottom of the fraction).
- The expression is valid only when the system is **at equilibrium**. If the system is not at equilibrium, the same expression gives Q (the reaction quotient), which we will discuss later.

### What to Include and What to Exclude

This is a critical rule that many students get wrong: **solids and pure liquids do not appear in the Kc expression.** The reason is that the concentration of a pure solid or a pure liquid is constant — it does not change during the reaction, no matter how much of it is present. Only species whose concentrations can change appear in Kc.

Specifically:
- **Gases (g):** Always included.
- **Aqueous solutions (aq):** Always included.
- **Pure solids (s):** Never included. Their "activity" is defined as 1.
- **Pure liquids (l):** Never included, unless the reaction takes place in a solution where the liquid is also acting as the solvent and participates in the reaction in a non-negligible way (for IB, in esterification reactions, water and alcohols may be included since they are not in vast excess as solvent).

### Worked Example: Writing Kc Expressions for Different Types of Reactions

**Reaction 1:** 2SO₂(g) + O₂(g) ⇌ 2SO₃(g)

All species are gases, so all appear in the expression:

\[
K_c = \frac{[\text{SO}_3]^2}{[\text{SO}_2]^2 [\text{O}_2]}
\]

**Reaction 2:** N₂(g) + 3H₂(g) ⇌ 2NH₃(g)

All gases:

\[
K_c = \frac{[\text{NH}_3]^2}{[\text{N}_2][\text{H}_2]^3}
\]

**Reaction 3:** CaCO₃(s) ⇌ CaO(s) + CO₂(g)

CaCO₃ and CaO are both solids — they do not appear. Only CO₂ (a gas) appears:

\[
K_c = [\text{CO}_2]
\]

This tells you something interesting: for this reaction, at a given temperature, the concentration (and therefore the partial pressure) of CO₂ at equilibrium is fixed, regardless of how much CaCO₃ or CaO is present — as long as both solids are present.

**Reaction 4:** CH₃COOH(aq) + H₂O(l) ⇌ CH₃COO⁻(aq) + H₃O⁺(aq)

Water is a pure liquid and is the solvent, present in vast excess. Its concentration remains essentially constant (about 55 mol dm⁻³), so it is omitted:

\[
K_c = \frac{[\text{CH}_3\text{COO}^-][\text{H}_3\text{O}^+]}{[\text{CH}_3\text{COOH}]}
\]

---

## 2. The Magnitude of Kc

### What This Concept Is and Why It Matters

The numerical value of Kc tells you, at a glance, whether the equilibrium position lies to the right (products favoured) or to the left (reactants favoured).

**Kc is very large (much greater than 1, such as 10⁵ or 10¹⁰):** At equilibrium, the numerator (product concentrations) is much larger than the denominator (reactant concentrations). This means the reaction has gone nearly to completion — most of the reactants have been converted to products. The equilibrium "lies to the right."

**Kc is approximately 1 (between about 0.1 and 10):** At equilibrium, there are significant amounts of both reactants and products. Neither side is strongly favoured.

**Kc is very small (much less than 1, such as 10⁻⁵ or 10⁻¹⁰):** At equilibrium, the denominator is much larger than the numerator. This means very little product has formed. The reaction hardly proceeds at all before reaching equilibrium. The equilibrium "lies to the left."

A key point: the magnitude of Kc tells you nothing about how fast equilibrium is reached. A reaction with Kc = 10²⁰ might take a million years to reach equilibrium if its activation energy is enormous. Kc is about thermodynamics (where equilibrium lies), not kinetics (how fast you get there).

### Worked Example 1: Interpreting Kc Values

**Problem:** At a certain temperature, the reaction H₂(g) + I₂(g) ⇌ 2HI(g) has Kc = 50. At the same temperature, the decomposition of ammonia 2NH₃(g) ⇌ N₂(g) + 3H₂(g) has Kc = 1.0 × 10⁻⁵. Interpret what these two values tell you about the equilibrium composition in each case.

**Strategy:** Compare each Kc value to 1 and reason about the relative sizes of the numerator and denominator.

**Solution:** For H₂ + I₂ ⇌ 2HI, Kc = 50. Since 50 is much greater than 1, the numerator [HI]² must be larger than the denominator [H₂][I₂] by a factor of 50. This means that at equilibrium, the concentration of HI is significantly higher than the concentrations of H₂ and I₂. The equilibrium favours products — the reaction goes a long way toward forming HI.

For 2NH₃ ⇌ N₂ + 3H₂, Kc = 1.0 × 10⁻⁵ (which is 0.00001). Since this is much less than 1, the denominator [NH₃]² must be much larger than the numerator [N₂][H₂]³. At equilibrium, the concentration of NH₃ dominates — only tiny amounts of N₂ and H₂ are present. The equilibrium heavily favours the reactant (NH₃) for this decomposition reaction.

---

## 3. Kc Depends Only on Temperature

### What This Concept Is and Why It Matters

The equilibrium constant Kc is not truly a universal constant — it changes with temperature. But for a given reaction at a given temperature, Kc has one fixed value. This is a profound and useful fact.

If you change the concentration of a reactant or product, the system is disturbed from equilibrium and will shift to re-establish equilibrium, but once it settles, the ratio of concentrations (raised to their powers) will return to exactly the same Kc value. If you change the pressure (for a gas-phase reaction), the system shifts, but Kc remains unchanged. Concentration and pressure changes shift the position of equilibrium but never change Kc.

Temperature is different. Changing the temperature actually changes the numerical value of Kc. The direction of the change depends on whether the forward reaction is endothermic or exothermic:

- **Exothermic forward reaction (ΔH negative):** Increasing the temperature shifts equilibrium toward reactants (left), so Kc **decreases**. Decreasing the temperature shifts equilibrium toward products (right), so Kc **increases**.

- **Endothermic forward reaction (ΔH positive):** Increasing the temperature shifts equilibrium toward products (right), so Kc **increases**. Decreasing the temperature shifts equilibrium toward reactants (left), so Kc **decreases**.

This is consistent with Le Chatelier's Principle: adding heat to an exothermic reaction reduces Kc because the equilibrium shifts away from products. Adding heat to an endothermic reaction increases Kc because the equilibrium shifts toward products.

---

## 4. The Reaction Quotient Q

### What This Concept Is and Why It Matters

Suppose you mix some reactants and products in a container. You do not know whether the mixture is at equilibrium. You need a way to predict which direction the reaction will go to reach equilibrium. The **reaction quotient**, given the symbol Q, serves this purpose.

Q is calculated using exactly the same formula as Kc — products over reactants, each raised to their stoichiometric coefficients — but using the **current** concentrations, which may or may not be the equilibrium concentrations:

\[
Q = \frac{[\text{C}]^c [\text{D}]^d}{[\text{A}]^a [\text{B}]^b}
\]

Once you have calculated Q, you compare it to the known value of Kc at that temperature:

- **If Q < Kc:** The numerator (products) is too small relative to the denominator (reactants) compared to what it should be at equilibrium. The reaction will proceed in the **forward direction** (toward products) to increase the numerator and decrease the denominator, raising Q until it equals Kc.

- **If Q = Kc:** The system is already at equilibrium. No net reaction occurs in either direction.

- **If Q > Kc:** The numerator is too large relative to the denominator. The reaction will proceed in the **reverse direction** (toward reactants) to decrease the numerator and increase the denominator, lowering Q until it equals Kc.

### Worked Example 2: Using Q to Predict Reaction Direction

**Problem:** For the reaction H₂(g) + I₂(g) ⇌ 2HI(g), the equilibrium constant Kc is 50 at 700 K. A chemist prepares a mixture with the following concentrations: [H₂] = 0.10 mol dm⁻³, [I₂] = 0.20 mol dm⁻³, and [HI] = 0.40 mol dm⁻³. Predict the direction in which the reaction will proceed to reach equilibrium.

**Strategy:** Calculate Q using the given concentrations and the same formula as Kc. Then compare Q to Kc.

**Solution:**

\[
Q = \frac{[\text{HI}]^2}{[\text{H}_2][\text{I}_2]} = \frac{(0.40)^2}{(0.10)(0.20)}
\]

Calculate the numerator: (0.40)² = 0.16.

Calculate the denominator: 0.10 × 0.20 = 0.020.

\[
Q = \frac{0.16}{0.020} = 8.0
\]

Now compare: Q = 8.0, and Kc = 50. Since Q (8.0) is less than Kc (50), the value of Q needs to increase to reach equilibrium. Q increases when the numerator (products) gets larger and the denominator (reactants) gets smaller. This means the reaction must proceed in the **forward direction**, converting H₂ and I₂ into more HI.

**Why this makes sense:** With the given concentrations, there is relatively little HI compared to H₂ and I₂ — the system has not yet made enough products. It needs to move forward to establish equilibrium.

---

## 5. Simple Kc Calculations

### Type 1: Calculate Kc from Equilibrium Concentrations

**Worked Example 3:** The reaction 2SO₂(g) + O₂(g) ⇌ 2SO₃(g) was allowed to reach equilibrium in a sealed container at a fixed temperature. Analysis of the mixture showed the following equilibrium concentrations: [SO₂] = 0.40 mol dm⁻³, [O₂] = 0.20 mol dm⁻³, and [SO₃] = 0.80 mol dm⁻³. Calculate the value of Kc at this temperature.

**Strategy:** Write the Kc expression, substitute the equilibrium concentrations, and compute.

**Solution:**

The balanced equation is 2SO₂ + O₂ ⇌ 2SO₃. The Kc expression is:

\[
K_c = \frac{[\text{SO}_3]^2}{[\text{SO}_2]^2 [\text{O}_2]}
\]

Substitute the values:

\[
K_c = \frac{(0.80)^2}{(0.40)^2 (0.20)}
\]

Calculate step by step:

(0.80)² = 0.64

(0.40)² = 0.16

0.16 × 0.20 = 0.032

\[
K_c = \frac{0.64}{0.032} = 20
\]

**Why this makes sense:** Kc = 20 is greater than 1, indicating that products are favoured — which matches the data, since [SO₃] is higher than [SO₂] despite the squared term.

### Type 2: Calculate an Unknown Equilibrium Concentration Given Kc

**Worked Example 4:** For the reaction H₂(g) + I₂(g) ⇌ 2HI(g), the equilibrium constant Kc has a value of 49 at a particular temperature. Analysis of an equilibrium mixture shows [H₂] = 0.10 mol dm⁻³ and [HI] = 0.70 mol dm⁻³. Calculate the equilibrium concentration of I₂.

**Strategy:** Write the Kc expression, substitute the known values, and solve for the unknown.

**Solution:**

\[
K_c = \frac{[\text{HI}]^2}{[\text{H}_2][\text{I}_2]} = 49
\]

Substitute the known values:

\[
49 = \frac{(0.70)^2}{(0.10)[\text{I}_2]}
\]

Calculate (0.70)² = 0.49:

\[
49 = \frac{0.49}{(0.10)[\text{I}_2]}
\]

Multiply both sides by (0.10)[I₂]:

\[
49 \times (0.10)[\text{I}_2] = 0.49
\]

\[
4.9 [\text{I}_2] = 0.49
\]

\[
[\text{I}_2] = \frac{0.49}{4.9} = 0.10 \text{ mol dm}^{-3}
\]

**Why this makes sense:** Since Kc = 49 and [H₂] = 0.10, we should have [I₂] = 0.10 as well. The symmetry of the reaction (one H₂ and one I₂ making two HI) means that at equilibrium, if you started with equal amounts and Kc is reasonably large, you end up with equal concentrations of the two reactants. And indeed [I₂] = [H₂] = 0.10 mol dm⁻³.

---

## Practice Problems

1. Write the equilibrium constant expression Kc for each of the following reactions. In each case, explain which species are included and which (if any) are omitted, and state the reason for any omissions.

   (a) 2NO(g) + O₂(g) ⇌ 2NO₂(g)

   (b) CH₄(g) + H₂O(g) ⇌ CO(g) + 3H₂(g)

   (c) Fe₂O₃(s) + 3CO(g) ⇌ 2Fe(s) + 3CO₂(g)

2. For the reaction CO(g) + 2H₂(g) ⇌ CH₃OH(g), the equilibrium constant Kc is 14.5 at a temperature of 500 K. At a particular moment during the reaction, the concentrations in the reaction vessel are: [CO] = 0.20 mol dm⁻³, [H₂] = 0.10 mol dm⁻³, and [CH₃OH] = 0.040 mol dm⁻³. Calculate the reaction quotient Q and use it to predict whether the reaction will proceed in the forward direction or the reverse direction to reach equilibrium. Explain your reasoning.

3. The equilibrium N₂O₄(g) ⇌ 2NO₂(g) is established in a sealed container at a certain temperature. Analysis of the equilibrium mixture gives the following concentrations: [N₂O₄] = 0.20 mol dm⁻³ and [NO₂] = 0.40 mol dm⁻³. Calculate the value of Kc at this temperature.

4. For the equilibrium PCl₅(g) ⇌ PCl₃(g) + Cl₂(g), the equilibrium constant Kc is 0.040 at a certain temperature. Analysis of an equilibrium mixture shows [PCl₅] = 0.10 mol dm⁻³ and [Cl₂] = 0.020 mol dm⁻³. Calculate the equilibrium concentration of PCl₃.

5. **(IB-Exam Style)** The decomposition of hydrogen iodide gas is represented by the following equilibrium:

   \[
   2\text{HI}(\text{g}) \rightleftharpoons \text{H}_2(\text{g}) + \text{I}_2(\text{g}) \quad \Delta H = +53 \text{ kJ mol}^{-1}
   \]

   At a temperature of 700 K, the equilibrium constant Kc for this reaction is 0.020.

   (a) State, with a brief explanation, what the value Kc = 0.020 tells you about the relative amounts of reactants and products present in the equilibrium mixture at 700 K.

   (b) The reaction is endothermic in the forward direction as written. Predict, with reasoning, whether the value of Kc at 800 K will be larger than, smaller than, or equal to 0.020.

   (c) In an experiment at 700 K, a chemist mixes HI, H₂, and I₂ in a sealed container so that the initial concentration of each gas is 0.50 mol dm⁻³. Calculate the reaction quotient Q for this mixture and determine the direction in which the reaction will proceed to reach equilibrium.

   (d) The chemist allows the mixture described in part (c) to reach equilibrium at 700 K. Sketch a graph showing how the concentration of HI changes from the initial mixing (t = 0) until equilibrium is established, and explain the shape of your graph.

---

## Answers

### Answer 1

**(a)** Kc = [NO₂]² / ([NO]²[O₂]). All three species are gases, so all appear in the expression. The exponent 2 for NO₂ and NO comes from the stoichiometric coefficient 2 in front of each in the balanced equation.

**(b)** Kc = [CO][H₂]³ / ([CH₄][H₂O]). All four species are gases, so all appear. The [H₂] has an exponent of 3 because the coefficient of H₂ in the balanced equation is 3.

**(c)** Kc = [CO₂]³ / [CO]³. The species Fe₂O₃(s) and Fe(s) are solids. Solids have constant concentration (their "activity" is defined as 1) and are omitted from the Kc expression. Only the gases CO and CO₂, whose concentrations can vary, appear. Both have exponents of 3 from their stoichiometric coefficients. Note that the expression could also be written as Kc = ([CO₂]/[CO])³.

### Answer 2

The Kc expression for CO(g) + 2H₂(g) ⇌ CH₃OH(g) is:

\[
Q = \frac{[\text{CH}_3\text{OH}]}{[\text{CO}][\text{H}_2]^2}
\]

Substitute the given concentrations:

\[
Q = \frac{0.040}{(0.20)(0.10)^2} = \frac{0.040}{(0.20)(0.010)} = \frac{0.040}{0.0020} = 20
\]

Now compare: Q = 20 and Kc = 14.5. Since Q (20) is greater than Kc (14.5), the value of Q needs to decrease to reach equilibrium. Q decreases when the numerator (product concentration) gets smaller and the denominator (reactant concentrations) gets larger. This means the reaction will proceed in the **reverse direction** — CH₃OH will decompose into CO and H₂ until the ratio of concentrations equals Kc = 14.5.

### Answer 3

The Kc expression for N₂O₄(g) ⇌ 2NO₂(g) is:

\[
K_c = \frac{[\text{NO}_2]^2}{[\text{N}_2\text{O}_4]}
\]

Substitute the equilibrium concentrations:

\[
K_c = \frac{(0.40)^2}{0.20} = \frac{0.16}{0.20} = 0.80
\]

The value of Kc is **0.80**. Since Kc is less than 1 (but not extremely small), the equilibrium slightly favours the reactant N₂O₄, but significant amounts of both species are present.

### Answer 4

The Kc expression for PCl₅(g) ⇌ PCl₃(g) + Cl₂(g) is:

\[
K_c = \frac{[\text{PCl}_3][\text{Cl}_2]}{[\text{PCl}_5]}
\]

Substitute Kc = 0.040, [PCl₅] = 0.10, and [Cl₂] = 0.020:

\[
0.040 = \frac{[\text{PCl}_3](0.020)}{0.10}
\]

Multiply both sides by 0.10:

\[
0.040 \times 0.10 = [\text{PCl}_3] \times 0.020
\]

\[
0.0040 = [\text{PCl}_3] \times 0.020
\]

\[
[\text{PCl}_3] = \frac{0.0040}{0.020} = 0.20 \text{ mol dm}^{-3}
\]

The equilibrium concentration of PCl₃ is **0.20 mol dm⁻³**.

### Answer 5

**(a)** Kc = 0.020 is a number much less than 1. Since Kc = [H₂][I₂] / [HI]², a value of 0.020 means the denominator [HI]² is much larger than the numerator [H₂][I₂] — by a factor of 1/0.020 = 50. This tells us that at equilibrium at 700 K, the reaction mixture contains much more HI than H₂ and I₂. The equilibrium position lies to the left — the reactants (HI in this case, since the reaction is written as 2HI ⇌ H₂ + I₂) are strongly favoured.

**(b)** The forward reaction as written (2HI → H₂ + I₂) is endothermic, with ΔH = +53 kJ mol⁻¹. According to Le Chatelier's Principle, increasing the temperature favours the endothermic direction — in this case, the forward direction. The equilibrium shifts to the right, producing more H₂ and I₂ at the expense of HI. This means the numerator [H₂][I₂] increases and the denominator [HI]² decreases. Therefore, the value of Kc **increases**. Kc at 800 K will be **larger** than 0.020.

**(c)** The expression for Q is the same as for Kc:

\[
Q = \frac{[\text{H}_2][\text{I}_2]}{[\text{HI}]^2} = \frac{(0.50)(0.50)}{(0.50)^2} = \frac{0.25}{0.25} = 1.0
\]

Now compare Q = 1.0 to Kc = 0.020. Since Q (1.0) is much greater than Kc (0.020), the quotient is too large — there are too many products (H₂ and I₂) relative to reactant (HI) compared to what equilibrium requires. The reaction will proceed in the **reverse direction** (from right to left: H₂ + I₂ → 2HI) to decrease Q toward Kc.

**(d)** At t = 0, the concentration of HI is 0.50 mol dm⁻³. Since Q > Kc, the reaction proceeds in the reverse direction — H₂ and I₂ combine to form HI. This means the concentration of HI begins to increase from its initial value. As the reaction proceeds, the rate of the reverse reaction slows down (because H₂ and I₂ are being consumed) and the rate of the forward reaction speeds up (because HI is being produced). Eventually the two rates become equal at equilibrium. On the graph, the [HI] starts at 0.50, then rises along a curve that is steep at first (when the reverse reaction is fastest) and gradually flattens out as equilibrium is approached. At equilibrium, the concentration reaches a constant value (which from Kc = 0.020 can be calculated to be higher than 0.50). The graph is a curve that asymptotically approaches a horizontal line — the equilibrium concentration of HI.
