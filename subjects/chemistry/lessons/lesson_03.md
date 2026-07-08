# Lesson 3: Electron Configuration — Orbitals, Aufbau, Hund, Pauli

## What You'll Learn
- Describe the hierarchy of energy levels, sub-levels, and orbitals, and state how many orbitals and electrons each sub-level can hold
- Apply the Aufbau principle to write the full electron configuration for any element with atomic number 1 to 36
- Use condensed notation with noble gas cores to write electron configurations quickly and correctly
- Apply Hund's rule and the Pauli exclusion principle to draw orbital diagrams using box-arrow notation
- Explain the chromium and copper exceptions to the expected electron filling order, with reference to the extra stability of half-filled and fully-filled d sub-levels
- Write correct electron configurations for transition metal ions by removing electrons from 4s before 3d

---

## 1. Energy Levels, Sub-Levels, and Orbitals — The Address of an Electron

### What the hierarchy of energy levels, sub-levels, and orbitals is and why it is needed

Every electron in an atom occupies a specific region of space and has a specific energy. To describe where an electron is and how much energy it has, we use a system with three levels of organisation: the **energy level** (also called a shell), the **sub-level** (also called a subshell), and the **orbital**.

Think of this as an address system. The energy level is like the country — it tells you broadly how far the electron is from the nucleus. The sub-level is like the city — it gives a more specific type of region. The orbital is like the street address — it specifies exactly which region of space the electron occupies.

### Energy levels — the shells

Energy levels are numbered with the symbol n, where n can be 1, 2, 3, 4, and so on. The number n is called the **principal quantum number**. The larger the value of n, the further the electron is from the nucleus on average, and the higher its energy. Energy level 1 (n = 1) is the closest to the nucleus and has the lowest energy. Energy level 2 (n = 2) is further out and has higher energy.

### Sub-levels — the types of regions within each shell

Within each energy level, there are one or more **sub-levels**. Sub-levels are labelled with letters: s, p, d, and f. Not every sub-level exists in every shell. The available sub-levels depend on the value of n:

- Shell n = 1 contains only the 1s sub-level.
- Shell n = 2 contains the 2s and 2p sub-levels.
- Shell n = 3 contains the 3s, 3p, and 3d sub-levels.
- Shell n = 4 contains the 4s, 4p, 4d, and 4f sub-levels.

### Orbitals — the specific regions where electrons live

Within each sub-level, there are one or more **orbitals**. An orbital is a three-dimensional region of space around the nucleus where there is a high probability (about 90%) of finding an electron. Each orbital can hold a maximum of two electrons.

The different sub-levels contain different numbers of orbitals:

| Sub-level | Number of Orbitals | Maximum Number of Electrons |
|-----------|-------------------|---------------------------|
| s | 1 | 2 |
| p | 3 | 6 |
| d | 5 | 10 |
| f | 7 | 14 |

This means the maximum number of electrons each shell can hold is:
- Shell n = 1: one s sub-level → 2 electrons maximum
- Shell n = 2: one s and one p sub-level → 2 + 6 = 8 electrons maximum
- Shell n = 3: one s, one p, and one d sub-level → 2 + 6 + 10 = 18 electrons maximum

This explains why the "2, 8, 8" pattern works for elements 1 through 20 (up to calcium), but then breaks down. After calcium, the 3d sub-level starts to fill, and simple shell-counting no longer works.

### The shapes of orbitals — a brief picture

An s orbital is spherical — it is the same shape in all directions around the nucleus. A p orbital has a dumbbell or figure-eight shape, with two lobes on opposite sides of the nucleus. Because there are three p orbitals in a p sub-level, they are arranged along three perpendicular axes and are labelled pₓ, p_y, and p_z. The d orbitals have more complex shapes; there are five of them in a d sub-level. For the IB examination, you do not need to draw orbital shapes, but you should know that s orbitals are spherical, p orbitals are dumbbell-shaped, and each sub-level has the number of orbitals listed in the table above.

A common misconception is that an orbital is like a planet's orbit — a fixed circular path. This is incorrect. An orbital is not a path. It is a probability cloud: a region of space where the electron is likely to be found. The electron does not travel around the nucleus in a circle like a planet around the sun. Instead, it exists as a spread-out cloud of probability.

### Worked Example 1: Counting Orbitals and Electron Capacity

**Problem:** How many orbitals are in the n = 3 shell, and what is the maximum number of electrons this shell can hold?

**Approach:** List the sub-levels in n = 3, count the orbitals in each, and multiply by 2 (since each orbital holds two electrons).

**Solution:** The n = 3 shell contains three sub-levels: 3s (1 orbital), 3p (3 orbitals), and 3d (5 orbitals). Total number of orbitals = 1 + 3 + 5 = 9. Maximum number of electrons = 9 × 2 = 18.

**Why this makes sense:** We can verify this with the formula 2n² for the maximum electron capacity of a shell. For n = 3, 2 × 3² = 2 × 9 = 18. The formula works because each shell has n² orbitals: 3² = 9, and each orbital holds 2 electrons: 9 × 2 = 18.

---

## 2. The Order of Filling Orbitals — The Aufbau Principle

### What the Aufbau principle is and why the filling order is not what you might expect

The word "Aufbau" is German for "building up." The **Aufbau principle** states that electrons occupy the lowest energy orbitals first, before filling higher energy orbitals. An atom in its ground state (its lowest possible energy state) has all its electrons arranged according to this principle.

You might expect the filling order to follow the shell number: 1s, then 2s, 2p, then 3s, 3p, 3d, then 4s, 4p, and so on. But this is not what happens. The actual order up to element 36 (krypton) is:

\[
\text{1s → 2s → 2p → 3s → 3p → 4s → 3d → 4p}
\]

Notice that **4s fills before 3d**. This happens because the 4s orbital, although it belongs to shell n = 4, penetrates closer to the nucleus on average than the 3d orbitals do. This penetration gives 4s a slightly lower energy than 3d for the elements in this region of the periodic table. This is a subtle quantum mechanical effect, but for IB, the key thing to remember is simply that 4s fills before 3d.

### The diagonal rule — a mnemonic for the filling order

A helpful way to remember the filling order is to write the sub-levels in a triangular arrangement and then read the diagonals from top-right to bottom-left:

```
1s
2s 2p
3s 3p 3d
4s 4p 4d 4f
5s 5p 5d 5f
```

Reading along the diagonals (top-right to bottom-left) gives: 1s, 2s, 2p, 3s, 3p, 4s, 3d, 4p, 5s, 4d, 5p, and so on. This sequence matches the actual filling order for neutral atoms in their ground state.

### Writing electron configurations — the notation

An electron configuration is written by listing each occupied sub-level followed by a superscript that tells you how many electrons are in that sub-level. For example, 1s² means the 1s sub-level contains 2 electrons. The sum of all superscripts must equal the total number of electrons in the atom, which equals the atomic number Z for a neutral atom.

By convention, we write sub-levels in order of increasing n, even though the filling order may put 4s before 3d. So the configuration of iron (Z = 26) is written as 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d⁶ — with 4s listed before 3d — even though 4s fills after 3p but before 3d.

### Worked Example 2: Writing a Full Electron Configuration

**Problem:** Write the full electron configuration of an iron atom, which has atomic number Z = 26.

**Approach:** Iron has 26 electrons. We fill orbitals in the Aufbau order, keeping a running total of electrons as we go, until we reach 26.

**Solution:**
- 1s² → 2 electrons placed (running total: 2)
- 2s² → 2 more (total: 4)
- 2p⁶ → 6 more (total: 10)
- 3s² → 2 more (total: 12)
- 3p⁶ → 6 more (total: 18)
- 4s² → 2 more (total: 20)
- 3d → we need 6 more to reach 26, so 3d⁶ (total: 26)

The full configuration is: **1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d⁶**

**Why this makes sense:** Iron is in Period 4, Group 8. The 4s² 3d⁶ configuration places it in the d-block, which is consistent with its position as a transition metal. The total number of electrons (2 + 2 + 6 + 2 + 6 + 2 + 6 = 26) matches Z.

---

## 3. Orbital Diagrams, Hund's Rule, and the Pauli Exclusion Principle

### What orbital diagrams show and why we draw them

An **orbital diagram** (also called a box-arrow diagram) shows not just which sub-levels are occupied, but also how the electrons are distributed among the individual orbitals within each sub-level and the direction of each electron's spin. Orbital diagrams help us visualise two important rules: the Pauli exclusion principle and Hund's rule.

In an orbital diagram, each orbital is represented by a box (or a line), and each electron is represented by an arrow (↑ or ↓). The direction of the arrow indicates the electron's spin — a quantum mechanical property that can take one of two values, which we call "spin up" (↑) and "spin down" (↓).

### The Pauli exclusion principle

The Pauli exclusion principle states that no two electrons in the same atom can have exactly the same set of four quantum numbers. In the context of an orbital diagram, this means that a single orbital can hold at most two electrons, and those two electrons must have opposite spins. In a diagram, this appears as ↑↓ in one box. You can never have ↑↑ or ↓↓ in the same box.

### Hund's rule

Hund's rule describes how electrons fill a sub-level that has multiple orbitals (such as p with three orbitals or d with five orbitals). The rule states that electrons will occupy separate orbitals within the sub-level before any orbital receives a second electron. Furthermore, all the unpaired electrons in a sub-level will have the same spin (all ↑ or all ↓).

A useful analogy: imagine passengers boarding an empty bus. Each passenger prefers to take an empty row rather than sit next to a stranger. Only after every row has at least one passenger will people start doubling up. Similarly, electrons prefer to occupy empty orbitals before pairing up, because electrons repel each other and pairing costs energy.

### Worked Example 3: Orbital Diagram for Nitrogen

**Problem:** Draw the orbital diagram for nitrogen (Z = 7), showing all occupied orbitals.

**Approach:** First write the electron configuration, then draw the boxes for each sub-level and place arrows according to Hund's rule and the Pauli principle.

**Solution:** Nitrogen has 7 electrons. Configuration: 1s² 2s² 2p³.

```
1s: [↑↓]
2s: [↑↓]
2p: [↑ ][↑ ][↑ ]
```

The three 2p electrons each occupy a different p orbital, and all three have the same spin (all ↑). This satisfies Hund's rule: the electrons spread out across the three available p orbitals before any pairing occurs.

**Why this makes sense:** The half-filled 2p sub-level (2p³) is especially stable because each electron occupies its own orbital with parallel spin, maximising what is called exchange energy. This stability explains why nitrogen has a slightly higher first ionisation energy than oxygen, which we explore in Lessons 5 and 6.

### Worked Example 4: Orbital Diagram for Oxygen

**Problem:** Draw the orbital diagram for oxygen (Z = 8), showing all occupied orbitals.

**Approach:** Oxygen has one more electron than nitrogen. Write the configuration, then fill the orbitals.

**Solution:** Oxygen has 8 electrons. Configuration: 1s² 2s² 2p⁴.

```
1s: [↑↓]
2s: [↑↓]
2p: [↑↓][↑ ][↑ ]
```

The fourth electron in the 2p sub-level must pair up in one of the already half-filled orbitals, because all three p orbitals already have one electron each. The paired electrons must have opposite spins (↑↓) according to the Pauli exclusion principle.

**Why this makes sense:** Now one of the p orbitals has a pair of electrons. These two electrons repel each other because they occupy the same region of space. This electron-electron repulsion makes one of them slightly easier to remove, which is why oxygen has a slightly lower first ionisation energy than nitrogen.

---

## 4. Condensed Electron Configurations and Transition Metal Ions

### What condensed configurations are and why we use them

Writing out the full configuration for every element, especially heavier ones, becomes very repetitive. A more compact method uses a **condensed electron configuration**. In condensed notation, you write the symbol of the preceding noble gas (the noble gas from the previous period) in square brackets to represent all the electrons in its configuration, and then add only the electrons beyond that noble gas core.

For example, neon (Ne) has the configuration 1s² 2s² 2p⁶. For sodium (Na, Z = 11), instead of writing 1s² 2s² 2p⁶ 3s¹, we write [Ne] 3s¹. The [Ne] stands for all 10 electrons of neon's configuration. Here are a few more examples:

- Chlorine (Cl, Z = 17): [Ne] 3s² 3p⁵
- Calcium (Ca, Z = 20): [Ar] 4s²
- Manganese (Mn, Z = 25): [Ar] 4s² 3d⁵
- Zinc (Zn, Z = 30): [Ar] 4s² 3d¹⁰

### Writing configurations for transition metal ions

When a transition metal atom forms a positive ion (a cation), electrons are removed. The crucial rule is: **electrons are removed from the 4s orbital before they are removed from the 3d orbital.** This is because, once the 3d orbitals are occupied, the 4s orbital becomes higher in energy than the 3d orbitals. Even though 4s fills before 3d, it also empties before 3d.

Consider iron (Fe, Z = 26):
- Neutral Fe atom: [Ar] 4s² 3d⁶
- Fe²⁺ ion: [Ar] 3d⁶ (both 4s electrons have been removed)
- Fe³⁺ ion: [Ar] 3d⁵ (both 4s electrons and one 3d electron have been removed)

A common mistake is to write Fe²⁺ as [Ar] 4s² 3d⁴ — removing electrons from 3d first. This is incorrect. Always remove from 4s first.

### Worked Example 5: Configuration of a Transition Metal Ion

**Problem:** Write the full electron configuration and the condensed electron configuration of the copper(II) ion, Cu²⁺. Copper has atomic number Z = 29.

**Approach:** First, determine the configuration of the neutral copper atom (remembering the copper exception — see Section 5). Then remove two electrons, starting with the 4s electron.

**Solution:**
- Neutral Cu atom (Z = 29): The expected configuration would be [Ar] 4s² 3d⁹, but due to the extra stability of a fully filled d sub-level, the actual configuration is [Ar] 4s¹ 3d¹⁰.
- Cu²⁺ ion: remove two electrons. First, remove the single 4s electron. Then remove one electron from the 3d sub-level. This gives [Ar] 3d⁹.
- Full configuration of Cu²⁺: 1s² 2s² 2p⁶ 3s² 3p⁶ 3d⁹.

**Why this makes sense:** Copper starts with one electron in 4s and ten in 3d. The ion loses the outermost (4s) electron first, then one from the 3d. The resulting Cu²⁺ ion has a 3d⁹ configuration, which has one unpaired electron. This unpaired electron is responsible for the blue colour of many copper(II) compounds — a topic explored in detail when studying transition metal complexes.

---

## 5. The Exceptions — Chromium and Copper

### What the exceptions are and why they happen

For almost every element from hydrogen to krypton, the Aufbau principle predicts the correct electron configuration. But there are two important exceptions: chromium (Cr, Z = 24) and copper (Cu, Z = 29). These exceptions occur because a half-filled d sub-level (d⁵) and a fully-filled d sub-level (d¹⁰) confer extra stability to the atom. When promoting one electron from the 4s orbital to the 3d set can achieve one of these stable arrangements, the atom adopts the anomalous configuration.

### The chromium exception

The expected configuration for chromium, following the Aufbau order, would be:
- Expected: [Ar] 4s² 3d⁴

But the actual configuration is:
- Actual: [Ar] 4s¹ 3d⁵

One electron has moved from the 4s orbital into the 3d set. This creates a half-filled 3d sub-level (3d⁵), in which each of the five d orbitals contains exactly one electron with parallel spin. This arrangement has maximum exchange energy — a quantum mechanical stabilisation that makes the half-filled sub-level particularly stable. The energy gained by achieving this half-filled state more than compensates for the energy cost of promoting one electron from 4s to 3d.

### The copper exception

The expected configuration for copper would be:
- Expected: [Ar] 4s² 3d⁹

But the actual configuration is:
- Actual: [Ar] 4s¹ 3d¹⁰

Again, one electron moves from 4s to 3d. This creates a completely filled 3d sub-level (3d¹⁰), which is also especially stable. A fully-filled sub-level has no unpaired electrons and a symmetrical electron distribution, both of which contribute to its stability.

### A pattern to remember

Both exceptions follow the same pattern: if moving one electron from 4s to 3d can achieve either a half-filled d sub-level (d⁵) or a fully-filled d sub-level (d¹⁰), the atom will do so. Cr goes from d⁴ to d⁵ (half-filled). Cu goes from d⁹ to d¹⁰ (fully-filled). These are the only two exceptions you need to know for elements 1 through 36.

---

## Practice Problems

**Problem 1:** Write the full electron configuration (1s² 2s² …) of a neutral sulfur atom, which has atomic number Z = 16.

**Problem 2:** (a) Write the condensed electron configuration (using a noble gas core) of a neutral nickel atom (Z = 28). (b) Write the condensed electron configuration of the nickel(II) ion, Ni²⁺.

**Problem 3:** Draw the full orbital diagram (box-arrow notation) for a neutral phosphorus atom (Z = 15). Label each box with the orbital it represents, and ensure that your diagram clearly shows Hund's rule in action.

**Problem 4:** For each of the following electron configurations, state whether it is correct for a neutral atom in its ground state. If the configuration is incorrect, write the correct configuration and explain what is wrong. (a) [Ar] 4s² 3d⁴ (b) 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 4p¹ (c) [Ar] 4s² 3d¹⁰

**Problem 5 (IB-Style):** The element cobalt has atomic number Z = 27 and forms the complex ion \(\ce{[Co(H2O)6]^{2+}}\) in aqueous solution. (a) Write the condensed electron configuration of a neutral cobalt atom, a Co²⁺ ion, and a Co³⁺ ion. (b) For each of the three species in part (a), state the number of unpaired electrons present. You may find it helpful to draw the orbital diagram of the 3d sub-level. (c) The element chromium (Z = 24) has the electron configuration [Ar] 4s¹ 3d⁵ rather than the expected [Ar] 4s² 3d⁴. Explain why the actual configuration is preferred, making reference to the concept of stability.

---

## Answers

**Answer 1:** Sulfur has Z = 16, so it has 16 electrons. Filling in Aufbau order: 1s² (2 e⁻), 2s² (4), 2p⁶ (10), 3s² (12), 3p⁴ (16). The full configuration is 1s² 2s² 2p⁶ 3s² 3p⁴.

---

**Answer 2:** (a) Nickel (Z = 28): The preceding noble gas is argon (Ar, Z = 18), which accounts for the first 18 electrons. The remaining 10 electrons fill 4s² then 3d⁸. The condensed configuration is [Ar] 4s² 3d⁸.

(b) For Ni²⁺, we remove two electrons. Electrons are removed from 4s before 3d, so we remove both 4s electrons. The condensed configuration of Ni²⁺ is [Ar] 3d⁸.

---

**Answer 3:** Phosphorus (Z = 15): 1s² 2s² 2p⁶ 3s² 3p³.

```
1s: [↑↓]
2s: [↑↓]
2p: [↑↓][↑↓][↑↓]
3s: [↑↓]
3p: [↑ ][↑ ][↑ ]
```

Hund's rule is demonstrated in the 3p sub-level: the three electrons occupy the three separate p orbitals rather than pairing up in one or two orbitals, and all three have parallel spins (all ↑).

---

**Answer 4:** (a) Incorrect. This configuration, [Ar] 4s² 3d⁴, is what one might naively expect for chromium. But the actual ground-state configuration of chromium is [Ar] 4s¹ 3d⁵, because the half-filled 3d sub-level (d⁵) provides extra stability.

(b) Incorrect. After filling 4s², the next lowest energy sub-level is 3d, not 4p. This configuration would represent an atom with Z = 19 + 2 + 1 = 22 (if 3d had zero electrons), but the actual element at Z = 22 is titanium, which has the configuration [Ar] 4s² 3d². The error is that 4p was filled before 3d, which violates the Aufbau principle.

(c) Correct. This is the configuration of neutral zinc (Z = 30). After the 4s sub-level is filled (4s²), the 3d sub-level fills completely (3d¹⁰). This follows the normal Aufbau order and is not an exception.

---

**Answer 5:** (a) Cobalt (Z = 27): The preceding noble gas is argon (Z = 18). The remaining 9 electrons fill 4s² then 3d⁷. Neutral Co: [Ar] 4s² 3d⁷.

Co²⁺: Remove two electrons from 4s first. This gives [Ar] 3d⁷.

Co³⁺: Remove two electrons from 4s and then one from 3d. This gives [Ar] 3d⁶.

(b) For counting unpaired electrons, we draw the 3d sub-level:

Neutral Co (d⁷): [↑↓][↑ ][↑ ][↑ ][↑ ] → 3 unpaired electrons. (The 4s² electrons are paired.)

Co²⁺ (d⁷): Same 3d arrangement as neutral Co → 3 unpaired electrons.

Co³⁺ (d⁶): [↑↓][↑ ][↑ ][↑ ][↑ ] → With six d electrons, Hund's rule gives us five unpaired electrons in separate orbitals, then the sixth pairs up in the first orbital. That leaves 4 unpaired electrons.

(c) The expected configuration for chromium would be [Ar] 4s² 3d⁴, but the actual configuration is [Ar] 4s¹ 3d⁵. In the actual configuration, the 3d sub-level is half-filled (d⁵), with one electron in each of the five d orbitals and all spins parallel. This half-filled arrangement has extra stability due to maximum exchange energy — a quantum mechanical effect that lowers the energy of the atom when electrons with parallel spin occupy different orbitals in the same sub-level. The energy gained by achieving this half-filled d sub-level is greater than the energy cost of promoting one electron from the 4s orbital to the 3d set, so the anomalous configuration is preferred.
