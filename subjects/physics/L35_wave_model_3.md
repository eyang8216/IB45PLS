# Lesson 35: Wave Model III — Diffraction, Huygens' Principle and Superposition

## What You'll Learn
- Use Huygens' principle to explain how waves propagate and diffract
- Understand why diffraction is most noticeable when the wavelength is comparable to the aperture size
- Apply the superposition principle to determine the result of overlapping waves
- Convert between path difference and phase difference
- Predict whether two waves at a point will interfere constructively or destructively

---

## 1. Huygens' Principle

### 1.1 What It Is

In 1678, Christiaan Huygens proposed a remarkably simple way to predict how a wavefront will evolve. His principle states: **every point on a wavefront acts as a source of tiny secondary wavelets that spread out in all directions at the wave speed. The new wavefront at a later time is the envelope (tangent surface) of all these secondary wavelets.**

Imagine dropping a stone into still water. The circular ripple that expands outward is the wavefront. Huygens says: take every point along that circle. Each point emits its own tiny circular wavelet. A moment later, all those tiny circles overlap. The outer edge where they all touch — the tangent line connecting their outermost points — forms the new, larger circular wavefront.

### 1.2 Why This Matters

Huygens' principle explains three fundamental wave behaviours that otherwise seem mysterious:

**Straight propagation:** Why does a plane wave stay plane? Each point on a straight wavefront produces circular wavelets. The envelope of all these circles is another straight line — but only in the forward direction. The wavelets going sideways and backward cancel each other out through interference (this was Huygens' great insight — he anticipated superposition before it was formally named).

**Reflection:** When a wavefront strikes a surface at an angle, different parts of the wavefront hit at different times. The secondary wavelets from the earlier-striking parts have travelled further by the time the later-striking parts reach the surface. The envelope of all these wavelets gives the reflected wavefront, with the angle of reflection equal to the angle of incidence. The law of reflection falls out naturally from Huygens' construction.

**Refraction:** When a wavefront crosses into a slower medium at an angle, the part that enters first slows down while the rest is still in the faster medium. The wavelets in the slower medium are smaller (same time, less distance). The envelope of the combined wavelets from both sides of the boundary produces a bent wavefront — exactly Snell's Law. This is the physical mechanism behind refraction.

### 1.3 Diffraction — When Waves Bend Around Corners

Huygens' principle also explains the phenomenon that most clearly distinguishes waves from particles: **diffraction**. When a wave passes through an aperture or past an obstacle, it spreads into the region behind the obstacle — the "shadow" region where particles would not reach.

Consider a plane wave approaching a narrow gap. According to Huygens, the points of the wavefront within the gap act as sources of secondary wavelets. If the gap is very wide compared to the wavelength, there are many such sources across the gap, and their wavelets combine to form a nearly straight wavefront continuing forward — the wave barely spreads. But if the gap is narrow (comparable to the wavelength), there are only a few sources, and their wavelets spread out in all directions with little cancellation — the wave fans out into the geometric shadow.

**The golden rule of diffraction:** Significant diffraction occurs when the size of the aperture or obstacle is comparable to (or smaller than) the wavelength. If the aperture is much larger than the wavelength, diffraction is negligible and the wave behaves like a ray (straight-line propagation).

This is why you can hear sound around a corner but cannot see around it. Sound waves have wavelengths of roughly 0.01–2 metres, comparable to doorways and corners. Light waves have wavelengths of roughly 400–700 nanometres — a billion times smaller — so everyday objects are enormous compared to the wavelength of light, and light travels in straight lines.

---

## 2. Superposition

### 2.1 The Principle

When two or more waves arrive at the same point at the same time, the resultant displacement at that point is simply the sum of the individual displacements. This is the **principle of superposition**.

$$y_{\text{resultant}} = y_1 + y_2 + y_3 + \dots$$

This principle is deceptively simple but has profound consequences. It means waves pass through each other unchanged — they do not bounce off each other or alter each other's paths. After overlapping, each wave continues as if the other was never there. What changes is only the net displacement while they overlap.

### 2.2 Constructive and Destructive Interference

When two waves of the same frequency meet, the result depends on their relative phase — that is, whether their crests and troughs align.

**Constructive interference** occurs when the waves are **in phase** (phase difference = 0, $2\pi$, $4\pi$, etc.). Crest meets crest and trough meets trough. The amplitudes add: $A_{\text{resultant}} = A_1 + A_2$. If the waves have equal amplitude, the resultant amplitude doubles, and the intensity quadruples (because intensity $\propto A^2$).

**Destructive interference** occurs when the waves are **exactly out of phase** (phase difference = $\pi$, $3\pi$, $5\pi$, etc.). Crest meets trough and they cancel. The amplitudes subtract: $A_{\text{resultant}} = |A_1 - A_2|$. If the waves have equal amplitude, the resultant amplitude is zero — complete cancellation.

At intermediate phase differences, the resultant amplitude is somewhere between the sum and the difference.

### 2.3 Path Difference

In most interference problems, the phase difference arises because one wave has travelled further than the other. The extra distance is called the **path difference** $\Delta L$.

The phase difference $\Delta\phi$ is related to the path difference by:

$$\Delta\phi = 2\pi \frac{\Delta L}{\lambda}$$

This makes intuitive sense: a path difference of one full wavelength ($\Delta L = \lambda$) means one wave is exactly one cycle behind the other, which is a phase difference of $2\pi$ radians — and the waves are back in phase. A path difference of half a wavelength means a phase difference of $\pi$ — the waves are exactly out of phase.

| Path Difference $\Delta L$ | Phase Difference $\Delta\phi$ | Result |
|---------------------------|------------------------------|--------|
| $0, \lambda, 2\lambda, \dots$ | $0, 2\pi, 4\pi, \dots$ | Constructive |
| $\lambda/2, 3\lambda/2, \dots$ | $\pi, 3\pi, \dots$ | Destructive |
| Anything else | Anything else | Partial interference |

---

## 3. Coherence — Why It Matters

For a stable interference pattern to be observed, the two sources must be **coherent**. Coherence means two things:

**Same frequency:** If the sources have different frequencies, the phase difference between them constantly changes. The interference pattern shifts so rapidly that the eye (or any detector) sees only the time-averaged intensity — uniform, with no fringes.

**Constant phase difference:** Even at the same frequency, if the relative phase drifts randomly (as with two independent light bulbs), the pattern averages out. A laser produces coherent light because all the emitted waves are in phase and maintain that relationship. In Young's double-slit experiment (Lesson 36), the two slits act as coherent sources because they are illuminated by the same primary wavefront — any phase fluctuation affects both slits equally.

---

## Worked Examples

### Worked Example 35.1 — Identifying Diffraction

**Problem:** A harbour has an entrance 50 m wide. Ocean waves with a wavelength of 20 m approach the entrance. Will the waves diffract significantly into the harbour? Explain. A second set of waves has a wavelength of 0.5 m. Will these diffract?

**Approach:** Compare the wavelength to the aperture size. Significant diffraction occurs when $\lambda$ is comparable to or larger than the aperture width.

**Solution:**
For the 20 m waves: $\lambda/a = 20/50 = 0.4$. The wavelength is a significant fraction of the aperture width — diffraction will be noticeable. The waves will spread into the harbour in a fan pattern.

For the 0.5 m waves: $\lambda/a = 0.5/50 = 0.01$. The wavelength is tiny compared to the aperture. These waves will pass through with negligible diffraction — they will travel in nearly straight lines, like light rays through a doorway.

**Why this makes sense:** This is exactly why harbours are designed with this physics in mind. Long-wavelength swell diffracts into harbour entrances, which is why breakwaters must be carefully positioned. Short-wavelength chop behaves more like particles, staying in straight lines.

---

### Worked Example 35.2 — Path Difference to Interference Type

**Problem:** Two coherent sources emit sound waves of wavelength 0.80 m. At a particular point, the distance to source 1 is 5.0 m and the distance to source 2 is 6.2 m. Determine whether the interference is constructive or destructive.

**Approach:** Find the path difference $\Delta L = |L_2 - L_1|$, then compare to multiples of $\lambda/2$.

**Solution:**
$$\Delta L = 6.2 - 5.0 = 1.2\text{ m}$$
$$\frac{\Delta L}{\lambda} = \frac{1.2}{0.80} = 1.5$$

A ratio of 1.5 means the path difference is $1.5\lambda = (1 + 0.5)\lambda$. This is a half-integer multiple of $\lambda$, corresponding to phase difference $\pi, 3\pi\text{ radians}$ — **destructive interference**. The waves arrive out of phase and partially cancel. If they have equal amplitudes, cancellation is complete.

---

### Worked Example 35.3 — Phase Difference from Path Difference

**Problem:** Two radio antennae emit coherent waves of frequency 100 MHz ($1.00 \times 10^8\text{ Hz}$). A receiver is placed 12 m from antenna A and 9.0 m from antenna B. Calculate the phase difference between the two signals at the receiver and state the type of interference. The speed of radio waves is $c = 3.00 \times 10^8\text{ m s}^{-1}$.

**Approach:** First find the wavelength from $c = f\lambda$. Then find path difference and convert to phase difference.

**Solution:**
$$\lambda = \frac{c}{f} = \frac{3.00 \times 10^8}{1.00 \times 10^8} = 3.0\text{ m}$$
$$\Delta L = 12 - 9.0 = 3.0\text{ m}$$
$$\frac{\Delta L}{\lambda} = 1.0$$

Path difference is exactly one wavelength → phase difference = $2\pi$ → **constructive interference**.

---

### Worked Example 35.4 — Superposition of Pulses (IB-Style)

**Problem:** Two triangular wave pulses travel toward each other on a string. Pulse A has a positive amplitude of 4.0 cm and travels to the right at 2.0 m s⁻¹. Pulse B has a negative amplitude of −3.0 cm and travels to the left at 2.0 m s⁻¹. At time $t = 0$, the peak of pulse A is at $x = 0$ and the peak of pulse B is at $x = 1.0\text{ m}$.

(a) Calculate the time at which the peaks of the two pulses meet. (2 marks)

(b) Determine the resultant displacement at the meeting point when the peaks coincide. (1 mark)

(c) Describe the motion of the pulses after they have passed through each other. (1 mark)

**Approach:** Relative speed determines meeting time. Superposition gives the resultant at overlap. After crossing, pulses continue unchanged.

**Solution:**
**(a)** The pulses approach each other at a relative speed of $2.0 + 2.0 = 4.0\text{ m s}^{-1}$. Initial separation of peaks = 1.0 m. Meeting time: $t = 1.0/4.0 = 0.25\text{ s}$.

**(b)** When peaks coincide, the resultant displacement is $4.0 + (-3.0) = +1.0\text{ cm}$ (positive, since the larger positive pulse dominates).

**(c)** After passing through each other, each pulse continues in its original direction with its original shape and amplitude. Pulse A continues right as a +4.0 cm pulse. Pulse B continues left as a −3.0 cm pulse. The superposition principle guarantees that waves pass through each other unchanged.

---

## Practice Problems

### Problem 1
Water waves of wavelength 6.0 m approach a gap between two breakwaters 18 m wide. Will the waves diffract significantly? Explain. What would happen if the gap were only 3.0 m wide?

### Problem 2
Two coherent sources produce waves of wavelength 2.0 m. At a certain point, the path difference from the two sources is 5.0 m. Determine the type of interference. The amplitude of each individual wave at this point is 0.50 m. Determine the resultant amplitude.

### Problem 3
Radio waves of frequency 50 MHz are transmitted from two coherent antennae. A receiver is positioned so that its distance to antenna A is 45 m and to antenna B is 39 m. Determine whether the receiver detects a strong signal (constructive interference) or a weak signal (destructive interference).

### Problem 4
Two loudspeakers emit sound waves of frequency 680 Hz in phase. The speed of sound is 340 m s⁻¹. An observer stands 5.0 m from speaker 1. At what distances from speaker 2 (closer than 5.0 m) would the observer experience destructive interference?

### Problem 5 — IB-Style Examination Question
Two identical microwave transmitters, A and B, are placed 0.60 m apart and emit coherent, in-phase waves of frequency 10 GHz ($1.0 \times 10^{10}\text{ Hz}$). A detector is moved along a line parallel to AB, at a distance of 3.0 m from the line joining the transmitters. The speed of electromagnetic waves is $3.0 \times 10^8\text{ m s}^{-1}$.

(a) Calculate the wavelength of the microwaves. (1 mark)

(b) Explain why the detector records a series of maxima and minima as it is moved parallel to AB. (2 marks)

(c) At the central position (equidistant from A and B), the detector records a maximum. Calculate how far the detector must be moved along its line to reach the first minimum. (3 marks)

(d) The frequency of the transmitters is doubled while all other parameters remain the same. Describe and explain how the spacing between adjacent maxima changes. (2 marks)

---

## Answers

### Answer 1
For gap 18 m: $\lambda/a = 6.0/18 = 0.33$. The wavelength is a third of the gap width — moderate diffraction will occur, but the waves will not fan out dramatically.

For gap 3.0 m: $\lambda/a = 6.0/3.0 = 2.0$. The wavelength is actually larger than the gap! Very strong diffraction — the gap acts almost as a point source, and the waves spread out in nearly semicircular wavefronts. This is the regime of maximum diffraction.

---

### Answer 2
$\Delta L/\lambda = 5.0/2.0 = 2.5$. This is a half-integer (2.5 = 2 + 0.5), meaning destructive interference. If the individual amplitudes are 0.50 m each and the waves are exactly out of phase, the resultant amplitude is $|0.50 - 0.50| = 0$ — complete cancellation. (This assumes equal amplitudes at the observation point, which is true for identical sources at different distances only if the distance difference is small compared to the absolute distances, so that amplitude decay with distance is negligible.)

---

### Answer 3
$\lambda = c/f = (3.0 \times 10^8)/(5.0 \times 10^7) = 6.0\text{ m}$. $\Delta L = 45 - 39 = 6.0\text{ m}$. $\Delta L/\lambda = 1.0$ — exactly one wavelength. This gives constructive interference, so the receiver detects a strong signal.

---

### Answer 4
$\lambda = v/f = 340/680 = 0.50\text{ m}$. The observer is 5.0 m from speaker 1. For destructive interference, the path difference must be an odd multiple of $\lambda/2 = 0.25\text{ m}$: $\Delta L = 0.25, 0.75, 1.25, \dots\text{ m}$.

Distance to speaker 2: $L_2 = L_1 \pm \Delta L$. Since we want $L_2 < 5.0\text{ m}$: $L_2 = 5.0 - 0.25 = 4.75\text{ m}$ (first minimum), $L_2 = 5.0 - 0.75 = 4.25\text{ m}$ (second minimum), $L_2 = 5.0 - 1.25 = 3.75\text{ m}$ (third minimum), etc., as long as $L_2 > 0$.

---

### Answer 5 — IB-Style Mark Scheme

**(a)** $\lambda = c/f = (3.0 \times 10^8)/(1.0 \times 10^{10}) = 0.030\text{ m} = 3.0\text{ cm}$. (1 mark)

**(b)** As the detector moves, the path difference between waves from A and B changes. When the path difference equals $n\lambda$, the waves arrive in phase and a maximum (constructive interference) is recorded. When the path difference equals $(n + 1/2)\lambda$, the waves arrive out of phase and a minimum (destructive interference) is recorded. The alternating constructive and destructive interference produces the series of maxima and minima. (2 marks — 1 for path difference explanation, 1 for linking to constructive/destructive.)

**(c)** At the central maximum, the detector is equidistant from A and B, so $\Delta L = 0$. The first minimum occurs when $\Delta L = \lambda/2 = 0.015\text{ m}$.

For a detector at lateral displacement $y$ from the centre, at distance $D = 3.0\text{ m}$ from the source line, the path difference is approximately $\Delta L \approx d(y/D)$ for small $y$, where $d = 0.60\text{ m}$ is the source separation.

$$0.015 = 0.60 \times \frac{y}{3.0}$$
$$y = 0.015 \times \frac{3.0}{0.60} = 0.075\text{ m} = 7.5\text{ cm}$$

(3 marks — 1 for $\Delta L = \lambda/2$, 1 for relating path difference to position, 1 for correct answer.)

**(d)** Doubling the frequency halves the wavelength (from 3.0 cm to 1.5 cm), since $\lambda = c/f$. The fringe separation is proportional to $\lambda$ (from $s = \lambda D/d$), so the spacing between adjacent maxima also halves. The maxima become twice as close together. (1 mark for stating the spacing decreases/halves. 1 mark for explaining why — wavelength halved, $s \propto \lambda$.) This is a general result: higher frequency → shorter wavelength → more tightly packed interference fringes.

---

## Key Takeaways

1. **Huygens' principle:** Every point on a wavefront acts as a source of secondary wavelets. The new wavefront is the envelope of these wavelets. This explains reflection, refraction, and diffraction.

2. **Diffraction is significant when aperture size ≈ wavelength.** Sound diffracts around corners; light does not, because its wavelength is microscopic.

3. **Superposition:** Resultant displacement = sum of individual displacements. Waves pass through each other unchanged.

4. **Path difference** $\Delta L$ determines interference type. $\Delta L = n\lambda$ → constructive. $\Delta L = (n + \frac{1}{2})\lambda$ → destructive.

5. **Phase difference** = $2\pi \times (\Delta L/\lambda)$. In phase ($0, 2\pi, 4\pi\dots$) → constructive. Out of phase ($\pi, 3\pi\dots$) → destructive.

6. **Coherence** (same frequency, constant phase difference) is essential for observable interference patterns.
