# Lesson 4: Percentages & Percent Change

## What You'll Learn
- Calculating percent increase: $\text{new} = \text{original} \times (1 + r)$
- Calculating percent decrease: $\text{new} = \text{original} \times (1 - r)$
- Successive percent changes and why they are NOT additive
- Finding original values given a percent change (working backwards)
- SAT-specific phrasing: "percent greater than," "percent less than," "percent of"
- The multiplying factor method for multi-step problems

## SAT Context

Percentage questions are among the most frequent on the SAT, appearing 3-5 times per test. The math is simple multiplication, but the SAT's phrasing is deliberately tricky. They love successive discounts ("20% off, then an additional 10% off"), percent change questions that require finding the original ("after a 25% increase, the price is $80"), and comparison questions ("by what percent is A greater than B?"). For an AAHL student, the computation is trivial—the challenge is the SAT's specific wording traps and the counterintuitive nature of successive percentages.

## The Multiplying Factor Method

Instead of calculating the percent change and then adding/subtracting, use a **multiplying factor**:

### Percent Increase
$$V_{\text{new}} = V_{\text{original}} \times (1 + r)$$
where $r$ is the decimal form of the percent.

| Percent Increase | Factor $(1 + r)$ |
|-----------------|------------------|
| 10%             | 1.10             |
| 25%             | 1.25             |
| 100% (double)   | 2.00             |
| 5.5%            | 1.055            |

### Percent Decrease
$$V_{\text{new}} = V_{\text{original}} \times (1 - r)$$

| Percent Decrease | Factor $(1 - r)$ |
|-----------------|------------------|
| 10%             | 0.90             |
| 25%             | 0.75             |
| 80%             | 0.20             |
| 3%              | 0.97             |

### Why This Method Is Superior
Instead of: $80 + 15\% \times 80 = 80 + 12 = 92$
Use: $80 \times 1.15 = 92$

The factor method scales to multiple steps cleanly and makes it easy to reverse the operation.

## Finding the Percent Change

When given original and new values:
$$\text{Percent change} = \frac{\text{new} - \text{original}}{\text{original}} \times 100\%$$

**Critical:** The denominator is always the **original** value, not the new value.

**Example:** Price goes from $50$ to $70$:
$$\text{Percent change} = \frac{70 - 50}{50} \times 100\% = \frac{20}{50} \times 100\% = 40\% \text{ increase}$$

**Example:** Price goes from $70$ to $50$:
$$\text{Percent change} = \frac{50 - 70}{70} \times 100\% = \frac{-20}{70} \times 100\% \approx -28.6\% \text{ decrease}$$

> **🚨 SAT TRAP ALERT: Successive Percentages Are NOT Additive.** A 20% discount followed by a 10% discount is NOT a 30% discount. The second discount applies to the already-reduced price.
>
> **Correct:** Original $\$100$ → 20% off = $\$80$ → 10% off $\$80$ = $\$72$. Total discount: $28\%$.
>
> **The SAT will put 30% as an answer choice.** Many students will pick it. Don't be one of them.
>
> **General formula for two successive changes** with factors $f_1$ and $f_2$:
> $$\text{Final} = \text{Original} \times f_1 \times f_2$$
> The combined factor for 20% off then 10% off: $0.80 \times 0.90 = 0.72$, which is a 28% discount.

> **🔍 PATTERN RECOGNITION: "Percent greater than" vs. "Percent of."** When the SAT says "$A$ is $p\%$ greater than $B$," it means $A = B \times (1 + \frac{p}{100})$. When it says "$A$ is $p\%$ of $B$," it means $A = B \times \frac{p}{100}$. These are totally different! "$A$ is 150% greater than $B$" means $A = B \times (1 + 1.50) = 2.5B$, while "$A$ is 150% of $B$" means $A = 1.5B$. This distinction is one of the SAT's favorite traps.

### Worked Example 1: Successive Discounts

**Problem:** A jacket originally priced at $\$180$ is on sale for 30% off. An additional 20% off is applied at the register for clearance items. What is the final price?

A) $\$90.00$
B) $\$100.80$
C) $\$108.00$
D) $\$115.20$

**Solution:**
1. First discount (30% off): factor $= 1 - 0.30 = 0.70$. Price $= 180 \times 0.70 = 126$.
2. Second discount (20% off): factor $= 1 - 0.20 = 0.80$. Price $= 126 \times 0.80 = 100.80$.
3. Or in one step: $180 \times 0.70 \times 0.80 = 180 \times 0.56 = 100.80$.

**Answer: B, $\$100.80$.**

**Wrong answer analysis:**
- A ($\$90.00$): This is what you get if you add the discounts (30% + 20% = 50%): $180 \times 0.50 = 90$. The classic successive-percent trap.
- C ($\$108.00$): This is 40% off: $180 \times 0.60 = 108$. Might come from 30% + "half of 20%" or other incorrect combination.
- D ($\$115.20$): This is 36% off: $180 \times 0.64 = 115.20$. Actually, that's close to $0.8 \times 0.8 = 0.64$, so maybe treating both as 20% off.

### Worked Example 2: Finding Original Given Percent Change

**Problem:** After a 25% increase, the population of a town is 15,000. What was the original population?

**Solution:**
1. Let original $= x$. After 25% increase: $x \times 1.25 = 15,000$.
2. Solve: $x = \frac{15,000}{1.25} = 12,000$.

**Common error:** Computing $15,000 - 25\% \times 15,000 = 15,000 - 3,750 = 11,250$. This is wrong because the 25% should be applied to the *original* (smaller) value, not the *final* (larger) value. A 25% increase followed by a 20% decrease does NOT return you to the original: $100 \to 125 \to 100$. Note: $1.25 \times 0.80 = 1.00$, so a 25% increase is reversed by a 20% decrease, not a 25% decrease!

**The reversal formula:** If increased by $r$, to return to original, multiply by $\frac{1}{1+r}$.

### Worked Example 3: "Percent Greater Than" Comparison

**Problem:** In 2020, Company A's revenue was $\$40$ million and Company B's revenue was $\$25$ million. Company A's revenue is what percent greater than Company B's?

**Solution:**
1. Difference: $40 - 25 = 15$ million.
2. Percent greater = $\frac{\text{difference}}{\text{Company B (reference)}} \times 100\% = \frac{15}{25} \times 100\% = 60\%$.

**Key:** "A is what percent greater than B" → the denominator is B, the reference point.

If instead the question asked "Company B's revenue is what percent less than Company A's?": $\frac{15}{40} \times 100\% = 37.5\%$. Different answer! The reference point matters.

> **🚨 SAT TRAP ALERT: Percent Decrease Does Not Reverse Percent Increase.** If a value increases 25%, then decreasing it by 25% does NOT return to the original. Example: $100 \xrightarrow{+25\%} 125 \xrightarrow{-25\%} 93.75$. The same principle applies in reverse: a 25% decrease ($100 \to 75$) is not reversed by a 25% increase ($75 \to 93.75$).

### Extra: Repeated Percent Change (Growth and Decay)

The SAT sometimes tests repeated percent changes (compound interest, population growth, depreciation):

$$\text{Final} = \text{Initial} \times (1 \pm r)^n$$

Where $n$ is the number of time periods.

**Example:** $\$1000$ invested at 5% annual interest for 3 years:
$$A = 1000(1.05)^3 = 1000 \times 1.157625 = \$1157.63$$

---

## Practice Problems

1. A store offers a 40% discount on a $\$250$ item, then takes an additional 15% off the discounted price. What is the final price?
   A) $\$112.50$
   B) $\$127.50$
   C) $\$137.50$
   D) $\$150.00$

2. After a 30% decrease in value, a car is worth $\$14,000$. What was the original value?
   A) $\$18,200$
   B) $\$20,000$
   C) $\$21,000$
   D) $\$23,333$

3. The population of a city increased by 15% from 2010 to 2020, then decreased by 5% from 2020 to 2025. If the population in 2010 was 80,000, what was the population in 2025?
   A) 87,400
   B) 88,000
   C) 92,000
   D) 96,600

4. The price of a stock increased from $\$45$ to $\$63$. What was the percent increase?
   A) 29%
   B) 33%
   C) 40%
   D) 43%

5. A smartphone's battery decreases by 8% each hour when in use. If the battery starts at 100%, what percent remains after 3 hours? (Round to the nearest percent.)
   A) 76%
   B) 78%
   C) 82%
   D) 84%

6. **(Challenge)** In an election, Candidate X received 60% of the votes, and Candidate Y received the rest. Candidate X won by 8,400 votes. How many total votes were cast?
   A) 28,000
   B) 35,000
   C) 42,000
   D) 48,000

---

## Answers

1. **Answer: B.** Factor method: $250 \times 0.60 \times 0.85 = 250 \times 0.51 = 127.50$. **Wrong answers:** A ($112.50$): $250 \times (1 - 0.40 - 0.15) = 250 \times 0.45 = 112.50$, the additive trap. C ($137.50$): 45% off total? $250 \times 0.55 = 137.50$. D ($150.00$): $250 \times 0.60 = 150$, forgetting the second discount.

2. **Answer: B.** After 30% decrease: original $\times 0.70 = 14,000$. Original $= 14,000 / 0.70 = 20,000$. **Wrong answers:** A ($18,200$): $14,000 \times 1.30 = 18,200$, incorrectly applying 30% to the reduced value. C ($21,000$): $14,000 / (2/3) = 21,000$, perhaps mistaking 30% as $\frac{3}{10}$ and dividing by $\frac{7}{10}$ incorrectly. D ($23,333$): $14,000 \times \frac{5}{3} \approx 23,333$, perhaps using $\frac{2}{3}$ factor instead of $0.70$.

3. **Answer: A.** $80,000 \times 1.15 \times 0.95 = 80,000 \times 1.0925 = 87,400$. **Wrong answers:** B ($88,000$): $80,000 \times 1.10 = 88,000$, treating 15% increase and 5% decrease as net 10% increase (additive trap). C ($92,000$): $80,000 \times 1.15 = 92,000$, ignoring the 5% decrease entirely. D ($96,600$): $80,000 \times 1.15 \times 1.05 = 96,600$, treating both as increases.

4. **Answer: C.** Percent change $= \frac{63 - 45}{45} \times 100\% = \frac{18}{45} \times 100\% = 0.40 \times 100\% = 40\%$. **Wrong answers:** A (29%): $\frac{18}{63} \times 100\% \approx 28.6\%$, using new value as denominator (classic trap). B (33%): rough estimate, no clear derivation. D (43%): $\frac{63}{45} \approx 1.4$, so 40% is correct; 43% might be from $\frac{63-45}{45} \times 100$ miscalculated.

5. **Answer: B.** Each hour: multiply by $0.92$. After 3 hours: $100\% \times 0.92^3 = 100\% \times 0.778688 \approx 77.9\%$, rounds to 78%. **Wrong answers:** A (76%): $100 - 8 \times 3 = 76$ (additive trap—subtracting 8% three times, which ignores compounding). C (82%): rough estimate, possibly only 2 hours of decay. D (84%): only one hour of decay ($100 \times 0.92 = 92$), then perhaps misreading.

6. **Answer: C.** Let total votes $= T$. Candidate X: $0.60T$, Candidate Y: $0.40T$. Difference: $0.60T - 0.40T = 0.20T = 8,400$. $T = \frac{8,400}{0.20} = 42,000$. **Wrong answers:** A ($28,000$): $8,400 / 0.30 = 28,000$, perhaps using 30% as the margin. B ($35,000$): $8,400 / 0.24 = 35,000$, unclear derivation. D ($48,000$): $8,400 / 0.175 = 48,000$, or $8,400 \times \frac{100}{60-40}$ miscalculated.
