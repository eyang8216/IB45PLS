# Lesson 39: Wave Phenomena IV — Resolution and Polarisation (HL)

## What You'll Learn
- Apply the Rayleigh criterion for resolvability: $\theta = 1.22\lambda/b$
- Calculate the resolving power of a diffraction grating: $R = \lambda/\Delta\lambda = Nn$
- Use Malus's Law for polarised light: $I = I_0\cos^2\theta$
- Understand polarisation by reflection (Brewster's angle)

---

## 1. Resolution — When Two Points Become One

### 1.1 The Problem

Every optical instrument — eye, telescope, microscope — has a limit to how much detail it can see. Two stars very close together in the sky appear as one. Two tiny structures in a cell blur together. This limit comes from diffraction: when light passes through a circular aperture (lens, pupil), it diffracts, forming a fuzzy disc (Airy disc) rather than a perfect point.

### 1.2 The Rayleigh Criterion

Two point sources are said to be **just resolved** when the central maximum of one diffraction pattern falls on the first minimum of the other. For a circular aperture of diameter $b$:

$$\theta = 1.22\frac{\lambda}{b}$$

where $\theta$ is the minimum angular separation that can be resolved (in radians), $\lambda$ is the wavelength, and $b$ is the aperture diameter.

- Larger aperture → better resolution (smaller $\theta$)
- Shorter wavelength → better resolution
- The factor $1.22$ comes from the mathematics of circular apertures

### 1.3 Resolving Power of a Grating

For a diffraction grating, the ability to separate two close wavelengths is:

$$R = \frac{\lambda}{\Delta\lambda} = Nn$$

where $N$ is the total number of lines (slits) illuminated and $n$ is the order. More lines and higher orders give better wavelength resolution.

---

## 2. Polarisation — Light Has an Orientation

### 2.1 What Is Polarisation?

Unpolarised light (from the Sun, a light bulb) has electric field oscillations in ALL directions perpendicular to the direction of travel. **Polarised light** has oscillations restricted to a single plane. Only TRANSVERSE waves can be polarised — this is evidence that light is a transverse electromagnetic wave. (Sound, being longitudinal, cannot be polarised.)

### 2.2 Polarisation by Filter (Polaroid)

A Polaroid filter transmits only the component of the electric field parallel to its transmission axis. For unpolarised light passing through one polariser, the intensity is halved: $I = I_0/2$.

### 2.3 Malus's Law

When already-polarised light passes through a second polariser (analyser) at angle $\theta$ to the polarisation direction:

$$I = I_0\cos^2\theta$$

- $\theta = 0^\circ$ (axes aligned): $I = I_0$ (full transmission)
- $\theta = 90^\circ$ (crossed): $I = 0$ (complete extinction)
- $\theta = 45^\circ$: $I = I_0/2$

### 2.4 Polarisation by Reflection — Brewster's Angle

When unpolarised light reflects from a surface, the reflected light is partially polarised. At a specific angle — **Brewster's angle** — the reflected light is COMPLETELY polarised parallel to the surface:

$$\tan\theta_B = n$$

where $n$ is the refractive index of the reflecting medium. At Brewster's angle, the reflected and refracted rays are perpendicular ($\theta_B + \theta_r = 90^\circ$). Polaroid sunglasses use this principle to reduce glare from horizontal surfaces (water, roads).

---

## Worked Examples

### Worked Example 39.1 — Telescope Resolution

**Problem:** A telescope has a $5.0\text{ m}$ diameter mirror. Using light of $550\text{ nm}$, find the minimum angular separation of two stars that can just be resolved.

**Solution:**
$\theta = 1.22\lambda/b = 1.22(550\times 10^{-9})/5.0 = 1.34 \times 10^{-7}\text{ rad}$ (about $0.028$ arcseconds).

---

### Worked Example 39.2 — Malus's Law

**Problem:** Unpolarised light of intensity $80\text{ W m}^{-2}$ passes through two polarisers with axes at $30^\circ$. Find the transmitted intensity.

**Solution:**
After first polariser: $I_1 = 80/2 = 40\text{ W m}^{-2}$.
After second: $I_2 = 40\cos^2 30^\circ = 40 \times 0.75 = 30\text{ W m}^{-2}$.

---

### Worked Example 39.3 — Brewster's Angle

**Problem:** Find Brewster's angle for light reflecting from water ($n = 1.33$).

**Solution:**
$\theta_B = \tan^{-1}(1.33) = 53.1^\circ$. At this angle, reflected light is fully polarised parallel to the water surface.

---

## Practice Problems

### Problem 1
The human pupil is about $5.0\text{ mm}$ in diameter. Using $\lambda = 550\text{ nm}$, find the minimum angular separation the eye can resolve. At $10\text{ m}$ distance, what is the minimum separation between two points that can be distinguished?

### Problem 2
A diffraction grating with $5,000$ lines illuminated is used in second order. Find the resolving power. Can it resolve two lines at $600.00\text{ nm}$ and $600.06\text{ nm}$?

### Problem 3
Unpolarised light of intensity $I_0$ passes through two polarisers at $60^\circ$. Express the transmitted intensity as a fraction of $I_0$.

### Problem 4
Calculate Brewster's angle for glass ($n = 1.55$). Explain why Polaroid sunglasses are effective at reducing glare from horizontal surfaces.

### Problem 5 — IB-Style
(a) Explain why two stars that are very close together in the sky may appear as a single star when viewed through a small telescope. (2 marks)
(b) A telescope with aperture $0.30\text{ m}$ observes light of wavelength $600\text{ nm}$. Calculate the minimum angular separation it can resolve. (2 marks)
(c) The telescope is replaced with one having a $1.2\text{ m}$ aperture. By what factor does the resolution improve? (1 mark)
(d) Unpolarised light passes through a polariser and then through an analyser at $45^\circ$ to the first. The transmitted intensity is $25\text{ W m}^{-2}$. Determine the intensity of the original unpolarised light. (3 marks)

---

## Answers

### Answer 1
$\theta = 1.22(550\times 10^{-9})/(5.0\times 10^{-3}) = 1.34 \times 10^{-4}\text{ rad}$. At $10\text{ m}$: $y = 10 \times 1.34\times 10^{-4} = 1.34\text{ mm}$.

### Answer 2
$R = Nn = 5,000 \times 2 = 10,000$. $\lambda/\Delta\lambda = 600/0.06 = 10,000$. Required $R = 10,000$ = available $R$ — just resolvable (by the Rayleigh criterion).

### Answer 3
$I_1 = I_0/2$. $I_2 = (I_0/2)\cos^2 60^\circ = (I_0/2)(0.25) = I_0/8$.

### Answer 4
$\theta_B = \tan^{-1}(1.55) = 57.2^\circ$. Sunlight reflecting from horizontal surfaces (water, wet roads) arrives at angles near Brewster's angle and is strongly polarised horizontally. Polaroid sunglasses have vertically-oriented transmission axes, blocking this horizontally-polarised glare.

### Answer 5 — IB-Style
**(a)** (2 marks) Light from each star diffracts at the telescope aperture, forming Airy disc patterns. If the angular separation is less than the Rayleigh criterion ($\theta < 1.22\lambda/b$), the central maxima overlap and the stars cannot be distinguished — they appear as a single point.

**(b)** (2 marks) $\theta = 1.22(600\times 10^{-9})/0.30 = 2.44 \times 10^{-6}\text{ rad}$.

**(c)** (1 mark) Aperture quadrupled → $\theta$ divided by 4. Resolution improves by factor of 4.

**(d)** (3 marks) After analyser: $25 = I_0/2 \times \cos^2 45^\circ = I_0/2 \times 0.5 = I_0/4$. So $I_0 = 100\text{ W m}^{-2}$. (1 mark for halving at first polariser, 1 for Malus's Law, 1 for answer.)

---

## Key Takeaways

1. **Rayleigh criterion:** $\theta = 1.22\lambda/b$. Smaller $\theta$ = better resolution. Larger aperture or shorter wavelength helps.

2. **Grating resolving power:** $R = \lambda/\Delta\lambda = Nn$. More lines, higher order → better separation.

3. **Malus's Law:** $I = I_0\cos^2\theta$. Crossed polarisers ($90^\circ$) give zero transmission. Unpolarised light halves at first polariser.

4. **Brewster's angle:** $\tan\theta_B = n$. Reflected light fully polarised. Used in Polaroid sunglasses and photography.
