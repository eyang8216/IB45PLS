# Lesson 41: Stereoisomerism and Synthetic Routes (HL)

## What You'll Learn

In this lesson, you will bring together many of the skills you have developed throughout organic chemistry. First, you will learn about stereoisomerism — molecules that have the same atoms connected in the same order but arranged differently in space. This includes E/Z (geometric) isomerism and optical isomerism (enantiomers). Second, you will learn how to plan synthetic routes — sequences of reactions that transform a starting material into a desired target molecule. This is called retrosynthetic analysis, and it is one of the most powerful skills in organic chemistry.

---

## 1. Isomerism — A Review of the Big Picture

Before we study stereoisomerism, let us review the types of isomerism. **Isomers** are different compounds that have the same molecular formula.

There are two broad categories:

**Structural isomers** (also called constitutional isomers) have the same molecular formula but **different connectivity** — the atoms are bonded to each other in a different order. Subtypes include:
- **Chain isomerism:** Different carbon skeleton arrangement. Example: butane (straight chain, CH₃CH₂CH₂CH₃) and 2-methylpropane (branched, (CH₃)₃CH). Both C₄H₁₀.
- **Position isomerism:** Same functional group but at a different position. Example: butan-1-ol (CH₃CH₂CH₂CH₂OH) and butan-2-ol (CH₃CH₂CH(OH)CH₃). Both C₄H₁₀O.
- **Functional group isomerism:** Different functional groups altogether. Example: ethanol (CH₃CH₂OH, an alcohol) and methoxymethane (CH₃OCH₃, an ether). Both C₂H₆O.

**Stereoisomers** have the same molecular formula AND the same connectivity — the same atoms are bonded to the same other atoms in the same order. The difference is purely in how those atoms are **arranged in three-dimensional space**. There are two types:
- **Geometric isomerism (E/Z or cis-trans):** Different arrangement of groups around a double bond or ring.
- **Optical isomerism (enantiomerism):** Non-superimposable mirror-image molecules.

---

## 2. E/Z Isomerism — Systematic Naming for Geometric Isomers

In Lesson 37, you learned about cis-trans isomerism in alkenes: cis means similar groups are on the same side of the C=C double bond; trans means they are on opposite sides. This system works well when each carbon of the double bond has one group that is clearly "similar" (usually H). But what about a molecule where all four groups are different?

### The CIP Priority Rules

The **Cahn-Ingold-Prelog (CIP) system** gives us a systematic way to assign priority to the two groups on each carbon of the double bond. The rules are:

**Rule 1: Higher atomic number = higher priority.** Compare the atoms directly bonded to the double-bond carbon. The atom with the higher atomic number gets higher priority.

**Rule 2: If the directly bonded atoms are the same, look at the next atoms along the chain.** Compare atomic numbers one step further out. Keep going until you find a difference.

**Rule 3: Multiple bonds count as multiple single bonds to that atom.** A C=O double bond is treated as the carbon being bonded to two oxygen atoms (for the purpose of comparing with other groups).

Once you have assigned priorities to both groups on each carbon, look at the two higher-priority groups:
- If they are on the **same side** of the double bond: **Z** (from the German "zusammen," meaning "together").
- If they are on **opposite sides**: **E** (from the German "entgegen," meaning "opposite").

<div class="worked">
<strong>Worked Example 1: Assign E or Z to 1-bromo-1-chloropropene.</strong>

The molecule is CH₃CH=CBrCl. The double bond is between C-1 (which has Br and Cl attached) and C-2 (which has CH₃ and H attached).

**On C-1:** The two groups are Br and Cl.
- Br has atomic number 35.
- Cl has atomic number 17.
- Br > Cl → **Br is higher priority**.

**On C-2:** The two groups are CH₃ (methyl) and H.
- In CH₃, the directly bonded atom is C (atomic number 6).
- H has atomic number 1.
- C > H → **CH₃ is higher priority**.

Now look at the two higher-priority groups: Br (on C-1) and CH₃ (on C-2). If they are on the same side → Z. If opposite → E.

In this case, Br and CH₃ are on **opposite sides** of the double bond. This is the **E** isomer: **(E)-1-bromo-1-chloropropene**.
</div>

---

## 3. Optical Isomerism — Chirality and Enantiomers

### What Makes a Molecule Chiral?

A carbon atom bonded to **four different groups** is called a **chiral centre** (or asymmetric carbon atom). The word "chiral" comes from the Greek word for "hand" — your left and right hands are mirror images that cannot be superimposed. In the same way, a molecule with a chiral centre exists as two different forms that are mirror images of each other but are not identical.

These two mirror-image forms are called **enantiomers**. Enantiomers have identical physical properties — same melting point, same boiling point, same solubility, same density. They react identically with non-chiral reagents. But they differ in **one** important physical property and in their biological activity:

**Interaction with plane-polarised light:** Normal light vibrates in all directions. When light passes through a polarising filter, it vibrates in only one plane — this is called **plane-polarised light**. When plane-polarised light passes through a solution of a single enantiomer, the plane of polarisation is **rotated**. One enantiomer rotates the plane clockwise (this is called **dextrorotatory**, given the symbol + or d). The other enantiomer rotates the plane by exactly the same amount but in the opposite direction — anticlockwise (**laevorotatory**, symbol − or l).

**Biological activity:** Many biological molecules — enzymes, receptors, DNA — are themselves chiral. Because of this, two enantiomers of a drug can have completely different biological effects. One may be therapeutic and the other toxic. The most famous example is thalidomide: one enantiomer was an effective sedative for morning sickness, but the other caused severe birth defects.

### How to Identify a Chiral Centre

Look for a carbon atom with four different things attached. If you find one, the molecule is chiral and will exist as a pair of enantiomers.

<div class="worked">
<strong>Worked Example 2: Determine whether butan-2-ol has optical isomers.</strong>

Butan-2-ol is CH₃CH₂CH(OH)CH₃. Look at the carbon bearing the −OH group (C-2). What four groups are attached to it?
1. −H (hydrogen atom)
2. −OH (hydroxyl group)
3. −CH₃ (methyl group)
4. −CH₂CH₃ (ethyl group)

These are four **different** groups. Therefore, C-2 is a chiral centre, and butan-2-ol exists as two enantiomers.

To draw them: one enantiomer has the −OH group as a wedge (coming out of the page toward you) and the −H as a dashed line (going into the page away from you), with CH₃ and CH₂CH₃ in the plane. The other enantiomer is the mirror image — −OH dashed and −H wedged. These two are non-superimposable — try to rotate one to match the other in your mind; you cannot without breaking and remaking bonds.
</div>

---

## 4. Racemic Mixtures

A **racemic mixture** (or racemate) is a **50:50 mixture** of two enantiomers. Because each enantiomer rotates plane-polarised light by the same amount but in opposite directions, the rotations **cancel exactly**. A racemic mixture has **zero net optical rotation** — it is optically inactive.

Racemic mixtures are formed whenever a chiral centre is created under conditions where both enantiomers are equally likely to form. The most important case for IB Chemistry HL is the **SN1 reaction** at a chiral carbon. Because the carbocation intermediate is planar (flat), the nucleophile can attack from either side with equal probability, producing a 50:50 mixture of the two enantiomers.

<div class="worked">
<strong>Worked Example 3: (R)-2-bromobutane is heated with water. Predict whether the product mixture will be optically active.</strong>

(R)-2-bromobutane has a chiral centre at C-2. The carbon bears −H, −Br, −CH₃, and −CH₂CH₃. The (R) designation tells us the specific three-dimensional arrangement of these groups.

Heating with water: The substrate is 2° (secondary), the nucleophile (H₂O) is weak, and the solvent (water) is polar protic. These conditions favour the **SN1 mechanism**.

In SN1, the C−Br bond breaks first, forming a **planar carbocation** at C-2. This carbocation has three bonds in a plane (to H, CH₃, and CH₂CH₃) with an empty p orbital perpendicular to the plane. Water can attack this carbocation from **either the top face or the bottom face** with equal probability.

Attack from one face gives (R)-butan-2-ol. Attack from the other gives (S)-butan-2-ol. Both are formed in equal amounts → **racemic mixture**.

The product mixture is therefore **optically inactive** — the rotations from the two enantiomers cancel. This is classic racemisation by the SN1 mechanism.
</div>

---

## 5. Key Synthetic Transformations — Your Reaction Toolkit

The following table summarises the reactions you have learned across Lessons 36–40. These are the tools you will use to plan synthetic routes. You do not need to memorise every reagent and condition right now, but you should be familiar with what transformations are possible.

| Starting Material | Product | Type of Reaction | Key Reagents/Conditions |
|-------------------|---------|------------------|------------------------|
| Alkane | Halogenoalkane | Free-radical substitution | X₂ (Cl₂ or Br₂), UV light |
| Alkene | Alkane | Hydrogenation (addition) | H₂, Ni catalyst, 150 °C |
| Alkene | Halogenoalkane | Electrophilic addition | HX (room temp) or X₂ (room temp, dark) |
| Alkene | Alcohol | Hydration (addition) | H₂O(g), H₃PO₄ catalyst, 300 °C, 60 atm |
| Halogenoalkane | Alcohol | Nucleophilic substitution | NaOH(aq), warm |
| Halogenoalkane | Nitrile | Nucleophilic substitution | KCN, ethanol, reflux |
| Halogenoalkane | Alkene | Elimination | NaOH(ethanolic), hot |
| 1° Alcohol | Aldehyde | Oxidation | K₂Cr₂O₇/H⁺, distillation |
| 1° Alcohol | Carboxylic acid | Oxidation | K₂Cr₂O₇/H⁺, reflux |
| 2° Alcohol | Ketone | Oxidation | K₂Cr₂O₇/H⁺, reflux |
| Aldehyde | 1° Alcohol | Reduction | NaBH₄ (or LiAlH₄) |
| Ketone | 2° Alcohol | Reduction | NaBH₄ (or LiAlH₄) |
| Carboxylic acid + Alcohol | Ester | Esterification (condensation) | H₂SO₄ catalyst, reflux |
| Ester | Carboxylic acid + Alcohol | Hydrolysis | H⁺/H₂O (acid) or NaOH (base) |
| Benzene | Nitrobenzene | Electrophilic substitution (nitration) | HNO₃/H₂SO₄, 50–55 °C |
| Nitrobenzene | Phenylamine | Reduction | Sn/HCl, reflux, then NaOH |
| Benzene | Alkylbenzene | Friedel-Crafts alkylation | RCl, AlCl₃ catalyst |

---

## 6. Retrosynthetic Analysis — Working Backwards

**Retrosynthetic analysis** is a method for planning the synthesis of a target molecule by working backwards — breaking the target into simpler starting materials step by step. At each step, you ask: "What reaction could have formed this functional group, and what were the reactants for that reaction?"

This is like planning a journey by starting at the destination and working backwards to find the route. Once the backward analysis is complete, you reverse it to get the forward synthesis.

<div class="worked">
<strong>Worked Example 4: Propose a synthesis of phenylamine (C₆H₅NH₂) starting from benzene.</strong>

**Retrosynthetic analysis:** Phenylamine has an −NH₂ group attached to a benzene ring. How can we put an −NH₂ onto benzene? There is no direct way to add −NH₂ via electrophilic substitution. But we learned that nitrobenzene (C₆H₅NO₂) can be reduced to phenylamine. And nitrobenzene is made directly from benzene by nitration.

So the route, working backwards: Phenylamine ← Nitrobenzene ← Benzene.

**Forward synthesis:**
Step 1: Benzene + HNO₃/H₂SO₄ (50–55 °C) → nitrobenzene (nitration).
Step 2: Nitrobenzene + Sn/HCl (reflux), then NaOH → phenylamine (reduction).

Overall: C₆H₆ → C₆H₅NO₂ → C₆H₅NH₂. This is a classic two-step aromatic synthesis.
</div>

<div class="worked">
<strong>Worked Example 5: Propose a synthesis of ethyl propanoate starting from ethene as the only source of carbon.</strong>

**Retrosynthetic analysis:** Ethyl propanoate is CH₃CH₂COOCH₂CH₃. It is an ester, formed from propanoic acid (CH₃CH₂COOH) and ethanol (CH₃CH₂OH).

We need to make both propanoic acid and ethanol from ethene (CH₂=CH₂). 

Ethanol from ethene: direct hydration — C₂H₄ + H₂O → C₂H₅OH (H₃PO₄, 300 °C, 60 atm).

Propanoic acid has 3 carbons. We need to extend the carbon chain. One way: make ethanol, oxidise to ethanoic acid, convert to something that can add a carbon. Or: starting from ethene, we can make bromoethane (C₂H₄ + HBr → C₂H₅Br), then react with KCN to make propanenitrile (C₂H₅CN), then hydrolyse the nitrile to propanoic acid:
- C₂H₅Br + KCN → C₂H₅CN (SN2)
- C₂H₅CN + 2H₂O + H⁺ → C₂H₅COOH + NH₄⁺ (acid hydrolysis of nitrile)

Then combine propanoic acid with ethanol (H₂SO₄, reflux) to make the ester.

This is a multi-step synthesis requiring careful planning and multiple reaction types.
</div>

---

## Practice Problems

**Problem 1:** Identify the type of isomerism (structural — chain, position, or functional group; or stereoisomerism — E/Z or optical) that exists between each of the following pairs of compounds.
(a) Butane, CH₃CH₂CH₂CH₃, and 2-methylpropane, (CH₃)₃CH.
(b) Butan-1-ol, CH₃CH₂CH₂CH₂OH, and butan-2-ol, CH₃CH₂CH(OH)CH₃.
(c) (E)-but-2-ene and (Z)-but-2-ene.
(d) (R)-butan-2-ol and (S)-butan-2-ol.

**Problem 2:** For each of the following compounds, assign the configuration as E or Z using the CIP priority rules. Explain your reasoning by stating which group has higher priority on each carbon of the double bond.
(a) 1,2-dichloroethene, ClCH=CHCl, in which the two chlorine atoms are on the same side of the double bond.
(b) 1-chloropropene, CH₃CH=CHCl, in which the chlorine atom and the methyl group are on the same side of the double bond.

**Problem 3:** Identify each chiral centre in the following molecules by marking it with an asterisk (*). If a molecule has no chiral centre, state this and explain why.
(a) Lactic acid (2-hydroxypropanoic acid): CH₃CH(OH)COOH.
(b) The amino acid cysteine: HSCH₂CH(NH₂)COOH.
(c) 2-chlorobutane: CH₃CHClCH₂CH₃.

**Problem 4:** Propose a synthetic route (showing reagents, conditions, and the product of each step) for each of the following transformations. You may use any necessary inorganic reagents.
(a) Ethene (CH₂=CH₂) → ethanoic acid (CH₃COOH). Two steps required.
(b) Benzene → 1,3-dinitrobenzene. Two steps required.
(c) Propan-1-ol (CH₃CH₂CH₂OH) → propan-2-ol (CH₃CH(OH)CH₃). Two or three steps required.

**Problem 5 (IB-style):** Compound X is a chiral alcohol with the molecular formula C₅H₁₂O. When X is heated with acidified potassium dichromate(VI), it is oxidised to compound Y, which has the molecular formula C₅H₁₀O. Compound Y gives a negative result with Tollens' reagent (no silver mirror forms). When X is heated with concentrated sulfuric acid, a mixture of three alkenes is formed, each with the formula C₅H₁₀. The alkene with the highest boiling point (call it Z₁) is the major product.
(a) Deduce the structural formula of X. Your answer must account for all the evidence: the chirality of X, the oxidation to Y with no Tollens' test, and the formation of three alkenes on dehydration. Give the IUPAC name of X and indicate the chiral centre with an asterisk (*).
(b) Give the structural formula and IUPAC name of Y. Explain why Y gives a negative Tollens' test.
(c) Draw the structures of the three alkenes formed by dehydration of X. Name each one. Identify Z₁ (the major product) by applying Saytzeff's rule. Explain, in terms of alkene stability, why Z₁ is the most abundant product.
(d) Propose a two-step synthesis of Y starting from an alkene of your choice. For each step, state the reagents and conditions and draw the structure of the intermediate.

---

## Answers

**Answer 1.**

(a) Butane and 2-methylpropane: Both C₄H₁₀. They differ in the arrangement of the carbon skeleton — straight chain versus branched. This is **chain isomerism**, a type of structural isomerism.

(b) Butan-1-ol and butan-2-ol: Both C₄H₁₀O, both alcohols. The −OH group is at C-1 in one and C-2 in the other. This is **position isomerism**, a type of structural isomerism.

(c) (E)-but-2-ene and (Z)-but-2-ene: Same connectivity (CH₃−CH=CH−CH₃), differ only in the spatial arrangement of the CH₃ groups around the double bond. This is **geometric (E/Z) isomerism**, a type of stereoisomerism.

(d) (R)-butan-2-ol and (S)-butan-2-ol: Same connectivity, non-superimposable mirror images. This is **optical isomerism** (enantiomerism), a type of stereoisomerism.

**Answer 2.**

(a) 1,2-dichloroethene, ClCH=CHCl. On each carbon, the two groups are Cl (atomic number 17) and H (atomic number 1). On both carbons, Cl has higher priority. Both high-priority Cl atoms are on the **same side** of the double bond → **Z (zusammen)**. The molecule is (Z)-1,2-dichloroethene.

(b) 1-chloropropene, CH₃CH=CHCl.

On C-1 (the carbon with Cl and H): Cl (Z=17) vs H (Z=1) → **Cl is higher priority**.

On C-2 (the carbon with CH₃ and H): the directly bonded atom in CH₃ is C (Z=6) vs H (Z=1) → **CH₃ is higher priority**.

The two higher-priority groups are Cl (on C-1) and CH₃ (on C-2). These are on the **same side** of the double bond → **Z**. The molecule is **(Z)-1-chloropropene**.

**Answer 3.**

(a) Lactic acid, CH₃CH(OH)COOH: Look at C-2. Attached to C-2 are −H, −OH, −CH₃, and −COOH. Four **different** groups → **C-2 is a chiral centre**. Mark it: CH₃−C*H(OH)−COOH.

(b) Cysteine, HSCH₂CH(NH₂)COOH: Look at the central carbon (C-2). Attached are −H, −NH₂, −COOH, and −CH₂SH. Four different groups → **C-2 is a chiral centre**. Mark it: HSCH₂−C*H(NH₂)−COOH.

(c) 2-chlorobutane, CH₃CHClCH₂CH₃: Look at C-2. Attached are −H, −Cl, −CH₃, and −CH₂CH₃. Four different groups → **C-2 is a chiral centre**. Mark it: CH₃−C*HCl−CH₂CH₃.

**Answer 4.**

(a) Ethene → ethanoic acid:
Step 1: Hydration of ethene to ethanol. C₂H₄ + H₂O → CH₃CH₂OH. Conditions: H₃PO₄ catalyst, 300 °C, 60 atm.
Step 2: Oxidation of ethanol to ethanoic acid. CH₃CH₂OH + 2[O] → CH₃COOH + H₂O. Conditions: K₂Cr₂O₇/H⁺, reflux.

(b) Benzene → 1,3-dinitrobenzene:
Step 1: Nitration of benzene to nitrobenzene. C₆H₆ + HNO₃ → C₆H₅NO₂ + H₂O. Conditions: H₂SO₄ catalyst, 50–55 °C.
Step 2: Further nitration of nitrobenzene to 1,3-dinitrobenzene. C₆H₅NO₂ + HNO₃ → C₆H₄(NO₂)₂ + H₂O. Conditions: H₂SO₄, higher temperature (the −NO₂ group is meta-directing, so the second nitro group goes to the 3-position).

(c) Propan-1-ol → propan-2-ol:
Step 1: Dehydration of propan-1-ol to propene. CH₃CH₂CH₂OH → CH₃CH=CH₂ + H₂O. Conditions: hot Al₂O₃ catalyst (or concentrated H₂SO₄, heat).
Step 2: Hydration of propene to propan-2-ol. CH₃CH=CH₂ + H₂O → CH₃CH(OH)CH₃. Conditions: H₃PO₄ catalyst, 300 °C, 60 atm. This follows Markovnikov's rule — the −OH attaches to the more substituted carbon (C-2), giving propan-2-ol.

**Answer 5.**

(a) X is C₅H₁₂O, chiral, an alcohol.

Evidence: X is oxidised to Y (C₅H₁₀O), which is a ketone (negative Tollens' test). This means X must be a **secondary (2°) alcohol** — oxidation of a 2° alcohol gives a ketone, and ketones do not react with Tollens' reagent.

X is also chiral. Dehydration of X gives three alkenes. If X is pentan-2-ol (CH₃CH₂CH₂CH(OH)CH₃), dehydration can remove H from C-1 (giving pent-1-ene) or from C-3 (giving cis and trans pent-2-ene) — three alkene products.

X is **pentan-2-ol**: CH₃CH₂CH₂C*H(OH)CH₃. The chiral centre is C-2, with four different groups: −H, −OH, −CH₃, and −CH₂CH₂CH₃.

(b) Y is **pentan-2-one**: CH₃CH₂CH₂COCH₃. It gives a negative Tollens' test because it is a **ketone** — ketones do not have a hydrogen atom attached to the carbonyl carbon, so they cannot be oxidised under the mild conditions of Tollens' reagent (which detects aldehydes).

(c) Dehydration of pentan-2-ol (removing H₂O, catalysed by concentrated H₂SO₄, heat):
- Z₁: **(E)-pent-2-ene** (trans), CH₃CH₂CH=CHCH₃ (more stable geometric isomer; CH₃ groups opposite).
- Z₂: **(Z)-pent-2-ene** (cis), CH₃CH₂CH=CHCH₃ (CH₃ groups on the same side).
- Z₃: **pent-1-ene**, CH₃CH₂CH₂CH=CH₂.

Z₁, pent-2-ene (specifically the E isomer, or both E and Z collectively), is the major product by **Saytzeff's rule**: the more substituted alkene is more stable. Pent-2-ene has two alkyl groups on the C=C carbons (ethyl and methyl), while pent-1-ene has only one alkyl group (propyl). More substituted alkenes are more stable due to hyperconjugation — the C−H σ bonds of adjacent alkyl groups donate electron density into the π* orbital, lowering the overall energy. Between E and Z pent-2-ene, the E (trans) isomer is more stable because the two alkyl groups are farther apart, minimising steric repulsion.

(d) Synthesis of pentan-2-one starting from an alkene:

Start with **pent-1-ene**, CH₃CH₂CH₂CH=CH₂.

Step 1: Hydration (Markovnikov addition of water). CH₃CH₂CH₂CH=CH₂ + H₂O → CH₃CH₂CH₂CH(OH)CH₃ (pentan-2-ol). Conditions: H₃PO₄ catalyst, 300 °C, 60 atm.

Step 2: Oxidation. CH₃CH₂CH₂CH(OH)CH₃ + [O] → CH₃CH₂CH₂COCH₃ + H₂O. Conditions: K₂Cr₂O₇/H⁺, reflux. The product is pentan-2-one (Y).
