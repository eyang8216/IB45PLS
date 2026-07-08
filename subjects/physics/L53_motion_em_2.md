# Lesson 53: Motion in EM Fields II — Mass Spectrometer and Cyclotron

## What You'll Learn
- Understand how a velocity selector works using crossed E and B fields
- Calculate ion masses in a mass spectrometer from orbit radius
- Explain the operation of a cyclotron and calculate particle energy
- Recognise why the cyclotron frequency is independent of particle speed

---

## 1. The Velocity Selector

### 1.1 Why Filter by Speed?

Mass spectrometers and other particle devices need ions of a specific speed. A velocity selector uses perpendicular electric and magnetic fields to let through only particles with exactly the right speed — too fast or too slow, and they are deflected away.

### 1.2 How It Works

Crossed fields: **E** points downward, **B** points into the page. A positive ion experiences:
- Electric force $F_E = qE$ downward
- Magnetic force $F_B = qvB$ upward (from Fleming's LHR — positive charge moving right, B into page, force is up)

When these balance: $qE = qvB$, giving:
$$v = \frac{E}{B}$$

Only particles with speed $v = E/B$ pass straight through. Slower particles ($v < E/B$) have $F_E > F_B$ and are deflected toward the electric force. Faster particles are deflected the other way.

The selected speed depends only on the field strengths, NOT on the particle's charge or mass. This is a crucial feature: all ions with $v = E/B$ pass, regardless of species.

---

## 2. The Mass Spectrometer

### 2.1 Separating Ions by Mass

A mass spectrometer has three stages:
1. **Ionisation:** Atoms are ionised (typically singly charged, +e)
2. **Velocity selection:** Crossed E and B fields pass only ions with $v = E/B$
3. **Magnetic deflection:** A uniform B-field deflects ions into semicircular paths

In the deflection chamber, the radius is:
$$r = \frac{mv}{qB}$$

Since all ions enter with the same $v$ and $q$, the radius is proportional to mass: $r \propto m$.

Combining with $v = E/B$ from the velocity selector:
$$m = \frac{qrB_{\text{def}}}{v} = \frac{qrB_{\text{def}}B_{\text{sel}}}{E}$$

Heavier ions have larger orbit radii and strike the detector further from the entry point.

---

## 3. The Cyclotron

### 3.1 Accelerating Particles in Spirals

A cyclotron uses a magnetic field to bend particles into circles and an alternating electric field to give them a "kick" twice per orbit. Two hollow D-shaped electrodes ("dees") sit in a uniform B-field. A high-frequency AC voltage is applied between them.

In each dee, the particle moves in a semicircle ($r = mv/qB$). At the gap, the electric field accelerates it into the other dee. With each crossing, the speed increases and the radius grows, producing a spiral path.

### 3.2 The Cyclotron Frequency

The time for a half-circle is independent of speed:
$$T_{\text{half}} = \frac{\pi m}{qB}$$

This is because $r \propto v$, so the distance ($\pi r$) and speed both scale proportionally — they cancel. The cyclotron frequency is:
$$f = \frac{qB}{2\pi m}$$

The AC voltage must match this frequency. For non-relativistic speeds, this frequency is constant.

### 3.3 Maximum Energy

When the spiral reaches the edge of the dees (radius $R$), the particle exits:
$$v_{\text{max}} = \frac{qBR}{m}$$
$$KE_{\text{max}} = \frac{q^2B^2R^2}{2m}$$

---

## Worked Examples

### Worked Example 53.1 — Velocity Selector

**Problem:** A velocity selector has $E = 2.0 \times 10^4\text{ V m}^{-1}$ and $B = 0.10\text{ T}$. (a) What speed passes through? (b) Protons enter at $1.5 \times 10^5\text{ m s}^{-1}$. Which way are they deflected?

**Solution (a):** $v = E/B = 2.0\times 10^4/0.10 = 2.0\times 10^5\text{ m s}^{-1}$.

**(b):** $v = 1.5\times 10^5 < v_{\text{sel}}$. Magnetic force ($\propto v$) is smaller than electric force → deflected in direction of electric force.

---

### Worked Example 53.2 — Mass Spectrometer

**Problem:** Singly charged ions pass through a velocity selector ($E = 5.0 \times 10^3\text{ V m}^{-1}$, $B = 0.20\text{ T}$) into a $0.15\text{ T}$ deflection field. Two ion species strike at $r_1 = 0.12\text{ m}$ and $r_2 = 0.16\text{ m}$. Find their masses in atomic mass units.

**Solution:**
$v = 5.0\times 10^3/0.20 = 2.5\times 10^4\text{ m s}^{-1}$.
$m_1 = qr_1B_{\text{def}}/v = (1.60\times 10^{-19})(0.12)(0.15)/(2.5\times 10^4) = 1.15\times 10^{-25}\text{ kg} = 69.4\text{ u}$.
$m_2 = m_1 \times 0.16/0.12 = 1.54\times 10^{-25}\text{ kg} = 92.5\text{ u}$.

These could be isotopes of gallium (Ga-69 and Ga-71, plus hydrides) or different elements entirely.

---

### Worked Example 53.3 — Cyclotron

**Problem:** A cyclotron with $B = 1.5\text{ T}$ and dee radius $R = 0.80\text{ m}$ accelerates protons. Find: (a) the cyclotron frequency, and (b) the maximum kinetic energy in MeV.

**Solution (a):**
$f = qB/(2\pi m) = (1.60\times 10^{-19})(1.5)/(2\pi \times 1.67\times 10^{-27}) = 2.29 \times 10^7\text{ Hz} = 22.9\text{ MHz}$.

**(b):**
$v_{\text{max}} = qBR/m = (1.60\times 10^{-19})(1.5)(0.80)/(1.67\times 10^{-27}) = 1.15 \times 10^8\text{ m s}^{-1}$. This is 38% of $c$ — relativistic corrections are significant!
$KE_{\text{max}} = \frac{1}{2}mv^2 = \frac{1}{2}(1.67\times 10^{-27})(1.32\times 10^{16}) = 1.10 \times 10^{-11}\text{ J} = 69\text{ MeV}$.

At these speeds, relativistic mass increase shifts the cyclotron frequency — this is why synchrotrons are used for very high energies.

---

## Practice Problems

### Problem 1
A velocity selector uses $E = 1.8 \times 10^4\text{ V m}^{-1}$ and $B = 0.060\text{ T}$. What speed is selected? Doubly charged ions of this speed enter — are they deflected?

### Problem 2
In a mass spectrometer, ions of speed $5.0 \times 10^4\text{ m s}^{-1}$ enter a $0.25\text{ T}$ field. Ions of mass 24 u strike the detector at what radius? ($1\text{ u} = 1.66 \times 10^{-27}\text{ kg}$)

### Problem 3
A cyclotron accelerates alpha particles ($q = +2e$, $m = 6.64 \times 10^{-27}\text{ kg}$) with $B = 0.80\text{ T}$ and $R = 0.60\text{ m}$. Find the frequency and maximum KE.

### Problem 4
Compare a mass spectrometer and a cyclotron: how does each use electric and magnetic fields, and what information does each provide?

### Problem 5 — IB-Style
A mass spectrometer analyses a sample containing two isotopes, both singly charged. The velocity selector uses $E = 3.0 \times 10^3\text{ V m}^{-1}$, $B_{\text{sel}} = 0.060\text{ T}$. The deflection field is $B_{\text{def}} = 0.15\text{ T}$. Two beams strike the detector at radii 8.2 cm and 9.8 cm.

(a) Calculate the speed of ions entering the deflection chamber. (1 mark)
(b) Determine the mass of each isotope in u. (3 marks)
(c) The detector records that the inner peak is 3 times taller than the outer peak. Suggest what this indicates about the sample. (2 marks)
(d) If the velocity selector's electric field drifts by 2%, what percentage error does this introduce in the mass determination? (2 marks)

---

## Answers

### Answer 1
$v = 1.8\times 10^4/0.060 = 3.0\times 10^5\text{ m s}^{-1}$. For doubly charged ions ($q = 2e$): $F_E = 2eE$, $F_B = 2evB$. The factor of 2 cancels. The velocity selector is independent of charge — doubly charged ions with the same speed also pass through.

### Answer 2
$m = 24 \times 1.66\times 10^{-27} = 3.98\times 10^{-26}\text{ kg}$. $r = mv/(qB) = (3.98\times 10^{-26})(5.0\times 10^4)/(1.60\times 10^{-19})(0.25) = 0.050\text{ m} = 5.0\text{ cm}$.

### Answer 3
$f = (2 \times 1.60\times 10^{-19})(0.80)/(2\pi \times 6.64\times 10^{-27}) = 6.13 \times 10^6\text{ Hz}$. $KE_{\text{max}} = (3.20\times 10^{-19})^2(0.80)^2(0.60)^2/(2 \times 6.64\times 10^{-27}) = 2.84 \times 10^{-12}\text{ J} = 17.8\text{ MeV}$.

### Answer 4
Mass spectrometer: uses E+B for velocity selection, then B alone for deflection. $r \propto m$ for fixed $v$ and $q$. Measures mass. Cyclotron: uses B for circular confinement, alternating E for acceleration. Measures nothing — it produces high-energy particles for experiments.

### Answer 5 — IB-Style
**(a)** $v = 3.0\times 10^3/0.060 = 5.0\times 10^4\text{ m s}^{-1}$. (1 mark)

**(b)** $m = qrB_{\text{def}}/v$. $m_1 = (1.60\times 10^{-19})(0.082)(0.15)/(5.0\times 10^4) = 3.94\times 10^{-26}\text{ kg} = 23.7\text{ u}$. $m_2 = (1.60\times 10^{-19})(0.098)(0.15)/(5.0\times 10^4) = 4.70\times 10^{-26}\text{ kg} = 28.3\text{ u}$. (3 marks)

**(c)** The taller inner peak (smaller radius, lighter isotope) at 23.7 u is about 3× more abundant than the heavier isotope at 28.3 u. This could indicate the sample is predominantly one isotope. (2 marks)

**(d)** $m \propto 1/E$, so a 2% change in $E$ gives a 2% error in $m$. Percentage error in mass = percentage error in $E$ = 2%. (2 marks — 1 for proportional reasoning, 1 for correct percentage.)

---

## Key Takeaways

1. **Velocity selector:** $v = E/B$. Selects by speed only, independent of $q$ and $m$.

2. **Mass spectrometer:** $r = mv/(qB)$. Heavier ions → larger radius. Used to identify isotopes and measure atomic masses.

3. **Cyclotron:** Frequency $f = qB/(2\pi m)$ is constant (non-relativistic). Maximum energy: $KE_{\text{max}} = q^2B^2R^2/(2m)$. Limited by relativity at high speeds — synchrotrons solve this.

4. **All three devices** exploit the interplay of electric and magnetic forces on moving charges.
