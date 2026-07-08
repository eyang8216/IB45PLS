# Lesson 13: Special Relativity IV — Relativistic Mechanics (HL)

## What You'll Learn
- Calculate relativistic momentum $p = \gamma mv$
- Use mass-energy equivalence $E_0 = mc^2$ and total energy $E = \gamma mc^2$
- Distinguish between rest energy, kinetic energy, and total energy
- Apply the relativistic velocity addition formula

---

## 1. Relativistic Momentum

### 1.1 Why $p = mv$ Isn't Enough

In Newtonian physics, momentum is $p = mv$. If you apply a constant force, speed increases without limit — eventually exceeding $c$. But nothing can exceed $c$. The fix: momentum grows faster than linearly as speed approaches $c$:

$$p = \gamma mv$$

As $v \to c$, $\gamma \to \infty$, so $p \to \infty$. You can keep adding momentum (by applying force), but the speed gets closer and closer to $c$ without ever reaching it. This is why particle accelerators can pump enormous energy into protons yet never quite reach $c$.

---

## 2. Mass-Energy Equivalence

### 2.1 Einstein's Most Famous Equation

Every object has **rest energy** by virtue of its mass:

$$E_0 = mc^2$$

A 1 kg mass at rest contains $9 \times 10^{16}\text{ J}$ of energy — equivalent to about 20 megatons of TNT. This is the energy released in nuclear reactions (fission and fusion) when a tiny fraction of mass is converted to kinetic energy.

### 2.2 Total Energy and Kinetic Energy

**Total energy** of a moving particle:
$$E = \gamma mc^2 = \gamma E_0$$

**Relativistic kinetic energy** — the energy due to motion:
$$E_k = E - E_0 = (\gamma - 1)mc^2$$

At low speeds ($v \ll c$), this approximates $\frac{1}{2}mv^2$ (you can show this using a binomial expansion). At high speeds, it diverges dramatically.

### 2.3 The Energy-Momentum Relation

$$E^2 = p^2c^2 + m^2c^4$$

This is the full relativistic energy-momentum relation. For a massless particle ($m = 0$, like a photon): $E = pc$. For a particle at rest ($p = 0$): $E = mc^2$. Both are special cases of this single equation.

---

## 3. Relativistic Velocity Addition

### 3.1 Why $u + v$ Doesn't Work

If a spaceship moves at $0.6c$ relative to Earth and fires a probe forward at $0.6c$ relative to the ship, the probe's speed relative to Earth is NOT $1.2c$. The correct relativistic formula:

$$u' = \frac{u + v}{1 + \frac{uv}{c^2}}$$

where $u$ is the probe's speed in the ship frame and $v$ is the ship's speed relative to Earth.

For the example: $u' = \frac{0.6c + 0.6c}{1 + (0.6)(0.6)} = \frac{1.2c}{1.36} = 0.882c$. Less than $c$, as required.

**Check:** If either speed is $c$, the result is always $c$ — consistent with Postulate 2.

---

## Worked Examples

### Worked Example 13.1 — Relativistic Momentum

**Problem:** An electron moves at $0.99c$. Its rest mass is $9.11 \times 10^{-31}\text{ kg}$. Find its relativistic momentum.

**Solution:**
$\gamma = 1/\sqrt{1-0.99^2} = 1/\sqrt{0.0199} = 7.09$.
$p = \gamma mv = (7.09)(9.11\times 10^{-31})(0.99 \times 3.00\times 10^8) = 1.92 \times 10^{-21}\text{ kg m s}^{-1}$.
Compare Newtonian: $p = mv = 2.71 \times 10^{-22}$. Relativistic is 7× larger.

---

### Worked Example 13.2 — Nuclear Energy

**Problem:** In a nuclear reaction, $0.010\text{ kg}$ of mass is converted to energy. How much energy is released?

**Solution:**
$E = mc^2 = (0.010)(3.00\times 10^8)^2 = 9.0 \times 10^{14}\text{ J}$.

---

### Worked Example 13.3 — Velocity Addition

**Problem:** Two spacecraft approach each other, each moving at $0.70c$ relative to Earth. What is their relative speed as measured by one spacecraft?

**Solution:**
Both moving at $0.70c$ in Earth frame. In one spacecraft's frame, Earth approaches at $0.70c$ and the other spacecraft approaches Earth at $0.70c$. Relative speed: $u' = (0.70c + 0.70c)/(1 + 0.49) = 1.40c/1.49 = 0.94c$. Always less than $c$.

---

## Practice Problems

### Problem 1
A proton ($m = 1.67 \times 10^{-27}\text{ kg}$) moves at $0.90c$. Find $\gamma$, relativistic momentum, and kinetic energy in joules and MeV.

### Problem 2
Calculate the rest energy of an electron in joules and MeV.

### Problem 3
A spaceship moves at $0.80c$ and fires a missile forward at $0.50c$ relative to the ship. Find the missile's speed relative to Earth.

### Problem 4
Show that for $v \ll c$, the relativistic kinetic energy $(\gamma - 1)mc^2$ approximates $\frac{1}{2}mv^2$.

### Problem 5 — IB-Style
A proton (rest mass $938\text{ MeV}/c^2$) is accelerated to a total energy of $2,500\text{ MeV}$.

(a) Calculate $\gamma$ and the proton's speed as a fraction of $c$. (3 marks)
(b) Determine the proton's kinetic energy in MeV. (1 mark)
(c) Calculate the proton's relativistic momentum in $\text{MeV}/c$. (2 marks)
(d) If the proton were instead a photon with the same total energy, what would be its momentum? (1 mark)

---

## Answers

### Answer 1
$\gamma = 1/\sqrt{1-0.81} = 2.29$. $p = (2.29)(1.67\times 10^{-27})(2.70\times 10^8) = 1.03 \times 10^{-18}\text{ kg m s}^{-1}$. $E_k = (2.29-1)(1.67\times 10^{-27})(9\times 10^{16}) = 1.94 \times 10^{-10}\text{ J} = 1,210\text{ MeV}$.

### Answer 2
$E_0 = (9.11\times 10^{-31})(9\times 10^{16}) = 8.20 \times 10^{-14}\text{ J} = 0.511\text{ MeV}$.

### Answer 3
$u' = (0.50c + 0.80c)/(1 + 0.40) = 1.30c/1.40 = 0.929c$.

### Answer 4
For $v \ll c$: $(\gamma - 1) = (1 - v^2/c^2)^{-1/2} - 1 \approx (1 + \frac{1}{2}v^2/c^2) - 1 = \frac{1}{2}v^2/c^2$. So $E_k \approx \frac{1}{2}mv^2$.

### Answer 5 — IB-Style
**(a)** $\gamma = E/mc^2 = 2,500/938 = 2.67$. $v/c = \sqrt{1 - 1/\gamma^2} = \sqrt{1 - 0.141} = 0.927$. (3 marks)
**(b)** $E_k = 2,500 - 938 = 1,562\text{ MeV}$. (1 mark)
**(c)** $p = \sqrt{E^2 - m^2c^4}/c = \sqrt{2,500^2 - 938^2}/c = \sqrt{5.37\times 10^6}/c = 2,317\text{ MeV}/c$. (2 marks)
**(d)** For photon ($m=0$): $p = E/c = 2,500\text{ MeV}/c$. (1 mark)

---

## Key Takeaways

1. **Relativistic momentum:** $p = \gamma mv$. Grows without bound as $v \to c$, preventing $v$ from reaching $c$.

2. **Rest energy:** $E_0 = mc^2$. Total energy: $E = \gamma mc^2$. Kinetic: $E_k = (\gamma-1)mc^2$.

3. **$E^2 = p^2c^2 + m^2c^4$** — the full energy-momentum relation. For photons ($m=0$): $E = pc$.

4. **Velocity addition:** $u' = (u+v)/(1+uv/c^2)$. Always gives result less than $c$. Reduces to $u+v$ for small speeds.
