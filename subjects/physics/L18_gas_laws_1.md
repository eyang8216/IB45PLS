# Lesson 18: Gas Laws 1 — The Ideal Gas Model, Moles, and Avogadro

## What You'll Learn

Gases are everywhere: the air you breathe, the helium in a party balloon, the steam from a boiling kettle. Despite being made of particles so small you can never see them directly, gases follow surprisingly simple and universal rules. To understand these rules, we first need a way to count gas particles (they're too numerous to count one by one!) and a simplified model of how they behave. In this lesson, you will learn about the **ideal gas model**, the concept of the **mole** as a counting unit, and **Avogadro's constant** — the bridge between the microscopic world of atoms and the macroscopic world of measurable quantities. This is the foundation upon which all gas laws are built.

---

## 1. What Is an Ideal Gas?

### Why This Matters

Real gases — the actual oxygen, nitrogen, and other gases in our atmosphere — are complicated. Their particles have finite size, attract each other at close range, and sometimes react chemically. If we tried to account for all these details, every gas problem would be impossibly complex. Instead, physicists use a simplified model called the **ideal gas**. This model strips away all the complications and captures the essential behavior that all gases share. Remarkably, at everyday temperatures and pressures, real gases behave very nearly like ideal gases, so the ideal gas model gives accurate predictions for most situations you'll encounter.

### Key Ideas

An **ideal gas** is a theoretical gas that obeys the following assumptions:

1. **Particles have negligible volume.** The actual volume occupied by the gas particles themselves is insignificant compared to the total volume of the container. In other words, gas particles are treated as point masses — they have mass but no size.

2. **No intermolecular forces.** Gas particles do not attract or repel each other, except during collisions. Between collisions, they move in straight lines at constant speed.

3. **Collisions are perfectly elastic.** When gas particles collide with each other or with the walls of the container, no kinetic energy is lost. The total kinetic energy of all particles is conserved.

4. **Particles are in constant, random motion.** The particles move in all directions with a range of speeds. There is no preferred direction of motion.

5. **The number of particles is very large.** Statistical descriptions apply — we describe the gas in terms of averages (average speed, average kinetic energy) rather than tracking individual particles.

6. **Newton's laws apply.** The motion of each particle is governed by classical mechanics. (Quantum effects are negligible at the temperatures and densities of ordinary gases.)

These six assumptions together define the **kinetic model of an ideal gas**. We will explore the consequences of this model in detail in later lessons. For now, the key takeaway is: an ideal gas is the simplest possible model of a gas, and it turns out to be remarkably accurate for real gases under ordinary conditions.

**When does the ideal gas model break down?** At very high pressures (where particles are squeezed so close together that their own volume becomes significant) and at very low temperatures (where intermolecular attractions become important relative to kinetic energy). Near the point of condensation into a liquid, gases deviate significantly from ideal behavior.

### Common Misconceptions

> **⚠️ MISCONCEPTION ALERT:** "Ideal gas particles have no volume, so they must be infinitely small." The phrase "negligible volume" means the volume of the particles is negligible **compared to the volume they move in**. It does not mean the particles literally have zero size. In a typical gas at atmospheric pressure, the particles themselves occupy only about 0.1% of the container volume — the rest is empty space.

> **⚠️ MISCONCEPTION ALERT:** "Ideal gas particles don't interact, so they never touch." They do collide (otherwise they couldn't exert pressure on the container walls), but the collisions are instantaneous and elastic. There are no lingering forces (attractions or repulsions) between particles.

---

## 2. The Mole: Counting Particles

### Why This Matters

A single breath of air contains roughly 10²² molecules. Writing numbers this large in everyday notation is impractical, and doing calculations with them is even worse. Physicists and chemists use a special counting unit called the **mole** (symbol: mol) to handle enormous numbers of particles. The mole is to counting particles what "dozen" is to counting eggs — except instead of 12, a mole contains approximately 6.02 × 10²³ things.

### Key Ideas

A **mole** is defined as the amount of substance that contains exactly 6.02214076 × 10²³ elementary entities (atoms, molecules, ions, electrons, or any other specified particle). For IB Physics, you can use **6.02 × 10²³**.

This number — 6.02 × 10²³ — is called **Avogadro's constant** (or Avogadro's number), symbol N_A (pronounced "N-sub-A"):

**N_A = 6.02 × 10²³ mol⁻¹**

The unit "mol⁻¹" means "per mole." When you multiply a number of moles by N_A, you get the total number of particles:

**N = n × N_A**

where:
- **N** is the total number of particles (no units — it's a count)
- **n** is the number of moles (units: mol)
- **N_A** is Avogadro's constant (6.02 × 10²³ mol⁻¹)

**Where does Avogadro's number come from?** This is not an arbitrary number. It is chosen so that the mass of one mole of a substance (in grams) is numerically equal to its atomic or molecular mass in atomic mass units (u). For example:
- One mole of carbon-12 atoms has a mass of exactly 12 grams (because a carbon-12 atom has a mass of 12 u).
- One mole of oxygen molecules (O₂) has a mass of about 32 grams (because an O₂ molecule has a mass of about 32 u).

**Molar mass** (symbol: M) is the mass of one mole of a substance, expressed in grams per mole (g/mol) or kilograms per mole (kg/mol). The relationship between mass, moles, and molar mass is:

**m = n × M** (when M is in kg/mol) or **m = n × M × 10⁻³** (when M is in g/mol and m is in kg)

For IB Physics:
- The molar mass of helium (He) is 4.00 g/mol = 0.00400 kg/mol
- The molar mass of nitrogen (N₂) is 28.0 g/mol = 0.0280 kg/mol
- The molar mass of oxygen (O₂) is 32.0 g/mol = 0.0320 kg/mol

### Common Misconceptions

> **⚠️ MISCONCEPTION ALERT:** Students often confuse the mass of a single particle (in kg) with the molar mass (in kg/mol). To find the mass of one particle, divide the molar mass by Avogadro's constant: m_particle = M / N_A. For example, the mass of one helium atom is 0.00400 kg/mol ÷ (6.02 × 10²³ mol⁻¹) ≈ 6.64 × 10⁻²⁷ kg.

> **⚠️ MISCONCEPTION ALERT:** "One mole of a gas always occupies 22.4 liters." This is true ONLY at standard temperature and pressure (STP: 0°C and 1 atm). At other conditions, the volume is different. The idea that "1 mol = 22.4 L" without qualification is a common error.

---

## 3. Connecting Microscopic and Macroscopic

### Why This Matters

The whole point of the mole concept is to connect the invisible microscopic world (individual atoms and molecules) with the measurable macroscopic world (pressure, volume, temperature, and mass). Without the mole, we'd have no way to relate the behavior of a gas in a cylinder to the motion of its individual particles.

### Key Ideas

There are two equivalent ways to describe a gas:

**Macroscopic description**: We measure pressure (p), volume (V), and temperature (T). These are the quantities that appear in gas laws.

**Microscopic description**: We talk about the number of particles (N), their masses (m), and their average kinetic energy.

The bridge between these two descriptions involves:
- **n** (number of moles): connects particle count to measurable amounts
- **N_A** (Avogadro's constant): converts between moles and number of particles
- **M** (molar mass): converts between moles and mass in kg
- **k_B** (Boltzmann constant, k_B = 1.38 × 10⁻²³ J/K): relates temperature to average particle kinetic energy

The **Boltzmann constant** (k_B), found in your IB Data Booklet, is essentially the gas constant per particle:

**k_B = R / N_A**

where R = 8.31 J/(mol·K) is the universal gas constant (which we'll meet in Lesson 20).

The Boltzmann constant tells us that the average translational kinetic energy of a particle in an ideal gas is:

**E_k,avg = (3/2) k_B T**

This is a profound result: temperature is directly proportional to the average kinetic energy of particles. If you double the absolute temperature, you double the average kinetic energy of the particles.

---

## Worked Examples

### Example 1: Counting Molecules

A sealed container holds 0.25 mol of helium gas. How many helium atoms are in the container? Use N_A = 6.02 × 10²³ mol⁻¹.

**Approach:** Multiply the number of moles by Avogadro's constant.

**Solution:**
N = n × N_A = 0.25 mol × (6.02 × 10²³ mol⁻¹) = 1.505 × 10²³ atoms

**Why this makes sense:** A quarter of a mole contains a quarter of Avogadro's number — about 1.5 × 10²³ atoms. Even this "small" amount is an unimaginably huge number by everyday standards.

---

### Example 2: Mass of a Single Molecule

Calculate the mass of a single nitrogen molecule (N₂). The molar mass of N₂ is 28.0 g/mol. Use N_A = 6.02 × 10²³ mol⁻¹.

**Approach:** Convert molar mass to kg/mol, then divide by Avogadro's constant.

**Solution:**
M = 28.0 g/mol = 0.0280 kg/mol
m_N₂ = M / N_A = 0.0280 / (6.02 × 10²³) = 4.65 × 10⁻²⁶ kg

**Why this makes sense:** Individual molecules have extremely small masses, on the order of 10⁻²⁶ kg. This is why we need moles — working with individual molecular masses in calculations would be absurdly inconvenient.

---

### Example 3: Moles from Mass

A gas cylinder contains 0.088 kg of carbon dioxide (CO₂). The molar mass of CO₂ is 44.0 g/mol. Calculate the number of moles of CO₂ in the cylinder.

**Approach:** Convert the mass to grams (or the molar mass to kg/mol), then use n = m / M.

**Solution:**
Method 1 (grams): m = 0.088 kg = 88 g, M = 44.0 g/mol
n = 88 g / 44.0 g/mol = 2.0 mol

Method 2 (kg): M = 44.0 g/mol = 0.0440 kg/mol
n = 0.088 kg / 0.0440 kg/mol = 2.0 mol

**Why this makes sense:** 88 g of CO₂ is exactly twice the molar mass, so it contains two moles.

---

### Example 4: Average Kinetic Energy at Room Temperature

Calculate the average translational kinetic energy of a gas particle at room temperature, which is 300 K. Use k_B = 1.38 × 10⁻²³ J/K.

**Approach:** Use E_k,avg = (3/2) k_B T.

**Solution:**
E_k,avg = (3/2) × (1.38 × 10⁻²³) × 300
= 1.5 × 1.38 × 10⁻²³ × 300
= 1.5 × 414 × 10⁻²³
= 621 × 10⁻²³
= 6.21 × 10⁻²¹ J

**Why this makes sense:** This is an extremely small amount of energy per particle. However, when you multiply by the enormous number of particles in even a small sample of gas, the total thermal energy becomes substantial.

---

### Example 5: Mass from Particle Count

A container holds 3.01 × 10²⁴ molecules of oxygen (O₂). Calculate the mass of oxygen in the container. The molar mass of O₂ is 32.0 g/mol and N_A = 6.02 × 10²³ mol⁻¹.

**Approach:** First find the number of moles, then convert to mass.

**Solution:**
n = N / N_A = (3.01 × 10²⁴) / (6.02 × 10²³) = 5.00 mol

m = n × M = 5.00 mol × 32.0 g/mol = 160 g = 0.160 kg

**Why this makes sense:** 3.01 × 10²⁴ is exactly 5 × (6.02 × 10²³), so it's 5 moles. Five moles of O₂ have a mass of 5 × 32 = 160 g.

---

## Practice Problems

### Problem 1
A balloon contains 0.80 mol of helium gas. Calculate the number of helium atoms in the balloon. Then calculate the mass of the helium in the balloon. The molar mass of helium is 4.00 g/mol. Use N_A = 6.02 × 10²³ mol⁻¹.

### Problem 2
A sealed flask contains 1.20 × 10²⁴ molecules of nitrogen gas (N₂). Calculate the number of moles of nitrogen in the flask and the mass of the nitrogen. The molar mass of N₂ is 28.0 g/mol. Use N_A = 6.02 × 10²³ mol⁻¹.

### Problem 3
A student has a sample of an unknown gas with a mass of 0.160 kg. The sample contains 5.00 moles of gas molecules. Calculate the molar mass of the gas in g/mol. Using the fact that common diatomic gases have molar masses of approximately 28 g/mol (N₂), 32 g/mol (O₂), and 2 g/mol (H₂), suggest which gas this might be.

### Problem 4
Calculate the average translational kinetic energy of a gas particle at (a) 100 K, (b) 300 K, and (c) 900 K. Use k_B = 1.38 × 10⁻²³ J/K. Express each answer in joules. What pattern do you notice?

### Problem 5
The mass of a single argon atom is 6.63 × 10⁻²⁶ kg. Calculate the molar mass of argon in g/mol. Use N_A = 6.02 × 10²³ mol⁻¹. Compare your answer to the known value of approximately 40 g/mol.

### Problem 6 (IB Exam-Style)
A gas cylinder contains 0.500 kg of an ideal monatomic gas. The gas is at a temperature of 350 K.

(a) The gas contains 12.5 moles of atoms. Calculate the molar mass of the gas in g/mol. [2 marks]

(b) Calculate the total number of atoms in the cylinder. Use N_A = 6.02 × 10²³ mol⁻¹. [2 marks]

(c) Calculate the average translational kinetic energy of one atom of this gas at 350 K. Use k_B = 1.38 × 10⁻²³ J/K. [2 marks]

(d) Calculate the total translational kinetic energy of all the atoms in the cylinder. [2 marks]

(e) The temperature of the gas is increased to 700 K. Calculate the new average translational kinetic energy per atom, and state the factor by which it has increased. [2 marks]

---

## Answers

### Answer 1
N = n × N_A = 0.80 × (6.02 × 10²³) = 4.816 × 10²³ atoms
Mass: m = n × M = 0.80 mol × 4.00 g/mol = 3.20 g = 0.00320 kg

A party balloon contains nearly half a septillion atoms!

---

### Answer 2
n = N / N_A = (1.20 × 10²⁴) / (6.02 × 10²³) = 1.99 mol (approximately 2.00 mol)
m = n × M = 2.00 mol × 28.0 g/mol = 56.0 g

---

### Answer 3
M = m / n = 0.160 kg / 5.00 mol = 0.0320 kg/mol = 32.0 g/mol

This molar mass corresponds to oxygen (O₂). The unknown gas is oxygen.

---

### Answer 4
(a) E_k = (3/2)k_B T = 1.5 × (1.38 × 10⁻²³) × 100 = 2.07 × 10⁻²¹ J
(b) E_k = 1.5 × (1.38 × 10⁻²³) × 300 = 6.21 × 10⁻²¹ J
(c) E_k = 1.5 × (1.38 × 10⁻²³) × 900 = 1.86 × 10⁻²⁰ J

The average kinetic energy is directly proportional to the absolute temperature. Tripling the temperature from 300 K to 900 K triples the average kinetic energy (6.21 × 10⁻²¹ × 3 = 1.86 × 10⁻²⁰).

---

### Answer 5
M = m_atom × N_A = (6.63 × 10⁻²⁶ kg) × (6.02 × 10²³ mol⁻¹)
= 6.63 × 6.02 × 10⁻³ = 39.9 × 10⁻³ kg/mol = 39.9 g/mol

This is very close to the known value of 39.95 g/mol for argon — the small difference is from rounding.

---

### Answer 6

**(a)** M = m / n = 0.500 kg / 12.5 mol = 0.0400 kg/mol = 40.0 g/mol [2 marks]

**(b)** N = n × N_A = 12.5 × (6.02 × 10²³) = 7.525 × 10²⁴ atoms [2 marks]

**(c)** E_k,avg = (3/2)k_B T = 1.5 × (1.38 × 10⁻²³) × 350 = 7.245 × 10⁻²¹ J [2 marks]

**(d)** Total E_k = N × E_k,avg = (7.525 × 10²⁴) × (7.245 × 10⁻²¹) = 5.45 × 10⁴ J [2 marks]

**(e)** At 700 K: E_k,avg = (3/2)k_B × 700 = 1.5 × 1.38 × 10⁻²³ × 700 = 1.449 × 10⁻²⁰ J
Factor: 700/350 = 2. The average kinetic energy doubles when the absolute temperature doubles. [2 marks]

---

## Key Takeaways

1. An **ideal gas** is a simplified model where particles have negligible volume, no intermolecular forces (except during elastic collisions), and are in constant random motion.

2. The **mole** is the unit for "amount of substance." One mole contains N_A = 6.02 × 10²³ elementary entities.

3. **Avogadro's constant** (N_A) converts between number of particles (N) and number of moles (n): N = n × N_A.

4. **Molar mass** (M) converts between mass and number of moles: m = n × M.

5. The mass of a single particle is related to the molar mass by: m_particle = M / N_A.

6. The **Boltzmann constant** (k_B = 1.38 × 10⁻²³ J/K) relates temperature to average kinetic energy: E_k,avg = (3/2) k_B T.

7. k_B and the universal gas constant R are related: k_B = R / N_A, where R = 8.31 J/(mol·K).

8. These concepts build the bridge between the microscopic world of atoms and the macroscopic world of measurable gas properties (pressure, volume, temperature).
