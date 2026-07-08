# Lesson 52: Motion in EM Fields I — Electron Gun and Parallel Plates

## What You'll Learn
- Understand thermionic emission and how an electron gun produces a beam
- Calculate the speed of electrons accelerated through a potential difference
- Analyse the parabolic motion of charged particles in uniform electric fields
- Apply projectile-motion thinking to electrons between parallel plates
- Understand the principle of the cathode ray tube (CRT)

---

## 1. Producing a Beam of Electrons

### 1.1 Why This Matters

In Lessons 48–51, we studied electric and magnetic fields and the forces they exert on charges. Now we put a specific charge — the electron — into those fields and watch what happens. An electron moving through electric and magnetic fields follows a path determined by the same principles as a projectile in a gravitational field, but with forces that are typically billions of times stronger relative to its mass. This is why electron beams can be steered with small voltages and why CRTs can paint an image on a screen in microseconds.

### 1.2 Thermionic Emission — Getting Electrons Out

Electrons are bound inside metals. To create a free beam of electrons, we need to give them enough energy to escape the metal surface. One way is **thermionic emission**: heat a metal filament until the electrons have enough thermal kinetic energy to boil off the surface.

In an electron gun, a heated cathode (negative electrode) emits electrons. A nearby anode (positive electrode) at a high positive voltage attracts and accelerates them. The electrons pass through a hole in the anode and emerge as a narrow beam.

### 1.3 The Electron Gun Equation

When an electron (charge $e$, mass $m_e$) is accelerated from rest through a potential difference $V$, the work done by the electric field is $eV$. This work becomes the electron's kinetic energy:

$$eV = \frac{1}{2}m_ev^2$$

Solving for the speed:
$$v = \sqrt{\frac{2eV}{m_e}}$$

This is one of the most-used equations in electron physics. It tells you the speed of an electron after being accelerated through $V$ volts.

**A common mistake:** The mass in this equation is the electron mass ($m_e = 9.11 \times 10^{-31}\text{ kg}$), NOT the mass of whatever particle you might be dealing with. If the problem involves a proton or an ion, use the appropriate mass.

---

## 2. Electrons in a Uniform Electric Field

### 2.1 The Setup

Consider an electron entering the space between two parallel plates. The plates are connected to a voltage source, creating a uniform electric field $E = V/d$ between them, where $d$ is the plate separation. The electron enters with an initial horizontal velocity $v_x$ and experiences a constant vertical electric force.

### 2.2 Why It Is Just Projectile Motion

The force on the electron is $F = eE$ (vertically, toward the positive plate). The acceleration is:
$$a = \frac{F}{m_e} = \frac{eE}{m_e}$$

This is exactly analogous to a projectile in a gravitational field, with $\frac{eE}{m_e}$ playing the role of $g$. The motion splits into independent horizontal and vertical components:

**Horizontal:** No force → constant velocity → $x = v_x t$

**Vertical:** Constant acceleration → $y = \frac{1}{2}at^2 = \frac{1}{2}\frac{eE}{m_e}t^2$

Eliminating $t$ gives the parabolic path:
$$y = \frac{eE}{2m_ev_x^2}x^2$$

The electron follows a parabola, curving toward the positive plate.

### 2.3 Deflection in a Given Field

For plates of length $L$, the time spent between them is $t = L/v_x$. The vertical deflection at the far end is:
$$y = \frac{1}{2}\frac{eE}{m_e}\left(\frac{L}{v_x}\right)^2$$

After leaving the plates, the electron travels in a straight line (no more field) toward a screen. The total deflection on the screen can be calculated by treating the exit as a launch point with the electron's velocity at that moment.

---

## 3. The Cathode Ray Tube (CRT)

### 3.1 How It Works

A CRT was the display technology in old televisions and computer monitors. It contains:
- An electron gun producing a narrow beam
- Deflection plates (or magnetic coils) to steer the beam horizontally and vertically
- A phosphorescent screen that glows when struck by electrons

By rapidly scanning the beam across the screen line by line while varying its intensity, a CRT paints a complete image. The physics that makes it work is exactly what we study in this lesson — electrons accelerated by an electric field and deflected by additional fields.

---

## Worked Examples

### Worked Example 52.1 — Electron Speed from Accelerating Voltage

**Problem:** Electrons are accelerated from rest through a potential difference of $5,000\text{ V}$ in an electron gun. Calculate their final speed.

**Approach:** Use $eV = \frac{1}{2}m_ev^2$. Check if the speed is relativistic (if $v > 0.1c$, we should consider relativistic corrections — for now, calculate and check).

**Solution:**
$$v = \sqrt{\frac{2eV}{m_e}} = \sqrt{\frac{2(1.60 \times 10^{-19})(5,000)}{9.11 \times 10^{-31}}} = \sqrt{\frac{1.60 \times 10^{-15}}{9.11 \times 10^{-31}}} = \sqrt{1.756 \times 10^{15}} = 4.19 \times 10^7\text{ m s}^{-1}$$

**Check:** $v/c = 4.19 \times 10^7 / 3.00 \times 10^8 = 0.14$. This is about 14% of light speed — relativistic corrections would be small (~1%) but not negligible for precise work. At IB level, we use the non-relativistic formula.

---

### Worked Example 52.2 — Electron Deflection in Parallel Plates

**Problem:** An electron enters the region between two parallel plates at $5.0 \times 10^6\text{ m s}^{-1}$ horizontally. The plates are $3.0\text{ cm}$ long and separated by $1.0\text{ cm}$, with a voltage of $200\text{ V}$ between them. Calculate the vertical deflection of the electron as it leaves the plates.

**Approach:** Find the electric field $E = V/d$. Find the vertical acceleration $a = eE/m_e$. Find the time between plates $t = L/v_x$. Find deflection $y = \frac{1}{2}at^2$.

**Solution:**
$$E = \frac{V}{d} = \frac{200}{0.010} = 20,000\text{ V m}^{-1}$$
$$a = \frac{eE}{m_e} = \frac{(1.60 \times 10^{-19})(20,000)}{9.11 \times 10^{-31}} = 3.51 \times 10^{15}\text{ m s}^{-2}$$
$$t = \frac{L}{v_x} = \frac{0.030}{5.0 \times 10^6} = 6.0 \times 10^{-9}\text{ s}$$
$$y = \frac{1}{2}at^2 = \frac{1}{2}(3.51 \times 10^{15})(6.0 \times 10^{-9})^2 = \frac{1}{2}(3.51 \times 10^{15})(3.6 \times 10^{-17}) = 0.063\text{ m} = 6.3\text{ cm}$$

**Why this makes sense:** The deflection (6.3 cm) is larger than the plate separation (1.0 cm), which means the electron would hit the positive plate before reaching the end. In a real CRT, the voltage would be adjusted to keep the beam between the plates. This example shows how sensitive electron beams are to electric fields — tiny voltages produce large deflections because electrons are so light.

---

### Worked Example 52.3 — Finding Acceleration Voltage from Speed

**Problem:** An electron in a beam has speed $6.0 \times 10^6\text{ m s}^{-1}$. Through what potential difference was it accelerated from rest?

**Approach:** Rearrange $eV = \frac{1}{2}mv^2$ to find $V$. The answer will be in volts.

**Solution:**
$$V = \frac{m_ev^2}{2e} = \frac{(9.11 \times 10^{-31})(6.0 \times 10^6)^2}{2(1.60 \times 10^{-19})} = \frac{(9.11 \times 10^{-31})(3.6 \times 10^{13})}{3.20 \times 10^{-19}} = \frac{3.28 \times 10^{-17}}{3.20 \times 10^{-19}} = 103\text{ V}$$

**Why this makes sense:** A modest 103 V accelerates an electron to 6 million metres per second — about 2% of light speed. The electron's tiny mass means small voltages produce enormous speeds.

---

### Worked Example 52.4 — IB-Style CRT Problem

**Problem:** The electron gun in an oscilloscope accelerates electrons through $2,000\text{ V}$. The beam then passes between horizontal deflection plates $4.0\text{ cm}$ long, separated by $0.50\text{ cm}$. A deflection voltage of $150\text{ V}$ is applied.

(a) Calculate the speed of electrons entering the deflection plates. (2 marks)
(b) Determine the vertical deflection at the end of the plates. (3 marks)
(c) After leaving the plates, the electrons travel $25\text{ cm}$ to the screen. Calculate the total vertical deflection on the screen. (3 marks)

**Solution (a):**
$$v = \sqrt{\frac{2eV}{m_e}} = \sqrt{\frac{2(1.60\times 10^{-19})(2,000)}{9.11\times 10^{-31}}} = 2.65 \times 10^7\text{ m s}^{-1}$$

**(b):**
$E = 150/0.005 = 30,000\text{ V m}^{-1}$.
$a = (1.60\times 10^{-19})(30,000)/(9.11\times 10^{-31}) = 5.27 \times 10^{15}\text{ m s}^{-2}$.
$t = 0.040/(2.65\times 10^7) = 1.51 \times 10^{-9}\text{ s}$.
$y_1 = \frac{1}{2}(5.27\times 10^{15})(1.51\times 10^{-9})^2 = 6.0 \times 10^{-3}\text{ m} = 0.60\text{ cm}$.

**(c):** Vertical velocity at exit: $v_y = at = (5.27\times 10^{15})(1.51\times 10^{-9}) = 7.96 \times 10^6\text{ m s}^{-1}$.
Time to screen after plates: $t_2 = 0.25/(2.65\times 10^7) = 9.43 \times 10^{-9}\text{ s}$.
Additional deflection: $y_2 = v_y t_2 = (7.96\times 10^6)(9.43\times 10^{-9}) = 0.075\text{ m} = 7.5\text{ cm}$.
Total: $y = 0.60 + 7.5 = 8.1\text{ cm}$.

---

## Practice Problems

### Problem 1
Electrons are accelerated from rest through a potential difference of 800 V. Calculate their final speed. Express the answer as a percentage of the speed of light.

### Problem 2
An electron enters a region of uniform electric field at $4.0 \times 10^6\text{ m s}^{-1}$ perpendicular to the field. The field strength is $5.0 \times 10^3\text{ V m}^{-1}$. After $2.0 \times 10^{-8}\text{ s}$, calculate: (a) the vertical deflection, and (b) the vertical component of velocity.

### Problem 3
An electron gun produces a beam of electrons with speed $3.0 \times 10^7\text{ m s}^{-1}$. A pair of parallel plates 5.0 cm long with a separation of 1.5 cm is used to deflect the beam. What voltage between the plates is needed to produce a deflection of 2.0 cm at the end of the plates?

### Problem 4
Explain why an electron beam between parallel plates follows a parabolic path, while an electron in a uniform magnetic field follows a circular path.

### Problem 5 — IB-Style
In an electron deflection experiment, electrons are accelerated through $3.0\text{ kV}$ in an electron gun and enter a region of uniform electric field between two parallel plates of length $6.0\text{ cm}$.

(a) Calculate the speed of the electrons. (1 mark)

(b) The electric field strength between the plates is $4.0 \times 10^4\text{ V m}^{-1}$. Calculate the acceleration of the electrons. (2 marks)

(c) Calculate the time an electron spends between the plates and the vertical deflection. (3 marks)

(d) The deflecting voltage is now doubled. By what factor does the deflection change? (2 marks)

(e) Suggest one way the deflection could be increased without changing the voltage between the plates, and explain why it works. (2 marks)

---

## Answers

### Answer 1
$v = \sqrt{2(1.60\times 10^{-19})(800)/(9.11\times 10^{-31})} = \sqrt{2.81\times 10^{14}} = 1.68 \times 10^7\text{ m s}^{-1}$. $v/c = 1.68\times 10^7/3.00\times 10^8 = 0.056 = 5.6\%$.

### Answer 2
**(a)** $a = eE/m_e = (1.60\times 10^{-19})(5.0\times 10^3)/(9.11\times 10^{-31}) = 8.78 \times 10^{14}\text{ m s}^{-2}$.
$y = \frac{1}{2}at^2 = \frac{1}{2}(8.78\times 10^{14})(2.0\times 10^{-8})^2 = 0.176\text{ m} = 17.6\text{ cm}$.
**(b)** $v_y = at = (8.78\times 10^{14})(2.0\times 10^{-8}) = 1.76 \times 10^7\text{ m s}^{-1}$.

### Answer 3
$t = 0.050/(3.0\times 10^7) = 1.67\times 10^{-9}\text{ s}$. $y = \frac{1}{2}at^2$, so $a = 2y/t^2 = 2(0.020)/(1.67\times 10^{-9})^2 = 1.44\times 10^{16}\text{ m s}^{-2}$. $E = m_ea/e = (9.11\times 10^{-31})(1.44\times 10^{16})/(1.60\times 10^{-19}) = 8.20 \times 10^4\text{ V m}^{-1}$. $V = Ed = (8.20\times 10^4)(0.015) = 1,230\text{ V}$.

### Answer 4
In a uniform E-field, the force is constant in magnitude and direction → constant acceleration → parabolic path (like projectile motion). In a uniform B-field, the force is always perpendicular to velocity → changes direction but not speed → uniform circular motion ($r = mv/qB$). The E-field changes the speed; the B-field only changes direction.

### Answer 5 — IB-Style
**(a)** $v = \sqrt{2(1.60\times 10^{-19})(3,000)/(9.11\times 10^{-31})} = 3.25 \times 10^7\text{ m s}^{-1}$. (1 mark)

**(b)** $a = eE/m_e = (1.60\times 10^{-19})(4.0\times 10^4)/(9.11\times 10^{-31}) = 7.02 \times 10^{15}\text{ m s}^{-2}$. (2 marks)

**(c)** $t = 0.060/(3.25\times 10^7) = 1.85 \times 10^{-9}\text{ s}$. $y = \frac{1}{2}(7.02\times 10^{15})(1.85\times 10^{-9})^2 = 1.20 \times 10^{-2}\text{ m} = 1.20\text{ cm}$. (3 marks)

**(d)** Doubling $V$ doubles $E$, which doubles $a$, which doubles $y$ (since $y \propto a$). Factor of 2. (2 marks — 1 for recognising proportional relationship, 1 for factor.)

**(e)** Increase the length $L$ of the plates. The electron spends longer in the field, so the deflection increases (and $y \propto L^2$). Alternatively: reduce the accelerating voltage in the electron gun, which reduces $v_x$, increasing the time in the field and thus the deflection. (2 marks.)

---

## Key Takeaways

1. **Electron gun:** $eV = \frac{1}{2}m_ev^2$. The speed depends on the accelerating voltage.

2. **Motion in uniform E-field = projectile motion.** Horizontal: constant velocity. Vertical: constant acceleration $a = eE/m_e$.

3. **Path is parabolic** — mathematically identical to a projectile in a gravitational field, with $eE/m_e$ replacing $g$.

4. **Electrons are extremely light** ($9.11\times 10^{-31}\text{ kg}$), so small voltages produce large accelerations and high speeds. 1,000 V → ~$2\times 10^7\text{ m s}^{-1}$ (7% of $c$).

5. **CRT principle:** Accelerate, deflect, detect. The same physics underlies oscilloscopes, old TVs, and electron microscopes.
