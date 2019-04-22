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



































