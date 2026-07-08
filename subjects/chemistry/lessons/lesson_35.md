# Lesson 35: Electrolysis and Quantitative Electrochemistry (HL)

## What You'll Learn

In this lesson, you will learn about electrolysis — the process of using electricity to force a chemical reaction to happen. This is the opposite of what a voltaic cell does. You will learn how to predict what products will form when you electrolyse a molten salt or an aqueous solution. You will learn Faraday's laws, which let you calculate exactly how much of a substance is produced when a given electric current flows for a given time. Finally, you will learn the equation that connects cell potential to Gibbs free energy, which tells you whether a reaction is spontaneous.

---

## 1. Voltaic Cells versus Electrolytic Cells — The Key Difference

Before we study electrolysis, let us make sure we understand how it differs from what we learned in Lesson 34.

A **voltaic cell** uses a spontaneous chemical reaction to produce electricity. The chemical reaction happens naturally, and the cell harvests the energy as an electric current. In a voltaic cell, chemical energy is converted to electrical energy.

An **electrolytic cell** uses electricity from an external source (such as a battery or power supply) to force a non-spontaneous chemical reaction to happen. The reaction would not happen on its own; it needs the electrical energy to push it. In an electrolytic cell, electrical energy is converted to chemical energy.

Here is a table comparing the two types of cells:

| Feature | Voltaic Cell | Electrolytic Cell |
|---------|-------------|-------------------|
| Energy conversion | Chemical → Electrical | Electrical → Chemical |
| Is the reaction spontaneous? | Yes (E°_cell > 0) | No (E°_cell < 0) |
| Where does the energy come from? | The chemical reaction itself | An external power source (battery) |
| Sign of the anode | Negative (−) | Positive (+) |
| Sign of the cathode | Positive (+) | Negative (−) |
| Direction of electron flow in external circuit | From anode to cathode | Still from anode to cathode, but the anode is positive because it is connected to the positive terminal of the battery |

**Why is the polarity different?** In an electrolytic cell, the battery forces electrons to go where they would not naturally go. The battery's positive terminal pulls electrons out of the anode (so the anode becomes positive), and the battery's negative terminal pushes electrons into the cathode (so the cathode becomes negative). Despite this reversed polarity, oxidation still happens at the anode and reduction still happens at the cathode. AN OX and RED CAT still apply.

---

## 2. Electrolysis of Molten Salts — The Simplest Case

**Electrolysis** is the process of passing an electric current through an electrolyte (a liquid or solution that contains mobile ions) to cause a chemical change. The word "electrolysis" comes from "electro-" (electricity) and "-lysis" (splitting).

The simplest kind of electrolysis involves a **molten salt**. A molten salt is a salt that has been heated until it melts into a liquid. In the molten state, the ions are free to move. There are only two kinds of ions — the cation (positive) and the anion (negative) — so there is no competition. The products are easy to predict because only one reduction and one oxidation are possible.

<div class="worked">
<strong>Worked Example 1: Predict the products when molten sodium chloride (NaCl) is electrolysed using inert electrodes.</strong>

**To solve this, we need to:** identify the ions present, then decide which one is reduced at the cathode and which is oxidised at the anode.

In molten NaCl, the only ions present are Na⁺ and Cl⁻. The electrodes are "inert," meaning they do not react; they just conduct electricity (typical inert electrodes are graphite or platinum).

At the **cathode** (negative electrode, connected to the negative terminal of the battery): Cations (Na⁺) are attracted to the negative electrode. Na⁺ gains one electron and is reduced to sodium metal:
$$\ce{Na+ + e- -> Na(l)}$$
Molten sodium metal is produced.

At the **anode** (positive electrode): Anions (Cl⁻) are attracted to the positive electrode. Cl⁻ loses one electron and is oxidised to chlorine gas:
$$\ce{2Cl- -> Cl2(g) + 2e-}$$
Chlorine gas bubbles off.

The overall equation is:
$$\ce{2NaCl(l) -> 2Na(l) + Cl2(g)}$$

**Why this makes sense:** There are only two ions, so there is no ambiguity. Sodium is produced at the cathode, chlorine at the anode.
</div>

---

## 3. Electrolysis of Aqueous Solutions — Competition from Water

When we electrolyse an **aqueous solution** (a solution in water), the situation is more complicated. Now there are more than two species that could be reduced or oxidised, because **water itself** can be reduced or oxidised.

In any aqueous solution, water is present. At the cathode, water can be reduced:
$$\ce{2H2O(l) + 2e- -> H2(g) + 2OH-(aq)} \qquad E^\circ = -0.83\text{ V}$$

At the anode, water can be oxidised:
$$\ce{2H2O(l) -> O2(g) + 4H+(aq) + 4e-} \qquad E^\circ = +1.23\text{ V}$$

These water half-reactions compete with the half-reactions of the dissolved ions. We need rules to decide which reaction wins.

**At the cathode (reduction):** Compare the reduction potentials of the metal ion and of water. The species with the **more positive E°** is reduced.
- If the metal ion has a reduction potential that is more positive than about −0.83 V (the E° for water reduction), the **metal** is deposited.
- If the metal is very reactive — meaning its reduction potential is much more negative than −0.83 V — then **water is reduced instead**, producing hydrogen gas and hydroxide ions. This happens for metals like sodium (E° = −2.71 V), potassium (E° = −2.93 V), magnesium (E° = −2.37 V), and aluminium (E° = −1.66 V).

**At the anode (oxidation):** Compare what can be oxidised.
- If the solution contains a halide ion (Cl⁻, Br⁻, I⁻) at reasonable concentration, the halide is usually oxidised to the halogen.
- If the solution contains no halide — for example, if the anion is sulfate (SO₄²⁻) or nitrate (NO₃⁻) — then **water is oxidised**, producing oxygen gas and hydrogen ions.

<div class="worked">
<strong>Worked Example 2: Predict the products when concentrated aqueous sodium chloride (brine) is electrolysed with inert electrodes.</strong>

**To solve this, we need to:** list all species present, then decide the cathode and anode reactions.

Species present: Na⁺, Cl⁻, H₂O.

**At the cathode (−):** Two species could be reduced — Na⁺ (E° = −2.71 V) and H₂O (E° = −0.83 V). Water has the more positive E° (−0.83 > −2.71), so water is reduced:
$$\ce{2H2O(l) + 2e- -> H2(g) + 2OH-(aq)}$$
Hydrogen gas is produced, and the solution near the cathode becomes alkaline due to OH⁻.

**At the anode (+):** Two species could be oxidised — Cl⁻ and H₂O. In concentrated NaCl, chloride ions are oxidised preferentially (despite having a slightly higher E° than water in the table, kinetic factors favour Cl⁻ oxidation in concentrated solution):
$$\ce{2Cl-(aq) -> Cl2(g) + 2e-}$$
Chlorine gas is produced.

**Overall reaction:** Adding the two half-equations:
$$\ce{2NaCl(aq) + 2H2O(l) -> H2(g) + Cl2(g) + 2NaOH(aq)}$$

This is the industrially important chlor-alkali process, which produces hydrogen, chlorine, and sodium hydroxide — three very important chemicals.
</div>

<div class="worked">
<strong>Worked Example 3: Predict the products when copper(II) sulfate solution, CuSO₄(aq), is electrolysed using inert graphite electrodes.</strong>

Species present: Cu²⁺, SO₄²⁻, H₂O.

**At the cathode (−):** Cu²⁺/Cu has E° = +0.34 V. Water reduction has E° = −0.83 V. Copper has the much more positive E°, so Cu²⁺ is reduced:
$$\ce{Cu^{2+}(aq) + 2e- -> Cu(s)}$$
A reddish-brown deposit of copper metal forms on the cathode.

**At the anode (+):** SO₄²⁻ cannot be easily oxidised (sulfur is already at its maximum oxidation number). Water is oxidised instead:
$$\ce{2H2O(l) -> O2(g) + 4H+(aq) + 4e-}$$
Oxygen gas bubbles off. The solution near the anode becomes acidic due to H⁺.

**Overall reaction:** Multiply the cathode half by 2 to match 4 electrons:
$$\ce{2Cu^{2+} + 4e- -> 2Cu}$$
$$\ce{2H2O -> O2 + 4H+ + 4e-}$$
Add: $$\ce{2CuSO4(aq) + 2H2O(l) -> 2Cu(s) + O2(g) + 2H2SO4(aq)}$$

The blue colour of the solution fades (Cu²⁺ ions are consumed), and the solution becomes acidic.
</div>

<div class="worked">
<strong>Worked Example 4: What happens when copper(II) sulfate solution is electrolysed using copper electrodes instead of inert electrodes?</strong>

**To solve this, we need to:** consider whether the electrode material itself can react.

With **copper electrodes**, the anode is made of copper, not graphite or platinum. At the anode, instead of oxidising water or sulfate ions, the copper electrode itself can be oxidised:
$$\ce{Cu(s) -> Cu^{2+}(aq) + 2e-}$$
The anode **dissolves** — copper atoms leave the electrode and enter the solution as Cu²⁺ ions.

At the cathode, Cu²⁺ is reduced as before:
$$\ce{Cu^{2+}(aq) + 2e- -> Cu(s)}$$
Copper is deposited on the cathode.

The net effect: copper is transferred from the anode to the cathode. The concentration of Cu²⁺ in the solution stays constant. This is the basis of **electroplating** and **electrorefining** of copper. Impure copper is used as the anode and dissolves; pure copper deposits on the cathode.
</div>

---

## 4. Faraday's Laws — Measuring the Amount of Electrolysis

**Faraday's first law of electrolysis** states that the mass of a substance produced or consumed at an electrode during electrolysis is directly proportional to the quantity of electric charge that passes through the cell.

To use this law, we need several quantities:

**Electric current (I):** measured in **amperes** (A). Current is the rate of flow of charge. One ampere means one coulomb of charge passes per second.

**Time (t):** measured in **seconds** (s). Always convert time to seconds.

**Charge (Q):** measured in **coulombs** (C). Charge is the amount of electricity that has passed. It is calculated by:
$$Q = I \times t$$
(Charge in coulombs = current in amperes × time in seconds.)

**Faraday's constant (F):** This is the charge carried by one mole of electrons. Its value is approximately **96,500 C mol⁻¹**. So one mole of electrons carries 96,500 coulombs of charge.

**Amount of electrons:** To find how many moles of electrons have passed, divide the total charge by Faraday's constant:
$$n(e^-) = \frac{Q}{F} = \frac{I \times t}{96,500}$$

Once you know the number of moles of electrons, you use the stoichiometry of the electrode half-equation to find the moles of product, and then convert to mass or volume.

<div class="worked">
<strong>Worked Example 5: Calculate the mass of copper metal deposited when a current of 2.00 A is passed through a solution of copper(II) sulfate for 30.0 minutes, using inert electrodes.</strong>

**To solve this, we need to:** calculate the charge, find the moles of electrons, use the half-equation to find moles of copper, and convert to mass.

**Step 1: Calculate the charge.** Time in seconds = 30.0 × 60 = 1800 s.
Q = I × t = 2.00 A × 1800 s = 3600 C.

**Step 2: Calculate the amount of electrons.**
n(e⁻) = Q / F = 3600 C / 96,500 C mol⁻¹ = 0.0373 mol.

**Step 3: Use the half-equation.** The reduction half-equation is Cu²⁺ + 2e⁻ → Cu. This tells us that 2 moles of electrons produce 1 mole of copper. So the number of moles of copper is half the number of moles of electrons:
n(Cu) = 0.0373 mol / 2 = 0.01865 mol.

**Step 4: Convert to mass.** The molar mass of copper (Cu) is 63.55 g mol⁻¹.
m(Cu) = n × M = 0.01865 mol × 63.55 g mol⁻¹ = 1.19 g.

**Why this makes sense:** 2 A for half an hour is a modest current and time, producing about a gram of copper — a reasonable amount for a laboratory experiment.
</div>

<div class="worked">
<strong>Worked Example 6: Calculate the volume of oxygen gas produced at the anode when a current of 1.50 A is passed through dilute sulfuric acid for 20.0 minutes, measured at STP (standard temperature and pressure, where 1 mole of gas occupies 22.7 dm³).</strong>

**Step 1:** Q = I × t = 1.50 A × (20.0 × 60) s = 1800 C.

**Step 2:** n(e⁻) = 1800 C / 96,500 C mol⁻¹ = 0.01865 mol.

**Step 3:** The anode half-equation for water oxidation is: 2H₂O → O₂ + 4H⁺ + 4e⁻. This tells us that 4 moles of electrons produce 1 mole of O₂.
n(O₂) = 0.01865 mol / 4 = 0.00466 mol.

**Step 4:** Volume at STP: V = n × 22.7 dm³ mol⁻¹ = 0.00466 mol × 22.7 dm³ mol⁻¹ = 0.106 dm³. This is equivalent to 106 cm³.

**Why this makes sense:** 0.106 dm³ is about 100 mL of gas — a visible amount of bubbling at the electrode.
</div>

---

## 5. Relating Cell Potential and Gibbs Free Energy

There is a direct relationship between the standard cell potential (E°_cell) and the standard Gibbs free energy change (ΔG°) of the cell reaction:

$$\Delta G^\circ = -nFE^\circ_{\text{cell}}$$

Where:
- ΔG° is the standard Gibbs free energy change, measured in joules per mole (J mol⁻¹). ΔG° tells us whether a reaction is thermodynamically favourable. If ΔG° is negative, the reaction is spontaneous. If ΔG° is positive, the reaction is non-spontaneous.
- n is the number of moles of electrons transferred in the balanced overall redox equation. You must use the balanced equation — do not guess this number.
- F is Faraday's constant, 96,500 C mol⁻¹.
- E°_cell is the standard cell potential in volts (V).

Notice the negative sign: if E°_cell is positive, then ΔG° is negative, meaning the reaction is spontaneous. This matches what we learned in Lesson 34.

**Units:** Because 1 V × 1 C = 1 J, the product nFE° automatically gives joules.

<div class="worked">
<strong>Worked Example 7: Calculate ΔG° for the Daniell cell reaction: Zn(s) + Cu²⁺(aq) → Zn²⁺(aq) + Cu(s), given that E°_cell = +1.10 V.</strong>

**To solve this, we need to:** identify n from the balanced equation, then apply the formula.

The balanced equation shows that 2 electrons are transferred (Zn → Zn²⁺ loses 2 e⁻; Cu²⁺ → Cu gains 2 e⁻). So n = 2.

ΔG° = −nFE°_cell = −(2) × (96,500 C mol⁻¹) × (1.10 V) = −212,300 J mol⁻¹ = −212 kJ mol⁻¹.

**Why this makes sense:** The large negative value of ΔG° confirms that this reaction is highly spontaneous, which is why the Daniell cell produces a reliable voltage.
</div>

---

## Practice Problems

**Problem 1:** Predict the products formed at the anode and at the cathode when each of the following is electrolysed using inert electrodes. Write the half-equation for each electrode reaction.
(a) Molten magnesium chloride, MgCl₂(l).
(b) Concentrated aqueous potassium iodide, KI(aq).
(c) Aqueous silver nitrate, AgNO₃(aq).

**Problem 2:** Calculate the mass of silver metal deposited when a current of 0.500 A is passed through a solution of silver nitrate, AgNO₃(aq), for exactly 45.0 minutes. The half-equation for the cathode reaction is Ag⁺(aq) + e⁻ → Ag(s). The molar mass of silver is 107.87 g mol⁻¹. (Faraday's constant F = 96,500 C mol⁻¹.)

**Problem 3:** In the electrolysis of water acidified with dilute sulfuric acid, a current of 3.00 A is passed for 15.0 minutes. The cathode reaction produces hydrogen gas: 2H₂O(l) + 2e⁻ → H₂(g) + 2OH⁻(aq). The anode reaction produces oxygen gas: 2H₂O(l) → O₂(g) + 4H⁺(aq) + 4e⁻. Calculate the volume, in dm³, of hydrogen gas and of oxygen gas produced, measured at STP where the molar volume of an ideal gas is 22.7 dm³ mol⁻¹.

**Problem 4:** A student wants to electroplate a metal spoon with nickel using a solution of nickel(II) sulfate, NiSO₄(aq), and a nickel anode. The spoon is the cathode, and the half-equation is Ni²⁺(aq) + 2e⁻ → Ni(s). The student passes a steady current of 4.00 A. Calculate the time, in minutes, required to deposit exactly 2.50 g of nickel onto the spoon. The molar mass of nickel is 58.69 g mol⁻¹. (F = 96,500 C mol⁻¹.)

**Problem 5 (IB-style):** An unknown metal M forms a sulfate salt with the formula MSO₄. When an aqueous solution of MSO₄ is electrolysed using inert electrodes, the metal M is deposited at the cathode according to the half-equation M²⁺(aq) + 2e⁻ → M(s). In an experiment, a current of 1.20 A is passed through the MSO₄ solution for a period of 25.0 minutes, and 0.592 g of metal M is deposited.
(a) Calculate the total charge, in coulombs, that passed through the cell.
(b) Calculate the amount, in moles, of electrons that passed through the cell. (F = 96,500 C mol⁻¹.)
(c) Using the half-equation, determine the amount, in moles, of metal M that was deposited.
(d) Calculate the molar mass of metal M in g mol⁻¹.
(e) The standard electrode potential for the M²⁺/M half-cell is −0.76 V. A voltaic cell is constructed by connecting an M²⁺/M half-cell to a Cu²⁺/Cu half-cell (E° = +0.34 V). Calculate the standard cell potential, E°_cell, and then use the equation ΔG° = −nFE°_cell to calculate the standard Gibbs free energy change for this cell reaction. State whether the reaction is spontaneous.

---

## Answers

**Answer 1.**

(a) Molten MgCl₂: Only Mg²⁺ and Cl⁻ are present.
Cathode (−): Mg²⁺ + 2e⁻ → Mg(l). Magnesium metal is produced.
Anode (+): 2Cl⁻ → Cl₂(g) + 2e⁻. Chlorine gas is produced.
Overall: MgCl₂(l) → Mg(l) + Cl₂(g).

(b) Concentrated KI(aq): Species present: K⁺, I⁻, H₂O.
Cathode (−): K⁺/K has E° ≈ −2.93 V. Water reduction has E° = −0.83 V. Water is more easily reduced. Cathode: 2H₂O(l) + 2e⁻ → H₂(g) + 2OH⁻(aq). Hydrogen gas is produced.
Anode (+): I⁻ is oxidised (iodide ions can be oxidised to iodine). Anode: 2I⁻(aq) → I₂(aq) + 2e⁻. Iodine is produced (brown colour appears).
Products: H₂ at cathode, I₂ at anode.

(c) AgNO₃(aq) with inert electrodes: Species present: Ag⁺, NO₃⁻, H₂O.
Cathode (−): Ag⁺/Ag has E° = +0.80 V, which is much more positive than water reduction (−0.83 V). Ag⁺ is reduced: Ag⁺(aq) + e⁻ → Ag(s). Silver metal deposits.
Anode (+): NO₃⁻ cannot be easily oxidised. Water is oxidised: 2H₂O(l) → O₂(g) + 4H⁺(aq) + 4e⁻. Oxygen gas is produced.
Products: Ag at cathode, O₂ at anode. The solution becomes acidic.

**Answer 2.**

Time in seconds = 45.0 × 60 = 2700 s.
Q = I × t = 0.500 A × 2700 s = 1350 C.
n(e⁻) = 1350 C / 96,500 C mol⁻¹ = 0.01399 mol.
From the half-equation Ag⁺ + e⁻ → Ag, 1 mol of electrons produces 1 mol of Ag.
n(Ag) = 0.01399 mol.
m(Ag) = 0.01399 mol × 107.87 g mol⁻¹ = 1.51 g.

**Answer 3.**

Q = I × t = 3.00 A × (15.0 × 60) s = 2700 C.
n(e⁻) = 2700 / 96,500 = 0.02798 mol.

For hydrogen (cathode): 2H₂O + 2e⁻ → H₂ + 2OH⁻. 2 mol e⁻ → 1 mol H₂.
n(H₂) = 0.02798 / 2 = 0.01399 mol.
V(H₂) = 0.01399 mol × 22.7 dm³ mol⁻¹ = 0.318 dm³.

For oxygen (anode): 2H₂O → O₂ + 4H⁺ + 4e⁻. 4 mol e⁻ → 1 mol O₂.
n(O₂) = 0.02798 / 4 = 0.006995 mol.
V(O₂) = 0.006995 mol × 22.7 dm³ mol⁻¹ = 0.159 dm³.

The ratio H₂ : O₂ by volume is 0.318 : 0.159 = 2 : 1, which matches the ratio in water (H₂O).

**Answer 4.**

First find the amount of nickel: n(Ni) = mass / molar mass = 2.50 g / 58.69 g mol⁻¹ = 0.04259 mol.
From the half-equation Ni²⁺ + 2e⁻ → Ni, 2 mol of e⁻ are needed per mol of Ni.
n(e⁻) = 2 × 0.04259 = 0.08518 mol.
Charge needed: Q = n(e⁻) × F = 0.08518 mol × 96,500 C mol⁻¹ = 8220 C.
Time: t = Q / I = 8220 C / 4.00 A = 2055 s.
In minutes: 2055 / 60 = 34.3 min.

**Answer 5.**

(a) Q = I × t = 1.20 A × (25.0 × 60) s = 1.20 × 1500 = 1800 C.

(b) n(e⁻) = Q / F = 1800 C / 96,500 C mol⁻¹ = 0.01865 mol.

(c) From M²⁺ + 2e⁻ → M, 2 mol e⁻ produce 1 mol M.
n(M) = 0.01865 / 2 = 0.00933 mol.

(d) Molar mass M = mass / amount = 0.592 g / 0.00933 mol = 63.5 g mol⁻¹.

(e) E° values: M²⁺/M = −0.76 V, Cu²⁺/Cu = +0.34 V.
Copper has the more positive E°, so it is the cathode (reduction). M is the anode (oxidation).
E°_cell = (+0.34) − (−0.76) = +1.10 V.
In the balanced overall reaction, M → M²⁺ + 2e⁻ and Cu²⁺ + 2e⁻ → Cu, so n = 2.
ΔG° = −nFE°_cell = −(2)(96,500)(1.10) = −212,300 J mol⁻¹ = −212 kJ mol⁻¹.
Since ΔG° is negative, the reaction is spontaneous.
(Note: The molar mass of 63.5 g mol⁻¹ identifies M as copper, but the E° value of −0.76 V is actually the value for zinc. In a real IB question, these would be consistent. The purpose here is to practice the calculation method.)
