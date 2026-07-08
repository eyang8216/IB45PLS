# Lesson 36: Wave Phenomena I — Young's Double Slit

## What You'll Learn

By the end of this lesson, you will be able to:
- Explain how Young's double-slit experiment provides evidence for the wave nature of light
- Calculate the fringe separation using $s = \frac{\lambda D}{d}$
- Predict how changing the wavelength, slit separation, or screen distance affects the interference pattern
- Distinguish between constructive and destructive interference in terms of path difference
- Understand the conditions needed for observable interference (coherence, monochromatic light)

---

## 1. Why Young's Experiment Changed Physics Forever

### 1.1 The Historical Context

In the late 1600s, Isaac Newton argued that light was made of particles (corpuscles). For over a century, Newton's immense reputation meant that the particle theory dominated. In 1801, Thomas Young performed an experiment so simple and elegant that it changed everything. He shone light through two closely spaced slits and observed a pattern of alternating bright and dark bands on a screen. This pattern — an interference pattern — could only be explained if light were a wave. Particles cannot cancel each other out; waves can. Young's double-slit experiment was the first clear experimental evidence that light behaves as a wave.

### 1.2 Why This Matters for You

Young's double-slit formula $s = \frac{\lambda D}{d}$ is one of the most frequently tested equations in IB Physics. It appears in Paper 1 multiple-choice questions, Paper 2 structured problems, and Paper 3 data-analysis questions. Beyond the formula itself, the experiment illustrates the fundamental wave concepts of superposition, interference, coherence, and path difference — concepts that apply to ALL waves, not just light. If you understand Young's experiment deeply, you understand interference, and interference is half of wave physics.

---

## 2. The Experiment — What You See and Why

### 2.1 The Setup

Young's experiment requires:
- A source of **monochromatic** light (light of a single wavelength — a laser is ideal)
- Two **narrow parallel slits** separated by a small distance $d$ (typically a fraction of a millimetre)
- A **screen** placed at a distance $D$ from the slits, where $D \gg d$ (the screen is much further away than the slit separation)

When monochromatic light passes through both slits, each slit acts as a new source of waves (this is Huygens' principle, covered in Lesson 35). The two sets of waves spread out and overlap on the screen. At each point on the screen, waves from the two slits have travelled slightly different distances. This path difference determines whether the waves arrive in phase (constructive interference — bright fringe) or out of phase (destructive interference — dark fringe).

### 2.2 The Pattern

The pattern consists of:
- A **central bright fringe** (the "zeroth order" maximum) directly opposite the midpoint between the slits
- **Bright fringes** (maxima) on either side, equally spaced
- **Dark fringes** (minima) between the bright fringes
- All fringes are equally spaced by a distance $s$, called the **fringe separation**

The fringes are equally spaced because, for small angles, the path difference changes linearly with position on the screen. This equal spacing is a hallmark of the double-slit pattern and distinguishes it from the single-slit diffraction pattern (which has a wide central maximum and narrower, dimmer side maxima — see Lesson 37).

### 2.3 The Fringe Separation Formula

$$s = \frac{\lambda D}{d}$$

where:
- $s$ is the distance between adjacent bright fringes (or adjacent dark fringes) — the fringe separation (m)
- $\lambda$ is the wavelength of the light (m)
- $D$ is the distance from the slits to the screen (m)
- $d$ is the separation between the two slits (m)

This formula is in the IB Data Booklet. It is derived from the condition for constructive interference in the small-angle approximation, where $\sin\theta \approx \tan\theta \approx \theta$ (in radians). You do not need to derive it from memory, but understanding the derivation helps you remember which variable goes where.

### 2.4 Physical Meaning of Each Variable

**Wavelength $\lambda$:** Longer wavelength (redder light) → larger fringe separation. The pattern spreads out. Shorter wavelength (bluer light) → smaller fringe separation. The pattern compresses.

**Screen distance $D$:** Moving the screen further away → larger fringe separation. The pattern magnifies. This is simple geometry — the same angular separation translates to a larger linear separation at a greater distance.

**Slit separation $d$:** Closer slits → larger fringe separation. This is the counter-intuitive one. Making the slits closer together actually spreads the pattern out. Conversely, wider slit separation compresses the pattern. If $d$ becomes too large, the fringes become too close to resolve, and the pattern disappears into uniform illumination.

### 2.5 Why Monochromatic and Coherent?

Young's experiment only produces a clear interference pattern if two conditions are met:

**Monochromatic light:** Light of a single wavelength is needed because different wavelengths produce fringes at different positions. If white light is used, each wavelength produces its own pattern at a slightly different position. The central fringe is white (all wavelengths overlap at zero path difference), but the side fringes show rainbow colours because blue fringes are closer together than red fringes.

**Coherence:** The light waves from the two slits must maintain a constant phase relationship. If the phase difference between the two sources varies randomly with time, the interference pattern shifts randomly and averages out to uniform illumination. Young achieved coherence by using a single source and splitting it with two slits — any phase fluctuation affects both slits equally, so their relative phase remains constant. A laser is inherently coherent, which is why modern versions of the experiment use lasers.

---

## 3. Path Difference and Phase Difference

### 3.1 The Connection

The condition for whether two waves interfere constructively or destructively depends on how much further one wave has travelled than the other. This is the **path difference** $\Delta L$.

For **constructive interference** (bright fringe):
$$\Delta L = n\lambda \quad \text{where } n = 0, \pm 1, \pm 2, \dots$$

The waves arrive in phase — crest meets crest and trough meets trough. The path difference is a whole number of wavelengths.

For **destructive interference** (dark fringe):
$$\Delta L = \left(n + \frac{1}{2}\right)\lambda \quad \text{where } n = 0, \pm 1, \pm 2, \dots$$

The waves arrive exactly out of phase — crest meets trough and they cancel. The path difference is a half-integer number of wavelengths.

### 3.2 Phase Difference

The phase difference $\Delta\phi$ is related to the path difference by:

$$\Delta\phi = 2\pi \frac{\Delta L}{\lambda}$$

A path difference of one wavelength ($\Delta L = \lambda$) corresponds to a phase difference of $2\pi$ radians (360°). A path difference of half a wavelength corresponds to a phase difference of $\pi$ radians (180°), producing cancellation.

### 3.3 The Small-Angle Derivation

For the $n$-th bright fringe at an angle $\theta_n$ from the central axis, the path difference from the two slits is approximately $d\sin\theta_n$. Setting this equal to $n\lambda$ gives:

$$d\sin\theta_n = n\lambda$$

The position of the $n$-th bright fringe on the screen is $y_n = D\tan\theta_n$. For small angles, $\sin\theta \approx \tan\theta \approx \theta$, so:

$$y_n \approx \frac{n\lambda D}{d}$$

The fringe separation is the distance between adjacent bright fringes:

$$s = y_{n+1} - y_n = \frac{(n+1)\lambda D}{d} - \frac{n\lambda D}{d} = \frac{\lambda D}{d}$$

This is the origin of the formula. The approximation is valid when $D \gg d$ and when we are looking at fringes close to the centre of the pattern.

---

## Worked Examples

### Worked Example 36.1 — Finding Fringe Separation

**Problem:** Red light of wavelength $650\text{ nm}$ passes through two slits separated by $0.25\text{ mm}$. The screen is placed $2.0\text{ m}$ from the slits. Calculate the fringe separation on the screen.

**Approach:** Use $s = \lambda D/d$. Convert all distances to metres.

**Solution:**
$$\lambda = 650 \times 10^{-9}\text{ m}, \quad d = 0.25 \times 10^{-3}\text{ m}, \quad D = 2.0\text{ m}$$
$$s = \frac{\lambda D}{d} = \frac{(650 \times 10^{-9})(2.0)}{0.25 \times 10^{-3}}$$
$$s = \frac{1.30 \times 10^{-6}}{2.5 \times 10^{-4}} = 5.2 \times 10^{-3}\text{ m} = 5.2\text{ mm}$$

**Why this makes sense:** With red light, a modest screen distance, and closely spaced slits, the fringes are about 5 mm apart — easily visible to the naked eye. This is typical for classroom demonstrations of Young's experiment.

---

### Worked Example 36.2 — Finding Wavelength from the Pattern

**Problem:** In a double-slit experiment, the slits are $0.40\text{ mm}$ apart and the screen is $1.5\text{ m}$ away. Ten bright fringes span a total distance of $24\text{ mm}$ on the screen. Calculate the wavelength of the light.

**Approach:** First find the fringe separation $s$ (the distance between adjacent fringes). If 10 fringes span 24 mm, the spacing between the first and tenth fringe is $9s$ (because there are 9 gaps between 10 fringes). Then use $\lambda = sd/D$.

**Solution:**

Distance from fringe 1 to fringe 10: $9s = 24\text{ mm}$, so $s = 24/9 = 2.67\text{ mm} = 2.67 \times 10^{-3}\text{ m}$.

$$\lambda = \frac{sd}{D} = \frac{(2.67 \times 10^{-3})(0.40 \times 10^{-3})}{1.5}$$
$$\lambda = \frac{1.07 \times 10^{-6}}{1.5} = 7.11 \times 10^{-7}\text{ m} = 711\text{ nm}$$

**Why this makes sense:** 711 nm is in the deep red part of the visible spectrum, which is plausible for a classroom laser (common wavelengths are 633 nm for helium-neon lasers and 650 nm for red diode lasers). The calculation is consistent.

A common mistake is to count 10 fringes as $10s$. Always remember: $N$ fringes have $N-1$ gaps between them. If you measure from the central fringe (fringe 0) to fringe $N$, that's exactly $Ns$.

---

### Worked Example 36.3 — Effect of Changing Parameters

**Problem:** In a double-slit experiment with blue light ($\lambda = 450\text{ nm}$), slits separated by $0.30\text{ mm}$, and a screen $1.8\text{ m}$ away, the fringe separation is $2.7\text{ mm}$. The blue light is replaced by red light of wavelength $650\text{ nm}$. All other parameters remain the same. Calculate the new fringe separation.

**Approach:** Since $D$ and $d$ are unchanged, $s$ is directly proportional to $\lambda$. The new fringe separation is the old one multiplied by the ratio of wavelengths.

**Solution:**
$$s_{\text{red}} = s_{\text{blue}} \times \frac{\lambda_{\text{red}}}{\lambda_{\text{blue}}} = 2.7 \times \frac{650}{450} = 2.7 \times 1.44 = 3.9\text{ mm}$$

**Why this makes sense:** Red light has a longer wavelength, so the fringes spread out. The factor of 1.44 means the pattern becomes about 44% wider. This also means that if white light is used, the red fringes appear further from the centre than the blue fringes, creating the rainbow effect in higher-order fringes.

---

### Worked Example 36.4 — IB-Style Path Difference Problem

**Problem:** In a double-slit experiment using light of wavelength $600\text{ nm}$, the slits are $0.20\text{ mm}$ apart and the screen is $3.0\text{ m}$ away. At a point on the screen $18\text{ mm}$ from the central bright fringe, determine whether the interference is constructive or destructive. State the order $n$ if constructive.

**Approach:** Find the fringe separation, then determine how many fringe separations the point is from the centre. Alternately, calculate the path difference using the small-angle approximation and compare to multiples of $\lambda$.

**Solution:**

Fringe separation: $s = \lambda D/d = (600 \times 10^{-9} \times 3.0)/(0.20 \times 10^{-3}) = 1.80 \times 10^{-6} / 2.0 \times 10^{-4} = 9.0 \times 10^{-3}\text{ m} = 9.0\text{ mm}$.

Distance from centre: $y = 18\text{ mm} = 2s$. This is exactly two fringe separations from the centre, corresponding to the $n = 2$ bright fringe. The interference is constructive.

Path difference approach: $\sin\theta \approx \tan\theta = y/D = 0.018/3.0 = 0.0060$. Path difference: $\Delta L = d\sin\theta = (0.20 \times 10^{-3})(0.0060) = 1.20 \times 10^{-6}\text{ m}$. Dividing by $\lambda$: $\Delta L/\lambda = 1.20 \times 10^{-6} / 600 \times 10^{-9} = 2.0$. Exactly 2 wavelengths → $n = 2$ constructive.

**Why this makes sense:** Both methods give the same result, confirming the consistency of the fringe separation formula with the path difference approach. The point is at the second bright fringe.

---

### Worked Example 36.5 — White Light and Fringe Width (IB-Style)

**Problem:** A double-slit experiment is performed first with a red laser ($\lambda = 650\text{ nm}$) and then with a blue laser ($\lambda = 450\text{ nm}$). The slit separation is $0.15\text{ mm}$ and the screen distance is $2.5\text{ m}$. 

(a) Calculate the fringe separation for each colour. (2 marks)

(b) The experiment is now performed with white light. Describe the appearance of the interference pattern on the screen, explaining why the central fringe is white and why the higher-order fringes show colours. (3 marks)

(c) Explain why a laser is preferable to a filament lamp for this experiment, even when a coloured filter is used with the lamp. (2 marks)

**Approach:** Use $s = \lambda D/d$ for each wavelength. Discuss coherence for part (c).

**Solution (a):**
$$s_{\text{red}} = \frac{(650 \times 10^{-9})(2.5)}{0.15 \times 10^{-3}} = \frac{1.625 \times 10^{-6}}{1.5 \times 10^{-4}} = 1.08 \times 10^{-2}\text{ m} = 10.8\text{ mm}$$
$$s_{\text{blue}} = \frac{(450 \times 10^{-9})(2.5)}{0.15 \times 10^{-3}} = \frac{1.125 \times 10^{-6}}{1.5 \times 10^{-4}} = 7.50 \times 10^{-3}\text{ m} = 7.5\text{ mm}$$

**(b)** With white light, each wavelength produces its own interference pattern at a different scale because $s \propto \lambda$. At the centre, all wavelengths have zero path difference, so all colours interfere constructively at the same position. The central fringe is therefore white — it is the sum of all colours.

Away from the centre, the fringe positions differ for each colour. Blue fringes are closer together (shorter wavelength); red fringes are further apart (longer wavelength). At a given position, some wavelengths interfere constructively while others interfere destructively. This produces coloured fringes — the colour you see at a given position is the colour that is constructively interfering there. The pattern shows a spectrum that repeats, with colours becoming increasingly mixed at higher orders. Eventually, for large $n$, the overlapping of many orders washes out into white light.

**(c)** A laser produces coherent light — all the light waves are in phase and maintain a constant phase relationship. A filament lamp, even with a filter, produces incoherent light — the phase of the emitted light fluctuates randomly on a timescale of nanoseconds. With incoherent light, the interference pattern shifts randomly and averages out. Young's original experiment used a single slit before the double slits to create spatial coherence from sunlight, but a laser is far brighter and produces a much clearer pattern. A filter only selects a narrow wavelength range; it does NOT make the light coherent.

---

## Practice Problems

### Problem 1
A double-slit experiment uses light of wavelength $550\text{ nm}$. The slits are $0.30\text{ mm}$ apart and the screen is $2.0\text{ m}$ from the slits. Calculate the fringe separation on the screen.

### Problem 2
In a double-slit experiment with slits $0.50\text{ mm}$ apart and a screen $1.2\text{ m}$ away, the distance between the central bright fringe and the fifth bright fringe (not including the central fringe) is $7.2\text{ mm}$. Calculate the wavelength of the light.

### Problem 3
A student performs a double-slit experiment and measures a fringe separation of $4.0\text{ mm}$. She then doubles the distance from the slits to the screen and halves the slit separation. All other parameters remain the same. Calculate the new fringe separation.

### Problem 4
Light of wavelength $480\text{ nm}$ illuminates two slits separated by $0.20\text{ mm}$. The screen is $1.6\text{ m}$ from the slits. At a point on the screen $14.4\text{ mm}$ from the central maximum, determine whether a bright fringe or a dark fringe occurs, and state its order.

### Problem 5 — IB-Style Examination Question
A student investigates the interference of light using a double-slit arrangement. The slits are separated by a distance $d = 0.250 \pm 0.005\text{ mm}$. The screen is placed at a distance $D = 2.00 \pm 0.01\text{ m}$ from the slits. A laser of unknown wavelength is used. The student measures the distance across 10 bright fringes (from fringe 1 to fringe 10) as $w = 47.0 \pm 0.5\text{ mm}$.

(a) Determine the fringe separation $s$, including its absolute uncertainty. (2 marks)

(b) Calculate the wavelength of the laser light. (2 marks)

(c) Determine the percentage uncertainty in the calculated wavelength arising from the uncertainties in $d$, $D$, and $s$. (3 marks)

(d) The student repeats the experiment with a different laser that produces light of longer wavelength. State and explain one change the student would observe in the interference pattern, assuming the apparatus remains otherwise unchanged. (2 marks)

---

## Answers

### Answer 1
$$s = \frac{\lambda D}{d} = \frac{(550 \times 10^{-9})(2.0)}{0.30 \times 10^{-3}} = \frac{1.10 \times 10^{-6}}{3.0 \times 10^{-4}} = 3.67 \times 10^{-3}\text{ m} \approx 3.7\text{ mm}$$

---

### Answer 2
The fifth bright fringe is at $y_5 = 5s$ from the central fringe. So $s = 7.2/5 = 1.44\text{ mm}$.
$$\lambda = \frac{sd}{D} = \frac{(1.44 \times 10^{-3})(0.50 \times 10^{-3})}{1.2} = \frac{7.2 \times 10^{-7}}{1.2} = 6.0 \times 10^{-7}\text{ m} = 600\text{ nm}$$

---

### Answer 3
$$s_{\text{new}} = s_{\text{old}} \times \frac{D_{\text{new}}/d_{\text{new}}}{D_{\text{old}}/d_{\text{old}}} = 4.0 \times \frac{2D_{\text{old}}/(d_{\text{old}}/2)}{D_{\text{old}}/d_{\text{old}}} = 4.0 \times \frac{2}{1/2} = 4.0 \times 4 = 16\text{ mm}$$

Doubling $D$ doubles $s$. Halving $d$ also doubles $s$. Both effects multiply together: $4.0 \times 2 \times 2 = 16\text{ mm}$.

---

### Answer 4
$$s = \frac{(480 \times 10^{-9})(1.6)}{0.20 \times 10^{-3}} = \frac{7.68 \times 10^{-7}}{2.0 \times 10^{-4}} = 3.84 \times 10^{-3}\text{ m} = 3.84\text{ mm}$$

Distance from centre: $y = 14.4\text{ mm}$. Number of fringe separations: $14.4/3.84 = 3.75$. Since this is not a whole number ($n = 3$) or a half-integer ($n + 0.5$), let me check more carefully.

Actually, $3.75$ is $3 + 0.75$, which is not an integer or half-integer. Wait — $3.75$ is $15/4$. That's not $n$ or $n+1/2$.

Let me recalculate: $s = 3.84\text{ mm}$. $y/s = 14.4/3.84 = 3.75$. This is exactly $3\frac{3}{4}$. 

A bright fringe occurs when $y = ns$, so $n = 3.75$ gives no integer $n$. A dark fringe occurs when $y = (n + 1/2)s$, so $n + 1/2 = 3.75$ means $n = 3.25$, also not an integer.

Hmm, $3.75 = 15/4$. Neither $n$ nor $n+1/2$ matches. So this point is between a bright and dark fringe — it's neither fully constructive nor fully destructive. At this position, the waves partially interfere, giving intermediate brightness.

Let me double-check: Path difference $\Delta L = d\sin\theta = d \times (y/D) = (2.0 \times 10^{-4})(14.4 \times 10^{-3}/1.6) = (2.0 \times 10^{-4})(9.0 \times 10^{-3}) = 1.80 \times 10^{-6}\text{ m}$.

$\Delta L / \lambda = 1.80 \times 10^{-6} / 480 \times 10^{-9} = 1.80/0.48 = 3.75$.

Since 3.75 is not an integer (constructive) or half-integer (destructive), the point experiences partial interference — it is between a bright and dark fringe. The brightness is intermediate.

---

### Answer 5 — IB-Style Full Solution with Mark Scheme

**(a)** (2 marks)
Ten fringes (1 through 10) span $9s$ gaps. So $9s = 47.0\text{ mm}$ and $s = 47.0/9 = 5.222\text{ mm} \approx 5.22\text{ mm}$. (1 mark)

Uncertainty: $\Delta s = \Delta w/9 = 0.5/9 = 0.0556\text{ mm} \approx 0.06\text{ mm}$. So $s = 5.22 \pm 0.06\text{ mm}$. (1 mark for correct propagation; accept $0.06$ or $0.056$.)

**(b)** (2 marks)
$$\lambda = \frac{sd}{D} = \frac{(5.22 \times 10^{-3})(0.250 \times 10^{-3})}{2.00} = \frac{1.305 \times 10^{-6}}{2.00} = 6.53 \times 10^{-7}\text{ m} = 653\text{ nm}$$
1 mark for correct substitution. 1 mark for correct answer with unit.

**(c)** (3 marks)
Percentage uncertainty in $s$: $\frac{0.056}{5.22} \times 100\% = 1.07\%$.
Percentage uncertainty in $d$: $\frac{0.005}{0.250} \times 100\% = 2.00\%$.
Percentage uncertainty in $D$: $\frac{0.01}{2.00} \times 100\% = 0.50\%$.

Since $\lambda = sd/D$, the percentage uncertainty in $\lambda$ is the sum of the individual percentage uncertainties (all are multiplied/divided):
$$\text{% uncertainty in } \lambda = 1.07\% + 2.00\% + 0.50\% = 3.57\% \approx 3.6\%$$

(1 mark for calculating each individual % uncertainty. 1 mark for recognising that % uncertainties add for multiplication/division. 1 mark for correct total.)

**(d)** (2 marks)
Longer wavelength means the fringe separation increases because $s \propto \lambda$. The interference pattern would spread out — the bright and dark fringes would be further apart on the screen. (1 mark for stating the change.)

This occurs because each fringe corresponds to a path difference of exactly one additional wavelength. With a longer wavelength, a larger lateral distance on the screen is needed to accumulate that additional wavelength of path difference. (1 mark for explanation.)

---

## Key Takeaways

1. **Young's double-slit experiment proved light is a wave** by demonstrating interference — waves can cancel, particles cannot.

2. **Fringe separation:** $s = \frac{\lambda D}{d}$. Memorise this. It is in the Data Booklet.

3. **Constructive interference:** path difference = $n\lambda$. **Destructive interference:** path difference = $(n + \frac{1}{2})\lambda$.

4. **The fringes are equally spaced** only for small angles. The formula $s = \lambda D/d$ assumes small-angle approximation.

5. **Changing parameters:** Increasing $\lambda$ or $D$ increases $s$ (spreads pattern). Increasing $d$ decreases $s$ (compresses pattern). Closer slits make wider fringes.

6. **Coherence is essential.** A laser is coherent; a filament bulb is not. Without coherence, the interference pattern washes out.
