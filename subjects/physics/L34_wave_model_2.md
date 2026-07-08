# Lesson 34: Wave Model II — Reflection, Refraction and Snell's Law

## What You'll Learn

By the end of this lesson, you will be able to:
- Predict the path of a wave reflecting from a surface using the law of reflection
- Use Snell's Law to calculate angles of refraction when waves cross a boundary between media
- Explain why waves change direction at boundaries in terms of changing wave speed
- Calculate critical angles and predict when total internal reflection occurs
- Apply these principles to optical fibres and other real-world applications

---

## 1. What Happens When a Wave Meets a Boundary?

### 1.1 Why This Matters

A wave travelling through a medium will eventually encounter a boundary — the interface between two different materials. What happens at that boundary depends on the properties of both materials. The wave might bounce back (reflection), pass through but change direction (refraction), or in some cases, be completely trapped inside the original material (total internal reflection).

These three phenomena are not separate topics — they are different outcomes of the same underlying physics: a change in wave speed at the boundary. Understanding reflection and refraction is essential for optics (lenses, mirrors, cameras), communications (optical fibres carrying internet data), medical imaging (endoscopes), and even seismology (earthquake waves bending through the Earth's interior).

### 1.2 The Common Thread — Wave Speed Changes

Every wave has a natural speed in a given medium. Light travels at $3.00 \times 10^8\text{ m s}^{-1}$ in a vacuum but slows to about $2.25 \times 10^8\text{ m s}^{-1}$ in water and about $2.00 \times 10^8\text{ m s}^{-1}$ in glass. Sound travels faster in water than in air. When a wave crosses from one medium to another where its speed is different, its direction changes — unless it strikes the boundary head-on. This change of direction is called refraction.

**A critical point about frequency:** When a wave crosses a boundary, its frequency does NOT change. The frequency is determined by whatever created the wave (the source). What changes is the speed and therefore the wavelength ($\lambda = v/f$). If the speed decreases, the wavelength decreases by the same factor. This is why a blue light source still looks blue whether you view it through air, water, or glass — the frequency (which determines colour) is unchanged.

---

## 2. Reflection

### 2.1 The Law of Reflection

When a wave strikes a smooth surface and bounces back, the angle at which it approaches equals the angle at which it leaves. This is the law of reflection:

$$\theta_i = \theta_r$$

where $\theta_i$ is the angle of incidence and $\theta_r$ is the angle of reflection. Both angles are measured between the ray and the **normal** — an imaginary line perpendicular to the surface at the point where the ray strikes.

There are three key things to remember about this law:

First, it works for all types of waves — light, sound, water waves, seismic waves. The physics of reflection does not depend on what kind of wave you are dealing with.

Second, the incident ray, the reflected ray, and the normal all lie in the same plane. You cannot have a ray come in from one plane and reflect out into a different plane.

Third, the law of reflection assumes a smooth surface. A rough surface scatters waves in many directions (diffuse reflection), which is why you can see a piece of paper from any angle but you can only see your reflection in a mirror from one specific angle.

### 2.2 Specular vs. Diffuse Reflection

A mirror produces specular reflection: parallel incident rays remain parallel after reflection. This happens because the surface is smooth at the scale of the wavelength. A piece of paper produces diffuse reflection: parallel incident rays scatter in all directions because the surface is rough at the scale of the wavelength. Both obey the law of reflection at the microscopic level — each individual ray reflects with $\theta_i = \theta_r$ relative to the local surface orientation, but since the surface orientation varies randomly, the reflected rays go in random directions.

---

## 3. Refraction — Why Waves Bend

### 3.1 The Physical Reason for Bending

Imagine a line of soldiers marching across a field. They approach a muddy patch at an angle. The first soldier to hit the mud slows down. A moment later, the next soldier hits the mud and also slows. The result: the whole line pivots — it changes direction. The side that hits the slow medium first gets delayed relative to the side still in the fast medium, causing the entire wavefront to rotate.

This is exactly what happens to a wave. When a wavefront approaches a boundary at an angle, one side of the wavefront enters the new medium first and changes speed while the other side is still in the original medium. This speed difference across the wavefront causes it to change direction.

If the wave slows down (entering a medium with higher refractive index), the wavefront bends toward the normal. If the wave speeds up (entering a medium with lower refractive index), the wavefront bends away from the normal.

### 3.2 Refractive Index

The refractive index $n$ of a medium quantifies how much light slows down in that medium compared to its speed in a vacuum:

$$n = \frac{c}{v}$$

where $c = 3.00 \times 10^8\text{ m s}^{-1}$ is the speed of light in a vacuum and $v$ is the speed of light in the medium. Since light always travels slower in a material than in a vacuum, $n$ is always greater than 1 for any material medium. A vacuum has $n = 1$ exactly.

Common values of refractive index:

| Medium | Refractive Index $n$ |
|--------|---------------------|
| Vacuum | 1.00 |
| Air | 1.0003 (≈ 1.00 for IB purposes) |
| Water | 1.33 |
| Crown glass | 1.50–1.55 |
| Diamond | 2.42 |

A higher refractive index means light travels more slowly in that medium, and the medium is said to be "optically denser." Note that optical density is NOT the same as physical density — it refers specifically to the effect on light speed.

### 3.3 Snell's Law

Snell's Law quantifies the relationship between the angles and the refractive indices when a wave crosses a boundary:

$$n_1 \sin\theta_1 = n_2 \sin\theta_2$$

where:
- $n_1$ and $n_2$ are the refractive indices of the first and second media
- $\theta_1$ is the angle of incidence (in medium 1, measured from the normal)
- $\theta_2$ is the angle of refraction (in medium 2, measured from the normal)

This formula is in the IB Data Booklet. When using it, always measure angles from the normal, never from the surface.

**How to reason about Snell's Law without calculating:**

If $n_2 > n_1$ (light enters a slower medium): $\sin\theta_2 < \sin\theta_1$, so $\theta_2 < \theta_1$. The ray bends TOWARD the normal.

If $n_2 < n_1$ (light enters a faster medium): $\sin\theta_2 > \sin\theta_1$, so $\theta_2 > \theta_1$. The ray bends AWAY from the normal.

### 3.4 A Common Misconception

Many students think that light always bends toward the normal when entering a new medium. This is only true when entering a medium with a HIGHER refractive index (slower speed). When light enters a medium with a LOWER refractive index (faster speed), it bends AWAY from the normal. The direction of bending is determined by whether the speed increases or decreases, not by the mere fact of crossing a boundary.

---

## 4. Total Internal Reflection

### 4.1 What It Is

When light travels from a medium with a higher refractive index to one with a lower refractive index (for example, from glass to air), it bends away from the normal. As the angle of incidence increases, the angle of refraction increases faster. At some critical angle of incidence, the angle of refraction reaches $90^\circ$ — the refracted ray skims along the boundary. For any angle of incidence larger than this critical angle, Snell's Law would predict $\sin\theta_2 > 1$, which is mathematically impossible. What actually happens is that no light is transmitted at all — it is all reflected back into the original medium. This is total internal reflection (TIR).

### 4.2 The Critical Angle

The critical angle $\theta_c$ is the angle of incidence for which the angle of refraction is $90^\circ$. Setting $\theta_2 = 90^\circ$ in Snell's Law:

$$n_1 \sin\theta_c = n_2 \sin 90^\circ$$
$$n_1 \sin\theta_c = n_2$$
$$\sin\theta_c = \frac{n_2}{n_1}$$

For the common case of light travelling from a medium into air ($n_2 \approx 1.00$):

$$\sin\theta_c = \frac{1}{n_1}$$

**Total internal reflection occurs when:**
1. Light is travelling from a medium with a higher refractive index to one with a lower refractive index ($n_1 > n_2$). You cannot get TIR going from air to glass.
2. The angle of incidence is greater than the critical angle ($\theta_1 > \theta_c$).

### 4.3 Why TIR Is "Total"

In ordinary reflection from a mirror, some light is always absorbed or transmitted — even the best mirrors reflect only 90–95% of incident light. Total internal reflection is called "total" because literally 100% of the incident light is reflected. No energy is lost to transmission. This makes TIR extremely efficient, which is why it is used in optical fibres for telecommunications.

---

## 5. Applications

### 5.1 Optical Fibres

An optical fibre consists of a thin glass core surrounded by a glass cladding with a slightly lower refractive index. Light entering the fibre at an angle shallower than the acceptance angle undergoes repeated total internal reflection at the core-cladding boundary and is guided along the fibre with minimal loss. Optical fibres carry internet data, telephone calls, and cable television signals across oceans. They also enable medical endoscopes that allow doctors to see inside the body without surgery.

### 5.2 Prisms and Periscopes

A 45°–45°–90° glass prism uses total internal reflection to reflect light through 90° or 180° with near-perfect efficiency. Binoculars and some periscopes use prisms rather than mirrors because TIR reflects more light and does not tarnish or degrade over time.

### 5.3 Diamond's Sparkle

Diamonds have an exceptionally high refractive index ($n = 2.42$), which gives them a very small critical angle (about $24.4^\circ$). Light entering a diamond undergoes multiple total internal reflections before escaping, which creates the characteristic sparkle. The diamond's cut is designed to maximise the number of TIR events.

---

## Worked Examples

### Worked Example 34.1 — Basic Snell's Law

**Problem:** Light travelling in air strikes a flat surface of glass ($n = 1.50$) at an angle of incidence of $40^\circ$ measured from the normal. Calculate the angle of refraction inside the glass. The refractive index of air is 1.00.

**Approach:** Use Snell's Law. We know $n_1 = 1.00$, $\theta_1 = 40^\circ$, $n_2 = 1.50$, and we need $\theta_2$.

**Solution:**
$$n_1 \sin\theta_1 = n_2 \sin\theta_2$$
$$1.00 \times \sin 40^\circ = 1.50 \times \sin\theta_2$$
$$\sin\theta_2 = \frac{\sin 40^\circ}{1.50} = \frac{0.643}{1.50} = 0.429$$
$$\theta_2 = \sin^{-1}(0.429) = 25.4^\circ$$

**Why this makes sense:** Glass has a higher refractive index than air (1.50 > 1.00), so light slows down and bends TOWARD the normal. The angle decreases from $40^\circ$ to $25.4^\circ$, which is toward the normal, confirming this expectation.

---

### Worked Example 34.2 — Light Leaving Glass into Air

**Problem:** A light ray inside glass ($n = 1.50$) strikes the glass-air boundary at an angle of $25^\circ$ from the normal. Calculate the angle at which it emerges into the air.

**Approach:** This time light is going from glass ($n_1 = 1.50$) to air ($n_2 = 1.00$). Light speeds up, so it bends away from the normal.

**Solution:**
$$1.50 \times \sin 25^\circ = 1.00 \times \sin\theta_2$$
$$\sin\theta_2 = 1.50 \times \sin 25^\circ = 1.50 \times 0.423 = 0.634$$
$$\theta_2 = \sin^{-1}(0.634) = 39.3^\circ$$

**Why this makes sense:** Going from glass to air, the angle increases from $25^\circ$ to $39.3^\circ$ — the ray bends away from the normal, as expected when speeding up.

---

### Worked Example 34.3 — Critical Angle

**Problem:** Calculate the critical angle for light travelling from glass ($n = 1.50$) into air ($n = 1.00$). If a ray inside the glass strikes the boundary at $50^\circ$, will total internal reflection occur?

**Approach:** Use $\sin\theta_c = n_2/n_1$, then compare the given angle to the critical angle.

**Solution:**
$$\sin\theta_c = \frac{1.00}{1.50} = 0.667$$
$$\theta_c = \sin^{-1}(0.667) = 41.8^\circ$$

The ray strikes at $50^\circ$, which is greater than $41.8^\circ$. Therefore total internal reflection occurs — no light is transmitted into the air.

**Why this makes sense:** The critical angle for glass-to-air is about $42^\circ$. Any ray approaching the boundary at a steeper angle than this is completely reflected. This is a relatively small critical angle, which is why TIR is easy to achieve with glass.

---

### Worked Example 34.4 — Optical Fibre Acceptance Angle (IB-Style)

**Problem:** An optical fibre has a core with refractive index $n_1 = 1.62$ and a cladding with refractive index $n_2 = 1.52$. A light ray enters the fibre from air ($n_0 = 1.00$). Calculate: (a) the critical angle at the core-cladding boundary, and (b) the maximum angle of incidence at the entrance face for which the ray will be guided by total internal reflection.

**Approach:** The critical angle at the core-cladding boundary determines the minimum angle a ray must make with the boundary to undergo TIR. This translates to a maximum acceptance angle at the entrance via Snell's Law.

**Solution (a):**
$$\sin\theta_c = \frac{n_2}{n_1} = \frac{1.52}{1.62} = 0.938$$
$$\theta_c = \sin^{-1}(0.938) = 69.8^\circ$$

This means a ray inside the core must strike the cladding at an angle greater than $69.8^\circ$ (measured from the normal) for TIR. In terms of the angle with the fibre axis, the ray must be within $90^\circ - 69.8^\circ = 20.2^\circ$ of the axis.

**(b)** At the entrance, the ray refracts from air into the core. For the steepest acceptable ray inside the core (making angle $20.2^\circ$ with the axis, or $69.8^\circ$ with the normal), apply Snell's Law at the entrance:

$$n_0 \sin\theta_{\text{max}} = n_1 \sin(20.2^\circ)$$
$$1.00 \times \sin\theta_{\text{max}} = 1.62 \times 0.345$$
$$\sin\theta_{\text{max}} = 0.559$$
$$\theta_{\text{max}} = \sin^{-1}(0.559) = 34.0^\circ$$

So any ray entering within $34^\circ$ of the fibre axis will be guided.

**Why this makes sense:** Optical fibres accept light within a cone of about $30$–$40^\circ$ half-angle. The small difference between core and cladding indices ($1.62 - 1.52 = 0.10$) produces a modest acceptance angle, which is typical for communication fibres.

---

## Practice Problems

### Problem 1
Light travelling in air ($n = 1.00$) enters a block of glass with refractive index $1.60$. The angle of incidence is $35^\circ$. Calculate the angle of refraction. Does the ray bend toward or away from the normal? Explain why.

### Problem 2
A light ray inside water ($n = 1.33$) approaches the water-air boundary at an angle of $40^\circ$ from the normal. The critical angle for the water-air boundary is $48.8^\circ$. Explain what happens to the ray and why. Calculate the angle of refraction if any light is transmitted.

### Problem 3
The critical angle for a particular type of glass in air is $38.0^\circ$. Calculate the refractive index of this glass. A light ray inside this glass strikes the boundary with air at an angle of $30^\circ$. Determine whether total internal reflection occurs and calculate the angle of refraction if light is transmitted.

### Problem 4
A light ray enters a rectangular glass block ($n = 1.50$) from air at an angle of incidence of $50^\circ$. The block has parallel faces. Calculate: (a) the angle of refraction at the first face, (b) the angle at which the ray strikes the second face (inside the glass), and (c) the angle at which it emerges back into air. Explain why the emerging ray is parallel to the incident ray.

### Problem 5 — IB-Style Examination Question
A student investigates the refraction of light using a semicircular glass block. The refractive index of the glass is 1.55. The student directs a narrow ray of light at the centre of the flat face, varying the angle of incidence.

(a) For an angle of incidence of $30^\circ$ in air, calculate the angle of refraction inside the glass. (2 marks)

(b) The student now directs the ray so that it strikes the curved face from inside the glass. She gradually increases the angle of incidence inside the glass until the refracted ray in air disappears. State the name of this phenomenon and calculate the angle of incidence inside the glass at which it occurs. (3 marks)

(c) The student repeats the experiment with the glass block submerged in water ($n = 1.33$) instead of air. Explain qualitatively how the critical angle changes and why. (2 marks)

(d) Suggest one technological application of the phenomenon observed in part (b) and explain briefly how the physics of total internal reflection enables this application. (2 marks)

---

## Answers

### Answer 1
$$1.00 \times \sin 35^\circ = 1.60 \times \sin\theta_2$$
$$\sin\theta_2 = \frac{\sin 35^\circ}{1.60} = \frac{0.574}{1.60} = 0.359$$
$$\theta_2 = \sin^{-1}(0.359) = 21.0^\circ$$

The ray bends TOWARD the normal because it enters a medium with a higher refractive index (1.60 > 1.00), meaning it slows down. The angle decreases from $35^\circ$ to $21.0^\circ$, consistent with bending toward the normal.

---

### Answer 2
The angle of incidence ($40^\circ$) is less than the critical angle ($48.8^\circ$), so total internal reflection does NOT occur. Some light is transmitted into the air. Using Snell's Law:

$$1.33 \times \sin 40^\circ = 1.00 \times \sin\theta_2$$
$$\sin\theta_2 = 1.33 \times 0.643 = 0.855$$
$$\theta_2 = \sin^{-1}(0.855) = 58.7^\circ$$

The ray emerges into air at $58.7^\circ$ from the normal, bent away from the normal because it is speeding up. A common mistake is to assume that any ray travelling from water to air will undergo TIR — this only happens when the angle exceeds the critical angle.

---

### Answer 3
$$\sin\theta_c = \frac{1}{n} \quad \Rightarrow \quad n = \frac{1}{\sin\theta_c} = \frac{1}{\sin 38.0^\circ} = \frac{1}{0.616} = 1.62$$

At $30^\circ$ incidence, this is less than the critical angle of $38.0^\circ$, so TIR does NOT occur. Light is transmitted:

$$1.62 \times \sin 30^\circ = 1.00 \times \sin\theta_2$$
$$\sin\theta_2 = 1.62 \times 0.500 = 0.810$$
$$\theta_2 = \sin^{-1}(0.810) = 54.1^\circ$$

---

### Answer 4
**(a)** At the first face (air to glass):
$$1.00 \times \sin 50^\circ = 1.50 \times \sin\theta_2$$
$$\sin\theta_2 = \frac{0.766}{1.50} = 0.511$$
$$\theta_2 = 30.7^\circ$$

**(b)** For a rectangular block with parallel faces, the ray inside the glass makes the same angle with the normal at both faces. At the second face, the angle of incidence inside the glass is $30.7^\circ$.

**(c)** At the second face (glass to air):
$$1.50 \times \sin 30.7^\circ = 1.00 \times \sin\theta_{\text{out}}$$
$$\sin\theta_{\text{out}} = 1.50 \times 0.511 = 0.766$$
$$\theta_{\text{out}} = \sin^{-1}(0.766) = 50^\circ$$

The emerging ray angle ($50^\circ$) equals the incident angle ($50^\circ$). For a rectangular block with parallel faces, the emerging ray is always parallel to the incident ray (though laterally displaced). This is because the refraction at the second face exactly reverses the refraction at the first face: Snell's Law applied in reverse gives the original angle. The ray is shifted sideways but its direction is unchanged.

---

### Answer 5 — IB-Style Full Solution with Mark Scheme

**(a)** (2 marks)
$$1.00 \times \sin 30^\circ = 1.55 \times \sin\theta_2$$
$$\sin\theta_2 = \frac{\sin 30^\circ}{1.55} = \frac{0.500}{1.55} = 0.323$$
$$\theta_2 = \sin^{-1}(0.323) = 18.8^\circ$$

1 mark for correct substitution into Snell's Law. 1 mark for correct angle to 3 significant figures. Accept $18.8^\circ$ or $19^\circ$.

**(b)** (3 marks)
The phenomenon is total internal reflection. (1 mark)

Critical angle:
$$\sin\theta_c = \frac{n_{\text{air}}}{n_{\text{glass}}} = \frac{1.00}{1.55} = 0.645$$
$$\theta_c = \sin^{-1}(0.645) = 40.2^\circ$$

(1 mark for correct formula and substitution. 1 mark for correct critical angle.)

Total internal reflection occurs when the angle of incidence inside the glass reaches or exceeds $40.2^\circ$.

**(c)** (2 marks)
When the glass is submerged in water ($n = 1.33$) instead of air ($n = 1.00$), the critical angle increases because $\theta_c = \sin^{-1}(n_2/n_1)$. With a larger $n_2$, the ratio $n_2/n_1$ is larger (1.33/1.55 = 0.858 vs. 1.00/1.55 = 0.645), so $\sin\theta_c$ is larger and $\theta_c$ is larger. (1 mark)

Physically, the speed difference between glass and water is smaller than between glass and air, so the bending at the boundary is less dramatic, and a larger angle is needed to achieve the $90^\circ$ refraction condition. (1 mark for physical reasoning.)

**(d)** (2 marks)
One application is optical fibres used in telecommunications. (1 mark for naming an application.) Light is injected into the glass core, which is surrounded by cladding with a slightly lower refractive index. The light rays strike the core-cladding boundary at angles greater than the critical angle and undergo repeated total internal reflection. Because TIR reflects 100% of the light, the signal can travel many kilometres with minimal loss. (1 mark for explaining how TIR enables the application.)

Other acceptable answers: endoscopes (medical imaging), prism reflectors in binoculars, diamond cutting for gemstones. Any application that correctly invokes total internal reflection is acceptable.

---

## Key Takeaways

1. **Law of reflection:** $\theta_i = \theta_r$, both measured from the normal. The incident ray, reflected ray, and normal all lie in the same plane.

2. **Refraction is caused by a change in wave speed at a boundary.** Frequency stays the same; speed changes; wavelength adjusts.

3. **Snell's Law:** $n_1\sin\theta_1 = n_2\sin\theta_2$. Into a slower medium ($n_2 > n_1$): bend toward the normal. Into a faster medium ($n_2 < n_1$): bend away from the normal.

4. **Total internal reflection** occurs when light travels from higher $n$ to lower $n$ AND the angle of incidence exceeds the critical angle: $\sin\theta_c = n_2/n_1$ where $n_1 > n_2$.

5. **TIR is 100% efficient** — no energy is lost to transmission. This makes it ideal for optical fibres, which form the backbone of global telecommunications.
