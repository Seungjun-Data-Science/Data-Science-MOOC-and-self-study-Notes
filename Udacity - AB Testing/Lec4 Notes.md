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

Size Example
- Situation: Udacity Promotions for coaching next to videos
- Experiment: change wording of message
- Metric: Click through rate = # clicks / # pageviews
- Unit of diversion: page view or cookie
- Analytic variability won’t change, but probably under-estimate for cookie diversion
- Empirical estimate with 5000 pageviews
* By pageview: 0.00515
* By cookie: 0.0119
Quite a difference but how will it actually affect the size of the experiment?
To calculate size, assume SE ~ 1/sqrt(N)
 
dmin= 0.02
Diverting by page view: 2600
By cookie: 13,900

### How to reduce size of an experiment
- Experiment: change the order of courses on course list
- Metric: Click through rate (total # user clicks on any course / # of pageviews)
- Unit of diversion: cookie
Alpha = 0.05; beta = 0.2; dmin = 0.01; SE=0.0628 for 1000 pageviews (empirically)
- Result: Need 300,000 pageviews per group

Udacity isn’t willing to spend that long getting results on just one experiment, especially if it means they can’t run any other experiments in the meantime. Which strategies could reduce the number of page views?
- Change unit of diversion to page view: Yes! Because it makes unit of diversion same as unit of analysis but will less consistent experience be okay? If SE changes to 0.0209 for the sample size, then only 34,000 page views per group would be necessary.
- Targeting experiment to specific traffic: Yes! Because non-English traffic will dilute the results. Filtering traffic can also impact choice of practical significance boundary (since you are only looking at a subset of your traffic, you might need a bigger change before it matters to the business or since variability is probably lower, you might want to detect smaller changes rather than decreasing the size of the experiment). If SE changes to 0.0188, dmin to 0.015, then only need 12,000 page views per group
- Change metric to cookie-based click through probability: Nope! Especially if you are using a short time window for the probability. If there is a difference, the probability will probably go down since the unit of analysis would be the same as the unit of diversion in this case. 

### Size Triggering
- If you don’t know what fraction of your population is going to be affected, you are going to have to be pretty conservative when you plan how much time and how many users have to see your experiment. 
- Now that said, either run a pilot where you turn on the experiment for a little while and see who’s affected or even just use the first day or week of the data to try to get a better guess

### Duration v.s. Exposure
- What’s the duration of the experiment that I want to run?
- When do I want to run the experiment? (e.g. holidays?)
- What fraction of your traffic you are going to through the experiment
e.g. unit of diversion: cookie; on any given day, what proportion of the cookies are you sending to your experiment and your control? Let’s say we need 1 million cookies in our experiment and our control combined. Now, if you only get a 100,000 cookies visiting your site on any given day, that means that if you want to run 50% of your traffic through the experiment and 50% through the control, you need to run your experiment control for 10 days. Another choice is to run your experiment at 25% each, say, because you want to run another test, then you’d have to run your experiment for 20 days as opposed to 10. And that’s how the duration of your experiment is related to the proportion of traffic you are sending through that experiment.

### Duration v.s. Exposure: Example
- Size of experiment: 1 million page views
- Average traffic per day: 500,000 page views
- Run experiment for 2 days
- Likely to have weekly variation (e.g. traffic higher on weekdays than weekends)
- Then, you should run on mix of weekend and weekday days and for 3 days
- For risky change, run larger with less traffic

### When to limit exposure: Which experiments are risky enough that Audacity might want to limit the number of users exposed?
- Changes database (O): If this goes wrong, effects could be huge!
- Changes color of “start now” button (X): Low risk (but should still test)
- Allows facebook login (O): If you don’t roll out, how to deal with Facebook logins?
- Changes order of courses on course list (X): Low risk if you’ve run similar experiments

### Learning Effects
- Learning effects is basically when you want to measure user learning or whether a user is adapting to change or not
- Two types of learning effects: change aversion—users see the change and they don’t like anything; novelty effect—oh this is new I want to try everything around
- Key issue with trying to measure a learning effect is time. It takes time for you to just adapt to a change and often times, you don’t have the luxury of taking that much time to make a decision
- Choosing the unit of diversion correctly: If you want to measure user learning, you need a stateful unit of diversion like a cookie or user ID
- A lot of user learning is based on how often they see the change (“dosage”), you probably want to use cohort as opposed to using the entire population. You would choose a cohort in both the experiment and the control based on either how long they’ve been exposed to the change or how many times they’ve seen it
- From duration perspective, it’s going to take some time to see what’s going to be happening
- From risk perspective, you are probably a little uncertain about what the effect is going to be which means it’s a higher risk change
- For both perspectives, you want to run it through a small proportion of your users for a longer period of time

### Pre periods & Post periods
- Before you run your A/B test, you are on a pre-period on the exact same populations but they are receiving the exact same treatment. It’s an A v.s. A test on the same set of users. And what happens in the pre-period is that if you measure any difference between your experiment and your control populations, that’s due to something else: system variability, user variability etc. Pre-period is useful not just when you want to test user learning but sort of across the board so that you know that any difference in your experiment and control is due to the experiment and not due to pre-existing, inherent differences in your population
- Post period: after I run my experiment, I’m going to run another A v.s. A test, and if there is any differences in the experiment and control populations after I run the experiment, then I can attribute those differences to user learning that happened in the experiment period







 






















