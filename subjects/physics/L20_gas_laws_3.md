# Lesson 20: Gas Laws III — Molecular Kinetic Energy and Pressure

## What You'll Learn
- Relate the pressure of a gas to the motion of its molecules
- Use $p = \frac{1}{3}\rho\langle v^2\rangle$ to connect macroscopic pressure to microscopic molecular speed
- Calculate the average kinetic energy of gas molecules: $\bar{E}_k = \frac{3}{2}k_B T$
- Determine root-mean-square speed from temperature and molar mass
- Interpret the Maxwell-Boltzmann distribution qualitatively

---

## 1. From Bouncing Molecules to Pressure

### 1.1 Why This Matters

The ideal gas equation $pV = nRT$ describes how gases behave, but it does not explain WHY they behave that way. Why does pressure increase with temperature? Why does squeezing a gas raise its pressure? To answer these questions, we must look inside the gas — at the molecules themselves.

The kinetic theory of gases connects the macroscopic world (pressure, temperature, volume — things we can measure with instruments) to the microscopic world (molecules moving, colliding, bouncing off walls). This connection is one of the most beautiful achievements of 19th-century physics. It shows that temperature is not some mysterious fluid but simply a measure of the average kinetic energy of molecules. When you feel something as "hot," you are feeling molecules hitting your skin harder and faster.

### 1.2 The Model — Assumptions of Kinetic Theory

The kinetic theory makes five simplifying assumptions about an ideal gas. You should know these for the exam:

1. **The gas consists of a large number of identical molecules.** This allows us to use statistical averages. The behaviour of any individual molecule is random, but the average behaviour of billions of molecules is predictable.

2. **The molecules are in constant, random motion.** They move in straight lines between collisions, in all directions with equal probability. No direction is preferred.

3. **The volume of the molecules themselves is negligible compared to the volume of the container.** This is why the model is "ideal" — real molecules do occupy space, but at low pressures the space between them is so vast that their own size is irrelevant.

4. **There are no forces between molecules except during collisions.** Between collisions, molecules move freely. They do not attract or repel each other. This is another idealisation — real molecules have weak attractive forces (van der Waals forces) that cause deviations at high pressure.

5. **All collisions are perfectly elastic.** When molecules hit each other or the container walls, kinetic energy is conserved. No energy is lost to deformation, sound, or heat. The total kinetic energy of all molecules remains constant unless the gas is heated or cooled.

---

## 2. The Pressure Equation

### 2.1 Deriving the Link

When a molecule hits a wall and bounces back, its momentum changes. By Newton's Second Law, a change in momentum means a force was applied. Billions of such collisions per second, spread over the wall's area, produce the steady force we measure as pressure.

The full derivation involves considering one molecule bouncing between two walls, calculating the force it exerts, then averaging over all molecules in all directions. The result is:

$$p = \frac{1}{3}\rho\langle v^2\rangle$$

where:
- $p$ is the pressure (Pa)
- $\rho$ is the density of the gas (kg m⁻³)
- $\langle v^2\rangle$ is the mean square speed of the molecules (m² s⁻²)

You do not need to reproduce the full derivation in an IB exam, but you SHOULD understand what this equation means physically:

- **Higher density ($\rho$)** → more molecules per unit volume → more collisions per second → higher pressure
- **Higher mean square speed ($\langle v^2\rangle$)** → molecules hit harder AND more often → higher pressure
- The factor $\frac{1}{3}$ comes from averaging over three dimensions — only one-third of the molecular motion is directed toward any given wall at any given time

### 2.2 Root-Mean-Square Speed

The quantity $\sqrt{\langle v^2\rangle}$ is called the **root-mean-square speed**, written $v_{\text{rms}}$. It is a measure of the typical speed of molecules in the gas. It is NOT the same as the average speed (the rms speed is always slightly larger because squaring gives more weight to faster molecules).

Combining $p = \frac{1}{3}\rho\langle v^2\rangle$ with the ideal gas equation $pV = nRT$, and noting that $\rho = \frac{\text{mass}}{\text{volume}} = \frac{nM}{V}$ (where $M$ is the molar mass), we get:

$$v_{\text{rms}} = \sqrt{\frac{3RT}{M}}$$

This is one of the most important results in kinetic theory. It tells us that the typical speed of gas molecules depends on two things: the temperature (higher $T$ → faster molecules) and the molar mass (heavier molecules → slower at the same temperature).

**IMPORTANT:** $M$ must be in kilograms per mole (kg mol⁻¹), NOT grams per mole. If a problem says "molar mass = 32 g mol⁻¹", you must convert to $0.032\text{ kg mol}^{-1}$ before using this formula.

---

## 3. Temperature and Kinetic Energy

### 3.1 The Fundamental Connection

Pressure arises from molecular collisions; collisions involve kinetic energy; kinetic energy depends on speed. What, then, is temperature?

From the kinetic theory, we can derive that the **average translational kinetic energy** of a molecule in an ideal gas is:

$$\bar{E}_k = \frac{3}{2}k_B T$$

where $k_B = 1.38 \times 10^{-23}\text{ J K}^{-1}$ is Boltzmann's constant.

This equation is profound. It says that temperature is directly proportional to the average kinetic energy of molecules. There is nothing else to temperature — it IS a measure of molecular motion. Absolute zero ($0\text{ K}$) is the temperature at which molecular motion would theoretically cease (in classical physics; quantum mechanics tells us there is still zero-point energy, but that is beyond IB scope).

### 3.2 Per Mole

For one mole of gas, multiply by Avogadro's number ($N_A k_B = R$):

$$\bar{E}_k^{\text{(per mole)}} = \frac{3}{2}RT$$

For $n$ moles: total internal kinetic energy (for a monatomic ideal gas) = $\frac{3}{2}nRT$.

### 3.3 The Factor of 3/2 — Where Does It Come From?

The factor $\frac{3}{2}$ comes from the **equipartition of energy**. A molecule in three-dimensional space can move in three independent directions ($x$, $y$, $z$). Each of these "degrees of freedom" contributes $\frac{1}{2}k_B T$ to the average kinetic energy. Three degrees of freedom gives $\frac{3}{2}k_B T$.

For monatomic gases (helium, neon, argon), this is the entire story — the atoms can only translate, not rotate or vibrate, so all their thermal energy is translational kinetic energy. For diatomic and polyatomic gases, rotational and vibrational degrees of freedom contribute additional energy, which we study in thermodynamics (Lesson 21).

### 3.4 Common Misconceptions

**Misconception 1:** "$\bar{E}_k = \frac{3}{2}k_B T$ means that at a given temperature, all molecules have the same kinetic energy." They emphatically do not. This is an AVERAGE. At any instant, some molecules are moving much faster and some much slower. The distribution of speeds is described by the Maxwell-Boltzmann distribution (see Section 4). What the equation tells you is the mean.

**Misconception 2 (from your diagnostic):** You wrote "Ek = 2/3 kt²." The correct formula is $\bar{E}_k = \frac{3}{2}k_B T$. Note: it is three-halves, not two-thirds. The temperature is to the first power, not squared. Boltzmann's constant is $k_B$, not $k$. These details matter — getting them wrong changes the physics completely.

**Misconception 3:** "If you double the Celsius temperature, you double the kinetic energy." Doubling the Celsius temperature does NOT double the kelvin temperature (unless you start at $0^\circ\text{C}$). Always use kelvin.

---

## 4. The Maxwell-Boltzmann Distribution

### 4.1 Not All Molecules Move at the Same Speed

The molecules in a gas do not all move at $v_{\text{rms}}$. They have a distribution of speeds — some are slow, most are near the average, and a few are very fast. The shape of this distribution was derived by James Clerk Maxwell and Ludwig Boltzmann.

The distribution depends on temperature and molar mass:
- At higher temperatures, the distribution shifts to the right (higher speeds) and broadens (wider spread of speeds)
- For heavier molecules at the same temperature, the distribution shifts to the left (lower speeds) and narrows

The rms speed is always larger than the average speed, which is larger than the most probable speed (the peak of the distribution). This is because the distribution has a long tail on the high-speed side.

### 4.2 Why This Matters

The high-speed tail of the distribution explains several important phenomena:
- **Evaporation:** Even in cool water, a few molecules have enough speed to escape the liquid surface. This is why puddles dry up even on cold days.
- **Chemical reactions:** Only molecules with energy above the activation barrier can react. The distribution tells you what fraction of molecules have sufficient energy at a given temperature.
- **Why the atmosphere retains light gases:** At a given temperature, hydrogen and helium molecules move fast enough that a significant fraction exceed Earth's escape velocity, which is why these gases are rare in our atmosphere.

---

## Worked Examples

### Worked Example 20.1 — RMS Speed of Air Molecules

**Problem:** Calculate the root-mean-square speed of nitrogen molecules (N₂, molar mass $28\text{ g mol}^{-1}$) at room temperature ($20^\circ\text{C}$).

**Approach:** Use $v_{\text{rms}} = \sqrt{3RT/M}$. Convert temperature to kelvin and molar mass to kg/mol.

**Solution:**
$T = 20 + 273 = 293\text{ K}$
$M = 28 \times 10^{-3}\text{ kg mol}^{-1}$

$$v_{\text{rms}} = \sqrt{\frac{3(8.31)(293)}{28 \times 10^{-3}}} = \sqrt{\frac{7,304}{0.028}} = \sqrt{260,857} = 511\text{ m s}^{-1}$$

**Why this makes sense:** 511 m s⁻¹ is about 1,840 km/h — faster than a bullet from some guns. Air molecules are constantly zipping around at tremendous speeds. The reason smells take time to travel across a room is not that molecules are slow, but that they undergo billions of collisions per second, bouncing in random directions — the net drift (diffusion) is much slower than the instantaneous speed.

---

### Worked Example 20.2 — Average Kinetic Energy

**Problem:** Calculate the average translational kinetic energy of a helium atom at $100^\circ\text{C}$.

**Approach:** Use $\bar{E}_k = \frac{3}{2}k_B T$. Convert temperature to kelvin.

**Solution:**
$T = 100 + 273 = 373\text{ K}$

$$\bar{E}_k = \frac{3}{2}(1.38 \times 10^{-23})(373) = 7.72 \times 10^{-21}\text{ J}$$

In electronvolts: $\bar{E}_k = 7.72 \times 10^{-21} / 1.60 \times 10^{-19} = 0.048\text{ eV}$

**Why this makes sense:** Molecular kinetic energies at everyday temperatures are tiny fractions of an electronvolt. For comparison, chemical bonds are typically 1–5 eV, and nuclear processes involve MeV. This is why chemical reactions require catalysts or heating — individual molecular collisions at room temperature generally lack the energy to break bonds.

---

### Worked Example 20.3 — Pressure from Molecular Motion

**Problem:** A gas has density $\rho = 1.2\text{ kg m}^{-3}$ and its molecules have an rms speed of $500\text{ m s}^{-1}$. Calculate the pressure exerted by the gas.

**Approach:** Use $p = \frac{1}{3}\rho\langle v^2\rangle$. Note that $\langle v^2\rangle = v_{\text{rms}}^2$.

**Solution:**
$$p = \frac{1}{3}(1.2)(500)^2 = \frac{1}{3}(1.2)(250,000) = \frac{300,000}{3} = 100,000\text{ Pa} = 1.0 \times 10^5\text{ Pa}$$

**Why this makes sense:** This is approximately atmospheric pressure, which is consistent with air at sea level having roughly this density and molecular speed.

---

### Worked Example 20.4 — Comparing Molecular Speeds

**Problem:** A container holds a mixture of helium (molar mass $4.0\text{ g mol}^{-1}$) and oxygen (molar mass $32\text{ g mol}^{-1}$) at the same temperature. Calculate the ratio of their rms speeds $v_{\text{rms,He}} / v_{\text{rms,O}_2}$.

**Approach:** At the same temperature, $v_{\text{rms}} \propto 1/\sqrt{M}$. The ratio is the inverse square root of the molar mass ratio.

**Solution:**
$$\frac{v_{\text{rms,He}}}{v_{\text{rms,O}_2}} = \sqrt{\frac{M_{\text{O}_2}}{M_{\text{He}}}} = \sqrt{\frac{32}{4.0}} = \sqrt{8} = 2.83$$

**Why this makes sense:** Helium atoms are 8 times lighter than oxygen molecules, so they move $\sqrt{8} \approx 2.8$ times faster at the same temperature. This is why helium escapes Earth's atmosphere much more readily than heavier gases.

---

### Worked Example 20.5 — IB-Style Combined Problem

**Problem:** A sealed container of volume $0.010\text{ m}^3$ contains argon gas (molar mass $40\text{ g mol}^{-1}$, monatomic) at a pressure of $3.0 \times 10^5\text{ Pa}$ and temperature $27^\circ\text{C}$.

(a) Calculate the number of moles of argon. (1 mark)

(b) Determine the total internal kinetic energy of the argon gas. (2 marks)

(c) Calculate the root-mean-square speed of the argon atoms. (2 marks)

(d) The gas is heated to $127^\circ\text{C}$ at constant volume. State and explain the effect on: (i) the rms speed, (ii) the average kinetic energy per atom, and (iii) the pressure. (3 marks)

**Solution (a):**
$T = 27 + 273 = 300\text{ K}$
$$n = \frac{pV}{RT} = \frac{(3.0 \times 10^5)(0.010)}{(8.31)(300)} = \frac{3,000}{2,493} = 1.20\text{ mol}$$

**(b):**
For a monatomic gas, total internal kinetic energy = $\frac{3}{2}nRT$.
$$E_k = \frac{3}{2}(1.20)(8.31)(300) = 4,487\text{ J} \approx 4,500\text{ J}$$

**(c):**
$M = 40 \times 10^{-3}\text{ kg mol}^{-1}$
$$v_{\text{rms}} = \sqrt{\frac{3RT}{M}} = \sqrt{\frac{3(8.31)(300)}{0.040}} = \sqrt{186,975} = 432\text{ m s}^{-1}$$

**(d):**
$T_2 = 127 + 273 = 400\text{ K}$. The kelvin temperature increases by a factor of $400/300 = 1.33$.

(i) $v_{\text{rms}} \propto \sqrt{T}$, so the rms speed increases by a factor of $\sqrt{1.33} = 1.15$ — about a 15% increase.

(ii) $\bar{E}_k = \frac{3}{2}k_B T$, so average KE per atom increases by the same factor as temperature — 33%. The KE increases faster than the rms speed because KE $\propto v^2$.

(iii) At constant volume, $p \propto T$ (Gay-Lussac's Law), so pressure also increases by 33%, from $3.0 \times 10^5$ to $4.0 \times 10^5\text{ Pa}$. This makes sense at the molecular level: higher temperature means atoms hit the walls harder and more often, raising the pressure.

---

## Practice Problems

### Problem 1
Calculate the root-mean-square speed of oxygen molecules (O₂, molar mass $32\text{ g mol}^{-1}$) at $0^\circ\text{C}$.

### Problem 2
A molecule in an ideal gas at $227^\circ\text{C}$ has a certain average kinetic energy. At what Celsius temperature would the average kinetic energy be half this value?

### Problem 3
A gas at pressure $2.0 \times 10^5\text{ Pa}$ has density $1.5\text{ kg m}^{-3}$. Calculate the root-mean-square speed of its molecules.

### Problem 4
A container holds equal numbers of helium atoms and neon atoms (molar mass $20\text{ g mol}^{-1}$) at the same temperature. The rms speed of helium atoms is $1,360\text{ m s}^{-1}$. Calculate the rms speed of the neon atoms.

### Problem 5 — IB-Style Examination Question
A cylinder contains $0.15\text{ mol}$ of an ideal monatomic gas at $300\text{ K}$.

(a) Calculate the total internal kinetic energy of the gas. (2 marks)

(b) The gas temperature is increased to $450\text{ K}$. Calculate the change in the internal kinetic energy of the gas. (2 marks)

(c) On average, how much kinetic energy does a single atom of the gas gain as a result of this temperature increase? Express your answer in joules and in electronvolts. (2 marks)

(d) Sketch a Maxwell-Boltzmann speed distribution curve for the gas at $300\text{ K}$ and at $450\text{ K}$ on the same axes. Label each curve with its temperature. Explain the differences between the two curves in terms of: (i) the position of the peak, (ii) the height of the peak, and (iii) the width of the distribution. (3 marks)

---

## Answers

### Answer 1
$T = 0 + 273 = 273\text{ K}$, $M = 0.032\text{ kg mol}^{-1}$
$$v_{\text{rms}} = \sqrt{\frac{3(8.31)(273)}{0.032}} = \sqrt{212,681} = 461\text{ m s}^{-1}$$

### Answer 2
$T_1 = 227 + 273 = 500\text{ K}$. $\bar{E}_k \propto T$, so half the KE means half the kelvin temperature: $T_2 = 250\text{ K}$. In Celsius: $250 - 273 = -23^\circ\text{C}$. Note: "half of $227^\circ\text{C}$" would be $113.5^\circ\text{C}$, which is wrong. Always use kelvin.

### Answer 3
$$v_{\text{rms}} = \sqrt{\frac{3p}{\rho}} = \sqrt{\frac{3(2.0 \times 10^5)}{1.5}} = \sqrt{4.0 \times 10^5} = 632\text{ m s}^{-1}$$

### Answer 4
$$\frac{v_{\text{rms,Ne}}}{v_{\text{rms,He}}} = \sqrt{\frac{M_{\text{He}}}{M_{\text{Ne}}}} = \sqrt{\frac{4.0}{20}} = \sqrt{0.20} = 0.447$$
$$v_{\text{rms,Ne}} = 1,360 \times 0.447 = 608\text{ m s}^{-1}$$

### Answer 5 — IB-Style
**(a)** $E_k = \frac{3}{2}nRT = \frac{3}{2}(0.15)(8.31)(300) = 561\text{ J}$. (2 marks — 1 for formula, 1 for answer)

**(b)** $E_k(450\text{ K}) = \frac{3}{2}(0.15)(8.31)(450) = 841\text{ J}$. $\Delta E_k = 841 - 561 = 280\text{ J}$. (2 marks)

**(c)** Number of atoms: $N = nN_A = 0.15(6.02 \times 10^{23}) = 9.03 \times 10^{22}$. Energy gain per atom: $280 / 9.03 \times 10^{22} = 3.10 \times 10^{-21}\text{ J} = 0.0194\text{ eV}$. (2 marks)

**(d)** (3 marks) The 450 K curve is shifted to the right (higher speeds), is lower in height (same total area but spread over wider range), and is broader (wider distribution of speeds). The peak moves right because the most probable speed increases with temperature. The height decreases because the same number of molecules is spread across a wider range of speeds. The width increases because higher temperature means greater variation in molecular speeds. (1 mark for each correct observation with explanation.)

---

## Key Takeaways

1. **Kinetic theory connects micro and macro:** Pressure comes from molecular collisions with walls. Temperature is proportional to average molecular KE.

2. **Pressure equation:** $p = \frac{1}{3}\rho\langle v^2\rangle$. Higher density or faster molecules → higher pressure.

3. **RMS speed:** $v_{\text{rms}} = \sqrt{3RT/M}$. Lighter molecules and higher temperatures give faster speeds.

4. **Average KE:** $\bar{E}_k = \frac{3}{2}k_B T$. You wrote $\frac{2}{3}kT^2$ on your diagnostic. The correct formula is $\frac{3}{2}k_B T$. Memorise it.

5. **Maxwell-Boltzmann distribution:** A spread of speeds exists. Higher $T$ shifts the curve right and broadens it. Heavier molecules shift it left.
