# Lesson 21: Rate Equations, Orders of Reaction, and Rate Constant (HL)

## What You'll Learn
- Write a rate equation (rate law) for a chemical reaction and explain what each symbol means
- Define the terms "order of reaction" and "overall order"
- Determine orders of reaction from experimental data using the method of initial rates
- Calculate the rate constant k from experimental data and determine its units
- Interpret concentration-time graphs and rate-concentration graphs for zero, first, and second order reactions

---

## 1. The Rate Equation

### What This Concept Is and Why It Matters

So far we have described reaction rates in qualitative terms: "higher temperature makes the reaction faster." But chemists need to be able to make precise quantitative predictions: "If I double the concentration of this reactant, exactly how much faster will the reaction go?" The rate equation — also called the rate law — is the mathematical tool that answers this question. It connects the concentrations of reactants to the measured rate.

For any reaction, the rate equation is determined by experiment. You cannot predict it just by looking at the balanced chemical equation. The one exception is for reactions that happen in a single step, which we will study in the next lesson.

### The General Form of a Rate Equation

Consider a reaction where substances A and B react to form products:

\[
\text{A} + \text{B} \rightarrow \text{products}
\]

The rate equation for this reaction has the following general form:

\[
\text{Rate} = k[\text{A}]^m[\text{B}]^n
\]

Let us define each symbol carefully:

- **Rate** is the speed of the reaction, measured in mol dm⁻³ s⁻¹ (change of concentration per second).
- **k** is the rate constant. This is a number that is specific to a particular reaction at a particular temperature. The value of k changes if you change the temperature, but it does not depend on the concentrations of reactants. A large k means a fast reaction; a small k means a slow reaction.
- **[A]** and **[B]** are the concentrations of the reactants in mol dm⁻³. The square brackets always mean "concentration of."
- **m** is the order of reaction with respect to reactant A. It tells you how the rate depends on the concentration of A.
- **n** is the order of reaction with respect to reactant B. It tells you how the rate depends on the concentration of B.
- The sum **m + n** is called the overall order of the reaction.

### What the Orders Mean Numerically

The order with respect to a particular reactant (m or n) is almost always 0, 1, or 2. Here is what each value means in practical terms:

**Zero order (m = 0):** The rate does not depend on the concentration of that reactant at all. If you double [A], triple [A], or halve [A], the rate stays exactly the same. Mathematically, anything raised to the power 0 equals 1, so [A]⁰ = 1 and the rate equation simply becomes Rate = k[B]ⁿ — the term for A disappears.

**First order (m = 1):** The rate is directly proportional to the concentration of that reactant. If you double [A], the rate doubles. If you triple [A], the rate triples. If you halve [A], the rate halves.

**Second order (m = 2):** The rate is proportional to the square of the concentration of that reactant. If you double [A], the rate quadruples (2² = 4). If you triple [A], the rate increases by a factor of 9 (3² = 9). If you halve [A], the rate becomes one-quarter of its original value.

The orders m and n are not the same as the stoichiometric coefficients in the balanced equation. For the reaction 2NO + O₂ → 2NO₂, you might guess that the rate equation is Rate = k[NO]²[O₂]. In this particular case, the guess happens to be correct — but this is a coincidence. For many reactions, the orders are completely different from the stoichiometric coefficients. That is why we do not guess: we measure.

---

## 2. Determining Orders: The Method of Initial Rates

### What This Concept Is and Why It Matters

To find the rate equation for a reaction, we need to measure how the rate changes when we change the concentration of each reactant, one at a time. The method of initial rates is the standard experimental approach. We measure the rate right at the beginning of the reaction (the "initial rate") for several different starting concentrations. By comparing experiments where only one concentration changes, we can deduce each order.

### The Logic of Comparison

Imagine we have two experiments. In Experiment 1, we use certain starting concentrations and measure the initial rate. In Experiment 2, we double [A] while keeping [B] the same as in Experiment 1. Then we compare the rates:

- If the rate does not change → order with respect to A is 0 (zero order).
- If the rate doubles → order with respect to A is 1 (first order).
- If the rate quadruples → order with respect to A is 2 (second order).
- If the rate increases by a factor of 8 → order with respect to A is 3 (third order — rare).

The same logic applies for B: find two experiments where [B] changes but [A] stays constant.

### Worked Example 1: Finding Orders and Rate Equation from Data

**Problem:** A reaction between substances A and B was studied by measuring the initial rate at different starting concentrations. The results are shown in the table below.

| Experiment | [A] / mol dm⁻³ | [B] / mol dm⁻³ | Initial rate / mol dm⁻³ s⁻¹ |
|------------|----------------|----------------|---------------------------|
| 1          | 0.10           | 0.10           | 2.0 × 10⁻⁴              |
| 2          | 0.20           | 0.10           | 4.0 × 10⁻⁴              |
| 3          | 0.10           | 0.30           | 6.0 × 10⁻⁴              |

(a) Determine the order of reaction with respect to A, explaining your reasoning.
(b) Determine the order of reaction with respect to B, explaining your reasoning.
(c) Write the rate equation for this reaction.
(d) Calculate the value of the rate constant k, including its units.

**Strategy:** We need to find pairs of experiments where one concentration changes and the other does not. Then we compare how the rate changes and deduce the order.

**Solution, part (a):** To find the order with respect to A, we need two experiments where [A] changes but [B] stays the same. Looking at the table, Experiment 1 and Experiment 2 satisfy this: [A] changes from 0.10 to 0.20 (doubles), while [B] stays at 0.10 in both experiments.

Now compare the rates: In Experiment 1, rate = 2.0 × 10⁻⁴. In Experiment 2, rate = 4.0 × 10⁻⁴. The rate has increased from 2.0 × 10⁻⁴ to 4.0 × 10⁻⁴ — it has doubled.

Since doubling [A] caused the rate to double, the order with respect to A is **1** (first order).

**Solution, part (b):** To find the order with respect to B, we look for two experiments where [B] changes but [A] stays the same. Experiment 1 and Experiment 3 satisfy this: [B] changes from 0.10 to 0.30 (triples), while [A] stays at 0.10 in both.

Now compare the rates: In Experiment 1, rate = 2.0 × 10⁻⁴. In Experiment 3, rate = 6.0 × 10⁻⁴. The rate has increased from 2.0 × 10⁻⁴ to 6.0 × 10⁻⁴ — it has tripled.

Since tripling [B] caused the rate to triple, the order with respect to B is **1** (first order).

**Solution, part (c):** Now we can write the rate equation. With m = 1 and n = 1:

\[
\text{Rate} = k[\text{A}]^1[\text{B}]^1 = k[\text{A}][\text{B}]
\]

The overall order is 1 + 1 = 2.

**Solution, part (d):** To find k, we rearrange the rate equation:

\[
k = \frac{\text{Rate}}{[\text{A}][\text{B}]}
\]

We can use the data from any experiment. Let us use Experiment 1:

\[
k = \frac{2.0 \times 10^{-4} \text{ mol dm}^{-3} \text{ s}^{-1}}{(0.10 \text{ mol dm}^{-3})(0.10 \text{ mol dm}^{-3})}
\]

\[
k = \frac{2.0 \times 10^{-4}}{0.010} = 2.0 \times 10^{-2}
\]

Now for the units. The rate has units of mol dm⁻³ s⁻¹. The denominator [A][B] has units of (mol dm⁻³)(mol dm⁻³) = (mol dm⁻³)² = mol² dm⁻⁶. So:

\[
\text{Units of } k = \frac{\text{mol dm}^{-3} \text{ s}^{-1}}{\text{mol}^2 \text{ dm}^{-6}} = \text{mol}^{-1} \text{ dm}^3 \text{ s}^{-1}
\]

We write this as dm³ mol⁻¹ s⁻¹. The full answer is: **k = 2.0 × 10⁻² dm³ mol⁻¹ s⁻¹**.

**Why this makes sense:** A first-order dependence on each reactant means doubling either one doubles the rate. The units dm³ mol⁻¹ s⁻¹ are the expected units for a second-order rate constant.

---

## 3. Units of the Rate Constant k

### What This Concept Is and Why It Matters

The rate constant k does not always have the same units. Its units change depending on the overall order of the reaction. This is because the rate itself always has units of mol dm⁻³ s⁻¹, but the concentration terms multiplied together have different total units depending on how many of them there are.

Here is a systematic way to find the units of k for any overall order. Let the overall order be p (so p = m + n + ...). Then:

\[
k = \frac{\text{Rate}}{(\text{concentration})^p}
\]

The units are:

\[
\text{Units of } k = \frac{\text{mol dm}^{-3} \text{ s}^{-1}}{(\text{mol dm}^{-3})^p} = (\text{mol dm}^{-3})^{1-p} \text{ s}^{-1}
\]

Applying this formula:

- For overall order 0 (p = 0): units = (mol dm⁻³)¹ s⁻¹ = **mol dm⁻³ s⁻¹**
- For overall order 1 (p = 1): units = (mol dm⁻³)⁰ s⁻¹ = **s⁻¹**
- For overall order 2 (p = 2): units = (mol dm⁻³)⁻¹ s⁻¹ = **dm³ mol⁻¹ s⁻¹**
- For overall order 3 (p = 3): units = (mol dm⁻³)⁻² s⁻¹ = **dm⁶ mol⁻² s⁻¹**

You can check your work by making sure the units of k, when multiplied by the concentration terms in the rate equation, produce mol dm⁻³ s⁻¹.

---

## 4. Graphical Determination of Reaction Order

### What This Concept Is and Why It Matters

Sometimes you are not given a neat table of initial rates. Instead, you might have a graph showing how the concentration of a reactant changes over time, or how the rate changes with concentration. The shape of these graphs reveals the order of reaction.

### Concentration-Time Graphs

These graphs plot the concentration of a reactant on the y-axis against time on the x-axis.

**Zero order:** The graph is a straight line with a constant negative gradient. The concentration falls at a steady rate. The gradient of this line equals −k (the negative of the rate constant).

**First order:** The graph is a curve that is steep at first and then gradually flattens out. The key diagnostic feature of a first-order reaction is that the **half-life is constant**. The half-life (t₁/₂) is the time it takes for the concentration of the reactant to fall to half of its starting value. For a first-order reaction, it takes the same amount of time to go from 100% to 50% as it does to go from 50% to 25%, and from 25% to 12.5%, and so on. The half-life does not depend on the starting concentration. The relationship is: t₁/₂ = ln 2 / k, where ln 2 ≈ 0.693.

**Second order:** The graph is an even steeper curve that flattens out. For a second-order reaction, the half-life is not constant — it gets longer as the concentration drops. If you start with a high concentration, the half-life is short. If you start with a low concentration, the half-life is long. Specifically, t₁/₂ = 1/(k[A]₀), where [A]₀ is the starting concentration.

### Rate-Concentration Graphs

These graphs plot the rate on the y-axis against the concentration of a reactant on the x-axis.

**Zero order:** The graph is a horizontal line. The rate does not change no matter what the concentration is.

**First order:** The graph is a straight line passing through the origin. The rate is directly proportional to concentration.

**Second order:** The graph is a curve that bends upward (a parabola). The rate increases faster than the concentration increases.

### Worked Example 2: Using Half-Life to Determine Order

**Problem:** A student studies the decomposition of a compound X. When the student starts with [X] = 0.40 mol dm⁻³, the half-life is measured as 80 seconds. When the student performs a second experiment starting with [X] = 0.20 mol dm⁻³, the half-life is again 80 seconds. Determine the order of reaction with respect to X and calculate the rate constant k.

**Strategy:** The half-life being the same at two different starting concentrations is the defining characteristic of a first-order reaction. We then use the first-order half-life formula.

**Solution:** Since t₁/₂ = 80 s regardless of whether [X]₀ = 0.40 mol dm⁻³ or 0.20 mol dm⁻³, the half-life is independent of initial concentration. This means the reaction is **first order** with respect to X.

For a first-order reaction, the rate constant k is related to the half-life by:

\[
k = \frac{\ln 2}{t_{1/2}} = \frac{0.693}{80 \text{ s}} = 8.66 \times 10^{-3} \text{ s}^{-1}
\]

**Why this makes sense:** The units are s⁻¹, which are the correct units for a first-order rate constant. And 0.693/80 gives a small number, which is typical for a reaction that takes over a minute to reach half completion.

### Worked Example 3: Using the Integrated Rate Law for First Order

**Problem:** A first-order reaction starts with a reactant concentration of 0.800 mol dm⁻³. After 40 minutes, the concentration has dropped to 0.200 mol dm⁻³. Calculate the rate constant k. Also calculate the half-life.

**Strategy:** For a first-order reaction, the integrated rate law is ln([A]/[A]₀) = −kt. We substitute the known concentrations and time to find k. Then we use t₁/₂ = ln2/k.

**Solution:** The integrated first-order rate equation is:

\[
\ln\left(\frac{[A]}{[A]_0}\right) = -kt
\]

Substitute [A] = 0.200, [A]₀ = 0.800, and t = 40 minutes:

\[
\ln\left(\frac{0.200}{0.800}\right) = -k(40)
\]

\[
\ln(0.25) = -k(40)
\]

The natural logarithm of 0.25 is −1.386 (since e^−1.386 ≈ 0.25):

\[
-1.386 = -k(40)
\]

\[
k = \frac{1.386}{40} = 0.0347 \text{ min}^{-1}
\]

Now for the half-life:

\[
t_{1/2} = \frac{\ln 2}{k} = \frac{0.693}{0.0347 \text{ min}^{-1}} = 20.0 \text{ min}
\]

**Why this makes sense:** We can verify this result independently. Starting at 0.800, one half-life (20 min) should bring us to 0.400. Another half-life (another 20 min, total 40 min) should bring us to 0.200. That is exactly what the problem states — 40 minutes to go from 0.800 to 0.200, which is two half-lives. So our calculated half-life of 20 minutes is confirmed.

---

## Practice Problems

1. A student studies the reaction A + 2B → C by measuring initial rates at different starting concentrations. The data obtained are shown in the table below.

   | Experiment | [A] / mol dm⁻³ | [B] / mol dm⁻³ | Initial rate / mol dm⁻³ s⁻¹ |
   |------------|----------------|----------------|---------------------------|
   | 1          | 0.10           | 0.10           | 1.0 × 10⁻³              |
   | 2          | 0.20           | 0.10           | 2.0 × 10⁻³              |
   | 3          | 0.10           | 0.20           | 4.0 × 10⁻³              |

   (a) Determine the order of reaction with respect to A, explaining each step of your reasoning.
   (b) Determine the order of reaction with respect to B, explaining each step of your reasoning.
   (c) Write the rate equation for this reaction and state the overall order.
   (d) Calculate the rate constant k and determine its units.

2. A chemical reaction is found to obey first-order kinetics. The concentration of the reactant starts at 0.500 mol dm⁻³ and drops to 0.250 mol dm⁻³ over a period of 30 minutes. Calculate the rate constant k and the half-life of the reaction. Verify that your answer for the half-life is consistent with the information given in the problem.

3. A student measures the half-life of a reaction at two different starting concentrations. When the initial concentration of the reactant is 0.40 mol dm⁻³, the half-life is 100 seconds. When the initial concentration is 0.20 mol dm⁻³, the half-life is 200 seconds. Determine the order of this reaction. Explain your reasoning, making reference to how half-life depends on initial concentration for zero, first, and second order reactions.

4. A reaction is found to be zero order with respect to its only reactant. (a) Sketch a graph showing how the concentration of this reactant changes with time. Label both axes and indicate what the gradient represents. (b) On a separate set of axes, sketch a graph showing how the rate of reaction depends on the concentration of this reactant. Label both axes and explain the shape of your graph.

5. **(IB-Exam Style)** The reaction between nitrogen monoxide gas and oxygen gas produces nitrogen dioxide gas according to the following equation:

   \[
   2\text{NO}(\text{g}) + \text{O}_2(\text{g}) \rightarrow 2\text{NO}_2(\text{g})
   \]

   The reaction was studied at a fixed temperature by measuring the initial rate at various starting concentrations of the two reactants. The results are shown in the table below.

   | Experiment | [NO] / mol dm⁻³ | [O₂] / mol dm⁻³ | Initial rate / mol dm⁻³ s⁻¹ |
   |------------|-----------------|-----------------|---------------------------|
   | 1          | 0.010           | 0.010           | 2.5 × 10⁻⁵              |
   | 2          | 0.020           | 0.010           | 1.0 × 10⁻⁴              |
   | 3          | 0.010           | 0.020           | 5.0 × 10⁻⁵              |

   (a) Determine the order of reaction with respect to NO and the order with respect to O₂. For each, explain clearly how you used the data to reach your conclusion.

   (b) Write the rate equation for this reaction and state the overall order.

   (c) Using the data from any one experiment, calculate the value of the rate constant k. Include its units.

   (d) Using your rate equation, predict the initial rate of reaction when [NO] = 0.030 mol dm⁻³ and [O₂] = 0.040 mol dm⁻³ at the same temperature.

---

## Answers

### Answer 1

**(a)** To find the order with respect to A, compare Experiment 1 and Experiment 2. In these two experiments, [A] changes from 0.10 to 0.20 mol dm⁻³ (it doubles), while [B] remains constant at 0.10 mol dm⁻³. The rate changes from 1.0 × 10⁻³ to 2.0 × 10⁻³ mol dm⁻³ s⁻¹ — it also doubles. Since doubling the concentration of A causes the rate to double, the order with respect to A is 1 (first order).

**(b)** To find the order with respect to B, compare Experiment 1 and Experiment 3. In these two experiments, [B] changes from 0.10 to 0.20 mol dm⁻³ (it doubles), while [A] remains constant at 0.10 mol dm⁻³. The rate changes from 1.0 × 10⁻³ to 4.0 × 10⁻³ mol dm⁻³ s⁻¹ — it quadruples (multiplied by 4). Since doubling the concentration of B causes the rate to quadruple, the order with respect to B is 2 (second order). A common mistake here is to see the doubling and assume first order; always check the factor by which the rate changes.

**(c)** The rate equation is Rate = k[A]¹[B]² = k[A][B]². The overall order is 1 + 2 = 3.

**(d)** Using Experiment 1: k = Rate / ([A][B]²) = (1.0 × 10⁻³) / (0.10 × (0.10)²) = (1.0 × 10⁻³) / (0.10 × 0.010) = (1.0 × 10⁻³) / 0.0010 = 1.0. The units: Rate has units mol dm⁻³ s⁻¹. The denominator [A][B]² has units (mol dm⁻³)(mol dm⁻³)² = (mol dm⁻³)³ = mol³ dm⁻⁹. So k has units (mol dm⁻³ s⁻¹) / (mol³ dm⁻⁹) = mol⁻² dm⁶ s⁻¹ (or dm⁶ mol⁻² s⁻¹). The full answer is **k = 1.0 dm⁶ mol⁻² s⁻¹**.

### Answer 2

For a first-order reaction, we use the integrated rate law: ln([A]/[A]₀) = −kt. Substituting [A] = 0.250, [A]₀ = 0.500, and t = 30 minutes: ln(0.250/0.500) = −k(30). This is ln(0.5) = −k(30). The natural logarithm of 0.5 is −0.693, so −0.693 = −k(30) and k = 0.693/30 = **0.0231 min⁻¹**. The half-life is t₁/₂ = ln 2 / k = 0.693 / 0.0231 = **30.0 minutes**. This is consistent because the problem states that the concentration halved (from 0.500 to 0.250) in exactly 30 minutes — so the half-life must be 30 minutes.

### Answer 3

The half-life doubles when the initial concentration is halved. This behaviour — where the half-life is inversely proportional to the initial concentration — is characteristic of a **second-order** reaction. For a zero-order reaction, the half-life would be halved when the initial concentration is halved (t₁/₂ ∝ [A]₀). For a first-order reaction, the half-life would remain constant regardless of the initial concentration. For a second-order reaction, t₁/₂ = 1/(k[A]₀), so halving [A]₀ doubles t₁/₂ — exactly what the data show.

### Answer 4

**(a)** For a zero-order reaction, the concentration-time graph is a straight line with a constant negative gradient. The y-axis is labelled [A] / mol dm⁻³ and the x-axis is labelled Time / s. The line starts at the initial concentration [A]₀ on the y-axis and slopes downward at a constant angle until it reaches the x-axis (where [A] = 0). The gradient of this line is equal to −k, the negative of the rate constant. Because the gradient is constant, the rate (which is the absolute value of the gradient, k) does not change as the reactant is consumed.

**(b)** For a zero-order reaction, the rate-concentration graph is a horizontal line. The y-axis is labelled Rate / mol dm⁻³ s⁻¹ and the x-axis is labelled [A] / mol dm⁻³. The line is parallel to the x-axis at a height equal to k. This shows that the rate remains constant regardless of the concentration of A. No matter how much A is present, the reaction proceeds at the same speed. This is unusual but can happen when a catalyst is saturated or when the reaction rate is limited by something other than the concentration of A (for example, by the availability of light in a photochemical reaction).

### Answer 5

**(a)** For the order with respect to NO: Compare Experiment 1 and Experiment 2. In these experiments, [NO] changes from 0.010 to 0.020 mol dm⁻³ (it doubles), while [O₂] remains constant at 0.010 mol dm⁻³. The rate changes from 2.5 × 10⁻⁵ to 1.0 × 10⁻⁴. The factor by which the rate increases is (1.0 × 10⁻⁴) / (2.5 × 10⁻⁵) = 4. The rate quadruples when [NO] doubles. Since 2² = 4, the order with respect to NO is **2** (second order).

For the order with respect to O₂: Compare Experiment 1 and Experiment 3. In these experiments, [O₂] changes from 0.010 to 0.020 mol dm⁻³ (it doubles), while [NO] remains constant at 0.010 mol dm⁻³. The rate changes from 2.5 × 10⁻⁵ to 5.0 × 10⁻⁵ — it doubles. Since doubling [O₂] doubles the rate, the order with respect to O₂ is **1** (first order).

**(b)** The rate equation is Rate = k[NO]²[O₂]. The overall order is 2 + 1 = 3.

**(c)** Using Experiment 1: k = Rate / ([NO]²[O₂]) = (2.5 × 10⁻⁵) / ((0.010)² × 0.010) = (2.5 × 10⁻⁵) / (0.0001 × 0.010) = (2.5 × 10⁻⁵) / (1.0 × 10⁻⁶) = 25. For the units: the denominator (mol dm⁻³)² × (mol dm⁻³) = (mol dm⁻³)³. So k has units = (mol dm⁻³ s⁻¹) / (mol dm⁻³)³ = mol⁻² dm⁶ s⁻¹ (or dm⁶ mol⁻² s⁻¹). The answer is **k = 25 dm⁶ mol⁻² s⁻¹**.

**(d)** Using the rate equation Rate = k[NO]²[O₂] with k = 25, [NO] = 0.030, and [O₂] = 0.040: Rate = 25 × (0.030)² × 0.040 = 25 × 0.0009 × 0.040 = 25 × 3.6 × 10⁻⁵ = 9.0 × 10⁻⁴. The predicted initial rate is **9.0 × 10⁻⁴ mol dm⁻³ s⁻¹**. Note that this is much larger than any of the individual experimental rates because both reactant concentrations have been increased.
