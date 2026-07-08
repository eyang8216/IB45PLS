# Lesson 56: Induction 3 — AC Generators, Transformers, and Power Transmission

## What You'll Learn

In Lessons 54 and 55, you learned that changing magnetic flux through a coil induces an emf, and that induced emf opposes the change that caused it. You learned about moving wires in magnetic fields, about Faraday's law, and about Lenz's law. But everything we studied used *steady* (DC) currents or *one-time* changes.

In this lesson, you'll learn how engineers exploit induction to generate the alternating current that powers every home, school, and factory on Earth. You'll learn how a spinning coil in a magnetic field produces a voltage that smoothly rises and falls, why the voltage in your wall outlet is described by something called "root mean square," how transformers can step voltage up or down with almost no energy loss, and why we transmit power at extremely high voltages across long distances.

These aren't just abstract concepts — every time you charge your phone, turn on a light, or watch TV, you're using technology built on the principles in this lesson.

---

## 1. AC Generators (Alternators)

### Why This Matters

Direct current has a problem: it's hard to change its voltage. A battery gives you a fixed voltage, and if you need a different voltage, you need a different battery or complex electronics. But most devices need different voltages — your phone charger needs 5 V, your laptop needs 19 V, your refrigerator needs 120 V or 240 V. Power plants generate at thousands of volts, and transmission lines carry hundreds of thousands of volts.

Alternating current (AC) solves this problem because AC voltage can be easily transformed up or down using a device with no moving parts: the transformer. But to use transformers, you first need AC. That's where the AC generator comes in.

### The Key Ideas

**What is an AC generator?** An AC generator (also called an alternator) is a device that converts mechanical energy — usually from a spinning turbine turned by steam, falling water, or wind — into electrical energy in the form of alternating current. It works on exactly the same principle you learned in Lesson 54: a changing magnetic flux through a coil induces an emf.

**How it works: the rotating coil.** Imagine a rectangular coil of wire with N turns, each of area A, rotating at a steady angular speed ω (omega) inside a uniform magnetic field B. The coil is mounted on an axle, and as it spins, the angle between the magnetic field and the normal to the coil's surface changes continuously.

At any instant, the magnetic flux through one turn of the coil is:

**Φ = B A cos(θ)**

where θ is the angle between the magnetic field direction and the normal (perpendicular) to the coil's surface. If the coil rotates at constant angular speed ω, then θ = ωt (starting from θ = 0 at t = 0). So:

**Φ(t) = B A cos(ωt)**

**From flux to emf.** Faraday's law tells us the induced emf is the negative rate of change of flux times the number of turns:

**ε(t) = −N dΦ/dt**

Taking the derivative of B A cos(ωt) with respect to time gives:

**ε(t) = −N B A (−ω sin(ωt)) = N B A ω sin(ωt)**

This is the fundamental equation of an AC generator. The induced emf varies sinusoidally with time. Let's define the **peak emf** ε₀:

**ε₀ = N B A ω**

Then: **ε(t) = ε₀ sin(ωt)**

**What this means physically.** When the coil's surface is perpendicular to the magnetic field (θ = 0, or θ = 180°), the flux is at its maximum but not changing — so the induced emf is zero. When the coil's surface is parallel to the field (θ = 90° or 270°), the flux is zero but changing at its fastest rate — so the induced emf is at its peak (±ε₀). This is a crucial point: **the emf depends on the RATE OF CHANGE of flux, not the amount of flux.**

**Frequency.** If the coil makes f complete revolutions per second, then ω = 2πf. In North America, the grid frequency is 60 Hz; in most of the rest of the world, it's 50 Hz. So the voltage at your wall outlet goes through a complete cycle 50 or 60 times each second.

### Common Misconceptions

**"The emf is maximum when flux is maximum."** No. The emf is maximum when the RATE OF CHANGE of flux is maximum. Flux is maximum when the coil is perpendicular to the field, but at that instant, the flux is momentarily not changing (the coil is moving parallel to the field lines), so the emf is zero. Flux is zero when the coil is parallel to the field, but it's changing most rapidly at that instant, so emf is maximum.

**"The coil must be connected to a battery to spin."** No. In a generator, mechanical energy spins the coil. The emf is induced by the changing flux. In a motor, electrical energy spins the coil. A generator and a motor are essentially the same device run in opposite directions. Many power plants use the same machine as both a generator (when producing electricity) and a motor (when starting up).

### Important Variations

**Slip rings vs. split rings.** An AC generator uses **slip rings** — two continuous metal rings, each connected to one end of the coil, with brushes sliding against them. Because each ring stays connected to the same end of the coil throughout the rotation, the output voltage alternates polarity. If you used a split-ring commutator instead (as in a DC motor), the output would be rectified — the negative half-cycles would be flipped to positive, giving a pulsating DC output. This is how a DC generator works.

**Practical generators.** Real power plant generators don't spin a coil inside a permanent magnet. Instead, they spin an electromagnet (the rotor) inside stationary coils (the stator). The rotor's magnetic field is produced by a DC current fed through slip rings. This design avoids passing the large output current through sliding contacts. The stator coils, which are stationary, can be directly connected to the external circuit.

---

## 2. Root Mean Square (RMS) Values

### Why This Matters

If an AC voltage is constantly changing, what number do you use to describe it? You can't say "120 volts" if the voltage goes from +170 V to −170 V. Which value is the "real" one? The answer uses a clever averaging technique that tells you the DC-equivalent voltage — the voltage that would deliver the same power to a resistor.

### The Key Ideas

**The problem with simple averaging.** The average of sin(ωt) over a complete cycle is zero — the positive half cancels the negative half. So the "average voltage" of AC is zero, which is clearly not useful for describing what the voltage "feels like" to a light bulb.

**The solution: root mean square.** Instead of averaging the voltage directly, we:
1. **Square** the voltage at every instant (making everything positive)
2. Take the **mean** (average) of those squared values over a cycle
3. Take the square **root** of that mean

For a sinusoidal voltage v(t) = V₀ sin(ωt):

- v²(t) = V₀² sin²(ωt)
- The average of sin²(ωt) over a cycle is 1/2
- So the mean of v² is V₀²/2
- Taking the square root: **V_rms = V₀ / √2**

Similarly for current: **I_rms = I₀ / √2**

**Why RMS matters: power.** The average power dissipated in a resistor R by an AC current is:

**P_avg = I_rms² R = V_rms² / R = I_rms V_rms**

This is exactly the same formula as for DC, using RMS values. An AC voltage with V_rms = 120 V delivers the same average power to a resistor as a 120 V DC source.

**Numerical example.** The wall outlet in North America is nominally 120 V RMS. The peak voltage is 120 × √2 ≈ 170 V. In countries with 230 V RMS, the peak is 230 × √2 ≈ 325 V. The peak-to-peak voltage is twice the peak: about 340 V in North America, 650 V elsewhere.

### Common Misconceptions

**"RMS means average."** No. The average of sin(ωt) is zero. The average of |sin(ωt)| (the absolute value) is 2V₀/π ≈ 0.637 V₀. The RMS value is V₀/√2 ≈ 0.707 V₀. These are three different numbers.

**"V_rms is the voltage you measure with a voltmeter."** For AC, yes — most voltmeters are designed to display RMS values. But they assume the waveform is a pure sine wave. For non-sinusoidal waveforms (like the output of a dimmer switch), a "true RMS" meter is needed. Cheap meters that assume a sine wave will give wrong readings for non-sinusoidal signals.

---

## 3. Transformers

### Why This Matters

Transformers are the reason we use AC for power distribution. They let us change voltage levels with remarkable efficiency (typically 95-99%) using no moving parts. Without transformers, the electrical grid as we know it would not exist. A transformer can take 11,000 V from a generator, step it up to 400,000 V for long-distance transmission, then step it down to 240 V for your home.

### The Key Ideas

**What is a transformer?** A transformer consists of two coils of wire (the primary and secondary) wound around a common iron core. When an alternating current flows through the primary coil, it creates a changing magnetic flux in the iron core. This changing flux passes through the secondary coil and, by Faraday's law, induces an emf across it.

**Why the iron core?** The iron core serves to "guide" the magnetic flux. Without it, the flux produced by the primary coil would spread out through the air, and only a tiny fraction would reach the secondary coil. Iron has a magnetic permeability thousands of times greater than air, so it concentrates the flux and channels almost all of it through both coils. This is essential for high efficiency.

**The ideal transformer equations.** In an ideal transformer (no energy losses):
- The flux through each turn of both coils is the same (because the same core links them).
- The rate of change of flux is the same for both.
- By Faraday's law, the emf per turn is the same for both coils.

So for the primary coil (N_p turns): ε_p = −N_p dΦ/dt
For the secondary coil (N_s turns): ε_s = −N_s dΦ/dt

Dividing: **ε_s / ε_p = N_s / N_p**

In terms of voltages: **V_s / V_p = N_s / N_p**

This is the **turns ratio equation**. The voltage ratio equals the turns ratio.

**Step-up transformer:** N_s > N_p, so V_s > V_p
**Step-down transformer:** N_s < N_p, so V_s < V_p

**Current in an ideal transformer.** If the transformer is 100% efficient (no energy lost), then the power into the primary equals the power out of the secondary:

**P_p = P_s**
**V_p I_p = V_s I_s**

Rearranging: **I_s / I_p = V_p / V_s = N_p / N_s**

So if a transformer steps UP the voltage by a factor of 10, it steps DOWN the current by a factor of 10. The product V × I stays constant (for an ideal transformer).

**A crucial point about current.** The secondary current I_s is determined by the LOAD connected to the secondary. If nothing is connected (open circuit), I_s = 0, and I_p is tiny (just enough to magnetize the core). When you connect a load, I_s flows, and this creates its own flux that OPPOSES the primary flux (by Lenz's law). The primary then draws more current to maintain the flux. So the primary current is determined by the secondary current, not the other way around.

### Common Misconceptions

**"A step-up transformer creates energy."** No. When voltage is stepped up, current is stepped down by the same factor. The power (V × I) stays the same (ignoring losses). Energy is conserved.

**"Transformers work with DC."** No. A transformer requires a CHANGING magnetic flux. Direct current produces a steady magnetic field, which does not induce any emf in the secondary after the initial turn-on transient. If you connect DC to a transformer primary, it acts like a short circuit (just the resistance of the copper wire) and will likely burn out.

**"The turns ratio determines the current ratio regardless of load."** No. The equation I_s/I_p = N_p/N_s is only true for an ideal transformer under load. If the secondary is open-circuited, I_s = 0, and I_p is very small — the turns ratio equation for current doesn't hold.

### Real Transformer Losses

Real transformers are not 100% efficient. The main losses are:

1. **Resistive (copper) losses:** The coils have resistance, so I²R power is dissipated as heat in the windings.

2. **Eddy current losses:** The changing magnetic flux also induces currents in the iron core itself. These circulating currents (eddy currents) waste energy as heat. They're reduced by making the core from thin, laminated sheets insulated from each other, which restricts the paths for eddy currents.

3. **Hysteresis losses:** The iron core's magnetization must be reversed 100 or 120 times per second (twice per cycle). Each reversal requires energy, which appears as heat. Using "soft" magnetic materials (easy to magnetize and demagnetize) minimizes this.

4. **Flux leakage:** Not all the flux from the primary reaches the secondary. Some "leaks" out into the surrounding air.

---

## 4. Power Transmission

### Why This Matters

Power plants are often hundreds of kilometers from the cities and factories they serve. Transmitting electrical power over long distances involves a fundamental trade-off, and understanding it explains why you see high-voltage transmission lines crisscrossing every country.

### The Key Ideas

**The fundamental problem: resistive losses.** Transmission lines have resistance R. When current I flows through them, power is lost as heat:

**P_lost = I² R**

This power is wasted — it heats the air, not your home. To minimize losses, we want to minimize either I or R.

**Why we can't just reduce R.** Making the resistance low enough would require impractically thick (and heavy, and expensive) copper or aluminum cables. The resistance of a wire is R = ρL/A. For a 100 km line, even a very thick cable has significant resistance.

**The solution: high voltage.** Instead of reducing R, we reduce I. Since the power being transmitted is P = V I, we can transmit the same power with lower current if we use higher voltage:

**P = V I  →  I = P / V**

If we double the voltage, we halve the current for the same power, and the losses (∝ I²) drop to one-quarter.

This is why power is transmitted at extremely high voltages: 110 kV, 220 kV, 400 kV, even 765 kV in some systems. At the power plant, a step-up transformer raises the generator voltage (typically 11-25 kV) to transmission voltage. Near the point of use, substations with step-down transformers reduce the voltage in stages: transmission voltage → subtransmission (33-66 kV) → distribution (11 kV) → household (120/240 V or 230/400 V).

**Numerical example.** Suppose a power plant generates 100 MW at 25 kV. The current would be I = 100×10⁶ / 25×10³ = 4000 A. If the transmission line has a resistance of 5 Ω, the losses would be I²R = (4000)² × 5 = 80 MW — that's 80% of the power generated, lost as heat!

If the voltage is stepped up to 400 kV for transmission, the current drops to I = 100×10⁶ / 400×10³ = 250 A. Now the losses are (250)² × 5 = 0.3125 MW, or 0.31% of the generated power. This is why we use high-voltage transmission.

**DC vs. AC transmission.** For very long distances (over about 600 km for overhead lines, or 50 km for underwater/underground cables), high-voltage DC (HVDC) transmission becomes more economical than AC. DC has no capacitive or inductive losses (which become significant for long AC lines), and it requires fewer conductors. Modern power electronics make AC-DC-AC conversion practical at both ends.

### Common Misconceptions

**"High voltage is dangerous, so why use it?"** High voltage is dangerous for people, which is why transmission lines are placed on tall towers far from the ground and insulated from their supports. The danger comes from current passing through your body, and the high voltage is safely contained within insulated cables.

**"Transformers waste the power they save."** A well-designed transformer is 95-99% efficient. The small loss in the transformer is vastly outweighed by the reduction in transmission losses achieved by raising the voltage.

---

## Worked Examples

### Example 1: AC Generator Output

A simple AC generator has a coil of 200 turns, each with an area of 0.050 m², rotating at 3000 revolutions per minute in a magnetic field of 0.20 T. Calculate the peak emf and the RMS emf.

**Approach:** Convert rpm to angular frequency. Use ε₀ = N B A ω. Then V_rms = ε₀/√2.

**Step 1:** Angular frequency.
f = 3000 / 60 = 50 Hz
ω = 2π × 50 = 314.2 rad/s

**Step 2:** Peak emf.
ε₀ = N B A ω = 200 × 0.20 × 0.050 × 314.2 = 628.3 V

**Step 3:** RMS emf.
ε_rms = 628.3 / √2 = 628.3 / 1.414 = 444.3 V

**Why this makes sense:** A generator with a large number of turns, a decent field, and a fast rotation produces hundreds of volts, which is a typical order of magnitude for power station generators before step-up.

---

### Example 2: Transformer Design

An ideal transformer is needed to operate a 12.0 V, 60.0 W lamp from a 240 V mains supply. The primary coil has 2000 turns. Calculate: (a) the number of turns needed on the secondary, (b) the current in the primary coil.

**Approach:** Use the turns ratio equation to find N_s. For current, find I_s from the lamp power, then use the ideal transformer power equation.

**Step 1:** Turns ratio.
N_s / N_p = V_s / V_p = 12.0 / 240 = 1/20
N_s = 2000 × (1/20) = 100 turns

**Step 2:** Secondary current.
P = V_s × I_s → I_s = 60.0 / 12.0 = 5.00 A

**Step 3:** Primary current.
V_p I_p = V_s I_s → I_p = (V_s I_s) / V_p = 60.0 / 240 = 0.250 A
Alternatively: I_p = I_s × (N_s/N_p) = 5.00 × (1/20) = 0.250 A

**Why this makes sense:** The transformer steps down voltage 20:1, so it steps up current 1:20. Power is conserved: 240 V × 0.25 A = 60 W = 12 V × 5 A.

---

### Example 3: RMS Current and Power

An AC voltage with RMS value 230 V is applied to a resistor of 50.0 Ω. Calculate: (a) the RMS current, (b) the peak current, (c) the average power dissipated.

**Approach:** Ohm's law works with RMS values. Then convert to peak. Power uses RMS values.

**Step 1:** RMS current.
I_rms = V_rms / R = 230 / 50.0 = 4.60 A

**Step 2:** Peak current.
I₀ = I_rms × √2 = 4.60 × 1.414 = 6.51 A

**Step 3:** Average power.
P_avg = I_rms² R = (4.60)² × 50.0 = 1058 W ≈ 1.06 kW
Or: P_avg = V_rms × I_rms = 230 × 4.60 = 1058 W

**Why this makes sense:** The peak current is about 1.4 times the RMS, which is the familiar √2 relationship. The power is what you'd expect for a 1 kW heating element.

---

### Example 4: Generator at Different Orientations

The generator from Example 1 has a peak emf of 628 V. Calculate the instantaneous emf at times corresponding to coil angles of: (a) 0°, (b) 45°, (c) 90°, (d) 180°.

**Approach:** Use ε(t) = ε₀ sin(θ), where θ is the angle from the perpendicular position.

**Step 1:** At 0°: ε = 628 × sin(0°) = 0 V. (Coil perpendicular to field; flux maximum but not changing.)

**Step 2:** At 45°: ε = 628 × sin(45°) = 628 × 0.707 = 444 V.

**Step 3:** At 90°: ε = 628 × sin(90°) = 628 V. (Coil parallel to field; flux zero but changing fastest.)

**Step 4:** At 180°: ε = 628 × sin(180°) = 0 V. (Coil perpendicular again, opposite orientation.)

**Why this makes sense:** The emf is zero when the coil is perpendicular to the field at both 0° and 180°, and peaks at 90°. This illustrates that emf depends on the RATE OF CHANGE of flux.

---

### Example 5: Transmission Line Losses

A power station generates 50.0 MW at 22.0 kV. The transmission line has a total resistance of 8.00 Ω. Compare the power losses when transmitting at: (a) the generator voltage of 22.0 kV, (b) 220 kV after stepping up the voltage.

**Approach:** Calculate current for each case. Then use P_lost = I²R.

**Step 1:** Current at 22.0 kV.
I = P / V = 50.0 × 10⁶ / 22.0 × 10³ = 2273 A
P_lost = I²R = (2273)² × 8.00 = 41.3 × 10⁶ W = 41.3 MW

This is 82.7% of the generated power — completely unacceptable.

**Step 2:** Current at 220 kV.
I = P / V = 50.0 × 10⁶ / 220 × 10³ = 227 A
P_lost = I²R = (227)² × 8.00 = 0.413 × 10⁶ W = 0.413 MW

This is 0.83% of the generated power — excellent.

**Why this makes sense:** Increasing voltage by a factor of 10 decreases current by a factor of 10, and losses (∝ I²) decrease by a factor of 100. This dramatic reduction is why we use high-voltage transmission.

---

## Practice Problems

### Problem 1
An AC generator has a rectangular coil of 500 turns, each measuring 0.12 m by 0.080 m, rotating at 1500 rpm in a uniform magnetic field of 0.35 T. (a) Calculate the peak emf generated. (b) Calculate the RMS emf. (c) What is the frequency of the AC output?

### Problem 2
An ideal transformer has 800 turns on the primary coil and 50 turns on the secondary. The primary is connected to a 120 V (RMS) AC supply. (a) Calculate the secondary voltage. (b) If a 24.0 W device is connected to the secondary, calculate the current in the secondary and in the primary. (c) Explain why the primary current is different from the secondary current.

### Problem 3
A 240 V (RMS) AC supply is connected to a 2.00 kW electric heater. (a) Calculate the RMS current drawn by the heater. (b) Calculate the peak current. (c) Calculate the resistance of the heater element.

### Problem 4
A power station generates 200 MW at 25.0 kV. The power is to be transmitted 150 km through cables with a total resistance of 6.50 Ω. (a) Calculate the power loss if the power were transmitted at the generator voltage. Express the loss as a percentage. (b) A step-up transformer raises the voltage to 500 kV for transmission. Calculate the new power loss and its percentage. (c) Explain physically why high-voltage transmission reduces losses.

### Problem 5
A transformer has a primary of 1200 turns and a secondary of 80 turns. The primary is connected to a 120 V (RMS), 60 Hz supply. (a) Is this a step-up or step-down transformer? (b) Calculate the voltage across the secondary when no load is connected. (c) When a resistive load is connected, the secondary current is 3.00 A (RMS). Assuming 100% efficiency, calculate the primary current. (d) Would the primary current be the same if the 120 V supply were DC instead of AC? Explain.

### Problem 6 (IB Exam Style)
A simple AC generator consists of a flat rectangular coil of 150 turns, each of area 0.040 m², rotating at a constant frequency f in a uniform magnetic field of strength 0.25 T. The output is connected to an oscilloscope, which displays a sinusoidal trace.

(a) The peak-to-peak voltage on the oscilloscope is 340 V. Calculate the peak emf of the generator. [1 mark]

(b) Show that the RMS emf of the generator is approximately 120 V. [1 mark]

(c) The frequency of the displayed signal is 50.0 Hz. Calculate the angular frequency of the coil's rotation. [1 mark]

(d) Determine the frequency of rotation of the coil in revolutions per minute. [1 mark]

(e) Using ε₀ = NBAω, determine the number of turns on the coil. A different coil with the stated 150 turns was actually used — comment on whether your calculation confirms this. [3 marks]

(f) The coil is now rotated at half its original frequency. State and explain what happens to: (i) the peak emf, (ii) the RMS emf, (iii) the period of the AC output. [3 marks]

---

## Answers

### Answer 1
(a) Area A = 0.12 × 0.080 = 0.0096 m².
f = 1500/60 = 25 Hz. ω = 2π × 25 = 157.1 rad/s.
ε₀ = NBAω = 500 × 0.35 × 0.0096 × 157.1 = 263.9 V ≈ 264 V.

(b) ε_rms = 264 / √2 = 186.7 V ≈ 187 V.

(c) Frequency = 25 Hz. (One complete electrical cycle per revolution for a 2-pole generator.)

### Answer 2
(a) V_s / V_p = N_s / N_p → V_s = 120 × (50/800) = 7.50 V.

(b) P = V_s I_s → I_s = 24.0 / 7.50 = 3.20 A.
I_p = P / V_p = 24.0 / 120 = 0.200 A.
Or: I_p = I_s × (N_s/N_p) = 3.20 × (50/800) = 0.200 A.

(c) The primary current is smaller because the transformer steps down voltage (by a factor of 800/50 = 16) and therefore steps up current by the same factor. Power is conserved: V_p I_p = V_s I_s. Since V_p > V_s, we must have I_p < I_s for the same power.

### Answer 3
(a) I_rms = P / V_rms = 2000 / 240 = 8.33 A.

(b) I₀ = I_rms × √2 = 8.33 × 1.414 = 11.8 A.

(c) R = V_rms / I_rms = 240 / 8.33 = 28.8 Ω.
Alternatively: R = V_rms² / P = 240² / 2000 = 28.8 Ω.

### Answer 4
(a) I = 200 × 10⁶ / 25.0 × 10³ = 8000 A.
P_lost = I²R = (8000)² × 6.50 = 4.16 × 10⁸ W = 416 MW.
Percentage = (416/200) × 100% = 208%. 
This is impossible — the losses exceed the generated power, meaning the voltage would collapse long before delivering any useful power. This illustrates why we MUST step up voltage for transmission.

(b) I = 200 × 10⁶ / 500 × 10³ = 400 A.
P_lost = (400)² × 6.50 = 1.04 × 10⁶ W = 1.04 MW.
Percentage = (1.04/200) × 100% = 0.52%.

(c) For a fixed transmitted power P = VI, increasing V decreases I proportionally. Since resistive power loss is P_lost = I²R, reducing I by a factor of n reduces losses by n². At 500 kV, current is 20× smaller than at 25 kV, so losses are 400× smaller. The energy saved far outweighs the small losses in the step-up and step-down transformers.

### Answer 5
(a) Step-down transformer because N_s < N_p (80 vs 1200).

(b) V_s = V_p × (N_s/N_p) = 120 × (80/1200) = 120 × (1/15) = 8.00 V.

(c) I_s = 3.00 A. Power: P = V_s I_s = 8.00 × 3.00 = 24.0 W.
I_p = P / V_p = 24.0 / 120 = 0.200 A.
Or: I_p = I_s × (N_s/N_p) = 3.00 × (1/15) = 0.200 A.

(d) No. With DC, there is no changing magnetic flux (after the initial transient when the circuit is first connected). Without changing flux, Faraday's law gives zero induced emf in the secondary. The primary would draw a very large current limited only by the resistance of the copper wire, likely causing the transformer to overheat and burn out. Transformers REQUIRE alternating current.

### Answer 6
(a) Peak emf = peak-to-peak / 2 = 340/2 = 170 V.

(b) ε_rms = ε₀/√2 = 170/1.414 = 120.2 V ≈ 120 V.

(c) ω = 2πf = 2π × 50.0 = 314.2 rad/s ≈ 314 rad/s.

(d) f = 50.0 Hz = 50.0 revolutions per second = 50.0 × 60 = 3000 rpm.

(e) ε₀ = NBAω → N = ε₀/(BAω) = 170 / (0.25 × 0.040 × 314.2) = 170 / 3.142 = 54.1 turns.
This does NOT confirm 150 turns — it gives about 54 turns. Either the peak-to-peak voltage was read incorrectly, the area was different, or the magnetic field was stronger than stated. The actual generator with 150 turns would produce ε₀ = 150 × 0.25 × 0.040 × 314.2 = 471 V, giving a peak-to-peak of 942 V, not 340 V.

(f) (i) The peak emf is halved because ε₀ = NBAω and ω is proportional to f.
(ii) The RMS emf is also halved, since ε_rms = ε₀/√2.
(iii) The period doubles because T = 1/f. When frequency is halved, the time for one complete cycle doubles.

**Common pitfall:** Some students think reducing frequency increases emf (confusing it with ω somehow being independent). No — the emf is directly proportional to ω, which is proportional to f.

---

## Key Takeaways

1. An AC generator produces a sinusoidal emf ε(t) = NBAω sin(ωt) by rotating a coil in a magnetic field. The peak emf is ε₀ = NBAω.

2. The emf is maximum when the flux is zero (coil parallel to field) and zero when the flux is maximum (coil perpendicular to field). Emf depends on the RATE OF CHANGE of flux.

3. RMS values for sinusoidal AC: V_rms = V₀/√2, I_rms = I₀/√2. These give the DC-equivalent value that produces the same average power in a resistor.

4. An ideal transformer satisfies V_s/V_p = N_s/N_p and V_p I_p = V_s I_s (power conservation). Transformers require AC — they do not work with DC.

5. High-voltage transmission minimizes I²R losses. For fixed power, doubling voltage halves current and cuts losses to ¼.

6. Real transformers have losses from coil resistance, eddy currents in the core, hysteresis, and flux leakage. Laminated cores reduce eddy currents; soft magnetic materials reduce hysteresis.
