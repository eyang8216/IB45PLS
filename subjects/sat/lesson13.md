# Lesson 13: Exponential Growth & Decay (SAT Applications)

## What You'll Learn
- The exponential model $y = a(1 \pm r)^t$ and what each variable represents
- How to calculate and apply **growth factors** ($1+r$) and **decay factors** ($1-r$)
- Doubling time, half-life, and how to set up equations for each
- Common SAT contexts: population growth, bacteria, investment returns, depreciation
- The critical distinction between the **rate** $r$ and the **multiplier** $(1 \pm r)$
- How to identify exponential patterns from tables, graphs, and word problems

## SAT Context
Exponential growth and decay problems appear in **4–6 questions** across both SAT math modules, typically in the Problem Solving and Data Analysis domain. These questions are dressed in real-world contexts — populations doubling, cars depreciating, investments compounding — and the SAT tests whether you truly understand what the multiplier means. The most frequent error students make is using the rate $r$ directly instead of $(1 \pm r)$, which produces an answer that looks "close enough" to be among the answer choices. The SAT designers know this and deliberately include that wrong answer as a distractor. Your IB AAHL background gives you the algebraic toolkit; this lesson connects that toolkit to the specific ways the SAT frames exponential problems.

---

## The Core Formula

$$y = a(1 \pm r)^t$$

Where:
- $y$ = final amount (what you're usually solving for, or given)
- $a$ = initial amount (starting value at $t = 0$)
- $r$ = rate of change, expressed as a **decimal** (not a percentage)
- $t$ = number of time periods elapsed
- Use $(1+r)$ for **growth** (the quantity increases each period)
- Use $(1-r)$ for **decay** (the quantity decreases each period)

> **🚨 SAT TRAP ALERT:** The SAT will give you a rate like "8% annual growth" and include answer choices with both $1.08$ and $0.08$. The multiplier is **always** $1+r$ (so $1.08$), never just $r$ ($0.08$). Using $r$ alone would mean your quantity shrinks to almost nothing immediately. If you see $0.92$ in a decay problem, that's $1 - 0.08$, not $0.08$ alone.

> **🔍 PATTERN RECOGNITION:** Whenever a problem uses language like "increases by the same percent each year," "loses value at a constant rate," "doubles every," or "halves every," you are dealing with an exponential model. The key signal is **repeated multiplication** by a constant factor.

### Understanding the Multiplier

| Percent Change | Decimal $r$ | Multiplier $(1 \pm r)$ |
|:---|---:|:---:|
| 5% growth | 0.05 | 1.05 |
| 8% growth | 0.08 | 1.08 |
| 12% growth | 0.12 | 1.12 |
| 50% growth | 0.50 | 1.50 |
| 100% growth (doubles) | 1.00 | 2.00 |
| 5% decay | 0.05 | 0.95 |
| 8% decay | 0.08 | 0.92 |
| 20% decay | 0.20 | 0.80 |

Notice: a 100% increase doubles the quantity (multiplier = 2), but a 100% decrease would reduce it to zero (multiplier = 0, not $-1$). Decay never uses a negative multiplier on the SAT — the quantity approaches but never reaches zero.

---

## Doubling Time

When a quantity doubles in fixed time intervals, you don't always get a percent rate directly. Instead, the problem gives you the **doubling period**.

**General setup:** If something doubles every $d$ time units, and you observe for $t$ time units:

$$y = a \cdot 2^{t/d}$$

Where $t/d$ counts how many doubling periods have elapsed.

> **🔍 PATTERN RECOGNITION:** "Doubles every 3 hours" means $d = 3$. After 12 hours, the exponent is $12/3 = 4$, so the quantity is multiplied by $2^4 = 16$. You can always convert this to a $(1+r)^t$ form by finding the equivalent rate, but the $2^{t/d}$ form is usually faster on the SAT.

### Worked Example 1: Bacteria Doubling

**Problem:** A colony of 500 bacteria doubles in size every 4 hours. Which expression gives the number of bacteria after 20 hours?

(A) $500(2)^{20}$  
(B) $500(2)^{5}$  
(C) $500(2)^{4}$  
(D) $500(20)^2$

**Solution:** Here $a = 500$, $d = 4$, and $t = 20$. The number of doubling periods is $t/d = 20/4 = 5$. So the colony size is $500 \cdot 2^5$. **Answer: (B)**

**Wrong-Answer Analysis:**
- (A) uses $t=20$ directly as the exponent — forgetting to divide by the doubling period
- (C) uses $d=4$ as the exponent — mixing up the doubling period with the number of periods
- (D) scrambles numbers into a completely wrong structure

---

## Half-Life (Exponential Decay)

For radioactive decay, medication in the bloodstream, or any quantity that halves in fixed intervals:

$$y = a \cdot \left(\frac{1}{2}\right)^{t/h}$$

Where $h$ is the half-life (time to reduce by half).

Equivalently: $y = a \cdot 2^{-t/h}$ or $y = a \cdot (0.5)^{t/h}$

> **🚨 SAT TRAP ALERT:** A half-life of 10 years does NOT mean the quantity is zero after 20 years. After 20 years, you've had two half-lives, so $\frac{1}{4}$ remains, not zero. The SAT will sometimes include 0 as a distractor.

### Worked Example 2: Medication Half-Life

**Problem:** A patient takes 200 mg of a medication. The amount remaining in the bloodstream halves every 6 hours. To the nearest mg, how much remains after 15 hours?

**Solution:** $a = 200$, $h = 6$, $t = 15$. The number of half-lives is $15/6 = 2.5$.

$$y = 200 \cdot \left(\frac{1}{2}\right)^{2.5} = 200 \cdot 0.1768 \approx 35 \text{ mg}$$

**Answer: 35**

---

## Compound Interest (A Special Case)

Though the SAT often provides the compound interest formula, knowing it helps:

$$A = P\left(1 + \frac{r}{n}\right)^{nt}$$

Where $n$ is the number of compounding periods per year. For annual compounding ($n=1$), this reduces to our standard form: $A = P(1+r)^t$.

> **🔍 PATTERN RECOGNITION:** If the problem says "compounded annually," you can use the simple $y = a(1+r)^t$ form. If it says "compounded quarterly" ($n=4$) or "compounded monthly" ($n=12$), you need the full formula. Most SAT compound interest questions stick to annual compounding.

---

## Identifying Exponential Behavior from Tables

The SAT may show you a table of values and ask whether the relationship is linear or exponential.

- **Linear:** Constant **difference** between consecutive y-values (add/subtract same amount)
- **Exponential:** Constant **ratio** between consecutive y-values (multiply by same factor)

| $x$ | 0 | 1 | 2 | 3 |
|:---:|:---:|:---:|:---:|:---:|
| $f(x)$ | 3 | 6 | 12 | 24 |

The ratios: $6/3 = 2$, $12/6 = 2$, $24/12 = 2$ — constant ratio of 2, so this is exponential with $f(x) = 3 \cdot 2^x$.

| $x$ | 0 | 1 | 2 | 3 |
|:---:|:---:|:---:|:---:|:---:|
| $g(x)$ | 5 | 8 | 11 | 14 |

The differences: $8-5 = 3$, $11-8 = 3$, $14-11 = 3$ — constant difference of 3, so linear.

> **🚨 SAT TRAP ALERT:** Don't rely on just the first two points. An exponential and a linear function can agree on two points but diverge wildly after that. Always check at least three consecutive data points when identifying the type of function.

---

## Solving for Unknown Variables

### Finding the Rate $r$

If you know $a$, $y$, and $t$, you can solve for $r$:

$$y = a(1 \pm r)^t \implies 1 \pm r = \left(\frac{y}{a}\right)^{1/t} \implies r = \left(\frac{y}{a}\right)^{1/t} - 1$$

### Worked Example 3: Finding the Growth Rate

**Problem:** An investment of \$5,000 grows to \$6,200 after 3 years with annual compounding. What is the approximate annual growth rate?

**Solution:**

$$6200 = 5000(1+r)^3$$
$$\frac{6200}{5000} = (1+r)^3$$
$$1.24 = (1+r)^3$$
$$1+r = \sqrt[3]{1.24} \approx 1.0743$$
$$r \approx 0.0743 = 7.43\%$$

---

## When Exponential Models Break Down (Domain Awareness)

On the SAT, exponential models are applied to discrete quantities (people, bacteria, cars) but the equation itself is continuous. The SAT wants you to:
1. Calculate correctly using the continuous equation
2. Recognize that fractional results may need rounding (e.g., 125.7 bacteria → 126)
3. Understand that the model is an approximation

---

## Practice Problems

### Problem 1
A town's population of 34,000 is growing at 3% per year. Which expression represents the population after $t$ years?

(A) $34000(0.03)^t$  
(B) $34000(1.03)^t$  
(C) $34000(0.97)^t$  
(D) $34000(3)^t$

### Problem 2
A car depreciates 15% of its value each year. If it was purchased for \$28,000, which of the following is closest to its value after 5 years?

(A) \$7,000  
(B) \$12,435  
(C) \$15,960  
(D) \$23,800

### Problem 3
A colony of bacteria triples every 2 hours. If there are initially 100 bacteria, how many bacteria will there be after 6 hours?

(A) 300  
(B) 900  
(C) 2,700  
(D) 8,100

### Problem 4
A radioactive substance decays so that half remains every 8 days. If the initial mass is 64 grams, how many grams remain after 20 days?

### Problem 5
The value of a certain stock decreases by 20% each month. At the end of how many full months will the stock first be worth less than 10% of its original value?

### Problem 6
The table shows values of an exponential function $f(x) = a \cdot b^x$. Find $f(4)$.

| $x$ | 0 | 1 | 2 | 3 | 4 |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $f(x)$ | 5 | 7.5 | 11.25 | 16.875 | ? |

---

## Answers

### Problem 1 — Answer: (B)

Growth of 3% → $r = 0.03$ → multiplier = $1 + 0.03 = 1.03$. Expression: $34000(1.03)^t$.

**Wrong-answer analysis:**
- (A) $34000(0.03)^t$ — uses the rate instead of the multiplier; this would make the population shrink toward zero
- (C) $34000(0.97)^t$ — decay multiplier (3% decrease), wrong direction
- (D) $34000(3)^t$ — uses the percentage as a whole number (300% growth), not 3%

---

### Problem 2 — Answer: (B)

$r = 0.15$, decay multiplier = $1 - 0.15 = 0.85$. After 5 years:

$$V = 28000(0.85)^5$$

$$(0.85)^5 = 0.85 \times 0.85 \times 0.85 \times 0.85 \times 0.85 \approx 0.4437$$

$$V = 28000 \times 0.4437 \approx 12424 \approx \$12,435$$

**Wrong-answer analysis:**
- (A) \$7,000 — comes from $28000 \times 0.25$ (linear decay: 15% × 5 = 75% loss), not exponential
- (C) \$15,960 — comes from $28000 \times (1 - 5 \times 0.15) = 28000 \times 0.25$ wrong calculation
- (D) \$23,800 — comes from $28000 \times 0.85$ (only one year of depreciation), not 5 years

---

### Problem 3 — Answer: (C)

Triples every 2 hours: multiplier per 2 hours is 3. After 6 hours, $6/2 = 3$ tripling periods.

$$y = 100 \cdot 3^3 = 100 \cdot 27 = 2700$$

**Wrong-answer analysis:**
- (A) 300 — used addition ($100 + 3 \times 100/2$...), not multiplication
- (B) 900 — tripled once ($100 \times 3^2$), thinking 6 hours = 2 periods
- (D) 8,100 — used $100 \times 3^4$, off by one period

---

### Problem 4 — Answer: Approximately 11.3 grams

Half-life $h = 8$ days, $t = 20$ days, $a = 64$.

Number of half-lives: $20/8 = 2.5$.

$$y = 64 \cdot \left(\frac{1}{2}\right)^{2.5} = 64 \cdot (0.5)^{2.5}$$

$(0.5)^{2.5} = \sqrt{(0.5)^5} = \sqrt{0.03125} \approx 0.1768$

$y = 64 \times 0.1768 \approx 11.3$ grams.

---

### Problem 5 — Answer: 11 months

After each month, the stock is worth $0.80$ of its previous value. After $m$ months, value = $P \cdot (0.80)^m$. We want this to be less than $0.10P$:

$$(0.80)^m < 0.10$$

Taking logs: $m \cdot \ln(0.80) < \ln(0.10)$

Since $\ln(0.80) \approx -0.2231$ and $\ln(0.10) \approx -2.3026$:

$$m > \frac{-2.3026}{-0.2231} \approx 10.32$$

So the first **full month** where the value drops below 10% is $m = 11$.

**Check:** $(0.80)^{10} \approx 0.1074$ (still above 10%), $(0.80)^{11} \approx 0.0859$ (below 10%). ✓

---

### Problem 6 — Answer: $f(4) = 25.3125$

Find the ratio: $7.5/5 = 1.5$, $11.25/7.5 = 1.5$, $16.875/11.25 = 1.5$. Constant ratio $b = 1.5$. Initial value $a = 5$.

$f(x) = 5 \cdot (1.5)^x$, so $f(4) = 5 \cdot (1.5)^4 = 5 \cdot 5.0625 = 25.3125$.

The function shows 50% growth per unit increase in $x$.

---

## Key Takeaways

1. **Always use $(1 \pm r)$, never just $r$.** This is the #1 SAT trap for exponential problems.
2. For doubling: $y = a \cdot 2^{t/d}$; for half-life: $y = a \cdot (1/2)^{t/h}$.
3. Check whether the problem uses the **same time unit** for rate and period (years vs. months is a common trap).
4. Exponential functions have constant **ratios** between consecutive outputs, not constant differences.
5. When solving for time, logarithms are your tool — but on the SAT, the answer choices for time are often small integers you can test.
