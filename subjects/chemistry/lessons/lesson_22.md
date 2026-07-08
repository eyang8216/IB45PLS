# Lesson 22: Reaction Mechanisms and The Arrhenius Equation (HL)

## What You'll Learn
- Define a reaction mechanism and identify elementary steps, intermediates, and the rate-determining step
- Predict the rate law from a given reaction mechanism by identifying the rate-determining step
- Determine whether a proposed mechanism is consistent with an experimentally measured rate law
- Define molecularity for elementary steps
- Apply the Arrhenius equation in both its exponential and linear forms
- Calculate activation energy from rate constants measured at two different temperatures

---

## 1. Reaction Mechanisms

### What This Concept Is and Why It Matters

When you write a balanced chemical equation like 2NO(g) + O₂(g) → 2NO₂(g), you are describing the overall change — what you have at the start and what you have at the end. But this equation does not tell you what actually happens at the molecular level. Do two NO molecules and one O₂ molecule all crash into each other at the same instant? Or does the reaction happen in a series of smaller, simpler steps?

A **reaction mechanism** is the detailed, step-by-step sequence of events at the molecular level that leads from reactants to products. Understanding mechanisms lets chemists predict rate laws, design catalysts, and control which products form.

### Elementary Steps

An **elementary step** is a single molecular event — one collision or one decomposition — that cannot be broken down into simpler chemical events. Each elementary step represents exactly what happens when particles interact.

For example, if an elementary step is written as A + B → C, it literally means that one particle of A collides with one particle of B, and in that single collision, they rearrange to form one particle of C.

The overall reaction is the sum of all the elementary steps in the mechanism. When you add up all the steps, any species that appears on both the left and right sides cancels out, leaving only the reactants and products shown in the overall balanced equation.

### Intermediates

An **intermediate** is a species that is produced in one elementary step and then consumed in a later elementary step. Intermediates do not appear in the overall balanced equation because they cancel out when the steps are added together. They exist only fleetingly during the reaction. They are real chemical species — you can sometimes detect them with special instruments — but they never accumulate because as soon as they are formed, they react further.

For example, in the mechanism:

Step 1: A + B → X (X is formed here)
Step 2: X + C → D (X is consumed here)

The species X is an intermediate. It appears in Step 1 as a product and in Step 2 as a reactant. When you add the two steps (A + B + X + C → X + D), X cancels, giving A + B + C → D.

---

## 2. The Rate-Determining Step

### What This Concept Is and Why It Matters

In any multi-step mechanism, the different elementary steps may happen at different speeds. One step will be slower than all the others. This slowest step is called the **rate-determining step** (often abbreviated RDS). It acts like a bottleneck: the overall reaction cannot go any faster than this slowest step.

A useful analogy is a multi-lane highway that narrows to a single lane. No matter how fast cars travel on the wide section, the rate at which cars pass through the whole road is limited by how fast they can get through the single-lane bottleneck. Similarly, no matter how fast the other steps in a mechanism are, the overall rate is limited by the rate of the slowest step.

### The Rate Law of the Overall Reaction

This is the most important practical consequence of the rate-determining step concept: the rate law for the overall reaction is determined by the molecularity of the rate-determining step.

Here is what that means in practice. If the slowest step in a mechanism is a single elementary reaction, then the rate law for the overall reaction matches the rate law you would write for that elementary step based on its molecularity:

- If the RDS is A → products (one molecule decomposing): Rate = k[A]
- If the RDS is A + B → products (two molecules colliding): Rate = k[A][B]
- If the RDS is 2A → products (two identical molecules colliding): Rate = k[A]²

Intermediates that appear in the rate-determining step must be expressed in terms of reactants using equilibrium relationships from fast, reversible steps that precede the RDS. But for most problems at this level, the RDS directly involves only reactants.

### Worked Example 1: Testing a Mechanism Against Experimental Rate Data

**Problem:** The reaction 2NO(g) + O₂(g) → 2NO₂(g) has been studied experimentally. The experimentally determined rate law is Rate = k[NO]²[O₂]. Two possible mechanisms are proposed:

**Mechanism A** (single step): 2NO + O₂ → 2NO₂

**Mechanism B** (two steps):
Step 1 (slow): 2NO → N₂O₂
Step 2 (fast): N₂O₂ + O₂ → 2NO₂

Determine which mechanism is consistent with the experimental rate law.

**Strategy:** For each mechanism, we identify the rate-determining step (or treat the only step as the RDS) and write the rate law it predicts. Then we compare with the experimental rate law.

**Solution:**

**Mechanism A:** This mechanism has only one step, so that step is necessarily the rate-determining step. It is an elementary step involving two NO molecules and one O₂ molecule colliding simultaneously. The rate law for an elementary step is determined by the stoichiometric coefficients of the reactants in that step: Rate = k[NO]²[O₂]. This matches the experimental rate law exactly. So Mechanism A is consistent with the data.

**Mechanism B:** The slow step is Step 1, which is the rate-determining step. Step 1 involves two NO molecules colliding: 2NO → N₂O₂. Since this is an elementary step, the rate law is Rate = k[NO]². This predicted rate law does not include [O₂], but the experimental rate law does include [O₂]. Therefore, Mechanism B predicts a rate law that does not match experiment. Mechanism B is not consistent.

**Why this makes sense:** Mechanism B would predict that changing the O₂ concentration has no effect on the rate, but experiments show that doubling [O₂] doubles the rate. Mechanism A correctly captures that all three molecules are involved in the crucial collision.

A note of caution: a single-step, three-molecule (termolecular) collision like Mechanism A is statistically very unlikely, and in reality this reaction probably proceeds through a more complex mechanism involving a pre-equilibrium. But for the purpose of this problem, Mechanism A is the one consistent with the data.

### Worked Example 2: Proposing a Mechanism from a Rate Law

**Problem:** The reaction (CH₃)₃CBr + OH⁻ → (CH₃)₃COH + Br⁻ has been studied. The experimentally determined rate law is Rate = k[(CH₃)₃CBr]. Notably, the concentration of OH⁻ does not appear in the rate law — the reaction is zero order with respect to OH⁻. Propose a two-step mechanism that is consistent with this rate law, and clearly identify the rate-determining step and any intermediates.

**Strategy:** Since the rate law is first order in (CH₃)₃CBr and zero order in OH⁻, the rate-determining step must involve only (CH₃)₃CBr. The OH⁻ must participate only in a fast step that occurs after the RDS.

**Solution:**

**Step 1 (slow, rate-determining):** (CH₃)₃CBr → (CH₃)₃C⁺ + Br⁻

This is a unimolecular step: one molecule of (CH₃)₃CBr breaks apart to form a positively charged carbocation intermediate, (CH₃)₃C⁺, and a bromide ion. The rate law for this elementary step is Rate = k[(CH₃)₃CBr], which matches the experimental rate law.

**Step 2 (fast):** (CH₃)₃C⁺ + OH⁻ → (CH₃)₃COH

The carbocation intermediate, once formed, reacts rapidly with any available OH⁻ ion to form the final alcohol product. Since this step is fast, it does not limit the overall rate.

The intermediate in this mechanism is (CH₃)₃C⁺. It is produced in Step 1 and consumed in Step 2, so it cancels out when the steps are added: (CH₃)₃CBr + OH⁻ → (CH₃)₃COH + Br⁻. This matches the overall reaction.

**Why this makes sense:** Because the slow step does not involve OH⁻, adding more OH⁻ cannot speed up the overall reaction — you are limited by how fast (CH₃)₃CBr falls apart, and that does not depend on OH⁻. This is the classic S_N1 mechanism.

---

## 3. Molecularity

### What This Concept Is and Why It Matters

Molecularity is a number that describes how many particles (molecules, atoms, or ions) come together and interact in a single elementary step. It applies only to elementary steps, not to overall reactions.

**Unimolecular:** One particle undergoes a change by itself — for example, a molecule breaks apart or rearranges its atoms. Example: Br₂ → 2Br•. The rate law is Rate = k[Br₂].

**Bimolecular:** Two particles collide and react. This is the most common type of elementary step. Example: H₂ + I• → HI + H•. The rate law is Rate = k[H₂][I•].

**Termolecular:** Three particles collide simultaneously and react. This is extremely rare because the probability of three particles all coming together at exactly the same instant with the right energy and orientation is vanishingly small. If a balanced equation seems to need three molecules, the reaction almost certainly proceeds through a sequence of bimolecular steps (or a bimolecular step followed by a fast unimolecular step), not a single termolecular step.

---

## 4. The Arrhenius Equation

### What This Concept Is and Why It Matters

We know from the previous lessons that the rate of a reaction depends dramatically on temperature, and that the rate constant k changes with temperature. But what is the precise mathematical relationship? The Arrhenius equation, discovered by the Swedish chemist Svante Arrhenius in 1889, gives us this relationship. It is one of the most important equations in all of chemical kinetics.

### The Exponential Form

The Arrhenius equation is:

\[
k = A e^{-E_a / RT}
\]

Let us define each symbol:

- **k** is the rate constant at temperature T.
- **A** is the pre-exponential factor (also called the frequency factor or the Arrhenius constant). It represents the frequency of collisions multiplied by the probability that those collisions have the correct orientation. A has the same units as k.
- **e** is the base of natural logarithms, approximately equal to 2.718.
- **Ea** is the activation energy, measured in joules per mole (J mol⁻¹). It is the minimum energy that colliding particles must have for a reaction to occur.
- **R** is the gas constant, which has the value 8.31 J K⁻¹ mol⁻¹. This constant appears because we are dealing with energy on a per-mole basis.
- **T** is the absolute temperature in kelvin (K).

The term e^(−Ea/RT) is a fraction between 0 and 1. It represents the fraction of collisions that have sufficient energy to overcome the activation barrier. When Ea is large, this fraction is very small. When T is large, this fraction is larger.

### The Linear Form

Taking the natural logarithm (ln) of both sides of the Arrhenius equation gives:

\[
\ln k = \ln A - \frac{E_a}{RT}
\]

This can be rearranged to:

\[
\ln k = -\frac{E_a}{R} \cdot \frac{1}{T} + \ln A
\]

This has the form of a straight line: y = mx + c.

- y is ln k (what we plot on the vertical axis).
- x is 1/T (what we plot on the horizontal axis).
- m, the gradient (slope), is −Ea/R.
- c, the y-intercept, is ln A.

If you measure k at several different temperatures, plot ln k against 1/T, and find the gradient of the best-fit line, you can calculate Ea by multiplying the gradient by −R.

### The Two-Point Form

If you only have rate constants at two different temperatures (T₁ and T₂), you can use this form:

\[
\ln\left(\frac{k_2}{k_1}\right) = \frac{E_a}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right)
\]

This equation is derived by writing the linear form at two temperatures and subtracting. It allows you to find Ea without needing a full graph.

### Worked Example 3: Finding Ea from Two Temperatures

**Problem:** The rate constant for a chemical reaction is measured at two temperatures. At 300 K, k = 1.00 × 10⁻³ s⁻¹. At 310 K, k = 2.00 × 10⁻³ s⁻¹. Calculate the activation energy Ea for this reaction. Use R = 8.31 J K⁻¹ mol⁻¹.

**Strategy:** We use the two-point Arrhenius equation. We know k₁, k₂, T₁, and T₂. We need to find Ea.

**Solution:**

First, identify the values: k₁ = 1.00 × 10⁻³ s⁻¹ at T₁ = 300 K; k₂ = 2.00 × 10⁻³ s⁻¹ at T₂ = 310 K. Note that k₂/k₁ = 2.00 (the rate constant doubles).

Now apply the two-point equation:

\[
\ln\left(\frac{k_2}{k_1}\right) = \frac{E_a}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right)
\]

Substitute the numbers:

\[
\ln(2.00) = \frac{E_a}{8.31}\left(\frac{1}{300} - \frac{1}{310}\right)
\]

Calculate ln(2.00) = 0.693.

Calculate the temperature difference term:

\[
\frac{1}{300} - \frac{1}{310} = \frac{310 - 300}{300 \times 310} = \frac{10}{93000} = 1.075 \times 10^{-4} \text{ K}^{-1}
\]

Now substitute:

\[
0.693 = \frac{E_a}{8.31} \times 1.075 \times 10^{-4}
\]

\[
E_a = \frac{0.693 \times 8.31}{1.075 \times 10^{-4}} = \frac{5.759}{1.075 \times 10^{-4}} = 53600 \text{ J mol}^{-1}
\]

Convert to kJ mol⁻¹ by dividing by 1000: **Ea = 53.6 kJ mol⁻¹**.

**Why this makes sense:** An activation energy around 50 kJ mol⁻¹ is fairly typical for a reaction that proceeds at a moderate rate near room temperature. The doubling of k for a 10 K rise is also a typical observation that corresponds to Ea values in the 50–60 kJ mol⁻¹ range.

### Worked Example 4: Predicting k at a New Temperature

**Problem:** For a certain decomposition reaction, the rate constant k is measured as 1.0 × 10⁻³ s⁻¹ at 298 K and as 3.0 × 10⁻³ s⁻¹ at 308 K. (a) Calculate the activation energy Ea. (b) Predict the value of the rate constant at 318 K.

**Strategy:** Part (a) uses the two-point equation as in the previous example. Part (b) uses the same equation again, but this time we know Ea and we want k at a new temperature.

**Solution, part (a):**

k₁ = 1.0 × 10⁻³ s⁻¹, T₁ = 298 K; k₂ = 3.0 × 10⁻³ s⁻¹, T₂ = 308 K.

\[
\ln\left(\frac{3.0 \times 10^{-3}}{1.0 \times 10^{-3}}\right) = \ln(3.0) = 1.099
\]

\[
\frac{1}{298} - \frac{1}{308} = \frac{308 - 298}{298 \times 308} = \frac{10}{91784} = 1.090 \times 10^{-4} \text{ K}^{-1}
\]

\[
1.099 = \frac{E_a}{8.31} \times 1.090 \times 10^{-4}
\]

\[
E_a = \frac{1.099 \times 8.31}{1.090 \times 10^{-4}} = \frac{9.133}{1.090 \times 10^{-4}} = 83800 \text{ J mol}^{-1} = 83.8 \text{ kJ mol}^{-1}
\]

**Solution, part (b):** Now use T₁ = 298 K, k₁ = 1.0 × 10⁻³ s⁻¹, T₂ = 318 K, and the Ea we just calculated.

\[
\frac{1}{298} - \frac{1}{318} = \frac{318 - 298}{298 \times 318} = \frac{20}{94764} = 2.111 \times 10^{-4} \text{ K}^{-1}
\]

\[
\ln\left(\frac{k_{318}}{1.0 \times 10^{-3}}\right) = \frac{83800}{8.31} \times 2.111 \times 10^{-4}
\]

\[
\frac{83800}{8.31} = 10084
\]

\[
\ln\left(\frac{k_{318}}{1.0 \times 10^{-3}}\right) = 10084 \times 2.111 \times 10^{-4} = 2.129
\]

\[
\frac{k_{318}}{1.0 \times 10^{-3}} = e^{2.129} = 8.41
\]

\[
k_{318} = 8.41 \times 1.0 \times 10^{-3} = 8.4 \times 10^{-3} \text{ s}^{-1}
\]

**Why this makes sense:** Going from 298 K to 308 K (10 K rise) roughly tripled k. Going another 10 K to 318 K roughly triples it again (1.0 → 3.0 → 8.4). This "rule of thumb" — that k increases by a factor of 2 to 3 for each 10 K rise near room temperature — holds for reactions with Ea in the 50–100 kJ mol⁻¹ range.

---

## Practice Problems

1. The gas-phase reaction 2NO₂Cl(g) → 2NO₂(g) + Cl₂(g) has been studied experimentally. The experimentally determined rate law is Rate = k[NO₂Cl], which means the reaction is first order with respect to NO₂Cl. Propose a two-step mechanism that is consistent with this rate law. For your mechanism, clearly identify the rate-determining step and label any reaction intermediates.

2. A student proposes two mechanisms for a reaction that has the experimental rate law Rate = k[A][B]².

   **Mechanism 1** (single step): A + 2B → products

   **Mechanism 2** (two steps):
   Step 1 (slow): A + B → C
   Step 2 (fast): C + B → products

   For each mechanism, write the rate law that the mechanism predicts. Determine which mechanism is consistent with the experimental rate law, and explain your reasoning.

3. The rate constant for a reaction is measured as 2.5 × 10⁻⁴ s⁻¹ at 298 K and as 1.0 × 10⁻³ s⁻¹ at 308 K. Calculate the activation energy Ea for this reaction in kJ mol⁻¹. The gas constant R has the value 8.31 J K⁻¹ mol⁻¹.

4. A chemist measures the rate constant k for a reaction at four different temperatures and obtains the following results:

   | T / K   | 290  | 300  | 310  | 320  |
   |---------|------|------|------|------|
   | k / s⁻¹ | 0.50 × 10⁻³ | 1.40 × 10⁻³ | 3.60 × 10⁻³ | 8.70 × 10⁻³ |

   Describe in detail how the chemist could determine the activation energy of this reaction graphically. State exactly what quantities should be plotted on each axis, what shape the graph should have, what the gradient represents, and how Ea is calculated from the gradient.

5. **(IB-Exam Style)** The hydrolysis of an organic ester in alkaline solution was studied at several temperatures. The reaction is first order with respect to the ester. The rate constant k was measured at different temperatures, and the results are shown below.

   | T / K | 290    | 300    | 310    | 320    |
   |-------|--------|--------|--------|--------|
   | k / 10⁻³ s⁻¹ | 0.50   | 1.40   | 3.60   | 8.70   |

   (a) Explain, using the Arrhenius equation k = A e^(−Ea/RT), why the rate constant k increases when the temperature is raised. Your explanation should refer to the mathematical form of the equation.

   (b) Using only the data at 290 K and 320 K, calculate the activation energy Ea for this reaction. Express your answer in kJ mol⁻¹. The value of the gas constant R is 8.31 J K⁻¹ mol⁻¹.

   (c) Using the value of Ea you calculated in part (b), predict the value of the rate constant k at a temperature of 330 K.

   (d) A student studying this reaction proposes a mechanism consisting of a fast first step followed by a slow second step. State which step is the rate-determining step, and explain how the overall rate law is related to the molecularity of this step. The student also suggests that an intermediate is formed. Explain what an intermediate is and why it does not appear in the overall balanced equation for the reaction.

---

## Answers

### Answer 1

Since the experimental rate law is Rate = k[NO₂Cl] — first order with only one reactant molecule appearing — the rate-determining step must be a unimolecular step involving only NO₂Cl. A consistent two-step mechanism is:

**Step 1 (slow, rate-determining):** NO₂Cl → NO₂ + Cl•. This is unimolecular and has the rate law Rate = k[NO₂Cl], matching the experimental data.

**Step 2 (fast):** NO₂Cl + Cl• → NO₂ + Cl₂. The chlorine atom (Cl•) produced in Step 1 rapidly attacks another NO₂Cl molecule.

When the two steps are added: NO₂Cl + NO₂Cl + Cl• → NO₂ + Cl• + NO₂ + Cl₂. The Cl• cancels (it is formed in Step 1 and consumed in Step 2), leaving 2NO₂Cl → 2NO₂ + Cl₂, which matches the overall reaction. The intermediate is the chlorine atom, Cl•.

### Answer 2

**Mechanism 1:** This is a single-step mechanism, so that step is the rate-determining step. For a single elementary step A + 2B → products, the rate law is determined by the molecularity: Rate = k[A][B]². This matches the experimental rate law exactly.

**Mechanism 2:** The slow step (Step 1) is the rate-determining step: A + B → C. Being bimolecular, the rate law is Rate = k[A][B]. This predicts first order in B, but the experimental rate law shows second order in B. Therefore, Mechanism 2 is **not consistent** with the experimental data.

Only Mechanism 1 is consistent. However, a termolecular elementary step (three particles colliding simultaneously) is statistically very unlikely. In reality, a reaction with this rate law probably proceeds through a pre-equilibrium mechanism (a fast equilibrium forming an intermediate, followed by a slow step). But for the purposes of this question, Mechanism 1 is the one that matches.

### Answer 3

Use the two-point Arrhenius equation. k₁ = 2.5 × 10⁻⁴ s⁻¹ at T₁ = 298 K; k₂ = 1.0 × 10⁻³ s⁻¹ at T₂ = 308 K. The ratio k₂/k₁ = (1.0 × 10⁻³) / (2.5 × 10⁻⁴) = 4.0.

ln(4.0) = 1.386.

1/T₁ − 1/T₂ = 1/298 − 1/308 = (308 − 298) / (298 × 308) = 10 / 91784 = 1.090 × 10⁻⁴ K⁻¹.

1.386 = (Ea / 8.31) × 1.090 × 10⁻⁴.

Ea = (1.386 × 8.31) / (1.090 × 10⁻⁴) = 11.52 / (1.090 × 10⁻⁴) = 105700 J mol⁻¹ = **106 kJ mol⁻¹** (to three significant figures).

### Answer 4

The chemist should plot ln k on the vertical y-axis against 1/T on the horizontal x-axis. First, the chemist needs to calculate ln k for each temperature (taking the natural logarithm of each k value) and 1/T for each temperature (dividing 1 by each T value in kelvin). The four data points should then be plotted. According to the linear form of the Arrhenius equation, ln k = −(Ea/R)(1/T) + ln A, this plot should produce a straight line. The gradient (slope) of this straight line is equal to −Ea/R. To find Ea, the chemist calculates the gradient from the best-fit line (gradient = Δ(ln k) / Δ(1/T)) and then multiplies the gradient by −R: Ea = −gradient × R. The y-intercept of the line gives ln A, from which the pre-exponential factor A can be found by taking e^(y-intercept). This graphical method is more reliable than using just two points because it uses all the data and averages out experimental errors.

### Answer 5

**(a)** The Arrhenius equation k = A e^(−Ea/RT) contains the term e^(−Ea/RT). The exponent is −Ea/(RT). As T (the denominator of the denominator) increases, the value of Ea/(RT) becomes smaller. Since there is a negative sign in front, −Ea/(RT) becomes less negative — it moves closer to zero from below. The exponential function e^x increases as x increases (becomes less negative), so e^(−Ea/RT) becomes larger. Since k = A multiplied by this exponential factor, and A is essentially constant with respect to temperature, k increases. Physically, this means that at higher temperatures, a larger fraction of molecular collisions have energy greater than or equal to Ea, so the reaction proceeds faster.

**(b)** k₁ = 0.50 × 10⁻³ s⁻¹ at T₁ = 290 K; k₂ = 8.70 × 10⁻³ s⁻¹ at T₂ = 320 K. The ratio k₂/k₁ = 8.70 / 0.50 = 17.4.

ln(17.4) = 2.856.

1/T₁ − 1/T₂ = 1/290 − 1/320 = (320 − 290) / (290 × 320) = 30 / 92800 = 3.233 × 10⁻⁴ K⁻¹.

2.856 = (Ea / 8.31) × 3.233 × 10⁻⁴.

Ea = (2.856 × 8.31) / (3.233 × 10⁻⁴) = 23.73 / (3.233 × 10⁻⁴) = 73400 J mol⁻¹ = **73.4 kJ mol⁻¹**.

**(c)** Use T₁ = 290 K (where k₁ = 0.50 × 10⁻³ s⁻¹) and T₂ = 330 K, with Ea = 73.4 kJ mol⁻¹ = 73400 J mol⁻¹.

1/T₁ − 1/T₂ = 1/290 − 1/330 = (330 − 290) / (290 × 330) = 40 / 95700 = 4.180 × 10⁻⁴ K⁻¹.

ln(k₃₃₀ / 0.50 × 10⁻³) = (73400 / 8.31) × 4.180 × 10⁻⁴ = 8833 × 4.180 × 10⁻⁴ = 3.692.

k₃₃₀ / 0.50 × 10⁻³ = e^3.692 = 40.1.

k₃₃₀ = 40.1 × 0.50 × 10⁻³ = **2.01 × 10⁻² s⁻¹** (approximately 2.0 × 10⁻² s⁻¹).

**(d)** The rate-determining step is the slow second step, because the rate-determining step is always the slowest step in a mechanism. The overall rate law is determined by the molecularity of this slow step. If the slow step is, for example, a reaction between the intermediate (call it X) and water, the rate law would be Rate = k[X][H₂O]. However, since X is an intermediate (it does not appear in the overall equation), its concentration must be expressed in terms of the reactants using the equilibrium constant of the fast first step. An intermediate is a species that is produced in one elementary step of a mechanism and consumed in a subsequent elementary step. It does not appear in the overall balanced equation because when all the elementary steps of the mechanism are added together, the intermediate appears as both a product (in one step) and a reactant (in another step), and thus cancels out algebraically.
