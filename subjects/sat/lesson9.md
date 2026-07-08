# Lesson 9: Statistical Claims, Margin of Error & Sampling

## What You'll Learn
- Interpreting margin of error: what it does and doesn't tell you
- Understanding what makes a sample random and representative
- Identifying common sampling biases: voluntary response, convenience, undercoverage
- Evaluating the validity of conclusions from survey and experiment data
- The difference between sample results and population conclusions
- SAT-specific statistical reasoning traps

## SAT Context

Margin of error and statistical reasoning questions appear 1-3 times per SAT. These are among the most missed questions nationally because they test statistical literacy rather than computation. The SAT does NOT ask you to calculate margin of error—it asks you to interpret it. For an AAHL student, these concepts are not covered in depth (AAHL focuses on probability theory, not survey methodology), making this one of the most important new topics to master. The good news: the reasoning patterns are predictable once you learn them.

## Margin of Error

### What It Means
A survey result reported as "$54\%$ with a margin of error of $\pm 3\%$" means the true population value is likely between $51\%$ and $57\%$.

### What Margin of Error Tells You
- The **range** of plausible values for the population parameter.
- If two ranges overlap, the difference between groups might not be statistically meaningful.

### What Margin of Error Does NOT Tell You
- It says nothing about whether the sample size was adequate.
- It says nothing about whether the sampling method was biased.
- It is not an "error" in the sense of a mistake—it reflects natural sampling variability.

> **🚨 SAT TRAP ALERT: Margin of Error Misinterpretation.** The SAT will give you a survey result like "62% of respondents support the proposal, margin of error ±4%" and ask which statement is correct. Wrong answer choices will say things like:
> - "The survey is wrong by 4%." (No—margin of error is about precision, not correctness.)
> - "Exactly 62% of the population supports the proposal." (No—that's the sample statistic, not the population parameter.)
> - "The sample size is too small." (Margin of error alone doesn't tell you this; it's not about the sample size being "wrong.")
> 
> **The correct interpretation is always:** "Between 58% and 66% of the population likely supports the proposal" or "The true percentage is likely within 4 percentage points of 62%."

> **🔍 PATTERN RECOGNITION: When Margin of Error ranges overlap, you can't declare a winner.** If Candidate A polls at 48% ±3% and Candidate B polls at 46% ±3%, the ranges are 45-51% and 43-49%. They overlap (45-49). This means the race is "too close to call" or "within the margin of error." The SAT loves to ask whether one candidate is definitively ahead—the answer is NO when ranges overlap.

## Sampling Methods

### Random Sampling (GOOD)
Every member of the population has an equal chance of being selected. This produces **representative samples** and allows valid conclusions about the population.

### Convenience Sampling (BAD)
Surveying whoever is easy to reach (e.g., people walking by the library). This introduces bias because the sample may not represent the population.

### Voluntary Response Sampling (BAD)
People choose to participate (e.g., online polls, call-in surveys). Those with strong opinions are more likely to respond, producing biased results.

### Undercoverage (BAD)
Some groups in the population are underrepresented or excluded from the sampling frame (e.g., phone surveys that miss people without phones).

### Key SAT Question Patterns

**"Which of the following conclusions is most appropriate?"**

To answer:
1. Check if the sample was randomly selected. If not, results may not generalize to the population.
2. Check if the question wording was neutral. Leading questions produce biased responses.
3. Check if the conclusion matches what was actually measured. (Correlation ≠ causation!)
4. Check if the margin of error allows a definitive conclusion.

### Valid vs. Invalid Conclusions

| Scenario | Valid Conclusion | Invalid Conclusion |
|----------|:----------------:|:------------------:|
| Random sample of 1,000 voters, 52% prefer A, MOE ±3% | Between 49% and 55% of voters likely prefer A | A will definitely win the election |
| Convenience sample of gym members about exercise habits | Gym members who responded exercise X hours/week | The average American exercises X hours/week |
| Observational study: coffee drinkers have lower heart disease | Association observed between coffee and heart disease | Coffee prevents heart disease |

### Worked Example 1: Margin of Error Interpretation

**Problem:** A poll of 500 randomly selected voters found that 54% support a ballot measure, with a margin of error of ±4.4%. Which of the following is the best interpretation?

A) Exactly 54% of all voters support the measure.
B) Between 49.6% and 58.4% of voters in the sample support the measure.
C) It is likely that between 49.6% and 58.4% of all voters support the measure.
D) The poll is inaccurate by at least 4.4%.

**Solution:**
- A: No—54% is the sample statistic, not the population parameter.
- B: No—the margin of error applies to the population estimate, not the sample (we know the sample result exactly).
- C: Yes—the margin of error gives a plausible range for the true population value.
- D: No—"inaccurate" is the wrong framing. Margin of error describes precision, not accuracy.

**Answer: C.**

### Worked Example 2: Sampling Bias

**Problem:** A website posts a poll asking "Should the city build a new park?" and 78% of the 2,000 respondents say yes. Which is the most appropriate conclusion?

A) About 78% of city residents support the new park.
B) The majority of city residents oppose the new park.
C) People who visit the website tend to support the new park.
D) No valid conclusion about all city residents can be drawn from this poll.

**Solution:**
The sample is voluntary response (only people who chose to visit the website and take the poll are counted). This is not a random sample. Results cannot be generalized to all city residents.

**Answer: D.**

**Wrong answer analysis:**
- A: Invalid generalization from a biased sample.
- B: Opposite of the result and still an invalid generalization.
- C: This may be true but only describes the biased sample, not the population. D is the better conclusion.

### Worked Example 3: Overlapping Margin of Error

**Problem:** Two candidates are running for mayor. Poll A (sample size 600) finds Candidate X at 51% ±4%. Poll B (sample size 800) finds Candidate Y at 48% ±3.5%. Based on these polls, which statement is most justified?

A) Candidate X will win because 51% > 48%.
B) Candidate X is clearly ahead because both polls show more support.
C) The race is too close to call because the margins of error overlap.
D) The polls disagree, so neither is reliable.

**Solution:**
Poll A range: 47% to 55%.
Poll B range: 44.5% to 51.5%.

These ranges overlap substantially (47% to 51.5%). So we cannot be confident that X is ahead.

**Answer: C.**

**Wrong answer analysis:**
- A ignores margin of error.
- B misstates—Poll B shows Y at 48%, not X.
- D is wrong; the polls don't necessarily disagree; the ranges overlap, meaning they're consistent with each other.

---

## Practice Problems

1. A survey of 1,200 randomly selected adults found that 67% support recycling programs, with a margin of error of ±2.8%. Which conclusion is most appropriate?
   A) Exactly 67% of all adults support recycling programs.
   B) Between 64.2% and 69.8% of all adults likely support recycling programs.
   C) The survey is flawed because the margin of error is too large.
   D) Most adults do not support recycling programs.

2. A radio station asks listeners to call in and vote for their favorite song. Song A receives 52% of 3,400 votes. What can be concluded?
   A) Song A is the favorite of a majority of the station's listeners.
   B) About 52% of all people in the city prefer Song A.
   C) Song A received the most votes among those who called in.
   D) The sample size is large enough to generalize to all music listeners.

3. A poll shows 46% of voters favor a candidate with a margin of error of ±3%. Another poll shows 49% with a margin of error of ±3%. A journalist claims the candidate's support is clearly increasing. Is this justified?
   A) Yes, because 49% > 46%.
   B) Yes, because both polls have the same margin of error.
   C) No, because the confidence intervals (43-49% and 46-52%) overlap significantly.
   D) No, because polls are always unreliable.

4. A researcher surveys 200 people at a shopping mall about their spending habits. Which is the most serious concern about this study?
   A) The sample size is too small.
   B) The sample is not random and may not represent the general population.
   C) People at malls never tell the truth about spending.
   D) The margin of error cannot be calculated for mall surveys.

5. A study randomly assigns 100 patients to a new drug and 100 to a placebo. The drug group improves by 35% on average, placebo group by 10%. Which conclusion is valid?
   A) The drug definitely cures the condition.
   B) The drug shows a possible effect, but we need to check if the difference is statistically significant.
   C) The placebo effect is stronger than the drug effect.
   D) The study is invalid because 100 patients is too few.

6. **(Challenge)** A survey with margin of error ±5% finds that 53% of respondents favor a policy. Which of the following additional facts would most increase confidence that a majority of the population truly favors the policy?
   A) The sample was collected via voluntary online response.
   B) The sample size was only 100 people.
   C) The survey used random sampling and had a large sample size.
   D) Several friends of the researcher agreed with the result.

---

## Answers

1. **Answer: B.** This correctly applies the margin of error: $67\% \pm 2.8\%$ gives the range $64.2\%$ to $69.8\%$. **Wrong answers:** A treats the sample statistic as the exact population value. C makes a value judgment about the margin of error without basis—2.8% is reasonable for a survey. D is the opposite of what the data shows.

2. **Answer: C.** This is the only valid conclusion—it describes only the respondents, not the broader population. **Wrong answers:** A generalizes from a voluntary response sample to all listeners. B generalizes to the entire city. D incorrectly assumes large sample size overcomes voluntary response bias (it doesn't—size doesn't fix bias).

3. **Answer: C.** First poll: 43-49%. Second poll: 46-52%. The ranges overlap (46-49%). The increase could be due to sampling variability, not a real change. **Wrong answers:** A ignores margin of error. B is irrelevant—same MOE doesn't mean the difference is significant. D is an overstatement—polls can be reliable when properly conducted.

4. **Answer: B.** The sample is a convenience sample (mall shoppers), not random. It may not represent the general population (undercoverage of people who don't shop at malls). **Wrong answers:** A—200 people isn't necessarily too small; the bias is the bigger issue. C is an unwarranted assumption. D is incorrect—margin of error can be calculated, but it still wouldn't fix the sampling bias.

5. **Answer: B.** This is an experiment with random assignment, so causation CAN be inferred IF the difference is statistically significant. But we need more information before declaring it "definitely" works. **Wrong answers:** A is too strong. C is backward—the drug group improved more. D makes an unsupported claim about sample size.

6. **Answer: C.** Random sampling with a large sample size produces the most reliable estimates and the narrowest margins of error. **Wrong answers:** A—voluntary response is biased regardless of size. B—small sample size gives wider margin of error (more uncertainty). D—friends' agreement is anecdotal and irrelevant to statistical validity.
