# Lec 3 – Choosing and Characterizing Metrics

First, think about what you are going to use the metrics for before deciding how you are going to define them

2 Use Cases
- Invariant checking: metrics that shouldn’t change across experiment and control

e.g. same number of users? Same distribution? Comparable numbers of users across countries, by language and so on. All of these sanity checks to make sure the experiment runs properly

- Evaluation
** High level Business metrics: revenue, market share, number of users
** More Detailed Metrics: User experience with product, how long they stay on the page

Other realistic considerations
- User Experience Research
- You may not have information you need, time is too short to measure what you want etc. Whether students get more jobs after taking the class or something more nebulous like do they have improve skills. Now the problem is it may take six months or even more to see if the students who took the online course will get jobs or not.

[1] Come up with a High level concept for a metric: One sentence summary (e.g. click through probability, active users etc)
[2]Figuring out details  How do you define active user (e.g. 7 day, 28 days?)
[3] Summary to a single metric (sum, mean, median etc.)

If you have multiple metrics: Composite metric
- Objective function
- OEC (Overall Evaluation Criterion): What Microsoft came up with. Weighted function that combines all of these different metrics

BUT using multiple metrics:
- Hard to define
- Possibility of Over-optimizing one perspective and disregard other perspectives
- Have to consider how generally applicable the metric is  It is better to use a metric that is less optimal for the test if you can use it across suites of AB tests you can do the comparison than it is to come up with the perfect metric for your test

### High Level Concept for metrics
Business Objective
- Helping students get a job
- Financial Sustainability 

### Funnel
Homepage visits  Exploring the site  Create Account  Complete

### Expanding the Funnel
- Homepage visits 
- Exploring the site  Number of users who view course list / Number of users who view course details
- Create an account  Number of users who enroll in a course / Number of users who finish Lesson 1, Lesson 2 etc. / Number of users who sign up for coaching at various levels
- Completing a course  Number of students who enroll in a second class / Number of users who get jobs after taking the course

### Expanded Funnel
Homepage visits
Course list visits
Visits to course page
Accounts created
Enrollment
Coaching Use
Completion
Jobs

- The funnel might be different across different platforms (e.g. android, ios, tablet PC, desktop etc)
- Each stage can be a metric (e.g. # of users who reach that point  Count)
- Don’t have to use Count for all funnels. For other points in the funnel, can switch to “rate” which can be acquired by dividing the number of users at that level of the funnel by the number at the previous level 
- Might want to see “rate” or “probability” because key interest here can be “rate of progression”

### Choosing Metrics
Potential Metrics are:
- Click through rate on start now button
- Click through probability on start now button
- Probability of progressing from course list to course page
- Probability of progressing from course page to enrolling
- Probability that enrolled student pays for coaching

- Experiment 1: Update a description of the course list page  Probability of progressing from course list to course page (nice to track continued progression down the funnel)
- Experiment 2: Increase size of “Start Now Button”  Click through rate on start now button (rates are usually better for usability test)
- Experiment 3: Explain benefits of paid service  Probability that enrolled student pays for coaching (good idea to think about retention rates and usage rate of how many/proportion of students actually started to use that service)

### Difficult Metrics
- Some metrics are difficult to measure: Don’t have access to data or simply take too long to collect (e.g. Number of students who get the job after taking online course)
- Rate of returning for 2nd course = # who start course / # who complete first  Has data, but takes too long
- Average happiness of shoppers  Doesn’t have data
- Probability of finding information via search  Doesn’t have data

### Other Techniques to Use
- Surveys, retrospective analyses, focus groups etc 
 Great for brainstorming, help you think of new metric ideas, good for validating metrics

### Using External Data
[1] Companies that actually collect fairly granular data about market share, how many people are interested in the travel industry and even for specific websites, they may have visitor data that they put together. E.g. ComScore, Nielson

[2] Companies that actually run surveys of users e.g. pew, Forrester  How many different devices do you have, how much time you do spend on each of those devices 

[3] Academic Research: Papers that actually try to establish metrics, may run correlation studies e.g. eye tracking: study where they have a bunch of people in a lab and look at how they read a page and collect how much reading they are doing v.s. how much time do their eyes spend on the page v.s. how long did it take them to actually click-through the next page

### What Can You Do With This External Data?

- First, you can validate simple business metrics if your site or industry appears in one of these lists. For example, if you want to look at total visitors to your site, you can compare your number with the numbers provided by Comscore or Hitwise, or you could compare the fraction of shopping traffic in each “vertical” category to what you see on your site. However, the numbers you see will almost never exactly match your own data. Generally speaking, a better way to do the validation is to look at a time series of both your internally computed metric and the externally available one, and see if the trends and seasonal variability line up.
- Second, you can provide supporting evidence for your business metrics, either direct measurable quantities
(look, this is used by lots of sites) or to get ideas for which measurable metrics make good proxies for other
harder-to-measure quantities.
- Publicly available academic papers, such as the User Experience ones, often establish a general equivalence between different types of metrics. One example that Carrie worked on was a paper with Dan Russell, which compared user reported satisfaction with a search task to the duration of the task as measured on the website. That gave a good general correlation for satisfaction with duration measured, though with some clear caveats. So this study helped validate a metric—duration—that could be computed at scale and then automatically converted to a metric that could not be compute at scale—user reported satisfaction.

### Using Internal Data
- Uses all of our existing data (data capture, existing log etc.)
- If you want to gather new data: When you can’t do analysis with existing data (e.g. User experience research, survey, focus groups)

What you can do with your own external logging data or data capture from your site
- Retrospective/Observational Analysis: Look at how a metric you are interested in or just measurements you take from your site, change in response to changes you’ve made in the past, experiments you’ve run, big spikes in your business. It’s good for getting a baseline and also help you develop theories. Can also use this data in conjunction with other methods such as surveys or UX Research. Issue is that it shows correlation, not necessarily causation cuz you are not running a parallel A v.s. B v.s. C v.s. D experiment, so it’s hard to establish that the change you made actually caused what happened, not some funny temporal effect.
- One method to validate metrics is to “actually run experiment”: want to measure that the metric is gonna move when me make changes
** e.g. If we are using the length of time it takes for a student to complete a quiz as a metric for wether or not that quiz is actually going to be a good measure of students understanding that material, then we have to try a bunch of quizzes and compare all of them, okay, well which ones actually move my proposed metric (sensitivity + robustness)
- Talk to colleagues who worked in research and other companies that use different metrics 
- Think about company’s culture: Some companies don’t want necessarily people developing website to think about how much revenue they are bringing in. They want to see innovative features. Some company might be focused on obtaining market share and adding more users, whereas another company might be interested in making their existing users happier. So, it’s important take into account “corporate culture” when deciding business metrics
- Usually good idea to lay a boundary around your metric

### Gathering additional data
- User Experience Research (UER): good for brainstorming and can use special equipment (e.g. special camera that tracks eye movement) but you have to validate results with something like retrospective studies. With UER, you can go really deep with a few users, either in a lab or even in a field study. This is the most in-depth and intensive, and can be a combination of observing users doing tasks and asking them questions. The idea is to spot problems and draw insights from the observations and timely questions. This can be useful for generating hypotheses for problems that you might want to tackle fixing in experiments. You can also generate possible metrics to track those problems given the behavior you've observed. In another variation of a UER study, often called a diary study, you ask users to self-document their behavior rather than observing them in a lab or in the field. Diary studies can usually get more users, because you don’t need a researcher to be spending time observing each participant, but they have more issues with self-reporting bias. UER studies are in-depth and qualitative, and you'll study maybe tens of users at most. They're great for generating ideas for metrics or for experiments, but you’ll want to validate the results with methods that scale up to many more users.
- Focus Groups: More participants than UER but less depth. Can get feedback on hypotheticals but has the risk of group think (minority opinion crushed by mainstream). In focus grous, you recruit a bunch of users or potential users and bring them together for a group discussion. Once you bring the users together, you could show them screenshots or images, or you can walk them through a demo, and then you can ask them questions to elicit feedback. You can talk to more users than in a UER study, maybe hundreds of users, and you can often ask hypothetical questions, but even if you have a skilled facilitator, you run the risk of group-think and convergence on fewer opinions. Haven’t you been in a room and there’s been a few loud voices that dominate? That same dynamic can occur in focus groups.
- Surveys: Useful for metrics you cannot directly measure but can’t directly compare to other results. The final method is to run surveys or questionnaires, where you recruit a population and ask them to answer a bunch of questions. The number of questions can vary, as can the type of question. You can have multiple-choice answers, or open-ended questions where users give a free-form response. These can be done online, either on your site or other methods of reaching and targeting users, such as Google’s Consumer Surveys. The main advantage of surveys is that you can typically reach thousands of users, if not more. The disadvantages are that the data is self-reported and users don’t always give full or truthful answers, even if the survey is anonymous. When running a survey, you'll need to take care in how you recruit your population to ensure that it’s representative, and you'll need to word the questions carefully since the wording may prime the participants to give specific answers. Surveys are useful as a way to get data for metrics that you cannot get from your system, but they’re not really comparable to the metrics that you will obtain from your own logs and data capture. For example, the populations may not be comparable since you may be reaching a biased population with your survey relative to the population using your website or app.

### Applying other techniques
- Homepage visit: Compare to external data
- Completion rate: compare to external data  UER to investigate low completion  Validate this with retrospective analysis or experiments
- Number of students who get Jobs: surveys e.g. did class help in interview? (but issue is that populations are not comparable)
- Rate of returning for 2nd course: survey  proxy
- Average happiness of shoppers: survey, UER
- Probability of finding information via search: length of time spent on search page, whether the user clicked on any results that were shown or whether there were any follow up queries trying to get at the right information in a different way. External data + UER. Human evaluation (pay human evaluators to evaluate your site)

Examples
- Measure user engagement: Course completion too long-term  Use survey, UER, retrospective analysis
- Decide whether to extend inventory: Focus Group, external data
- Which ads get most views: External data, UER, retrospective analysis

### Issues you face when you actually compute metrics
- First step: define exactly what data we are going to look at (e.g. which events do I count as my numerator and denominator, am I going to remove robots or spams)
- Second step: how do I summarize metric (e.g. median? Mean?)

e.g. Click Through Probability 
- Count total number of clicks & total number of page views and just divide
- Nuanced version: Did a cookie (anonymous identifier of user) visit the site and then given that a cookie visited, did it click or not
- rate v.s. probability: Also impact the actual implementation of metric as well as things like variability

### Defining a metric
High level metric: Click through probability = # users who click / # users who visit
- Def #1: For each minute (hour/day), # cookies that click / # cookies
 
- Def #2: # of pageviews with click within time interval / # of pageviews
	** If user refreshes within time interval, def#1 and def#2 will yield different values
 
- Def #3: # of clicks / # of page views (click through rate)

Check mark: will still yield the same results (won’t be affected by the event)
 
- First case (Double click): Only rate will change because the number of clicks change while the prob remains the same
 

- Second case (back button caches page): Denominator will be different, so back button that caches pages will impact the denominator, and thus the page view prob and rate
 

- Third case (click tracking bug): all three metrics use clicks in some way or the another in the calculation, so this bug will affect all three metrics (pic below: click 1 v.s. 0)
 

### Filtering and Segmenting
- Abuse in your site (spam, fraud etc): If you have a competitor, for example, looking for your site clicking on everything that’s data you may not want to use in the experiment
- What happens if your change only impacts a subset of your traffic?  only impacts English traffic / only impacts mobile version but not the web version
- Ultimate purpose of filtering is to “De-bias” data
- Especially long weird sessions of user behavior: First need to check that it’s not actually your website, your metric or even your logging that’s causing these sessions to come up
- How do you decide whether to use a filter?
** Slice data, compute metrics on disjoint sets e.g. by country, language, platform… compute metrics on these different slices and see if you are removing traffic disproportionately from one of these places or not. Now if it is, it may an indication that you are actually biasing your results further.
- Looking at week over week or day over day traffic pattern changes is a good way to spot something looks at least a little unusual
- Segmenting: Good for evaluating definitions and building intuition

Week over week: Divide # of cookies at a certain point by # of cookies at the same day a week earlier
 
The “weekend spikes” disappear in week-over-week plot which means it was due to weekly variation but that weird huge spike is still there which means it’s not due to weekly variation, so it needs further inspection

We look “cookies by country” and we observe that spike was due to one country that had abnormality
 
### Summary Metrics
- We want to summarize all of these individual events into a single summary metric
- In some cases, summary metrics are obvious. E.g. If you are counting how many cookies are visiting the homepage, it’s a count or a sum or just the total count. Can also summarize further into something like the average number of visitors per week. For rate or probability, it’s actually calculating an average over the clicks per page view for every single individual event.
- In all of these cases, summarization is actually part of the metric definition
- Cases where you actually have a choice of summary metric: Per event measurement is itself a number e.g. load time of video, how many terms are in a query, what the position of the first click of a page is  can choose from mean, median, 25th percentile etc
- First establish few characteristics for the metric: sensitivity (sensitive enough to be able to detect a change when you are testing possible feature options) and robustness + characterize what the distribution of metric looks like (doing retrospective analysis e.g. histogram x axis different values for metric, y axis frequency)

### Common distributions in online data

For example, let’s measure the rate at which users click on a result on our search page, analogously, we could measure the average stay time on the results page before traveling to a result. In this case, you’d probably see what we call a Poisson distribution, or that the stay times would be exponentially distributed.

Another common distribution of user data is a “power-law,” Zipfian or Pareto distribution. That basically means that the probability of a more extreme value, z, decreases like 1/z (or 1/z^exponent). This distribution also comes up in other rare events such as the frequency of words in a text (the most common word is really common compared to the next word on the list). These types of heavy-tailed distributions are common in internet data.

Finally, you may have data that is a composition of different distributions - latency often has this characteristic because users on fast internet connection form one group and users on dial-up or cell phone networks form another. Even on mobile phones you may have differences between carriers, or newer cell phones vs. older text-based displays. This forms what is called a mixture distribution that can be hard to detect or characterize well.

The key here is not to necessarily come up with a distribution to match if the answer isn’t clear - that can be helpful - but to choose summary statistics that make the most sense for what you do have. If you have a distribution that is lopsided with a very long tail, choosing the mean probably doesn’t work for you very well - and in the case of something like the Pareto, the mean may be infinite!

4 categories of summary metrics
- Sum and counts (e.g. # of users who visited page)
- Distributional metric (mean, 25th percentile etc)  mean age of users who completed a course
- Probability and rate (e.g. probability has 0 or 1 outcome in each case, rate has 0 or more)
- Ratios: useful because they can compute a whole range of different business models but they can be very difficult to characterize (e.g. Pr(revenue generating click) / Pr(any click))

### Sensitivity and Robustness
- Sensitivity of metric: want to choose metric that picks up changes you care about
- Robustness of metric: but that metric should be robust against changes that you don’t care about

e.g. Latency example where we are looking at the load time of a video
- mean is sensitive to outliers (not being robust)
- median tends to be more robust to outliers but if you only affect a fraction of your users, even if it’s a fairly large fraction, like 20% with a change, you might not see the median move at all. So the median is robust but not that sensitive, so want to consider using other metrics like 90th or 99th percentile, and see how those change as well

How do we measure sensitivity and robustness?
- Run simple experiments, say increase the quality of the videos, which in theory increase the load time for users and we could see if the metrics were interested in, actually respond to that
Now the date is going to get a fuzzier so they may not respond exactly the way that we think, but we should be able to tell if they are moving in a way that intuitively makes sense
- A versus A experiment: use this to determine if the metric is too sensitive. You just compare people who saw the same thing to each other. See if metrics pick up any spurious differences between the two and that’s a really critical element to make sure that you are not calling things significant that maybe don’t really mean anything.
- Can look back at experiments that happened before and now you have the hindsight benefit (e.g. user data about how well people liked it and how they responded) and you can see if those experiments move the metric you are interested in.
- Retrospective analysis of logs: look back at changes you know you made to your site and see if the metrics you are interested in actually moved in conjunction with those changes

e.g. choose summary metric for latency of a video
  
90th and 99th percentile not robust enough

Median and 80th percentile not sensitive enough

### Absolute or Relative Difference
- First, have to decide how to compute the comparison. We have value for experiment and value for control but have to decide how we are going to compute the comparison between the experiment and the control.
- Simplest way is to take difference but if you are running lots of experiments, you may want to consider computing the “relative change (percent change)” as opposed to “absolute change”.
- Main advantage of computing the Percent change is that you only have to choose one practical significance boundary to get stability over time  applicable to mainly situations with “seasonality” and your system is changing over time e.g. shopping site: In June, most people are on vacation, not shopping a lot, so you have users and lower click through rate whereas in December, you’ve got higher click through rate and if you have the same practical significance boundary across the same times, you basically have the same comparison.
- Other situation is if you are running a lot of experiments and your system is actually changing over time, your metrics are probably changing over time as well. If you are using relative difference, you can stick with one practical boundary as opposed to having to change it as your system changes. 
- Main disadvantage of relative difference (e.g. ratios) is variability. It is not always as well behaved as absolute differences, so if you are just starting out, it’s often good to start with absolute difference and work your way up.

### Variability
- Want to check that the practical significance level we are interested in is really realistic for our metric. If we have a metric that varies a lot under normal circumstances, that may not really work for us in practice.
- If you are using count or probability, you are only really dealing with the variability of a single measurement or of a constrained one in the case of probability, so you can do confidence intervals theoretically but if you move on to using ratios or percentiles or if your data is lumpy, want to compute variability empirically

Calculating Variability
- To calculate a confidence interval, you need:
	** Variance (or std)
	** Distribution
- Metric, Distributions and estimated variance
  
Cf. Difference between Poisson variables
 
### Nonparametric Methods
- You have a way to analyze the data without making an assumption about what the distribution is
- It can be noisier and computationally expensive but can be very useful
- e.g. Sign Test: Let’s say we ran AB test for 20 days and on 15 of those days, the experiment side had a higher measurement than the control side. We can use binominal distribution just like we learned before but the downside of this is that it doesn’t help you estimate the size of the effect. That is, you can’t say you know I’m confident this is at least 2% change in my metric. The upside is that it is easy to do under a lot of circumstances.

### Empirical Variability
- For more complicated metrics, you might need to estimate the variance empirically instead of computing it analytically
- For complicated metrics, distribution can be very weird and that’s why you want to shift to a empirical estimate. Google found that even for some simple metrics, the analytical estimate of the variance ended up being an underestimate. Thus, shifted to using A versus A experiments across the board to estimate the empirical variability of all the metrics.
- A versus A experiment: control A against another control A, so there’s actually no change in what the users are seeing. That means any differences that you measure are due to the underlying variability, of the system, user population etc. We can use this test for sensitivity and robustness of metric. For example, if you see a lot of variability in a metric in a A v.s. A test, maybe it’s too sensitive to use in evaluating a real experiment.
- There’s a diminishing return as you run more A v.s. A tests. The key rule of thumb is that the standard deviation is going to be proportional to the square root of the number of sample.
- If you don’t have enough traffic and can’t run your experiment, alternatives are: 
** Run one really big A v.s. A experiment
** Bootstrap: take that big sample and randomly divvy it into a bunch of small samples and you do the comparison within those random subsets
- If you bootstrap estimate is agreeing with my analytical estimate, we can probably move on, but if not, you may want to consider running a lot of A versus A tests and really digging into what’s going on
- Use Case of A/A tests
	** Compare results to what you expect (sanity check)
	** Estimate variance and calculate confidence
	** Directly estimate confidence interval
e.g. 20 experiments, each on 0.5% of traffic (50 users in each group)
20 more, each on 1% (100 users per group)
10 more, each on 5% (500 users per group)
How many experiments will show a statistically significant difference at the 95% level?
Out of 20 experiments, we expect to see 1 significant result
 
### Variability Summary & Lessons
- Different metrics have different variability. If a variability is too high, a metric may not be practical for use even when it makes a lot of business or product sense. 
- Need to understand underlying distribution of data (analytical + empirical techniques)
- Trickiness of metric selection and data capture
** Let’s say click through rate. Are we talking about impressions or page views? First page of search results or all the next pages? Us only or globally? Removing spam or not? Just being able to standardize the definition was really important towards just being able to start the conversation to another different level. 
	** In search, we love metric “tasks per user per day”. Now the problem is that it’s a very stable metric. Just about experiment, you aren’t changing the metric. In fact, if you did actually measure a change in task per user per day, it was probably a sign that you screwed up your experiment. It also has definition issues like what time period actually makes the most sense (per day, per week?). 


