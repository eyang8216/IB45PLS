# Lesson 54: Induction I — Magnetic Flux and Faraday's Law

## What You'll Learn
- Define magnetic flux $\Phi = BA\cos\theta$ and understand what it physically represents
- State Faraday's Law and use it to calculate induced EMF
- Apply Lenz's Law to determine the direction of induced current
- Identify the three ways to change magnetic flux: change B, change A, change angle

---

## 1. Magnetic Flux — Counting Field Lines

### 1.1 What Flux Means

Imagine a loop of wire placed in a magnetic field. How much of the field passes through the loop? That quantity is **magnetic flux** $\Phi$. Physically, you can think of flux as counting the number of magnetic field lines that pass through the loop's area.

$$\Phi = BA\cos\theta$$

where:
- $B$ is the magnetic field strength (T)
- $A$ is the area of the loop (m²)
- $\theta$ is the angle between the magnetic field direction and the **normal** (perpendicular) to the loop's surface

The unit of flux is the **weber** (Wb): $1\text{ Wb} = 1\text{ T}\cdot\text{m}^2$.

### 1.2 Understanding the Cosine

When the field is perpendicular to the loop ($\theta = 0^\circ$), $\cos 0^\circ = 1$ and $\Phi = BA$ — maximum flux. The field passes straight through.

When the field is parallel to the loop ($\theta = 90^\circ$), $\cos 90^\circ = 0$ and $\Phi = 0$ — no field lines pass through. They skim along the surface.

For a coil of $N$ turns, the **flux linkage** is $N\Phi$.

---

## 2. Faraday's Law — Changing Flux Creates EMF

### 2.1 The Discovery That Changed the World

In 1831, Michael Faraday discovered that a changing magnetic flux through a coil induces an electromotive force (EMF) in the coil. This single discovery is the basis of every electrical generator on Earth, every transformer in the power grid, and every wireless charger.

$$\varepsilon = -N\frac{\Delta\Phi}{\Delta t}$$

- $\varepsilon$ is the induced EMF (V)
- $N$ is the number of turns
- $\Delta\Phi/\Delta t$ is the rate of change of flux (Wb s⁻¹)

### 2.2 Three Ways to Change Flux

Since $\Phi = BA\cos\theta$, there are exactly three ways to change it:

1. **Change $B$:** Move a magnet toward or away from a coil. Vary the current in an electromagnet.
2. **Change $A$:** Deform the loop, or have a sliding rod change the enclosed area.
3. **Change $\theta$:** Rotate the coil in a magnetic field — this is how AC generators work.

Any one of these produces an induced EMF. The key is CHANGE — a constant flux produces zero EMF, no matter how large.

---

## 3. Lenz's Law — The Direction of Opposition

### 3.1 The Negative Sign Has Meaning

The minus sign in Faraday's Law is Lenz's Law: **the induced current flows in a direction that opposes the change in flux that produced it.**

This is not an arbitrary rule — it is required by conservation of energy. If the induced current REINFORCED the change, you would get a runaway effect producing infinite energy. Lenz's Law ensures you always have to do work to generate electrical energy.

### 3.2 Applying Lenz's Law

1. Determine whether flux is **increasing** or **decreasing** through the loop
2. The induced current creates its own magnetic field that **opposes** this change
3. Use the right-hand grip rule to find the current direction

**Example:** A bar magnet's N-pole moves TOWARD a coil. Flux through the coil increases (more field lines). The coil "wants" to oppose this increase, so it creates a magnetic field pointing OPPOSITE to the magnet's field. This requires current in a specific direction — the end of the coil facing the magnet becomes a N-pole, repelling the approaching magnet. You feel this as resistance when you push a magnet into a coil.

---

## 4. Motional EMF — A Moving Conductor in a Field

### 4.1 The Simplest Case

A conducting rod of length $L$ moves at speed $v$ perpendicular to a uniform magnetic field $B$. The area swept out per unit time is $Lv$, so the flux change per second is $B \times Lv$:

$$\varepsilon = BLv$$

This is called **motional EMF**. It's a special case of Faraday's Law — the area of the loop is changing because the rod is moving.

---

## Worked Examples

### Worked Example 54.1 — Flux Calculation

**Problem:** A square coil of side $0.10\text{ m}$ with $50$ turns sits in a $0.40\text{ T}$ field perpendicular to its plane. Find the flux linkage.

**Solution:**
$A = (0.10)^2 = 0.010\text{ m}^2$. $\Phi = BA = (0.40)(0.010) = 0.0040\text{ Wb}$. Flux linkage = $N\Phi = 50 \times 0.0040 = 0.20\text{ Wb}$.

---

### Worked Example 54.2 — Faraday's Law

**Problem:** A 100-turn coil experiences flux changing from $0.30\text{ Wb}$ to $0.10\text{ Wb}$ in $0.050\text{ s}$. Find the average induced EMF.

**Solution:**
$\Delta\Phi = 0.10 - 0.30 = -0.20\text{ Wb}$. $\varepsilon = -N\Delta\Phi/\Delta t = -100(-0.20)/0.050 = 400\text{ V}$.

---

### Worked Example 54.3 — Motional EMF

**Problem:** A $0.50\text{ m}$ rod moves at $8.0\text{ m s}^{-1}$ perpendicular to a $0.25\text{ T}$ field. Find the induced EMF. If the rod slides on rails connected by a $4.0\text{ Ω}$ resistor, find the current.

**Solution:**
$\varepsilon = BLv = (0.25)(0.50)(8.0) = 1.0\text{ V}$. $I = \varepsilon/R = 1.0/4.0 = 0.25\text{ A}$.

---

### Worked Example 54.4 — IB-Style Lenz's Law

**Problem:** A magnet's S-pole is pulled AWAY from a coil. Determine the direction of induced current.

**Solution:**
The S-pole pulling away means flux directed toward the coil is DECREASING. To oppose this decrease, the coil creates flux in the SAME direction as the magnet (trying to maintain the flux). The coil's end facing the magnet becomes a S-pole, attracting — you must do work to pull against this attraction.

---

## Practice Problems

### Problem 1
A 200-turn circular coil of radius $0.030\text{ m}$ sits in a $0.60\text{ T}$ field perpendicular to its plane. The field is reduced to zero in $0.12\text{ s}$. Find the average induced EMF.

### Problem 2
A $0.40\text{ m}$ rod moves at $6.0\text{ m s}^{-1}$ through a $0.35\text{ T}$ field on frictionless rails connected by a $7.0\text{ Ω}$ resistor. Find: (a) EMF, (b) current, (c) force required to maintain constant speed.

### Problem 3
A magnet is pushed into a coil and then held stationary inside it. Describe the induced EMF during: (a) the pushing phase, and (b) the holding phase. Explain using Faraday's Law.

### Problem 4
A coil is rotated from $\theta = 0^\circ$ (field perpendicular) to $\theta = 90^\circ$ (field parallel) in $0.020\text{ s}$. The coil has $100$ turns, area $0.0050\text{ m}^2$, and $B = 0.30\text{ T}$. Find the average EMF.

### Problem 5 — IB-Style
A student drops a bar magnet through a horizontal coil connected to a data logger. The EMF-vs-time graph shows a positive peak followed by a negative peak.

(a) Explain why the two peaks have opposite signs. (2 marks)
(b) The second peak has a larger magnitude than the first. Explain this observation. (2 marks)
(c) State how the area under each peak relates to the flux change $N\Delta\Phi$. (2 marks)
(d) The student repeats the experiment with a stronger magnet. Describe and explain two changes in the EMF-time graph. (2 marks)

---

## Answers

### Answer 1
$A = \pi(0.030)^2 = 2.83\times 10^{-3}\text{ m}^2$. $\Phi_{\text{initial}} = (0.60)(2.83\times 10^{-3}) = 1.70\times 10^{-3}\text{ Wb}$. $\varepsilon = 200(1.70\times 10^{-3})/0.12 = 2.83\text{ V}$.

### Answer 2
**(a)** $\varepsilon = (0.35)(0.40)(6.0) = 0.84\text{ V}$. **(b)** $I = 0.84/7.0 = 0.12\text{ A}$. **(c)** $F = BIL = (0.35)(0.12)(0.40) = 0.017\text{ N}$ opposing motion — you must push with $0.017\text{ N}$.

### Answer 3
**(a)** EMF is non-zero — flux is changing. **(b)** EMF is zero — flux is constant (magnet not moving), so $\Delta\Phi/\Delta t = 0$. Faraday's Law: EMF only when flux CHANGES.

### Answer 4
$\Phi_{\text{initial}} = (0.30)(0.0050) = 1.50\times 10^{-3}\text{ Wb}$. $\Phi_{\text{final}} = (0.30)(0.0050)\cos 90^\circ = 0$. $\varepsilon = 100(1.50\times 10^{-3})/0.020 = 7.5\text{ V}$.

### Answer 5 — IB-Style
**(a)** (2 marks) As the magnet enters, flux through the coil increases → EMF in one direction (say positive). As it leaves, flux decreases → EMF in opposite direction (negative). Lenz's Law gives opposite induced EMF for increasing vs. decreasing flux.

**(b)** (2 marks) The magnet accelerates due to gravity, so it's moving faster when it exits the coil than when it entered. Greater speed → faster rate of flux change → larger induced EMF ($\varepsilon \propto \Delta\Phi/\Delta t \propto v$).

**(c)** (2 marks) The area under each EMF-time peak equals the total flux change $N\Delta\Phi$ for that portion of the motion ($\int \varepsilon\,dt = N\Delta\Phi$). This is independent of the speed — faster motion gives taller but narrower peaks with the same area.

**(d)** (2 marks) Stronger magnet → larger $B$ → larger flux AND faster flux change → both peaks taller. Same transit times (speed unchanged by magnet strength) but larger EMF throughout. (1 mark for taller peaks, 1 mark for linking to $B$.)

---

## Key Takeaways

1. **Flux:** $\Phi = BA\cos\theta$. Measures magnetic field passing through an area.

2. **Faraday's Law:** $\varepsilon = -N\Delta\Phi/\Delta t$. EMF induced whenever flux CHANGES — not when it's constant.

3. **Three ways to change flux:** Change B, change A, change angle.

4. **Lenz's Law:** Induced current opposes the flux change. The minus sign matters — it's energy conservation.

5. **Motional EMF:** $\varepsilon = BLv$ for a rod cutting field lines.
