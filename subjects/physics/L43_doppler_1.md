# Lesson 43: The Doppler Effect I — Sound Waves

## What You'll Learn
- What the Doppler effect is and why it happens
- The Doppler equation for sound: what each symbol means
- The sign convention — when to use + and when to use −
- How moving source and moving observer differ physically
- Sonic booms, shock waves, and the Mach number
- Applications to police radar, astronomy, and medical ultrasound

---

## 1. What Is the Doppler Effect?

### The Basic Observation

Imagine you are standing on a sidewalk. An ambulance drives past you with its siren on. As it approaches, the siren sounds **higher in pitch**. The moment it passes, the pitch **drops** and sounds lower as it drives away. The siren itself never changes — the ambulance driver hears the same steady note the whole time.

This is the **Doppler effect**: the change in observed frequency when a wave source and an observer move relative to each other.

The effect is named after Christian Doppler, an Austrian physicist who first described it mathematically in 1842.

### Why It Happens — The Intuition

A sound wave is a series of compressions (high pressure regions) travelling through the air. The **frequency** is the number of compressions that reach your ear per second. The **wavelength** is the distance between successive compressions.

- **Stationary source:** The compressions spread out evenly in all directions. The distance between compressions is the same everywhere. An observer at any position hears the same frequency that the source emits.

- **Source moving toward you:** Each time the source emits a new compression, it has moved closer to you. The compressions are now closer together — the wavelength is **shorter**. Since the wave speed in air is fixed (at a given temperature), a shorter wavelength means a **higher frequency**. You hear a higher pitch.

- **Source moving away from you:** The source moves away between emitting each compression. The compressions spread out — the wavelength is **longer**. This means a **lower frequency**. You hear a lower pitch.

**The key physical idea:** The wave speed in the medium does NOT change. The wavelength changes because the source moves between emitting successive wavefronts. Since v = fλ and v is constant, a change in λ forces a change in f.

### Common Misconception #1

> "The sound waves travel faster when the source moves toward me."

No. The speed of sound in air is determined by the properties of the air (temperature, pressure), not by the motion of the source. The waves travel at the same speed regardless. The frequency and wavelength change, but the wave speed stays the same.

### Common Misconception #2

> "The Doppler effect only happens with sound."

The Doppler effect happens with **all** waves — sound, light, water waves, even the ripples on a pond. For light waves, the effect produces redshift and blueshift (Lesson 44).

---

## 2. The Doppler Equation for Sound

For sound waves, which require a medium (air, water, solid), the observed frequency is:

$$f' = f \left(\frac{v \pm v_o}{v \mp v_s}\right)$$

Where each symbol means:

| Symbol | Meaning | Units |
|--------|---------|-------|
| **f** | Frequency emitted by the source | Hz (hertz, per second) |
| **f'** | Frequency detected by the observer | Hz |
| **v** | Speed of sound in the medium | m/s |
| **v_o** | Speed of the observer relative to the medium | m/s |
| **v_s** | Speed of the source relative to the medium | m/s |

**All speeds are measured relative to the medium (usually still air).** This is crucial — we are not measuring speeds relative to each other. The air is the reference frame.

### The Sign Convention

This is the part that trips up almost everyone. Learn it carefully.

**Upper signs give an increase in frequency (approaching). Lower signs give a decrease (receding).**

#### Numerator: v ± v_o

The numerator deals with the **observer's** motion.

- Use **+** (plus) when the observer moves **toward** the source.
- Use **−** (minus) when the observer moves **away** from the source.

#### Denominator: v ∓ v_s

The denominator deals with the **source's** motion.

- Use **−** (minus) when the source moves **toward** the observer.
- Use **+** (plus) when the source moves **away** from the observer.

The ∓ symbol means "use the opposite of whatever the numerator used." If you used + in the numerator, use − in the denominator, and vice versa. But it's simpler to remember this rule:

> The fraction should get **bigger** (f' > f) when source and observer are getting closer together, and **smaller** (f' < f) when they are moving apart. Choose the signs that make this happen.

### Memory Strategy

Think of an ambulance approaching you:
- The source moves toward you: v_s should make the denominator **smaller** → use minus → f' gets bigger. ✓
- You move toward the source: v_o should make the numerator **bigger** → use plus → f' gets bigger. ✓

Think of an ambulance receding:
- Source moves away: denominator gets **bigger** → use plus → f' gets smaller. ✓
- You move away: numerator gets **smaller** → use minus → f' gets smaller. ✓

### Special Case: Only the Source Moves

If the observer is stationary (v_o = 0):

$$f' = f \left(\frac{v}{v \mp v_s}\right)$$

- Source approaching: $f' = f \left(\frac{v}{v - v_s}\right)$ → larger denominator → f' > f
- Source receding: $f' = f \left(\frac{v}{v + v_s}\right)$ → smaller denominator → f' < f

### Special Case: Only the Observer Moves

If the source is stationary (v_s = 0):

$$f' = f \left(\frac{v \pm v_o}{v}\right)$$

- Observer approaching source: $f' = f \left(\frac{v + v_o}{v}\right)$
- Observer receding from source: $f' = f \left(\frac{v - v_o}{v}\right)$

### Why Moving Source and Moving Observer Give Different Results

A source moving at 10 m/s toward a stationary observer does NOT produce the same frequency shift as an observer moving at 10 m/s toward a stationary source. The physics is different.

When the **source** moves, the wavelength in the medium actually changes (compressions bunch up or spread out). When the **observer** moves, the wavelength in the medium stays the same, but the observer encounters the wave crests at a different rate.

The full equation accounts for both effects simultaneously.

---

## 3. The Speed of Sound

The Doppler equation needs v, the speed of sound. At room temperature (20°C):

$$v \approx 343 \text{ m/s}$$

For IB problems, you will usually be told the speed of sound. If not stated, use 340 m/s (unless the problem specifically says otherwise). Sound travels faster in warmer air and slower in colder air, but IB problems typically give you v directly.

---

## 4. Sonic Booms and Mach Number

### What Happens When v_s = v?

Look at the equation: if the source moves toward you at exactly the speed of sound, the denominator becomes v − v_s = v − v = 0. The frequency becomes infinite. This is not physically meaningful — it tells you that something drastic happens.

When v_s = v, all the wavefronts pile up on top of each other at the source. A massive pressure wall builds up. This is the **sound barrier**.

### What Happens When v_s > v?

When the source moves faster than sound (supersonic), it outruns its own wavefronts. The wavefronts form a cone behind the source — a **shock wave**. When this shock wave passes over you, you hear a **sonic boom**.

The **Mach number** is defined as:

$$M = \frac{v_s}{v}$$

- M < 1: subsonic
- M = 1: sonic (sound barrier)
- M > 1: supersonic

A person on the ground does not hear a continuous sonic boom. They hear a single "boom" when the shock wave passes over them. The pilot does not hear the boom at all — they are ahead of it.

---

## 5. Common Misconceptions Summary

| Misconception | Reality |
|--------------|---------|
| Sound waves travel faster from a moving source | Wave speed depends on the medium, not the source speed |
| The Doppler effect changes the source frequency | The source emits the same f; only the observed f' changes |
| Moving source and moving observer give identical shifts | They differ physically; the equation accounts for both |
| The Doppler effect is only for sound | All waves experience it, including light |
| Sonic boom happens exactly at M = 1 | The boom is a continuous shock cone when M > 1; you hear it once as it passes |

---

## Worked Examples

### Example 1: Ambulance Approaching

An ambulance emits a siren at 800 Hz. It approaches a stationary observer at 30 m/s. The speed of sound is 340 m/s. What frequency does the observer hear?

**Approach:** The source moves toward the observer (v_s subtracts in denominator). Observer is stationary (v_o = 0). Use upper signs (approach → f' should increase).

$$f' = f \left(\frac{v}{v - v_s}\right) = 800 \times \frac{340}{340 - 30} = 800 \times \frac{340}{310}$$

$$f' = 800 \times 1.0968 = 877.4 \text{ Hz}$$

**Why this makes sense:** The source is approaching, so the frequency should increase. 877 Hz > 800 Hz. The ambulance is moving at about 9% of the speed of sound, so we expect roughly a 9% frequency increase — and that's what we got.

---

### Example 2: Ambulance Receding

The same ambulance, after passing, moves away at 30 m/s. What does the observer now hear?

**Approach:** Source moves away → add v_s in denominator.

$$f' = 800 \times \frac{340}{340 + 30} = 800 \times \frac{340}{370} = 800 \times 0.9189 = 735.1 \text{ Hz}$$

**Why this makes sense:** Moving away → frequency drops. 735 Hz < 800 Hz.

---

### Example 3: Observer Moving Toward a Stationary Source

A stationary speaker emits a tone at 500 Hz. A student runs toward it at 5 m/s. What frequency does the student hear? Take v = 340 m/s.

**Approach:** Source is stationary (v_s = 0). Observer moves toward source → add v_o in numerator.

$$f' = f \left(\frac{v + v_o}{v}\right) = 500 \times \frac{340 + 5}{340} = 500 \times \frac{345}{340}$$

$$f' = 500 \times 1.0147 = 507.4 \text{ Hz}$$

**Why this makes sense:** Small speed (5 m/s is only about 1.5% of the speed of sound), small frequency increase. ✓

---

### Example 4: Both Moving

A train blows its horn at 400 Hz while approaching a station at 25 m/s. A passenger on the platform walks toward the train at 2 m/s. What frequency does the passenger hear? v = 340 m/s.

**Approach:** Both moving toward each other. Both motions increase f'. Numerator: +v_o (observer toward source). Denominator: −v_s (source toward observer).

$$f' = 400 \times \frac{340 + 2}{340 - 25} = 400 \times \frac{342}{315}$$

$$f' = 400 \times 1.0857 = 434.3 \text{ Hz}$$

**Why this makes sense:** Both motions increase the frequency. The source's motion (25 m/s) is the dominant effect since it's much larger than the observer's speed (2 m/s).

---

### Example 5: Bat Echolocation

A bat flies at 8 m/s toward a wall while emitting a chirp at 50 kHz. The sound reflects off the wall and returns to the bat. What frequency does the bat hear in the echo? v = 340 m/s. (Hint: treat this as a two-step problem.)

**Approach:** Step 1: The wall is a stationary "observer" that receives a frequency from the approaching bat. Step 2: The wall acts as a stationary "source" reflecting that frequency. Step 3: The bat is now an observer moving toward this reflected sound.

Step 1 — frequency at the wall (f_wall):
$$f_{wall} = 50000 \times \frac{340}{340 - 8} = 50000 \times \frac{340}{332} = 50000 \times 1.0241 = 51205 \text{ Hz}$$

Step 2 — the wall reflects 51205 Hz. The bat now approaches this reflected sound as an observer:
$$f' = 51205 \times \frac{340 + 8}{340} = 51205 \times \frac{348}{340} = 51205 \times 1.0235 = 52398 \text{ Hz}$$

**Why this makes sense:** The frequency shift is nearly doubled because the bat experiences the Doppler shift twice — once as the source approaching a stationary reflector, and once as the observer approaching the reflected wave.

---

## Practice Problems

### Problem 1
A police car siren emits a frequency of 600 Hz. The car approaches a stationary pedestrian at 20 m/s. The speed of sound is 340 m/s.
(a) Calculate the frequency the pedestrian hears as the car approaches.
(b) Calculate the frequency the pedestrian hears after the car has passed and is receding.
(c) The pedestrian claims the pitch dropped by an octave. An octave is a factor of 2 in frequency. Is the pedestrian's claim correct? Explain using your calculations.

### Problem 2
A stationary loudspeaker emits a constant 1000 Hz tone. A student on a bicycle rides directly away from the speaker at 6 m/s. Take v = 340 m/s.
(a) What frequency does the student hear?
(b) The student then turns around and rides toward the speaker at the same speed. What frequency does she hear now?
(c) Explain why the answer to (b) is not simply 1000 Hz plus the difference found in (a).

### Problem 3
A train horn sounds at 440 Hz. The train approaches a crossing at 35 m/s. At the same time, a car drives toward the train at 15 m/s. v = 340 m/s.
(a) What frequency does the driver of the car hear?
(b) What frequency would the driver hear if the car were stationary?
(c) What frequency does a passenger on the train hear directly from the horn? (Hint: what is the relative speed of the passenger with respect to the horn?)

### Problem 4
A bat emits ultrasonic chirps at 40 kHz. It flies at 10 m/s toward a moth. v = 340 m/s.
(a) If the moth is stationary, what frequency does the moth receive?
(b) The reflected echo returns to the bat. What frequency does the bat hear in the echo?
(c) Explain why the bat hears a higher frequency in the echo than the moth hears directly.

### Problem 5
An airplane flies at Mach 1.5 at an altitude where the speed of sound is 330 m/s.
(a) What is the speed of the airplane in m/s?
(b) Explain why a person on the ground does not hear the airplane at all until it has already passed overhead.
(c) Why does the pilot not hear a sonic boom?

### Problem 6 (IB Exam-Style)
A car with a horn of frequency 520 Hz is involved in a police chase. The speed of sound in air is 340 m/s.
(a) The car travels at 28 m/s toward a stationary observer. Show that the observed frequency is approximately 570 Hz. [2 marks]
(b) After passing the observer, the car moves away. The observer measures the frequency as 480 Hz. Calculate the speed of the car. [3 marks]
(c) A second car also has a horn at 520 Hz. When both cars are stationary, a beat frequency of 0 Hz is observed. When one car moves toward the other at speed u, a beat frequency of 12 Hz is heard by the stationary car. Estimate u. You may use the approximation (1 − x)⁻¹ ≈ 1 + x for small x. [3 marks]

---

## Answers

### Answer 1
(a) $f' = 600 \times \frac{340}{340 - 20} = 600 \times \frac{340}{320} = 637.5 \text{ Hz}$

(b) $f' = 600 \times \frac{340}{340 + 20} = 600 \times \frac{340}{360} = 566.7 \text{ Hz}$

(c) An octave drop would mean f' = 300 Hz. The actual drop is from 637.5 Hz to 566.7 Hz, which is a ratio of only about 0.89, not 0.5. The pedestrian is incorrect. For the frequency to halve, the source would need to move at a significant fraction of the speed of sound — specifically, for f'/f = 0.5, we would need v/(v+v_s) = 0.5, giving v_s = v = 340 m/s (Mach 1). A police car at 20 m/s cannot produce an octave drop.

### Answer 2
(a) Observer receding: $f' = 1000 \times \frac{340 - 6}{340} = 1000 \times \frac{334}{340} = 982.4 \text{ Hz}$

(b) Observer approaching: $f' = 1000 \times \frac{340 + 6}{340} = 1000 \times \frac{346}{340} = 1017.6 \text{ Hz}$

(c) 1000 − 982.4 = 17.6 Hz decrease, and 1017.6 − 1000 = 17.6 Hz increase. In this case the shifts are symmetric because only the observer moves at a low speed. However, this symmetry breaks down at higher speeds and when both source and observer move. The Doppler equation is not linear in speed, so the shifts are only approximately symmetric for small v_o.

### Answer 3
(a) Both moving toward each other: $f' = 440 \times \frac{340 + 15}{340 - 35} = 440 \times \frac{355}{305} = 440 \times 1.1639 = 512.1 \text{ Hz}$

(b) Car stationary, only train moving: $f' = 440 \times \frac{340}{340 - 35} = 440 \times \frac{340}{305} = 490.5 \text{ Hz}$

(c) The passenger is stationary relative to the horn, so there is no Doppler shift. The passenger hears 440 Hz. The Doppler effect requires relative motion between source and observer, and the train passenger moves with the horn.

### Answer 4
(a) $f_{\text{moth}} = 40000 \times \frac{340}{340 - 10} = 40000 \times \frac{340}{330} = 41,212 \text{ Hz}$

(b) The moth reflects 41,212 Hz. The bat approaches this reflection: $f' = 41212 \times \frac{340 + 10}{340} = 41212 \times \frac{350}{340} = 42,433 \text{ Hz}$

(c) The bat hears a higher frequency because the frequency shift happens twice. First, the bat's motion as a source increases the frequency received by the moth. Second, the bat's motion as an observer of the reflected wave increases the frequency again. The moth only experiences the first shift.

### Answer 5
(a) $v_s = M \times v = 1.5 \times 330 = 495 \text{ m/s}$

(b) When an object moves faster than sound, the sound waves it emits trail behind it in a cone (the Mach cone). The wavefronts never reach a point ahead of the airplane. A person on the ground only hears the airplane after it has passed overhead and the shock cone sweeps over them.

(c) The pilot is ahead of the shock wave. The sonic boom propagates outward and backward from the plane. The pilot is inside the plane, moving with it, and never crosses the shock front.

### Answer 6
(a) $f' = 520 \times \frac{340}{340 - 28} = 520 \times \frac{340}{312} = 520 \times 1.0897 = 566.7 \text{ Hz} \approx 570 \text{ Hz}$ ✓ [2 marks]

(b) $480 = 520 \times \frac{340}{340 + v_s}$ → $340 + v_s = 520 \times 340 / 480 = 368.33$ → $v_s = 28.3 \text{ m/s}$ [3 marks]

(c) For the moving car approaching: $f' \approx 520(1 + u/v)$. Beat frequency = |f' − 520| = 520 × u/340 = 12 Hz. So u = 12 × 340 / 520 = 7.85 m/s. The approximation is valid since u/v ≈ 0.023, which is small. [3 marks]

---

## Key Takeaways

1. **The Doppler effect is a change in observed frequency when source and observer move relative to each other.** The source frequency itself never changes.

2. **The wave speed in the medium does NOT change.** Only the wavelength and the rate at which the observer encounters wavefronts change.

3. **Use the full equation $f' = f(v \pm v_o)/(v \mp v_s)$** and choose signs so that f' increases when approaching and decreases when receding.

4. **Moving source and moving observer are physically different.** A source moving at 10 m/s does not produce the same shift as an observer moving at 10 m/s.

5. **Sonic booms occur when v_s > v.** The sound waves form a shock cone behind the source. You hear the boom once as the cone passes over you.

6. **Always identify your reference frame** — all speeds are measured relative to the medium (usually still air).

7. **For reflected waves (radar, bat echolocation), the Doppler shift happens twice** — once on the way to the reflector and once on the way back.
