# Lesson 1: Stoichiometry Review — Moles, Formulas, Yield, Gases

## What You'll Learn
- Convert between mass, moles, and number of particles using molar mass and Avogadro's number
- Use balanced chemical equations to determine mole ratios between reactants and products
- Identify the limiting reagent in a reaction and calculate the theoretical yield of product
- Apply the ideal gas equation \(PV = nRT\) to find moles, volume, pressure, or temperature of a gas
- Calculate percentage yield and explain common reasons why yields are below 100%
- Solve back-titration problems by working backwards from the excess reagent

---

## 1. The Mole — Chemistry's Counting Unit

### What the mole is and why it matters

In everyday life, we count eggs by the dozen (12) and paper by the ream (500). In chemistry, we count atoms, molecules, and ions by the **mole**. A mole is simply a specific number of particles. That number, called Avogadro's number, is \(6.02 \times 10^{23}\). This means that one mole of any substance contains \(6.02 \times 10^{23}\) particles — just as one dozen eggs always contains 12 eggs, one mole of carbon atoms always contains \(6.02 \times 10^{23}\) carbon atoms.

We need the mole because individual atoms are far too small to count one by one. A single grain of sand contains roughly \(10^{19}\) atoms — far more than we can meaningfully handle. The mole lets us bridge the gap between the atomic scale (which is invisible to us) and the laboratory scale (where we measure things in grams). When you measure out 12 grams of carbon on a balance, you are holding one mole of carbon atoms in your hand — that is \(6.02 \times 10^{23}\) atoms.

### The key formula connecting mass, moles, and molar mass

The simplest and most important formula in stoichiometry is:

\[
n = \frac{m}{M}
\]

where:
- \(n\) is the amount of substance, measured in moles (abbreviated mol)
- \(m\) is the mass of the substance, measured in grams (g)
- \(M\) is the molar mass, measured in grams per mole (g mol⁻¹)

Molar mass is the mass of one mole of a substance. For an element, the molar mass in grams per mole is numerically equal to the relative atomic mass (Aᵣ) found on the periodic table. For example, carbon has Aᵣ = 12.01, so its molar mass is 12.01 g mol⁻¹. For a compound, you add up the molar masses of all the atoms in the formula. Water, H₂O, has molar mass = (2 × 1.01) + (1 × 16.00) = 18.02 g mol⁻¹.

A common misconception is confusing mass with moles. A student might say "I have more moles of hydrogen than oxygen" when they actually mean "I have more grams of hydrogen." These are entirely different quantities. Always check: are you talking about mass (grams) or amount (moles)?

### Using mole ratios from balanced equations

A balanced chemical equation tells you the ratio in which reactants combine and products form. For the reaction:

\[
\ce{2H2(g) + O2(g) -> 2H2O(l)}
\]

The coefficients (the numbers in front of each formula) tell us that 2 moles of hydrogen gas react with 1 mole of oxygen gas to produce 2 moles of liquid water. The ratio H₂ : O₂ : H₂O is 2 : 1 : 2. This is called the **mole ratio**. The mole ratio is the foundation of every stoichiometry calculation. Once you know how many moles of one substance you have, you can use the ratio to find how many moles of any other substance are involved.

### Worked Example 1: Mass of Product from a Given Mass of Reactant

**Problem:** How many grams of water are produced when 8.0 grams of hydrogen gas burns completely in oxygen?

**Approach:** To solve this, we need to convert the mass of hydrogen to moles, use the mole ratio from the balanced equation to find moles of water, then convert that number of moles back to grams.

**Step 1:** Calculate the number of moles of hydrogen. The molar mass of H₂ is 2.0 g mol⁻¹ (since each H atom has a mass of about 1.0 g mol⁻¹ and there are two H atoms).

\[
n(\ce{H2}) = \frac{m(\ce{H2})}{M(\ce{H2})} = \frac{8.0\text{ g}}{2.0\text{ g mol}^{-1}} = 4.0\text{ mol}
\]

**Step 2:** Use the mole ratio from the balanced equation. The equation \(\ce{2H2 + O2 -> 2H2O}\) shows that H₂ and H₂O are in a 2:2 ratio, which simplifies to 1:1. This means that for every mole of H₂ consumed, one mole of H₂O is produced.

\[
n(\ce{H2O}) = n(\ce{H2}) \times \frac{2}{2} = 4.0 \times 1 = 4.0\text{ mol}
\]

**Step 3:** Convert moles of water to grams. The molar mass of H₂O is 18.0 g mol⁻¹ (2 × 1.0 for the hydrogens plus 16.0 for the oxygen).

\[
m(\ce{H2O}) = n(\ce{H2O}) \times M(\ce{H2O}) = 4.0\text{ mol} \times 18.0\text{ g mol}^{-1} = 72\text{ g}
\]

**Why this makes sense:** The mole ratio is 1:1, and hydrogen gas is much lighter than water (2.0 vs 18.0 g mol⁻¹). So if you start with 8.0 g of H₂ (which is 4.0 mol), you should get 4.0 mol of H₂O, which weighs 4.0 × 18.0 = 72 g. The mass increases because each H₂ molecule picks up an oxygen atom to become H₂O, adding significant mass.

---

## 2. Limiting Reagents — The Reactant That Runs Out First

### What a limiting reagent is and why it matters

In a chemical reaction, one reactant is almost always used up before the others. The reactant that is completely consumed — the one that runs out first — is called the **limiting reagent**. It determines, or limits, how much product can form. Any other reactants are called **excess reagents** — they are present in amounts larger than needed, and some of them will remain unreacted when the reaction stops.

Think of building bicycles. Each bicycle needs 2 wheels and 1 frame. If you have 10 wheels and 4 frames, which limits your production? Even though 10 wheels could make 5 bicycles, you only have 4 frames. The frames are the limiting component — you can build only 4 bicycles. The 10 wheels are in excess; after building 4 bicycles (using 8 wheels), you will have 2 wheels left over. Chemical reactions work the same way: the limiting reagent controls how much product you can make, and the excess reagent is left over.

### How to identify the limiting reagent

Many students assume that the reactant with the smaller mass (or the smaller number of moles) is the limiting reagent. This is incorrect. You must compare the mole ratio required by the balanced equation with the mole ratio you actually have. The correct procedure is:

1. Convert the mass (or volume, or concentration) of every reactant to moles.
2. For each reactant, divide the number of moles by its coefficient in the balanced equation.
3. The reactant that gives the smallest result is the limiting reagent.

### Worked Example 2: Identifying the Limiting Reagent

**Problem:** 8.0 grams of hydrogen gas reacts with 16.0 grams of oxygen gas. Which reactant is the limiting reagent, and what mass of water is produced?

**Approach:** We will convert both masses to moles, divide each by its coefficient, and compare. The smaller value identifies the limiting reagent. Then we use the limiting reagent to calculate the product.

The balanced equation is:

\[
\ce{2H2(g) + O2(g) -> 2H2O(l)}
\]

**Step 1:** Calculate moles of each reactant.

\[
n(\ce{H2}) = \frac{8.0\text{ g}}{2.0\text{ g mol}^{-1}} = 4.0\text{ mol}
\]

\[
n(\ce{O2}) = \frac{16.0\text{ g}}{32.0\text{ g mol}^{-1}} = 0.50\text{ mol}
\]

**Step 2:** Divide each by its coefficient. The coefficient of H₂ is 2, and the coefficient of O₂ is 1.

\[
\frac{n(\ce{H2})}{\text{coefficient}} = \frac{4.0}{2} = 2.0
\]

\[
\frac{n(\ce{O2})}{\text{coefficient}} = \frac{0.50}{1} = 0.50
\]

**Step 3:** Compare. Since 0.50 is smaller than 2.0, oxygen is the limiting reagent. Even though we have more moles of hydrogen (4.0 vs 0.50), the balanced equation requires twice as much H₂ as O₂. Oxygen runs out first and therefore limits the reaction.

**Step 4:** Calculate the product using the limiting reagent. The mole ratio of O₂ to H₂O is 1:2.

\[
n(\ce{H2O}) = n(\ce{O2}) \times \frac{2}{1} = 0.50 \times 2 = 1.0\text{ mol}
\]

\[
m(\ce{H2O}) = 1.0\text{ mol} \times 18.0\text{ g mol}^{-1} = 18\text{ g}
\]

**Why this makes sense:** Even though we had 4.0 mol of H₂ — enough to make 4.0 mol of H₂O — we only had 0.50 mol of O₂. Every 1 mol of O₂ makes 2 mol of H₂O, so 0.50 mol of O₂ can only make 1.0 mol of H₂O. After that, the O₂ is gone, and the reaction stops. The remaining H₂ has nothing to react with.

---

## 3. The Ideal Gas Equation — Connecting Gases to Moles

### What the ideal gas equation is and why we need it

In the previous sections, we measured reactants and products by mass. But gases are hard to weigh. They expand to fill whatever container they are in, and their mass depends on pressure and temperature. Instead of weighing a gas, we usually measure its volume, pressure, and temperature — and then use these measurements to calculate the number of moles.

The relationship between pressure, volume, temperature, and moles for an ideal gas is given by the ideal gas equation:

\[
PV = nRT
\]

Each symbol has a specific meaning and must be used with consistent units:

| Symbol | Meaning | SI Unit | Common alternative |
|--------|---------|---------|-------------------|
| \(P\) | Pressure | pascal (Pa) | kilopascal (kPa) or atmosphere (atm) |
| \(V\) | Volume | cubic metre (m³) | cubic decimetre (dm³) |
| \(n\) | Number of moles | mole (mol) | — |
| \(R\) | Gas constant | 8.31 J K⁻¹ mol⁻¹ | — |
| \(T\) | Temperature | kelvin (K) | — |

**The most critical thing to get right is unit consistency.** When you use R = 8.31 J K⁻¹ mol⁻¹, pressure must be in pascals (Pa) and volume must be in cubic metres (m³). If you prefer to work in kilopascals (kPa) and cubic decimetres (dm³), you can do so because the conversion factors cancel out: 1 m³ = 1000 dm³ and 1 kPa = 1000 Pa. The factor of 1000 appears in both numerator and denominator and cancels.

A helpful reference point: at Standard Temperature and Pressure (STP, which is 273 K and 100 kPa), one mole of any ideal gas occupies 22.7 dm³.

A common mistake is forgetting to convert temperature from degrees Celsius to kelvin. The kelvin scale starts at absolute zero (−273 °C), and all gas law calculations must use kelvin. To convert: K = °C + 273.

### Worked Example 3: Finding Moles from Gas Measurements

**Problem:** A sample of gas occupies a volume of 2.50 dm³ at a temperature of 300 K and a pressure of 100 kPa. Calculate the number of moles of gas in the sample.

**Approach:** We will use the ideal gas equation rearranged to solve for n: \(n = PV / RT\). Since we are given pressure in kPa and volume in dm³, we can use these units directly because the conversion factors cancel.

**Step 1:** Write the rearranged formula.

\[
n = \frac{PV}{RT}
\]

**Step 2:** Substitute the values with units.

\[
n = \frac{100\text{ kPa} \times 2.50\text{ dm}^3}{8.31\text{ J K}^{-1}\text{ mol}^{-1} \times 300\text{ K}}
\]

**Step 3:** Calculate.

\[
n = \frac{250}{2493} = 0.100\text{ mol}
\]

**Why this makes sense:** At STP (273 K, 100 kPa), 1 mol occupies 22.7 dm³. Here the temperature is slightly higher (300 K vs 273 K), so the gas expands a bit. At 300 K, 1 mol would occupy about 22.7 × (300/273) ≈ 25.0 dm³. Our sample is 2.50 dm³, which is one tenth of 25 dm³, so 0.10 mol is exactly what we expect.

---

## 4. Percentage Yield — How Much Product You Actually Get

### What percentage yield is and why it is rarely 100%

The **theoretical yield** is the maximum amount of product that can be formed according to the stoichiometry of the balanced equation — this is what we calculate assuming the reaction goes perfectly. The **actual yield** is the amount of product you actually collect in the laboratory. In almost every real chemical reaction, the actual yield is less than the theoretical yield. The **percentage yield** tells us what fraction of the theoretical maximum we actually obtained:

\[
\text{Percentage yield} = \frac{\text{actual yield}}{\text{theoretical yield}} \times 100\%
\]

There are several common reasons why yields fall below 100%:
- The reaction may not go to completion; some reactants may remain unreacted.
- Side reactions may occur, producing unwanted products instead of the desired one.
- Product may be lost during purification steps such as filtration, crystallisation, or transfer between containers.
- If the product is a liquid, some may evaporate.
- If the reaction is reversible, it may reach equilibrium before all reactants are consumed.

It is also possible (though less common) for the apparent yield to exceed 100%. This is not a genuine yield above 100%; rather, it indicates that the product is impure — it contains other substances (such as water or unreacted starting material) that add to the measured mass.

### Worked Example 4: Calculating Percentage Yield

**Problem:** Using the limiting reagent from Worked Example 2, the theoretical yield of water was 18.0 g. In a real experiment, only 14.4 g of water was collected. Calculate the percentage yield.

**Approach:** We simply divide the actual mass obtained by the theoretical mass and multiply by 100%.

\[
\text{Percentage yield} = \frac{14.4\text{ g}}{18.0\text{ g}} \times 100\% = 80.0\%
\]

**Why this makes sense:** An 80% yield is realistic for many reactions. The missing 20% (3.6 g of water) could have been lost as water vapour that escaped to the atmosphere, or some hydrogen and oxygen may not have fully reacted.

---

## 5. Back-Titrations — Analysing Substances That Cannot Be Titrated Directly

### What a back-titration is and when we use it

A regular titration involves directly adding one solution to another until the reaction is complete. But some substances cannot be titrated directly — for example, they may be insoluble (a solid that does not dissolve), they may react too slowly, or they may be volatile (easily evaporate). In these cases, we use a **back-titration**.

In a back-titration, you add a known excess of a reagent to the sample. "Excess" means you add more than enough to react completely with the sample. After the reaction between the sample and the added reagent goes to completion, some of the added reagent is left over (unreacted). You then titrate this leftover reagent with a second standard solution. By finding out how much of the added reagent remains, you can calculate how much reacted with your sample — and from that, how much of your sample was present.

The procedure can be summarised as:

1. Add a known number of moles of reagent A (in excess) to your unknown sample.
2. Allow the reaction between the sample and reagent A to go to completion.
3. Titrate the remaining, unreacted reagent A with a standard solution of reagent B.
4. Calculate: moles of A that reacted with the sample = initial moles of A − moles of A remaining.
5. Use the stoichiometry of the reaction between the sample and A to find the moles of your unknown.

### Worked Example 5: Back-Titration for Purity Analysis

**Problem:** A 0.500 g sample of impure calcium carbonate (CaCO₃) is treated with 50.0 cm³ of hydrochloric acid (HCl) with a concentration of 0.200 mol dm⁻³. The acid is in excess — there is more than enough to react with all the CaCO₃. After the reaction is complete, the remaining (unreacted) HCl is titrated against sodium hydroxide (NaOH) with a concentration of 0.100 mol dm⁻³, and 30.0 cm³ of the NaOH solution is required to neutralise it. Calculate the percentage purity of the CaCO₃ sample, meaning the percentage by mass that is actually CaCO₃.

**Approach:** We will calculate the initial moles of HCl added, then the moles of HCl that remained (found from the NaOH titration), subtract to find the moles of HCl that reacted with CaCO₃, use the stoichiometric ratio to find moles of CaCO₃, convert to mass, and finally calculate the percentage purity.

The relevant balanced equations are:

\[
\ce{CaCO3(s) + 2HCl(aq) -> CaCl2(aq) + CO2(g) + H2O(l)}
\]

\[
\ce{HCl(aq) + NaOH(aq) -> NaCl(aq) + H2O(l)}
\]

**Step 1:** Calculate the initial number of moles of HCl added to the sample.

\[
n(\ce{HCl})_{\text{initial}} = c \times V = 0.200\text{ mol dm}^{-3} \times 0.0500\text{ dm}^3 = 0.0100\text{ mol}
\]

(Note: 50.0 cm³ was converted to dm³ by dividing by 1000, giving 0.0500 dm³.)

**Step 2:** Calculate the number of moles of NaOH used in the titration. This equals the number of moles of HCl that remained unreacted, because HCl and NaOH react in a 1:1 ratio.

\[
n(\ce{NaOH}) = 0.100\text{ mol dm}^{-3} \times 0.0300\text{ dm}^3 = 0.00300\text{ mol}
\]

\[
n(\ce{HCl})_{\text{remaining}} = n(\ce{NaOH}) = 0.00300\text{ mol}
\]

**Step 3:** Find the number of moles of HCl that actually reacted with the CaCO₃.

\[
n(\ce{HCl})_{\text{reacted}} = n(\ce{HCl})_{\text{initial}} - n(\ce{HCl})_{\text{remaining}} = 0.0100 - 0.00300 = 0.00700\text{ mol}
\]

**Step 4:** Use the stoichiometric ratio to find moles of CaCO₃. The balanced equation shows that 2 moles of HCl react with 1 mole of CaCO₃, so the number of moles of CaCO₃ is half the number of moles of HCl that reacted.

\[
n(\ce{CaCO3}) = \frac{n(\ce{HCl})_{\text{reacted}}}{2} = \frac{0.00700}{2} = 0.00350\text{ mol}
\]

**Step 5:** Convert moles of CaCO₃ to mass. The molar mass of CaCO₃ is approximately 100 g mol⁻¹ (Ca = 40, C = 12, O₃ = 3 × 16 = 48; total = 100).

\[
m(\ce{CaCO3}) = n \times M = 0.00350\text{ mol} \times 100\text{ g mol}^{-1} = 0.350\text{ g}
\]

**Step 6:** Calculate the percentage purity. This is the mass of pure CaCO₃ divided by the total mass of the impure sample, multiplied by 100.

\[
\text{Purity} = \frac{0.350\text{ g}}{0.500\text{ g}} \times 100\% = 70.0\%
\]

**Why this makes sense:** The sample was impure — only 0.350 g out of 0.500 g was actually CaCO₃. The rest (0.150 g, or 30%) was some other material that did not react with the acid. A purity of 70% is reasonable for an impure mineral sample. Notice also that if we had done a regular forward titration, the insoluble impurities would have interfered. The back-titration cleverly sidesteps this problem by measuring what is left over rather than what reacted directly.

---

## Practice Problems

**Problem 1:** A student burns 4.0 grams of methane gas (CH₄) in 16.0 grams of oxygen gas (O₂). The balanced equation for the reaction is \(\ce{CH4(g) + 2O2(g) -> CO2(g) + 2H2O(l)}\). (a) Determine which reactant is the limiting reagent. (b) Calculate the mass of carbon dioxide (CO₂) that can be produced. (c) State how many grams of the excess reagent remain unreacted after the reaction is complete.

**Problem 2:** A sealed container holds an unknown gas at a pressure of 200 kPa, a temperature of 400 K, and a volume of 5.0 dm³. (a) Calculate the number of moles of gas in the container using the ideal gas equation \(PV = nRT\), where R = 8.31 J K⁻¹ mol⁻¹. (b) If the molar mass of the gas is 44.0 g mol⁻¹, calculate the mass of gas in the container.

**Problem 3:** Nitrogen gas reacts with hydrogen gas to form ammonia according to the equation \(\ce{N2(g) + 3H2(g) -> 2NH3(g)}\). A chemist starts with 28.0 grams of nitrogen gas and an excess of hydrogen gas, and collects 25.5 grams of ammonia. Calculate the percentage yield of ammonia.

**Problem 4:** A 1.00 gram sample of impure magnesium hydroxide, Mg(OH)₂, is reacted with 40.0 cm³ of hydrochloric acid with concentration 1.00 mol dm⁻³. The acid is in excess. After the reaction is complete, the remaining HCl is titrated against sodium hydroxide solution with concentration 0.500 mol dm⁻³, and 15.0 cm³ of the NaOH is required. The balanced equation for the reaction between Mg(OH)₂ and HCl is \(\ce{Mg(OH)2(s) + 2HCl(aq) -> MgCl2(aq) + 2H2O(l)}\). Calculate the percentage purity of the Mg(OH)₂ sample. The molar mass of Mg(OH)₂ is 58.3 g mol⁻¹.

**Problem 5 (IB-Style):** A student heats a 2.50 g sample of an unknown Group 2 metal carbonate, with the formula MCO₃, causing it to decompose. The decomposition reaction is \(\ce{MCO3(s) -> MO(s) + CO2(g)}\). The carbon dioxide gas produced is collected over water at a temperature of 300 K and a pressure of 100 kPa, and it occupies a volume of 0.615 dm³. (a) Calculate the number of moles of CO₂ gas produced, using the ideal gas equation with R = 8.31 J K⁻¹ mol⁻¹. (b) Assuming the decomposition went to completion, determine the number of moles of MCO₃ that decomposed. Hence calculate the molar mass of MCO₃. (c) By subtracting the mass of the carbonate group (CO₃²⁻ has a mass of 60.0 g mol⁻¹) from the molar mass of MCO₃, determine the relative atomic mass of the metal M and identify the metal. (d) In a second trial, the student only collects 0.492 dm³ of CO₂. Calculate the percentage yield of this second trial.

---

## Answers

**Answer 1:** (a) The balanced equation is \(\ce{CH4 + 2O2 -> CO2 + 2H2O}\).

First, calculate moles: \(n(\ce{CH4}) = 4.0 / 16.0 = 0.25\text{ mol}\). \(n(\ce{O2}) = 16.0 / 32.0 = 0.50\text{ mol}\).

Now divide each by its coefficient: CH₄: 0.25 / 1 = 0.25. O₂: 0.50 / 2 = 0.25. Both values are equal. This means neither reactant is in excess — both are exactly limiting. Both will be completely consumed.

(b) The mole ratio between CH₄ and CO₂ is 1:1, so \(n(\ce{CO2}) = 0.25\text{ mol}\). The molar mass of CO₂ is 44.0 g mol⁻¹ (12 + 2 × 16). Mass of CO₂ = 0.25 × 44.0 = 11.0 g.

(c) Since both reactants are exactly consumed, the mass of excess reagent remaining is 0 g. This is unusual; in most real reactions, one reactant is in excess.

---

**Answer 2:** (a) Using \(n = PV / RT\):

\[
n = \frac{200\text{ kPa} \times 5.0\text{ dm}^3}{8.31\text{ J K}^{-1}\text{ mol}^{-1} \times 400\text{ K}} = \frac{1000}{3324} = 0.30\text{ mol}
\]

(If you convert to SI units first: P = 2.00 × 10⁵ Pa, V = 5.0 × 10⁻³ m³, then n = (2.00 × 10⁵ × 5.0 × 10⁻³) / (8.31 × 400) = 1000 / 3324 = 0.30 mol. Both methods give the same answer.)

(b) Mass = n × M = 0.30 mol × 44.0 g mol⁻¹ = 13.2 g (or approximately 13 g to two significant figures).

---

**Answer 3:** First, calculate the theoretical yield. Moles of N₂: \(n(\ce{N2}) = 28.0 / 28.0 = 1.00\text{ mol}\). The mole ratio N₂ : NH₃ is 1 : 2, so theoretical moles of NH₃ = 2.00 mol. Molar mass of NH₃ = 14.0 + (3 × 1.0) = 17.0 g mol⁻¹. Theoretical mass = 2.00 × 17.0 = 34.0 g.

Percentage yield = (actual / theoretical) × 100% = (25.5 / 34.0) × 100% = 75.0%.

---

**Answer 4:** Step 1: Initial moles of HCl = 1.00 mol dm⁻³ × 0.0400 dm³ = 0.0400 mol.

Step 2: Moles of NaOH used = 0.500 mol dm⁻³ × 0.0150 dm³ = 0.00750 mol. Since HCl and NaOH react 1:1, this is also the moles of HCl remaining.

Step 3: Moles of HCl that reacted with Mg(OH)₂ = 0.0400 − 0.00750 = 0.0325 mol.

Step 4: From the balanced equation, 2 mol HCl react with 1 mol Mg(OH)₂, so moles of Mg(OH)₂ = 0.0325 / 2 = 0.01625 mol.

Step 5: Mass of pure Mg(OH)₂ = 0.01625 mol × 58.3 g mol⁻¹ = 0.947 g.

Step 6: Percentage purity = (0.947 / 1.00) × 100% = 94.7%.

---

**Answer 5:** (a) Using the ideal gas equation:

\[
n(\ce{CO2}) = \frac{PV}{RT} = \frac{100\text{ kPa} \times 0.615\text{ dm}^3}{8.31\text{ J K}^{-1}\text{ mol}^{-1} \times 300\text{ K}} = \frac{61.5}{2493} = 0.0247\text{ mol}
\]

(b) From the balanced equation, MCO₃ and CO₂ are in a 1:1 mole ratio, so \(n(\ce{MCO3}) = 0.0247\text{ mol}\). The molar mass of MCO₃ is mass / moles = 2.50 g / 0.0247 mol = 101 g mol⁻¹.

(c) The carbonate group CO₃²⁻ has a mass of 60.0 g mol⁻¹. Therefore, the relative atomic mass of M = 101 − 60 = 41. Looking at the periodic table, the Group 2 metal with relative atomic mass closest to 41 is calcium (Ca), which has Aᵣ = 40.1. The slight difference (41 vs 40.1) comes from rounding in the calculation. Using more precise values would give a result closer to 40.1. The metal is calcium.

(d) First, calculate the actual moles of CO₂ collected in the second trial:

\[
n(\ce{CO2})_{\text{actual}} = \frac{100 \times 0.492}{8.31 \times 300} = \frac{49.2}{2493} = 0.0197\text{ mol}
\]

Percentage yield = (actual moles / theoretical moles) × 100% = (0.0197 / 0.0247) × 100% = 79.8%.

The lower yield could be due to incomplete decomposition of the carbonate or loss of CO₂ gas during collection.
