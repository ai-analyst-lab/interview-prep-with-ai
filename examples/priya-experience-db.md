# Example: Priya's experience database (built from the kickoff transcript)

This is what the extraction prompt produces from `priya-kickoff-transcript.md`. Priya and Fernly are fictional.

## Story cards

### 1. The iOS orders drop
- **Situation:** Weekly orders fell about 12% one Monday, right before the quarterly review.
- **What I did:** Broke the drop down by platform, customer type, and region; found it was iOS only; matched it to the previous Thursday's release; traced it to the payment step in the funnel; sent the evidence to the iOS team; set up a checkout-completion alert by platform afterward.
- **Result:** A broken Apple Pay flow was fixed in about 2 days and orders recovered. Lost orders during the incident: `[NEED NUMBER]`. How much faster the new alert catches issues: `[NEED DETAIL]`.
- **Headline:** "I traced a 12% drop in weekly orders to a broken iOS payment step within a day, and the fix brought orders back within a week."
- **Answers questions like:** Tell me about a time a metric dropped. Walk me through how you diagnose a problem. Tell me about an analysis that changed a decision.
- **Likely follow-ups:** How did you rule out a real demand drop? How long did it take you to find it?
- **Undersold:** You called it "kind of a small thing." You caught a revenue-impacting bug before a quarterly review and built the alert that prevents the next one. (suggested)

### 2. Annual plan pricing test
- **Situation:** The growth PM wanted to test a discount on the annual plan to move subscribers off monthly.
- **What I did:** Ran the power calculation (about 3 weeks needed), defined the metrics with the PM, and did the readout, insisting on revenue as a guardrail next to uptake.
- **Result:** Annual plan uptake went from about 9% to 14% of new subscribers. Revenue impact: `[NEED NUMBER]`. Rolled out to everyone.
- **Headline:** "I designed and read out a pricing test that lifted annual plan uptake from 9% to 14%, and made sure we checked revenue before rolling it out." (suggested)
- **Answers questions like:** Tell me about an experiment you ran. How do you choose metrics for a test? Tell me about a trade-off you had to call.
- **Likely follow-ups:** What was the revenue impact? What was the minimum detectable effect?
- **Undersold:** You said "I helped with the experiment." You designed it, sized it, and ran the readout. (suggested)

### 3. Stopping an early call on a test
- **Situation:** A PM wanted to ship a test after 4 days because it looked positive.
- **What I did:** Pushed back and held the test to the full 2 weeks, because Sunday ordering makes weekends behave differently.
- **Result:** The test ended flat, so the team didn't ship a change that did nothing. Engineering time saved: `[NEED DETAIL]`.
- **Headline:** "I stopped us from shipping a false positive by holding a test to its full two weeks, and it came back flat."
- **Answers questions like:** Tell me about a time you pushed back on a stakeholder. How do you handle peeking in A/B tests? Tell me about a disagreement with a PM.
- **Likely follow-ups:** How did the PM react? What would you have done if they'd shipped anyway?

### 4. Retention dashboard
- **Situation:** The retention team needed cohort retention by acquisition channel.
- **What I did:** Built the dashboard: cohort retention curves by acquisition channel.
- **Result:** Used weekly in the retention team meeting. Decisions it has driven: `[NEED DETAIL]`.
- **Headline:** `[NEED DETAIL]` (needs a decision the dashboard changed before it can open an answer)
- **Undersold:** You called it "just a dashboard." It's the retention team's weekly source of truth. (suggested)

## Numbers card
| Number | Context |
|---|---|
| 12% | Weekly orders drop traced to the iOS payment bug |
| 2 days | Time for the iOS hotfix after my analysis |
| 9% to 14% | Annual plan uptake among new subscribers in the pricing test |
| 3 weeks | Test length from my power calculation |
| 4 days vs 2 weeks | When the PM wanted to call the test vs the full run |
| `[NEED NUMBER]` | Revenue impact of the annual plan rollout |
| `[NEED NUMBER]` | Orders lost during the iOS incident |

## Coverage map
| Round | Common question | Status |
|---|---|---|
| Screen | Walk me through your background | Missing (run session 1) |
| Screen | What do you own today? | Thin (the dashboard and alerts hint at it) |
| Case | A metric dropped, walk me through it | **Strong** (story 1) |
| Case | How would you measure success of a launch? | Thin (story 2, needs revenue number) |
| Technical | Design an A/B test and size it | **Strong** (story 2) |
| Technical | What's wrong with peeking at results? | **Strong** (story 3) |
| Behavioral | Tell me about a disagreement with a stakeholder | **Strong** (story 3) |
| Behavioral | Tell me about a mistake you made | Missing (run session 4) |
| Behavioral | Influencing without authority | Thin (story 3) |

## Follow-up questions (most important first)
1. What was the revenue impact of the annual plan rollout, even roughly?
2. About how many orders were lost during the iOS incident, or how much revenue?
3. Name one decision the retention team made because of your dashboard.
4. Tell me about an analysis you got wrong. (session 4)
