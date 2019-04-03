## Lec 2 – Policy and Ethics for Experiments

### Medical: Tuskegee Syphilis Experiment
- 600 rural African American men in Tuskegee (1932-1972) thought they were receiving free healthcare from government but they were, in fact, being cited regarding the natural progression of untreated syphilis. This study continued even after penicillin was established as a standard treatment for syphilis and the men were both not treated and not informed of a possible treatment

### Psychology - Milgram Experiment
- (early 1960s) Yale professor Stanley Milgram measured willingness of studied participants to obey an authority figure who instructed them to administer electric shocks to a third person. That 3rd person was an actor who simply pretended to be shocked with gradually increasing responses and pleas to stop. The question was, how far the participants would would go in causing pain with prompts from an authority figure. 

- In both cases, participants were subject a high risk for permanent harm.

Facebook Experiment
Facebook and Cornell Researchers: Studied how emotions can be spread on social media
Made two random groups see newsfeed with fewer negative/positive posts, then a week later measured whether the posts from the participants are negative or positive
The risk is lower than the previous two experiments but there is no discussion about the potential benefits that might result from such a study.

Institutional Review Boards
Review possible experiments and ensure that participants are adequately protected

4 Core principles to consider
- Risk
The main threshold is whether the risk exceeds that of “minimal risk”. Minimal risk is defined as the probability and magnitude of harm that a participant would encounter in normal daily life. The harm considered encompasses physical, psychological and emotional, social, and economic concerns. If the risk exceeds minimal risk, then informed consent is required. We’ll discuss informed consent further below.

In most, but not all, online experiments, it can certainly be debated as to whether any of the experiments lead to anything beyond minimal risk. What risk is a participant going to be exposed to if we change the ranking of courses on an educational site, or if we change the UI on an online game?

Exceptions would certainly be any websites or applications that are health or financial related. In the Facebook experiment, for example, it can be debated as to whether participants were really being exposed to anything beyond minimal risk: all items shown were going to be in their feed anyway, it’s only a question of whether removing some of the posts led to increased risk.

e.g. 
Search Engine tests change adding price $$ information to result page (Minimal Risk)
Health App lets users know possible consequences of their diets (Potentially more than minimal risk, may be subject to FDA regulation)
Online Encyclopedia tests changing the location of the search bar (Minimal Risk)

- Benefit
In most online A/B testing, the benefits are around improving the product. In other social sciences, it is about understanding the human condition in ways that might help, for example in education and development. In medicine, the risks are often higher but the benefits are often around improved health outcomes.

- Choice: What other choices do participants have
The main issue is that the fewer alternatives that participants have, the more issue that there is around coercion and whether participants really have a choice in whether to participate or not, and how that balances against the risks and benefits.

For example, in medical clinical trials testing out new drugs for cancer, given that the other main choice that most participants face is death, the risk allowable for participants, given informed consent, is quite high.

In online experiments, the issues to consider are what the other alternative services that a user might have, and what the switching costs might be, in terms of time, money, information, etc.

- Privacy

Do participants understand what data is being collected about them?
What harm would befall them should that data be made public?
Would they expect that data to be considered private and confidential?
For example, if participants are being observed in a public setting (e.g., a football stadium), there is really no expectation of privacy. If the study is on existing public data, then there is also no expectation of further confidentiality.

If, however, new data is being gathered, then the questions come down to:

What data is being gathered? How sensitive is it? Does it include financial and health data?
Can the data being gathered be tied to the individual, i.e., is it considered personally identifiable?
How is the data being handled, with what security? What level of confidentiality can participants expect?
What harm would befall the individual should the data become public, where the harm would encompass health, psychological / emotional, social, and financial concerns?

Three main issues with data collection with regards to experiments:

- For new data being collected and stored, how sensitive is the data and what are the internal safeguards for handling that data? E.g., what access controls are there, how are breaches to that security caught and managed, etc.? 
- What is the re-identification risk of individuals from the data?
- Then, for that data, how will it be used and how will participants’ data be protected? How are participants guaranteed that their data, which was collected for use in the study, will not be used for some other purpose? - This becomes more important as the sensitivity of the data increases.
- Finally, what data may be published more broadly, and does that introduce any additional risk to the participants?

Differences in Identified, Anonymous and Anonymized Data
Identified data means that data is stored and collected with personally identifiable information. This can be names, IDs such as a social security number or driver’s license ID, phone numbers, etc. HIPAA is a common standard, and that standard has 18 identifiers (see the Safe Harbor method) that it considers personally identifiable. Device id, such as a smartphone’s device id, are considered personally identifiable in many instances.

Anonymous data means that data is stored and collected without any personally identifiable information. This data can be considered pseudonymous if it is stored with a randomly generated id such as a cookie that gets assigned on some event, such as the first time that a user goes to an app or website and does not have such an id stored.

In most cases, anonymous data still has time-stamps -- which is one of the HIPAA 18 identifiers. Why? Well, we need to distinguish between anonymous data and anonymized data. 

Anonymized data is identified or anonymous data that has been looked at and guaranteed in some way that the re-identification risk is low to non-existent, i.e., that given the data, it would be hard to impossible for someone to be able to figure out which individual this data refers to. Often times, this guarantee is done statistically, and looks at how many individuals would fall into every possible bucket (i.e., combination of values).

e.g. Assessing Data Sensitivity
- Existing census data with race, age, and gender by zipcode (X, too granular for re-identification)
- Number of users visiting specific sites each day (X, not sensitive cuz can’t identify individuals)
- User entered glucose levels with timestamp and anonymous id (O, Timestamps could identify, May be subject to additional Regulation such as HIPAA for Health data)
- Achievements, skills and level advances in an online game by anonymous id (X, Game data not sensitive)
- Number of purchases and total money spent by zipcode (X, Too granular for re-identification)
- Credit card information (O, Very sensitive!)

Questions and Consent
- Are users informed about the data gathering in some form? (e.g. terms and services, privacy policy)
- What user identifiers are tied to the data being gathered? Especially if there is personally identifiable info such as name, e-mail, phone number, address etc. then data becomes more sensitive
- What type of data being collected (e.g. health, financial etc.)
- What level of confidentiality and security is the data subject to? Can anyone in the company have access the data?

What about informed consent?  Participants are told about the risk, benefit, other options they have, what data is being gathered, and how that data is being handled

Arguably, a neutral third party outside of the company should be making these calls rather than someone with a vested interest in the outcome. One growing risk in online studies is that of bias and the potential for discrimination, such as differential pricing and whether that is discriminatory to a particular population for example.

- Are participants facing more than minimal risk?
- Do participants understand what data is being gathered?
- Is that data identifiable?
- How is the data handled?

e.g. Would you seek further review, or possibly obtain user consent?
- Survey about net worth on financial news site. Test survey at bottom of article v.s. after first page, not allowing user to advance until they complete the survey (X, depends on what information is being gathered such as names but usually not that sensitive)
- Different menu output for meal delivery company (X, no new sensitive data is being collected and risk is minimal)
- Test different ways of presenting user heartrate data (O, should get additional review)

Provided Information
Which information is ethically necessary to provide to users?

- A Terms of Service (TOS) or a Private Policy (O)
- History of Funding (X)
- Navigation bar (X)
- List of Experiments you are planning on running (X): might skew the results
- Search Bar (X)

Internal Training
Which information is it ethically necessary for anyone who runs A/B tests to know?

- Which questions to consider when evaluating ethics (O)
- History of A/B testing (X)
- History of IRBs (X)
- Data Policy detailing acceptable data uses (O)
- Principles to uphold (X)



















