# Lec 4 – Designing an Experiment 

### Choose what you use as a “subject” in your experiment and in your control
- What are the units in the population that you are going to be running the test on and comparing (Unit of diversion)?
- Next, decide which subjects are eligible (everyone? Only subjects in US?)
- “Size” your experiment
- “Duration” of the experiment

### Unit of Diversion
- Need to decide how to assign events to either control or to the experiment
- Randomly assign every event (e.g. every page view to either control or experiment)
- So typically what you want to do for user visible change is assigning people as opposed to events  But how do you determine what’s a person? 
- Maybe use “user ID” but each person can have multiple log-ins
- Use anonymous identifier “cookie”: It’s tied to single browser and single device, so if you change from laptop to mobile phone, this will change cookie

### How to choose unit of diversion?
- User Consistency: If you are using User ID, then user gets a consistent experience as they change devices as long as they are signed in (e.g. If you are testing how courses are being displayed, then user will get consistent experience across devices) / BUT if you are testing a change that crosses the sign in sign out border the user id doesn’t work that well like changing the layout of the page or location of the sign in bar, then you may want to use cookie instead so that you can get consistency across the sig in and sign out border but not across devices
- For user visible changes, you definitely would use a cookie or user ID. But there are lot of changes that are not visible to users (e.g. latency changes, ranking function change). In this case, you consider what you want to measure. For example, if you want to see if users adapt to the new change (e.g. making the site slower, trying to see if users use the site less), you also need a unit of diversion like a cookie or user ID.
- IP Address
- You usually don’t get the consistency that you get from a user ID or a cookie because the user’s IP address could randomly change depending on what’s happening with the provider nor do you get the clean randomization that you get from like event based diversion
- But IP based diversion may be the only choice in some cases: e.g. testing out infra change when you are testing out one hosting provider v.s. different hosting provider to understand impact on latency
- Face analysis challenge: may not get clean comparison between your experiment and your control (so have to a lot of post analysis to try and find those good comparisons between your experiment and control)

### Ethical Considerations
- User ID is innately “identifiable”, so confidentiality & privacy become important considerations
- Informed consent
 
### Unit of Analysis v.s. Unit of Diversion
- Changing the unit of diversion can change the variability of a metric, sometimes pretty dramatically
 
### Intra-User Experiment
- Expose the same user to this feature being on and off over time and analyze how they behave in different time windows
- Pitfalls: have to really careful that you choose a comparable time window; frustration & learning problem where people learn to use the particular feature in the first two weeks and then when you turn it off, they are like, why did my website change? So you can get different results as a result

### Interleaved experiment
- Expose the same user to the A and the B side at the same time for things like search ranking, preferences or things have ordered ranked list
- This typically only works in cases where you are looking at reordering a list
- In an interleaved ranking experiment, suppose you have two ranking algorithms, X and Y. Algorithm X would show results X1, X2, … XN in that order, and algorithm Y would show Y1, Y2, … YN. An interleaved experiment would show some interleaving of those results, for example, X1, Y1, X2, Y2, … with duplicate results removed. One way to measure this would be by comparing the click-through-rate or -probability of the results from the two algorithms.

### Target Population in Inter-user Experiment
- There are different users in the different groups. What’s next?
- Need to decide who you are targeting in your users. For example, there are some easy divisions. What brower, what geo location, country, language etc.
- You may not want to dilute the effect of your experiment across a global population. So if you are analyzing an experiment for the first time, and it only affects English, you may want to actually do your analysis specific on English, and be able to ignore the rest of the population
- Before you launch a big change, you may want to go back and run a global experiment and make sure that you don’t have any unintentional effects on users you weren’t targeting
- Filtering traffic can affect variability of metric as well
 
### Population v.s. Cohort
- Within the population, you can define what’s called a cohort. This means people who enter the experiment at the same time. 
- If you just divert by cookie or user ID and you look at this particular country, you may have all kinds of problems during the span of your experiment where people come who come in classified as that country, either drop out of that experiment or gets reclassified into a different region, so co cohort means that you define an entering class and you only look at users who entered your experiment on both sides around the same time and you go forward from there
- Cohorts are harder to analyze and they are going to take more data because you’ll lose users. So typically, you only want to use them when you are looking for user stability. So say, you have a learning effect or you want to measure something like increased usage of the site, those are cases where you really want to see if your change had a real effect on their behavior relative to their history. Then you need a cohort. If you don’t need those types of metrics, then you can probably stick with the population.
 
### Sizing
- It’s iterative process. Try out some decisions and see what the implications are for size and duration of our experiment and then if we don’t like the results, we go back and iterate
- e.g. page load time, 90th percentile latency: if you want to use ID as diversion metric, you need a lot of data to make that work. So, you know what, I’m really affecting the 90th percentile here, that’s what I’m targeting, so let’s look at people with slow connections. Then, I want to look at cohort of users who’ve used my site fairly regularly over the past two months. In that way, I can get more data about them more quickly. 







 






















