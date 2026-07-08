# Lesson 18: Entropy, Gibbs Free Energy, and Spontaneity (HL)

## What You'll Learn
- Define entropy as a measure of disorder and energy dispersal in a system
- Predict whether the entropy change (ΔS) for a reaction is positive or negative by examining states and particle counts
- Calculate ΔS⦵ for a reaction using standard entropy values from a data table
- Calculate the Gibbs free energy change (ΔG⦵) using the equation ΔG⦵ = ΔH⦵ − TΔS⦵
- Use the sign of ΔG⦵ to determine whether a reaction is spontaneous at a given temperature
- Calculate the temperature at which a reaction becomes spontaneous by setting ΔG = 0

---

## 1. What Is Entropy?

### A New Way to Think About Chemical Change

In Lessons 14 through 17, we focused almost entirely on enthalpy — the heat absorbed or released by a reaction. But enthalpy alone cannot explain why some reactions happen and others do not. There is a second factor that determines whether a chemical process will occur: **entropy**.

Entropy (symbol: S) is a measure of the **disorder** of a system. More precisely, entropy measures the number of ways that energy can be distributed among the particles in a system. A system with high entropy has its energy spread out among many different arrangements; a system with low entropy has its energy concentrated in fewer arrangements.

### An Analogy: A Deck of Cards

Imagine a brand-new deck of playing cards, perfectly sorted by suit and rank. This ordered arrangement has low entropy — there is essentially only one way to arrange the cards in this order. Now shuffle the deck thoroughly. The cards are now in a random, disordered arrangement. There are an enormous number of possible random arrangements. The shuffled deck has high entropy.

In chemistry, nature tends to favor states with higher entropy — just as a shuffled deck is far more probable than a perfectly sorted one, a disordered distribution of molecules is far more probable than an ordered one.

### Key Facts About Entropy

**Fact 1: Solids have the lowest entropy.** In a solid, particles are locked into fixed positions in a crystal lattice. They can vibrate, but they cannot move from place to place. The arrangement is highly ordered, so the number of ways to distribute energy is relatively small. Entropy values for solids are low.

**Fact 2: Liquids have higher entropy than solids.** When a solid melts, the particles gain the ability to move past one another. The arrangement becomes less ordered, and the number of ways to distribute energy increases. The entropy of a liquid is always greater than the entropy of the same substance as a solid at the same temperature.

**Fact 3: Gases have much higher entropy than liquids.** In a gas, particles move freely in all directions and occupy the entire volume of their container. There are vastly more possible arrangements. The entropy of a gas is much larger than the entropy of the same substance as a liquid.

**Fact 4: More particles mean more entropy.** If a reaction produces more gas molecules than it consumes, the entropy increases (ΔS is positive). More particles mean more possible arrangements and more ways to distribute energy.

**Fact 5: Dissolving usually increases entropy.** When a solid dissolves, its ions or molecules become dispersed throughout the solution. This spread-out arrangement has much higher entropy than the orderly crystal lattice.

### A Critical Difference Between Entropy and Enthalpy

There is a very important difference between standard entropy values (S⦵) and standard enthalpies of formation (ΔH_f⦵) that many students miss:

- ΔH_f⦵ of an **element** in its standard state is **zero by definition**.
- S⦵ of an **element** in its standard state is **NOT zero**. Every substance, including elements, has a positive entropy at temperatures above absolute zero.

For example, at 298 K:
- S⦵[H₂(g)] = 131 J K⁻¹ mol⁻¹
- S⦵[O₂(g)] = 205 J K⁻¹ mol⁻¹
- S⦵[C(s, graphite)] = 5.7 J K⁻¹ mol⁻¹
- S⦵[Fe(s)] = 27 J K⁻¹ mol⁻¹

Notice that even graphite, a highly ordered solid, has a small positive entropy. Only at absolute zero (0 K) would a perfectly ordered crystal have S = 0. This is the Third Law of Thermodynamics.

### Units of Entropy

Entropy is measured in **J K⁻¹ mol⁻¹** (joules per kelvin per mole). Note the unit: joules, not kilojoules. This is the source of one of the most common calculation errors in this topic — forgetting to convert between joules and kilojoules when combining ΔH (usually in kJ) and ΔS (always in J K⁻¹). We will address this carefully in Section 4.

---

## 2. Predicting the Sign of ΔS

### What to Look For

You can predict whether the entropy change (ΔS) for a reaction is positive or negative by looking at the balanced chemical equation and asking two questions:

**Question 1: Is there a change of state?**
If a reaction produces gases from solids or liquids, ΔS is strongly positive. If a reaction consumes gases to make solids or liquids, ΔS is strongly negative. Changes of state almost always dominate over other considerations.

**Question 2: Does the number of gas molecules change?**
If a reaction has more gas molecules on the product side than on the reactant side, ΔS is positive (more disorder). If there are fewer gas molecules on the product side, ΔS is negative (more order).

### Worked Example 1: Predicting ΔS Signs

**Problem:** Predict the sign of ΔS (positive or negative) for each of the following reactions. Give a brief reason for each prediction.

(a) CaCO₃(s) → CaO(s) + CO₂(g)
(b) N₂(g) + 3H₂(g) → 2NH₃(g)
(c) H₂O(l) → H₂O(s)
(d) NH₄NO₃(s) → NH₄⁺(aq) + NO₃⁻(aq)

**Answers:**

(a) **ΔS is positive.** On the reactant side, there are zero gas molecules (only a solid). On the product side, one molecule of CO₂ gas is produced. Producing a gas from a solid represents a huge increase in disorder.

(b) **ΔS is negative.** Count the gas molecules: on the reactant side, there are 1 + 3 = 4 moles of gas. On the product side, there are only 2 moles of gas. Fewer gas molecules means fewer possible arrangements, so entropy decreases.

(c) **ΔS is negative.** Liquid water freezing to solid ice represents a transition from a disordered state (liquid, where molecules move freely) to an ordered state (solid, where molecules are locked in a crystal lattice). Freezing always decreases entropy.

(d) **ΔS is positive.** A solid ionic compound dissolves, releasing ions that become dispersed throughout the aqueous solution. The ions in solution have far more possible arrangements than they did in the ordered crystal lattice. Dissolving a solid almost always increases entropy.

### Common Misconception

Students sometimes think that if the number of molecules stays the same, ΔS must be zero. This is not correct. The entropy change depends on many factors, including the complexity of the molecules and the states involved. For example, the reaction H₂(g) + I₂(g) → 2HI(g) has the same number of gas molecules on both sides (2 → 2), but the actual ΔS is small but not zero.

---

## 3. Calculating ΔS⦵ Using Standard Entropy Values

### The Formula

The standard entropy change for a reaction is calculated in the same way we calculated ΔH from enthalpies of formation:

**ΔS⦵ = ΣS⦵(products) − ΣS⦵(reactants)**

You take each product's standard entropy, multiply it by the coefficient in the balanced equation, add them all up, then subtract the sum for the reactants (each multiplied by its coefficient).

### Worked Example 2: Calculating ΔS⦵

**Problem:** Calculate the standard entropy change for the reaction: 2H₂(g) + O₂(g) → 2H₂O(l). The standard entropy values are:
- S⦵[H₂(g)] = 131 J K⁻¹ mol⁻¹
- S⦵[O₂(g)] = 205 J K⁻¹ mol⁻¹
- S⦵[H₂O(l)] = 70 J K⁻¹ mol⁻¹

**Strategy:** Apply the formula. Multiply each S⦵ by its coefficient.

**Step 1 — Sum of S⦵ for products:**
ΣS⦵(products) = 2 × 70 = 140 J K⁻¹.

**Step 2 — Sum of S⦵ for reactants:**
ΣS⦵(reactants) = 2 × 131 + 1 × 205 = 262 + 205 = 467 J K⁻¹.

**Step 3 — Calculate ΔS⦵:**
ΔS⦵ = 140 − 467 = −327 J K⁻¹ mol⁻¹.

**Why this makes sense:** The reaction converts 3 moles of gas (2H₂ + O₂) into 2 moles of liquid water. Gases have much higher entropy than liquids, so a large decrease in entropy is expected. The negative sign is correct.

### Worked Example 3: Formation of Ammonia

**Problem:** Calculate ΔS⦵ for: N₂(g) + 3H₂(g) → 2NH₃(g). Data:
- S⦵[N₂(g)] = 192 J K⁻¹ mol⁻¹
- S⦵[H₂(g)] = 131 J K⁻¹ mol⁻¹
- S⦵[NH₃(g)] = 193 J K⁻¹ mol⁻¹

**Calculation:**
ΣS⦵(products) = 2 × 193 = 386 J K⁻¹.
ΣS⦵(reactants) = 1 × 192 + 3 × 131 = 192 + 393 = 585 J K⁻¹.
ΔS⦵ = 386 − 585 = −199 J K⁻¹ mol⁻¹.

**Why this makes sense:** Four moles of gas become two moles of gas. Fewer gas molecules means lower entropy, so ΔS is negative.

---

## 4. Gibbs Free Energy: Combining Enthalpy and Entropy

### The Problem That Gibbs Free Energy Solves

We now have two quantities that describe a reaction: ΔH (the enthalpy change, which tells us about heat) and ΔS (the entropy change, which tells us about disorder). But how do we decide whether a reaction will actually happen? Some reactions are exothermic but do not occur (like the conversion of diamond to graphite at room temperature — it is exothermic but incredibly slow). Some reactions are endothermic but occur spontaneously (like the dissolving of ammonium nitrate in water, which gets cold but happens readily).

The answer is that both ΔH and ΔS matter. The quantity that combines them is called the **Gibbs free energy change**, symbol ΔG.

### The Definition of Gibbs Free Energy

**ΔG⦵ = ΔH⦵ − TΔS⦵**

Where:
- ΔG⦵ is the standard Gibbs free energy change (in J mol⁻¹ or kJ mol⁻¹)
- ΔH⦵ is the standard enthalpy change (typically in kJ mol⁻¹)
- T is the absolute temperature in **kelvin (K)**
- ΔS⦵ is the standard entropy change (in J K⁻¹ mol⁻¹)

### What ΔG Tells Us

The sign of ΔG tells us whether a reaction is spontaneous (thermodynamically feasible) under the given conditions:

- If ΔG < 0 (negative): The reaction is **spontaneous** in the forward direction. It can occur without an external input of energy.
- If ΔG > 0 (positive): The reaction is **non-spontaneous** in the forward direction. It will not occur unless energy is supplied. (The reverse reaction would be spontaneous.)
- If ΔG = 0: The reaction is at **equilibrium**. The forward and reverse rates are equal.

### The Meaning of "Spontaneous"

In thermodynamics, "spontaneous" does not mean "fast." A spontaneous reaction can be very slow. For example, the combustion of diamond in oxygen has a negative ΔG, meaning it is thermodynamically spontaneous, but a diamond ring does not burst into flames when you wear it because the activation energy is very high. "Spontaneous" means that the reaction is energetically and entropically favored — it will eventually happen if given a suitable pathway (or an eternity).

### The Critical Unit Trap

This is where many students lose marks. Look at the equation: ΔG = ΔH − TΔS. The term TΔS must have the same units as ΔH. ΔH is typically given in kilojoules per mole (kJ mol⁻¹). ΔS is always given in joules per kelvin per mole (J K⁻¹ mol⁻¹). When you multiply T (in K) by ΔS (in J K⁻¹ mol⁻¹), you get an answer in J mol⁻¹.

Therefore, before you can subtract TΔS from ΔH, you must either:
- Convert ΔH from kJ to J (multiply by 1000), do the calculation in joules, and then convert back to kJ if needed, OR
- Convert TΔS from J to kJ (divide by 1000) and then subtract from ΔH in kJ.

I strongly recommend the first method: convert everything to joules, calculate, then convert back. This reduces the chance of a factor-of-1000 error.

### Worked Example 4: Calculating ΔG

**Problem:** For the decomposition of calcium carbonate: CaCO₃(s) → CaO(s) + CO₂(g), the following data are given: ΔH⦵ = +178 kJ mol⁻¹, ΔS⦵ = +161 J K⁻¹ mol⁻¹. Calculate ΔG⦵ at 298 K and determine whether the reaction is spontaneous at this temperature.

**Strategy:** Convert ΔH to J, compute TΔS in J, subtract, then convert back to kJ if desired.

**Calculation:**
ΔH⦵ = +178 kJ mol⁻¹ = +178,000 J mol⁻¹.
TΔS⦵ = 298 K × 161 J K⁻¹ mol⁻¹ = 47,978 J mol⁻¹.
ΔG⦵ = 178,000 − 47,978 = +130,022 J mol⁻¹ = +130 kJ mol⁻¹.

ΔG⦵ is positive, so the reaction is **not spontaneous** at 298 K. This makes sense: calcium carbonate (limestone, chalk, marble) does not spontaneously decompose to calcium oxide and carbon dioxide at room temperature — it is stable.

---

## 5. The Four Cases: How ΔH and ΔS Interact

### Understanding Temperature Dependence

The TΔS term in the Gibbs equation means that temperature plays a crucial role in determining spontaneity. As temperature increases, the TΔS term becomes larger in magnitude. This means that ΔS becomes more important at high temperatures, while ΔH dominates at low temperatures.

There are four possible combinations of ΔH and ΔS:

### Case 1: ΔH negative, ΔS positive (the dream scenario)

ΔG = (negative) − T(positive) = always negative, at all temperatures.
This reaction is **spontaneous at all temperatures**.

Example: The combustion of fuels. Burning methane is exothermic (ΔH negative) and produces more gas molecules than it consumes (ΔS positive). These reactions happen readily once ignited.

### Case 2: ΔH positive, ΔS negative (the nightmare scenario)

ΔG = (positive) − T(negative) = positive + (positive number) = always positive, at all temperatures.
This reaction is **never spontaneous**.

Example: The reverse of combustion — trying to turn CO₂ and H₂O back into methane and oxygen without an input of energy. This will not happen spontaneously at any temperature.

### Case 3: ΔH negative, ΔS negative (spontaneous only at low T)

ΔG = (negative) − T(negative) = negative + T|ΔS|.
At low temperatures, the T|ΔS| term is small, so the negative ΔH dominates, and ΔG is negative (spontaneous). At high temperatures, T|ΔS| becomes larger than |ΔH|, and ΔG becomes positive (non-spontaneous).

Example: The Haber process: N₂(g) + 3H₂(g) → 2NH₃(g). ΔH = −92 kJ mol⁻¹, ΔS = −199 J K⁻¹ mol⁻¹. This reaction is spontaneous at low temperatures but becomes non-spontaneous above a certain threshold.

### Case 4: ΔH positive, ΔS positive (spontaneous only at high T)

ΔG = (positive) − T(positive).
At low temperatures, the positive ΔH dominates, so ΔG is positive (non-spontaneous). At high temperatures, TΔS exceeds ΔH, making ΔG negative (spontaneous).

Example: The thermal decomposition of CaCO₃(s) → CaO(s) + CO₂(g). ΔH = +178 kJ mol⁻¹, ΔS = +161 J K⁻¹ mol⁻¹. This reaction requires high temperature to become spontaneous — which is why limestone is heated in a kiln to make quicklime.

### Finding the Threshold Temperature

For Cases 3 and 4, there is a temperature at which the reaction switches from spontaneous to non-spontaneous (or vice versa). At this threshold, ΔG = 0.

Setting ΔG = 0 in the Gibbs equation:

0 = ΔH − TΔS
T = ΔH / ΔS

This formula gives the temperature (in kelvin) at which ΔG changes sign. **You must use consistent units** — both ΔH and ΔS must be in joules, or both in kilojoules.

### Worked Example 5: Finding the Threshold Temperature

**Problem:** For the Haber process, N₂(g) + 3H₂(g) → 2NH₃(g), ΔH = −92 kJ mol⁻¹ and ΔS = −199 J K⁻¹ mol⁻¹. Above what temperature does this reaction become non-spontaneous?

**Strategy:** Both ΔH and ΔS are negative, so this is Case 3 (spontaneous at low T). The threshold is found from T = ΔH/ΔS. We must use consistent units.

**Calculation:**
Convert ΔH to J: −92 kJ mol⁻¹ = −92,000 J mol⁻¹.
T = ΔH/ΔS = −92,000 / (−199) = 462 K.

Below 462 K (approximately 189°C), ΔG is negative and the reaction is spontaneous. Above 462 K, ΔG becomes positive and the reaction is no longer spontaneous.

**Why this makes sense:** The Haber process is actually run at about 700 K in industry. At 700 K, ΔG is positive, which seems contradictory. The reason is that the reaction is run at high temperature not because it is thermodynamically ideal, but because the rate is far too slow at low temperatures. A catalyst is used, and the high temperature is a compromise: it sacrifices some thermodynamic favorability to gain a practical reaction rate. The ammonia is continuously removed, which shifts the equilibrium and helps compensate.

### Worked Example 6: Decomposition Temperature

**Problem:** Sodium hydrogen carbonate (baking soda) decomposes when heated: 2NaHCO₃(s) → Na₂CO₃(s) + H₂O(g) + CO₂(g). For this reaction, ΔH⦵ = +135 kJ mol⁻¹ and ΔS⦵ = +335 J K⁻¹ mol⁻¹. Calculate the minimum temperature at which this reaction becomes spontaneous.

**Strategy:** ΔH positive, ΔS positive → Case 4. The reaction becomes spontaneous when T exceeds ΔH/ΔS.

**Calculation:**
Convert ΔH to J: +135 kJ mol⁻¹ = +135,000 J mol⁻¹.
T = ΔH/ΔS = 135,000 / 335 = 403 K.

Above 403 K (approximately 130°C), ΔG is negative and the decomposition is spontaneous. Below 403 K, ΔG is positive and baking soda is stable.

**Why this makes sense:** This is precisely why baking powder (which contains sodium hydrogen carbonate) causes cakes to rise in a hot oven (typically 175–200°C = 448–473 K). At oven temperature, the decomposition becomes spontaneous, releasing CO₂ gas that creates the bubbles that make the cake light and fluffy. At room temperature (298 K), ΔG is positive and the baking powder does not decompose — which is why it can sit in your cupboard without reacting.

---

## Practice Problems

1. Predict the sign of ΔS (positive or negative) for each of the following reactions and give a one-sentence reason for each prediction:
   (a) 2SO₂(g) + O₂(g) → 2SO₃(g)
   (b) H₂O(l) → H₂O(g)
   (c) Mg(s) + 2HCl(aq) → MgCl₂(aq) + H₂(g)
   (d) 2Na(s) + Cl₂(g) → 2NaCl(s)

2. Calculate the standard entropy change, ΔS⦵, for the reaction: 2NO₂(g) → N₂O₄(g). The standard entropy values are S⦵[NO₂(g)] = 240 J K⁻¹ mol⁻¹ and S⦵[N₂O₄(g)] = 304 J K⁻¹ mol⁻¹.

3. For the reaction 2NO₂(g) → N₂O₄(g), the standard enthalpy change is ΔH⦵ = −57 kJ mol⁻¹. Use your answer from Problem 2 to calculate ΔG⦵ at 298 K. State whether the reaction is spontaneous at this temperature.

4. A certain reaction has ΔH⦵ = +45 kJ mol⁻¹ and ΔS⦵ = +150 J K⁻¹ mol⁻¹. Calculate the temperature above which this reaction becomes spontaneous. Explain which of the four cases this reaction belongs to and why.

5. **(IB-exam style)** The contact process is used to manufacture sulfuric acid. One of the key steps is the oxidation of sulfur dioxide: 2SO₂(g) + O₂(g) → 2SO₃(g). Thermodynamic data for this reaction at 298 K are provided below:
   - ΔH⦵ = −197 kJ mol⁻¹
   - S⦵[SO₂(g)] = 248 J K⁻¹ mol⁻¹
   - S⦵[O₂(g)] = 205 J K⁻¹ mol⁻¹
   - S⦵[SO₃(g)] = 257 J K⁻¹ mol⁻¹
   (a) Calculate the standard entropy change, ΔS⦵, for this reaction. Show your working.
   (b) Calculate ΔG⦵ for this reaction at 298 K and state whether the reaction is spontaneous at this temperature.
   (c) Calculate ΔG⦵ at 800 K, which is a typical operating temperature for the contact process. You may assume that ΔH⦵ and ΔS⦵ do not change significantly with temperature.
   (d) Although the reaction is thermodynamically feasible at 298 K, in practice the contact process is operated at approximately 700–800 K. Suggest a reason for this, based on your knowledge of chemical kinetics and the role of the vanadium(V) oxide catalyst used in this process.

---

## Answers

1. **(a)** ΔS is negative. The reaction converts 3 moles of gas (2SO₂ + O₂) into 2 moles of gas (2SO₃), so there are fewer gas particles and therefore less disorder.

   **(b)** ΔS is positive. Water changing from liquid to gas represents a transition to a state with far more molecular disorder — gas molecules move freely and occupy much more space than liquid molecules.

   **(c)** ΔS is positive. Although a solid magnesium is consumed, hydrogen gas is produced from aqueous H⁺ ions. The production of a gas (H₂) from species in solution represents a significant increase in disorder.

   **(d)** ΔS is negative. Two moles of gas (Cl₂) and a solid metal react to form only a solid ionic compound. The loss of all gas molecules and the formation of a highly ordered crystal lattice means entropy decreases substantially.

2. ΣS⦵(products) = 1 × 304 = 304 J K⁻¹.
   ΣS⦵(reactants) = 2 × 240 = 480 J K⁻¹.
   ΔS⦵ = 304 − 480 = −176 J K⁻¹ mol⁻¹.

   The negative value is expected because two gas molecules combine to form one gas molecule. Fewer particles means fewer possible arrangements.

3. First convert ΔH to joules: ΔH⦵ = −57 kJ mol⁻¹ = −57,000 J mol⁻¹.
   ΔS⦵ = −176 J K⁻¹ mol⁻¹ (from Problem 2).
   T = 298 K.
   TΔS⦵ = 298 × (−176) = −52,448 J mol⁻¹.

   ΔG⦵ = ΔH⦵ − TΔS⦵ = −57,000 − (−52,448) = −57,000 + 52,448 = −4,552 J mol⁻¹ = −4.55 kJ mol⁻¹.

   ΔG⦵ is negative, so the dimerization of NO₂ to N₂O₄ is **spontaneous** at 298 K. This is Case 3: both ΔH and ΔS are negative. The favorable (exothermic) enthalpy change dominates over the unfavorable (negative) entropy change at room temperature. This is consistent with the observation that NO₂ gas (brown) spontaneously dimerizes to N₂O₄ (colorless) at low temperatures, while at higher temperatures the equilibrium shifts back toward NO₂.

   **Common mistake:** When ΔS is negative, TΔS is also negative. Subtracting a negative is the same as adding a positive: ΔH − (−T|ΔS|) = ΔH + T|ΔS|. Students who incorrectly write ΔG = ΔH − TΔS as −57,000 − 298(−176) and get −57,000 − 52,448 = −109,448 J are making a sign error. The correct evaluation is −57,000 − (−52,448) = −57,000 + 52,448 = −4,552 J.

4. ΔH positive and ΔS positive → this reaction belongs to **Case 4**: spontaneous only at high temperatures.

   To find the threshold temperature, convert ΔH to joules: ΔH = +45 kJ mol⁻¹ = +45,000 J mol⁻¹.

   T = ΔH/ΔS = 45,000 / 150 = 300 K.

   The reaction becomes spontaneous above 300 K (approximately 27°C). Below 300 K, ΔG is positive and the reaction is non-spontaneous. At exactly 300 K, ΔG = 0 and the reaction is at equilibrium. Above 300 K, the TΔS term (300 K × 150 J K⁻¹ = 45,000 J) exceeds the positive ΔH, making ΔG negative.

   **Why this makes sense:** At low temperatures, the unfavorable enthalpy term (+45 kJ mol⁻¹) dominates because the TΔS term is small. As temperature increases, the favorable entropy term (TΔS) grows and eventually overtakes the enthalpy term. This is a general pattern for Case 4 reactions: they require sufficient thermal energy for the favorable entropy change to overcome the unfavorable enthalpy change.

5. **(a)** ΔS⦵ = ΣS⦵(products) − ΣS⦵(reactants).
   ΣS⦵(products) = 2 × 257 = 514 J K⁻¹.
   ΣS⦵(reactants) = 2 × 248 + 1 × 205 = 496 + 205 = 701 J K⁻¹.
   ΔS⦵ = 514 − 701 = −187 J K⁻¹ mol⁻¹.

   **(b)** At 298 K:
   ΔH⦵ = −197 kJ mol⁻¹ = −197,000 J mol⁻¹.
   TΔS⦵ = 298 × (−187) = −55,726 J mol⁻¹.
   ΔG⦵ = −197,000 − (−55,726) = −197,000 + 55,726 = −141,274 J mol⁻¹ = −141 kJ mol⁻¹.

   ΔG⦵ is negative, so the reaction is **spontaneous** at 298 K.

   **(c)** At 800 K:
   TΔS⦵ = 800 × (−187) = −149,600 J mol⁻¹.
   ΔG⦵ = −197,000 − (−149,600) = −197,000 + 149,600 = −47,400 J mol⁻¹ = −47.4 kJ mol⁻¹.

   ΔG⦵ is still negative at 800 K, so the reaction remains thermodynamically spontaneous at the operating temperature. However, notice that ΔG has become less negative — it has shifted from −141 kJ mol⁻¹ to −47.4 kJ mol⁻¹. This is because the unfavorable TΔS term (negative ΔS multiplied by T) is larger at the higher temperature, partially offsetting the favorable ΔH.

   **(d)** Even though the reaction has a negative ΔG at 298 K, it is extremely slow at that temperature because the activation energy is very high. A vanadium(V) oxide (V₂O₅) catalyst is used to lower the activation energy and provide an alternative pathway. However, the catalyst is only effective at elevated temperatures — typically 700–800 K. At these temperatures, the catalyst is active and the reaction rate is commercially viable. The compromise is that the equilibrium position is less favorable at higher temperatures (as shown by the less negative ΔG at 800 K compared to 298 K), but the gain in reaction rate more than compensates. This is a classic example of the trade-off between thermodynamics (which favors low temperature for this exothermic reaction with negative ΔS) and kinetics (which requires high temperature for the catalyst to work effectively and the reaction to proceed at a practical speed).
