# Lesson 64: Radioactive Decay 1 — Random Nature, Activity, Decay Constant, and Half-Life

## What You'll Learn

Some atomic nuclei are unstable. They spontaneously transform into other nuclei, emitting radiation in the process. This is **radioactive decay**, and it's fundamentally different from any process you've studied before. Chemical reactions happen when atoms collide with enough energy. Radioactive decay doesn't need a collision — it just happens, at random, from within.

This lesson introduces the key concepts of radioactive decay: the random and spontaneous nature of the process, what "activity" means, what a decay constant tells you, and the most famous concept in nuclear physics — half-life. You'll learn why a sample of one billion radioactive atoms decays to 500 million in one half-life, then to 250 million in the next — not to zero, as you might intuitively expect.

---

## 1. What Makes a Nucleus Radioactive?

### Why This Matters

Before you can understand radioactive decay, you need to understand what makes some nuclei stable and others unstable. This connects back to the nuclear model from Lesson 57 and forward to the binding energy concepts in Lesson 66.

### The Key Ideas

**The stability problem.** A nucleus contains positively charged protons packed into an incredibly tiny volume (radius ~10⁻¹⁵ m). The electrostatic repulsion between protons is enormous — if that were the only force, every nucleus would explode instantly. Something must hold nuclei together against this repulsion. That something is the **strong nuclear force** — an attractive force between all nucleons (protons and neutrons) that acts only at very short range (~10⁻¹⁵ m).

**Stability depends on the neutron-to-proton ratio.** For light nuclei (up to about calcium, Z = 20), stability occurs when the number of neutrons roughly equals the number of protons: N ≈ Z. The strong force from both protons and neutrons binds the nucleus, while the electrostatic force only repels protons. Having about equal numbers works.

For heavier nuclei, more neutrons are needed. As Z increases, the electrostatic repulsion grows (each proton repels every other proton), but the strong force only acts between nearest neighbors. To compensate, heavy stable nuclei have more neutrons than protons — the neutrons provide additional strong-force attraction without adding to the electrostatic repulsion. For example:
- ⁵⁶Fe (Z = 26, N = 30): N/Z ≈ 1.15
- ²⁰⁸Pb (Z = 82, N = 126): N/Z ≈ 1.54

**Radioactivity: what it is.** A nucleus is **radioactive** (unstable) if it has either:
1. Too many neutrons relative to protons (neutron-rich)
2. Too many protons relative to neutrons (proton-rich)
3. Simply too many nucleons altogether (very heavy nuclei, Z > 83)

An unstable nucleus will eventually undergo **radioactive decay** — a spontaneous transformation that changes the composition of the nucleus, emitting radiation and moving toward stability.

**Types of radioactive decay (preview):**
- **Alpha (α) decay:** Emission of a helium nucleus (⁴₂He). Reduces Z by 2, A by 4. Common in heavy nuclei (Z > 83).
- **Beta-minus (β⁻) decay:** A neutron turns into a proton, emitting an electron and an antineutrino. Increases Z by 1, A unchanged. Common in neutron-rich nuclei.
- **Beta-plus (β⁺) decay:** A proton turns into a neutron, emitting a positron and a neutrino. Decreases Z by 1, A unchanged. Common in proton-rich nuclei.
- **Gamma (γ) decay:** Emission of a high-energy photon. Z and A unchanged. Usually follows alpha or beta decay when the daughter nucleus is in an excited state.

### Common Misconceptions

**"Radioactive means dangerous."** Radioactivity is a physical property of certain nuclei. Whether it's dangerous depends on the type of radiation, the intensity, the exposure time, and whether the radioactive material enters your body. We are all exposed to natural background radiation every day. A banana contains radioactive potassium-40. Being "radioactive" doesn't automatically mean deadly — it's about dose and context.

**"Radioactive decay is like a chemical reaction."** No. Chemical reactions involve electron rearrangements and have rates that depend on temperature, pressure, and concentration. Radioactive decay involves changes in the NUCLEUS, and its rate is unaffected by temperature, pressure, or chemical environment. Heating a radioactive sample to 10,000°C doesn't make it decay faster. This is because nuclear forces are millions of times stronger than the energies involved in chemical or thermal processes.

---

## 2. The Random and Spontaneous Nature of Decay

### Why This Matters

Radioactive decay is fundamentally random. You can predict with great accuracy what fraction of a large sample will decay in the next hour. But you CANNOT predict when any INDIVIDUAL nucleus will decay. This distinction — between statistical predictability for large numbers and complete unpredictability for individuals — is one of the deepest ideas in physics. It's the same distinction that appears in quantum mechanics (Lesson 62) and statistical mechanics.

### The Key Ideas

**Spontaneous.** Radioactive decay happens without any external trigger. You don't need to heat the sample, shine light on it, or collide particles into it. The decay originates from within the nucleus itself. An unstable nucleus will decay when it decays — and nothing you do can speed it up or slow it down (except for electron capture, which has a tiny dependence on chemical environment, but that's an advanced topic).

**Random.** You cannot predict WHEN a specific nucleus will decay. If you have a single uranium-238 atom, it might decay in the next second. Or it might decay 10 billion years from now. Both are possible. The decay is governed by quantum tunneling (Lesson 63) — the alpha particle has a probability of tunneling out of the nucleus each time it "bounces" against the barrier. Each bounce is like a lottery ticket with an incredibly tiny chance of winning.

**Statistical predictability.** For a large number of nuclei, the AVERAGE behavior becomes extremely predictable. This is like coin flipping: you can't predict the outcome of a single flip, but you can be very confident that in 1,000,000 flips, about 500,000 will be heads. Similarly, you can't predict which nuclei will decay, but you can predict with high precision what fraction will decay in a given time.

**The critical insight.** The probability that a given nucleus decays in the next second is CONSTANT — it doesn't depend on how long the nucleus has already existed. A uranium-238 nucleus that formed 4.5 billion years ago has exactly the same probability of decaying in the next second as one that formed 10 seconds ago. There is no "aging" — nuclei don't get "weaker" or "more likely to decay" as time passes. This is completely different from biological aging.

### Common Misconceptions

**"After one half-life, half the remaining atoms will decay in the same time."** YES — this is correct and is THE definition of half-life. If you start with N atoms, after one half-life you have N/2. After two half-lives, N/4 (half of N/2). After three, N/8. It halves each time.

**"After two half-lives, all atoms have decayed."** NO. This is a very common mistake. After 1 half-life: ½ remains. After 2 half-lives: ¼ remains. After 3: ⅛. After 10: about 1/1000. The number never reaches exactly zero in the exponential decay model, though eventually it becomes small enough that the last atom decays.

**"Nuclei that have been around longer are more likely to decay."** NO. This is the "aging" misconception. The decay probability per unit time is CONSTANT. An "old" nucleus is no more likely to decay in the next second than a "young" one. This is why radioactive decay follows exponential rather than linear decay.

---

## 3. Activity and the Decay Constant

### Why This Matters

How do we quantify how "radioactive" a sample is? The answer involves two connected concepts: activity (how many decays per second) and the decay constant (the probability per unit time that any given nucleus decays).

### The Key Ideas

**Activity (A).** The **activity** of a radioactive sample is the number of decays occurring per unit time. It is measured in **becquerels (Bq)**: 1 Bq = 1 decay per second. This is an SI unit and is very small. Typical activities:
- Human body (mostly from ¹⁴C and ⁴⁰K): ~8000 Bq
- Banana (⁴⁰K): ~15 Bq
- Smoke detector (²⁴¹Am): ~37,000 Bq (37 kBq)
- Medical radioisotope for PET scan: ~400 MBq
- Spent nuclear fuel rod: ~10¹⁸ Bq

**Decay constant (λ).** The **decay constant** λ (Greek lambda) is the probability that a given nucleus decays per unit time. Its units are s⁻¹ (or min⁻¹, yr⁻¹, etc.). If λ = 0.01 s⁻¹, it means each nucleus has a 1% probability of decaying in the next second.

**The fundamental relationship.** The activity A is proportional to the number of undecayed nuclei N present:

$$A = \lambda N$$

This makes intuitive sense: the more radioactive nuclei you have, the more decays per second. If each nucleus has probability λ of decaying per second, and you have N nuclei, expect λN decays per second.

**How N changes with time.** If A = λN is the rate at which nuclei are disappearing (each decay removes one nucleus), then:

$$\frac{dN}{dt} = -A = -\lambda N$$

This is a differential equation. In words: the rate of change of the number of nuclei is proportional to (and negative of) the number present. The more you have, the faster you lose them — but as you lose them, the rate slows down.

**The solution: exponential decay.** Solving this differential equation (not required for IB, but you should know the result and be able to use it) gives:

$$N(t) = N_0 e^{-\lambda t}$$

where N₀ is the initial number of undecayed nuclei at t = 0. This is the **exponential decay law**.

Similarly for activity:

$$A(t) = A_0 e^{-\lambda t} = \lambda N_0 e^{-\lambda t}$$

### Common Misconceptions

**"Activity and decay constant are the same thing."** No. Activity A = λN is the number of decays per second (units: Bq = s⁻¹). Decay constant λ is the probability per second for one nucleus (units: s⁻¹). They have the same units but different meanings: A depends on sample size; λ is a property of the isotope.

**"λ gets smaller as the sample decays."** No. λ is CONSTANT for a given isotope. What changes is N — the number of nuclei present. As N decreases, A = λN decreases proportionally.

---

## 4. Half-Life

### Why This Matters

Half-life is the most intuitive way to describe how quickly a radioactive isotope decays. It's what you hear about in news reports ("Cesium-137 has a half-life of 30 years") and what you calculate in carbon dating. Understanding half-life deeply — including its relationship to the decay constant — is essential for IB Physics.

### The Key Ideas

**Definition.** The **half-life** T₁/₂ is the time required for half the nuclei in a sample to decay. Equivalently, it's the time for the activity to fall to half its initial value.

**Mathematical definition.** After one half-life: N(T₁/₂) = N₀/2. Using N(t) = N₀ e^(−λt):

$$\frac{N_0}{2} = N_0 e^{-\lambda T_{1/2}}$$

$$\frac{1}{2} = e^{-\lambda T_{1/2}}$$

$$2 = e^{\lambda T_{1/2}}$$

$$\ln 2 = \lambda T_{1/2}$$

$$T_{1/2} = \frac{\ln 2}{\lambda} \approx \frac{0.693}{\lambda}$$

This is one of the most important equations in nuclear physics. It connects the decay constant (a probability per unit time) to the half-life (an intuitively understandable time).

**What happens over multiple half-lives:**
- t = 0: N₀ (100%)
- t = T₁/₂: N₀/2 (50%)
- t = 2T₁/₂: N₀/4 (25%)
- t = 3T₁/₂: N₀/8 (12.5%)
- t = 4T₁/₂: N₀/16 (6.25%)
- t = 10T₁/₂: N₀/1024 ≈ 0.1%

**The fraction remaining after n half-lives:** N/N₀ = (1/2)^n = 2^(-n).

**A crucial conceptual point.** The half-life does NOT mean "half the remaining time until all atoms are gone." If T₁/₂ = 10 years, it doesn't mean the sample will be completely decayed in 20 years. After 10 years, half remains. After 20 years, a quarter remains. After 30 years, an eighth. The decay never technically reaches zero.

**Range of half-lives observed in nature:**
- ²¹²Po: 0.30 μs (alpha decay)
- ¹⁴C: 5730 years (beta-minus)
- ⁴⁰K: 1.25 billion years (beta-minus and electron capture)
- ²³⁸U: 4.47 billion years (alpha)
- ²⁰⁹Bi: 1.9 × 10¹⁹ years (alpha — effectively stable)

### Common Misconceptions

**"Half-life means the time until half the radioactivity is gone."** This is actually correct IF you interpret it as: the time for the activity (and the number of nuclei) to be reduced by half. It does NOT mean "half the time until it's all gone."

**"After two half-lives, everything has decayed."** This is the most common misconception about radioactive decay. Think of it as repeatedly halving: 100% → 50% → 25% → 12.5% → 6.25% → ... Each half-life cuts the REMAINING amount in half, not the original amount.

**"The half-life changes as the sample decays."** No. T₁/₂ is a constant property of the isotope. Whether you have 1 kg or 1 μg of ¹⁴C, the half-life is still 5730 years. The ACTIVITY scales with sample size, but the half-life doesn't.

---

## Worked Examples

### Example 1: Activity and Number of Nuclei

A sample of ⁶⁰Co (cobalt-60) has an activity of 3.70 × 10⁷ Bq. The decay constant of ⁶⁰Co is 4.17 × 10⁻⁹ s⁻¹. (a) Calculate the number of ⁶⁰Co nuclei in the sample. (b) Calculate the mass of ⁶⁰Co in the sample. (Molar mass of ⁶⁰Co = 60.0 g/mol.)

**Approach:** N = A/λ. Then mass from number of nuclei and Avogadro's number.

**Step 1:** N = A/λ = 3.70 × 10⁷ / (4.17 × 10⁻⁹) = 8.87 × 10¹⁵ nuclei.

**Step 2:** n = N/N_A = 8.87 × 10¹⁵ / (6.022 × 10²³) = 1.473 × 10⁻⁸ mol.
Mass = n × M = 1.473 × 10⁻⁸ × 60.0 = 8.84 × 10⁻⁷ g = 0.884 μg.

**Why this makes sense:** A tiny amount of radioactive material (less than 1 microgram) produces tens of millions of decays per second. Radioactive isotopes have enormous specific activity (activity per unit mass).

---

### Example 2: Half-Life and Decay Constant

The half-life of iodine-131 is 8.02 days. Calculate: (a) the decay constant in s⁻¹, (b) the fraction of a sample remaining after 30.0 days.

**Approach:** λ = ln 2 / T₁/₂. Convert days to seconds. Then N/N₀ = e^(−λt).

**Step 1:** T₁/₂ = 8.02 days = 8.02 × 24 × 3600 = 6.929 × 10⁵ s.
λ = ln 2 / T₁/₂ = 0.6931 / (6.929 × 10⁵) = 1.000 × 10⁻⁶ s⁻¹.

**Step 2:** t = 30.0 days = 2.592 × 10⁶ s.
λt = 1.000 × 10⁻⁶ × 2.592 × 10⁶ = 2.592.
N/N₀ = e⁻²·⁵⁹² = 0.0749 = 7.49%.

Alternative using half-lives: 30.0 / 8.02 = 3.74 half-lives. N/N₀ = (1/2)^3.74 = 2⁻³·⁷⁴ = 0.0749. ✓

**Why this makes sense:** After 3.74 half-lives, about 7.5% remains. This is consistent: after 3 half-lives (24.06 days), 12.5% remains; after 4 (32.08 days), 6.25%. 7.5% is between these values.

---

### Example 3: Finding Half-Life from Activity Measurements

A freshly prepared radioactive sample has an activity of 8000 Bq. After 6.0 hours, the activity has fallen to 3500 Bq. Calculate the half-life.

**Approach:** Use A = A₀ e^(−λt). Solve for λ, then T₁/₂.

**Step 1:** 3500 = 8000 e^(−λ × 6.0).
3500/8000 = 0.4375 = e^(−6.0λ).
ln(0.4375) = −6.0λ.
−0.8267 = −6.0λ.
λ = 0.8267 / 6.0 = 0.1378 hr⁻¹.

**Step 2:** T₁/₂ = ln 2 / λ = 0.6931 / 0.1378 = 5.03 hours.

Check: after 5.03 hours, A should be 8000/2 = 4000 Bq. After 6.0 hours, slightly less than 4000 → 3500 Bq is reasonable.

**Why this makes sense:** The half-life (5.03 h) is close to 6 h, which explains why the activity dropped to slightly less than half (3500/8000 = 0.44) in 6 hours.

---

### Example 4: Number of Half-Lives

A radioactive sample has decayed until only 3.125% of the original nuclei remain. How many half-lives have elapsed?

**Approach:** 3.125% = 1/32 = (1/2)⁵. So n = 5 half-lives.

Let's verify: (1/2)⁵ = 1/32 = 0.03125 = 3.125%. ✓

**Why this makes sense:** After each half-life, the fraction is halved: 100% → 50% → 25% → 12.5% → 6.25% → 3.125%. Five halvings take you from 100% to 3.125%.

---

### Example 5: Activity After Multiple Half-Lives

The initial activity of a ¹³⁷Cs source is 2.00 × 10⁵ Bq. The half-life of ¹³⁷Cs is 30.0 years. Calculate the activity after: (a) 90.0 years, (b) 150 years.

**Approach:** Use the half-life method.

**(a)** 90.0 / 30.0 = 3 half-lives.
A = A₀ × (1/2)³ = 2.00 × 10⁵ × 1/8 = 2.50 × 10⁴ Bq.

**(b)** 150 / 30.0 = 5 half-lives.
A = 2.00 × 10⁵ × (1/2)⁵ = 2.00 × 10⁵ / 32 = 6.25 × 10³ Bq.

Using the exponential formula to verify (a):
λ = 0.6931 / (30.0 × 365 × 24 × 3600) = 7.33 × 10⁻¹⁰ s⁻¹.
t = 90.0 × 365 × 24 × 3600 = 2.838 × 10⁹ s.
λt = 7.33 × 10⁻¹⁰ × 2.838 × 10⁹ = 2.079.
A = 2.00 × 10⁵ × e⁻²·⁰⁷⁹ = 2.00 × 10⁵ × 0.125 = 2.50 × 10⁴ Bq. ✓

**Why this makes sense:** Using the half-life shortcut (halving the activity for each half-life) gives the same result as the exponential formula. The shortcut works because (1/2)^n = e^(−n ln 2).

---

## Practice Problems

### Problem 1
A radioactive isotope has a decay constant of 5.80 × 10⁻³ s⁻¹. (a) Calculate its half-life in seconds. (b) If a sample initially contains 3.00 × 10²⁰ nuclei, calculate the initial activity in Bq. (c) Calculate the number of undecayed nuclei remaining after 200 seconds. (d) Calculate the activity at this time.

### Problem 2
The half-life of radon-222 is 3.82 days. (a) Calculate the decay constant in s⁻¹. (b) A sample has an activity of 4.80 × 10⁶ Bq. How many radon-222 nuclei are present? (c) What mass of radon-222 does this correspond to? (Molar mass = 222 g/mol.) (d) After how many days will the activity drop to 3.00 × 10⁵ Bq?

### Problem 3
A radioactive sample has its activity measured every 10 minutes. The data are:

| t / min | 0 | 10 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|
| A / Bq | 1600 | 1131 | 800 | 566 | 400 | 283 |

(a) Show that the half-life is approximately 20 minutes. (b) Determine the decay constant in min⁻¹. (c) Estimate the activity at t = 65 minutes. (d) Explain why the activity at t = 65 minutes cannot be exactly predicted even with a perfect measurement.

### Problem 4
A student says: "The half-life of carbon-14 is 5730 years. This means that after 5730 years, half of the carbon-14 in a sample has decayed, and after 11,460 years, all of it has decayed." (a) Identify the error in this statement. (b) Calculate the actual percentage of carbon-14 remaining after 11,460 years. (c) How many half-lives does it take for the amount to fall below 1% of the original?

### Problem 5
Two samples are prepared. Sample A has 1.00 × 10¹⁵ nuclei of isotope X (half-life 10.0 min). Sample B has 4.00 × 10¹⁵ nuclei of isotope Y (half-life 20.0 min). (a) Calculate the initial activity of each sample. (b) After 20.0 min, which sample has the higher activity? (c) At what time are the activities equal?

### Problem 6 (IB Exam Style)
A pure sample of a radioactive isotope is prepared. The initial activity is measured as 6.40 × 10⁶ Bq. After 6.0 hours, the activity has decreased to 1.60 × 10⁶ Bq.

(a) Explain what is meant by "activity" of a radioactive sample. [1 mark]

(b) Show that the half-life of the isotope is 3.0 hours. [2 marks]

(c) Calculate the decay constant of the isotope in s⁻¹. [2 marks]

(d) Determine the number of radioactive nuclei present in the sample when the activity is 1.60 × 10⁶ Bq. [2 marks]

(e) State and explain what happens to the half-life of the sample as time increases. [2 marks]

(f) The sample is heated to 800°C in a furnace. State and explain the effect, if any, on: (i) the activity, (ii) the half-life. [3 marks]

---

## Answers

### Answer 1
(a) T₁/₂ = ln 2 / λ = 0.6931 / (5.80 × 10⁻³) = 119.5 s ≈ 120 s.

(b) A₀ = λN₀ = 5.80 × 10⁻³ × 3.00 × 10²⁰ = 1.74 × 10¹⁸ Bq.

(c) N = N₀ e^(−λt) = 3.00 × 10²⁰ × e^(−5.80 × 10⁻³ × 200) = 3.00 × 10²⁰ × e^(−1.16) = 3.00 × 10²⁰ × 0.3135 = 9.41 × 10¹⁹ nuclei.

(d) A = λN = 5.80 × 10⁻³ × 9.41 × 10¹⁹ = 5.46 × 10¹⁷ Bq.
Or: A = A₀ e^(−λt) = 1.74 × 10¹⁸ × 0.3135 = 5.45 × 10¹⁷ Bq. ✓

### Answer 2
(a) T₁/₂ = 3.82 × 24 × 3600 = 3.300 × 10⁵ s.
λ = 0.6931 / (3.300 × 10⁵) = 2.10 × 10⁻⁶ s⁻¹.

(b) N = A/λ = 4.80 × 10⁶ / (2.10 × 10⁻⁶) = 2.29 × 10¹² nuclei.

(c) n = N/N_A = 2.29 × 10¹² / (6.022 × 10²³) = 3.80 × 10⁻¹² mol.
Mass = 3.80 × 10⁻¹² × 222 = 8.44 × 10⁻¹⁰ g = 0.844 ng.

(d) A = A₀ e^(−λt) → 3.00 × 10⁵ = 4.80 × 10⁶ e^(−λt).
3.00/4.80 = 0.0625 = e^(−λt).
ln(0.0625) = −λt → −2.7726 = −λt.
t = 2.7726 / (2.10 × 10⁻⁶) = 1.32 × 10⁶ s = 15.3 days.
Check: 15.3/3.82 = 4.00 half-lives. (1/2)⁴ × 4.80 × 10⁶ = 3.00 × 10⁵ Bq. ✓

### Answer 3
(a) From the data: at t = 0, A = 1600. At t = 20, A = 800. That's exactly half. At t = 40, A = 400 — half of 800. At t = 10, A = 1131 — between 1600 and 800. The data is consistent with T₁/₂ = 20 min.

(b) λ = ln 2 / T₁/₂ = 0.6931 / 20 = 0.03466 min⁻¹.

(c) t = 65 min. Number of half-lives = 65/20 = 3.25.
A = 1600 × (1/2)^3.25 = 1600 × 0.1051 = 168 Bq.
Or: e^(−λt) = e^(−0.03466 × 65) = e^(−2.253) = 0.1051. A = 1600 × 0.1051 = 168 Bq. ✓

(d) Radioactive decay is a random process. The exponential decay law gives the EXPECTED (average) activity for a large number of nuclei. For a finite sample, there are statistical fluctuations. At t = 65 min, the expected number of decays per second is about 168, but the actual count in any given second might be different (standard deviation ≈ √168 ≈ 13). Also, the exponential model is a continuous approximation to a discrete random process — the exact activity at any instant cannot be precisely predicted; only the probability distribution can be.

### Answer 4
(a) The student incorrectly thinks that after two half-lives, all the material has decayed. The correct interpretation is that each half-life reduces the REMAINING amount by half. After 2 half-lives, 1/4 remains, not zero. The decay is exponential, never reaching exactly zero.

(b) After 11,460 years = 2 half-lives. Remaining = (1/2)² = 1/4 = 25%.

(c) (1/2)^n < 0.01 → 2^n > 100 → n > log₂(100) = ln(100)/ln(2) = 4.605/0.6931 = 6.64.
So 7 half-lives are needed. At n = 7: (1/2)⁷ = 1/128 = 0.78% < 1%. At n = 6: 1/64 = 1.56% > 1%.

### Answer 5
(a) λ_A = ln 2 / 10.0 = 0.06931 min⁻¹.
A_A(0) = 0.06931 × 1.00 × 10¹⁵ = 6.931 × 10¹³ Bq.

λ_B = ln 2 / 20.0 = 0.03466 min⁻¹.
A_B(0) = 0.03466 × 4.00 × 10¹⁵ = 1.386 × 10¹⁴ Bq.

Sample B has higher initial activity (about twice A's), despite having a longer half-life, because it has four times as many nuclei.

(b) t = 20.0 min = 2 half-lives for A, 1 half-life for B.
A_A = 6.931 × 10¹³ × (1/2)² = 1.733 × 10¹³ Bq.
A_B = 1.386 × 10¹⁴ × (1/2)¹ = 6.931 × 10¹³ Bq.
Sample B still has the higher activity (by a factor of 4).

(c) A_A = A_B → λ_A N_A e^(−λ_A t) = λ_B N_B e^(−λ_B t).
0.06931 × 1 × 10¹⁵ × e^(−0.06931t) = 0.03466 × 4 × 10¹⁵ × e^(−0.03466t).
6.931 × 10¹³ e^(−0.06931t) = 1.386 × 10¹⁴ e^(−0.03466t).
e^(−0.06931t + 0.03466t) = 1.386 × 10¹⁴ / 6.931 × 10¹³ = 2.0.
e^(−0.03465t) = 2.0.
−0.03465t = ln(2) = 0.6931.
t = −0.6931 / 0.03465 = −20.0 min.

Wait, that gives negative time. Let me recheck the signs.
e^((λ_B − λ_A)t) = A_B(0)/A_A(0) = 2.
(λ_B − λ_A) = 0.03466 − 0.06931 = −0.03465.
e^(−0.03465t) = 2.0 → −0.03465t = 0.6931 → t = −20.0 min.

A negative time means the activities were equal 20 minutes ago, before the initial measurement. At t = 0, B already has higher activity. Since B's half-life is longer (slower decay) and it starts with higher activity, B will always be more active than A going forward. They never cross after t = 0.

### Answer 6
(a) The activity of a radioactive sample is the number of nuclear decays occurring per unit time. It is measured in becquerels (Bq), where 1 Bq = 1 decay per second.

(b) In 6.0 hours, the activity falls from 6.40 × 10⁶ to 1.60 × 10⁶ Bq.
Ratio: 1.60/6.40 = 1/4 = (1/2)².
This means 2 half-lives have elapsed in 6.0 hours.
Therefore, T₁/₂ = 6.0/2 = 3.0 hours.

(c) T₁/₂ = 3.0 hours = 3.0 × 3600 = 10,800 s.
λ = ln 2 / T₁/₂ = 0.6931 / 10,800 = 6.42 × 10⁻⁵ s⁻¹.

(d) N = A/λ = 1.60 × 10⁶ / (6.42 × 10⁻⁵) = 2.49 × 10¹⁰ nuclei.

(e) The half-life remains constant. T₁/₂ is a property of the isotope — it does not change as the sample decays. Each nucleus of the same isotope always has the same probability λ of decaying per unit time, regardless of how long the sample has been decaying or how many nuclei remain. The ACTIVITY decreases as N decreases, but T₁/₂ = ln 2/λ is fixed.

(f) (i) No effect on the activity. Radioactive decay is a nuclear process, unaffected by temperature. The decay constant λ, and therefore the activity A = λN, remains the same regardless of whether the sample is at −200°C or +800°C. Nuclear energy scales (~MeV) are millions of times larger than thermal energy scales (~0.1 eV at 800°C).
(ii) No effect on the half-life. T₁/₂ = ln 2/λ depends only on λ, which is determined by nuclear structure and the type of decay. Temperature does not affect nuclear instability. The half-life at 800°C is exactly the same as at room temperature. [Note: there are extremely rare exceptions involving electron capture decay, where the chemical environment can change the half-life by a tiny fraction of a percent, but this is negligible at IB level and does not apply to typical alpha/beta/gamma emitters.]

---

## Key Takeaways

1. Radioactive decay is a spontaneous, random nuclear process. It is unaffected by temperature, pressure, or chemical environment.

2. The probability that a given nucleus decays per unit time is the decay constant λ. It is constant — nuclei don't "age."

3. Activity A = λN measures decays per second (in Bq). As N decreases, A decreases proportionally.

4. The half-life T₁/₂ = ln 2 / λ is the time for half the nuclei to decay. After n half-lives, the fraction remaining is (1/2)^n.

5. Radioactive decay follows the exponential decay law: N = N₀ e^(−λt) and A = A₀ e^(−λt).

6. Each half-life halves the REMAINING amount, not the original. The decay never reaches exactly zero. After 10 half-lives, about 0.1% remains.
