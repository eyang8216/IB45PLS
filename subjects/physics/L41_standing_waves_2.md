# Lesson 41: Standing Waves II — Pipes & Resonance

## What You'll Learn
- Standing waves in open pipes (both ends open)
- Standing waves in closed pipes (one end closed)
- Why closed pipes only produce odd harmonics
- End correction and its effect on effective pipe length
- Comparing open and closed pipe behaviour

---

## 1. Standing Waves in Pipes

Sound waves in pipes form standing waves when the frequency matches the pipe's natural (resonant) frequencies. The boundary conditions differ from strings:

| Boundary | Condition | What forms there |
|----------|-----------|-----------------|
| **Open end** | Pressure node, displacement antinode | Antinode (A) |
| **Closed end** | Pressure antinode, displacement node | Node (N) |

> **Why?** At an open end, air is free to move (max displacement), but pressure equals atmospheric (pressure node). At a closed end, air cannot move (zero displacement = node), but pressure varies maximally.

---

## 2. Open Pipes (Both Ends Open)

Both ends are **antinodes** (A). The simplest standing wave has one node in the middle.

### Harmonics

$$L = n \cdot \frac{\lambda_n}{2} \quad n = 1, 2, 3, ...$$

$$\lambda_n = \frac{2L}{n}$$

$$f_n = \frac{nv}{2L} = n \cdot f_1$$

**All harmonics are possible.** This is the same formula as strings!

### Patterns

| Harmonic | n | Pattern | λ | f |
|----------|---|--------|---|---|
| 1st (fundamental) | 1 | A–N–A | 2L | v/(2L) |
| 2nd | 2 | A–N–A–N–A | L | v/L |
| 3rd | 3 | A–N–A–N–A–N–A | 2L/3 | 3v/(2L) |

```
Open Pipe Patterns (displacement):

Fundamental (n=1):     A     N     A
                       ↑     .     ↑

2nd Harmonic (n=2):    A  N  A  N  A
                       ↑  .  ↑  .  ↑

3rd Harmonic (n=3):    A N A N A N A
                       ↑ . ↑ . ↑ . ↑
```

---

## 3. Closed Pipes (One End Closed)

One end is a **node** (closed), one end is an **antinode** (open). The simplest standing wave fits 1/4 wavelength.

### Harmonics — Odd Only!

$$L = n \cdot \frac{\lambda_n}{4} \quad n = 1, 3, 5, ...$$

$$\lambda_n = \frac{4L}{n}$$

$$f_n = \frac{nv}{4L} = n \cdot f_1$$

**Only odd harmonics exist!** (n = 1, 3, 5, 7, ...)

### Why No Even Harmonics?

An even harmonic would require an antinode at the closed end or a node at the open end — both violate boundary conditions. Try n = 2: λ = 2L, which would put a node at the open end. Impossible.

### Patterns

| Harmonic | n | Pattern | λ | f |
|----------|---|--------|---|---|
| 1st (fundamental) | 1 | N–A (one node, one antinode) | 4L | v/(4L) |
| 3rd (1st overtone) | 3 | N–A–N–A | 4L/3 | 3v/(4L) |
| 5th (2nd overtone) | 5 | N–A–N–A–N–A | 4L/5 | 5v/(4L) |

```
Closed Pipe Patterns (displacement, closed end on left):

Fundamental (n=1):     N        A
                       .        ↑

3rd Harmonic (n=3):    N  A  N  A
                       .  ↑  .  ↑

5th Harmonic (n=5):    N A N A N A
                       . ↑ . ↑ . ↑
```

---

## 4. Comparison: Open vs Closed Pipes

| Property | Open Pipe | Closed Pipe |
|----------|-----------|-------------|
| End conditions | A–A (both antinodes) | N–A (node, antinode) |
| Fundamental λ | 2L | 4L |
| Fundamental f | v/(2L) | v/(4L) |
| Harmonics | All: 1, 2, 3, 4, 5... | Odd only: 1, 3, 5, 7... |
| f₁ for same L | Higher | Lower (half of open pipe f₁) |

**Key insight:** For pipes of the same length, a closed pipe's fundamental frequency is half that of an open pipe — it sounds an octave lower.

---

## 5. End Correction (Qualitative)

In practice, the antinode at an open end is **slightly beyond** the physical end of the pipe. The vibrating air column extends a small distance past the opening.

$$L_{\text{effective}} = L_{\text{physical}} + c$$

where c ≈ 0.6 × r (r = pipe radius) for each open end.

### Effect:
- Open pipe: two end corrections (both ends), L_eff = L + 2c
- Closed pipe: one end correction (open end only), L_eff = L + c

This means:
- Actual frequencies are **slightly lower** than the simple theory predicts
- For precise work, use an effective length: measure f experimentally and calculate L_eff

The end correction is usually on the order of a few mm for typical lab pipes, so the simple formula is a good first approximation.

---

## 6. Resonance

**Resonance** occurs when a driving frequency matches a natural frequency of a system, causing large-amplitude oscillations.

In pipes:
- The air column has natural frequencies (harmonics)
- When a sound wave of matching frequency enters, a standing wave forms with large amplitude
- This is why blowing across a bottle top produces a tone — you're exciting the resonant frequency

### Resonance Tube Experiment (IB Classic)
A tuning fork is held over a tube with water. By adjusting the water level (changing L), resonance positions are found where the sound becomes loud. The distance between consecutive resonances = λ/2.

---

## Worked Examples

### Worked Example 41.1 — Fundamental of a Closed Pipe

**Problem:** A closed organ pipe (stopped at one end) is 0.85 m long. The speed of sound in air is 340 m/s. Find:
(a) the fundamental frequency
(b) the frequencies of the first two overtones

**Solution:**

**(a) Closed pipe fundamental:**
$$f_1 = \frac{v}{4L} = \frac{340}{4 \times 0.85} = \frac{340}{3.40} = 100 \text{ Hz}$$

**(b)** Closed pipes have only odd harmonics:
- 1st overtone = 3rd harmonic: f₃ = 3f₁ = 3 × 100 = **300 Hz**
- 2nd overtone = 5th harmonic: f₅ = 5f₁ = 5 × 100 = **500 Hz**

---

### Worked Example 41.2 — Open Pipe Harmonics

**Problem:** An open organ pipe produces a fundamental of 256 Hz. The speed of sound is 340 m/s. Find:
(a) the length of the pipe
(b) the frequency of the 4th harmonic

**Solution:**

**(a)** For an open pipe:
$$f_1 = \frac{v}{2L}$$
$$L = \frac{v}{2f_1} = \frac{340}{2 \times 256} = \frac{340}{512} = 0.664 \text{ m}$$

**(b)** Open pipe has all harmonics:
$$f_4 = 4f_1 = 4 \times 256 = 1024 \text{ Hz}$$

---

### Worked Example 41.3 — Finding Pipe Length for a Given Note

**Problem:** You need a closed pipe that resonates at 440 Hz (concert A). Sound speed = 340 m/s.
(a) What length should the pipe be?
(b) What are the next two possible resonant frequencies of this pipe?

**Solution:**

**(a)** For fundamental in closed pipe:
$$f_1 = \frac{v}{4L}$$
$$L = \frac{v}{4f_1} = \frac{340}{4 \times 440} = \frac{340}{1760} = 0.193 \text{ m} \approx 19.3 \text{ cm}$$

**(b)** Only odd harmonics:
f₃ = 3 × 440 = **1320 Hz**
f₅ = 5 × 440 = **2200 Hz**

---

### Worked Example 41.4 — Comparing Open and Closed Pipes

**Problem:** Two pipes have the same length of 1.00 m. One is open at both ends, the other is closed at one end. Speed of sound = 340 m/s. Compare:
(a) their fundamental frequencies
(b) the number of harmonics below 1000 Hz for each

**Solution:**

**(a)**
- Open: f₁ = v/(2L) = 340/(2×1.00) = **170 Hz**
- Closed: f₁ = v/(4L) = 340/(4×1.00) = **85.0 Hz**

The closed pipe's fundamental is half — it sounds an octave lower.

**(b)**
- **Open:** f₁=170, f₂=340, f₃=510, f₄=680, f₅=850 → **5 harmonics below 1000 Hz**
- **Closed:** f₁=85, f₃=255, f₅=425, f₇=595, f₉=765, f₁₁=935 → **6 harmonics below 1000 Hz**

---

### Worked Example 41.5 — End Correction (IB-Style)

**Problem:** A student holds a tuning fork of frequency 512 Hz over a resonance tube. The first resonance (loudest sound) occurs when the air column length is 16.2 cm. The second resonance occurs at 49.8 cm. The tube diameter is 3.0 cm.

(a) Use the difference between resonance positions to find the wavelength and speed of sound.
(b) Calculate the end correction.
(c) Compare your end correction with the theoretical value c ≈ 0.6r.

**Solution:**

**(a)** The distance between consecutive resonances in a closed pipe = λ/2:
$$\frac{\lambda}{2} = 49.8 - 16.2 = 33.6 \text{ cm}$$
$$\lambda = 67.2 \text{ cm} = 0.672 \text{ m}$$
$$v = f\lambda = 512 \times 0.672 = 344 \text{ m/s}$$

**(b)** For first resonance (n = 1): L_eff = λ/4 = 67.2/4 = 16.8 cm
Physical length L = 16.2 cm
End correction c = L_eff − L = 16.8 − 16.2 = **0.6 cm**

**(c)** Tube radius r = 3.0/2 = 1.5 cm
Theoretical: c ≈ 0.6r = 0.6 × 1.5 = **0.9 cm**
The measured 0.6 cm is reasonably close to the theoretical 0.9 cm.

---

## Practice Problems

### Problem 1
An open organ pipe is 1.20 m long. Speed of sound in air = 340 m/s.
(a) Find the fundamental frequency.
(b) List the frequencies of the first four harmonics.
(c) What is the wavelength of the 3rd harmonic?

### Problem 2
A closed pipe (stopped at one end) is 0.40 m long. Speed of sound = 340 m/s.
(a) Find the fundamental frequency.
(b) Explain why the 2nd harmonic cannot exist in this pipe.
(c) Find the frequencies of the first three harmonics that do exist.

### Problem 3
A pipe produces its 3rd harmonic at 750 Hz. The sound speed is 340 m/s.
(a) If the pipe is open at both ends, find its length.
(b) If instead the pipe is closed at one end, find its length.

### Problem 4
In a resonance tube experiment, a tuning fork of 440 Hz gives first resonance at 18.5 cm air column length, and second resonance at 57.0 cm.
(a) Determine the wavelength of the sound.
(b) Calculate the speed of sound from this data.
(c) Find the end correction.

### Problem 5 (IB-Style)
An organ pipe closed at one end has length 0.60 m and is played in a room where the temperature is such that v = 345 m/s. The pipe diameter is 4.0 cm.

(a) Calculate the fundamental frequency using the simple formula (ignoring end correction).
(b) Estimate the effective length including end correction (c ≈ 0.6r) and recalculate the fundamental.
(c) A second pipe, open at both ends, is cut so that its fundamental matches the corrected fundamental from (b). Determine its length.
(d) The temperature rises, increasing the speed of sound by 2%. Explain the effect on the pitch of both pipes — does the open or closed pipe change more in absolute terms?

---

## Answers

### Answer 1
**(a)** f₁ = v/(2L) = 340/(2 × 1.20) = **142 Hz**

**(b)** f₁ = 142 Hz, f₂ = 283 Hz, f₃ = 425 Hz, f₄ = 567 Hz

**(c)** λ₃ = v/f₃ = 340/425 = 0.800 m (or: λ₃ = 2L/3 = 0.800 m)

---

### Answer 2
**(a)** f₁ = v/(4L) = 340/(4 × 0.40) = **213 Hz**

**(b)** The 2nd harmonic would require a node at the open end or an antinode at the closed end, violating boundary conditions. Mathematically, n = 2 gives λ = 2L, which doesn't fit N–A in L.

**(c)** Only odd harmonics exist: f₁ = 213 Hz, f₃ = 638 Hz, f₅ = 1063 Hz

---

### Answer 3
**(a) Open pipe, 3rd harmonic:** f₃ = 3v/(2L) → L = 3v/(2f₃) = 3×340/(2×750) = **0.680 m**

**(b) Closed pipe, 3rd harmonic:** f₃ = 3v/(4L) → L = 3v/(4f₃) = 3×340/(4×750) = **0.340 m**

---

### Answer 4
**(a)** λ/2 = 57.0 − 18.5 = 38.5 cm → λ = **0.770 m**

**(b)** v = fλ = 440 × 0.770 = **339 m/s**

**(c)** L_eff (1st resonance) = λ/4 = 0.770/4 = 0.1925 m = 19.25 cm
c = L_eff − L = 19.25 − 18.5 = **0.75 cm**

---

### Answer 5 (IB-Style)
**(a)** f₁ = v/(4L) = 345/(4 × 0.60) = 345/2.40 = **144 Hz**

**(b)** r = 2.0 cm = 0.020 m, c ≈ 0.6 × 0.020 = 0.012 m
L_eff = L + c = 0.60 + 0.012 = 0.612 m
f₁_corrected = 345/(4 × 0.612) = 345/2.448 = **141 Hz**

**(c)** Open pipe: f₁ = v/(2L) → L = v/(2f₁) = 345/(2 × 141) = **1.22 m**

Adding end corrections (two ends): L_physical = L_eff − 2c = 1.22 − 0.024 = 1.20 m

**(d)** New v = 345 × 1.02 = 352 m/s
Both frequencies increase by 2% since f ∝ v (length unchanged). Absolute change:
- Closed: Δf = 141 × 0.02 = **2.82 Hz**
- Open: Δf = 141 × 0.02 = **2.82 Hz**
They change by the same percentage but if open pipe is longer (lower f₁), its absolute change might differ — however here the fundamentals match, so the absolute change is the same.

---

## Key Takeaways

| Concept | Open Pipe | Closed Pipe |
|---------|-----------|-------------|
| Boundary | A–A | N–A |
| λ_n | 2L/n (all n) | 4L/n (odd n only) |
| f_n | nv/(2L) | nv/(4L), n odd |
| Harmonics | All: 1,2,3,4,5... | Odd only: 1,3,5,7... |
| Fundamental | v/(2L) | v/(4L) |
| End correction | 2c (both ends) | c (open end only) |

> **IB Data Booklet:** v = fλ (Sub-topic 4.2). Pipe formulas must be derived from boundary conditions. Remember: open pipes have all harmonics (like strings); closed pipes have only odd harmonics.
