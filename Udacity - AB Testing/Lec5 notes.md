# Lec 5 – Analyzing Results

### Sanity Checks
- Maybe something went wrong in the experiment diversion and now your experiment and your control aren’t comparable
- Maybe you set up the filter differently in the experiment and the control
- Set up data capture and your data capture isn’t actually capturing the events that you want to look for in your experiment

### Invariant Metrics
- Population sizing metrics based on unit of diversion: Checking whether your experiment population and control population are actually comparable
- Actual invariants (those metrics that shouldn’t change when you run your experiment): test that they didn’t change
 
### How to check invariant and see whether it’s reasonably close between the control and experiment groups
- Run experiment for 2 weeks
- Unit of diversion: cookie
 
Total Control: 64,454
Total Experiment: 61,818

 Is this difference within what we expect? Ignoring the day-by-day data for a minute, how would we figure out whether the difference between the total number of cookies in control and experiment group is within what we expect? (Given each cookie is randomly assigned to the control or experiment group with probability 0.5)
- Compute SD of binomial with probability 0.5 of success
	* SD = sqrt(0.5 * 0.5 / 64,454 + 61,818) = 0.0014
- Multiply by z-score to get margin of error
	* m = SD * 1.96 = 0.0027
- Compute confidence interval around 0.5
	* 0.4973 to 0.5027
- Check whether observed fraction is within interval
	* p^ = 64,454 / 64,454 + 61,818 = 0.5104
  
 0.5104 doesn’t fall into CI, so something is off

To get a better idea of what could be going wrong, it’s a good idea to look at day-by-day data
 
There were a few days with 0.53 or higher, and no day stands out as the highest. This points to an overall problem rather than a problem on a specific day. Should talk to the engineers and figure out something is wrong with the experiment set up. Also, can try slicing to see if one particular slice is weird. Check age of cookies – does one group have more new cookies.

Another experiment: run experiment for 7 days; unit of diversion is “event”
- Total events control: 15,348
- Total events experiment: 15,312

SD = sqrt(0.5*0.5 / 15,348+15,312) = 0.0029
m = 1.96 * SD = 0.0056
 
If one of our sanity checks fail, analyze why sanity check went wrong. So, how do you figure out what went wrong?
- Talk to engineers: Is there something wrong with the experiment infrastructure? Is the experiment set up correctly? Something wrong with unit of diversion?
- Retrospective Analysis: Is there something endemic to what you are trying to do that may be causing the situation
- Pre-period & Post-period: Did I see the same changes in those invariances in my pre-period. If I saw them in the pre-period and the experiment, that probably means there is a problem with the experiment infrastructure & set up. On the other hand, if you only see the change only in your experiment but not in the pre-period, that points to something with the experiment itself, maybe the “data capture” or something along those lines. 

### Single Metric
- Goal is to make a business decision about whether your experiment has favorably impacted your metrics. Analytically, that means you want to decide if you’ve observed a statistically significant result of your experiment
- We also want to measure the magnitude and the direction of the change.
- What if our results are not statistically significant?
	* Break down into different platforms or different days of the week. This can not only help you find bugs in the experiment setup but it might give you a new hypothesis about how people are reacting to your experiment
	* Cross checking results with other results (e.g. non-parametric sign tests)

###### Single Metric Example
- Experiment: Change color and placement of “Start Now” button
- Metric: Click through rate
- Unit of diversion: cookie
- dmin=0.01; alpha=0.05; beta=0.2
 
Confidence Interval: 0.0220 to 0.0380
Recommendation: Launch

Now we also do a sanity check
- Number of days: 7
- Number of days with positive change (days where experiment click through rate is higher than control): 7
- If no difference, 50% chance of positive change on each day (Cannot assume normal because 7 is not enough for binomial to approximate normal distribution)  two tail p value = 0.0156 < alpha=0.05  Unlikely to have happened by chance  Recommendation: Launch doesn’t change

###### Single Metric Another Example
 
Empirical SE: 0.0062 with 5000 page views in each group
 
Days where CTR is higher in experiment: 9/14  Two tail p value = 0.4240 > 0.05
 
- Could be that weekend is more likely to have larger difference than weekdays
- Recommendation: Do not launch (yet). Dig into deeper why the change didn’t affect weekday visitors as much.

###### What to do when Sign test and hypothesis test disagree
- Take a critical look about how your feature functions: Is it really operating differently for different subgroups, for example on a specific platform
- Simpson’s paradox: Bunch of different subgroups in your data (e.g. user populations) and within each subgroup, the results are stable but if you aggregate altogether it’s the mix of subgroups that actually drives the result
 
### Multiple Metrics
- For multiple metrics, the more things you test, the more likely you are to see significant differences just by chance. So if you are testing 20 metrics ad you have a 95% confidence level, you would expect to see one case at least that time where you got a result that says it’s significant but it’s only occurring by chance. So this is a problem, but you are not sunk because it shouldn’t be repeatable.
- Have technique to account for this called “multiple comparisons” that adjust significance level, so that it accounts for how many metrics or how many different tests you are doing
- If you want to set up say automatic alerting that tells you, oh one of my metrics was significantly different on this experiment, you probably want to use multiple comparisons
https://en.wikipedia.org/wiki/Multiple_comparisons_problem

### Multiple Metrics: Example
- Experiment: Prompt students to contact coach more frequently
- Metrics: Probability that student signs up for coaching; How early students sign up for coaching; Average price paid per student
- If Audacity tracks all three metrics and does three separate significance tests (alpha = 0.05), what is the probability at least one metric will show a significant different if there is no true difference (i.e. For 3 metrics, what is the chance of at least 1 False Positive)
* P(FP=0) = 0.95 * 0.95 * 0.95 = 0.857 (Assuming Independence)
* P(FP >= 1) = 1 – 0.857 = 0.143
- What is the probability of at least one false positive for: 
* 10 metrics and 95% confidence: 0.401 (alpha overall = 1 – (1 – alpha individual)^n)
* 10 metrics and 99% confidence: 0.096
 
### Another Example
- Problem: Probability of any false positive increases as you increase number of metrics
- Solution: Use higher confidence level for each metric
- Method 1: Assume Independence  alpha_overall = 1 – (1 - alpha_individual)^n
- Method 2: Bonferrori Correction (simple, no assumptions, conservation because guaranteed to give alpha_overall at least as small as specified)
https://en.wikipedia.org/wiki/Bonferroni_correction
* alpha_individual = alpha_overall / n 
* alpha_overall = 0.05; n = 3; alpha_individual = 0.0167

https://en.wikipedia.org/wiki/False_discovery_rate
https://en.wikipedia.org/wiki/Closed_testing_procedure
https://en.wikipedia.org/wiki/Boole%27s_inequality
https://en.wikipedia.org/wiki/Holm%E2%80%93Bonferroni_method

### Analyzing Multiple Metrics
- All related metrics are going to move in the same direction (e.g. click through rate & click through probability)
- When you have a composite metric (e.g. RPM revenue per thousand queries is composed of click through rate and cost per clicks)
- Multiple metrics can be unruly: Let’s say you’ve decided that reading time on the page or stay time is a good signal. People like your page. But clicks are also a good signal. And so then you might see that when you make a UI change to the page, people spend time less reading but more time clicking. You can’t really quantitatively evaluate which one is better.
- OEC (Overall Evaluation Criteria): It doesn’t absolve you of understanding why stay time and clicks are moving in these different directions. What it can be helpful with this balancing long term investment like return visits to the site with short term day to day metrics like increased clicks, you don’t want to lose one in pursuing the other one. So often the best OICs give you a good balance between those two things.
- How do you find a good OEC? : A lot of validation. But start from some kind of business analysis. Our company wants to look at 25% revenue plus 75% increase usage of the site. But you want to make sure that you don’t plan so much around what the company thinks should happen with those experiments that you steer yourself in a way that you hid other changes that you weren’t expecting.

### Drawing Conclusions
- Once we figured out which metrics have significant changes, what comes next: Now you have to decide what your results do and don’t tell you. If you have statistically significant results, then that means you are unlikely to have zero impact on the user experience. But now the questions come down to A, do you understand the change and B, do you want to launch the change?
- How do you decide whether to launch your change or not: (1) Do I have statistically and practically significant results in order to justify the change? (2) Do I understand what that change has actually done with user experience (3) Is it worth it?

### Changes over time
- Good practice to always do a ramp-up when you actually want to launch a change
- Remove all of the filters (e.g. only testing change only on English, for example, you want to test your change during your ramp-up on all users) Because what you want to know is if there’s been any incidental impact to unaffected users that you didn’t test in the original experiment
- But the effect may actually flatten out as you ramp up the change. 
* seasonality effects: when students go on vacation, behavior totally changes. And Black Friday etc shopping behavior is totally different.  To capture these kinds of seasonal and event drive variations, use “holdback”: launch change to everyone except for small holdback, a set of users, that don’t get the change, and you continue comparing their behavior to control. Now, in that case, you should see the reverse of the impact that you saw in your experiment and what you can do is you can track that over time until you are confident that your results are repeatable.
* Novelty effect, change aversion behavior of users  use “cohort”
































