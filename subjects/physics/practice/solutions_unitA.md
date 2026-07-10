# Unit A: Space, Time & Motion — Solutions

---

## Solution 1 — Kinematics: Multi-stage motion (MCQ)

**[a] Correct answer: B — $100~\text{m}$**

**[b] Step-by-step reasoning:**

**Phase 1 — Acceleration ($t = 0$ to $5.0~\text{s}$):**
$$v_1 = at = (2.0)(5.0) = 10~\text{m/s}$$
$$s_1 = \frac{1}{2}at^2 = \frac{1}{2}(2.0)(5.0)^2 = 25~\text{m}$$

**Phase 2 — Constant velocity ($t = 5.0$ to $10.0~\text{s}$):**
$$s_2 = v_1 t = (10)(5.0) = 50~\text{m}$$

**Phase 3 — Deceleration ($t = 10.0$ to $15.0~\text{s}$):**
Deceleration: $a = -\frac{10}{5.0} = -2.0~\text{m/s}^2$
$$s_3 = v_1 t + \frac{1}{2}at^2 = (10)(5.0) + \frac{1}{2}(-2.0)(5.0)^2 = 50 - 25 = 25~\text{m}$$
(Equivalently, $s_3 = \frac{v_1 + 0}{2} \cdot t = 5 \times 5 = 25~\text{m}$)

**Total distance:**
$$s_\text{total} = 25 + 50 + 25 = 100~\text{m}$$

**Why each wrong answer is wrong:**
- **A ($75~\text{m}$):** Forgets Phase 3 — adds only Phase 1 ($25$) + Phase 2 ($50$) = $75~\text{m}$.
- **C ($125~\text{m}$):** Treats Phase 3 as if the whole $10~\text{m/s}$ is maintained for $5.0~\text{s}$ without deceleration, giving $50~\text{m}$ instead of the correct $25~\text{m}$ ($100 + 25 = 125$).
- **D ($150~\text{m}$):** Multiplies the maximum speed $10~\text{m/s}$ by the total time $15~\text{s}$ — this would be correct only if the object moved at $10~\text{m/s}$ the entire time.

---

## Solution 2 — Kinematics: Velocity–time graph (MCQ)

**[a] Correct answer: C — $120~\text{m}$**

**[b] Step-by-step reasoning:**

Distance = area under the $v\!-\!t$ graph. The graph consists of three regions:

**Region 1 ($0$ to $4.0~\text{s}$):** Triangle, base $4.0~\text{s}$, height $12~\text{m/s}$
$$A_1 = \frac{1}{2} \times 4.0 \times 12 = 24~\text{m}$$

**Region 2 ($4.0$ to $10.0~\text{s}$):** Rectangle, width $6.0~\text{s}$, height $12~\text{m/s}$
$$A_2 = 6.0 \times 12 = 72~\text{m}$$

**Region 3 ($10.0$ to $14.0~\text{s}$):** Triangle, base $4.0~\text{s}$, height $12~\text{m/s}$
$$A_3 = \frac{1}{2} \times 4.0 \times 12 = 24~\text{m}$$

**Total:**
$$s = 24 + 72 + 24 = 120~\text{m}$$

**Why each wrong answer is wrong:**
- **A ($96~\text{m}$):** Uses $4.0~\text{s}$ width for Region 2 instead of $6.0~\text{s}$: $24 + 48 + 24 = 96$.
- **B ($108~\text{m}$):** Computes Region 3 as a rectangle ($4 \times 12 = 48$) instead of a triangle ($24$): $24 + 72 + 12 = 108$ (only uses half width for Region 3 wrong).
- **D ($144~\text{m}$):** Treats all three regions as rectangles: $4 \times 12 + 6 \times 12 + 4 \times 12 = 48 + 72 + 48 = 168$ (not 144), or attempts $12 \times 12$ (confusing average speed).

---

## Solution 3 — Kinematics: Relative motion — boat crossing river (MCQ)

**[a] Correct answer: B — $8.0~\text{s}$**

**[b] Step-by-step reasoning:**

The boat's velocity perpendicular to the banks is its own speed in still water: $v_\perp = 5.0~\text{m/s}$. The river's flow is entirely parallel to the banks and does **not** affect the time to cross.

$$t = \frac{\text{width}}{v_\perp} = \frac{40}{5.0} = 8.0~\text{s}$$

The downstream drift caused by the river current does not change the crossing time — it only determines where the boat lands on the opposite bank.

**Why each wrong answer is wrong:**
- **A ($5.0~\text{s}$):** Adds the two velocities: $t = 40/(5+3) = 5.0~\text{s}$. This incorrectly treats the river current as helping the boat cross.
- **C ($10.0~\text{s}$):** Uses $t = 40/\sqrt{5^2 - 3^2} = 40/4 = 10~\text{s}$. This would be the crossing time if the boat were aimed upstream so that its **resultant** velocity is directly across — but the boat is headed "directly across," not aimed upstream.
- **D ($13.3~\text{s}$):** Uses only the river speed: $t = 40/3 \approx 13.3~\text{s}$ — nonsensical.

---

## Solution 4 — Kinematics: Stone from cliff (MCQ)

**[a] Correct answer: C — $40~\text{m/s}$**

**[b] Step-by-step reasoning:**

Use conservation of energy. The stone has initial kinetic energy $\frac{1}{2}mv_0^2$ and gravitational potential energy $mgh$ relative to the sea.

$$\frac{1}{2}mv^2 = \frac{1}{2}mv_0^2 + mgh$$

Cancel $m$:
$$v^2 = v_0^2 + 2gh = (30)^2 + 2(10)(35) = 900 + 700 = 1600$$
$$v = \sqrt{1600} = 40~\text{m/s}$$

(Note: the stone does **not** simply return to its launch speed of $30~\text{m/s}$ because it is launched from above the water — it has further to fall.)

**Why each wrong answer is wrong:**
- **A ($10~\text{m/s}$):** Arbitrary small value — ignores energy addition from the height.
- **B ($30~\text{m/s}$):** Uses only the initial speed — assumes the stone returns to its launch height (i.e., lands back on the cliff edge), forgetting the extra $35~\text{m}$ fall to the sea.
- **D ($50~\text{m/s}$):** Double-counting or arithmetic error — e.g., $v_0 + gt$ with a wrong time, or $30 + 2 \times 10 = 50$.

---

## Solution 5 — Forces: Newton's Second Law (MCQ)

**[a] Correct answer: D — $20~\text{m/s}$**

**[b] Step-by-step reasoning:**

$$a = \frac{F}{m} = \frac{15}{3.0} = 5.0~\text{m/s}^2$$

Since the mass starts from rest:
$$v = at = (5.0)(4.0) = 20~\text{m/s}$$

**Why each wrong answer is wrong:**
- **A ($5.0~\text{m/s}$):** Uses $v = F/m = 5$ — confuses acceleration with velocity.
- **B ($12~\text{m/s}$):** Uses $v = Ft/m$ — dimensionally incorrect; possibly $15 \times 4 / 5 = 12$.
- **C ($15~\text{m/s}$):** Uses the force value ($15$) directly as the speed — confuses force with velocity.

---

## Solution 6 — Forces: Inclined plane with friction (MCQ)

**[a] Correct answer: B — $0.58$**

**[b] Step-by-step reasoning:**

The block slides at **constant speed**, so the net force along the incline is zero. The component of weight down the incline is balanced by kinetic friction.

Down the incline: $mg\sin 30^\circ$
Friction up the incline: $\mu_k N = \mu_k (mg\cos 30^\circ)$

At equilibrium:
$$mg\sin 30^\circ = \mu_k mg\cos 30^\circ$$
$$\mu_k = \frac{\sin 30^\circ}{\cos 30^\circ} = \tan 30^\circ = \frac{0.5}{0.866} \approx 0.577$$

Rounding to two significant figures: $\boxed{0.58}$

**Why each wrong answer is wrong:**
- **A ($0.50$):** Uses $\mu_k = \sin 30^\circ = 0.50$ — forgets the $\cos 30^\circ$ factor from the normal force, implicitly assuming a horizontal surface where $N = mg$.
- **C ($0.87$):** Uses $\mu_k = \cos 30^\circ \approx 0.866$, or inverts the ratio: $\cos 30^\circ / \sin 30^\circ$.
- **D ($1.00$):** Picks the maximum possible $\mu_k$ without calculation; $\mu_k = 1$ would give $a=0$ on a $45^\circ$ incline, not $30^\circ$.

---

## Solution 7 — Forces: Terminal velocity (MCQ)

**[a] Correct answer: C — $800~\text{N}$**

**[b] Step-by-step reasoning:**

At terminal velocity, the net force is zero (no acceleration). The downward weight is exactly balanced by the upward air resistance.

$$F_\text{air} = mg = (80)(10) = 800~\text{N}$$

**Why each wrong answer is wrong:**
- **A ($0$):** Incorrect — air resistance must balance weight; if it were zero, the skydiver would accelerate indefinitely.
- **B ($400~\text{N}$):** Uses $m = 40~\text{kg}$ (halved mass) or $g = 5~\text{m/s}^2$ — arithmetic error.
- **D ($1600~\text{N}$):** Doubles the correct value — possibly uses $2mg$, confusing terminal velocity with something else.

---

## Solution 8 — Energy: Work done by a force at an angle (MCQ)

**[a] Correct answer: B — $50~\text{J}$**

**[b] Step-by-step reasoning:**

Only the horizontal component of the force does work (since the displacement is horizontal).

$$W = F d \cos\theta = (20)(5.0)(\cos 60^\circ) = 100 \times 0.5 = 50~\text{J}$$

**Why each wrong answer is wrong:**
- **A ($25~\text{J}$):** Uses $\cos 60^\circ = 0.25$ (halved again) or halves the answer again: $100/4 = 25$.
- **C ($87~\text{J}$):** Uses $\sin 60^\circ \approx 0.866$ instead of $\cos 60^\circ$: $100 \times 0.866 \approx 87~\text{J}$.
- **D ($100~\text{J}$):** Ignores the angle entirely and uses $W = Fd = 100~\text{J}$ — treats the force as if it were entirely in the direction of displacement.

---

## Solution 9 — Energy: Power (MCQ)

**[a] Correct answer: C — $1000~\text{W}$**

**[b] Step-by-step reasoning:**

The motor lifts at constant speed, so the tension equals the weight. Power is force × velocity:

$$P = Fv = (mg)v = (200 \times 10)(0.50) = 2000 \times 0.50 = 1000~\text{W}$$

**Why each wrong answer is wrong:**
- **A ($100~\text{W}$):** Uses $P = m v = 200 \times 0.5 = 100~\text{W}$ — forgets $g$.
- **B ($500~\text{W}$):** Uses $P = m g = 2000$ and then divides by 4 (confusion with time).
- **D ($2000~\text{W}$):** Uses $P = mg = 2000~\text{W}$ — confuses force with power, forgetting the velocity factor.

---

## Solution 10 — Momentum: Impulse (MCQ)

**[a] Correct answer: A — $10~\text{N·s}$**

**[b] Step-by-step reasoning:**

Impulse is the area under the force–time graph. For a constant force:

$$J = F \Delta t = (40)(0.25) = 10~\text{N·s}$$

**Why each wrong answer is wrong:**
- **B ($40~\text{N·s}$):** Uses $J = F$ — confuses impulse with force; ignores the time.
- **C ($100~\text{N·s}$):** Uses $F/\Delta t = 40/0.25 = 160$ (not 100), or $40 \times 2.5 = 100$ — misreads time.
- **D ($160~\text{N·s}$):** Uses $F/\Delta t = 40/0.25 = 160$ — divides instead of multiplies.

---

## Solution 11 — Momentum: Inelastic collision (MCQ)

**[a] Correct answer: A — $\dfrac{1}{4}$**

**[b] Step-by-step reasoning:**

This is a perfectly inelastic collision (objects stick together).

Conservation of momentum:
$$m_1 v_1 + m_2 v_2 = (m_1 + m_2) v_f$$
$$(3.0)(4.0) + (1.0)(0) = (4.0)v_f$$
$$12 = 4.0 v_f \quad\Rightarrow\quad v_f = 3.0~\text{m/s}$$

Initial kinetic energy:
$$KE_i = \frac{1}{2}(3.0)(4.0)^2 = 24~\text{J}$$

Final kinetic energy:
$$KE_f = \frac{1}{2}(4.0)(3.0)^2 = 18~\text{J}$$

Fraction lost:
$$\frac{KE_i - KE_f}{KE_i} = \frac{24 - 18}{24} = \frac{6}{24} = \frac{1}{4}$$

**Why each wrong answer is wrong:**
- **B ($1/2$):** Uses the mass ratio ($3:1$, difference $2/4 = 1/2$) rather than the energy calculation.
- **C ($3/4$):** Inverts the fraction — computes $KE_f / KE_i = 18/24 = 3/4$ and mistakes this for the fraction lost.
- **D (All):** Thinks all kinetic energy is lost in an inelastic collision — but only the **relative** kinetic energy in the centre-of-mass frame is converted; there is still bulk translational KE.

---

## Solution 12 — Rigid Body: Torque (MCQ)

**[a] Correct answer: B — $12~\text{N·m}$**

**[b] Step-by-step reasoning:**

Torque is force × perpendicular distance from the pivot:
$$\tau = F r_\perp = (30)(0.40) = 12~\text{N·m}$$

**Why each wrong answer is wrong:**
- **A ($7.5~\text{N·m}$):** Uses $\tau = F/r = 30/0.4 = 75$ (not 7.5), or uses only half the distance.
- **C ($75~\text{N·m}$):** Uses $F/r = 30/0.40 = 75$ — divides instead of multiplies.
- **D ($120~\text{N·m}$):** Multiplies by an extra factor of 10 — possibly converts cm incorrectly: $30 \times 4.0 = 120$.

---

## Solution 13 — Special Relativity: Time dilation (MCQ) **[HL]**

**[a] Correct answer: C — $10.0~\text{years}$**

**[b] Step-by-step reasoning:**

The Lorentz factor:
$$\gamma = \frac{1}{\sqrt{1 - v^2/c^2}} = \frac{1}{\sqrt{1 - (0.60)^2}} = \frac{1}{\sqrt{1 - 0.36}} = \frac{1}{\sqrt{0.64}} = \frac{1}{0.80} = 1.25$$

The $8.0$ years measured by the astronaut is the **proper time** $\Delta t_0$ (measured in the spacecraft rest frame). The dilated time on Earth is:
$$\Delta t = \gamma \Delta t_0 = (1.25)(8.0) = 10.0~\text{years}$$

**Why each wrong answer is wrong:**
- **A ($4.8~\text{years}$):** Computes $\Delta t = 8.0 \times 0.60 = 4.8$ — multiplies proper time by $v/c$ instead of using the Lorentz factor; this has no physical meaning.
- **B ($6.4~\text{years}$):** Computes $\Delta t = 8.0 \times 0.80 = 6.4$ — multiplies by $\sqrt{1 - v^2/c^2}$ instead of $\gamma$, effectively using length contraction on time.
- **D ($13.3~\text{years}$):** Computes $\Delta t = 8.0 / 0.60 \approx 13.3$ — divides by $v/c$, another physically meaningless operation.

---

## Solution 14 — Kinematics: Projectile motion **[9 marks]**

**(a) Resolve initial velocity into components [2 marks]**

Horizontal component: $v_x = v_0 \cos 37^\circ = 25 \times 0.8 = 20~\text{m/s}$ **[1 mark]**

Vertical component: $v_y = v_0 \sin 37^\circ = 25 \times 0.6 = 15~\text{m/s}$ **[1 mark]**

---

**(b) Time of flight [2 marks]**

Use $s_y = v_y t - \frac{1}{2}gt^2$. The ball returns to ground level so $s_y = 0$:
$$0 = 15t - 5t^2$$
$$5t(3 - t) = 0$$
$$t = 0 \text{ (launch) or } t = 3.0~\text{s}~\text{(landing)}$$ **[2 marks]**

(Alternative: $t = 2v_y/g = 2 \times 15 / 10 = 3.0~\text{s}$.)

---

**(c) Horizontal range [2 marks]**

Horizontal motion is uniform ($a_x = 0$):
$$R = v_x t = 20 \times 3.0 = 60~\text{m}$$ **[2 marks]**

---

**(d) Maximum height [2 marks]**

At maximum height, $v_y = 0$. Using $v_y^2 = v_{y0}^2 - 2gh$:
$$0 = 15^2 - 2 \times 10 \times h_\text{max}$$
$$h_\text{max} = \frac{225}{20} = 11.25~\text{m}$$ **[2 marks]**

(Or: time to max height $t = 15/10 = 1.5~\text{s}$, $h = 15 \times 1.5 - 5 \times (1.5)^2 = 22.5 - 11.25 = 11.25~\text{m}$.)

---

**(e) Speed on hitting the ground [1 mark]**

By conservation of energy (or symmetry of projectile motion on level ground), the speed on landing equals the launch speed: $25~\text{m/s}$. **[1 mark]**

The horizontal component is unchanged ($20~\text{m/s}$), and the vertical component has magnitude $15~\text{m/s}$ downward: $v = \sqrt{20^2 + 15^2} = \sqrt{400+225} = \sqrt{625} = 25~\text{m/s}$.

---

## Solution 15 — Kinematics: Data analysis **[6 marks]**

**(a) Show $x \propto t^2$ [2 marks]**

Calculate $x / t^2$ for each non-zero data point:

| $t$ / s | $x$ / m | $t^2$ / s² | $x/t^2$ / m·s⁻² |
|---------|---------|------------|------------------|
| 0.50 | 0.25 | 0.25 | 1.00 |
| 1.00 | 1.00 | 1.00 | 1.00 |
| 1.50 | 2.25 | 2.25 | 1.00 |
| 2.00 | 4.00 | 4.00 | 1.00 |
| 2.50 | 6.25 | 6.25 | 1.00 |
| 3.00 | 9.00 | 9.00 | 1.00 |

Since $x/t^2$ is constant ($= 1.00~\text{m·s}^{-2}$) for all data points, $x \propto t^2$. **[2 marks]**

---

**(b) Determine acceleration [3 marks]**

For uniformly accelerated motion from rest: $x = \frac{1}{2}at^2$. **[1 mark]**

Therefore $\frac{x}{t^2} = \frac{1}{2}a$. **[1 mark]**

From the table, $x/t^2 = 1.00$, so:
$$\frac{1}{2}a = 1.00 \quad\Rightarrow\quad a = 2.0~\text{m/s}^2$$ **[1 mark]**

---

**(c) Show $\sin\theta = 0.20$ [1 mark]**

$$a = g\sin\theta \quad\Rightarrow\quad \sin\theta = \frac{a}{g} = \frac{2.0}{10} = 0.20$$ **[1 mark]**

---

## Solution 16 — Forces: Connected bodies **[8 marks]**

**(a) Free-body diagrams [3 marks]**

**Block A (on table):**
- Weight $W_A = m_A g = 40~\text{N}$ downwards
- Normal reaction $N = 40~\text{N}$ upwards
- Tension $T$ to the right

**Block B (hanging):**
- Weight $W_B = m_B g = 10~\text{N}$ downwards
- Tension $T$ upwards

[3 marks: 1 mark for correct forces on A, 1 mark for correct forces on B, 1 mark for arrows and labels]

---

**(b) Newton's second law equations [2 marks]**

Block A (horizontal only): $T = m_A a = 4.0a$ **[1 mark]**

Block B (vertical, taking down as positive): $m_B g - T = m_B a$, i.e. $10 - T = 1.0a$ **[1 mark]**

---

**(c) Acceleration [2 marks]**

Substitute $T = 4.0a$ into $10 - T = 1.0a$: **[1 mark]**

$$10 - 4.0a = 1.0a$$
$$10 = 5.0a$$
$$a = 2.0~\text{m/s}^2$$ **[1 mark]**

---

**(d) Tension [1 mark]**

$$T = m_A a = 4.0 \times 2.0 = 8.0~\text{N}$$ **[1 mark]**

(Check: $10 - T = 10 - 8 = 2 = m_B a$, consistent.)

---

## Solution 17 — Forces: Circular motion **[7 marks]**

**(a) Angular velocity [1 mark]**

$$\omega = 2\pi f = 2\pi \times 3.0 = 6\pi~\text{rad/s}$$ **[1 mark]**

---

**(b) Centripetal acceleration [2 marks]**

$$a_c = \omega^2 r$$ **[1 mark]**

$$a_c = (6\pi)^2 \times 0.50 = 36\pi^2 \times 0.50 = 18\pi^2~\text{m/s}^2$$ **[1 mark]**

---

**(c) Tension [1 mark]**

The tension provides the centripetal force:
$$T = m a_c = 2.0 \times 18\pi^2 = 36\pi^2~\text{N}$$ **[1 mark]**

---

**(d) Maximum angular velocity [3 marks]**

The string breaks when $T = 400~\text{N}$. At the breaking point: **[1 mark]**

$$T_\text{max} = m \omega_\text{max}^2 r$$ **[1 mark]**

$$400 = 2.0 \times \omega_\text{max}^2 \times 0.50$$
$$400 = 1.0 \times \omega_\text{max}^2$$
$$\omega_\text{max}^2 = 400$$
$$\omega_\text{max} = 20~\text{rad/s}$$ **[1 mark]**

---

## Solution 18 — Energy: Spring compression **[6 marks]**

**(a) Initial kinetic energy [1 mark]**

$$KE_i = \frac{1}{2}mv^2 = \frac{1}{2}(2.0)(5.0)^2 = 25~\text{J}$$ **[1 mark]**

---

**(b) Maximum compression [2 marks]**

At maximum compression, all KE has been converted to elastic potential energy: **[1 mark]**

$$\frac{1}{2}kx_\text{max}^2 = 25$$
$$\frac{1}{2}(200)x_\text{max}^2 = 25$$
$$100x_\text{max}^2 = 25$$
$$x_\text{max}^2 = 0.25$$
$$x_\text{max} = 0.50~\text{m}$$ **[1 mark]**

---

**(c) Speed at $x = 0.30~\text{m}$ [3 marks]**

At this compression, the elastic potential energy is: **[1 mark]**

$$EPE = \frac{1}{2}kx^2 = \frac{1}{2}(200)(0.30)^2 = 100 \times 0.09 = 9.0~\text{J}$$ **[1 mark]**

By conservation of energy:
$$KE = KE_i - EPE = 25 - 9.0 = 16~\text{J}$$
$$\frac{1}{2}mv^2 = 16$$
$$v^2 = \frac{2 \times 16}{2.0} = 16$$
$$v = 4.0~\text{m/s}$$ **[1 mark]**

---

## Solution 19 — Energy: Incline and friction **[6 marks]**

**(a) Show $\sin\theta = 0.40$ [1 mark]**

$$\sin\theta = \frac{\text{height}}{\text{length}} = \frac{4.0}{10.0} = 0.40$$ **[1 mark]**

---

**(b) Speed at bottom of incline [2 marks]**

By conservation of energy (no friction on incline): **[1 mark]**

$$mgh = \frac{1}{2}mv^2$$
$$v^2 = 2gh = 2 \times 10 \times 4.0 = 80$$
$$v = \sqrt{80} = 4\sqrt{5}~\text{m/s}$$ **[1 mark]**

---

**(c) Distance on rough surface [3 marks]**

On the rough horizontal surface, friction does work to stop the block: **[1 mark]**

$$KE_\text{bottom} = \text{work done by friction}$$
$$\frac{1}{2}mv^2 = \mu_k mg d$$ **[1 mark]**

Cancel $m$:
$$\frac{1}{2}v^2 = \mu_k g d$$
$$d = \frac{v^2}{2\mu_k g} = \frac{80}{2 \times 0.40 \times 10} = \frac{80}{8.0} = 10~\text{m}$$ **[1 mark]**

---

## Solution 20 — Momentum: Elastic collision **[8 marks]**

**(a) Conserved quantities [1 mark]**

Momentum and kinetic energy are both conserved in an elastic collision. **[1 mark]**

---

**(b) Final velocity of $2.0~\text{kg}$ cart [3 marks]**

For a 1D elastic collision where $m_2$ is initially at rest, the velocity of $m_1$ after collision is: **[1 mark]**

$$v_1' = \frac{m_1 - m_2}{m_1 + m_2} \cdot v_1$$ **[1 mark]**

$$v_1' = \frac{2.0 - 4.0}{2.0 + 4.0} \times 6.0 = \frac{-2.0}{6.0} \times 6.0 = -2.0~\text{m/s}$$

The $2.0~\text{kg}$ cart moves at $2.0~\text{m/s}$ to the **left**. **[1 mark]**

---

**(c) Final velocity of $4.0~\text{kg}$ cart [2 marks]**

Using the formula for $m_2$ initially at rest: **[1 mark]**

$$v_2' = \frac{2m_1}{m_1 + m_2} \cdot v_1 = \frac{2 \times 2.0}{6.0} \times 6.0 = 4.0~\text{m/s}$$

The $4.0~\text{kg}$ cart moves at $4.0~\text{m/s}$ to the **right**. **[1 mark]**

---

**(d) Verify kinetic energy conservation [2 marks]**

Before: $KE_i = \frac{1}{2}(2.0)(6.0)^2 = 36~\text{J}$ **[1 mark]**

After: $KE_f = \frac{1}{2}(2.0)(-2.0)^2 + \frac{1}{2}(4.0)(4.0)^2 = 4.0 + 32 = 36~\text{J}$ **[1 mark]**

$KE_i = KE_f = 36~\text{J}$ ✓ — kinetic energy is conserved.

---

## Solution 21 — Momentum: Impulse and bounce **[7 marks]**

**(a) Speed just before impact [1 mark]**

Using $v^2 = v_0^2 + 2gh$ with $v_0 = 0$ (dropped from rest):
$$v_\text{before} = \sqrt{2gh} = \sqrt{2 \times 10 \times 5.0} = \sqrt{100} = 10~\text{m/s}~\text{downwards}$$ **[1 mark]**

---

**(b) Speed just after impact [1 mark]**

The ball reaches height $3.2~\text{m}$. At the top, $v=0$. Using $v^2 = v_0^2 - 2gh$ in reverse:
$$v_\text{after} = \sqrt{2gh} = \sqrt{2 \times 10 \times 3.2} = \sqrt{64} = 8.0~\text{m/s}~\text{upwards}$$ **[1 mark]**

---

**(c) Impulse from the floor [2 marks]**

Taking upwards as positive: **[1 mark]**

$$J = \Delta p = m(v_f - v_i) = 0.50(8.0 - (-10)) = 0.50 \times 18 = 9.0~\text{N·s}$$

The impulse is $9.0~\text{N·s}$ **upwards**. **[1 mark]**

---

**(d) Average force [2 marks]**

$$J = F_\text{avg} \Delta t$$ **[1 mark]**

$$F_\text{avg} = \frac{J}{\Delta t} = \frac{9.0}{0.040} = 225~\text{N}~\text{upwards}$$ **[1 mark]**

---

**(e) Energy "loss" [1 mark]**

Initial mechanical energy: $mgh = 0.50 \times 10 \times 5.0 = 25~\text{J}$.

Final mechanical energy: $mgh' = 0.50 \times 10 \times 3.2 = 16~\text{J}$.

The $9.0~\text{J}$ difference is converted to thermal energy (heat) and sound during the inelastic deformation of the ball on impact. **[1 mark]**

---

## Solution 22 — Rigid Body: Static equilibrium **[8 marks] [HL]**

**(a) Free-body diagram [2 marks]**

Forces on the beam:
- Weight of beam: $W_\text{beam} = 30 \times 10 = 300~\text{N}$, acting downwards at the centre ($2.0~\text{m}$ from pivot)
- Weight of hanging mass: $W_\text{mass} = 40 \times 10 = 400~\text{N}$, acting downwards at $3.0~\text{m}$ from pivot
- Tension $T$ in cable: upwards at the right end ($4.0~\text{m}$ from pivot)
- Reaction force $R$ at pivot: unknown magnitude, upwards

[2 marks: 1 for all forces, 1 for correct positions/directions]

---

**(b) Tension in the cable [4 marks]**

Take torques about the pivot (positive = anticlockwise): **[1 mark]**

$$\sum \tau = 0 \quad\text{(rotational equilibrium)}$$ **[1 mark]**

Clockwise torques (negative): $W_\text{beam}$ at $2.0~\text{m}$ and $W_\text{mass}$ at $3.0~\text{m}$.

Anticlockwise torque (positive): $T$ at $4.0~\text{m}$.

$$T \times 4.0 - 300 \times 2.0 - 400 \times 3.0 = 0$$ **[1 mark]**

$$4.0T = 600 + 1200 = 1800$$
$$T = \frac{1800}{4.0} = 450~\text{N}$$ **[1 mark]**

---

**(c) Reaction force at pivot [2 marks]**

From translational equilibrium (vertical): **[1 mark]**

$$R + T = W_\text{beam} + W_\text{mass}$$
$$R + 450 = 300 + 400 = 700$$
$$R = 250~\text{N}~\text{upwards}$$ **[1 mark]**

---

## Solution 23 — Rigid Body: Angular momentum **[1 mark] [HL]**

**[a] Correct answer: D — $8.0~\text{rad/s}$**

**[b] Step-by-step reasoning:**

In the absence of external torques, angular momentum is conserved:
$$L_i = L_f$$
$$I_i \omega_i = I_f \omega_f$$
$$(4.0)(2.0) = (1.0)\omega_f$$
$$\omega_f = 8.0~\text{rad/s}$$

**Why each wrong answer is wrong:**
- **A ($0.50~\text{rad/s}$):** Divides $\omega_i$ by the ratio of moments of inertia: $2.0 / 4 = 0.5$ — gets the inverse relationship.
- **B ($2.0~\text{rad/s}$):** Assumes angular velocity stays the same when moment of inertia changes — ignores conservation of angular momentum.
- **C ($4.0~\text{rad/s}$):** Uses $I_i/I_f = 4$ and multiplies by $1$ instead of $2$, or uses the wrong conservation law. Possibly $\omega_f = \omega_i \times (I_i/I_f)^{1/2} = 2.0 \times 2 = 4.0$.

---

## Solution 24 — Rigid Body: Rolling without slipping **[8 marks] [HL]**

**(a) Show $KE = \frac{3}{4}Mv^2$ [3 marks]**

Total KE = translational KE + rotational KE: **[1 mark]**

$$KE = \frac{1}{2}Mv^2 + \frac{1}{2}I\omega^2$$ **[1 mark]**

For rolling without slipping: $\omega = v/R$. For a solid cylinder: $I = \frac{1}{2}MR^2$.

$$KE = \frac{1}{2}Mv^2 + \frac{1}{2}\left(\frac{1}{2}MR^2\right)\left(\frac{v}{R}\right)^2$$
$$= \frac{1}{2}Mv^2 + \frac{1}{4}Mv^2$$
$$= \frac{3}{4}Mv^2$$ **[1 mark]**

---

**(b) Translational speed at bottom [3 marks]**

By conservation of energy ($KE_\text{initial} = 0$, $GPE_\text{initial} = Mgh$): **[1 mark]**

$$Mgh = \frac{3}{4}Mv^2$$ **[1 mark]**

Cancel $M$:
$$v^2 = \frac{4}{3}gh = \frac{4}{3}(10)(1.2) = \frac{48}{3} = 16$$
$$v = 4.0~\text{m/s}$$ **[1 mark]**

---

**(c) Angular velocity at bottom [2 marks]**

$$\omega = \frac{v}{R}$$ **[1 mark]**

$$\omega = \frac{4.0}{0.20} = 20~\text{rad/s}$$ **[1 mark]**

---

## Solution 25 — Special Relativity: Muon dilemma **[8 marks] [HL]**

**(a) Lorentz factor [1 mark]**

$$\gamma = \frac{1}{\sqrt{1 - v^2/c^2}} = \frac{1}{\sqrt{1 - (0.80)^2}} = \frac{1}{\sqrt{1 - 0.64}} = \frac{1}{\sqrt{0.36}} = \frac{1}{0.60} = \frac{5}{3}$$ **[1 mark]**

---

**(b) Dilated mean lifetime in Earth frame [1 mark]**

$$\tau = \gamma \tau_0 = \frac{5}{3} \times 2.0 = \frac{10}{3}~\mu\text{s} \approx 3.33~\mu\text{s}$$ **[1 mark]**

---

**(c) Mean distance in one dilated lifetime [2 marks]**

$$d = v \tau$$ **[1 mark]**

$$d = (0.80 \times 3.0 \times 10^8) \times \left(\frac{10}{3} \times 10^{-6}\right)$$
$$= 0.80 \times 3.0 \times 10^8 \times \frac{10}{3} \times 10^{-6}$$
$$= 0.80 \times 1000 = 800~\text{m}$$ **[1 mark]**

---

**(d) Explanation [2 marks]**

Without relativity, the muon would travel only $v\tau_0 = 0.80 \times 3.0 \times 10^8 \times 2.0 \times 10^{-6} = 480~\text{m}$ in one proper lifetime. **[1 mark]**

At $480~\text{m}$ per lifetime, reaching $10~\text{km}$ would require over 20 half-lives (in fact over 20 **mean** lifetimes), meaning virtually all muons would decay before reaching the surface.

With time dilation, the muon's lifetime in the Earth frame is stretched by $\gamma = 5/3$, giving it a mean travel distance of $800~\text{m}$ per dilated lifetime. This dramatically increases the probability that a muon survives the journey to sea level — equivalent to requiring fewer lifetimes to cover $10~\text{km}$. **[1 mark]**

---

**(e) Length-contracted distance in muon frame [2 marks]**

In the muon's rest frame, the $10~\text{km}$ distance (Earth frame) is length-contracted: **[1 mark]**

$$L = \frac{L_0}{\gamma} = \frac{10}{5/3} = 10 \times \frac{3}{5} = 6.0~\text{km}$$ **[1 mark]**

In the muon frame, the Earth's surface approaches at $0.80c$ and only needs to cover $6.0~\text{km}$, taking $6000/(0.80 \times 3 \times 10^8) = 25~\mu\text{s}$ in the Earth frame. In the muon's proper time, this is $25/\gamma = 15~\mu\text{s} = 7.5$ proper lifetimes — a substantial fraction survive.

---

## Mark Scheme Summary

| Question | Topic | Style | Marks | Key Answer(s) |
|----------|-------|-------|-------|---------------|
| Q1 | Kinematics | P1 MCQ | 1 | B — $100~\text{m}$ |
| Q2 | Kinematics | P1 MCQ | 1 | C — $120~\text{m}$ |
| Q3 | Kinematics | P1 MCQ | 1 | B — $8.0~\text{s}$ |
| Q4 | Kinematics | P1 MCQ | 1 | C — $40~\text{m/s}$ |
| Q5 | Forces | P1 MCQ | 1 | D — $20~\text{m/s}$ |
| Q6 | Forces | P1 MCQ | 1 | B — $0.58$ |
| Q7 | Forces | P1 MCQ | 1 | C — $800~\text{N}$ |
| Q8 | Energy | P1 MCQ | 1 | B — $50~\text{J}$ |
| Q9 | Energy | P1 MCQ | 1 | C — $1000~\text{W}$ |
| Q10 | Momentum | P1 MCQ | 1 | A — $10~\text{N·s}$ |
| Q11 | Momentum | P1 MCQ | 1 | A — $1/4$ |
| Q12 | Rigid Body | P1 MCQ | 1 | B — $12~\text{N·m}$ |
| Q13 | Relativity | P1 MCQ | 1 | C — $10.0~\text{years}$ |
| Q14 | Kinematics — Projectile | P2 | 9 | $v_x=20$, $v_y=15$; $t=3.0$; $R=60$; $h=11.25$; $v=25$ |
| Q15 | Kinematics — Data | P2 | 6 | $x/t^2 = 1.00$; $a = 2.0$; $\sin\theta=0.20$ |
| Q16 | Forces — Connected | P2 | 8 | $a = 2.0$; $T = 8.0$ |
| Q17 | Forces — Circular | P2 | 7 | $\omega=6\pi$; $a_c=18\pi^2$; $T=36\pi^2$; $\omega_\text{max}=20$ |
| Q18 | Energy — Spring | P2 | 6 | $KE_i=25$; $x_\text{max}=0.50$; $v=4.0$ |
| Q19 | Energy — Incline | P2 | 6 | $\sin\theta=0.40$; $v=\sqrt{80}=4\sqrt{5}$; $d=10$ |
| Q20 | Momentum — Elastic | P2 | 8 | $v_1'=-2.0$ (left); $v_2'=4.0$ (right); $KE=36$ both sides |
| Q21 | Momentum — Impulse | P2 | 7 | $v_b=10$↓, $v_a=8$↑; $J=9.0$↑; $F_\text{avg}=225$ |
| Q22 | Rigid Body — Equilibrium | P2 | 8 | $T=450$; $R=250$↑ |
| Q23 | Rigid Body — Angular | P1 MCQ | 1 | D — $8.0~\text{rad/s}$ |
| Q24 | Rigid Body — Rolling | P2 | 8 | $KE=\frac{3}{4}Mv^2$; $v=4.0$; $\omega=20$ |
| Q25 | Relativity — Muons | P2 | 8 | $\gamma=5/3$; $\tau=10/3~\mu\text{s}$; $d=800~\text{m}$; $L=6.0~\text{km}$ |

### Totals by Topic

| Topic | Questions | MCQ marks | P2 marks | Total marks |
|-------|-----------|-----------|----------|-------------|
| Kinematics | Q1–Q4, Q14–Q15 | 4 | 15 | **19** |
| Forces | Q5–Q7, Q16–Q17 | 3 | 15 | **18** |
| Energy | Q8–Q9, Q18–Q19 | 2 | 12 | **14** |
| Momentum | Q10–Q11, Q20–Q21 | 2 | 15 | **17** |
| Rigid Body | Q12, Q22–Q24 | 2 | 16 | **18** |
| Relativity (HL) | Q13, Q25 | 1 | 8 | **9** |
| **Grand Total** | **25 questions** | **14** | **81** | **95 marks** |

---

**End of Solutions**
