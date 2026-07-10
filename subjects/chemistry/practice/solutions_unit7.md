# Unit 7: Acids &amp; Bases — Solutions

## Problem 1

The two conjugate acid–base pairs are:

- **Pair 1**: $\ce{CH3COOH}$ (acid) and $\ce{CH3COO-}$ (conjugate base)
- **Pair 2**: $\ce{H3O+}$ (conjugate acid) and $\ce{H2O}$ (base)

**Explanation of Pair 1**: In the forward reaction, $\ce{CH3COOH}$ donates a proton ($\ce{H+}$) to $\ce{H2O}$, forming the ethanoate ion $\ce{CH3COO-}$. The species $\ce{CH3COOH}$ and $\ce{CH3COO-}$ are a conjugate pair because they differ by exactly one proton: the acid has one more proton than its conjugate base. In the reverse reaction, $\ce{CH3COO-}$ accepts a proton from $\ce{H3O+}$, regenerating $\ce{CH3COOH}$.

**Pitfall**: Students sometimes identify $\ce{H2O}$ and $\ce{OH-}$ as a conjugate pair — but hydroxide does not appear in this equilibrium. Always check what species are actually present in the equation.

---

## Problem 2

**Step 1: Calculate pH.**
The formula for pH is $\text{pH} = -\log_{10}[\ce{H+}]$. Since $\ce{HCl}$ is a strong acid, $[\ce{H+}] = [\ce{H3O+}] = 3.2 \times 10^{-6}\ \text{mol}\ \text{dm}^{-3}$.

$$\text{pH} = -\log_{10}(3.2 \times 10^{-6}) = 5.49$$

**Step 2: Calculate $[\ce{OH-}]$.**
Using the ionic product of water: $K_w = [\ce{H+}][\ce{OH-}] = 1.0 \times 10^{-14}$ at 298 K.

$$[\ce{OH-}] = \frac{K_w}{[\ce{H+}]} = \frac{1.0 \times 10^{-14}}{3.2 \times 10^{-6}} = 3.1 \times 10^{-9}\ \text{mol}\ \text{dm}^{-3}$$

**Interpretation**: pH = 5.49 < 7, so the rainwater is acidic (due to dissolved $\ce{CO2}$ forming carbonic acid).

**Pitfall**: Always check that $[\ce{H+}][\ce{OH-}] = 1.0 \times 10^{-14}$ — if your two values don't multiply to $10^{-14}$, you've made a calculation error.

---

## Problem 3

**Step 1: Calculate $[\ce{H+}]$ from pH.**
$$\text{pH} = 1.70 \implies [\ce{H+}] = 10^{-\text{pH}} = 10^{-1.70} = 0.020\ \text{mol}\ \text{dm}^{-3}$$

Since $\ce{HCl}$ is a strong monoprotic acid and dissociates completely, $[\ce{HCl}]_{\text{initial}} = [\ce{H+}] = 0.020\ \text{mol}\ \text{dm}^{-3}$.

**Step 2: Calculate pOH.**
$$\text{pOH} = 14.00 - \text{pH} = 14.00 - 1.70 = 12.30$$

**Interpretation**: A low pH means high acidity. The pOH is correspondingly high, reflecting the extremely low $[\ce{OH-}]$ in a strongly acidic solution.

**Pitfall**: $10^{-1.70}$ is not $10^{-1} \times 10^{-0.70}$ in the sense of simple multiplication. Use: $10^{-1.70} = 10^{-2} \times 10^{0.30} = 0.01 \times 2.0 = 0.020$.

---

## Problem 4

**Step 1: Calculate moles of $\ce{NaOH}$.**
$$n(\ce{NaOH}) = \frac{m}{M} = \frac{0.40\ \text{g}}{40.0\ \text{g}\ \text{mol}^{-1}} = 0.010\ \text{mol}$$

**Step 2: Calculate concentration.**
$$[\ce{NaOH}] = \frac{n}{V} = \frac{0.010\ \text{mol}}{0.500\ \text{dm}^3} = 0.020\ \text{mol}\ \text{dm}^{-3}$$

**Step 3: Calculate $[\ce{OH-}]$ and pOH.**
$\ce{NaOH}$ is a strong base and dissociates completely: $[\ce{OH-}] = 0.020\ \text{mol}\ \text{dm}^{-3}$.

$$\text{pOH} = -\log_{10}(0.020) = 1.70$$

**Step 4: Calculate pH.**
$$\text{pH} = 14.00 - \text{pOH} = 14.00 - 1.70 = 12.30$$

**Pitfall**: Don't forget to convert cm³ to dm³! $500\ \text{cm}^3 = 0.500\ \text{dm}^3$.

---

## Problem 5

**Step 1: Calculate $[\ce{H+}]$ from pH.**
$$[\ce{H+}] = 10^{-\text{pH}} = 10^{-2.87} = 1.35 \times 10^{-3}\ \text{mol}\ \text{dm}^{-3}$$

**Step 2: Determine equilibrium concentrations.**
Weak acid dissociation: $\ce{HA <=> H+ + A-}$

| | $\ce{HA}$ | $\ce{H+}$ | $\ce{A-}$ |
|---|---|---|---|
| Initial | 0.10 | 0 | 0 |
| Change | $-x$ | $+x$ | $+x$ |
| Equilibrium | $0.10 - x$ | $x$ | $x$ |

From the pH, $x = [\ce{H+}] = 1.35 \times 10^{-3}\ \text{mol}\ \text{dm}^{-3}$.

**Step 3: Calculate $K_a$.**
$$K_a = \frac{[\ce{H+}][\ce{A-}]}{[\ce{HA}]} = \frac{x \cdot x}{0.10 - x} = \frac{(1.35 \times 10^{-3})^2}{0.10 - 1.35 \times 10^{-3}}$$

Since $x \ll 0.10$ (it's about 1.35% of 0.10), we can approximate $0.10 - x \approx 0.10$ to give:

$$K_a \approx \frac{(1.35 \times 10^{-3})^2}{0.10} = \frac{1.82 \times 10^{-6}}{0.10} = 1.8 \times 10^{-5}$$

**Step 4: Calculate $\text{p}K_a$.**
$$\text{p}K_a = -\log_{10}(K_a) = -\log_{10}(1.8 \times 10^{-5}) = 4.74$$

**Pitfall**: Always check that $x$ is less than 5% of the initial concentration before using the approximation. Here, $1.35 \times 10^{-3} / 0.10 = 1.35\%$, so the approximation is valid.

---

## Problem 6

**Step 1: Convert $\text{p}K_a$ to $K_a$.**
$$K_a = 10^{-\text{p}K_a} = 10^{-3.75} = 1.78 \times 10^{-4}$$

**Step 2: Set up ICE table for $\ce{HCOOH <=> H+ + HCOO-}$.**

| | $\ce{HCOOH}$ | $\ce{H+}$ | $\ce{HCOO-}$ |
|---|---|---|---|
| Initial | 0.20 | 0 | 0 |
| Change | $-x$ | $+x$ | $+x$ |
| Equilibrium | $0.20 - x$ | $x$ | $x$ |

$$K_a = \frac{x^2}{0.20 - x} = 1.78 \times 10^{-4}$$

**Step 3: Apply approximation.**
Assume $x \ll 0.20$, so $0.20 - x \approx 0.20$:

$$x^2 = (1.78 \times 10^{-4})(0.20) = 3.56 \times 10^{-5}$$
$$x = \sqrt{3.56 \times 10^{-5}} = 5.97 \times 10^{-3}$$

Check approximation: $\frac{5.97 \times 10^{-3}}{0.20} \times 100\% = 3.0\% < 5\%$, so the approximation is valid.

**Step 4: Calculate pH.**
$$\text{pH} = -\log_{10}(5.97 \times 10^{-3}) = 2.22$$

**Assumption**: That $x$ is negligible compared to the initial concentration (less than 5% dissociation). This is valid because methanoic acid is a weak acid with a relatively small $K_a$, so it is only slightly dissociated at this concentration.

---

## Problem 7

**Step 1: Use the relationship $K_a \times K_b = K_w$.**
For a conjugate acid–base pair: $K_a(\ce{CH3COOH}) \times K_b(\ce{CH3COO-}) = K_w = 1.0 \times 10^{-14}$.

$$K_b(\ce{CH3COO-}) = \frac{K_w}{K_a} = \frac{1.0 \times 10^{-14}}{1.8 \times 10^{-5}} = 5.6 \times 10^{-10}$$

**Step 2: Calculate $\text{p}K_b$.**
$$\text{p}K_b = -\log_{10}(5.6 \times 10^{-10}) = 9.25$$

Alternatively: $\text{p}K_a + \text{p}K_b = 14.00$.

$$\text{p}K_a = -\log_{10}(1.8 \times 10^{-5}) = 4.74$$
$$\text{p}K_b = 14.00 - 4.74 = 9.26 \quad \text{(consistent with the above)}$$

**Explanation of the relationship**: $K_a \times K_b = K_w$ arises because:
$$\ce{HA + H2O <=> H3O+ + A-} \quad K_a = \frac{[\ce{H3O+}][\ce{A-}]}{[\ce{HA}]}$$
$$\ce{A- + H2O <=> HA + OH-} \quad K_b = \frac{[\ce{HA}][\ce{OH-}]}{[\ce{A-}]}$$

Multiplying: $K_a \times K_b = \frac{[\ce{H3O+}][\ce{A-}]}{[\ce{HA}]} \times \frac{[\ce{HA}][\ce{OH-}]}{[\ce{A-}]} = [\ce{H3O+}][\ce{OH-}] = K_w$.

---

## Problem 8

The $\text{p}K_a$ of chloroethanoic acid (2.86) is lower than that of ethanoic acid (4.76), meaning chloroethanoic acid is a stronger acid.

**Reason**: The chlorine atom in chloroethanoic acid is highly electronegative and exerts an **electron-withdrawing inductive effect** ($-I$ effect) through the $\sigma$-bond framework. This pulls electron density away from the carboxyl group ($\ce{-COOH}$), which:

1. **Weakens the $\ce{O-H}$ bond** in the acid, making the proton easier to donate.
2. **Stabilises the conjugate base** ($\ce{ClCH2COO-}$) by dispersing the negative charge more effectively than in the ethanoate ion ($\ce{CH3COO-}$). A more stable conjugate base shifts the dissociation equilibrium to the right, increasing $K_a$ and thus lowering $\text{p}K_a$.

This is a classic example of how substituent effects (specifically inductive effects) influence acid strength.

---

## Problem 9

**Step 1: Calculate pH using the Henderson–Hasselbalch equation.**

Since the acid and its conjugate base are present at equal concentrations:

$$\text{pH} = \text{p}K_a + \log_{10}\frac{[\ce{A-}]}{[\ce{HA}]}$$

$$\text{p}K_a = -\log_{10}(1.8 \times 10^{-5}) = 4.74$$

$$\text{pH} = 4.74 + \log_{10}\frac{0.050}{0.050} = 4.74 + \log_{10}(1) = 4.74 + 0 = 4.74$$

**Step 2: Buffer mechanism when $\ce{HCl}$ is added.**

When a small amount of $\ce{HCl}$ (strong acid) is added, it dissociates completely to give $\ce{H+}$ ions. The buffer resists pH change as follows:

The ethanoate ions (the basic component) react with the added $\ce{H+}$:

$$\ce{CH3COO-(aq) + H+(aq) -> CH3COOH(aq)}$$

This converts the strong acid ($\ce{H+}$) into the weak acid ($\ce{CH3COOH}$), which only partially dissociates. As a result, the concentration of free $\ce{H+}$ ions increases only very slightly, and the pH remains nearly constant. The ratio $[\ce{CH3COO-}]/[\ce{CH3COOH}]$ changes slightly, but since both concentrations are large relative to the amount of $\ce{H+}$ added, the pH change is minimal.

---

## Problem 10

**Step 1: Calculate the new concentrations after mixing.**

Total volume = $40.0 + 60.0 = 100.0\ \text{cm}^3 = 0.100\ \text{dm}^3$.

Moles of $\ce{CH3COOH}$: $n = 0.100 \times 0.0400 = 0.00400\ \text{mol}$.

Moles of $\ce{CH3COO-}$: $n = 0.100 \times 0.0600 = 0.00600\ \text{mol}$.

Since both species are in the same total volume, we can use the mole ratio directly in the Henderson–Hasselbalch equation:

$$\text{pH} = \text{p}K_a + \log_{10}\frac{n(\ce{A-})}{n(\ce{HA})}$$

$$\text{p}K_a = -\log_{10}(1.8 \times 10^{-5}) = 4.74$$

$$\text{pH} = 4.74 + \log_{10}\frac{0.00600}{0.00400} = 4.74 + \log_{10}(1.50) = 4.74 + 0.176 = 4.92$$

**Pitfall**: When both species are dissolved in the same final volume, the volume cancels in the ratio $[\ce{A-}]/[\ce{HA}]$, so you can use the mole ratio directly. This is a useful shortcut in buffer calculations.

---

## Problem 11

**Step 1: Determine moles before reaction.**

Moles of propanoic acid: $n(\ce{C2H5COOH}) = 0.200 \times 0.0500 = 0.0100\ \text{mol}$.

Moles of $\ce{NaOH}$: $n(\ce{NaOH}) = 0.200 \times 0.0250 = 0.00500\ \text{mol}$.

**Step 2: Neutralisation reaction.**

$$\ce{C2H5COOH + OH- -> C2H5COO- + H2O}$$

The $\ce{NaOH}$ completely neutralises 0.00500 mol of the acid, producing 0.00500 mol of propanoate ions.

After reaction:
- $n(\ce{C2H5COOH}) = 0.0100 - 0.00500 = 0.00500\ \text{mol}$
- $n(\ce{C2H5COO-}) = 0.00500\ \text{mol}$

Total volume = $50.0 + 25.0 = 75.0\ \text{cm}^3$.

**Step 3: Calculate pH.**

Since the acid and conjugate base are present in equal amounts:

$$\text{p}K_a = -\log_{10}(1.3 \times 10^{-5}) = 4.89$$

$$\text{pH} = \text{p}K_a + \log_{10}\frac{0.00500}{0.00500} = 4.89 + 0 = 4.89$$

This is an example of the **half-neutralisation** method of buffer preparation: when half the weak acid has been neutralised, $[\ce{HA}] = [\ce{A-}]$ and $\text{pH} = \text{p}K_a$.

---

## Problem 12

**Step 1: Calculate pH using the Henderson–Hasselbalch equation.**

$$\text{p}K_a = -\log_{10}(2.5 \times 10^{-6}) = 5.60$$

$$\text{pH} = 5.60 + \log_{10}\frac{0.015}{0.010} = 5.60 + \log_{10}(1.5) = 5.60 + 0.176 = 5.78$$

**Step 2: Assess buffer effectiveness at pH = 2.0.**

The buffer range is $\text{p}K_a \pm 1$, i.e., pH 4.60 to 6.60. A pH of 2.0 is far outside this range. At pH = 2.0, the ratio $[\ce{A-}]/[\ce{HA}]$ would need to be:

$$\frac{[\ce{A-}]}{[\ce{HA}]} = 10^{\text{pH} - \text{p}K_a} = 10^{2.0 - 5.60} = 10^{-3.6} \approx 2.5 \times 10^{-4}$$

This means essentially all of the $\ce{A-}$ would be protonated to $\ce{HA}$, and the buffer would have virtually no capacity to neutralise added acid. The buffer is **not effective** at pH = 2.0.

---

## Problem 13

**Key features of the weak-acid–strong-base titration curve ($\ce{CH3COOH}$ vs $\ce{NaOH}$):**

1. **Initial pH**: The initial pH is relatively high (around 2.9 for $0.10\ \text{mol}\ \text{dm}^{-3}$ ethanoic acid) compared to a strong acid, because ethanoic acid is only partially dissociated.

2. **Buffer region**: After the first addition of $\ce{NaOH}$, the pH rises gradually. A buffer system ($\ce{CH3COOH}/\ce{CH3COO-}$) is established, and the curve is relatively flat in the middle region. The pH changes slowly because the buffer resists pH change.

3. **Half-equivalence point**: At 12.5 cm³ of $\ce{NaOH}$ added (halfway to equivalence), $[\ce{CH3COOH}] = [\ce{CH3COO-}]$, giving $\text{pH} = \text{p}K_a \approx 4.74$. The curve is at its flattest here (maximum buffer capacity).

4. **Equivalence point**: At 25.0 cm³, all the acid has been neutralised. The solution contains only sodium ethanoate, $\ce{CH3COONa}$. The pH at the equivalence point is **approximately 8.7**, which is **greater than 7.00**.

   **Reason**: The ethanoate ion, $\ce{CH3COO-}$, is the conjugate base of a weak acid and undergoes hydrolysis:
   $$\ce{CH3COO-(aq) + H2O(l) <=> CH3COOH(aq) + OH-(aq)}$$
   This produces $\ce{OH-}$ ions, making the solution basic at the equivalence point.

5. **Beyond equivalence**: Excess $\ce{NaOH}$ dominates, and the pH rises sharply then levels off near pH 13, similar to a strong-acid–strong-base titration beyond equivalence.

---

## Problem 14

**Sketch description**: The titration of a weak base ($\ce{NH3}$) with a strong acid ($\ce{HCl}$) produces a curve that starts at a moderately high pH (around 11.1 for $0.10\ \text{mol}\ \text{dm}^{-3}$ $\ce{NH3}$), decreases gradually through a buffer region, drops sharply at the equivalence point, and then levels off at low pH.

**pH at equivalence point**: The equivalence point pH is **less than 7.00** (approximately 5.3).

**Justification**: At the equivalence point, all the $\ce{NH3}$ has been converted to $\ce{NH4+}$ ions (the ammonium ion). The salt present in solution is ammonium chloride, $\ce{NH4Cl}$. The ammonium ion is the conjugate acid of the weak base $\ce{NH3}$ and undergoes hydrolysis:

$$\ce{NH4+(aq) + H2O(l) <=> NH3(aq) + H3O+(aq)}$$

This produces $\ce{H3O+}$ ions, making the solution acidic at the equivalence point.

The curve is essentially the mirror image (reflected vertically) of a weak-acid–strong-base titration.

---

## Problem 15

**Step 1: Recognise the situation.**

The student has added 25.0 cm³ of $0.10\ \text{mol}\ \text{dm}^{-3}$ $\ce{NaOH}$ to 25.0 cm³ of $0.10\ \text{mol}\ \text{dm}^{-3}$ $\ce{CH3COOH}$. At this point, exactly half the acid has been neutralised (the equivalence point would require 25.0 cm³ total, so we are at 12.5 cm³ — **wait, re-read**: both are the same volume and concentration. Moles of acid = $0.10 \times 0.0250 = 0.00250\ \text{mol}$, moles of $\ce{NaOH}$ = $0.00250\ \text{mol}$. This is actually the **equivalence point**, not the half-equivalence point!

The problem states "show that pH ≈ 8.7" — let's recalculate. At the equivalence point, all the ethanoic acid is converted to ethanoate. The ethanoate ion hydrolyses:

**Step 2: Calculate $K_b$ for ethanoate.**
$$K_b = \frac{K_w}{K_a} = \frac{1.0 \times 10^{-14}}{1.8 \times 10^{-5}} = 5.56 \times 10^{-10}$$

**Step 3: Calculate concentration of ethanoate at equivalence.**
Total volume = $50.0\ \text{cm}^3$. Moles of $\ce{CH3COO-}$ = 0.00250 mol (all from neutralisation).

$$[\ce{CH3COO-}] = \frac{0.00250}{0.0500} = 0.0500\ \text{mol}\ \text{dm}^{-3}$$

**Step 4: Hydrolysis equilibrium.**
$$\ce{CH3COO- + H2O <=> CH3COOH + OH-}$$

$$K_b = \frac{[\ce{CH3COOH}][\ce{OH-}]}{[\ce{CH3COO-}]} = \frac{x^2}{0.0500 - x}$$

Assume $x \ll 0.0500$:

$$x^2 = (5.56 \times 10^{-10})(0.0500) = 2.78 \times 10^{-11}$$
$$x = [\ce{OH-}] = \sqrt{2.78 \times 10^{-11}} = 5.27 \times 10^{-6}$$

$$\text{pOH} = -\log_{10}(5.27 \times 10^{-6}) = 5.28$$
$$\text{pH} = 14.00 - 5.28 = 8.72 \approx 8.7$$

This confirms the pH at the equivalence point.

**Half-equivalence point significance**: The half-equivalence point occurs when exactly half the acid has been neutralised. At this point, $[\ce{HA}] = [\ce{A-}]$, and from the Henderson–Hasselbalch equation, $\text{pH} = \text{p}K_a$. This is a crucial concept because the $\text{p}K_a$ of a weak acid can be read directly from the titration curve at the half-equivalence point.

**Note on problem wording**: The problem says "adds 25.0 cm³ NaOH to 25.0 cm³ CH3COOH" — equal volumes and concentrations means this is the equivalence point. The half-equivalence point would be at 12.5 cm³ NaOH added.

---

## Problem 16

**Step 1: Determine $\text{p}K_a$ and $K_a$.**

At the half-equivalence point, $\text{pH} = \text{p}K_a$. Therefore:

$$\text{p}K_a = 4.52$$
$$K_a = 10^{-4.52} = 3.0 \times 10^{-5}$$

**Step 2: Explain the theoretical basis.**

During the titration of a weak acid $\ce{HA}$ with a strong base, at the half-equivalence point exactly half the acid has been neutralised:

$$\ce{HA + OH- -> A- + H2O}$$

Moles of $\ce{HA}$ remaining = moles of $\ce{A-}$ formed. Since both are in the same total volume:

$$[\ce{HA}] = [\ce{A-}]$$

From the acid dissociation constant expression:

$$K_a = \frac{[\ce{H+}][\ce{A-}]}{[\ce{HA}]}$$

When $[\ce{HA}] = [\ce{A-}]$, the expression simplifies to:

$$K_a = [\ce{H+}]$$

Taking negative logarithms: $\text{p}K_a = \text{pH}$.

This is why the half-equivalence point on a titration curve directly yields the $\text{p}K_a$ of the weak acid. It is a standard method for experimentally determining $K_a$.

---

## Problem 17

(a) **$\ce{HCl}$ vs $\ce{NaOH}$ (strong acid–strong base)**: The equivalence point pH is 7.00. Either phenolphthalein or methyl orange would work, but **phenolphthalein** is commonly preferred because its colour change from colourless to pink at pH 8.2–10.0 is sharp and easy to detect. The steep portion of a strong-acid–strong-base curve spans several pH units, so the endpoint will be very close to the equivalence point regardless. Bromothymol blue (pH 6.0–7.6) is actually the best choice for this titration.

(b) **$\ce{CH3COOH}$ vs $\ce{NaOH}$ (weak acid–strong base)**: The equivalence point pH is approximately 8.7 (basic), so **phenolphthalein** (pH range 8.2–10.0) is the appropriate indicator. Its $\text{p}K_a$ (~9.3) is close to the equivalence point pH. Methyl orange would change colour at pH 3.1–4.4, long before the equivalence point, giving a large systematic error.

(c) **$\ce{HCl}$ vs $\ce{NH3}$ (strong acid–weak base)**: The equivalence point pH is approximately 5.3 (acidic), so **methyl orange** (pH range 3.1–4.4) is more appropriate, although the equivalence point pH of 5.3 is slightly above its range. In practice, methyl orange works reasonably well for this titration because the curve drops sharply in the acidic region. Phenolphthalein would change colour too early (at pH ~8–10), well before the equivalence point.

---

## Problem 18

**Definitions**:
- A **Lewis acid** is an electron pair acceptor.
- A **Lewis base** is an electron pair donor.

In the reaction $\ce{BF3 + NH3 -> F3B-NH3}$:

- **$\ce{BF3}$ is the Lewis acid**. The boron atom in $\ce{BF3}$ has only six electrons in its valence shell (it is electron-deficient). It can accept a lone pair of electrons to complete its octet.
- **$\ce{NH3}$ is the Lewis base**. The nitrogen atom in ammonia has a lone pair of electrons that it can donate to form a coordinate (dative covalent) bond.

The product, $\ce{F3B-NH3}$, contains an $\ce{N->B}$ dative bond formed by donation of the nitrogen lone pair into the empty $p$-orbital of boron.

This reaction extends the Brønsted–Lowry definition (which requires proton transfer) to include species that can accept or donate electron pairs without any proton being involved.

---

## Problem 19

**$\ce{AlCl3}$**: The aluminium atom in $\ce{AlCl3}$ has only six valence electrons (three bonds to chlorine), making it electron-deficient. It can accept an electron pair to complete its octet — this makes it a Lewis acid. Reaction with water:

$$\ce{AlCl3 + H2O -> Cl3Al-OH2}$$

The water molecule donates a lone pair from its oxygen atom to the aluminium, acting as a Lewis base.

**$\ce{[Cu(H2O)6]^{2+}}$**: The central $\ce{Cu^{2+}}$ ion has a high charge density and can accept electron pairs. Water molecules are coordinated as ligands, but the $\ce{Cu^{2+}}$ ion can also polarise the $\ce{O-H}$ bonds of coordinated water, making them acidic. More directly, the hydrated copper(II) ion acts as a Lewis acid because the $\ce{Cu^{2+}}$ centre can accept a lone pair from an incoming ligand. Reaction:

$$\ce{[Cu(H2O)6]^{2+} + H2O <=> [Cu(H2O)5(OH)]+ + H3O+}$$

Here, the $\ce{Cu^{2+}}$ polarises a coordinated water molecule, facilitating proton loss, but the fundamental Lewis acidity arises from the ability of $\ce{Cu^{2+}}$ (an ion with vacant $d$-orbitals) to accept electron pairs.

---

## Problem 20

**Why successive $K_a$ values decrease**: Each successive dissociation removes a proton from a species that is increasingly negatively charged:

- $\ce{H3PO4}$ (neutral) → loses $\ce{H+}$ → $\ce{H2PO4-}$ (charge −1)
- $\ce{H2PO4-}$ (charge −1) → loses $\ce{H+}$ → $\ce{HPO4^{2-}}$ (charge −2)
- $\ce{HPO4^{2-}}$ (charge −2) → loses $\ce{H+}$ → $\ce{PO4^{3-}}$ (charge −3)

It becomes progressively more difficult to remove a positively charged proton from an increasingly negatively charged species due to increasing electrostatic attraction. This is why $K_{a1} > K_{a2} > K_{a3}$. The large differences (roughly $10^5$ between each) are typical for polyprotic acids.

**pH calculation**: Since $K_{a1} \gg K_{a2} \gg K_{a3}$, the pH is dominated by the **first dissociation**. We treat $\ce{H3PO4}$ as a monoprotic weak acid with $K_a = 7.1 \times 10^{-3}$.

For $[\ce{H3PO4}] = 0.10\ \text{mol}\ \text{dm}^{-3}$:

$$K_{a1} = \frac{[\ce{H+}][\ce{H2PO4-}]}{[\ce{H3PO4}]} = \frac{x^2}{0.10 - x} = 7.1 \times 10^{-3}$$

Here, $K_{a1}$ is relatively large, so the approximation $x \ll 0.10$ may not be valid. Solve the quadratic:

$$x^2 = 7.1 \times 10^{-3}(0.10 - x)$$
$$x^2 + 7.1 \times 10^{-3}x - 7.1 \times 10^{-4} = 0$$

$$x = \frac{-7.1 \times 10^{-3} + \sqrt{(7.1 \times 10^{-3})^2 + 4(7.1 \times 10^{-4})}}{2}$$
$$x = \frac{-7.1 \times 10^{-3} + \sqrt{5.04 \times 10^{-5} + 2.84 \times 10^{-3}}}{2}$$
$$x = \frac{-7.1 \times 10^{-3} + \sqrt{2.89 \times 10^{-3}}}{2}$$
$$x = \frac{-7.1 \times 10^{-3} + 5.38 \times 10^{-2}}{2} = \frac{4.67 \times 10^{-2}}{2} = 2.33 \times 10^{-2}$$

$$\text{pH} = -\log_{10}(2.33 \times 10^{-2}) = 1.63$$

The contribution from $K_{a2}$ and $K_{a3}$ is negligible (about $10^{-8}$ and $10^{-13}$ mol dm⁻³ in $\ce{H+}$), confirming the assumption.

---

## Problem 21

**Step 1: pH from first dissociation only.**

Since $K_{a1} \gg K_{a2}$ (by a factor of about $10^4$), the first dissociation dominates the $\ce{[H+]}$.

$$\ce{H2CO3 <=> H+ + HCO3-} \quad K_{a1} = 4.3 \times 10^{-7}$$

$$K_{a1} = \frac{[\ce{H+}][\ce{HCO3-}]}{[\ce{H2CO3}]} = \frac{x^2}{0.050 - x}$$

Since $K_{a1}$ is very small, $x \ll 0.050$, so:

$$x^2 = (4.3 \times 10^{-7})(0.050) = 2.15 \times 10^{-8}$$
$$x = [\ce{H+}] = \sqrt{2.15 \times 10^{-8}} = 1.47 \times 10^{-4}\ \text{mol}\ \text{dm}^{-3}$$

$$\text{pH} = -\log_{10}(1.47 \times 10^{-4}) = 3.83$$

**Step 2: Concentration of $\ce{HCO3-}$.**

From the first dissociation, $[\ce{HCO3-}] \approx [\ce{H+}] = 1.47 \times 10^{-4}\ \text{mol}\ \text{dm}^{-3}$.

**Step 3: Concentration of $\ce{CO3^{2-}}$.**

From the second dissociation: $\ce{HCO3- <=> H+ + CO3^{2-}}$, $K_{a2} = 5.6 \times 10^{-11}$.

$$K_{a2} = \frac{[\ce{H+}][\ce{CO3^{2-}}]}{[\ce{HCO3-}]}$$

Since $[\ce{H+}] \approx [\ce{HCO3-}]$ (from the first dissociation), they cancel:

$$K_{a2} \approx [\ce{CO3^{2-}}] = 5.6 \times 10^{-11}\ \text{mol}\ \text{dm}^{-3}$$

This is a well-known result for diprotic acids: when $K_{a1} \gg K_{a2}$, $[\ce{A^{2-}}] \approx K_{a2}$ at equilibrium.

---

## Problem 22

**Step 1: Hydrolysis equation.**

The ethanoate ion, the conjugate base of a weak acid, reacts with water:

$$\ce{CH3COO-(aq) + H2O(l) <=> CH3COOH(aq) + OH-(aq)}$$

**Step 2: Calculate $K_b$ for ethanoate.**
$$K_b = \frac{K_w}{K_a} = \frac{1.0 \times 10^{-14}}{1.8 \times 10^{-5}} = 5.56 \times 10^{-10}$$

**Step 3: Set up equilibrium calculation.**

| | $\ce{CH3COO-}$ | $\ce{CH3COOH}$ | $\ce{OH-}$ |
|---|---|---|---|
| Initial | 0.10 | 0 | 0 |
| Change | $-x$ | $+x$ | $+x$ |
| Equilibrium | $0.10 - x$ | $x$ | $x$ |

$$K_b = \frac{x^2}{0.10 - x} = 5.56 \times 10^{-10}$$

Since $K_b$ is extremely small, $x \ll 0.10$:

$$x^2 = (5.56 \times 10^{-10})(0.10) = 5.56 \times 10^{-11}$$
$$x = [\ce{OH-}] = \sqrt{5.56 \times 10^{-11}} = 7.46 \times 10^{-6}$$

**Step 4: Calculate pH.**
$$\text{pOH} = -\log_{10}(7.46 \times 10^{-6}) = 5.13$$
$$\text{pH} = 14.00 - 5.13 = 8.87$$

The solution is basic, consistent with the hydrolysis of the conjugate base of a weak acid.

---

## Problem 23

**Step 1: Hydrolysis equation.**

The ammonium ion, the conjugate acid of a weak base, reacts with water:

$$\ce{NH4+(aq) + H2O(l) <=> NH3(aq) + H3O+(aq)}$$

**Step 2: Calculate $K_a$ for $\ce{NH4+}$.**
$$K_a(\ce{NH4+}) = \frac{K_w}{K_b(\ce{NH3})} = \frac{1.0 \times 10^{-14}}{1.8 \times 10^{-5}} = 5.56 \times 10^{-10}$$

**Step 3: Set up equilibrium calculation.**

| | $\ce{NH4+}$ | $\ce{NH3}$ | $\ce{H3O+}$ |
|---|---|---|---|
| Initial | 0.20 | 0 | 0 |
| Change | $-x$ | $+x$ | $+x$ |
| Equilibrium | $0.20 - x$ | $x$ | $x$ |

$$K_a = \frac{x^2}{0.20 - x} = 5.56 \times 10^{-10}$$

Since $K_a$ is very small, $x \ll 0.20$:

$$x^2 = (5.56 \times 10^{-10})(0.20) = 1.11 \times 10^{-10}$$
$$x = [\ce{H3O+}] = \sqrt{1.11 \times 10^{-10}} = 1.05 \times 10^{-5}$$

$$\text{pH} = -\log_{10}(1.05 \times 10^{-5}) = 4.98$$

**Pitfall**: Don't confuse $K_a$ of the conjugate acid with $K_a$ of the parent acid. Here, $\ce{NH4+}$ is the *conjugate acid* of $\ce{NH3}$, so you must use $K_a = K_w/K_b$.

---

## Problem 24

**(a) $\ce{KNO3}$ — Neutral**

Potassium nitrate dissociates completely: $\ce{KNO3 -> K+ + NO3-}$.
- $\ce{K+}$ is the cation of a strong base ($\ce{KOH}$) — it does not hydrolyse.
- $\ce{NO3-}$ is the anion of a strong acid ($\ce{HNO3}$) — it does not hydrolyse.

Neither ion reacts with water, so the solution remains neutral (pH ≈ 7).

**(b) $\ce{Na2CO3}$ — Basic**

Sodium carbonate dissociates: $\ce{Na2CO3 -> 2Na+ + CO3^{2-}}$.
- $\ce{Na+}$ (from strong base $\ce{NaOH}$) does not hydrolyse.
- $\ce{CO3^{2-}}$ is the conjugate base of the weak acid $\ce{HCO3-}$ and hydrolyses:

$$\ce{CO3^{2-}(aq) + H2O(l) <=> HCO3-(aq) + OH-(aq)}$$

The production of $\ce{OH-}$ makes the solution basic.

**(c) $\ce{FeCl3}$ — Acidic**

Iron(III) chloride dissociates: $\ce{FeCl3 -> Fe^{3+} + 3Cl-}$.
- $\ce{Cl-}$ (from strong acid $\ce{HCl}$) does not hydrolyse.
- $\ce{Fe^{3+}}$ is a small, highly charged cation. It polarises coordinated water molecules, and the hydrated ion acts as an acid:

$$\ce{[Fe(H2O)6]^{3+}(aq) + H2O(l) <=> [Fe(H2O)5(OH)]^{2+}(aq) + H3O+(aq)}$$

The production of $\ce{H3O+}$ makes the solution acidic.

**General rule**: Salts of strong acid + strong base → neutral; salts of weak acid + strong base → basic; salts of strong acid + weak base → acidic.

---

## Problem 25

**The student is largely correct, but with a caveat.** The $\ce{HSO4-}$ ion can act as a Brønsted–Lowry acid:

$$\ce{HSO4-(aq) + H2O(l) <=> SO4^{2-}(aq) + H3O+(aq)} \quad K_{a2} = 1.2 \times 10^{-2}$$

Since $K_{a2}$ is relatively large (for a weak acid), the pH of a $0.10\ \text{mol}\ \text{dm}^{-3}$ solution is dominated by this dissociation. However, $\ce{HSO4-}$ is **amphiprotic**, meaning it can also act as a Brønsted–Lowry base:

$$\ce{HSO4-(aq) + H2O(l) <=> H2SO4(aq) + OH-(aq)}$$

This reaction has $K_b = K_w / K_{a1}$, where $K_{a1}$ for $\ce{H2SO4}$ is very large (strong acid). So $K_b$ is extremely small and this reaction is negligible. The hydrolysis to produce $\ce{OH-}$ is therefore insignificant compared to the acidic dissociation.

For a $0.10\ \text{mol}\ \text{dm}^{-3}$ solution, using $K_{a2}$:

$$K_{a2} = \frac{[\ce{H+}][\ce{SO4^{2-}}]}{[\ce{HSO4-}]} = \frac{x^2}{0.10 - x} = 1.2 \times 10^{-2}$$

$x$ is likely significant; solving properly gives pH ≈ 1.5–1.6.

**Conclusion**: The student is correct that $K_{a2}$ determines the pH; the basic hydrolysis of $\ce{HSO4-}$ is negligible.

---

## Problem 26

**(a) Calculate pH of each buffer.**

$\text{p}K_a = 4.80$. All solutions have the same total volume, so use mole ratios:

- **Buffer X**: $[\ce{HA}] = [\ce{NaA}]$, so $\text{pH} = \text{p}K_a = 4.80$.

- **Buffer Y**: $\text{pH} = 4.80 + \log_{10}\frac{0.020}{0.080} = 4.80 + \log_{10}(0.25) = 4.80 - 0.602 = 4.20$.

- **Buffer Z**: $\text{pH} = 4.80 + \log_{10}\frac{0.080}{0.020} = 4.80 + \log_{10}(4.0) = 4.80 + 0.602 = 5.40$.

**(b) Buffer capacity analysis.**

- **Greatest capacity when acid is added**: Buffer Z has the greatest capacity to resist added acid because it has the highest concentration of the basic component ($\ce{A-}$, 0.080 mol) to neutralise incoming $\ce{H+}$ ions.

- **Greatest capacity when base is added**: Buffer Y has the greatest capacity to resist added base because it has the highest concentration of the acidic component ($\ce{HA}$, 0.080 mol) to neutralise incoming $\ce{OH-}$ ions.

**General principle**: Buffer capacity is maximised when both components are present in high concentrations. Buffer X has both components at 0.050 mol, giving it the most balanced and overall highest total buffer capacity. However, the question asks specifically about adding acid vs. adding base. For adding acid, the $[\ce{A-}]$ matters most; for adding base, $[\ce{HA}]$ matters most.

---

## Problem 27

**Equilibrium equations:**

*As an acid* (donating a proton from the $\ce{-NH3+}$ group):

$$\ce{^{+}H3NCH2COOH(aq) + H2O(l) <=> H2NCH2COOH(aq) + H3O+(aq)} \quad K_{a1}$$

*As a base* (the amino group accepting a proton):

$$\ce{H2NCH2COOH(aq) + H2O(l) <=> ^{-}OOCCH2NH3+(aq) + OH-(aq)}$$

Or equivalently, the carboxyl group donating a proton to water (this is the relevant $K_{a2}$):

$$\ce{H2NCH2COOH(aq) + H2O(l) <=> H2NCH2COO-(aq) + H3O+(aq)} \quad K_{a2}$$

(In practice, glycine exists predominantly as the zwitterion $\ce{^{+}H3NCH2COO-}$ in aqueous solution near neutral pH. The $K_{a1}$ and $K_{a2}$ values given refer to the zwitterion as the reference species.)

**Isoelectric point calculation:**

The isoelectric point (pI) is the pH at which the net charge on the amino acid is zero (the zwitterion predominates). For an amino acid with two $\text{p}K_a$ values:

$$\text{pI} = \frac{\text{p}K_{a1} + \text{p}K_{a2}}{2} = \frac{2.34 + 9.60}{2} = \frac{11.94}{2} = 5.97$$

At pH 5.97, glycine exists predominantly as the neutral zwitterion $\ce{^{+}H3NCH2COO-}$, with equal (and negligible) concentrations of the cationic and anionic forms.

---

## Problem 28

**Step 1: Calculate $[\ce{H+}]$.**
$$[\ce{H+}] = 10^{-\text{pH}} = 10^{-3.40} = 3.98 \times 10^{-4}\ \text{mol}\ \text{dm}^{-3}$$

**Step 2: Calculate percentage ionisation.**

The weak acid dissociates: $\ce{HA <=> H+ + A-}$. The concentration of $\ce{H+}$ equals the concentration of dissociated acid.

$$\text{Percentage ionisation} = \frac{[\ce{H+}]}{[\ce{HA}]_{\text{initial}}} \times 100\% = \frac{3.98 \times 10^{-4}}{0.010} \times 100\% = 3.98\%$$

**Step 3: Explain why percentage ionisation increases on dilution.**

Consider the equilibrium: $\ce{HA(aq) + H2O(l) <=> H3O+(aq) + A-(aq)}$.

On dilution (adding water), the concentrations of all aqueous species decrease. According to **Le Chatelier's principle**, the system shifts to oppose this change. The forward reaction produces two particles ($\ce{H3O+}$ and $\ce{A-}$) from one ($\ce{HA}$), so the forward direction increases the total number of particles. The equilibrium therefore shifts to the **right**, increasing the degree of dissociation.

Mathematically: $K_a = \frac{[\ce{H+}][\ce{A-}]}{[\ce{HA}]}$. If the initial concentration $c$ decreases, the fraction dissociated $\alpha = \sqrt{K_a/c}$ increases (for a weak acid where $\alpha \ll 1$). This shows that dilution increases $\alpha$, the degree of ionisation.

---

## Problem 29

**Step 1: Use Henderson–Hasselbalch equation.**

$$\text{pH} = \text{p}K_a + \log_{10}\frac{[\ce{CH3COO-}]}{[\ce{CH3COOH}]}$$

$$\text{p}K_a = -\log_{10}(1.8 \times 10^{-5}) = 4.74$$

$$5.00 = 4.74 + \log_{10}\frac{[\ce{CH3COO-}]}{[\ce{CH3COOH}]}$$

$$\log_{10}\frac{[\ce{CH3COO-}]}{[\ce{CH3COOH}]} = 0.26$$

$$\frac{[\ce{CH3COO-}]}{[\ce{CH3COOH}]} = 10^{0.26} = 1.82$$

**Step 2: Determine volume ratio.**

Both stock solutions are $0.10\ \text{mol}\ \text{dm}^{-3}$. Let $V_a$ = volume of acid, $V_b$ = volume of conjugate base. After mixing, the mole ratio equals the volume ratio (since concentrations are equal):

$$\frac{V_b}{V_a} = 1.82$$

**Step 3: Calculate specific volumes for 100 cm³.**

$$V_a + V_b = 100\ \text{cm}^3$$
$$V_b = 1.82\,V_a$$
$$V_a + 1.82\,V_a = 100 \implies 2.82\,V_a = 100 \implies V_a = 35.5\ \text{cm}^3$$
$$V_b = 100 - 35.5 = 64.5\ \text{cm}^3$$

So approximately 35.5 cm³ of ethanoic acid solution and 64.5 cm³ of sodium ethanoate solution.

**Pitfall**: The Henderson–Hasselbalch uses the ratio of *equilibrium* concentrations. Since both stock solutions have the same concentration, the volume ratio gives the mole ratio, and dilution to the same final volume means the concentration ratio equals the mole ratio.

---

## Problem 30

**Equivalence point vs. endpoint**:
- The **equivalence point** is the point in a titration at which the amount of titrant added is *stoichiometrically equivalent* to the amount of analyte present — i.e., the reaction is exactly complete. It is a theoretical point determined by the stoichiometry of the reaction.
- The **endpoint** is the point at which the indicator changes colour, signalling to the experimenter that the titration is complete. It is an *experimental observation*.

Ideally, the endpoint and the equivalence point should coincide. In practice, there is usually a small difference, which contributes to the **indicator error**.

**Importance of indicator selection**: The indicator should be chosen so that its $\text{p}K_a$ is as close as possible to the pH at the equivalence point. This ensures that the colour change occurs within the steep portion of the titration curve, where a very small addition of titrant causes a large pH change. The endpoint will then be very close to the true equivalence point.

**Why bromothymol blue is a poor choice for $\ce{CH3COOH}$ vs $\ce{NaOH}$**: The equivalence point of this weak-acid–strong-base titration is at approximately pH 8.7. Bromothymol blue changes colour over the range pH 6.0–7.6, with its $\text{p}K_a$ around 7.0. This means the indicator will change colour **before** the equivalence point is reached — while there is still unreacted ethanoic acid in the flask. The endpoint will occur too early, resulting in a **systematic negative error**: the titre volume will be too low, and the calculated concentration of the acid will be underestimated.
