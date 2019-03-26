- A/B Testing is a general methodology used online when you want to test out a new product or a feature. 
- One set (control set), existing product or feature v.s. New experiment (new version)
- How did these users respond differently in order to determine which version of your feature better?

Should you use A/B testing for every change you are considering or are there certain types of changes that work better than others?

- John Lilly (VC of GreyLock and former President of Mozilla)
“A/B Testing is very useful in helping you climb to the peak of your current mountain but if you want to figure out whether you want to be in this mountain or that mountain, A/B testing isn’t that useful””
- Can test a pretty wide variety of things with A/B testing, everything from some new features, additions to your UI, and different look for AI etc. (e.g. Amazon: discovered had significant increase in revenue from personalized recommendations with A/B Testing)
- Can test “less visible change” as well (e.g. ranking change)
Linkedin tested a change where they were trying to figure out whether they should show a news article or an encouragement to basically add new contacts
Google: ranking between search lists and ads
- Can test stuff that users won’t even notice
e.g. Amazon showed in 2007 that for every 100 ms added to the page, they actually had a 1% decrease in revenue
- Isn’t useful for testing out “new experiences”
Change aversion & novelty effect
One question is what is your baseline for comparison? But two is a question about how much time you need so that you can actually say what is going to be the plateaued experience so that I can actually make a robust decision
- Can’t tell if you are missing something
E.g. Digital camera review site: A/B testing can tell you whether or not you should be showing this camera review above this camera review but can’t really tell if you are missing this entire other camera that you should be reviewing but you aren't reviewing at all.

Examples of when you can & can’t use A/B testing
- Online shopping company: Is my website complete? (whether there are products users
want to buy, that they don't have)
Can’t figure out whether you are carrying all the products users need by running a A/B test
Could try carrying a specific additional product, but if users don't buy it, you still won't know if there's
a different product you're missing. Instead, you might want to try asking users whether there's anything they feel is missing.

- Freemium business model: they want to provide a premium service that offers additional functionality. (To access the premium service, users would need to upgrade, create a log in, and explore the new functionality.)
Wouldn't be able to fully test whether the premium service is a good business decision using A/B testing. Users have to opt into a premium service, so randomly assigning people to one group or another wouldn't really work and you would not have a control group to compare against.
But still valuable information: you could see how many users will read about the additional features or how many will choose to upgrade if you make the choice available.

- Netflix: They create a new algorithm to rank the possible recommendations.
    ** Great use case of A/B testing because there are clear control and experiment groups, the old algorithm and the new algorithm. Also, have clear metrics (e.g. the probability of a user clicking on a recommendation or actually watching the movie)

- Website selling cars: want to if some change will make customers more likely to return or refer their friends
Won’t be able to use A/B testing because it would take too long to see if you get repeat customers (since people buy cars rarely) and you won’t necessarily even have data about whether customers are recommending 

- Company wants to update their brand, including the main logo for their site
 The second case seems like it would be easy to A/B test, and you certainly could collect data about
user behavior with the new and old logo. But they might need some time to get used to
the new logo, so you wouldn't want to make a decision based on a short time window of data collected in an A/B test.

- Suppose you want to test some changes to the initial page of your mobile application. Want to change things like what information is included, what wording you use and what colors you use
Good case for A/B testing. Possible metric can be probability that the user progresses past the initial page.

History of A/B Testing
- A/B testing was around for a long time (maybe not necessarily called A/B testing)
e.g. Agriculture: people would actually divide up their land into sections and then test what would work better for a particular crop or how it grew.
- Medicine: A/B testing is called “clinical trials” and that’s how they determine whether a new drug is effective or not
- Having consistent response from your control and your experiment group is important
- Difference between normal experiments and online A/B test
    ** Online world has a lot of more data but lower resolution
    ** Normal experiment has way less participants and it’s more personal while online A/B testing may have millions of users, thousands of clicks etc and may have trouble distinguishing whether this is a single person, whether there’s multiple people. Is it an internet café computer? 

Business Case Example
Company focused on providing free finance courses: trying to test features that increase student engagement.
Consider change to “Start Now button”: change color from orange to pink  Will this increase how many students explore Audacity's courses?

Potential metrics
- Total number of courses completed: it can take students weeks or months to finish courses, so this metric would simply take too much time to be practical
- Number of Clicks
  ** Click through rate: number of clicks / number of page views
  ** Click through probability: Unique visitors who click / unique visitors to page

Click through rate v.s. Click through probability
If you want to measure the usability of a particular button, you use a rate because the users have a variety of different places on the page that they can actually choose to click on. And so the rate will say how often do they actually find that button.

Now, if you just want to know how often users went to the second level page on your site, you use a probability, because you don't want to count if users just double-clicked, or did they reload, or all of those types of issues. If you are interested in whether users are progressing to the second level of the funnel, probability will be a better choice for metric.

E.g. 1,000 unique users visit the Audacity homepage and 100 of those visitors clicked the start now button at least once. Then, click through probability = 10/ 100 = 10%

Binomial Distribution
As you increase n, the binomial distribution starts to look more and more like a normal distribution 
- Mean = p
- std = sqrt[p(1-p) / N]

Assumptions
- There have to be exactly two types of outcomes (e.g. success, failure)
- Events have to be independent
- Events need to follow an identical distribution. That is, p needs to be the same for all of them.

E.g. In which cases can we use a binomial distribution?
- Drawing 20 cards from a shuffled deck (X): p becomes different as we draw more cards
- Roll a die 50 times (O)
- Clicks on a search results page (X): Not independent cuz if user doesn’t find results they want, they will use different key words and so forth
- Student completion of course after 2 months (O): overall reasonable unless one user makes two accounts and they are correlated and there is no way to distinguish them etc.
- Purchase of items within a week (X): One customer can buy bunch of items and they can be all correlated

Confidence Interval
- To be able to use the normal distribution of confidence intervals, N x p^ > 5 & N(1-p^) > 5
- Margin of error = Z * SE = Z * sqrt[p^ (1-p^) / N]

Hypothesis Testing
- Null Hypothesis(H0): Pcont = Pexp
- Alternative Hypothesis(HA): Pexp – Pcont =! 0 
- Calculate P(P^exp – P^cont | H0): Reject null if this probability is < 0.05 (or some significance alpha level)

Pooled Standard Error
- If you have two samples, we need standard error that gives a good comparison of both. In this case, we can use “pooled error”.
- Number of users in each group: Xcont, Xexp 
- Total number of users in each group: Ncont, Nexp
- P^pool = Xcont + Xexp / Ncont + Nexp
- SEpool = sqrt[^Ppool * (1-^Ppool)*(1/Ncont + 1/Nexp)]
- ^d = ^Pexp - ^Pcont
- H0: d = 0, ^d ~ N(0, SEpool)
- If ^d > 1.96 * SEpool or ^d < -1.96 * SEpool, reject null

Size v.s. Power Trade-Off
- Main question is how many page views we need to get a statistically significant result. This is called “statistical power”
- Power has an inverse trade-off with size. The smaller the change you want to detect, you have to run an experience with larger sample size
- Alpha = P(reject null | null true) = Percent of the time a difference will be detected, assuming one does not exist
- Beta = P(fail to reject | null false)
  ** Small sample: alpha low, beta high
  ** Larger sample: alpha same, beta lower
- 1 – beta = sensitivity (often 80%) = percent of time the minimum effect size will be detected, assuming it exists

How do the following changes affect page views?
- Higher click through probability in control (but still less than 0.5): This will increase SE which means we need to increase N(page views) to in order to reduce the SE back to its original level
- Increased practical significance level (dmin): Decrease page views because larger changes are easier to detect, so doesn’t need as many page views
- Increased confidence level (1 – alpha): saying that you want to be more certain that a change has occurred before you reject the null. In essence, you are being more conservative. You could accomplish that by rejecting the null less often, but then your sensitivity goes down. If you want to keep sensitivity the same, you’ll need to increase the page views you collect.
- Higher Sensitivity (1-beta): If you want to increase sensitivity, need to collect more page views to narrow the distribution

Different Confidence Interval Cases – How to deal with uncertainty
 

Cases in bold are tricky cases

- 1st case: Launch for sure
- 2nd case: called “Neutral” No statistically significant change from 0 since the CI includes 0 and you are also confident there’s not a practically significant change. Given this, it’s not worth the effort to launch the change
- 3rd case: You are statistically confident that there was a positive change but it’s not practically significant change. Thus, not worth launching.
- 4th case: You do not have enough power to draw a strong conclusion. Running additional test with stronger power is recommended
- 5th case: The point estimate is beyond what is practically significant but CI overlaps 0, so repeating this test with greater power would give additional confidence to the results
- 6th case: Your best guess is again that there is a practically significant positive change, however it’s also possible your change is not practically significant, and thus should run additional tests
























