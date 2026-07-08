# Lesson 15: Thermal Physics 2 — Specific Heat Capacity and Latent Heat

## What You'll Learn

When you heat a pot of water on a stove, something interesting happens: the temperature rises steadily, but when the water starts boiling, the temperature stops rising even though you're still adding heat. Where does that energy go? In this lesson, you will learn about two fundamental concepts that explain this behavior: **specific heat capacity**, which tells you how much energy is needed to raise the temperature of a substance, and **latent heat**, which tells you how much energy is needed to change a substance's state without changing its temperature. These concepts are essential for understanding everything from cooking to climate science to the design of thermal systems in engineering.

---

## 1. Specific Heat Capacity

### Why This Matters

Different materials require different amounts of energy to heat up. A metal spoon left in a hot cup of tea becomes painful to touch within seconds, but the ceramic cup itself stays comfortable to hold for much longer. This is not just because of different starting temperatures — it reflects a fundamental property of each material called **specific heat capacity**. Understanding this property allows engineers to choose materials for heat sinks, insulation, and thermal storage. It also explains why coastal cities have milder climates than inland cities at the same latitude: water has an unusually high specific heat capacity.

### Key Ideas

**Specific heat capacity** (symbol: c) is defined as the amount of energy required to raise the temperature of 1 kilogram of a substance by 1 kelvin (or 1°C, since a change of 1 K equals a change of 1°C). Its SI unit is joules per kilogram per kelvin, written as J/(kg·K) or equivalently J/(kg·°C).

The mathematical relationship is:

**Q = m c ΔT**

where:
- **Q** is the thermal energy transferred (in joules, J). Some textbooks call this "heat," but in physics we prefer "thermal energy transfer."
- **m** is the mass of the substance (in kilograms, kg)
- **c** is the specific heat capacity (in J/(kg·K))
- **ΔT** is the change in temperature (in kelvin or °C)

The symbol Δ (Greek letter "delta") means "change in." So ΔT means "final temperature minus initial temperature."

When a substance gains thermal energy, Q is positive and ΔT is positive (temperature rises). When a substance loses thermal energy, Q is negative and ΔT is negative (temperature falls). The same formula works for both heating and cooling.

**Why does specific heat capacity vary between substances?** At the microscopic level, when you add energy to a material, that energy goes into increasing the kinetic energy of its particles (atoms or molecules). Different materials have different atomic masses, different bonding structures, and different numbers of ways to store energy (called "degrees of freedom"). A monatomic gas like helium has only translational motion (3 degrees of freedom). A diatomic gas like oxygen has both translational and rotational motion (5 degrees of freedom). A solid has vibrational modes as well. The more ways a substance can store energy internally, the more energy it takes to raise its temperature by a given amount — so its specific heat capacity is higher.

The specific heat capacity of water is approximately **4200 J/(kg·K)**. This is one of the highest values for any common substance, which has profound consequences for life on Earth and for climate.

### Common Misconceptions

> **⚠️ MISCONCEPTION ALERT:** Many students think that a substance with a high specific heat capacity "heats up faster." The opposite is true. A high specific heat capacity means the substance *resists* temperature change — it takes more energy to raise its temperature by 1 K. Think of specific heat capacity as "thermal inertia": a high value means the substance is sluggish to change temperature.

> **⚠️ MISCONCEPTION ALERT:** Some students confuse temperature (measured in K or °C) with thermal energy (measured in J). A large lake at 15°C contains vastly more thermal energy than a cup of tea at 80°C, because thermal energy depends on both temperature and mass. Temperature measures the average kinetic energy per particle, not the total energy of the system.

> **⚠️ MISCONCEPTION ALERT:** The specific heat capacity is not a constant for all temperatures. It varies slightly with temperature and pressure. However, for IB Physics, you should treat it as a constant for a given substance unless told otherwise.

---

## 2. Latent Heat

### Why This Matters

When ice melts into water at 0°C, or when water boils into steam at 100°C, the temperature does not change during the phase transition even though energy is being added continuously. This energy is not "lost" — it is used to break the bonds between particles rather than to increase their kinetic energy. This "hidden" energy is called **latent heat** (from the Latin word *latens*, meaning "hidden").

Understanding latent heat explains why steam burns are so much more severe than boiling water burns: steam at 100°C contains the latent heat of vaporization, which is released onto your skin when the steam condenses back into water. It also explains why sweating cools you down: the evaporation of sweat absorbs latent heat from your skin.

### Key Ideas

**Latent heat** (symbol: L, not to be confused with length) is the thermal energy absorbed or released during a change of state at constant temperature. There are two types:

1. **Latent heat of fusion** (L_f): The energy required to change 1 kg of a substance from solid to liquid (melting) or released when changing from liquid to solid (freezing). Both processes occur at the same temperature (the melting point).

2. **Latent heat of vaporization** (L_v): The energy required to change 1 kg of a substance from liquid to gas (boiling/evaporating) or released when changing from gas to liquid (condensing). Both processes occur at the same temperature (the boiling point at a given pressure).

The mathematical relationship is:

**Q = m L**

where:
- **Q** is the thermal energy transferred (in J)
- **m** is the mass of the substance changing state (in kg)
- **L** is the specific latent heat (in J/kg)

The same formula works for both fusion and vaporization. For melting, use L_f; for boiling, use L_v.

For water:
- Specific latent heat of fusion: approximately **3.34 × 10⁵ J/kg** (or 334,000 J/kg)
- Specific latent heat of vaporization: approximately **2.26 × 10⁶ J/kg** (or 2,260,000 J/kg)

Notice that the latent heat of vaporization is roughly seven times larger than the latent heat of fusion. This makes sense microscopically: melting only requires particles to break free from fixed positions in the solid lattice while remaining close together. Vaporization requires particles to completely escape from the liquid and move far apart, overcoming all intermolecular attractions.

### The Heating Curve

A **heating curve** is a graph of temperature versus energy added. When you heat a solid:
1. The temperature rises (solid phase) — Q = m c_solid ΔT
2. The temperature plateaus at the melting point while the solid melts — Q = m L_f
3. The temperature rises again (liquid phase) — Q = m c_liquid ΔT
4. The temperature plateaus at the boiling point while the liquid boils — Q = m L_v
5. The temperature rises again (gas phase) — Q = m c_gas ΔT

The flat sections of the curve (where temperature stays constant) correspond to latent heat. The sloping sections correspond to specific heat capacity.

### Common Misconceptions

> **⚠️ MISCONCEPTION ALERT:** Many students ask, "If the temperature isn't changing, where is the energy going?" The energy goes into increasing the **potential energy** of the particles, not their **kinetic energy**. Temperature measures average kinetic energy. During a phase change, the added energy breaks intermolecular bonds (increasing potential energy), so the kinetic energy — and therefore the temperature — stays constant.

> **⚠️ MISCONCEPTION ALERT:** Students often think that boiling water is hotter than water that is "just about to boil." Both are at exactly 100°C (at standard atmospheric pressure). The difference is that the boiling water contains more energy because of the latent heat already absorbed.

> **⚠️ MISCONCEPTION ALERT:** Evaporation and boiling are not the same thing. Boiling occurs at a specific temperature (the boiling point) and happens throughout the liquid. Evaporation can occur at any temperature and only happens at the surface of the liquid. Both involve the same latent heat of vaporization.

---

## 3. Using Specific Heat Capacity and Latent Heat Together

### Why This Matters

Real-world problems often involve both temperature changes and phase changes. For example, to find the total energy needed to turn ice at −10°C into steam at 120°C, you must calculate:
1. Energy to warm the ice from −10°C to 0°C (specific heat of ice)
2. Energy to melt the ice at 0°C (latent heat of fusion)
3. Energy to warm the water from 0°C to 100°C (specific heat of water)
4. Energy to boil the water at 100°C (latent heat of vaporization)
5. Energy to warm the steam from 100°C to 120°C (specific heat of steam)

Each step uses a different value of c or L. The total energy is the sum of all five contributions.

### Conservation of Energy in Thermal Interactions

When two substances at different temperatures are brought into thermal contact (with no phase changes), the hotter substance loses thermal energy and the colder substance gains thermal energy until they reach the same temperature. Assuming no energy is lost to the surroundings:

**Energy lost by hot substance = Energy gained by cold substance**

m_hot × c_hot × (T_hot,initial − T_final) = m_cold × c_cold × (T_final − T_cold,initial)

This is the fundamental principle of **calorimetry**, the measurement of heat transfer. (Note: the proper term in physics is "thermal energy transfer," but "calorimetry" is the traditional name of the technique.)

---

## Worked Examples

### Example 1: Heating a Metal Block

A 2.0 kg block of aluminum is heated from 20°C to 80°C. The specific heat capacity of aluminum is 900 J/(kg·K). Calculate the thermal energy absorbed by the block.

**Approach:** This is a straightforward temperature change with no phase change. Use Q = m c ΔT, identifying each quantity carefully.

**Solution:**
- m = 2.0 kg
- c = 900 J/(kg·K)
- ΔT = 80°C − 20°C = 60°C (which equals 60 K)

Q = m c ΔT
Q = (2.0 kg) × (900 J/(kg·K)) × (60 K)
Q = 2.0 × 900 × 60 = 108,000 J = 1.08 × 10⁵ J

**Why this makes sense:** Aluminum has a moderately low specific heat capacity. 1.08 × 10⁵ J is roughly the energy a 100 W light bulb uses in about 18 minutes, which is reasonable for heating a 2 kg block through 60°C.

---

### Example 2: Melting Ice

How much energy is required to melt 0.50 kg of ice at 0°C? The specific latent heat of fusion of water is 3.34 × 10⁵ J/kg.

**Approach:** This is a pure phase change at constant temperature. Use Q = m L_f.

**Solution:**
- m = 0.50 kg
- L_f = 3.34 × 10⁵ J/kg

Q = m L_f
Q = (0.50 kg) × (3.34 × 10⁵ J/kg)
Q = 1.67 × 10⁵ J

**Why this makes sense:** This is about 167 kJ. For comparison, the same energy could raise 0.50 kg of liquid water from 0°C to about 80°C. The energy required just to break the crystal structure (without any temperature change) is substantial.

---

### Example 3: Ice to Warm Water

A student places 0.20 kg of ice at 0°C into an insulated cup. How much energy is needed to turn all of this into water at 25°C? Use L_f = 3.34 × 10⁵ J/kg and c_water = 4200 J/(kg·K).

**Approach:** This problem has two stages: first melt the ice (latent heat), then warm the resulting water (specific heat capacity). Calculate each contribution separately and add them.

**Solution:**

**Step 1: Melting the ice at 0°C**
Q₁ = m L_f = (0.20 kg) × (3.34 × 10⁵ J/kg) = 6.68 × 10⁴ J

**Step 2: Warming the water from 0°C to 25°C**
ΔT = 25°C − 0°C = 25 K
Q₂ = m c ΔT = (0.20 kg) × (4200 J/(kg·K)) × (25 K)
Q₂ = 0.20 × 4200 × 25 = 21,000 J = 2.10 × 10⁴ J

**Total energy:**
Q_total = Q₁ + Q₂ = 6.68 × 10⁴ J + 2.10 × 10⁴ J = 8.78 × 10⁴ J

**Why this makes sense:** The melting step requires more than three times as much energy as the warming step. This illustrates how much energy is "hidden" in phase changes.

---

### Example 4: Cooling Water with Ice

A drink contains 0.30 kg of water at 25°C. A student adds 0.050 kg of ice at 0°C to cool it down. Assuming no energy is exchanged with the surroundings, what is the final temperature of the drink after all the ice has melted? Use L_f = 3.34 × 10⁵ J/kg and c_water = 4200 J/(kg·K).

**Approach:** This is a conservation of energy problem. The ice will absorb energy to melt and then absorb more energy as the resulting water warms up. The original water will lose energy as it cools. Set energy lost by warm water equal to energy gained by ice (melting + warming).

**Solution:**
Let T be the final temperature of everything (in °C).

**Energy lost by warm water:**
Q_lost = m_warm × c × (25 − T) = (0.30 kg) × (4200 J/(kg·K)) × (25 − T)

**Energy gained by ice (melting):**
Q_melt = m_ice × L_f = (0.050 kg) × (3.34 × 10⁵ J/kg) = 16,700 J

**Energy gained by melted ice warming from 0°C to T:**
Q_warm_ice = m_ice × c × (T − 0) = (0.050 kg) × (4200 J/(kg·K)) × T

**Conservation of energy:**
Q_lost = Q_melt + Q_warm_ice

(0.30)(4200)(25 − T) = 16,700 + (0.050)(4200)T

1260 × (25 − T) = 16,700 + 210T
31,500 − 1260T = 16,700 + 210T
31,500 − 16,700 = 1260T + 210T
14,800 = 1470T
T = 14,800 / 1470 ≈ 10.1°C

**Why this makes sense:** The temperature drops from 25°C to about 10°C — a significant cooling effect from just 50 g of ice. This is why ice is so effective at cooling drinks: the latent heat of fusion absorbs enormous energy.

---

### Example 5: Steam Burn vs. Boiling Water Burn

A person spills 0.010 kg of boiling water at 100°C onto their hand. Another person's hand is exposed to 0.010 kg of steam at 100°C that condenses onto their skin and cools to 50°C. Compare the energy released in each case. Use L_v = 2.26 × 10⁶ J/kg and c_water = 4200 J/(kg·K).

**Approach:** For boiling water, only specific heat capacity cooling from 100°C to 50°C. For steam, first the latent heat of condensation is released at 100°C, then the resulting water cools from 100°C to 50°C.

**Solution:**

**Boiling water (100°C → 50°C):**
ΔT = 50 K
Q_water = m c ΔT = (0.010 kg) × (4200 J/(kg·K)) × (50 K) = 2100 J

**Steam (condenses at 100°C, then cools to 50°C):**
Q_steam = m L_v + m c ΔT
Q_steam = (0.010 kg) × (2.26 × 10⁶ J/kg) + (0.010 kg) × (4200 J/(kg·K)) × (50 K)
Q_steam = 22,600 J + 2100 J = 24,700 J

**Comparison:**
Q_steam / Q_water = 24,700 / 2100 ≈ 11.8

**Why this makes sense:** Steam releases nearly 12 times more energy than boiling water at the same initial temperature. The latent heat of vaporization dominates. This explains why steam burns are far more dangerous than boiling water burns.

---

## Practice Problems

### Problem 1
A 1.5 kg iron skillet is heated on a stove from 25°C to 175°C. The specific heat capacity of iron is 450 J/(kg·K). Calculate the thermal energy absorbed by the skillet. If the stove supplies energy at a rate of 1500 W (joules per second), how long does the heating take, assuming no energy is lost to the surroundings?

### Problem 2
A 3.0 kg aluminum pot contains 2.0 kg of water, both initially at 20°C. A heater supplies 5.0 × 10⁵ J of energy to the pot-water system. Assuming no energy is lost to the surroundings, calculate the final temperature of the water and pot. The specific heat capacity of aluminum is 900 J/(kg·K) and of water is 4200 J/(kg·K). Hint: both the pot and the water end up at the same final temperature.

### Problem 3
An ice cube of mass 0.025 kg is taken from a freezer at −18°C and dropped into a glass containing 0.22 kg of water at 22°C. Calculate the final temperature of the water after the ice has completely melted, assuming no energy exchange with the surroundings. The specific heat capacity of ice is 2100 J/(kg·K), the specific latent heat of fusion of water is 3.34 × 10⁵ J/kg, and the specific heat capacity of water is 4200 J/(kg·K).

### Problem 4
A student wants to cool 0.40 kg of water from 30°C to 10°C by adding ice at 0°C. Calculate the minimum mass of ice required. Use L_f = 3.34 × 10⁵ J/kg and c_water = 4200 J/(kg·K).

### Problem 5
A 0.500 kg block of a mystery metal at 100°C is placed into 0.400 kg of water at 15°C in an insulated container. The final equilibrium temperature is 23°C. Calculate the specific heat capacity of the mystery metal. The specific heat capacity of water is 4200 J/(kg·K). Suggest what metal this might be.

### Problem 6 (IB Exam-Style)
A student investigates the specific latent heat of fusion of ice using the method of mixtures. The student places 0.120 kg of warm water at 40.0°C into a calorimeter (an insulated container used for thermal measurements). Ice cubes at 0°C are dried with a paper towel and added one at a time until the temperature reaches 10.0°C. The total mass of ice added is 0.042 kg. The specific heat capacity of water is 4200 J/(kg·K).

(a) Explain why the ice cubes are dried before adding them to the warm water. [2 marks]

(b) Explain why the water is stirred during the experiment. [1 mark]

(c) Calculate the experimental value for the specific latent heat of fusion of ice. [4 marks]

(d) The accepted value for the specific latent heat of fusion of ice is 3.34 × 10⁵ J/kg. Calculate the percentage difference between the experimental and accepted values. [1 mark]

(e) Suggest one reason why the experimental value might differ from the accepted value, and state whether this would make the experimental value too high or too low. [2 marks]

---

## Answers

### Answer 1

**Calculation:**
ΔT = 175°C − 25°C = 150 K
Q = m c ΔT = (1.5 kg) × (450 J/(kg·K)) × (150 K) = 101,250 J ≈ 1.01 × 10⁵ J

**Time calculation:**
Power P = 1500 W = 1500 J/s
Time t = Q / P = 101,250 J / 1500 J/s = 67.5 s

The heating takes approximately 68 seconds, or just over one minute.

**Common pitfall:** Students sometimes forget to convert °C to change in temperature as K. In this case, ΔT in °C equals ΔT in K, so no issue, but always check.

---

### Answer 2

Both the aluminum pot and the water start at 20°C and end at temperature T. Energy goes into both:

Energy into aluminum: Q_Al = m_Al × c_Al × (T − 20) = (3.0)(900)(T − 20)
Energy into water: Q_water = m_water × c_water × (T − 20) = (2.0)(4200)(T − 20)

Total energy: Q_total = Q_Al + Q_water = 5.0 × 10⁵ J

(3.0)(900)(T − 20) + (2.0)(4200)(T − 20) = 5.0 × 10⁵
2700(T − 20) + 8400(T − 20) = 5.0 × 10⁵
(2700 + 8400)(T − 20) = 5.0 × 10⁵
11,100(T − 20) = 5.0 × 10⁵
T − 20 = 500,000 / 11,100 ≈ 45.0
T ≈ 65.0°C

The final temperature is approximately 65°C.

**Common pitfall:** Forgetting that the pot also absorbs energy. The pot's contribution is significant because it has both substantial mass and is in direct contact with the heat source.

---

### Answer 3

The ice goes through three stages:
1. Warm from −18°C to 0°C (ice): Q₁ = (0.025)(2100)(18) = 945 J
2. Melt at 0°C: Q₂ = (0.025)(3.34 × 10⁵) = 8350 J
3. Warm from 0°C to final T (water): Q₃ = (0.025)(4200)(T)

The warm water cools from 22°C to T: Q₄ = (0.22)(4200)(22 − T) = 924(22 − T)

Conservation of energy: energy gained by ice = energy lost by water
Q₁ + Q₂ + Q₃ = Q₄
945 + 8350 + (0.025)(4200)(T) = (0.22)(4200)(22 − T)
9295 + 105T = 924(22 − T)
9295 + 105T = 20,328 − 924T
105T + 924T = 20,328 − 9295
1029T = 11,033
T ≈ 10.7°C

The final temperature is approximately 10.7°C.

---

### Answer 4

The energy that needs to be removed from the water:
Q_remove = m_water × c × (30 − 10) = (0.40)(4200)(20) = 33,600 J

Let m be the mass of ice. The ice absorbs energy by melting (at 0°C) and then the resulting water warms from 0°C to 10°C:
Q_absorb = m × L_f + m × c × (10 − 0) = m × 3.34 × 10⁵ + m × 4200 × 10
Q_absorb = m × 334,000 + m × 42,000 = m × 376,000

Set equal:
m × 376,000 = 33,600
m = 33,600 / 376,000 = 0.0894 kg ≈ 0.089 kg

About 89 g of ice is needed. This is over 20% of the water's mass — ice is effective but you need a fair amount.

---

### Answer 5

Energy gained by water:
Q_water = (0.400)(4200)(23 − 15) = (0.400)(4200)(8) = 13,440 J

Energy lost by metal:
Q_metal = (0.500)(c_metal)(100 − 23) = (0.500)(c_metal)(77) = 38.5 × c_metal

Conservation of energy:
38.5 × c_metal = 13,440
c_metal = 13,440 / 38.5 ≈ 349 J/(kg·K)

The specific heat capacity is approximately 350 J/(kg·K). This is close to brass (about 380 J/(kg·K)) or zinc (about 390 J/(kg·K)).

---

### Answer 6

**(a)** The ice cubes are dried to remove any liquid water clinging to their surface. If undried ice is added, the mass of water on the surface would contribute to the final mass without having absorbed latent heat to melt, since it's already liquid. This would make the measured mass of ice larger than the actual mass that underwent melting, causing the calculated latent heat to be too low. [2 marks]

**(b)** Stirring ensures that thermal energy is distributed evenly throughout the water, so the temperature reading represents the true temperature of all the water, not just the liquid near the thermometer. [1 mark]

**(c)** Energy lost by warm water:
Q_lost = m_warm × c × (T_initial − T_final)
Q_lost = (0.120 kg) × (4200 J/(kg·K)) × (40.0 − 10.0) K
Q_lost = 0.120 × 4200 × 30.0 = 15,120 J

Energy gained by ice:
Melting: Q_melt = 0.042 × L_f
Warming from 0°C to 10°C: Q_warm = 0.042 × 4200 × 10.0 = 1764 J

Energy conservation:
0.042 × L_f + 1764 = 15,120
0.042 × L_f = 15,120 − 1764 = 13,356
L_f = 13,356 / 0.042 = 318,000 J/kg = 3.18 × 10⁵ J/kg [4 marks]

**(d)** Percentage difference:
|3.18 × 10⁵ − 3.34 × 10⁵| / 3.34 × 10⁵ × 100% = (0.16 / 3.34) × 100% ≈ 4.8% [1 mark]

**(e)** One possible reason: the calorimeter itself absorbs some thermal energy from the warm water, meaning not all the energy lost by the water goes into melting the ice. This would cause the calculated L_f to be too low, because the calculation assumes all energy lost by the water went to the ice. Other acceptable answers: heat gain from surroundings (makes L_f too high if ice melts from room temperature air), or incomplete drying of ice cubes (makes L_f too low because extra water mass inflates the "ice" mass). [2 marks]

---

## Key Takeaways

1. **Specific heat capacity** (c) measures how much energy is needed to raise the temperature of 1 kg of a substance by 1 K. The formula is Q = m c ΔT.

2. Water has an exceptionally high specific heat capacity (4200 J/(kg·K)), which moderates Earth's climate and makes water an excellent coolant.

3. **Latent heat** (L) is the energy absorbed or released during a phase change at constant temperature. The formula is Q = m L.

4. During a phase change, temperature stays constant because energy goes into changing potential energy (breaking bonds), not kinetic energy.

5. The **latent heat of vaporization** is much larger than the **latent heat of fusion** because vaporization requires particles to escape completely from the liquid.

6. In **calorimetry problems**, apply conservation of energy: the total energy lost by hot substances equals the total energy gained by cold substances (including any latent heat contributions).

7. When a problem involves both temperature changes and phase changes, break it into stages, calculate each stage separately, and sum the results.

8. The IB Data Booklet provides values for specific heat capacities and latent heats. Always check which values are provided.
