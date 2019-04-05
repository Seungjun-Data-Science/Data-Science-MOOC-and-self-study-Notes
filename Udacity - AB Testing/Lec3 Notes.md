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




