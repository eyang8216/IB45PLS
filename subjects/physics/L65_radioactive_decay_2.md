# Lesson 65: Radioactive Decay 2 — Exponential Decay Law, Carbon Dating, and Background Radiation

## What You'll Learn

In Lesson 64, you learned the core concepts of radioactive decay: activity, decay constant, and half-life. You learned that decay is exponential — each half-life cuts the remaining amount in half. Now we go deeper: how to USE the exponential decay law to solve quantitative problems, how carbon-14 dating works (and what its limitations are), and what background radiation is — both natural and artificial sources.

These topics aren't just exam material. Carbon dating revolutionized archaeology and paleontology. Background radiation shapes how we design everything from nuclear power plants to medical treatments. Understanding these topics helps you evaluate news about nuclear accidents, medical procedures, and radon in homes.

---

## 1. The Exponential Decay Law in Depth

### Why This Matters

The exponential decay law N = N₀ e^(−λt) appears simple, but it packs enormous predictive power. It lets you calculate how much of a radioactive sample remains after any time interval, determine ages of archaeological specimens, and design radiation therapy treatments. Mastering its mathematical forms is essential for IB exam success.

### The Key Ideas

**The fundamental equations:**

Number of undecayed nuclei: $$N(t) = N_0 e^{-\lambda t}$$

Activity: $$A(t) = A_0 e^{-\lambda t} = \lambda N_0 e^{-\lambda t}$$

These are mathematically identical — the activity decays with the same exponential time constant as the number of nuclei.

**The three forms you must be comfortable with:**

1. **Exponential form:** N = N₀ e^(−λt). Direct and general. Use when you have λ and t.
2. **Half-life form:** N = N₀ (1/2)^(t/T₁/₂). Use when t is given in terms of (or converted to) half-lives.
3. **Logarithmic form:** ln(N/N₀) = −λt. Use when solving for t (time) given N/N₀.

**Converting between forms.** Since e^(−λt) = (e^(−λ))^t and e^(−λT₁/₂) = 1/2:

$$e^{-\lambda t} = (1/2)^{t/T_{1/2}}$$

Both sides represent the fraction remaining after time t.

**When to use each form:**

| You're given | You want | Use |
|---|---|---|
| λ, t, N₀ | N or A | N = N₀ e^(−λt) |
| T₁/₂, n (number of half-lives) | N/N₀ | (1/2)^n |
| N/N₀ (fraction remaining), λ | t | t = −ln(N/N₀)/λ |
| A₀, A, T₁/₂ | t | t = (T₁/₂/ln 2) × ln(A₀/A) |

**The number of half-lives elapsed.** A powerful mental shortcut:

$$n = \frac{t}{T_{1/2}}$$

Then: N/N₀ = (1/2)^n, A/A₀ = (1/2)^n.

This is exact (not an approximation) because of the relationship between e^(−λt) and (1/2)^(t/T₁/₂).

### Common Misconceptions

**"The exponential formula and the half-life formula give different results."** They are mathematically identical. e^(−λt) = e^(−(ln 2)t/T₁/₂) = (e^(ln 2))^(−t/T₁/₂) = 2^(−t/T₁/₂) = (1/2)^(t/T₁/₂). Use whichever is more convenient.

**"You can't use the half-life formula if the time isn't an exact multiple."** You CAN use the half-life formula for ANY time: (1/2)^(t/T₁/₂) works for fractional exponents. For t = 5 hours and T₁/₂ = 3 hours: (1/2)^(5/3) = 2^(−1.667) = 0.315. This is perfectly valid.

---

## 2. Carbon-14 Dating

### Why This Matters

Carbon dating is the most famous application of radioactive decay. It's used to date organic materials up to about 50,000 years old. It helped determine the age of the Dead Sea Scrolls, Ötzi the Iceman, and countless archaeological sites. Understanding its principles and limitations is a classic IB Physics topic.

### The Key Ideas

**What is carbon-14?** Carbon has three naturally occurring isotopes: ¹²C (98.9%, stable), ¹³C (1.1%, stable), and ¹⁴C (trace, radioactive). Carbon-14 has 6 protons and 8 neutrons. It undergoes beta-minus decay:

$${}^{14}_{6}\text{C} \rightarrow {}^{14}_{7}\text{N} + e^- + \bar{\nu}_e$$

with a half-life of 5730 years.

**How carbon-14 is produced.** Cosmic rays (high-energy protons from space) collide with nitrogen atoms in the upper atmosphere, producing carbon-14:

$$n + {}^{14}_{7}\text{N} \rightarrow {}^{14}_{6}\text{C} + p$$

The carbon-14 quickly combines with oxygen to form ¹⁴CO₂, which mixes throughout the atmosphere. Plants absorb ¹⁴CO₂ during photosynthesis, and animals eat the plants. As long as an organism is alive, it continually exchanges carbon with the environment, maintaining a ¹⁴C/¹²C ratio equal to the atmospheric ratio.

**How carbon dating works.** When the organism dies, it stops exchanging carbon with the environment. No new ¹⁴C enters. The existing ¹⁴C begins to decay with its 5730-year half-life. By measuring the current ¹⁴C/¹²C ratio in the sample and comparing it to the known atmospheric ratio at the time the organism lived, you can calculate how long the organism has been dead:

$$t = \frac{T_{1/2}}{\ln 2} \ln\left(\frac{N_0}{N}\right) = \frac{5730 \text{ years}}{\ln 2} \ln\left(\frac{\text{initial } ^{14}\text{C ratio}}{\text{current } ^{14}\text{C ratio}}\right)$$

**The assumptions of carbon dating.** Carbon dating relies on several assumptions that must be understood:

1. **Constant atmospheric ¹⁴C ratio:** The method assumes the ¹⁴C/¹²C ratio in the atmosphere has been constant over time. It hasn't been — it varies due to changes in cosmic ray flux, solar activity, and fossil fuel burning. To correct for this, scientists use calibration curves based on tree rings (dendrochronology), which provide an absolute date for each ring.

2. **No contamination:** The sample must not have been contaminated with modern carbon (which would make it appear younger) or old carbon (which would make it appear older). This is a major practical challenge in archaeology.

3. **Closed system:** No carbon has entered or left the sample since death.

**Limitations of carbon dating:**
- Only works for organic material (things that were once alive).
- Upper limit: about 50,000 years (after ~9 half-lives, only ~0.2% of original ¹⁴C remains, making accurate measurement difficult).
- Lower limit: about 300 years (after such a short time, the change in ¹⁴C is too small to measure precisely, especially given the calibration uncertainties).
- Doesn't work for marine organisms without correction (marine carbon has a different ¹⁴C age — the "reservoir effect").
- Nuclear weapons testing (1950s-1960s) doubled atmospheric ¹⁴C, so post-1950 samples require special handling.

### Common Misconceptions

**"Carbon dating tells you the age of rocks."** No. Carbon dating only works on organic material — things that were once alive and incorporated atmospheric carbon. Rocks are typically dated using isotopes with much longer half-lives, such as uranium-lead (half-life 4.47 billion years for ²³⁸U) or potassium-argon (half-life 1.25 billion years for ⁴⁰K).

**"Carbon dating is accurate to the exact year."** No. There are calibration uncertainties, measurement uncertainties, and the assumption violations mentioned above. Modern AMS (Accelerator Mass Spectrometry) carbon dating can achieve precision of ±20-40 years for relatively recent samples, but the uncertainty increases for older samples.

**"Carbon-14 is the only isotope used for radioactive dating."** There are many radiometric dating methods: uranium-lead (²³⁸U → ²⁰⁶Pb, 4.47 Gyr), potassium-argon (⁴⁰K → ⁴⁰Ar, 1.25 Gyr), rubidium-strontium (⁸⁷Rb → ⁸⁷Sr, 48.8 Gyr), and others. Each is suited to different time scales and materials.

---

## 3. Background Radiation

### Why This Matters

You are radioactive. So is the food you eat, the air you breathe, and the ground beneath your feet. **Background radiation** is the ionizing radiation present in the environment from natural and artificial sources. Understanding where it comes from, how much there is, and what the risks are is essential for informed decision-making about nuclear technology, medical procedures, and public health.

### The Key Ideas

**What is background radiation?** Background radiation is the ubiquitous low-level ionizing radiation to which all living things are exposed. It has several components:

**Natural sources (about 85% of average exposure):**

1. **Radon gas (~50% of natural):** Radon-222 is a radioactive gas produced by the decay of uranium in soil and rock. It seeps into buildings through foundations and accumulates in basements. It decays by alpha emission with a half-life of 3.8 days, and its solid daughter products (polonium, bismuth, lead) lodge in lung tissue, delivering alpha radiation that damages DNA. Radon is the second leading cause of lung cancer after smoking.

2. **Terrestrial radiation (~15% of natural):** Radioactive isotopes in the Earth's crust — primarily ⁴⁰K, ²³⁸U, ²³²Th and their decay products. These are present in soil, rocks, and building materials. Granite areas have higher background radiation than limestone areas.

3. **Cosmic radiation (~15% of natural):** High-energy particles (mostly protons) from space produce showers of secondary particles when they hit the atmosphere. Cosmic ray exposure increases with altitude — airline crews receive about 3-5 mSv/year additional exposure. At sea level, cosmic radiation contributes about 0.3 mSv/year.

4. **Internal radiation (~10% of natural):** Radioactive isotopes inside our bodies, mainly ⁴⁰K (in muscles) and ¹⁴C (in all organic molecules). A 70 kg person contains about 9000 Bq of ⁴⁰K and 3700 Bq of ¹⁴C, contributing about 0.3 mSv/year.

**Artificial sources (~15% of average exposure):**

1. **Medical procedures:** X-rays, CT scans, nuclear medicine. A chest X-ray: ~0.1 mSv. CT scan: ~10 mSv. PET scan: ~5 mSv. These are by far the largest artificial source for most people.

2. **Nuclear weapons testing fallout:** Residual radioactivity from atmospheric tests (1945-1980). Now a very small fraction of total exposure.

3. **Nuclear power and fuel cycle:** Very small contribution to public exposure (~0.1% of average).

4. **Consumer products:** Smoke detectors (²⁴¹Am), some older luminous watches (²²⁶Ra), certain ceramics and glass with uranium glazes.

**Measuring radiation dose.** The sievert (Sv) is the SI unit of equivalent dose, which accounts for the biological effect of different types of radiation. For IB, you should know:
- **Absorbed dose (gray, Gy):** Energy deposited per unit mass (1 Gy = 1 J/kg).
- **Equivalent dose (sievert, Sv):** Absorbed dose × radiation weighting factor.
- Alpha particles have a weighting factor of 20 (they're 20× more damaging per unit energy than beta/gamma, which have weight 1).

**Typical annual doses:**
- Average worldwide: ~3 mSv
- Denver (high altitude): ~10 mSv
- Kerala, India (high natural thorium): ~30 mSv
- Airline crew: ~5-10 mSv/year
- CT scan (one): ~10 mSv
- Occupational limit for radiation workers: 20 mSv/year

### Common Misconceptions

**"Any radiation is dangerous."** We are all exposed to radiation constantly. The linear no-threshold model (used for radiation protection) assumes any dose carries some risk, but at natural background levels (~3 mSv/year), the risk is extremely small and indistinguishable from other environmental cancer risks. The body has DNA repair mechanisms that fix most radiation damage. The danger comes from elevated doses.

**"Background radiation is only from human activities."** The vast majority (~85%) comes from natural sources that have been present throughout Earth's history. Humans evolved in a radioactive environment.

---

## 4. Radiometric Dating Beyond Carbon

### Why This Matters

Carbon dating is limited to the last 50,000 years. To date the Earth (4.54 billion years old), fossils hundreds of millions of years old, or the formation of the solar system, you need isotopes with much longer half-lives.

### The Key Ideas

**Uranium-Lead dating.** ²³⁸U decays to ²⁰⁶Pb with a half-life of 4.47 billion years. ²³⁵U decays to ²⁰⁷Pb with a half-life of 704 million years. By measuring the ratios of uranium to lead isotopes in a zircon crystal (which incorporates uranium but not lead when it forms), geologists can date rocks as old as the Earth itself. The two independent "clocks" (²³⁸U and ²³⁵U) provide a powerful cross-check.

**Potassium-Argon dating.** ⁴⁰K decays to ⁴⁰Ar (by electron capture) with a half-life of 1.25 billion years. When volcanic rock solidifies, any argon (a gas) escapes, resetting the clock. The ⁴⁰Ar produced by subsequent ⁴⁰K decay is trapped in the rock, so the ⁴⁰Ar/⁴⁰K ratio gives the time since solidification. This method is especially useful for dating early hominid fossils in volcanic ash layers.

**Choosing the right clock.** The isotope must have a half-life comparable to the age being measured. Too short, and too little remains to measure. Too long, and too little daughter product has accumulated.

---

### The Concept of the "Age of the Earth"

Radiometric dating provides our best estimate for the age of the Earth: 4.54 ± 0.05 billion years. This comes primarily from uranium-lead dating of meteorites (which formed at the same time as the solar system) and the oldest Earth rocks (zircons from Australia, ~4.4 billion years).

The key insight: the Earth must be OLDER than its oldest rocks, and meteorites provide an independent sample of the primordial solar system material. By dating many meteorites with multiple decay systems (U-Pb, Rb-Sr, Sm-Nd), scientists get consistent results converging on ~4.54 Gyr.

This is a triumph of the exponential decay law: the same mathematics that describes the decay of a laboratory sample also describes the history of the entire solar system. The universality of radioactive decay — λ doesn't change with time, temperature, pressure, or chemical environment — makes it the most reliable clock in science.

### Medical Applications of Radioisotopes

Radioactive isotopes are used extensively in medicine:

**Diagnostic imaging:**
- **Technetium-99m (T₁/₂ = 6.0 hours):** The most widely used medical radioisotope. It emits gamma rays (140 keV) that are detected by gamma cameras, producing images of organs. The short half-life minimizes patient dose. It's used for bone scans, cardiac stress tests, and thyroid imaging.
- **PET scans (Positron Emission Tomography):** Uses ¹⁸F (T₁/₂ = 110 min) attached to glucose molecules. Cancer cells consume more glucose, so they accumulate more ¹⁸F. The positrons annihilate with electrons, producing back-to-back 511 keV gamma rays that are detected by a ring of detectors. PET scans can detect tumors as small as a few millimeters.

**Therapy:**
- **Iodine-131 (T₁/₂ = 8.0 days):** Concentrates in the thyroid gland. Used to treat thyroid cancer — the beta particles destroy thyroid cells while the short range limits damage to surrounding tissue.
- **Cobalt-60 (T₁/₂ = 5.27 years):** A gamma source used in external beam radiotherapy (the "gamma knife"). Precisely focused beams from multiple directions deliver a high dose to a tumor while sparing surrounding tissue.

**The ideal isotope properties:** Short enough half-life to minimize patient dose, but long enough to prepare and administer. Gamma emission (penetrates tissue for external detection) rather than alpha or beta (which would be absorbed before reaching the detector). Chemically compatible with biological molecules.

---

## Worked Examples

### Example 1: Solving for Time

A wooden artifact contains 12.5% of the ¹⁴C found in living wood. How old is the artifact? (T₁/₂ = 5730 years.)

**Approach:** 12.5% = 1/8 = (1/2)³. So 3 half-lives have elapsed.

**Step 1:** n = 3. t = n × T₁/₂ = 3 × 5730 = 17,190 years.

Using the formula: t = (T₁/₂/ln 2) × ln(N₀/N) = (5730/0.6931) × ln(1/0.125) = 8267 × ln(8) = 8267 × 2.079 = 17,190 years. ✓

---

### Example 2: Fraction Remaining

A radioactive sample has T₁/₂ = 8.0 days. What fraction remains after 30.0 days?

**Approach:** n = t/T₁/₂ = 30.0/8.0 = 3.75. Fraction = (1/2)^3.75.

**Step 1:** (1/2)^3.75 = 2^(−3.75). Using calculator: 2^(−3.75) = 0.0743 = 7.43%.

Verify with exponential formula: λ = 0.6931/8.0 = 0.08664 day⁻¹. 
Fraction = e^(−0.08664 × 30.0) = e^(−2.599) = 0.0744. ✓

---

### Example 3: Carbon Dating with Activity

A sample of ancient charcoal has a ¹⁴C activity of 0.150 Bq per gram of carbon. Living wood has an activity of 0.230 Bq per gram. The half-life of ¹⁴C is 5730 years. Calculate the age of the charcoal.

**Approach:** t = (T₁/₂/ln 2) × ln(A₀/A).

**Step 1:** A₀/A = 0.230/0.150 = 1.5333.
ln(1.5333) = 0.4274.

**Step 2:** t = (5730/0.6931) × 0.4274 = 8267 × 0.4274 = 3533 years.

**Why this makes sense:** The activity has dropped to 65% of its original value, which is less than one half-life (50%). The age should be less than 5730 years, and 3533 years is reasonable.

---

### Example 4: Remaining Mass

A laboratory has 2.50 μg of ¹³¹I (T₁/₂ = 8.02 days). The sample is used 30.0 days after it was prepared. How much ¹³¹I remains?

**Approach:** Mass is proportional to number of nuclei. Mass = initial mass × (1/2)^(t/T₁/₂).

**Step 1:** n = 30.0/8.02 = 3.741 half-lives.
Fraction = (1/2)^3.741 = 2^(−3.741) = 0.0748.

**Step 2:** Remaining mass = 2.50 × 0.0748 = 0.187 μg.

**Why this makes sense:** After ~3.74 half-lives, about 7.5% remains. 7.5% of 2.50 μg = 0.188 μg. The exponential decay applies to mass just as it does to the number of nuclei and activity.

---

### Example 5: Equivalent Dose

A person of mass 70 kg absorbs 2.0 × 10⁻³ J of energy from alpha radiation uniformly throughout their body. (a) Calculate the absorbed dose in Gy. (b) Calculate the equivalent dose in Sv. (Radiation weighting factor for alpha = 20.)

**Approach:** Absorbed dose = energy/mass. Equivalent dose = absorbed dose × w_R.

**Step 1:** D = 2.0 × 10⁻³ / 70 = 2.86 × 10⁻⁵ Gy.

**Step 2:** H = D × w_R = 2.86 × 10⁻⁵ × 20 = 5.71 × 10⁻⁴ Sv = 0.571 mSv.

**Why this makes sense:** This is about 1/5 of the average annual background dose. It's a small but measurable amount. The factor of 20 for alpha radiation reflects its high biological effectiveness — alpha particles create dense ionization tracks that cause more DNA damage per unit energy than beta or gamma radiation.

---

## Practice Problems

### Problem 1
A radioactive isotope has a half-life of 14.0 hours. (a) Calculate the decay constant in s⁻¹. (b) A sample has an initial activity of 5.00 × 10⁴ Bq. Calculate the activity after 2.00 days. (c) How long will it take for the activity to drop below 100 Bq?

### Problem 2
An archaeological sample of bone contains 0.125 Bq of ¹⁴C per gram of carbon. Living bone contains 0.230 Bq/g. The half-life of ¹⁴C is 5730 years. (a) Estimate the age of the bone. (b) Explain two assumptions made in this calculation. (c) Suggest why carbon dating cannot be used for a sample believed to be 200,000 years old.

### Problem 3
A sample of ²³⁸U has a mass of 10.0 g. The half-life is 4.47 × 10⁹ years. (a) Calculate the number of ²³⁸U atoms in the sample. (b) Calculate the decay constant in s⁻¹. (c) Calculate the activity of the sample in Bq. (d) Explain why this sample is only very weakly radioactive despite containing 10 g of a radioactive material.

### Problem 4
A patient receives an injection of a radioactive tracer with half-life 6.0 hours and initial activity 4.0 × 10⁶ Bq. The tracer is eliminated from the body with a biological half-life of 10.0 hours (in addition to the physical decay). The effective half-life T_eff is given by 1/T_eff = 1/T_phys + 1/T_bio. (a) Calculate the effective half-life. (b) Calculate the activity in the patient's body after 12.0 hours. (c) Explain why the effective half-life is shorter than either the physical or biological half-life.

### Problem 5
Describe the main sources of natural background radiation and explain why background radiation levels vary with geographical location and altitude. Include quantitative estimates of typical doses.

### Problem 6 (IB Exam Style)
The isotope potassium-40 (⁴⁰K), which has a half-life of 1.25 × 10⁹ years, is a significant source of natural background radiation. It decays by β⁻ emission to calcium-40 (89.3%) and by electron capture to argon-40 (10.7%).

(a) Write the nuclear equation for the β⁻ decay of ⁴⁰K. [1 mark]

(b) Show that the decay constant of ⁴⁰K is approximately 1.76 × 10⁻¹⁷ s⁻¹. [2 marks]

(c) The human body contains about 140 g of potassium, of which 0.0117% is ⁴⁰K. Calculate: (i) the number of ⁴⁰K atoms in the body, (ii) the activity of ⁴⁰K in the body. [4 marks]

(d) The average absorbed dose rate from ⁴⁰K in the body is about 0.18 mGy per year. The radiation weighting factor for β⁻ particles is 1. Calculate the equivalent dose in mSv per year. [1 mark]

(e) Carbon-14 dating was used to determine the age of the Shroud of Turin. (i) Explain the principle of carbon-14 dating. (ii) State one assumption made in carbon-14 dating and explain how it might affect the accuracy of the result. [4 marks]

---

## Answers

### Answer 1
(a) T₁/₂ = 14.0 h = 5.04 × 10⁴ s. λ = 0.6931 / (5.04 × 10⁴) = 1.375 × 10⁻⁵ s⁻¹.

(b) t = 2.00 days = 48.0 h. n = 48.0/14.0 = 3.429 half-lives.
A = 5.00 × 10⁴ × (1/2)^3.429 = 5.00 × 10⁴ × 0.0928 = 4.64 × 10³ Bq.
Or: λt = 1.375 × 10⁻⁵ × 1.728 × 10⁵ = 2.376. e⁻²·³⁷⁶ = 0.0929. A = 5.00 × 10⁴ × 0.0929 = 4.65 × 10³ Bq. ✓

(c) A = A₀(1/2)^(t/T₁/₂) → 100 = 5.00 × 10⁴ (1/2)^(t/14.0).
(1/2)^(t/14.0) = 100/50000 = 0.002.
t/14.0 = log₂(500) = ln(500)/ln(2) = 6.215/0.6931 = 8.97.
t = 8.97 × 14.0 = 125.6 h ≈ 5.23 days.

### Answer 2
(a) A₀/A = 0.230/0.125 = 1.84.
t = (5730/0.6931) × ln(1.84) = 8267 × 0.6098 = 5040 years.

(b) Assumptions: (i) The atmospheric ¹⁴C/¹²C ratio has been constant over the past ~5000 years. In reality, it has varied due to changes in cosmic ray flux and solar activity. Calibration using tree-ring data corrects for this. (ii) The sample has not been contaminated with modern carbon (which would increase the ¹⁴C/¹²C ratio, making it appear younger) or ancient carbon (making it appear older). Proper sample preparation and cleaning minimize this.

(c) After 200,000 years, the number of half-lives elapsed is 200,000/5730 ≈ 34.9. The fraction of ¹⁴C remaining would be (1/2)^34.9 ≈ 3 × 10⁻¹¹. This is far too small to measure — the ¹⁴C signal would be buried in background noise. Additionally, at such low levels, even the tiniest contamination would dominate the measurement. The practical upper limit for carbon dating is about 50,000 years (roughly 9 half-lives, ~0.2% remaining).

### Answer 3
(a) Molar mass of ²³⁸U = 238 g/mol. n = 10.0/238 = 0.04202 mol.
N = 0.04202 × 6.022 × 10²³ = 2.53 × 10²² atoms.

(b) T₁/₂ = 4.47 × 10⁹ × 365 × 24 × 3600 = 1.410 × 10¹⁷ s.
λ = 0.6931 / (1.410 × 10¹⁷) = 4.92 × 10⁻¹⁸ s⁻¹.

(c) A = λN = 4.92 × 10⁻¹⁸ × 2.53 × 10²² = 1.24 × 10⁵ Bq.

(d) Despite containing 10 g of radioactive material, the sample is only weakly radioactive because ²³⁸U has an extremely long half-life (4.47 billion years). The decay constant is tiny (λ ≈ 5 × 10⁻¹⁸ s⁻¹), meaning the probability of any given nucleus decaying in the next second is extremely small. The 1.24 × 10⁵ Bq (124 kBq) might seem large, but for 10 g of material with 2.53 × 10²² nuclei, it means only about 1 in 2 × 10¹⁷ nuclei decays each second. The specific activity (activity per gram) is only 12.4 kBq/g, compared to, say, ¹³¹I at ~4.6 × 10¹⁵ Bq/g.

### Answer 4
(a) 1/T_eff = 1/6.0 + 1/10.0 = 0.1667 + 0.1000 = 0.2667.
T_eff = 1/0.2667 = 3.75 h.

(b) t = 12.0 h. n = 12.0/3.75 = 3.2 half-lives.
A = 4.0 × 10⁶ × (1/2)^3.2 = 4.0 × 10⁶ × 0.1088 = 4.35 × 10⁵ Bq.

(c) The effective half-life is shorter because the radioactive material is being removed from the body by TWO simultaneous processes: physical radioactive decay AND biological elimination (excretion, metabolism). Each process independently reduces the amount present, so the combined removal rate is the sum of the individual rates. The effective decay constant is λ_eff = λ_phys + λ_bio, which is larger than either alone, giving a shorter effective half-life. This is why effective half-life is always shorter than the shorter of the physical and biological half-lives.

### Answer 5
Natural background radiation has four main sources:

1. **Radon gas (~50% of natural, ~1.3 mSv/year average):** Radon-222, a radioactive gas from uranium decay in soil and rock, seeps into buildings. Highly variable geographically — areas with granite or uranium-rich soil have higher levels. Indoor concentrations depend on building ventilation and foundation sealing.

2. **Terrestrial gamma radiation (~15% of natural, ~0.5 mSv/year):** From radioactive isotopes (⁴⁰K, ²³⁸U, ²³²Th series) in rocks and soil. Varies with local geology: granite areas (e.g., parts of Scotland, Cornwall, Brazil) have 3-5× higher levels; limestone areas have lower levels. Some regions (Kerala, India; Ramsar, Iran) have extremely high natural background due to thorium-rich monazite sands — up to 30-260 mSv/year.

3. **Cosmic radiation (~15% of natural, ~0.3 mSv/year at sea level):** High-energy particles from space. Dose approximately doubles every 1500 m increase in altitude. Denver, Colorado (~1600 m) receives about twice the sea-level cosmic dose. Airline flights at 10,000 m altitude receive ~100× the sea-level rate — a transatlantic flight gives ~0.05 mSv.

4. **Internal radiation (~10% of natural, ~0.3 mSv/year):** From ⁴⁰K naturally present in our bodies and ¹⁴C in all organic matter. The potassium in our bodies (essential for nerve function) includes radioactive ⁴⁰K at 0.0117% abundance. A 70 kg person has ~9000 Bq of ⁴⁰K, producing a constant internal dose.

The total average worldwide: ~3 mSv/year, with a typical range of 1-13 mSv/year depending on location and altitude. No health effects have been conclusively demonstrated at these levels.

### Answer 6
(a) ⁴⁰₁₉K → ⁴⁰₂₀Ca + e⁻ + ν̄_e (antineutrino).

(b) T₁/₂ = 1.25 × 10⁹ × 365 × 24 × 3600 = 3.942 × 10¹⁶ s.
λ = ln 2 / T₁/₂ = 0.6931 / (3.942 × 10¹⁶) = 1.758 × 10⁻¹⁷ s⁻¹ ≈ 1.76 × 10⁻¹⁷ s⁻¹.

(c) (i) Mass of ⁴⁰K = 140 × 0.000117 = 0.01638 g.
n = 0.01638/40 = 4.095 × 10⁻⁴ mol.
N = 4.095 × 10⁻⁴ × 6.022 × 10²³ = 2.466 × 10²⁰ atoms.

(ii) A = λN = 1.758 × 10⁻¹⁷ × 2.466 × 10²⁰ = 4.34 × 10³ Bq = 4340 Bq.

(d) H = D × w_R = 0.18 mGy × 1 = 0.18 mSv per year. This is a small fraction (~6%) of the average annual background dose of ~3 mSv.

(e) (i) Carbon-14 dating is based on the decay of radioactive ¹⁴C (T₁/₂ = 5730 years). While an organism is alive, it continuously exchanges carbon with the atmosphere, maintaining an equilibrium ¹⁴C/¹²C ratio equal to the atmospheric ratio. When the organism dies, exchange stops, and ¹⁴C decays without replacement. By measuring the current ¹⁴C/¹²C ratio in the organic remains and comparing it to the known initial ratio, the time since death can be calculated using the exponential decay law: N = N₀ e^(−λt).

(ii) Key assumption: The atmospheric ¹⁴C/¹²C ratio has been constant over time. In reality, it has varied due to changes in the Earth's magnetic field (affecting cosmic ray flux), solar activity, and, in modern times, the Suess effect (dilution by fossil fuel CO₂, which contains no ¹⁴C) and nuclear weapons testing (which added ¹⁴C). These variations can affect the accuracy of uncorrected carbon dates. Calibration curves using dendrochronology (tree-ring dating) correct for these variations — each tree ring's absolute age is known, and its ¹⁴C content is measured to create a calibration curve. This allows "radiocarbon years" to be converted to calibrated calendar years, significantly improving accuracy.

---

## Key Takeaways

1. The exponential decay law: N = N₀ e^(−λt), A = A₀ e^(−λt). Equivalent form: N = N₀ (1/2)^(t/T₁/₂).

2. To solve for time: t = (T₁/₂/ln 2) × ln(N₀/N) = (T₁/₂/ln 2) × ln(A₀/A).

3. Carbon-14 dating uses the decay of ¹⁴C (T₁/₂ = 5730 years) to date organic materials up to ~50,000 years old. It assumes constant atmospheric ¹⁴C ratio (corrected by calibration) and no sample contamination.

4. Background radiation (~85% natural, ~15% artificial) comes from radon, terrestrial sources, cosmic rays, internal isotopes, and medical procedures. Average world dose: ~3 mSv/year.

5. Equivalent dose (Sv) = absorbed dose (Gy) × radiation weighting factor (w_R). Alpha particles have w_R = 20; beta, gamma, and X-rays have w_R = 1.

6. The effective half-life for biological systems includes both physical decay and biological elimination: 1/T_eff = 1/T_phys + 1/T_bio.
