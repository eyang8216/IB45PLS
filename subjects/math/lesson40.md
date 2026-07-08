# Lesson 40: Counting Principles — Permutations and Combinations

## What Are Counting Principles?

**Counting principles** are systematic methods for answering questions like "how many ways can this be done?" without having to list every possibility. They are the foundation of probability (Lessons 33–37) and are directly connected to the binomial coefficients you saw in Lesson 39.

## Why Learn This?

Imagine you need to find the probability of being dealt exactly two aces in a five-card poker hand. To compute that probability, you first need to count: how many total five-card hands exist, and how many of those contain exactly two aces. Counting principles give you the tools to answer these kinds of questions efficiently. They also explain where those $\binom{n}{r}$ numbers in the binomial theorem come from.

---

## Part 1: The Multiplication Principle (The "AND" Rule)

If one choice can be made in *m* different ways, and a second, independent choice can be made in *n* different ways, then the two choices together can be made in **m × n** ways.

**Worked Example:** You own 3 shirts and 4 pairs of pants. How many different outfits (one shirt and one pair of pants) can you wear?

For each shirt, you have 4 choices of pants. With 3 shirts, that is 3 × 4 = **12 outfits**.

**Key idea:** When you see "AND" connecting choices (pick a shirt AND pick pants), you multiply the numbers.

---

## Part 2: Permutations (Order Matters)

A **permutation** is an arrangement of items where the **order matters**. For example, the arrangement ABC is different from the arrangement CBA — even though they contain the same letters, the order is different.

### 2.1 Arranging All n Objects

The number of ways to arrange n **distinct** (different from each other) objects in a line is **n!** (n factorial).

**Why?** You have n choices for the first position, then (n − 1) for the second, (n − 2) for the third, and so on. By the multiplication principle, the total is n × (n − 1) × (n − 2) × ... × 1 = n!.

**Worked Example:** How many ways can 5 people line up for a photograph?

5! = 5 × 4 × 3 × 2 × 1 = **120** ways.

### 2.2 Arranging r Objects Chosen from n

Sometimes you want to arrange only some of the available objects. The number of ways to choose and arrange r objects from a set of n distinct objects is written as P(n, r) or $_nP_r$:

$$P(n, r) = \frac{n!}{(n-r)!}$$

**Why this formula?** You have n choices for the first position, (n − 1) for the second, ..., down to (n − r + 1) for the r-th position. That product is exactly n! divided by (n − r)!.

**Worked Example:** How many three-letter "words" (arrangements of three letters, not necessarily real English words) can be formed from the letters A, B, C, D, E, using each letter at most once?

We have n = 5 letters and we are choosing and arranging r = 3 of them.
P(5, 3) = 5! / (5 − 3)! = 5! / 2! = (5 × 4 × 3 × 2 × 1) / (2 × 1) = 5 × 4 × 3 = **60** arrangements.

### 2.3 Permutations with Repeated Items

What if some of the objects are identical? For example, the letters in the word "MISSISSIPPI" have repeated letters. If you treat all letters as distinct, you overcount — swapping two identical I's does not produce a new arrangement.

If there are n objects in total, with one type repeated a times, another repeated b times, another repeated c times, and so on, the number of distinct arrangements is:

$$\frac{n!}{a! \cdot b! \cdot c! \cdots}$$

**Worked Example:** How many distinct arrangements of the letters in "MISSISSIPPI" are there?

Count the letters: M appears 1 time, I appears 4 times, S appears 4 times, P appears 2 times. Total letters: 11.

Number of arrangements = $\frac{11!}{1! \cdot 4! \cdot 4! \cdot 2!}$.

Compute: 11! = 39,916,800. 4! = 24. 2! = 2.

Denominator = 1 × 24 × 24 × 2 = 1,152.

39,916,800 / 1,152 = **34,650** distinct arrangements.

---

## Part 3: Combinations (Order Does NOT Matter)

A **combination** is a selection of items where the **order does not matter**. Choosing Alice, Bob, and Carol for a committee is the same committee as choosing Carol, Bob, and Alice — the group is what matters, not the order in which they were named.

The number of ways to choose r objects from a set of n distinct objects (order not important) is:

$$\binom{n}{r} = C(n, r) = \frac{n!}{r!(n-r)!}$$

This is the same binomial coefficient from Lesson 39. It is often read as "n choose r."

**Why does dividing by r! work?** When order matters, there are P(n, r) = n!/(n−r)! arrangements. But each group of r items can be arranged in r! different orders. Since we don't care about order, we divide by r! to collapse all those arrangements into one combination.

**Worked Example:** How many ways can a committee of 3 people be chosen from a group of 10?

C(10, 3) = $\frac{10!}{3! \cdot 7!} = \frac{10 \times 9 \times 8}{3 \times 2 \times 1} = \frac{720}{6} = 120$.

---

## Part 4: When to Use Permutations vs. Combinations — A Simple Test

Ask yourself: "If I swap two items in my selection, do I get a different result?"

- If swapping changes the result → **order matters** → use **permutations**.
- If swapping does NOT change the result → **order does NOT matter** → use **combinations**.

**Examples:**
- Choosing a president, vice president, and secretary from a club: swapping the president and vice president changes who has which role → **permutation**.
- Choosing 3 people to be on a party-planning committee (all equal roles): swapping two people gives the same committee → **combination**.
- Arranging books on a shelf: different order = different arrangement → **permutation**.
- Selecting 5 cards from a deck for a poker hand: the order you receive them does not change the hand → **combination**.

---

## Part 5: Multi-Step Counting with Combinations

Many problems require you to break the situation into cases and then add the results.

**Worked Example:** From a group of 8 boys and 5 girls, a committee of 4 is to be chosen. The committee must contain at least 2 girls. How many different committees are possible?

**Approach:** "At least 2 girls" means 2, 3, or 4 girls. We count each case separately and then add.

**Case 1: Exactly 2 girls and 2 boys.**
Choose 2 girls from 5: C(5, 2) = 10.
Choose 2 boys from 8: C(8, 2) = 28.
Total for this case: 10 × 28 = 280.

**Case 2: Exactly 3 girls and 1 boy.**
Choose 3 girls from 5: C(5, 3) = 10.
Choose 1 boy from 8: C(8, 1) = 8.
Total for this case: 10 × 8 = 80.

**Case 3: Exactly 4 girls and 0 boys.**
Choose 4 girls from 5: C(5, 4) = 5.
Choose 0 boys from 8: C(8, 0) = 1.
Total for this case: 5 × 1 = 5.

**Grand total:** 280 + 80 + 5 = **365** possible committees.

---

## Part 6: Useful Properties of Binomial Coefficients

These properties can save time and help check your work:

**Symmetry:** $\binom{n}{r} = \binom{n}{n-r}$. Choosing r items to include is the same as choosing n−r items to exclude.

**Sum of all coefficients:** $\binom{n}{0} + \binom{n}{1} + \cdots + \binom{n}{n} = 2^n$. This is the total number of subsets (of any size) you can form from n items.

**Pascal's Identity:** $\binom{n}{r} + \binom{n}{r+1} = \binom{n+1}{r+1}$. This is how you build Pascal's triangle: each entry is the sum of the two entries above it.

---

## Common Misconceptions

**Misconception 1:** "Permutation and combination are just two names for the same thing." They are different. Permutations count ordered arrangements; combinations count unordered selections. Using the wrong one will give you a completely wrong answer.

**Misconception 2:** "C(n, r) and P(n, r) are always large numbers." They can be, but not always. C(5, 5) = 1 (there is only one way to choose all five items), and P(5, 0) = 1 (there is only one way to arrange zero items).

**Misconception 3:** "When items are repeated, I should still use n! for arrangements." Using n! when items are repeated overcounts. You must divide by the factorial of each repetition count. For example, the word "BOB" has 3 letters but only 3!/(2!) = 3 distinct arrangements (BOB, BBO, OBB), not 6.

**Misconception 4:** "If the problem doesn't say whether order matters, it doesn't matter." Always ask yourself: does rearranging the selected items produce a meaningfully different outcome? If yes, order matters.

---

## Practice Problems

**1.** How many four-digit PIN codes can be formed using the digits 0 through 9, if digits may be repeated?

**2.** A password consists of 3 uppercase letters (A–Z) followed by 2 digits (0–9). Letters and digits may be repeated. How many different passwords are possible?

**3.** You have 7 different books. You want to arrange them on a shelf, but 3 of these books form a trilogy and must stay together (in any order within the trilogy). How many shelf arrangements are possible?

**4.** From a club of 12 students, a president, a vice president, and a secretary are to be elected (no student can hold more than one position). How many different sets of officers are possible? (Hint: does it matter who is president vs. who is vice president?)

**5.** A basketball coach must choose a starting lineup of 5 players from a squad of 15. All 5 positions are considered interchangeable for this problem. How many different starting lineups are possible?

**6. [IB Exam Style — 5 marks]** A standard deck has 52 playing cards, including 4 aces. You are dealt a hand of 5 cards.

(a) How many total 5-card hands are possible? [1 mark]

(b) How many hands contain exactly 2 aces? [3 marks]

(c) What is the probability of being dealt exactly 2 aces? Give your answer as a fraction. [1 mark]

---

## Answers

**1.** For each of the 4 digits, there are 10 choices (0 through 9). Using the multiplication principle: 10 × 10 × 10 × 10 = 10⁴ = **10,000** possible PINs.

**2.** For the 3 letters: 26 choices each, so 26³ = 17,576. For the 2 digits: 10 choices each, so 10² = 100. Combined: 17,576 × 100 = **1,757,600** passwords.

**3.** Treat the trilogy as a single "block." Now you have 5 items to arrange: 4 single books plus 1 trilogy block. These 5 items can be arranged in 5! = 120 ways. Inside the trilogy block, the 3 books can be arranged in 3! = 6 ways. Using the multiplication principle: 120 × 6 = **720** arrangements.

**4.** Order matters (president is different from vice president), so this is a permutation. Choose 3 from 12 and arrange them: P(12, 3) = 12 × 11 × 10 = **1,320** possible sets of officers.

**5.** All 5 positions are equivalent, so order does not matter. This is a combination. C(15, 5) = 15!/(5! × 10!) = (15 × 14 × 13 × 12 × 11)/(5 × 4 × 3 × 2 × 1) = 360,360/120 = **3,003** lineups.

**6.** (a) Total 5-card hands from 52 cards: C(52, 5) = 2,598,960. [1 mark]

(b) Choose exactly 2 aces from the 4 aces: C(4, 2) = 6. Choose the remaining 3 cards from the 48 non-ace cards: C(48, 3) = 17,296. Multiply: 6 × 17,296 = **103,776** hands. [3 marks]

(c) Probability = (favorable hands) / (total hands) = 103,776 / 2,598,960. This fraction simplifies to **54,145 / 1,294,962** (in lowest terms), which is approximately 0.0399 or about 4%. [1 mark]
