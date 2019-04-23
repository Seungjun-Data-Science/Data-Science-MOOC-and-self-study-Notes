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


































