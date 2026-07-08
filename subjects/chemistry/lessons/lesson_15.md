# Lesson 15: Hess's Law — Enthalpy Cycles, ΔH_f⦵ and ΔH_c⦵ Methods

## What You'll Learn
- State Hess's Law and explain what it means for enthalpy to be a state function
- Calculate ΔH for a reaction using standard enthalpies of formation (the ΔH_f⦵ method)
- Calculate ΔH for a reaction using standard enthalpies of combustion (the ΔH_c⦵ method)
- Manipulate given chemical equations — flipping, multiplying, and adding — to find an unknown ΔH
- Construct enthalpy cycle diagrams to visualize and solve multi-step problems

---

## 1. Hess's Law: Why the Path Does Not Matter

### What Does Hess's Law Say?

Hess's Law states that the enthalpy change for a chemical reaction is the same regardless of whether the reaction happens in one step or in a series of steps, as long as the starting materials (the initial state) and the final products (the final state) are the same in every case.

This can be written more formally: **ΔH for a reaction depends only on the initial and final states, not on the route taken between them.**

### What Does "Route" Mean?

Imagine you want to travel from New York to Los Angeles. You could fly directly. Or you could fly from New York to Chicago, then from Chicago to Denver, then from Denver to Los Angeles. The distance you travel is different in each case, but you start in New York and end in Los Angeles either way.

In chemistry, the "route" is the sequence of reaction steps. The overall enthalpy change ΔH is like the straight-line distance between the starting point and the ending point — it does not depend on how you got there. The individual ΔH values for each step add up to the same total no matter which steps you choose.

### Why Is This Useful?

Some reactions are impossible to measure directly in a calorimeter. For example, you cannot simply put carbon and hydrogen in a calorimeter and measure the enthalpy of formation of ethane directly — the reaction between C(s) and H₂(g) does not happen in a simple, clean way. But if you can find a route from carbon and hydrogen to ethane using reactions whose ΔH values are known, you can calculate the desired ΔH without ever measuring it.

### Enthalpy Is a State Function

The phrase "state function" means a quantity whose value depends only on the current state of the system, not on how the system got there. Your altitude above sea level is a state function — if you climb a mountain, your final altitude depends only on where you are standing, not on whether you took the steep route or the gentle route. Enthalpy is a state function in exactly the same way.

### Common Misconception

Some students think Hess's Law is a special rule that only applies in certain circumstances. But Hess's Law is simply a consequence of the First Law of Thermodynamics (energy is conserved) and the fact that enthalpy is a state function. It always applies. There are no exceptions.

---

## 2. Method 1: Calculating ΔH Using Standard Enthalpies of Formation (ΔH_f⦵)

### The Logic of the Formation Method

Imagine you have a reaction: Reactants → Products. One way to go from reactants to products is directly. Another way is to first "un-form" all the reactants — break them down into their constituent elements — and then "form" the products from those same elements.

Un-forming a compound is the reverse of its formation reaction, so the enthalpy change is the negative of ΔH_f⦵. Forming a product from elements has an enthalpy change equal to ΔH_f⦵ of that product.

Since both routes must have the same total ΔH (Hess's Law), we can write:

**ΔH_reaction = ΣΔH_f⦵(products) − ΣΔH_f⦵(reactants)**

The symbol Σ (capital Greek letter sigma) means "the sum of." You take each product's ΔH_f⦵, multiply it by the number of moles of that product in the balanced equation (its coefficient), and add them all up. Then you do the same for the reactants. Then you subtract the reactants sum from the products sum.

### Why This Formula Has a Minus Sign

The minus sign appears because the formation enthalpies of reactants are being "reversed" in the enthalpy cycle. Going from reactants to elements is the opposite of forming the reactants from elements, so we subtract instead of adding.

### What to Do with Elements in the Equation

If a reactant or product is an element in its standard state, its ΔH_f⦵ is zero. This is the rule we learned in Lesson 14. For example, in the combustion of methane:

CH₄(g) + 2O₂(g) → CO₂(g) + 2H₂O(l)

O₂(g) is an element, so ΔH_f⦵[O₂(g)] = 0. CH₄ is a compound, so its ΔH_f⦵ is not zero. CO₂ and H₂O are compounds, so their ΔH_f⦵ values are not zero.

### Worked Example 1: Combustion of Methane

**Problem:** Calculate the standard enthalpy change for the complete combustion of methane: CH₄(g) + 2O₂(g) → CO₂(g) + 2H₂O(l). Use the following standard enthalpies of formation:
- ΔH_f⦵[CH₄(g)] = −75 kJ mol⁻¹
- ΔH_f⦵[CO₂(g)] = −394 kJ mol⁻¹
- ΔH_f⦵[H₂O(l)] = −286 kJ mol⁻¹

**Strategy:** We apply the formula ΔH = ΣΔH_f⦵(products) − ΣΔH_f⦵(reactants). For each substance, we multiply its ΔH_f⦵ by its coefficient from the balanced equation. O₂ is an element so its ΔH_f⦵ is zero.

**Step 1 — Sum of ΔH_f⦵ for products:**
The products are CO₂(g) with coefficient 1, and H₂O(l) with coefficient 2.
ΣΔH_f⦵(products) = 1 × (−394) + 2 × (−286)
= −394 + (−572)
= −966 kJ mol⁻¹.

**Step 2 — Sum of ΔH_f⦵ for reactants:**
The reactants are CH₄(g) with coefficient 1, and O₂(g) with coefficient 2.
ΣΔH_f⦵(reactants) = 1 × (−75) + 2 × (0)
= −75 + 0
= −75 kJ mol⁻¹.

**Step 3 — Calculate ΔH:**
ΔH = ΣΔH_f⦵(products) − ΣΔH_f⦵(reactants)
= −966 − (−75)
= −966 + 75
= −891 kJ mol⁻¹.

**Why this makes sense:** Combustion of methane is known to be highly exothermic, releasing a large amount of energy. A value of −891 kJ mol⁻¹ confirms this. The negative sign is correct.

### Worked Example 2: Formation Method with More Complex Stoichiometry

**Problem:** Calculate ΔH for the reaction: 2Al(s) + Fe₂O₃(s) → Al₂O₃(s) + 2Fe(s). The standard enthalpies of formation are:
- ΔH_f⦵[Fe₂O₃(s)] = −824 kJ mol⁻¹
- ΔH_f⦵[Al₂O₃(s)] = −1676 kJ mol⁻¹

**Strategy:** Both Al(s) and Fe(s) are elements in their standard states, so their ΔH_f⦵ values are zero. We only need to consider the two compounds.

**Step 1 — Products:**
ΣΔH_f⦵(products) = 1 × (−1676) + 2 × (0) = −1676 kJ mol⁻¹.

**Step 2 — Reactants:**
ΣΔH_f⦵(reactants) = 2 × (0) + 1 × (−824) = −824 kJ mol⁻¹.

**Step 3 — Calculate ΔH:**
ΔH = −1676 − (−824) = −1676 + 824 = −852 kJ mol⁻¹.

**Why this makes sense:** This is the thermite reaction, famous for being extremely exothermic — hot enough to melt iron. The large negative ΔH confirms this.

---

## 3. Method 2: Calculating ΔH Using Standard Enthalpies of Combustion (ΔH_c⦵)

### The Logic of the Combustion Method

The formation method uses the idea of going "down to elements" and back up. The combustion method uses the idea of going "up to combustion products" (CO₂, H₂O, etc.) and back.

Imagine that both the reactants and the products can be burned in oxygen to produce the same set of combustion products (CO₂, H₂O, SO₂, etc.). One route from reactants to products is direct. Another route is: burn the reactants to their combustion products, and then "un-burn" those combustion products to form the reaction products.

Un-burning is the reverse of combustion, so the enthalpy change is the negative of ΔH_c⦵. This leads to a formula that is similar to the formation formula but with the order reversed:

**ΔH_reaction = ΣΔH_c⦵(reactants) − ΣΔH_c⦵(products)**

Notice carefully: for the combustion method, we subtract the PRODUCTS from the REACTANTS. This is the opposite of the formation method. Many students get the sign wrong by using the formation formula when they should be using the combustion formula. If you always remember "combustion = reactants minus products," you will avoid this error.

### When Is the Combustion Method Used?

The combustion method is most useful for reactions involving organic compounds (hydrocarbons, alcohols, carboxylic acids, etc.), because the enthalpies of combustion of organic compounds are easy to measure experimentally and are widely tabulated. Enthalpies of formation for organic compounds are sometimes harder to find.

Also, if you are given ΔH_c⦵ values for all the species in a reaction, use the combustion method. If you are given ΔH_f⦵ values, use the formation method. Mixing methods within one calculation is a recipe for errors.

### What about Water?

The ΔH_c⦵ of H₂O(l) is zero, because water is already a combustion product — it cannot be burned further. Similarly, the ΔH_c⦵ of CO₂(g) is zero. This makes sense: you cannot burn ash.

### Worked Example 3: Hydrogenation of Ethene

**Problem:** Calculate the enthalpy change for the hydrogenation of ethene: C₂H₄(g) + H₂(g) → C₂H₆(g). Use the following standard enthalpies of combustion:
- ΔH_c⦵[C₂H₄(g)] = −1411 kJ mol⁻¹
- ΔH_c⦵[H₂(g)] = −286 kJ mol⁻¹
- ΔH_c⦵[C₂H₆(g)] = −1560 kJ mol⁻¹

**Strategy:** We use the combustion formula: ΔH = ΣΔH_c⦵(reactants) − ΣΔH_c⦵(products).

**Step 1 — Sum of ΔH_c⦵ for reactants:**
ΣΔH_c⦵(reactants) = 1 × (−1411) + 1 × (−286) = −1697 kJ mol⁻¹.

**Step 2 — Sum of ΔH_c⦵ for products:**
ΣΔH_c⦵(products) = 1 × (−1560) = −1560 kJ mol⁻¹.

**Step 3 — Calculate ΔH:**
ΔH = −1697 − (−1560) = −1697 + 1560 = −137 kJ mol⁻¹.

**Why this makes sense:** Hydrogenation reactions (adding H₂ across a double bond) are typically exothermic because a weaker π bond is replaced by a stronger σ bond. The negative ΔH is consistent with this expectation.

### Worked Example 4: Esterification

**Problem:** Calculate ΔH for the esterification reaction: CH₃COOH(l) + C₂H₅OH(l) → CH₃COOC₂H₅(l) + H₂O(l). The standard enthalpies of combustion are:
- ΔH_c⦵[CH₃COOH(l)] = −875 kJ mol⁻¹
- ΔH_c⦵[C₂H₅OH(l)] = −1367 kJ mol⁻¹
- ΔH_c⦵[CH₃COOC₂H₅(l)] = −2250 kJ mol⁻¹
- ΔH_c⦵[H₂O(l)] = 0 kJ mol⁻¹

**Strategy:** Water's ΔH_c⦵ is zero. Apply the combustion formula.

**Step 1 — Reactants:**
ΣΔH_c⦵(reactants) = (−875) + (−1367) = −2242 kJ mol⁻¹.

**Step 2 — Products:**
ΣΔH_c⦵(products) = (−2250) + (0) = −2250 kJ mol⁻¹.

**Step 3 — Calculate ΔH:**
ΔH = −2242 − (−2250) = −2242 + 2250 = +8 kJ mol⁻¹.

**Why this makes sense:** Esterification reactions typically have very small ΔH values, often close to zero. The value of +8 kJ mol⁻¹ means this reaction is very slightly endothermic, which is entirely plausible.

---

## 4. Method 3: Manipulating and Combining Given Equations

### The Puzzle Approach

Sometimes you are given two or three reactions with their ΔH values and asked to find ΔH for a target reaction. The target reaction does not appear directly in the given data, but you can construct it by combining the given reactions — flipping them, multiplying them, and adding them together.

This method is sometimes called the "thermochemical equation method" or the "Hess cycle puzzle method." It is the most direct application of Hess's Law: if you can build the target equation from given equations, the ΔH for the target is the sum of the ΔH values of the equations you combined, with each ΔH adjusted for any flipping or multiplying you did.

### Three Allowed Operations

There are exactly three things you are allowed to do to a thermochemical equation:

**Operation 1: Flip (reverse) an equation.**
If you reverse a reaction, you must change the sign of its ΔH.
Example: If C(s) + O₂(g) → CO₂(g) has ΔH = −394 kJ, then the reverse, CO₂(g) → C(s) + O₂(g), has ΔH = +394 kJ.

**Operation 2: Multiply an equation by a number.**
If you multiply all coefficients in an equation by n, you must multiply ΔH by n as well.
Example: If H₂(g) + ½O₂(g) → H₂O(l) has ΔH = −286 kJ, then multiplying by 2 gives 2H₂(g) + O₂(g) → 2H₂O(l) with ΔH = −572 kJ.

**Operation 3: Add equations together.**
If you write two (or more) equations and add them, the ΔH of the combined equation is the sum of the individual ΔH values. When adding equations, identical species appearing on both the left and right sides cancel out, just like in algebra.

### A Systematic Approach

When faced with a "combine equations" problem, follow these steps every time:

1. Write down the target equation.
2. Look at the first substance in the target equation. Find which given equation contains that substance on the correct side. If it is on the wrong side, flip that equation (and change the sign of its ΔH).
3. If the coefficient of that substance in the given equation does not match the target, multiply the entire equation (and its ΔH) by the appropriate factor.
4. Repeat for the next substance, always making sure substances you do not want in the final equation will cancel when you add everything up.
5. Add all the manipulated equations. Cancel identical species on both sides.
6. Verify that the resulting equation exactly matches the target equation.
7. Add up all the manipulated ΔH values to get the answer.

### Worked Example 5: Iron Extraction

**Problem:** Calculate ΔH for the reaction: Fe₂O₃(s) + 3CO(g) → 2Fe(s) + 3CO₂(g). This is the key reaction in a blast furnace for extracting iron. Use the following data:
- Equation (1): 2Fe(s) + ³⁄₂O₂(g) → Fe₂O₃(s), ΔH = −824 kJ mol⁻¹
- Equation (2): C(s) + ½O₂(g) → CO(g), ΔH = −111 kJ mol⁻¹
- Equation (3): C(s) + O₂(g) → CO₂(g), ΔH = −394 kJ mol⁻¹

**Strategy:** The target equation has Fe₂O₃ as a reactant, but equation (1) has Fe₂O₃ as a product. So we must flip equation (1). The target has CO as a reactant, but equation (2) has CO as a product. So we must flip equation (2). The target has CO₂ as a product, and equation (3) has CO₂ as a product — we keep equation (3) as is. We also need the carbon atoms from equations (2) and (3) to cancel.

**Step 1 — Flip equation (1):**
Fe₂O₃(s) → 2Fe(s) + ³⁄₂O₂(g), ΔH = +824 kJ.

**Step 2 — Flip equation (2) and multiply by 3:**
We need 3CO as a reactant. Equation (2) makes 1CO as a product. Flip it: CO(g) → C(s) + ½O₂(g), ΔH = +111 kJ. Then multiply by 3: 3CO(g) → 3C(s) + ³⁄₂O₂(g), ΔH = 3 × (+111) = +333 kJ.

**Step 3 — Keep equation (3) and multiply by 3:**
We need 3CO₂ as a product. Equation (3) makes 1CO₂. Multiply by 3: 3C(s) + 3O₂(g) → 3CO₂(g), ΔH = 3 × (−394) = −1182 kJ.

**Step 4 — Add all three equations:**

```
   Fe₂O₃(s)       → 2Fe(s) + ³⁄₂O₂(g)         ΔH = +824
   3CO(g)          → 3C(s)  + ³⁄₂O₂(g)         ΔH = +333
   3C(s) + 3O₂(g)  → 3CO₂(g)                   ΔH = −1182
   ─────────────────────────────────────────
   Fe₂O₃(s) + 3CO(g) + 3C(s) + 3O₂(g) → 2Fe(s) + ³⁄₂O₂(g) + ³⁄₂O₂(g) + 3C(s) + 3CO₂(g)
```

Now cancel: 3C(s) appears on both sides, so it cancels. For the oxygen species: on the left we have 3O₂(g); on the right we have ³⁄₂O₂(g) + ³⁄₂O₂(g) = 3O₂(g). These also cancel completely. What remains is exactly: Fe₂O₃(s) + 3CO(g) → 2Fe(s) + 3CO₂(g). This matches the target.

**Step 5 — Sum the ΔH values:**
ΔH = +824 + 333 + (−1182) = −25 kJ mol⁻¹.

**Why this makes sense:** The blast furnace reaction is known to be slightly exothermic. The value of −25 kJ mol⁻¹ is small in magnitude, which is reasonable for a reaction where both reactants and products are relatively stable compounds.

### Worked Example 6: Formation of Hydrazine

**Problem:** Hydrazine, N₂H₄, is used as rocket fuel. Calculate ΔH for the reaction: N₂(g) + 2H₂(g) → N₂H₄(l). This is actually the formation of hydrazine from its elements, so the answer is ΔH_f⦵ of hydrazine. Use:
- Equation (1): N₂H₄(l) + O₂(g) → N₂(g) + 2H₂O(l), ΔH = −622 kJ mol⁻¹
- Equation (2): H₂(g) + ½O₂(g) → H₂O(l), ΔH = −286 kJ mol⁻¹

**Strategy:** The target has N₂H₄ as a product, but equation (1) has N₂H₄ as a reactant. So we flip equation (1). The target has 2H₂ as a reactant, and equation (2) has H₂ as a reactant — we keep equation (2) but multiply by 2. We also need H₂O(l) and O₂(g) to cancel.

**Step 1 — Flip equation (1):**
N₂(g) + 2H₂O(l) → N₂H₄(l) + O₂(g), ΔH = +622 kJ.

**Step 2 — Multiply equation (2) by 2:**
2H₂(g) + O₂(g) → 2H₂O(l), ΔH = 2 × (−286) = −572 kJ.

**Step 3 — Add the equations:**

```
   N₂(g) + 2H₂O(l)   → N₂H₄(l) + O₂(g)    ΔH = +622
   2H₂(g) + O₂(g)     → 2H₂O(l)            ΔH = −572
   ────────────────────────────────────────
   N₂(g) + 2H₂O(l) + 2H₂(g) + O₂(g) → N₂H₄(l) + O₂(g) + 2H₂O(l)
```

Cancel 2H₂O(l) and O₂(g) from both sides. What remains: N₂(g) + 2H₂(g) → N₂H₄(l). This matches the target.

**Step 4 — Sum ΔH:**
ΔH = +622 + (−572) = +50 kJ mol⁻¹.

**Why this makes sense:** Hydrazine has a positive enthalpy of formation, meaning it is thermodynamically unstable relative to its elements. This is precisely why it is useful as a rocket fuel — it stores energy that can be released upon decomposition or combustion.

---

## 5. Enthalpy Cycle Diagrams: A Visual Tool

### What Is an Enthalpy Cycle?

An enthalpy cycle is a diagram that shows different possible routes from reactants to products. These diagrams are especially helpful for avoiding sign errors, because you can write down the two routes and set them equal to each other.

### The Formation Cycle

For a reaction using the formation method, the cycle looks like this:

```
             ΔH (unknown)
Reactants ───────────────→ Products
    │                          │
    │ −ΣΔH_f⦵(reactants)      │ +ΣΔH_f⦵(products)
    │                          │
    └──────────────────────────┘
              Elements
```

Going from Reactants to Elements requires reversing the formation of the reactants, so the enthalpy change is −ΣΔH_f⦵(reactants). Going from Elements to Products is the formation of the products, with enthalpy change +ΣΔH_f⦵(products). By Hess's Law, the direct route (Reactants → Products) must equal the sum of the two-step route:

ΔH = −ΣΔH_f⦵(reactants) + ΣΔH_f⦵(products)
ΔH = ΣΔH_f⦵(products) − ΣΔH_f⦵(reactants)

This is exactly the formula we used in Section 2.

### The Combustion Cycle

For the combustion method, the cycle is:

```
             ΔH (unknown)
Reactants ───────────────→ Products
    │                          │
    │ +ΣΔH_c⦵(reactants)      │ +ΣΔH_c⦵(products)
    │                          │
    └──────────────────────────┘
         Combustion Products
         (CO₂, H₂O, etc.)
```

This time the two-step route goes down: Reactants burn to combustion products (+ΣΔH_c⦵ reactants), then combustion products "un-burn" to form Products (−ΣΔH_c⦵ products). Setting the routes equal:

ΔH = ΣΔH_c⦵(reactants) − ΣΔH_c⦵(products)

### Drawing Cycles in an Exam

A rough sketch of an enthalpy cycle can earn you marks even if your final numerical answer is wrong, because it shows the examiner that you understand the logic. Label each arrow with the chemical change it represents and the ΔH value. Make sure the arrows form a complete loop. The cycle does not need to be beautiful — it needs to be logically correct.

---

## Practice Problems

1. Calculate the standard enthalpy change for the complete combustion of ethanol: C₂H₅OH(l) + 3O₂(g) → 2CO₂(g) + 3H₂O(l). Use the following standard enthalpies of formation: ΔH_f⦵[C₂H₅OH(l)] = −278 kJ mol⁻¹, ΔH_f⦵[CO₂(g)] = −394 kJ mol⁻¹, ΔH_f⦵[H₂O(l)] = −286 kJ mol⁻¹.

2. Calculate the standard enthalpy change for the dimerization of nitrogen dioxide: 2NO₂(g) → N₂O₄(g). Use the following standard enthalpies of formation: ΔH_f⦵[NO₂(g)] = +33 kJ mol⁻¹, ΔH_f⦵[N₂O₄(g)] = +9 kJ mol⁻¹. Explain what the sign of your answer means.

3. Use the combustion method to find ΔH for the reaction: 2C(s, graphite) + 3H₂(g) + ½O₂(g) → C₂H₅OH(l). The relevant standard enthalpies of combustion are: ΔH_c⦵[C(s, graphite)] = −394 kJ mol⁻¹, ΔH_c⦵[H₂(g)] = −286 kJ mol⁻¹, ΔH_c⦵[C₂H₅OH(l)] = −1367 kJ mol⁻¹.

4. The reaction 2NO(g) + O₂(g) → 2NO₂(g) is important in atmospheric chemistry. Use the following data to calculate its ΔH:
   - Equation (a): N₂(g) + O₂(g) → 2NO(g), ΔH = +181 kJ mol⁻¹
   - Equation (b): N₂(g) + 2O₂(g) → 2NO₂(g), ΔH = +67 kJ mol⁻¹

5. **(IB-exam style)** The standard enthalpy of formation of methane, CH₄(g), can be determined indirectly using Hess's Law. A student has the following experimental data:
   - Reaction 1: C(s, graphite) + O₂(g) → CO₂(g), ΔH = −394 kJ mol⁻¹
   - Reaction 2: H₂(g) + ½O₂(g) → H₂O(l), ΔH = −286 kJ mol⁻¹
   - Reaction 3: CH₄(g) + 2O₂(g) → CO₂(g) + 2H₂O(l), ΔH = −891 kJ mol⁻¹
   The target reaction is: C(s, graphite) + 2H₂(g) → CH₄(g).
   (a) By manipulating and combining reactions 1, 2, and 3 as necessary, determine ΔH_f⦵ of methane. Show clearly how you manipulate each equation and calculate the final value.
   (b) Draw a fully labeled enthalpy cycle diagram (formation cycle) that represents your calculation.
   (c) The data book value for ΔH_f⦵[CH₄(g)] is −75 kJ mol⁻¹. A student claims that because this value is negative, methane must be thermodynamically unstable. Explain why this claim is incorrect.

---

## Answers

1. **Step 1 — Products:** ΣΔH_f⦵(products) = 2(−394) + 3(−286) = −788 + (−858) = −1646 kJ mol⁻¹.

   **Step 2 — Reactants:** ΣΔH_f⦵(reactants) = (−278) + 3(0) = −278 kJ mol⁻¹. (O₂ is an element, so its ΔH_f⦵ = 0.)

   **Step 3 — Calculate ΔH:** ΔH = −1646 − (−278) = −1646 + 278 = −1368 kJ mol⁻¹.

   **Why this makes sense:** This is the combustion of ethanol, and the value (−1368) matches the known ΔH_c⦵ of ethanol. The large negative value confirms that alcohols release a great deal of energy when burned.

   **Common mistake:** Forgetting to multiply the ΔH_f⦵ values by the stoichiometric coefficients. The coefficient of H₂O is 3, so you must use 3 × (−286), not just −286.

2. **Step 1 — Products:** ΣΔH_f⦵(products) = 1 × (+9) = +9 kJ mol⁻¹.

   **Step 2 — Reactants:** ΣΔH_f⦵(reactants) = 2 × (+33) = +66 kJ mol⁻¹.

   **Step 3 — Calculate ΔH:** ΔH = +9 − (+66) = −57 kJ mol⁻¹.

   The negative sign tells us that the dimerization (two NO₂ molecules combining to form one N₂O₄ molecule) is exothermic. This means N₂O₄ is more thermodynamically stable than two separate NO₂ molecules under standard conditions.

3. **Step 1 — Reactants:** ΣΔH_c⦵(reactants) = 2(−394) + 3(−286) + ½(0) = −788 + (−858) + 0 = −1646 kJ mol⁻¹. (O₂ has ΔH_c⦵ = 0 because it cannot be burned.)

   **Step 2 — Products:** ΣΔH_c⦵(products) = 1 × (−1367) = −1367 kJ mol⁻¹.

   **Step 3 — Calculate ΔH:** ΔH = −1646 − (−1367) = −1646 + 1367 = −279 kJ mol⁻¹.

   This value should be the negative of the combustion enthalpy of ethanol (since this reaction is the reverse of combustion "from the elements' perspective"), and indeed |−279| ≈ |−278|, the known ΔH_f⦵ of ethanol. The small discrepancy is due to rounding in the given data.

   **Important check:** This problem asks for ΔH, and the target reaction happens to be the formation of ethanol from its elements. So the answer should be ΔH_f⦵ of ethanol. The formation method gave −278 kJ mol⁻¹. The combustion method gives approximately the same value. This cross-check confirms that both methods are consistent.

4. **Strategy:** The target has 2NO as a reactant. Equation (a) has 2NO as a product, so flip equation (a). The target has 2NO₂ as a product. Equation (b) has 2NO₂ as a product, so keep equation (b) as is. N₂ and O₂ should cancel.

   **Step 1 — Flip equation (a):** 2NO(g) → N₂(g) + O₂(g), ΔH = −181 kJ mol⁻¹.

   **Step 2 — Keep equation (b):** N₂(g) + 2O₂(g) → 2NO₂(g), ΔH = +67 kJ mol⁻¹.

   **Step 3 — Add:**
   ```
   2NO(g)           → N₂(g) + O₂(g)      ΔH = −181
   N₂(g) + 2O₂(g)   → 2NO₂(g)            ΔH = +67
   ─────────────────────────────────────
   2NO(g) + N₂(g) + 2O₂(g) → N₂(g) + O₂(g) + 2NO₂(g)
   ```
   Cancel N₂(g). On the left we have 2O₂(g), on the right we have O₂(g). So one O₂(g) remains on the left. The resulting equation: 2NO(g) + O₂(g) → 2NO₂(g). This matches the target.

   **Step 4 — Sum ΔH:** ΔH = −181 + 67 = −114 kJ mol⁻¹.

   **Why this makes sense:** The oxidation of NO to NO₂ is known to be exothermic, which is consistent with the negative ΔH.

5. **(a)** Target: C(s, graphite) + 2H₂(g) → CH₄(g). We need C and 2H₂ on the left and CH₄ on the right.

   Equation (1) has C on the left: keep it. C(s) + O₂(g) → CO₂(g), ΔH = −394.
   Equation (2) has H₂ on the left but only 1H₂: multiply by 2. 2H₂(g) + O₂(g) → 2H₂O(l), ΔH = 2(−286) = −572.
   Equation (3) has CH₄ on the left, but we need CH₄ on the right: flip it. CO₂(g) + 2H₂O(l) → CH₄(g) + 2O₂(g), ΔH = +891.

   Now add:
   ```
   C(s) + O₂(g)               → CO₂(g)           ΔH = −394
   2H₂(g) + O₂(g)             → 2H₂O(l)          ΔH = −572
   CO₂(g) + 2H₂O(l)           → CH₄(g) + 2O₂(g)  ΔH = +891
   ──────────────────────────────────────────────
   C(s) + O₂(g) + 2H₂(g) + O₂(g) + CO₂(g) + 2H₂O(l) → CO₂(g) + 2H₂O(l) + CH₄(g) + 2O₂(g)
   ```
   Cancel CO₂(g), 2H₂O(l). On the left: O₂(g) + O₂(g) = 2O₂(g). On the right: 2O₂(g). Cancel. What remains: C(s) + 2H₂(g) → CH₄(g). This matches the target.

   ΔH = −394 + (−572) + 891 = −75 kJ mol⁻¹. So ΔH_f⦵[CH₄(g)] = −75 kJ mol⁻¹.

   **(b)** The formation cycle for methane has three levels:

   Top level (left): Reactants = C(s) + 2H₂(g)
   Top level (right): Product = CH₄(g)
   Middle level: Elements (the same as the reactants in this case, since the reactants are already elements)
   Bottom level: Combustion products = CO₂(g) + 2H₂O(l)

   Route 1 (direct): C(s) + 2H₂(g) → CH₄(g), ΔH = ? (the unknown).
   Route 2 (via combustion): C(s) + 2H₂(g) + 2O₂(g) → CO₂(g) + 2H₂O(l), then CO₂(g) + 2H₂O(l) → CH₄(g) + 2O₂(g).

   The cycle confirms: ΔH = (−394 − 572) − (−891) = −75 kJ mol⁻¹.

   **(c)** The student's claim is incorrect because a negative ΔH_f⦵ does not indicate instability — in fact, it indicates the opposite. A negative ΔH_f⦵ means that the formation of the compound from its elements releases energy, which means the compound is at a lower energy level than the separate elements. Lower energy corresponds to greater thermodynamic stability. Methane, with ΔH_f⦵ = −75 kJ mol⁻¹, is thermodynamically more stable than separated carbon (graphite) and hydrogen gas. If a compound had a positive ΔH_f⦵ (like hydrazine at +50 kJ mol⁻¹), that would indicate thermodynamic instability relative to its elements.
