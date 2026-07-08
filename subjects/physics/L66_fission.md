# Lesson 66: Fission — Chain Reactions, Binding Energy Curve, and Nuclear Reactors

## What You'll Learn

In 1938, two German chemists (Otto Hahn and Fritz Strassmann) bombarded uranium with neutrons and detected barium in the products. Their colleague Lise Meitner (a physicist who had fled Nazi Germany) realized what had happened: the uranium nucleus had SPLIT. Nuclear fission had been discovered.

This lesson explains what fission is, WHY it releases energy (the binding energy curve is the key), how a single splitting nucleus can trigger a chain reaction that releases enormous amounts of energy, and how nuclear reactors harness this process for peaceful purposes. You'll learn the physics behind both nuclear power and nuclear weapons, and understand why certain isotopes can sustain chain reactions while others cannot.

---

## 1. What Is Nuclear Fission?

### Why This Matters

Fission is the process that powers nuclear reactors and nuclear weapons. It's fundamentally different from chemical reactions like burning coal. One fission event releases about 200 MeV of energy — roughly 50 million times more than burning one carbon atom. Understanding fission means understanding the most concentrated energy source humanity has ever harnessed.

### The Key Ideas

**Definition.** **Nuclear fission** is the splitting of a heavy nucleus into two (or occasionally three) lighter nuclei, accompanied by the release of energy and usually several neutrons. The products are called **fission fragments**. The process can be spontaneous (very rare) or induced by neutron capture.

**A typical fission reaction.** When uranium-235 captures a slow neutron, it becomes uranium-236 in an excited state. The excited ²³⁶U nucleus oscillates wildly, deforms into an elongated shape, and splits. A typical fission yields:

$${}^{235}_{92}\text{U} + n \rightarrow {}^{141}_{56}\text{Ba} + {}^{92}_{36}\text{Kr} + 3n + \text{energy}$$

This is ONE possible outcome. Fission is a messy process — the exact products vary. The mass distribution of fission fragments shows two peaks around A ≈ 95 and A ≈ 140 (asymmetric fission is more common than symmetric splitting into two equal fragments).

**Energy released: ~200 MeV per fission.** Where does this energy go?
- Kinetic energy of fission fragments: ~165 MeV
- Kinetic energy of prompt neutrons: ~5 MeV
- Gamma rays (prompt): ~7 MeV
- Beta particles and gamma rays from fission product decay: ~20 MeV
- Neutrinos (from beta decay): ~10 MeV (these escape and are unrecoverable)

**The source of the energy: the binding energy curve.** Why does splitting a heavy nucleus release energy? The answer is the most important graph in nuclear physics.

---

## 2. The Binding Energy Curve

### Why This Matters

The binding energy curve is the Rosetta Stone of nuclear physics. It explains why fission releases energy for heavy nuclei, why fusion releases energy for light nuclei, why iron is the most stable element, and why the universe has the elemental abundances it does. If you understand this curve, you understand why stars shine and why nuclear reactors work.

### The Key Ideas

**What is binding energy?** The **binding energy** of a nucleus is the energy required to separate it into its individual protons and neutrons. It is also the energy RELEASED when the nucleus forms from free nucleons. A larger binding energy means a more tightly bound, more stable nucleus.

Because E = mc², the mass of a nucleus is LESS than the sum of the masses of its individual nucleons. This **mass defect** Δm is converted to binding energy:

$$E_{\text{binding}} = \Delta m \, c^2$$

For example, a helium-4 nucleus (²He) consists of 2 protons and 2 neutrons:
Mass of 2 protons + 2 neutrons = 2(1.007276 u) + 2(1.008665 u) = 4.031882 u
Actual mass of ²He nucleus = 4.002603 u
Mass defect Δm = 0.029279 u
Binding energy = 0.029279 u × 931.5 MeV/u = 27.27 MeV

**Binding energy per nucleon.** A more useful quantity is the **binding energy per nucleon** (BE/A) — the total binding energy divided by the number of nucleons. This tells you how tightly bound the AVERAGE nucleon is in that nucleus.

**The curve.** Plot BE/A (y-axis) against mass number A (x-axis):

- BE/A rises steeply from low A, reaching a broad maximum around A = 56-62 (iron and nickel).
- BE/A for iron-56 is about 8.79 MeV per nucleon — the highest of any nucleus.
- Beyond iron, BE/A gradually decreases, falling to about 7.6 MeV per nucleon for uranium.

**What the curve tells us:**

1. **Light nuclei gain BE/A by fusing.** If you fuse two very light nuclei (low BE/A) into a heavier one (higher BE/A), the products are more tightly bound, and energy is released. This is nuclear FUSION.

2. **Heavy nuclei gain BE/A by splitting.** If you split a very heavy nucleus (BE/A ≈ 7.6 MeV) into two medium-mass nuclei (BE/A ≈ 8.5 MeV), the products are more tightly bound, and energy is released. This is nuclear FISSION.

3. **Iron-56 is the "dead end."** Neither fusion nor fission can extract energy from iron-56 — it's already at the peak of the binding energy curve. You can't gain binding energy per nucleon by fusing iron or splitting iron. This is why the cores of massive stars accumulate iron before they collapse — the star runs out of nuclear fuel.

**Why fission releases ~200 MeV.** For uranium-235 (A = 235, BE/A ≈ 7.6 MeV/nucleon):
Total binding energy of ²³⁵U: 235 × 7.6 ≈ 1786 MeV.
Two medium-mass fission fragments (A ≈ 95 and 140): BE/A ≈ 8.5 MeV/nucleon.
Total binding energy of fragments: 95 × 8.5 + 140 × 8.5 ≈ 1998 MeV.
Energy released = 1998 − 1786 ≈ 212 MeV (close to the measured ~200 MeV, considering approximations).

The energy released per fission, while enormous on the atomic scale, is tiny in joules: 200 MeV = 3.2 × 10⁻¹¹ J. But for 1 gram of ²³⁵U undergoing complete fission: (N_A/235) × 3.2 × 10⁻¹¹ = 2.56 × 10²¹ × 3.2 × 10⁻¹¹ ≈ 8.2 × 10¹⁰ J ≈ 23,000 kWh — the energy equivalent of burning about 2.7 tonnes of coal.

### Common Misconceptions

**"Fission and fusion both release energy because they're 'nuclear,' regardless of which elements are involved."** This is FALSE and it's a critical misconception. Fission releases energy ONLY for heavy nuclei (above iron on the binding energy curve). Fusion releases energy ONLY for light nuclei (below iron). Both processes move products TOWARD the peak of the binding energy curve (iron-56). Fission of a light nucleus would CONSUME energy. Fusion of heavy nuclei would CONSUME energy. The direction that releases energy is always toward greater binding energy per nucleon.

**"Binding energy is the energy that holds the nucleus together."** The binding energy IS the energy that holds the nucleus together — it's the energy you would need to ADD to pull the nucleus apart. But the binding energy per nucleon curve shows the energy ALREADY released when those nucleons came together. A higher BE/A means more energy was released per nucleon during the nucleus's formation (and more energy would be needed to pull it apart).

---

## 3. Chain Reactions

### Why This Matters

A single fission releases ~200 MeV — about 3.2 × 10⁻¹¹ J. That's a completely negligible amount of energy. What makes fission useful (or dangerous) is the possibility of a **chain reaction**: the neutrons released by one fission can induce further fissions, which release more neutrons, and so on. If each fission causes, on average, one more fission, the reaction is self-sustaining and can produce steady power. If each fission causes more than one, the reaction grows exponentially — this is the principle of nuclear weapons.

### The Key Ideas

**The chain reaction mechanism.** Fission of ²³⁵U releases, on average, about 2.5 neutrons. These neutrons can:
1. Cause another ²³⁵U nucleus to fission (sustaining the chain).
2. Be absorbed by ²³⁸U without causing fission (²³⁸U captures neutrons to become ²³⁹U, which beta-decays to ²³⁹Pu).
3. Escape from the system entirely (leakage).
4. Be absorbed by control rods or other structural materials.

**The multiplication factor k.** The **neutron multiplication factor** k (also called k_eff) is the average number of neutrons from one fission that go on to cause another fission.

- k < 1: subcritical — the reaction dies out.
- k = 1: critical — the reaction is self-sustaining at a constant rate. This is the operating condition for a nuclear reactor.
- k > 1: supercritical — the reaction grows exponentially. This is what happens in a nuclear weapon (deliberately) or a nuclear accident (unintentionally).

**Critical mass.** The **critical mass** is the minimum mass of fissile material needed to sustain a chain reaction. If the mass is too small, too many neutrons escape through the surface before causing fissions — the surface-to-volume ratio is too high. The critical mass depends on:
- The isotope (²³⁵U: ~50 kg for bare sphere; ²³⁹Pu: ~10 kg)
- The shape (sphere minimizes surface area)
- The presence of a neutron reflector (surrounding the material with a material that reflects neutrons back inward)
- The density (compression increases density, reducing the mean free path of neutrons and thus the critical mass)

**Enrichment.** Natural uranium is only 0.72% ²³⁵U (the rest is ²³⁸U, which doesn't sustain a chain reaction with slow neutrons). Most reactors require uranium "enriched" to 3-5% ²³⁵U. Weapons-grade uranium is enriched to >90% ²³⁵U.

### Common Misconceptions

**"A nuclear reactor can explode like a nuclear bomb."** No. The enrichment and design of a reactor make a nuclear explosion physically impossible. Reactor fuel is 3-5% ²³⁵U; bomb fuel is >90%. A reactor can experience a steam explosion or hydrogen explosion (as at Chernobyl and Fukushima), which can rupture the containment and spread radioactive material, but there is no mechanism for a nuclear detonation in a power reactor.

**"The chain reaction is uncontrolled in a reactor."** No. Reactors are carefully controlled to maintain k = 1. Control rods made of neutron-absorbing materials (boron, cadmium, hafnium) are inserted to reduce k and withdrawn to increase it. The reactor operates at exactly critical, with k maintained at 1.0000 by automatic control systems.

---

## 4. Nuclear Reactors

### Why This Matters

Nuclear power provides about 10% of the world's electricity from about 440 reactors in 32 countries. Understanding how a reactor works — the fuel, the moderator, the control systems, and the safety features — is essential for evaluating the role of nuclear energy in addressing climate change and energy security.

### The Key Ideas

**Core components of a thermal nuclear reactor:**

1. **Fuel:** Usually uranium dioxide (UO₂) pellets enriched to 3-5% ²³⁵U, sealed in zirconium alloy tubes (fuel rods). The fuel rods are assembled into bundles.

2. **Moderator:** Fission neutrons are "fast" — they're born with ~2 MeV of kinetic energy. But ²³⁵U is much more likely to fission with SLOW ("thermal") neutrons (~0.025 eV). The moderator slows the neutrons down through elastic collisions. Good moderators use light nuclei (so neutrons lose more energy per collision) and have low neutron absorption:
   - Water (H₂O): Most common moderator. Light hydrogen nuclei are excellent at slowing neutrons, but hydrogen also absorbs some neutrons. This is why light-water reactors need enriched uranium.
   - Heavy water (D₂O): Deuterium absorbs far fewer neutrons than ordinary hydrogen, so heavy-water reactors (like CANDU) can use natural (unenriched) uranium.
   - Graphite (carbon): Used in early reactors (and the Chernobyl RBMK design). Does not absorb many neutrons but is flammable at very high temperatures.

3. **Control rods:** Made of neutron-absorbing materials (boron carbide, cadmium, hafnium, or silver-indium-cadmium alloy). Inserted into the core to absorb neutrons and reduce k; withdrawn to increase k. In an emergency, control rods are rapidly inserted ("SCRAM") to shut down the chain reaction.

4. **Coolant:** Removes heat from the core and transfers it to a steam generator (in PWRs) or directly to a turbine (in BWRs). Common coolants: water, heavy water, carbon dioxide, helium, liquid sodium.

5. **Containment:** A thick reinforced concrete and steel structure that encloses the reactor. Designed to withstand internal pressures from accidents and external impacts.

**Types of reactors:**
- **Pressurized Water Reactor (PWR):** The most common type. Water at high pressure (~150 atm) serves as both moderator and coolant. The primary loop transfers heat to a secondary loop where steam is generated.
- **Boiling Water Reactor (BWR):** Water boils directly in the core, and the steam drives the turbine. Simpler design but the turbine becomes radioactive.
- **CANDU (CANada Deuterium Uranium):** Uses heavy water moderator, allowing natural uranium fuel. Can be refueled while operating.

**Fertile materials and breeder reactors.** ²³⁸U (99.3% of natural uranium) is not fissile — it doesn't fission with slow neutrons. But when ²³⁸U captures a neutron, it becomes ²³⁹U, which beta-decays (half-life 23.5 min) to ²³⁹Np, which beta-decays (half-life 2.36 days) to ²³⁹Pu, which IS fissile. A breeder reactor produces MORE fissile material (²³⁹Pu) than it consumes, by surrounding the core with a "blanket" of ²³⁸U.

### Common Misconceptions

**"Nuclear waste is all dangerously radioactive for millions of years."** Most fission products have half-lives of seconds to decades. The ones that matter for long-term storage are a handful of isotopes with half-lives of thousands to millions of years (like ⁹⁹Tc, 211,000 yr), plus the transuranic elements (plutonium, americium, curium). High-level waste is intensely radioactive for the first few hundred years, after which the activity drops significantly. The long-lived components have lower activity and are primarily an ingestion/inhalation hazard, not an external radiation hazard.

---

### The Oklo Natural Reactor

About 2 billion years ago, in what is now Gabon, Africa, a natural nuclear reactor operated spontaneously. At Oklo, uranium deposits in the rock became critical when groundwater moderated neutrons. The reactor ran intermittently for hundreds of thousands of years, producing about 100 kW of thermal power.

How was this possible? Two billion years ago, the isotopic abundance of ²³⁵U was about 3% (compared to 0.72% today) because ²³⁵U decays faster than ²³⁸U (half-life 0.70 billion years vs. 4.47 billion years). With 3% enrichment and groundwater as moderator, natural uranium deposits could reach criticality.

The Oklo reactor is evidence that the laws of physics haven't changed over billions of years. The fission product distribution and neutron capture cross-sections inferred from the Oklo rocks match modern measurements perfectly. This is an extraordinary confirmation that nuclear physics constants have been stable over cosmological timescales.

### Why Nuclear Waste Is Challenging

Spent nuclear fuel contains a complex mixture of radioactive isotopes:

- **Fission products:** ⁹⁰Sr (T₁/₂ = 29 years), ¹³⁷Cs (30 years), ⁹⁹Tc (211,000 years), ¹²⁹I (15.7 million years). These are mostly beta/gamma emitters. The 30-year half-life isotopes dominate the radiation hazard for the first few hundred years.
- **Transuranic elements:** ²³⁹Pu (24,100 years), ²⁴⁰Pu (6,560 years), ²⁴¹Am (432 years). These are alpha emitters produced by neutron capture on ²³⁸U. They dominate the long-term radiotoxicity.

The "high-level waste" challenge: after ~300 years of cooling in storage pools, the short-lived fission products have decayed significantly. What remains is primarily the transuranic elements and long-lived fission products, which need isolation for ~10,000-100,000 years. This is the timescale for geological disposal — burying the waste deep underground in stable rock formations.

Reprocessing (chemically separating plutonium and uranium from spent fuel) can reduce the waste volume and recover fissile material, but it raises proliferation concerns because separated plutonium could be diverted for weapons.

---

### Separated Isotopes and Enrichment

Naturally occurring elements consist of isotopic mixtures, but for many applications, specific isotopes are needed. **Isotope separation** (enrichment) is the process of increasing the proportion of a particular isotope. 

Methods include:
- **Gas diffusion:** UF₆ gas is forced through porous membranes. Lighter ²³⁵UF₆ diffuses slightly faster than ²³⁸UF₆. Repeating thousands of times achieves the desired enrichment.
- **Gas centrifugation:** UF₆ gas is spun at extremely high speeds (~50,000-70,000 rpm). The heavier ²³⁸UF₆ concentrates at the outer wall; the lighter ²³⁵UF₆ concentrates near the center. This is the dominant method today.
- **Mass spectrometry:** Ionized atoms are deflected by magnetic fields. Different isotopes follow paths with slightly different radii. Used for small-scale separation (like producing radioisotopes for medicine).

The enrichment level determines use:
- Natural uranium (0.72% ²³⁵U): CANDU reactors (with heavy water moderator)
- Low-enriched uranium (3-5% ²³⁵U): Most power reactors (PWR, BWR)
- Highly enriched uranium (>20% ²³⁵U): Research reactors, naval propulsion
- Weapons-grade uranium (>90% ²³⁵U): Nuclear weapons

The same technology that enriches uranium for reactors can be used to produce weapons-grade material — this is the central challenge of nuclear non-proliferation. The distinction between peaceful and weapons applications is political, not technological.

---

## Worked Examples

### Example 1: Energy from Fission

Calculate the energy released when 1.00 kg of ²³⁵U undergoes complete fission. Assume 200 MeV per fission.

**Approach:** Find number of nuclei, multiply by energy per fission.

**Step 1:** N = (1.00 × 10³ g / 235 g/mol) × 6.022 × 10²³ = 2.563 × 10²⁴ nuclei.

**Step 2:** E = 2.563 × 10²⁴ × 200 MeV = 5.126 × 10²⁶ MeV.
Convert to joules: 5.126 × 10²⁶ × 1.60 × 10⁻¹³ = 8.20 × 10¹³ J.

**Why this makes sense:** This is about 8.2 × 10¹³ J, which is the energy equivalent of burning ~2,700 tonnes of coal or ~20 kilotons of TNT. The energy density of nuclear fuel is about 2 million times that of chemical fuel.

---

### Example 2: Binding Energy per Nucleon

Calculate the binding energy per nucleon for iron-56. The mass of ⁵⁶Fe is 55.934937 u. The mass of a proton is 1.007276 u and the mass of a neutron is 1.008665 u.

**Approach:** Δm = (Z·m_p + N·m_n) − m_nucleus. Then E = Δm c² with 1 u = 931.5 MeV/c².

**Step 1:** ⁵⁶Fe has Z = 26, N = 30.
Sum of nucleon masses = 26 × 1.007276 + 30 × 1.008665 = 26.18918 + 30.25995 = 56.44913 u.

**Step 2:** Δm = 56.44913 − 55.93494 = 0.51419 u.

**Step 3:** E = 0.51419 × 931.5 = 479.0 MeV.
BE/A = 479.0 / 56 = 8.55 MeV/nucleon.

(The accepted value is ~8.79 MeV/nucleon. The difference arises because we used the mass of the neutral iron-56 ATOM, which includes 26 electrons, and the masses of protons (hydrogen atoms) include electrons. A more careful calculation accounting for electron binding energies gives the accepted value.)

---

### Example 3: Energy from Mass Defect

In the fission reaction: n + ²³⁵U → ¹⁴¹Ba + ⁹²Kr + 3n, the masses are:
²³⁵U: 235.0439 u
n: 1.008665 u
¹⁴¹Ba: 140.9144 u
⁹²Kr: 91.9262 u
Calculate the energy released in MeV.

**Approach:** Total mass before − total mass after = Δm. E = Δm c².

**Step 1:** Mass before: 235.0439 + 1.0087 = 236.0526 u.
Mass after: 140.9144 + 91.9262 + 3 × 1.0087 = 140.9144 + 91.9262 + 3.0260 = 235.8666 u.

**Step 2:** Δm = 236.0526 − 235.8666 = 0.1860 u.

**Step 3:** E = 0.1860 × 931.5 = 173.3 MeV.

**Why this makes sense:** This is in the 200 MeV ballpark. The exact energy depends on the specific fission products. Some energy also appears as gamma rays and delayed beta decays, bringing the total to ~200 MeV. The 173 MeV here is just the prompt energy from this particular fission channel.

---

### Example 4: Critical Mass Concept

Explain why a subcritical mass of ²³⁵U cannot sustain a chain reaction, and how a critical mass is achieved in a nuclear weapon.

**Approach:** Surface-to-volume ratio argument. Two techniques: gun-type and implosion.

**Explanation:** A subcritical mass is too small for a chain reaction because the surface-to-volume ratio is too high — too many neutrons escape through the surface before they can cause further fissions. The neutron multiplication factor k < 1.

Nuclear weapons achieve supercriticality by:
- **Gun-type (Hiroshima bomb):** Two subcritical pieces of ²³⁵U are brought together rapidly using a conventional explosive charge. Once combined, the mass exceeds critical, and the chain reaction multiplies exponentially until the energy released blows the assembly apart.
- **Implosion (Nagasaki bomb, modern weapons):** A subcritical sphere of plutonium is surrounded by conventional high explosives arranged to produce an inwardly directed shock wave. The shock wave compresses the plutonium, increasing its density. Since critical mass is inversely proportional to the square of density, compression dramatically reduces the critical mass, making the sphere highly supercritical.

---

### Example 5: Reactor Power

A nuclear reactor operates at a thermal power of 3000 MW. Assuming 200 MeV per fission and that the energy is entirely from fission, calculate: (a) the number of fissions per second, (b) the mass of ²³⁵U consumed per day.

**Approach:** Power = energy per fission × fissions per second.

**Step 1:** Energy per fission = 200 MeV = 3.20 × 10⁻¹¹ J.
Fissions/s = 3000 × 10⁶ J/s / (3.20 × 10⁻¹¹ J) = 9.375 × 10¹⁹ fissions/s.

**Step 2:** Number of fissions per day = 9.375 × 10¹⁹ × 86400 = 8.10 × 10²⁴.
Moles = 8.10 × 10²⁴ / (6.022 × 10²³) = 13.45 mol.
Mass = 13.45 × 235 = 3160 g ≈ 3.16 kg/day.

**Why this makes sense:** A 3000 MW thermal reactor consumes about 3 kg of ²³⁵U per day. A coal plant of the same power would burn about 10,000 tonnes per day — a factor of ~3 million. This enormous difference in fuel consumption is why nuclear power, despite its challenges, remains a significant energy source.

---

## Practice Problems

### Problem 1
Calculate the binding energy per nucleon of uranium-238. The atomic mass of ²³⁸U is 238.05079 u. (m_p = 1.007276 u, m_n = 1.008665 u.)

### Problem 2
A nuclear reactor consumes 2.50 kg of ²³⁵U per day through fission, with each fission releasing approximately 200 MeV. (a) Calculate the total energy released per day in joules. (b) Calculate the average thermal power output in MW. (c) If the plant's electrical efficiency is 33%, calculate the electrical power output.

### Problem 3
Explain why: (a) ²³⁵U can sustain a chain reaction with slow neutrons but ²³⁸U cannot. (b) A moderator is necessary in most reactors. (c) Nuclear reactors must be carefully controlled to maintain k ≈ 1.

### Problem 4
Using the binding energy per nucleon curve, explain: (a) Why fission of ²³⁵U releases energy. (b) Why fusion of hydrogen to helium releases energy. (c) Why neither fission nor fusion of iron-56 can release energy.

### Problem 5
A student says: "Nuclear power is dangerous because the reactor can explode like an atomic bomb." Evaluate this statement, explaining why a nuclear reactor cannot produce a nuclear explosion.

### Problem 6 (IB Exam Style)
The fission of uranium-235 can be induced by the absorption of a slow neutron.

(a) State what is meant by nuclear fission. [1 mark]

(b) One possible fission reaction is:
n + ²³⁵U → ¹⁴⁰Xe + ⁹⁴Sr + 2n
The masses are: ²³⁵U = 235.0439 u, ¹⁴⁰Xe = 139.9216 u, ⁹⁴Sr = 93.9154 u, n = 1.008665 u. (i) Show that the mass defect for this reaction is approximately 0.198 u. (ii) Calculate the energy released in MeV. [4 marks]

(c) On average, 2.5 neutrons are released in each fission of ²³⁵U. Explain how this enables a self-sustaining chain reaction. [2 marks]

(d) Outline the role of the following components in a nuclear reactor: (i) moderator, (ii) control rods. [4 marks]

(e) State one advantage and one disadvantage of nuclear power compared to fossil fuel power stations. [2 marks]

---

## Answers

### Answer 1
Z = 92, N = 238 − 92 = 146.
Sum of nucleon masses = 92 × 1.007276 + 146 × 1.008665 = 92.6694 + 147.2651 = 239.9345 u.
Δm = 239.9345 − 238.0508 = 1.8837 u.
E = 1.8837 × 931.5 = 1754.7 MeV.
BE/A = 1754.7 / 238 = 7.37 MeV/nucleon.

This is lower than iron's 8.79 MeV/nucleon — confirming that uranium is less tightly bound, and splitting it releases energy.

### Answer 2
(a) N = (2.50 × 10³ / 235) × 6.022 × 10²³ = 6.407 × 10²⁴ nuclei.
E = 6.407 × 10²⁴ × 200 MeV = 1.281 × 10²⁷ MeV = 2.050 × 10¹⁴ J.

(b) P_thermal = 2.050 × 10¹⁴ J / (24 × 3600 s) = 2.373 × 10⁹ W = 2373 MW.

(c) P_electrical = 0.33 × 2373 = 783 MW.

### Answer 3
(a) ²³⁵U is fissile: it undergoes fission when it captures a slow (thermal) neutron. The compound nucleus ²³⁶U has enough excitation energy to fission. ²³⁸U captures slow neutrons but the compound nucleus ²³⁹U has insufficient excitation energy to fission — it de-excites by gamma emission instead. ²³⁸U can fission with FAST neutrons (>1 MeV), but those are rare in a moderated reactor. This is why ²³⁵U sustains a chain reaction and ²³⁸U does not in a thermal reactor.

(b) Fission neutrons are born fast (~2 MeV). ²³⁵U has a much higher fission cross-section (probability) for SLOW neutrons. The moderator slows the neutrons through elastic collisions with light nuclei (hydrogen in water), increasing the probability that the next neutron interaction causes fission rather than being captured. Without a moderator, fast-neutron reactors are possible, but they require higher enrichment and different design.

(c) k = 1 means exactly one neutron from each fission goes on to cause another fission. k > 1 causes exponential growth — the reactor power would surge dangerously, potentially melting the fuel. k < 1 causes the chain reaction to die out. Maintaining k ≈ 1.0000 is achieved by fine adjustment of control rods and (in PWRs) boron concentration in the coolant. The delayed neutrons (from fission product decay) provide a crucial margin of controllability — without them, reactor control would be impossible.

### Answer 4
(a) Uranium-235 has BE/A ≈ 7.6 MeV/nucleon — relatively low. When it splits into two medium-mass fragments, those fragments have BE/A ≈ 8.5 MeV/nucleon — higher. The nucleons become more tightly bound. The difference in binding energy (about 0.9 MeV per nucleon × 235 nucleons ≈ 200 MeV) is released.

(b) Hydrogen nuclei (protons) have BE/A = 0 (they're not bound to anything). When four protons fuse to form helium-4 (BE/A = 7.07 MeV/nucleon), the nucleons go from zero binding to very tightly bound. The difference is released as energy: about 26.7 MeV per helium nucleus formed.

(c) Iron-56 sits at the PEAK of the BE/A curve (~8.79 MeV/nucleon). To move away from the peak — by fusing iron into heavier nuclei or splitting iron into lighter nuclei — would DECREASE binding energy per nucleon. That would CONSUME energy rather than release it. Iron is the most stable nucleus; you can't extract nuclear energy from it by either fission or fusion. This is why fusion in stars stops at iron.

### Answer 5
The student's statement reflects a fundamental misunderstanding. A nuclear reactor CANNOT explode like an atomic bomb. Here's why:

1. **Enrichment:** Reactor fuel is typically 3-5% ²³⁵U. Bomb-grade uranium is >90% enriched. At 3-5%, a rapid supercritical chain reaction is physically impossible — there are too many ²³⁸U atoms absorbing neutrons.

2. **Geometry and configuration:** An atomic bomb requires precisely timed assembly of a supercritical mass. A reactor's fuel is distributed in thousands of separate fuel rods with moderator and coolant between them. Even if control were completely lost, the geometry prevents the rapid exponential multiplication required for a nuclear explosion.

3. **What CAN happen:** The worst reactor accidents (Chernobyl, Fukushima) involved steam explosions, hydrogen explosions, or core meltdowns — NOT nuclear detonations. At Chernobyl, a power surge ruptured the reactor vessel and a steam explosion dispersed radioactive material. At Fukushima, hydrogen gas exploded outside the containment. These were chemical/physical explosions, not nuclear.

4. **Physics limitation:** Even in a prompt criticality event (which DID happen at Chernobyl), the energy release is limited by the Doppler broadening effect (fuel heats up, thermal motion of nuclei makes neutron capture less likely) and by the eventual dispersal of the fuel. You get a steam explosion from the rapid energy release, not a nuclear detonation.

So: nuclear reactors can be dangerous, and accidents can release radioactive material, but they cannot produce a nuclear explosion. The statement conflates two very different designs.

### Answer 6
(a) Nuclear fission is the splitting of a heavy nucleus into two (or more) lighter nuclei, accompanied by the release of energy and typically several neutrons.

(b) (i) Mass before: 235.0439 + 1.008665 = 236.052565 u.
Mass after: 139.9216 + 93.9154 + 2 × 1.008665 = 139.9216 + 93.9154 + 2.017330 = 235.854330 u.
Δm = 236.052565 − 235.854330 = 0.198235 u ≈ 0.198 u. ✓

(ii) E = 0.1982 × 931.5 = 184.6 MeV ≈ 185 MeV.

(c) Each fission releases 2-3 neutrons on average. If at least one of these neutrons goes on to induce another fission, the process becomes self-sustaining — each generation of fissions produces the neutrons for the next generation. This is a chain reaction. If k = 1, exactly one neutron per fission creates another fission, and the reaction continues at a steady rate. If k > 1, the reaction grows exponentially.

(d) (i) **Moderator:** Slows down fast fission neutrons through elastic collisions. Most reactors use water as moderator. Slow (thermal) neutrons are much more likely to cause fission in ²³⁵U than fast neutrons. The moderator material must have light nuclei (for efficient energy transfer) and low neutron absorption cross-section. Without the moderator, the chain reaction would not be sustainable at low enrichment levels.

(ii) **Control rods:** Contain materials with high neutron absorption cross-sections (boron, cadmium, hafnium). By inserting or withdrawing control rods, operators adjust the neutron multiplication factor k. Inserting rods absorbs more neutrons, decreasing k; withdrawing rods increases k. During normal operation, control rods are positioned to maintain k ≈ 1.000. In an emergency, rods are rapidly fully inserted (SCRAM) to shut down the chain reaction by making k ≪ 1.

(e) **Advantage:** Nuclear power produces extremely low greenhouse gas emissions during operation (essentially zero CO₂, unlike fossil fuel plants). It has a very high energy density — a few kg of uranium replaces thousands of tonnes of coal. It provides reliable baseload power independent of weather conditions (unlike solar and wind).

**Disadvantage:** Nuclear power produces radioactive waste that requires safe long-term storage (thousands of years for some isotopes). There are risks of severe accidents (though very rare) that can contaminate large areas, as at Chernobyl and Fukushima. The capital costs of building nuclear plants are very high. There are also proliferation concerns related to the fuel cycle.

---

## Key Takeaways

1. Nuclear fission is the splitting of a heavy nucleus (typically ²³⁵U) by neutron capture, releasing ~200 MeV, fission fragments, and 2-3 neutrons.

2. The binding energy per nucleon curve explains WHY fission releases energy: heavy nuclei have lower BE/A, so splitting them into medium-mass nuclei (higher BE/A) releases the difference.

3. A chain reaction occurs when neutrons from one fission induce further fissions. The multiplication factor k determines whether the reaction is subcritical (k < 1), critical (k = 1), or supercritical (k > 1).

4. Critical mass depends on isotope, enrichment, shape, density, and the presence of reflectors. ²³⁵U requires ~50 kg (bare sphere); ²³⁹Pu requires ~10 kg.

5. A nuclear reactor consists of fuel (enriched uranium), moderator (to slow neutrons), control rods (to regulate k), coolant (to remove heat), and containment. The most common type is the PWR.

6. Fission releases energy only for heavy nuclei (moving TOWARD iron on the BE/A curve). Fusion releases energy only for light nuclei. Iron-56, at the peak, can release energy by neither process.
