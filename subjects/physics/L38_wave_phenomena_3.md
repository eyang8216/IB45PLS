# Lesson 38: Wave Phenomena III — Thin-Film Interference (HL)

## What You'll Learn
- Explain thin-film interference using phase changes on reflection
- Determine whether reflected light undergoes a $\pi$ phase shift based on refractive indices
- Calculate film thickness for constructive and destructive interference
- Apply to soap bubbles, oil films, and anti-reflection coatings

---

## 1. What Is Thin-Film Interference?

### 1.1 The Colours of Soap Bubbles

A soap bubble or an oil slick on water displays vivid colours. These are NOT from pigments — they are from interference. Light reflects from BOTH the top surface AND the bottom surface of the thin film. The two reflected waves overlap and interfere. Whether they interfere constructively or destructively depends on the film thickness and the wavelength.

### 1.2 Why Thickness Matters

The wave reflecting from the bottom surface travels an extra distance of approximately $2t$ (down and back up through the film, where $t$ is the film thickness). If this path difference equals a whole number of wavelengths IN THE FILM, the two waves arrive in phase and reinforce (bright reflection). If it equals a half-integer number, they cancel (dark reflection).

But there is an additional complication: phase changes on reflection.

---

## 2. Phase Change on Reflection

### 2.1 The Rule

When light reflects from a medium with a HIGHER refractive index, the reflected wave undergoes a phase change of $\pi$ radians ($180^\circ$) — equivalent to an extra path difference of $\lambda/2$. When light reflects from a LOWER refractive index, there is NO phase change.

**Memory aid:** "High to low, let it go. Low to high, phase shift by $\pi$."

### 2.2 How Many Phase Changes?

For a thin film (refractive index $n_f$) between two media:
- **Air-film-air** (soap bubble): Reflection at air→film (low→high): $\pi$ shift. Reflection at film→air (high→low): NO shift. Net: ONE $\pi$ shift.
- **Air-film-glass** (anti-reflection coating, $n_{\text{air}} < n_f < n_{\text{glass}}$): BOTH reflections are low→high. Net: TWO $\pi$ shifts, which cancel (equivalent to zero net shift).

The net number of $\pi$ shifts (0, 1, or 2) determines whether you add $\lambda/2$ to the path difference.

---

## 3. Conditions for Interference

### 3.1 Near-Normal Incidence

For light incident nearly perpendicularly, the path difference between the two reflected rays is $2n_f t$ (the optical path — extra distance × refractive index of the film).

**Constructive interference (bright reflection):**
$$2n_f t = m\lambda \quad (m = 0, 1, 2, \dots) \quad \text{if ZERO or TWO } \pi \text{ shifts}$$
$$2n_f t = \left(m + \frac{1}{2}\right)\lambda \quad (m = 0, 1, 2, \dots) \quad \text{if ONE } \pi \text{ shift}$$

**Destructive interference (dark/no reflection):**
Swap the formulas above.

### 3.2 Physical Meaning

For a soap bubble (one $\pi$ shift): the thinnest films ($t \approx 0$) give DESTRUCTIVE interference — the bubble appears dark/transparent at its thinnest point. As thickness increases, different colours satisfy the constructive condition, producing the rainbow patterns.

---

## 4. Applications

### 4.1 Anti-Reflection Coatings

Camera lenses and glasses have thin coatings ($n_{\text{coating}} < n_{\text{glass}}$). With both reflections having $\pi$ shifts (cancelling), the destructive condition for reflected light is $2nt = \lambda/2$, or $t = \lambda/(4n)$. For green light ($550\text{ nm}$) with $n = 1.38$: $t = 550/(4 \times 1.38) = 100\text{ nm}$. The coating eliminates reflection for green (the eye's most sensitive colour), making the lens appear slightly purple (red and blue still partially reflected).

### 4.2 Soap Bubbles and Oil Films

The varying thickness of a soap film or oil slick means different colours satisfy the constructive condition at different points, creating the characteristic rainbow patterns.

---

## Worked Examples

### Worked Example 38.1 — Anti-Reflection Coating

**Problem:** A glass lens ($n = 1.55$) is coated with a thin film ($n = 1.38$). Find the minimum thickness for destructive interference of reflected green light ($\lambda = 550\text{ nm}$ in vacuum) at normal incidence.

**Approach:** Air ($n=1$) → coating ($n=1.38$): $\pi$ shift. Coating ($n=1.38$) → glass ($n=1.55$): $\pi$ shift. Two $\pi$ shifts cancel → use $2nt = (m + 1/2)\lambda$ for destructive (dark reflection). Minimum: $m = 0$.

**Solution:**
$2nt = \lambda/2$, so $t = \lambda/(4n) = 550/(4 \times 1.38) = 99.6\text{ nm} \approx 100\text{ nm}$.

---

### Worked Example 38.2 — Soap Film

**Problem:** A soap film ($n = 1.33$) in air appears red ($\lambda = 650\text{ nm}$) in reflected light at normal incidence. Find the minimum thickness.

**Approach:** Air→film: $\pi$ shift. Film→air: no shift. ONE net $\pi$ shift. Constructive condition: $2nt = (m + 1/2)\lambda$. Minimum: $m = 0$.

**Solution:**
$2(1.33)t = 650/2$, $t = 650/(4 \times 1.33) = 122\text{ nm}$.

---

## Practice Problems

### Problem 1
Determine the number of $\pi$ phase changes for: (a) a soap film in air, (b) an oil film ($n=1.45$) on water ($n=1.33$), (c) a coating ($n=1.50$) on glass ($n=1.70$).

### Problem 2
A soap film ($n=1.35$) in air has thickness $300\text{ nm}$. For visible light ($400-700\text{ nm}$), which wavelengths experience constructive interference in reflection?

### Problem 3
An anti-reflection coating ($n=1.40$) on glass ($n=1.60$) is designed to eliminate reflection at $500\text{ nm}$. Calculate the minimum thickness.

### Problem 4
Explain why the centre of a soap bubble appears black just before it bursts.

### Problem 5 — IB-Style
A thin film of oil ($n = 1.48$) floats on water ($n = 1.33$). White light is incident nearly perpendicularly.

(a) Determine how many $\pi$ phase changes occur and state the condition for constructive interference in reflected light. (2 marks)
(b) The film appears blue ($480\text{ nm}$) at normal incidence. Calculate the minimum film thickness. (2 marks)
(c) At a different location, the film thickness is $240\text{ nm}$. Determine which visible wavelength(s) are most strongly reflected. (3 marks)
(d) Explain why the film shows different colours at different locations. (1 mark)

---

## Answers

### Answer 1
(a) Air→film: $\pi$ shift. Film→air: no shift. Net: 1 shift.
(b) Air→oil ($1<1.45$): $\pi$. Oil→water ($1.45>1.33$): no shift. Net: 1 shift.
(c) Air→coating ($1<1.50$): $\pi$. Coating→glass ($1.50<1.70$): $\pi$. Net: 2 shifts (cancel).

### Answer 2
One $\pi$ shift → constructive: $2nt = (m+1/2)\lambda$. $2(1.35)(300) = 810\text{ nm} = (m+0.5)\lambda$. $\lambda = 810/(m+0.5)$. For $m=0$: $1,620\text{ nm}$ (IR). $m=1$: $540\text{ nm}$ (green). $m=2$: $324\text{ nm}$ (UV). Only $540\text{ nm}$ is visible.

### Answer 3
Two $\pi$ shifts → destructive: $2nt = (m+1/2)\lambda$. Minimum $m=0$: $t = \lambda/(4n) = 500/(4 \times 1.40) = 89.3\text{ nm}$.

### Answer 4
At the thinnest point, $t \approx 0$. With one net $\pi$ shift, the path difference approaches zero but the $\pi$ phase change remains, giving destructive interference — the reflected waves cancel. The film appears black because no light is reflected at that point. This is visible just before the film ruptures.

### Answer 5 — IB-Style
**(a)** (2 marks) Air→oil ($1<1.48$): $\pi$. Oil→water ($1.48>1.33$): no $\pi$. Net: 1 shift. Constructive: $2nt = (m+1/2)\lambda$, $m=0,1,2\dots$.

**(b)** (2 marks) $2(1.48)t = (0+0.5)(480)$. $t = 240/(2.96) = 81.1\text{ nm}$.

**(c)** (3 marks) $\lambda = 2nt/(m+0.5) = 2(1.48)(240)/(m+0.5) = 710.4/(m+0.5)$. $m=0$: $1,421\text{ nm}$ (IR). $m=1$: $473.6\text{ nm}$ (blue). $m=2$: $284\text{ nm}$ (UV). Strongest visible = $474\text{ nm}$ (blue-violet).

**(d)** (1 mark) Film thickness varies across the surface due to gravity and surface tension. Different thicknesses satisfy the constructive condition for different wavelengths, producing the coloured pattern.

---

## Key Takeaways

1. **Phase change on reflection:** Reflection from higher $n$ → $\pi$ shift. From lower $n$ → no shift.

2. **Path difference:** $2nt$ (optical path). Add $\lambda/2$ for each net $\pi$ shift.

3. **Soap film (one $\pi$ shift):** Thinnest films appear black (destructive). Thicker = colours.

4. **Anti-reflection coating (two $\pi$ shifts cancel):** $t = \lambda/(4n)$ for destructive reflection.
