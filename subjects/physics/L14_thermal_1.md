# Lesson 14: Thermal Energy Transfers I — Heat & Temperature

## What You'll Learn
- Temperature scales: Celsius, Kelvin, and absolute zero
- Thermal equilibrium and the zeroth law of thermodynamics
- Specific heat capacity: $Q = mc\Delta\theta$
- Specific latent heat: $Q = mL$
- Heating curves and phase changes
- Internal energy: kinetic and potential molecular contributions

---

## 1. Temperature and Temperature Scales

**Temperature** is a measure of the average random kinetic energy of particles in a substance. It determines the direction of spontaneous thermal energy transfer — energy flows from higher to lower temperature.

### Temperature Scales

| Scale | Freezing point of water | Boiling point of water | Absolute zero |
|-------|------------------------|------------------------|---------------|
| Celsius (°C) | 0°C | 100°C | −273.15°C |
| Kelvin (K) | 273.15 K | 373.15 K | 0 K |

**Conversion:** $T(\text{K}) = T(\text{°C}) + 273.15 \approx T(\text{°C}) + 273$

The Kelvin scale is the SI base unit. **Absolute zero** (0 K) is the theoretical lowest temperature, where particles have minimum kinetic energy. It cannot be reached, but experiments have achieved nanokelvin temperatures.

**Temperature difference:** $\Delta T$ in K = $\Delta T$ in °C (since the scales differ only by a constant offset).

---

## 2. Thermal Equilibrium (Zeroth Law)

**The zeroth law of thermodynamics:** If two systems are each in thermal equilibrium with a third system, they are in thermal equilibrium with each other.

This allows us to use thermometers: when the thermometer reaches the same temperature as the object being measured, they are in thermal equilibrium.

---

## 3. Internal Energy

The **internal energy** $U$ of a substance is the sum of:
1. **Kinetic energy** of all particles (random translational, rotational, vibrational motion) — directly related to temperature.
2. **Potential energy** of all particles (due to intermolecular forces) — changes during phase transitions.

**Key distinction:** During a phase change, temperature stays constant but internal energy changes — the potential energy changes while kinetic energy stays the same.

For an ideal gas, internal energy depends only on temperature: $U = \frac{3}{2}nRT$ (monatomic) or $U = \frac{5}{2}nRT$ (diatomic).

---

## 4. Specific Heat Capacity

The thermal energy $Q$ required to change the temperature of mass $m$ of a substance by $\Delta\theta$ is:

$$Q = mc\Delta\theta$$

where $c$ is the **specific heat capacity** (J·kg⁻¹·K⁻¹).

| Substance | $c$ (J·kg⁻¹·K⁻¹) |
|-----------|-------------------|
| Water | 4186 |
| Ice | 2100 |
| Steam | 2010 |
| Aluminum | 900 |
| Copper | 385 |
| Iron | 450 |

Water has an unusually high specific heat capacity, which moderates Earth's climate.

---

### Worked Example 14.1 — Heating Water

**Problem:** How much energy is required to heat 2.50 kg of water from 20.0°C to 85.0°C?

**Solution:**

$m = 2.50 \text{ kg}$, $c = 4186 \text{ J·kg}^{-1}\text{·K}^{-1}$, $\Delta\theta = 85.0 - 20.0 = 65.0 \text{ K}$

$Q = mc\Delta\theta = 2.50 \times 4186 \times 65.0$
$= 2.50 \times 4186 \times 65.0 = 680,225 \text{ J}$

$$\boxed{Q \approx 6.80 \times 10^5 \text{ J} = 680 \text{ kJ}}$$

---

## 5. Specific Latent Heat

During a phase change, temperature remains constant while energy is absorbed or released. The energy per unit mass is the **specific latent heat** $L$:

$$Q = mL$$

- **Latent heat of fusion** $L_f$: solid ↔ liquid
- **Latent heat of vaporization** $L_v$: liquid ↔ gas

| Substance | $L_f$ (kJ/kg) | $L_v$ (kJ/kg) |
|-----------|---------------|----------------|
| Water | 334 | 2257 |
| Ethanol | 108 | 855 |
| Lead | 25 | 870 |

---

### Worked Example 14.2 — Melting Ice

**Problem:** How much energy is required to completely melt 0.500 kg of ice at 0°C?

**Solution:**

$Q = mL_f = 0.500 \times (3.34 \times 10^5) = 1.67 \times 10^5 \text{ J}$

$$\boxed{Q = 167 \text{ kJ}}$$

Note: This is the same energy needed to heat the resulting water by about $Q/(mc) = 1.67 \times 10^5/(0.500 \times 4186) \approx 79.8 \text{ K}$, i.e., from 0°C to nearly 80°C. The energy to break intermolecular bonds is substantial!

---

## 6. Heating Curves

A **heating curve** plots temperature vs. energy added. Flat regions represent phase changes.

```
T (°C)
120 |                    _______
    |                   /
100 |    ______________/  ← boiling (L_v)
    |   /
  0 |__/  ← melting (L_f)
    |/
-20 |_______
    +------------------------> Q
```

**Interpreting the curve:**
- Sloping sections: $Q = mc\Delta\theta$, temperature rises
- Flat sections: $Q = mL$, phase change at constant temperature

---

### Worked Example 14.3 — Heating Ice to Steam

**Problem:** Calculate the total energy needed to convert 0.200 kg of ice at −10.0°C to steam at 100.0°C. Given: $c_{\text{ice}} = 2100 \text{ J·kg}^{-1}\text{·K}^{-1}$, $c_{\text{water}} = 4186 \text{ J·kg}^{-1}\text{·K}^{-1}$, $L_f = 3.34 \times 10^5 \text{ J/kg}$, $L_v = 2.26 \times 10^6 \text{ J/kg}$.

**Solution:**

Break into stages:

**Stage 1:** Heat ice from −10.0°C to 0°C
$Q_1 = mc_{\text{ice}}\Delta\theta = 0.200 \times 2100 \times 10.0 = 4,200 \text{ J}$

**Stage 2:** Melt ice at 0°C
$Q_2 = mL_f = 0.200 \times 3.34 \times 10^5 = 66,800 \text{ J}$

**Stage 3:** Heat water from 0°C to 100°C
$Q_3 = mc_{\text{water}}\Delta\theta = 0.200 \times 4186 \times 100 = 83,720 \text{ J}$

**Stage 4:** Vaporize water at 100°C
$Q_4 = mL_v = 0.200 \times 2.26 \times 10^6 = 452,000 \text{ J}$

**Total:** $Q = 4,200 + 66,800 + 83,720 + 452,000 = 606,720 \text{ J}$

$$\boxed{Q \approx 607 \text{ kJ}}$$

The vaporization step dominates (≈74% of total energy).

---

### Worked Example 14.4 — Mixing Hot and Cold Water

**Problem:** 0.300 kg of water at 80.0°C is mixed with 0.200 kg of water at 15.0°C in an insulated container. Find the final equilibrium temperature.

**Solution:**

Energy lost by hot water = energy gained by cold water (no heat loss to surroundings).

$$m_h c (T_h - T_f) = m_c c (T_f - T_c)$$

Cancel $c$ (same substance):
$$0.300(80.0 - T_f) = 0.200(T_f - 15.0)$$

$$24.0 - 0.300T_f = 0.200T_f - 3.00$$

$$24.0 + 3.00 = 0.200T_f + 0.300T_f$$

$$27.0 = 0.500T_f$$

$$T_f = \boxed{54.0\text{°C}}$$

---

### Worked Example 14.5 — Finding Specific Heat Capacity

**Problem:** A 0.150 kg aluminum block at 100°C is placed in 0.250 kg of water at 20.0°C in an insulated calorimeter. The final temperature is 28.5°C. Determine the specific heat capacity of aluminum. ($c_{\text{water}} = 4186 \text{ J·kg}^{-1}\text{·K}^{-1}$)

**Solution:**

Energy lost by Al = energy gained by water:
$$m_{\text{Al}} c_{\text{Al}} (100 - 28.5) = m_w c_w (28.5 - 20.0)$$

$$0.150 \times c_{\text{Al}} \times 71.5 = 0.250 \times 4186 \times 8.5$$

$$10.725 \, c_{\text{Al}} = 0.250 \times 4186 \times 8.5 = 8895.25$$

$$c_{\text{Al}} = \frac{8895.25}{10.725} = 829 \text{ J·kg}^{-1}\text{·K}^{-1}$$

$$\boxed{c_{\text{Al}} \approx 8.3 \times 10^2 \text{ J·kg}^{-1}\text{·K}^{-1}}$$

This is close to the accepted value of 900 J·kg⁻¹·K⁻¹; the ≈8% discrepancy could be due to heat loss, thermometer errors, or the calorimeter absorbing some heat.

---

## Practice Problems

### Problem 1 — Simple Heating
How much energy is needed to raise the temperature of 5.00 kg of copper ($c = 385 \text{ J·kg}^{-1}\text{·K}^{-1}$) from 25.0°C to 85.0°C?

### Problem 2 — Phase Change
A 0.500 kg block of ice at 0°C is placed in 2.00 kg of water at 30.0°C in an insulated container. (a) How much energy is needed to melt all the ice? (b) Does all the ice melt? (c) What is the final temperature after equilibrium is reached?

### Problem 3 — Internal Energy
Explain why the temperature of a boiling liquid remains constant even though energy is continuously being supplied. Discuss what happens to the internal energy of the system.

### Problem 4 — IB-Style: Multi-Stage Heating
A student heats 0.100 kg of a solid substance at −20.0°C. The substance melts at 50.0°C and vaporizes at 150.0°C. Given: $c_{\text{solid}} = 1500 \text{ J·kg}^{-1}\text{·K}^{-1}$, $c_{\text{liquid}} = 2500 \text{ J·kg}^{-1}\text{·K}^{-1}$, $L_f = 4.00 \times 10^4 \text{ J/kg}$, $L_v = 8.50 \times 10^5 \text{ J/kg}$. Calculate the total energy to convert it to gas at 150.0°C.

### Problem 5 — IB-Style: Calorimetry with Phase Change
A 0.0500 kg piece of ice at −5.0°C is added to 0.300 kg of water at 40.0°C in a perfectly insulated calorimeter of negligible heat capacity. Determine the final temperature. ($c_{\text{ice}} = 2100 \text{ J·kg}^{-1}\text{·K}^{-1}$, $c_{\text{water}} = 4186 \text{ J·kg}^{-1}\text{·K}^{-1}$, $L_f = 3.34 \times 10^5 \text{ J/kg}$)

---

## Answers

### Answer 1
$Q = mc\Delta\theta = 5.00 \times 385 \times (85.0 - 25.0)$
$= 5.00 \times 385 \times 60.0 = \boxed{1.16 \times 10^5 \text{ J} = 116 \text{ kJ}}$

### Answer 2
**(a)** $Q_{\text{melt}} = mL_f = 0.500 \times 3.34 \times 10^5 = \boxed{1.67 \times 10^5 \text{ J}}$

**(b)** Energy available from cooling water to 0°C:
$Q_{\text{avail}} = m_w c_w \Delta\theta = 2.00 \times 4186 \times 30.0 = 2.51 \times 10^5 \text{ J}$

Since $Q_{\text{avail}} > Q_{\text{melt}}$ ($2.51 \times 10^5 > 1.67 \times 10^5$), **yes**, all the ice melts.

**(c)** After melting, we have 0.500 kg of water at 0°C and 2.00 kg of water that has been cooled. The energy remaining after melting:
$Q_{\text{remaining}} = 2.51 \times 10^5 - 1.67 \times 10^5 = 8.40 \times 10^4 \text{ J}$

This energy warms 2.50 kg of water:
$Q = (m_{\text{ice}} + m_w)c_w\Delta\theta$
$8.40 \times 10^4 = 2.50 \times 4186 \times \Delta\theta$
$\Delta\theta = \frac{8.40 \times 10^4}{2.50 \times 4186} = 8.03 \text{ K}$

Final temperature: $\boxed{8.03\text{°C}}$

### Answer 3
During boiling, the energy supplied goes into **breaking intermolecular bonds** rather than increasing kinetic energy. The potential energy component of internal energy increases (molecules move apart to form vapor), while the kinetic energy (temperature) remains constant. Thus, internal energy $U$ **increases** during boiling even though temperature doesn't change. The energy per unit mass for this process is the latent heat of vaporization.

### Answer 4
**Stage 1:** Solid −20.0°C → 50.0°C: $\Delta\theta = 70.0 \text{ K}$
$Q_1 = 0.100 \times 1500 \times 70.0 = 10,500 \text{ J}$

**Stage 2:** Melt at 50.0°C:
$Q_2 = 0.100 \times 4.00 \times 10^4 = 4,000 \text{ J}$

**Stage 3:** Liquid 50.0°C → 150.0°C: $\Delta\theta = 100.0 \text{ K}$
$Q_3 = 0.100 \times 2500 \times 100.0 = 25,000 \text{ J}$

**Stage 4:** Vaporize at 150.0°C:
$Q_4 = 0.100 \times 8.50 \times 10^5 = 85,000 \text{ J}$

**Total:** $Q = 10,500 + 4,000 + 25,000 + 85,000 = \boxed{1.245 \times 10^5 \text{ J} \approx 125 \text{ kJ}}$

### Answer 5
**Step 1:** Heat ice from −5.0°C to 0°C:
$Q_1 = 0.0500 \times 2100 \times 5.0 = 525 \text{ J}$

**Step 2:** Melt ice at 0°C:
$Q_2 = 0.0500 \times 3.34 \times 10^5 = 16,700 \text{ J}$

Total to bring ice to water at 0°C: $525 + 16,700 = 17,225 \text{ J}$

**Step 3:** Check if this energy can come from cooling 0.300 kg of water from 40.0°C to 0°C:
$Q_{\text{max}} = 0.300 \times 4186 \times 40.0 = 50,232 \text{ J}$

Since $Q_{\text{max}} > 17,225 \text{ J}$, all ice melts and the resulting water warms.

**Step 4:** Final temperature with 0.350 kg total water:
Energy remaining = $50,232 - 17,225 = 33,007 \text{ J}$

$33,007 = 0.350 \times 4186 \times (T_f - 0)$

$T_f = \frac{33,007}{0.350 \times 4186} = \frac{33,007}{1465.1} = 22.5\text{°C}$

$$\boxed{T_f \approx 22.5\text{°C}}$$

---

## Key Takeaways
1. **Temperature** measures average kinetic energy; convert between °C and K using $T(\text{K}) = T(\text{°C}) + 273$.
2. **Specific heat capacity** $Q = mc\Delta\theta$ governs temperature changes.
3. **Specific latent heat** $Q = mL$ governs phase changes at constant temperature.
4. **Internal energy** = kinetic (temperature) + potential (intermolecular bonds) contributions.
5. Phase changes involve potential energy changes at constant temperature.
6. **Heating curves** show temperature plateaus during melting and boiling.
