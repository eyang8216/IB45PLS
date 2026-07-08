# Lesson 17: Born-Haber Cycles and Enthalpy of Solution (HL)

## What You'll Learn
- Define lattice enthalpy and explain what it tells us about the strength of ionic bonding
- Construct a complete Born-Haber cycle for an ionic compound and use it to calculate lattice enthalpy
- Identify and describe each step in a Born-Haber cycle: atomisation, ionisation, electron affinity, and lattice formation
- Explain how ionic charge and ionic radius affect the magnitude of lattice enthalpy
- Define enthalpy of solution and enthalpy of hydration, and calculate ΔH_sol using a simple energy cycle

---

## 1. What Is Lattice Enthalpy?

### The Meaning of Lattice Enthalpy

An ionic compound such as sodium chloride, NaCl, exists as a solid crystal at room temperature. In this crystal, sodium ions (Na⁺) and chloride ions (Cl⁻) are arranged in a regular repeating pattern called a crystal lattice. The ions are held together by strong electrostatic attractions — the positive Na⁺ ions attract the negative Cl⁻ ions, and vice versa. To pull this lattice apart into separate, free-moving gaseous ions would require a great deal of energy.

**Lattice enthalpy** (symbol: ΔH_lat⦵) is a measure of how strongly the ions are held together in the crystal. There are two equivalent ways to define it, and you must be careful to use the definition expected in IB Chemistry:

The **IB definition** (which we will use throughout this lesson) is: Lattice enthalpy is the enthalpy change when **one mole of a solid ionic compound is formed from its gaseous ions**.

For sodium chloride, this is written as:

Na⁺(g) + Cl⁻(g) → NaCl(s)

Because bringing oppositely charged ions together releases energy, lattice enthalpy defined this way is always **exothermic** — it always has a **negative** sign. The more negative the lattice enthalpy, the stronger the ionic bonding.

### An Alternative Definition

Some textbooks and exam boards define lattice enthalpy as the energy required to **separate** one mole of a solid ionic compound into its gaseous ions (the reverse of the IB definition). Under this alternative definition, lattice enthalpy is endothermic (positive). The two definitions describe the same process but in opposite directions, so the numerical value is the same, only the sign is different. In this lesson and in IB examinations, we use the formation definition (exothermic, negative).

### Why Lattice Enthalpy Matters

The magnitude of the lattice enthalpy tells you how stable the ionic crystal is. A compound with a very exothermic lattice enthalpy (large negative value) has very strong ionic bonds. This affects many properties: melting point, solubility in water, and hardness. For example, magnesium oxide (MgO) has a lattice enthalpy of approximately −3845 kJ mol⁻¹ and melts at about 2852°C, while sodium chloride (NaCl) has a lattice enthalpy of only −788 kJ mol⁻¹ and melts at 801°C. The much larger lattice enthalpy of MgO explains its much higher melting point.

---

## 2. The Born-Haber Cycle: An Energy Map for Ionic Compounds

### What Is a Born-Haber Cycle?

A Born-Haber cycle is a special type of enthalpy cycle (an application of Hess's Law) that is used to determine the lattice enthalpy of an ionic compound. It breaks the overall formation of the ionic compound from its elements into a series of individual steps, each with a known or measurable enthalpy change. By adding up all these steps, we can calculate the lattice enthalpy — a quantity that cannot be measured directly.

### The Steps of a Born-Haber Cycle

Every Born-Haber cycle for a compound with +1 and −1 ions (such as NaCl) follows the same sequence of steps. I will describe each step in the order they appear.

**Step 1: Atomisation of the metal.** The solid metal must be converted into individual gaseous atoms. Atomisation is always endothermic (ΔH positive) because you must supply energy to overcome the metallic bonding that holds the atoms together in the solid.

For sodium: Na(s) → Na(g), ΔH_at⦵ = +108 kJ mol⁻¹.

**Step 2: Ionisation of the gaseous metal atom.** The gaseous metal atom must lose one (or more) electrons to become a positive ion. This is the ionisation energy, and it is always endothermic (positive) because energy is needed to remove an electron from an atom. For elements that form 2+ ions (like Mg²⁺), both the first and second ionisation energies must be included.

For sodium: Na(g) → Na⁺(g) + e⁻, IE₁ = +496 kJ mol⁻¹.

**Step 3: Atomisation of the non-metal.** If the non-metal is diatomic in its standard state (like Cl₂, O₂, N₂), it must be split into individual gaseous atoms. This is the atomisation enthalpy (sometimes called bond dissociation enthalpy) and is endothermic.

For chlorine: ½Cl₂(g) → Cl(g), ΔH_at⦵ = +122 kJ mol⁻¹.

Note the coefficient of ½: we are making exactly 1 mole of Cl atoms because the formula NaCl has one Cl⁻ per formula unit.

**Step 4: Electron affinity of the non-metal.** The gaseous non-metal atom gains one (or more) electrons to become a negative ion. The first electron affinity is usually exothermic (negative) because energy is released when an electron is attracted to a neutral atom. However, the second electron affinity (adding an electron to an already negative ion, as in O⁻ + e⁻ → O²⁻) is endothermic because you are forcing a negatively charged electron onto an already negatively charged ion, which repels it.

For chlorine: Cl(g) + e⁻ → Cl⁻(g), EA = −349 kJ mol⁻¹.

**Step 5: Formation of the ionic solid from gaseous ions.** This is the lattice enthalpy — the step we usually calculate. It is exothermic.

For NaCl: Na⁺(g) + Cl⁻(g) → NaCl(s), ΔH_lat⦵ = ? (this is what we want to find).

**Step 6 (reference): Overall formation from elements.** This is the standard enthalpy of formation of the ionic compound, ΔH_f⦵, which is usually measured experimentally.

For NaCl: Na(s) + ½Cl₂(g) → NaCl(s), ΔH_f⦵ = −411 kJ mol⁻¹.

### The Born-Haber Cycle Diagram

The Born-Haber cycle visually connects all these steps. It starts at the bottom with the elements in their standard states, goes up through atomisation and ionisation to gaseous ions, and then comes back down through lattice formation to the ionic solid.

```
    Na⁺(g) + Cl⁻(g)
         ↑
         │ + EA(Cl) = −349
         │
    Na⁺(g) + Cl(g) + e⁻
         ↑
         │ + IE₁(Na) = +496
         │
    Na(g) + Cl(g)
         ↑                  ↘
         │ + ΔH_at(Cl)       │ ΔH_lat⦵ (unknown)
         │ = +122            │
    Na(g) + ½Cl₂(g)          │
         ↑                   │
         │ + ΔH_at(Na)       │
         │ = +108            │
         │                   ↓
    Na(s) + ½Cl₂(g) ────→ NaCl(s)
                   ΔH_f⦵ = −411
```

### The Calculation

By Hess's Law, going up the left side and then down the right side must give the same total ΔH as going directly across the bottom:

ΔH_f⦵ = ΔH_at⦵(Na) + IE₁(Na) + ΔH_at⦵(Cl) + EA(Cl) + ΔH_lat⦵

Now we substitute the numbers:

−411 = +108 + 496 + 122 + (−349) + ΔH_lat⦵
−411 = +377 + ΔH_lat⦵
ΔH_lat⦵ = −411 − 377 = −788 kJ mol⁻¹

The lattice enthalpy of sodium chloride is −788 kJ mol⁻¹.

### Worked Example 1: Lattice Enthalpy of Potassium Chloride

**Problem:** Calculate the lattice enthalpy of potassium chloride, KCl(s). Use the following data (all values in kJ mol⁻¹):
- ΔH_f⦵[KCl(s)] = −437
- ΔH_at⦵[K(s)] = +90
- IE₁[K(g)] = +419
- ΔH_at⦵[Cl₂(g)] = +244 (this is for Cl₂ → 2Cl, so for ½Cl₂ → Cl it is +122)
- EA[Cl(g)] = −349

**Strategy:** Set up the Born-Haber equation. The atomisation enthalpy of chlorine is given for the full Cl₂ molecule; since we need only ½Cl₂ (to make one Cl atom), we divide by 2: +244/2 = +122 kJ mol⁻¹.

**Calculation:**
ΔH_f⦵ = ΔH_at⦵(K) + IE₁(K) + ΔH_at⦵(Cl) + EA(Cl) + ΔH_lat⦵
−437 = +90 + 419 + 122 + (−349) + ΔH_lat⦵
−437 = +282 + ΔH_lat⦵
ΔH_lat⦵ = −437 − 282 = −719 kJ mol⁻¹.

**Why this makes sense:** KCl has a lattice enthalpy of −719 kJ mol⁻¹, which is less exothermic than NaCl (−788 kJ mol⁻¹). This is expected because K⁺ is a larger ion than Na⁺ (potassium is in period 4, sodium in period 3). A larger cation means the ions cannot get as close together, so the electrostatic attraction is weaker and the lattice enthalpy is less exothermic.

---

## 3. Born-Haber Cycle for a 2+ / 2− Compound: Magnesium Oxide

### Why MgO Is Different

Magnesium oxide, MgO, contains Mg²⁺ and O²⁻ ions. Because both ions carry double charges, we must include two ionisation energies for magnesium (to remove two electrons) and two electron affinity steps for oxygen (to add two electrons). The second electron affinity of oxygen is particularly interesting: it is endothermic, not exothermic.

### Data for MgO (all values in kJ mol⁻¹)

- ΔH_f⦵[MgO(s)] = −602
- ΔH_at⦵[Mg(s)] = +148
- IE₁[Mg(g)] = +738 (first electron removed)
- IE₂[Mg⁺(g)] = +1451 (second electron removed)
- ΔH_at⦵[O₂(g)] = +498 (for O₂ → 2O, so ½O₂ → O = +249)
- EA₁[O(g)] = −141 (first electron added to neutral oxygen)
- EA₂[O⁻(g)] = +798 (second electron added to O⁻ — endothermic!)

### Understanding the Second Electron Affinity of Oxygen

The first electron affinity of oxygen is exothermic (−141 kJ mol⁻¹) because a neutral oxygen atom attracts an extra electron. But adding a second electron to O⁻ is endothermic (+798 kJ mol⁻¹). Why? The O⁻ ion already has a negative charge. The second electron being added is also negatively charged. The O⁻ ion repels the incoming electron. Energy must be supplied to overcome this repulsion. This is a common pattern: the first electron affinity is usually exothermic, but the second (and any beyond) is always endothermic.

### The Calculation

ΔH_f⦵ = ΔH_at⦵(Mg) + IE₁(Mg) + IE₂(Mg) + ΔH_at⦵(O) + EA₁(O) + EA₂(O) + ΔH_lat⦵

First, sum all the "uphill" steps (the endothermic ones that take us from elements to gaseous ions):

Sum = +148 + 738 + 1451 + 249 + (−141) + 798
Sum = +148 + 738 + 1451 + 249 − 141 + 798
Sum = +3243 kJ mol⁻¹.

Now use the formation enthalpy:

−602 = +3243 + ΔH_lat⦵
ΔH_lat⦵ = −602 − 3243 = −3845 kJ mol⁻¹.

The lattice enthalpy of MgO is −3845 kJ mol⁻¹. This is enormously exothermic — nearly five times the magnitude of NaCl's lattice enthalpy.

### Why Is MgO's Lattice Enthalpy So Large?

There are two reinforcing reasons, both coming from Coulomb's Law, which governs the force between charged particles. Coulomb's Law states that the force of attraction between two oppositely charged ions is proportional to the product of their charges (q₁ × q₂) and inversely proportional to the square of the distance between them (1/r²).

For MgO: q₁ × q₂ = (+2) × (−2) = 4 in magnitude.
For NaCl: q₁ × q₂ = (+1) × (−1) = 1 in magnitude.

So the charge product for MgO is four times larger than for NaCl. Additionally, Mg²⁺ is smaller than Na⁺ (magnesium is in period 3 but has lost two electrons, making the ion very compact), and O²⁻ is smaller than Cl⁻ (oxygen is in period 2, chlorine is in period 3). Smaller ions can approach more closely, which makes the 1/r² term in Coulomb's Law larger. Both the charge effect and the size effect work in the same direction, making MgO's lattice enthalpy dramatically larger.

---

## 4. Factors That Affect Lattice Enthalpy

### Factor 1: Ionic Charge

This is the most important factor. The magnitude of lattice enthalpy increases rapidly as the ionic charges increase. Going from +1/−1 charges (like NaCl) to +2/−2 charges (like MgO) increases the charge product from 1 to 4. Going to +3/−2 (like Al₂O₃) increases it even further. This is why compounds with highly charged ions, such as aluminium oxide, have extremely high melting points.

### Factor 2: Ionic Radius

For ions with the same charge, smaller ions produce a more exothermic lattice enthalpy because they can pack closer together. The closer the ions, the stronger the electrostatic attraction. For example:

- NaF has a more exothermic lattice enthalpy than NaCl, which is more exothermic than NaBr, which is more exothermic than NaI. In this series, the fluoride ion (F⁻) is the smallest halide ion and the iodide ion (I⁻) is the largest.

- MgO has a more exothermic lattice enthalpy than CaO. Mg²⁺ (ionic radius ≈ 72 pm) is smaller than Ca²⁺ (ionic radius ≈ 100 pm), so the Mg²⁺/O²⁻ distance is shorter.

### Comparing Lattice Enthalpies: A Systematic Approach

When asked to compare the lattice enthalpies of two ionic compounds, check two things in order:

1. **Charges:** If the charges are different, the compound with higher charges will have the larger lattice enthalpy magnitude. Charge almost always dominates.

2. **Radii:** If the charges are the same, the compound with the smaller ions will have the larger lattice enthalpy magnitude.

**Example:** Which has the more exothermic lattice enthalpy, NaF or KBr? Both have +1/−1 charges. But Na⁺ is smaller than K⁺, and F⁻ is smaller than Br⁻. Therefore NaF has the more exothermic (more negative) lattice enthalpy.

**Example:** Which has the more exothermic lattice enthalpy, NaCl or MgO? MgO has 2+/2− charges versus 1+/1− for NaCl. The charge effect dominates, so MgO has a much more exothermic lattice enthalpy despite Mg²⁺ being similar in size to Na⁺.

---

## 5. Enthalpy of Solution and Enthalpy of Hydration

### What Happens When an Ionic Compound Dissolves?

When you add an ionic solid like NaCl to water, the solid dissolves. Two things must happen:

1. The ionic lattice must be broken apart. This requires energy — it is endothermic. The energy needed is the opposite of the lattice enthalpy: −ΔH_lat⦵ (which is positive, since ΔH_lat⦵ is negative).

2. The separated gaseous ions become surrounded by water molecules. Water is a polar molecule: the oxygen end has a partial negative charge and the hydrogen ends have partial positive charges. The water molecules orient themselves around the ions — the oxygen side toward the cation, the hydrogen side toward the anion. This process is called **hydration**, and it releases energy (it is exothermic).

### Definition of Hydration Enthalpy

The **standard enthalpy of hydration** (ΔH_hyd⦵) is the enthalpy change when **one mole of gaseous ions** is dissolved in water to form an infinitely dilute solution. Because ion-dipole attractions are formed, hydration enthalpy is always **exothermic** (negative).

Each ion has its own hydration enthalpy. For NaCl:
- ΔH_hyd⦵[Na⁺] = −406 kJ mol⁻¹
- ΔH_hyd⦵[Cl⁻] = −364 kJ mol⁻¹

### Definition of Enthalpy of Solution

The **standard enthalpy of solution** (ΔH_sol⦵) is the enthalpy change when **one mole of a substance** dissolves in water to form an infinitely dilute solution. Unlike lattice enthalpy or hydration enthalpy, ΔH_sol can be either exothermic (negative) or endothermic (positive), depending on the balance between the two competing processes.

### The Energy Cycle for Dissolution

Using Hess's Law, we can relate these quantities:

```
NaCl(s) ────────→ Na⁺(aq) + Cl⁻(aq)
   │                    ↑
   │                    │
   │ −ΔH_lat⦵           │ ΣΔH_hyd⦵
   │ (lattice broken)   │ (ions hydrated)
   │                    │
   └──→ Na⁺(g) + Cl⁻(g) ─┘
```

The enthalpy of solution is the sum of:
- Breaking the lattice: −ΔH_lat⦵ (endothermic, because ΔH_lat⦵ is negative, so −ΔH_lat⦵ is positive)
- Hydrating the ions: ΣΔH_hyd⦵ (exothermic, negative)

So: **ΔH_sol⦵ = −ΔH_lat⦵ + ΣΔH_hyd⦵**

Or equivalently: **ΔH_sol⦵ = ΣΔH_hyd⦵ − ΔH_lat⦵**

### Worked Example 2: Enthalpy of Solution of NaCl

**Problem:** Calculate the enthalpy of solution of sodium chloride using the following data:
- ΔH_lat⦵[NaCl(s)] = −788 kJ mol⁻¹
- ΔH_hyd⦵[Na⁺(g)] = −406 kJ mol⁻¹
- ΔH_hyd⦵[Cl⁻(g)] = −364 kJ mol⁻¹

**Strategy:** Apply the formula ΔH_sol = ΣΔH_hyd − ΔH_lat.

**Calculation:**
ΣΔH_hyd = (−406) + (−364) = −770 kJ mol⁻¹.
ΔH_sol = −770 − (−788) = −770 + 788 = +18 kJ mol⁻¹.

The enthalpy of solution of NaCl is +18 kJ mol⁻¹, meaning it is **slightly endothermic**. When NaCl dissolves, the energy required to break the lattice (788 kJ) is almost — but not quite — compensated by the energy released during hydration (770 kJ). The net result is a small absorption of heat. This is why you might notice a very slight cooling when you dissolve table salt in water, although the effect is subtle compared to, say, ammonium nitrate.

### Worked Example 3: Enthalpy of Solution of Calcium Chloride

**Problem:** Calculate the enthalpy of solution of calcium chloride, CaCl₂(s). Data:
- ΔH_lat⦵[CaCl₂(s)] = −2258 kJ mol⁻¹
- ΔH_hyd⦵[Ca²⁺(g)] = −1592 kJ mol⁻¹
- ΔH_hyd⦵[Cl⁻(g)] = −364 kJ mol⁻¹ (per mole of Cl⁻ ions)

**Strategy:** CaCl₂ produces one Ca²⁺ ion and two Cl⁻ ions per formula unit. So the total hydration enthalpy includes the hydration of one Ca²⁺ plus two Cl⁻.

**Calculation:**
ΣΔH_hyd = (−1592) + 2 × (−364) = −1592 − 728 = −2320 kJ mol⁻¹.
ΔH_sol = −2320 − (−2258) = −2320 + 2258 = −62 kJ mol⁻¹.

The enthalpy of solution is −62 kJ mol⁻¹, which is **exothermic**. When CaCl₂ dissolves, the hydration energy released (−2320 kJ) exceeds the energy required to break the lattice (+2258 kJ), so there is a net release of heat.

### When Is Dissolution Exothermic vs. Endothermic?

The sign of ΔH_sol depends on the competition between lattice enthalpy and hydration enthalpy:

- If the magnitude of the hydration enthalpy (|ΣΔH_hyd|) is **greater** than the magnitude of the lattice enthalpy (|ΔH_lat|), then ΔH_sol is negative and dissolution is **exothermic** (the solution gets warm). CaCl₂ is an example.

- If |ΣΔH_hyd| is **smaller** than |ΔH_lat|, then ΔH_sol is positive and dissolution is **endothermic** (the solution gets cold). NaCl is a borderline case; NH₄NO₃ and KCl are clearer examples of endothermic dissolution.

### Common Misconception

Many students think that if a compound is soluble, its dissolution must be exothermic. This is not true. Solubility depends on Gibbs free energy (ΔG = ΔH − TΔS), not on ΔH alone. A compound can dissolve even if ΔH_sol is positive, as long as the entropy increase (ΔS) is large enough to make ΔG negative. We will study this in detail in Lesson 18.

---

## Practice Problems

1. Calculate the lattice enthalpy of lithium fluoride, LiF(s), using the following data (all values in kJ mol⁻¹): ΔH_f⦵[LiF(s)] = −617; ΔH_at⦵[Li(s)] = +161; IE₁[Li(g)] = +520; ΔH_at⦵[F₂(g)] = +158 (this is for F₂ → 2F); EA[F(g)] = −328.

2. Sodium fluoride (NaF) and potassium bromide (KBr) both have ions with +1 and −1 charges. Explain in detail which compound has the more exothermic lattice enthalpy and why. Refer to both ionic charge and ionic radius in your answer.

3. The Born-Haber cycle for magnesium chloride, MgCl₂, involves atomisation of magnesium, two ionisation energies for magnesium, atomisation of chlorine (twice, since two Cl⁻ ions are formed), and two electron affinities for chlorine. Using the following data (all in kJ mol⁻¹), calculate the lattice enthalpy of MgCl₂: ΔH_f⦵[MgCl₂] = −641; ΔH_at⦵[Mg] = +148; IE₁[Mg] = +738; IE₂[Mg] = +1451; ΔH_at⦵[Cl₂] = +244 (for Cl₂ → 2Cl); EA[Cl] = −349. State clearly how you account for the stoichiometry (there are two chloride ions in the formula).

4. The lattice enthalpy of silver chloride, AgCl(s), is −915 kJ mol⁻¹. The hydration enthalpies are: ΔH_hyd⦵[Ag⁺] = −464 kJ mol⁻¹ and ΔH_hyd⦵[Cl⁻] = −364 kJ mol⁻¹. Calculate the enthalpy of solution of AgCl and state whether dissolution is exothermic or endothermic.

5. **(IB-exam style)** The Born-Haber cycle can be used to calculate the lattice enthalpy of calcium oxide, CaO(s). The relevant data are provided below, all in kJ mol⁻¹:
   - Standard enthalpy of formation of CaO(s): ΔH_f⦵ = −635
   - Standard enthalpy of atomisation of Ca(s): ΔH_at⦵ = +178
   - First ionisation energy of Ca(g): IE₁ = +590
   - Second ionisation energy of Ca⁺(g): IE₂ = +1145
   - Standard enthalpy of atomisation of O₂(g): +498 (for O₂(g) → 2O(g))
   - First electron affinity of O(g): EA₁ = −141
   - Second electron affinity of O⁻(g): EA₂ = +798
   (a) Construct a fully labeled Born-Haber cycle diagram for CaO(s). Show all the steps with the correct chemical equations and their associated enthalpy values.
   (b) Calculate the lattice enthalpy of CaO(s) using the data provided.
   (c) The lattice enthalpy of MgO(s) is −3845 kJ mol⁻¹. Explain, with reference to ionic radius, why CaO has a less exothermic lattice enthalpy than MgO despite both having 2+ and 2− ions.

---

## Answers

1. **Step 1:** Convert ΔH_at⦵[F₂] to the value for one F atom. The given value +158 is for F₂(g) → 2F(g). For ½F₂(g) → F(g), we divide by 2: ΔH_at⦵ = +158/2 = +79 kJ mol⁻¹.

   **Step 2:** Set up the Born-Haber equation:
   ΔH_f⦵ = ΔH_at⦵(Li) + IE₁(Li) + ΔH_at⦵(F) + EA(F) + ΔH_lat⦵
   −617 = +161 + 520 + 79 + (−328) + ΔH_lat⦵
   −617 = +432 + ΔH_lat⦵
   ΔH_lat⦵ = −617 − 432 = −1049 kJ mol⁻¹.

   **Why this makes sense:** LiF has a more exothermic lattice enthalpy (−1049) than NaCl (−788). Both Li⁺ and F⁻ are very small ions (they are in the second period), so they can approach each other very closely, resulting in strong electrostatic attraction.

2. Both NaF and KBr have ions with +1 and −1 charges, so the charge factor does not differentiate them. We must compare the ionic radii. Sodium fluoride contains the Na⁺ ion and the F⁻ ion. Potassium bromide contains the K⁺ ion and the Br⁻ ion. Na⁺ has a smaller ionic radius than K⁺ because sodium is in period 3 while potassium is in period 4 — the K⁺ ion has an extra electron shell, making it larger. Similarly, F⁻ has a smaller ionic radius than Br⁻ because fluorine is in period 2 while bromine is in period 4. According to Coulomb's Law, the electrostatic force between ions is inversely proportional to the square of the distance between them (F ∝ 1/r²). Because both ions in NaF are smaller than their counterparts in KBr, the interionic distance in NaF is shorter. This means the electrostatic attraction between Na⁺ and F⁻ is stronger than the attraction between K⁺ and Br⁻. A stronger attraction means more energy is released when the lattice forms, so NaF has a more exothermic lattice enthalpy.

3. **Step 1 — Account for stoichiometry:** MgCl₂ has two chloride ions. This means the atomisation of chlorine is needed for two Cl atoms: 2 × ½Cl₂ → 2Cl, or equivalently, one full Cl₂ molecule → 2Cl. The given ΔH_at⦵[Cl₂] = +244 already covers Cl₂ → 2Cl, so we do not divide by 2 — we use the full +244. Similarly, the electron affinity applies twice: two Cl atoms each gain one electron, so 2 × EA(Cl) = 2 × (−349) = −698.

   **Step 2 — Sum all the "uphill" steps:**
   ΔH_at⦵(Mg) = +148
   IE₁(Mg) = +738
   IE₂(Mg) = +1451
   ΔH_at⦵(2Cl) = +244
   2 × EA(Cl) = −698
   Sum = 148 + 738 + 1451 + 244 + (−698) = +1883 kJ mol⁻¹.

   **Step 3 — Born-Haber equation:**
   ΔH_f⦵ = sum + ΔH_lat⦵
   −641 = +1883 + ΔH_lat⦵
   ΔH_lat⦵ = −641 − 1883 = −2524 kJ mol⁻¹.

   **Why this makes sense:** The magnitude (2524) is much larger than NaCl (788) because of the 2+ charge on magnesium, but smaller than MgO (3845) because Cl⁻ has only a 1− charge compared to O²⁻ with 2−. The charge product for MgCl₂ is (+2) × (−1) = 2, compared to (+2) × (−2) = 4 for MgO.

4. ΔH_sol = ΣΔH_hyd − ΔH_lat
   ΣΔH_hyd = (−464) + (−364) = −828 kJ mol⁻¹.
   ΔH_sol = −828 − (−915) = −828 + 915 = +87 kJ mol⁻¹.

   ΔH_sol is positive, so the dissolution of AgCl is **endothermic**. This means AgCl absorbs heat from its surroundings when it dissolves. This is consistent with the fact that AgCl is very sparingly soluble — the endothermic enthalpy of solution contributes to its low solubility.

5. **(a)** Born-Haber cycle for CaO:

   ```
       Ca²⁺(g) + O²⁻(g)
            ↑
            │ + EA₂(O) = +798
            │
       Ca²⁺(g) + O⁻(g) + e⁻
            ↑
            │ + EA₁(O) = −141
            │
       Ca²⁺(g) + O(g) + 2e⁻
            ↑
            │ + IE₂(Ca) = +1145
            │
       Ca⁺(g) + O(g) + e⁻
            ↑
            │ + IE₁(Ca) = +590
            │
       Ca(g) + O(g)
            ↑                     ↘
            │ + ΔH_at(O) = +249    │ ΔH_lat⦵ (unknown)
            │                      │
       Ca(g) + ½O₂(g)              │
            ↑                      │
            │ + ΔH_at(Ca) = +178   │
            │                      ↓
       Ca(s) + ½O₂(g) ──────────→ CaO(s)
                     ΔH_f⦵ = −635
   ```

   **(b)** Sum of the endothermic steps going up:
   +178 + 590 + 1145 + 249 + (−141) + 798
   = 178 + 590 = 768
   768 + 1145 = 1913
   1913 + 249 = 2162
   2162 + (−141) = 2021
   2021 + 798 = 2819 kJ mol⁻¹.

   Born-Haber equation:
   −635 = +2819 + ΔH_lat⦵
   ΔH_lat⦵ = −635 − 2819 = −3454 kJ mol⁻¹.

   **(c)** Both CaO and MgO have ions with 2+ and 2− charges, so the charge product (q₁ × q₂ = 4) is identical for both compounds. The difference in lattice enthalpy must therefore come from the ionic radii. Calcium is directly below magnesium in Group 2 of the periodic table, meaning the Ca²⁺ ion is larger than the Mg²⁺ ion because calcium has one extra electron shell. With a larger cation, the interionic distance in CaO is greater than in MgO. According to Coulomb's Law (F ∝ 1/r²), a larger distance means a weaker electrostatic attraction between the ions. A weaker attraction means less energy is released when the lattice forms, so CaO has a less exothermic lattice enthalpy (−3454 kJ mol⁻¹) than MgO (−3845 kJ mol⁻¹). The difference of approximately 391 kJ mol⁻¹ is entirely attributable to the larger size of the Ca²⁺ ion compared to the Mg²⁺ ion, since the O²⁻ ion is common to both compounds.
