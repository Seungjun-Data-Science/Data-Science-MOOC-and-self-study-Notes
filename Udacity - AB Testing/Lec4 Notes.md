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
 

 






















