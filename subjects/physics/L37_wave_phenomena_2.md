# Lesson 37: Wave Phenomena II — Single-Slit Diffraction and Gratings (HL)

## What You'll Learn
- Calculate the position of the first minimum in single-slit diffraction: $\theta \approx \lambda/b$
- Explain why the central maximum is twice as wide as side maxima
- Use the diffraction grating equation $n\lambda = d\sin\theta$
- Determine wavelengths and grating spacing from diffraction patterns

---

## 1. Single-Slit Diffraction — When One Slit Is Enough

### 1.1 What Happens

Shine monochromatic light through a single narrow slit. Instead of a single bright line on the screen (as ray optics would predict), you see a pattern: a wide, bright central maximum flanked by narrower, dimmer side maxima, separated by dark minima. This is single-slit diffraction.

### 1.2 The First Minimum

The first dark fringe (minimum) occurs at an angle $\theta$ given by:

$$\theta \approx \frac{\lambda}{b}$$

where $b$ is the slit width. This is the small-angle approximation ($\sin\theta \approx \theta$ in radians). More precisely: $b\sin\theta = \lambda$ for the first minimum.

The central maximum extends from $\theta = -\lambda/b$ to $\theta = +\lambda/b$, so its angular width is $2\lambda/b$ — twice the width of the side maxima.

### 1.3 Why Does Diffraction Happen?

Huygens' principle: every point across the slit acts as a source of wavelets. When the path difference between wavelets from opposite edges of the slit equals $\lambda$, the wavelets from the top half of the slit cancel with those from the bottom half — producing the first dark fringe. For $b\sin\theta = n\lambda$ ($n = 1, 2, 3\dots$), we get minima.

### 1.4 Effect of Slit Width

- Narrower slit ($b$ small) → wider diffraction pattern ($\theta$ large)
- Wider slit ($b$ large) → narrower pattern ($\theta$ small)
- When $b \gg \lambda$: diffraction negligible — light travels in straight lines (ray optics)

---

## 2. Diffraction Gratings — Many Slits, Sharp Lines

### 2.1 What a Grating Is

A diffraction grating consists of many parallel, equally spaced slits (or grooves). Commercial gratings have hundreds or thousands of lines per millimetre. The grating spacing $d$ is the distance between adjacent slits: $d = 1/N$ where $N$ is lines per metre.

### 2.2 The Grating Equation

For a transmission grating, bright maxima occur at angles $\theta_n$ where:

$$n\lambda = d\sin\theta_n$$

- $n = 0, \pm 1, \pm 2, \dots$ is the order number
- $n = 0$ gives the central maximum (all wavelengths overlap — white for white light)
- Higher orders: red light (longer $\lambda$) appears at larger angles than blue

### 2.3 Why Gratings Are Better Than Double Slits

A grating produces much sharper, brighter maxima than Young's double slit because:
- Many slits (not just two) contribute to each maximum
- Maxima are very narrow — the angular width decreases as the number of slits increases
- This allows precise wavelength measurements

### 2.4 Maximum Order

Since $\sin\theta \leq 1$, the maximum observable order is $n_{\text{max}} = d/\lambda$ (rounded down). If $d < \lambda$, only $n = 0$ appears.

---

## 3. Comparing Single-Slit, Double-Slit, and Grating Patterns

| Feature | Single Slit | Double Slit | Grating |
|---------|------------|-------------|---------|
| Central maximum | Wide ($2\lambda/b$) | Same width as others | Very narrow |
| Fringe spacing | Unequal (central wider) | Equal ($s = \lambda D/d$) | Equal |
| Intensity | Bright central, dim sides | Equal bright fringes | Very sharp bright lines |
| Number of slits | 1 | 2 | Many (hundreds+) |

---

## Worked Examples

### Worked Example 37.1 — Single-Slit Minimum

**Problem:** Light of wavelength $600\text{ nm}$ passes through a slit $0.20\text{ mm}$ wide. The screen is $1.5\text{ m}$ away. Find the distance from the centre to the first dark fringe.

**Solution:**
$\theta \approx \lambda/b = 600\times 10^{-9}/(0.20\times 10^{-3}) = 3.0 \times 10^{-3}\text{ rad}$. Distance $y = D\theta = 1.5 \times 3.0\times 10^{-3} = 4.5\text{ mm}$. Central maximum width: $2 \times 4.5 = 9.0\text{ mm}$.

---

### Worked Example 37.2 — Grating Wavelength

**Problem:** A grating with 400 lines per mm produces a first-order maximum at $14.5^\circ$. Find the wavelength.

**Solution:**
$d = 1/(400\times 10^3) = 2.50 \times 10^{-6}\text{ m}$. $\lambda = d\sin\theta = (2.50\times 10^{-6})\sin 14.5^\circ = 6.25 \times 10^{-7}\text{ m} = 625\text{ nm}$.

---

### Worked Example 37.3 — Maximum Order

**Problem:** A grating with 600 lines/mm is illuminated with light of wavelength $500\text{ nm}$. What is the highest observable order?

**Solution:**
$d = 1/(600\times 10^3) = 1.667 \times 10^{-6}\text{ m}$. $n_{\text{max}} = d/\lambda = 1.667\times 10^{-6}/500\times 10^{-9} = 3.33$. Only $n = 0, 1, 2, 3$ are observable (order 3 appears at $\sin\theta = 3(500)/1667 = 0.90$, $\theta = 64^\circ$). $n = 4$ would require $\sin\theta > 1$.

---

## Practice Problems

### Problem 1
Light of $550\text{ nm}$ falls on a single slit of width $0.15\text{ mm}$. Find the angular width of the central maximum.

### Problem 2
A grating with 500 lines/mm produces a second-order maximum at $36.9^\circ$. Find the wavelength.

### Problem 3
A grating with 300 lines/mm is illuminated by light containing two wavelengths: $400\text{ nm}$ and $700\text{ nm}$. Find the angular separation between the first-order maxima for these wavelengths.

### Problem 4
Explain why a CD or DVD acts as a reflection diffraction grating, producing rainbow colours.

### Problem 5 — IB-Style
A student uses a grating with $250\text{ lines per mm}$ and a laser of unknown wavelength. The distance from grating to screen is $1.20\text{ m}$.

(a) Calculate the grating spacing $d$. (1 mark)
(b) The first-order bright spot appears $18.5\text{ cm}$ from the central spot. Calculate $\theta_1$ and the laser wavelength. (3 marks)
(c) Determine the highest order visible for this wavelength. (2 marks)
(d) The student replaces the laser with white light. Describe the appearance of the pattern. (2 marks)

---

## Answers

### Answer 1
$\theta \approx \lambda/b = 550\times 10^{-9}/(0.15\times 10^{-3}) = 3.67\times 10^{-3}\text{ rad}$. Central maximum angular width = $2\theta = 7.33\times 10^{-3}\text{ rad} \approx 0.42^\circ$.

### Answer 2
$d = 1/(500\times 10^3) = 2.0\times 10^{-6}\text{ m}$. $\lambda = d\sin\theta/n = (2.0\times 10^{-6})\sin 36.9^\circ/2 = 6.0\times 10^{-7}\text{ m} = 600\text{ nm}$.

### Answer 3
$d = 1/(300\times 10^3) = 3.33\times 10^{-6}\text{ m}$. $\theta_{400} = \sin^{-1}(400\times 10^{-9}/3.33\times 10^{-6}) = 6.90^\circ$. $\theta_{700} = \sin^{-1}(700\times 10^{-9}/3.33\times 10^{-6}) = 12.1^\circ$. Separation = $5.2^\circ$.

### Answer 4
CD/DVD surfaces have microscopic spiral grooves (pits) spaced at regular intervals (~1.6 μm for CD). These act as a reflection grating. Different wavelengths are reflected at different angles ($n\lambda = d\sin\theta$), separating white light into its component colours — visible as rainbow patterns when the disc is tilted in light.

### Answer 5 — IB-Style
**(a)** $d = 1/(250,000) = 4.00 \times 10^{-6}\text{ m}$. (1 mark)
**(b)** $\tan\theta_1 = 0.185/1.20 = 0.154$, $\theta_1 = 8.77^\circ$. $\lambda = d\sin\theta_1 = (4.00\times 10^{-6})\sin 8.77^\circ = 6.10\times 10^{-7}\text{ m} = 610\text{ nm}$. (3 marks)
**(c)** $n_{\text{max}} = d/\lambda = 4.00\times 10^{-6}/610\times 10^{-9} = 6.56$. Orders $0, 1, 2, 3, 4, 5, 6$. Highest = 6. (2 marks)
**(d)** (2 marks) Central maximum ($n=0$) is white — all wavelengths overlap at $\theta=0$. For $n \geq 1$, each wavelength appears at a different angle ($\sin\theta = n\lambda/d$), producing continuous spectra (rainbow bands). Red appears at larger angles; blue at smaller angles. Higher orders may overlap (e.g., blue in order 3 may coincide with red in order 2).

---

## Key Takeaways

1. **Single slit:** $\theta \approx \lambda/b$ for first minimum. Central max is twice as wide as side maxima.

2. **Grating:** $n\lambda = d\sin\theta$. Sharp, bright maxima. $d = 1/N$ where $N$ = lines per metre.

3. **Maximum order:** $n_{\text{max}} = \lfloor d/\lambda \rfloor$. Limited by $\sin\theta \leq 1$.

4. **Gratings separate wavelengths** — used in spectrometers. Longer $\lambda$ → larger angle.
