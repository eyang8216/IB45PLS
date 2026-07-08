# Lesson 23: Thermodynamics III — The Second Law and Entropy (HL)

## What You'll Learn
- State the Second Law of Thermodynamics in both the Clausius and Kelvin-Planck forms
- Define entropy as a measure of disorder and calculate entropy changes for reversible processes
- Explain why entropy always increases in isolated systems
- Understand why heat engines cannot be 100% efficient
- Appreciate that the entropy increase of the universe gives time its direction

---

## 1. Why We Need a Second Law

### 1.1 The First Law Is Not Enough

The First Law says energy is conserved. It tells us that if a gas expands and does work, it must lose internal energy or absorb heat. What the First Law does NOT tell us is why certain energy transfers happen spontaneously and others never do.

A hot cup of coffee cools to room temperature. The First Law would be perfectly satisfied if the coffee got hotter while the room got colder — the total energy would still be conserved. But we never observe this. A dropped egg splatters; the reverse — a splattered egg reassembling itself — conserves energy too, but we never see it.

Something deeper than energy conservation determines the direction of natural processes. That something is entropy.

### 1.2 Two Equivalent Statements

The Second Law can be stated in several equivalent ways. The IB syllabus uses these two:

**Clausius statement:** Heat cannot spontaneously flow from a colder body to a hotter body. To move heat from cold to hot, you must do work (this is what a refrigerator does — it's not spontaneous; it requires an electric motor).

**Kelvin-Planck statement:** It is impossible to construct a heat engine that, operating in a cycle, converts ALL the heat absorbed from a single reservoir into work. Some heat must always be rejected to a colder reservoir.

These two statements are equivalent — each implies the other. Together, they explain why heat engines cannot be 100% efficient and why refrigerators need power input.

---

## 2. What Is Entropy?

### 2.1 A Measure of Disorder

Entropy ($S$) is a measure of the disorder or randomness of a system. A highly ordered system (like a crystal at low temperature) has low entropy. A highly disordered system (like a gas filling its container randomly) has high entropy.

The Second Law, stated in terms of entropy: **The total entropy of an isolated system never decreases. It either increases or, in ideal reversible processes, remains constant.**

$$\Delta S_{\text{total}} \geq 0$$

This is a law of nature as fundamental as conservation of energy. The entropy of the universe is always increasing.

### 2.2 Calculating Entropy Change

For a reversible process at constant temperature, the change in entropy is:

$$\Delta S = \frac{\Delta Q}{T}$$

where:
- $\Delta S$ is the change in entropy (J K⁻¹)
- $\Delta Q$ is the heat transferred (J)
- $T$ is the absolute temperature (K) at which the transfer occurs

When heat enters a system ($\Delta Q > 0$), its entropy increases. When heat leaves ($\Delta Q < 0$), its entropy decreases. The TOTAL entropy of system + surroundings must increase or stay the same.

### 2.3 Entropy in Reversible vs. Irreversible Processes

**Reversible process:** The system passes through a continuous sequence of equilibrium states. The process can be reversed by an infinitesimal change in conditions. For a reversible process: $\Delta S_{\text{total}} = 0$ — the entropy of the system may change, but the surroundings change by an equal and opposite amount.

**Irreversible process:** The system moves through non-equilibrium states. The process cannot be reversed without leaving a permanent change in the universe. For an irreversible process: $\Delta S_{\text{total}} > 0$ — entropy is generated.

All real processes are, to some degree, irreversible. Friction, turbulence, heat flow across finite temperature differences, mixing — all generate entropy.

---

## 3. The Arrow of Time

### 3.1 Why Time Moves Forward

The laws of mechanics (Newton's equations, Schrödinger's equation) are time-symmetric — they work equally well forward and backward in time. If you watch a film of two billiard balls colliding, you cannot tell whether the film is running forward or backward. Both directions obey the laws of physics.

But if you watch a film of an egg breaking, you instantly know which direction is forward. The un-breaking of an egg does not violate energy conservation, but it would represent a spontaneous decrease in entropy — and the Second Law forbids that.

The increase of entropy gives time its direction. The universe began in a state of extremely low entropy (the Big Bang) and has been moving toward higher entropy ever since. This is often called the "arrow of time."

### 3.2 The Heat Death of the Universe

If the universe continues expanding and entropy continues increasing, eventually the universe will reach a state of maximum entropy — thermal equilibrium, where everything is at the same temperature. At that point, no work can be extracted, no life can exist, and no interesting processes can occur. This hypothetical end state is called the "heat death of the universe." It is a consequence of relentless entropy increase on cosmic timescales.

---

## 4. Entropy and Heat Engines — The Deeper Connection

### 4.1 Why Engines Must Reject Heat

Consider a heat engine that absorbs heat $Q_h$ from a hot reservoir at $T_h$ and rejects $Q_c$ to a cold reservoir at $T_c$. The engine itself returns to its initial state after each cycle, so $\Delta S_{\text{engine}} = 0$.

The total entropy change of the universe is:
$$\Delta S_{\text{total}} = \Delta S_{\text{hot}} + \Delta S_{\text{cold}} = -\frac{Q_h}{T_h} + \frac{Q_c}{T_c}$$

The hot reservoir loses entropy (negative) because heat leaves it. The cold reservoir gains entropy (positive) because heat enters it. For the process to be allowed ($\Delta S_{\text{total}} \geq 0$):
$$\frac{Q_c}{T_c} \geq \frac{Q_h}{T_h} \quad \Rightarrow \quad \frac{Q_c}{Q_h} \geq \frac{T_c}{T_h}$$

Since $Q_c = Q_h - W$:
$$\frac{Q_h - W}{Q_h} \geq \frac{T_c}{T_h} \quad \Rightarrow \quad 1 - \frac{W}{Q_h} \geq \frac{T_c}{T_h} \quad \Rightarrow \quad \eta_{\text{max}} = 1 - \frac{T_c}{T_h}$$

**The Carnot efficiency limit arises directly from the requirement that entropy not decrease.** It is not an engineering limitation — it is a law of nature.

---

## 5. Examples of Entropy Increase in Everyday Life

- **Mixing:** When you pour milk into coffee, the two liquids mix and never spontaneously unmix. The mixed state is more disordered (higher entropy) than the separated state.

- **Melting:** Ice melts at room temperature. The liquid state has higher entropy than the solid state because molecules in a liquid are more randomly arranged.

- **Evaporation:** A puddle dries up. Water molecules in the vapour phase have vastly more positional randomness than in the liquid phase.

- **Diffusion:** A drop of ink spreads through water. The ink molecules distributed randomly throughout the water represent a much higher-entropy state than ink concentrated in one spot.

---

## Worked Examples

### Worked Example 23.1 — Entropy Change in Melting

**Problem:** $0.10\text{ kg}$ of ice at $0^\circ\text{C}$ melts to water at $0^\circ\text{C}$. The latent heat of fusion of ice is $3.34 \times 10^5\text{ J kg}^{-1}$. Calculate the entropy change of the ice.

**Approach:** Melting occurs at constant temperature ($T = 273\text{ K}$). The heat absorbed is $Q = mL$. $\Delta S = Q/T$.

**Solution:**
$$Q = mL = (0.10)(3.34 \times 10^5) = 33,400\text{ J}$$
$$\Delta S = \frac{Q}{T} = \frac{33,400}{273} = 122.3\text{ J K}^{-1}$$

**Why this makes sense:** The entropy increases (positive) because the liquid state has more disorder than the solid state. The surroundings lose entropy (as they provide the heat), but the total entropy of the universe increases — consistent with a spontaneous process.

---

### Worked Example 23.2 — Carnot Efficiency from Temperatures

**Problem:** A power plant uses steam at $800\text{ K}$ and rejects heat to a cooling tower at $300\text{ K}$. What is the maximum possible efficiency? If real efficiency is 35%, explain the difference.

**Solution:**
$$\eta_{\text{Carnot}} = 1 - \frac{300}{800} = 1 - 0.375 = 0.625 = 62.5\%$$

The real efficiency (35%) is far below the Carnot limit due to irreversible processes: friction in turbines, heat lost through pipes, non-ideal heat transfer across finite temperature differences, and the fact that the working fluid does not follow an ideal Carnot cycle. The Carnot efficiency is a theoretical upper bound that can never be attained in practice.

---

### Worked Example 23.3 — Total Entropy Change

**Problem:** $200\text{ J}$ of heat flows spontaneously from a hot reservoir at $500\text{ K}$ to a cold reservoir at $250\text{ K}$. Calculate the total entropy change of the universe.

**Approach:** The hot reservoir loses entropy ($\Delta S_h = -Q/T_h$). The cold reservoir gains entropy ($\Delta S_c = +Q/T_c$). Total is their sum.

**Solution:**
$$\Delta S_h = -\frac{200}{500} = -0.40\text{ J K}^{-1}$$
$$\Delta S_c = +\frac{200}{250} = +0.80\text{ J K}^{-1}$$
$$\Delta S_{\text{total}} = -0.40 + 0.80 = +0.40\text{ J K}^{-1}$$

**Why this makes sense:** The total entropy is positive — the process is spontaneous and irreversible. The entropy gained by the cold reservoir exceeds the entropy lost by the hot reservoir because the same amount of heat has a larger entropy impact at lower temperature ($\Delta S = Q/T$ is larger when $T$ is smaller).

---

## Practice Problems

### Problem 1
$2.0\text{ kg}$ of water at $100^\circ\text{C}$ is boiled to steam at $100^\circ\text{C}$. The latent heat of vaporisation of water is $2.26 \times 10^6\text{ J kg}^{-1}$. Calculate the entropy change of the water.

### Problem 2
A Carnot engine operates between $500\text{ K}$ and $300\text{ K}$. It absorbs $800\text{ J}$ of heat per cycle. Calculate the work done and the heat rejected per cycle.

### Problem 3
$500\text{ J}$ of heat is transferred from a reservoir at $600\text{ K}$ to a reservoir at $300\text{ K}$. (a) Calculate the total entropy change. (b) Explain why this process, if spontaneous, is consistent with the Second Law.

### Problem 4
Explain why a refrigerator must consume electrical power to transfer heat from its cold interior to the warmer room. Use entropy in your explanation.

### Problem 5 — IB-Style Examination Question
A student claims to have invented an engine that, operating between reservoirs at $400\text{ K}$ and $200\text{ K}$, absorbs $1,000\text{ J}$ of heat and produces $600\text{ J}$ of work.

(a) Calculate the efficiency the student claims. (1 mark)
(b) Calculate the Carnot efficiency for these temperatures. (1 mark)
(c) Show, using entropy considerations, whether this engine is theoretically possible. (3 marks)
(d) Suggest an experimental test that could reveal whether the engine actually works as claimed. (2 marks)
(e) The student's engine, when tested, actually has an efficiency of 30%. The hot reservoir is combustion gases; the cold reservoir is river water. Calculate the mass of river water that must flow through the cooling system per second to maintain the cold reservoir temperature when the engine operates at 10 kW useful power. The specific heat capacity of water is $4,200\text{ J kg}^{-1}\text{ K}^{-1}$ and the maximum allowable temperature rise of the river water is $5.0\text{ K}$. (3 marks)

---

## Answers

### Answer 1
$Q = mL = (2.0)(2.26 \times 10^6) = 4.52 \times 10^6\text{ J}$. $T = 100 + 273 = 373\text{ K}$.
$\Delta S = Q/T = 4.52 \times 10^6/373 = 1.21 \times 10^4\text{ J K}^{-1}$.

### Answer 2
$\eta = 1 - 300/500 = 0.40$. $W = \eta Q_h = 0.40 \times 800 = 320\text{ J}$. $Q_c = 800 - 320 = 480\text{ J}$.

### Answer 3
**(a)** $\Delta S = -500/600 + 500/300 = -0.833 + 1.667 = +0.834\text{ J K}^{-1}$.
**(b)** Total entropy increases, so the process is consistent with the Second Law. The entropy gain at the cold reservoir (larger because $T$ is lower) outweighs the entropy loss at the hot reservoir.

### Answer 4
If heat flowed spontaneously from cold to hot, the total entropy would decrease ($\Delta S = -Q/T_{\text{cold}} + Q/T_{\text{hot}} < 0$), violating the Second Law. A refrigerator uses electrical work to "pump" heat against the temperature gradient. The work input generates additional entropy (through irreversibilities), ensuring the total entropy of the universe still increases. The net effect: $\Delta S = -Q_c/T_c + (Q_c + W)/T_h > 0$ when $W$ is sufficiently large.

### Answer 5 — IB-Style
**(a)** $\eta = W/Q_h = 600/1,000 = 0.60 = 60\%$. (1 mark)

**(b)** $\eta_{\text{Carnot}} = 1 - 200/400 = 0.50 = 50\%$. (1 mark)

**(c)** (3 marks) The claimed efficiency (60%) exceeds the Carnot efficiency (50%), which is impossible. Using entropy: $Q_c = Q_h - W = 400\text{ J}$. $\Delta S_{\text{total}} = -1,000/400 + 400/200 = -2.50 + 2.00 = -0.50\text{ J K}^{-1} < 0$. Total entropy would decrease, violating the Second Law. The engine is theoretically impossible. (1 mark for calculating $Q_c$, 1 mark for entropy calculation, 1 mark for conclusion.)

**(d)** (2 marks) Measure the actual heat absorbed and work output independently. Use a calorimeter to measure $Q_h$ (temperature change of hot reservoir). Measure $W$ with a dynamometer or by having the engine lift a known mass. Compare the measured efficiency to the Carnot limit. If the measured efficiency truly exceeded 50%, it would contradict thermodynamics — more likely, measurement error or an unaccounted heat source explains the claim. (1 mark for method, 1 mark for comparison to Carnot limit.)

**(e)** (3 marks) At 30% efficiency with 10 kW useful power: $P_{\text{in}} = 10/0.30 = 33.3\text{ kW}$. Heat rejected: $P_{\text{rejected}} = 33.3 - 10 = 23.3\text{ kW}$.

Heat rejected per second: $Q = 23,300\text{ J}$. To limit temperature rise to $5.0\text{ K}$: $Q = mc\Delta\theta$, so $m = Q/(c\Delta\theta) = 23,300/(4,200 \times 5.0) = 1.11\text{ kg}$. The river water must flow at $1.11\text{ kg s}^{-1} \approx 1.1\text{ L s}^{-1}$. (1 mark for $P_{\text{in}}$, 1 mark for $P_{\text{rejected}}$, 1 mark for mass flow rate.)

---

## Key Takeaways

1. **Second Law:** Heat won't flow spontaneously from cold to hot. No engine converts all heat to work. Both express that total entropy never decreases.

2. **Entropy:** $\Delta S = Q/T$ for reversible processes. Entropy measures disorder. Isolated systems evolve toward maximum entropy.

3. **Carnot efficiency** $\eta = 1 - T_c/T_h$ arises directly from the requirement $\Delta S_{\text{total}} \geq 0$.

4. **Arrow of time:** Entropy increase gives time its direction. The universe began in a low-entropy state and moves toward heat death.

5. **Every real process generates entropy.** Reversible processes are idealisations. The entropy of the universe increases with every spontaneous change.
