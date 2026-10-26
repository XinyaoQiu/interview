# Behavioral Stories

## Scope

### Main story 1 — Premium subscription system

I built the backend for our Premium subscription system at NewsBreak. The goal was to offer premium features and make sure subscribers got the access they paid for. I owned the purchase APIs, the subscription state machine, and Apple's notification handler.

I wrote two APIs for the purchase flow. Before payment, a prepare API linked our user account to an app account token. After payment, the app called subscribe API with Apple's signed payload. The backend verified it and granted Premium access. Apple's webhook then handled subscription lifecycle events, including renewals, cancellations, and billing failures.

I built a state machine and stored each user's subscription state in MongoDB. I tracked two separate status: the subscription status and whether the user had Premium access. For example, canceling auto-renewal doesn't immediately remove Premium access because the user has already paid for the current period. And a user in a billing grace period also keeps access, but will lose it if the grace period ends and payment still hasn't recovered.

The hardest part was handling concurrent, out-of-order, and duplicate notifications. For example, a renewal could fail and then recover. If the recovery notification arrived first and the failure notification arrived later, processing the delayed failure notification could incorrectly remove the user's access.

So first I used a Redis lock to serialize processing and a MongoDB version check to prevent concurrency conflict. To handle out-of-order notifications, I stored a timestamp watermark in MongoDB. It's like for the same transaction ID, I rejected notifications with an older event time. When the transaction IDs were different, I called Apple's subscription status API inside the same lock to check which one was current.

For idempotency, I used the notification ID as a Redis key to prevent processing the same notification again.

One mistake I made was initially comparing our server's write time against the record's `updated_time` to decide whether an update was newer. But a delayed notification would get a later timestamp and could overwrite a newer subscription state. I traced the notification logs, switched to notification event time, and tested delayed and reordered notifications. I also checked the affected subscriptions against Apple and repaired their local states.

By the third month after launch, the app had over 2,300 paid subscribers and generated about $190K in annual revenue. We also received positive feedback from users who said they were happy with the Premium experience.

#### Follow-up: If you built it again, what would you change?

I would consider removing the Redis lock and adding the idempotency key into the user status record. I would keep the MongoDB version check we already had.

That would let me save the state, watermark, and idempotency key in one atomic update. If the version check failed, the worker would reread the record and reconsider the notification.

The benefit would be fewer Redis operations and no gap between saving the state and saving the idempotency key. The trade-off would be handling concurrent requests through version conflicts and retries instead of serializing them upfront.

---

### Main story 2 — Anti-abuse middleware

I built a distributed rate limiter for our video upload system. The goal was to reduce abusive uploads without disrupting legitimate creators. The challenge was keeping limits consistent across Server instances while supporting different policies for users, IP addresses, and Premium users.

I used Redis Cluster to share rate-limit state across the Server instances. For the sliding-window algorithm, I used Redis sorted sets to store request events ordered by timestamp. The base policy allowed 40 upload requests per user within a rolling 24-hour window. When evaluating a request, the limiter removed entries outside the window and checked the remaining count to determine whether the user had reached the limit.

I chose a sliding-window log because we needed to enforce an exact upload quota over any rolling 24-hour period. I accepted the additional memory cost of storing individual request timestamps to get that precision.

I used Apollo to control configurable rules, like premium users, ip, api key, etc. And High frequency wasn't always abuse: legitimate users could batch-upload, share an IP, or retry on poor connections. I ran the limiter in shadow mode, which means it logs decisions without blocking requests, and I checked downstream signals to tune the rules until the false-positive rate was low.

After enabling enforcement, clients exceeding their quota received HTTP 429 with `Retry-After`. Some malicious clients were added into a blacklist after review and received 429 without that header. I also chose a fail-open policy. If the limiter’s Redis dependency was unavailable, requests could continue through the upload pipeline.

Finally, the rate limiter could support 1.5M daily requests, and blocked 14.8% of malicious traffic. The false-positive rate was as low as 0.14%. The overall upload completion increased by 22.3%.


## Ownership

### Tell me a project that out of your scope
During on-call shifts, engineers had to manually search logs, find troubleshooting documents, and run commands, sometimes in the middle of the night. Improving this process wasn’t part of my assigned work, but I saw an opportunity to reduce the manual effort. I spent about an extra hour each day on an AI on-call assistant and worked with two other engineers to build it.

I designed the architecture with three agents: a retrieval agent that accessed our existing RAG system, a ReAct conversation agent that engineers could mention in Slack threads, and a DevOps agent that followed troubleshooting guides to execute commands and generate reports. I built an MCP tool layer connecting log search, Prometheus alerts, MySQL operations, and web lookup. Automatic execution was limited to commands documented in our troubleshooting guides, mainly read operations and predefined restarts. Update and delete commands required approval.

The three of us delivered an MVP in one month and continued improving it. Around 20 engineers used it. In one incident, it automatically restarted a server pod affected by an out-of-memory issue, resolving the immediate alert. I then used its report and discussed the evidence with the agent to identify the root cause. This showed how it could help with both immediate recovery and follow-up investigation.

I learned that ownership extends beyond my assigned projects. When I noticed a recurring problem affecting the team, I could take the initiative to address it.

## Ambiguity

### Tell me an ambiguous project
During my TikTok internship, I was asked to clean up a MongoDB collection containing 2.5 billion hotel-room price records from third-party partners. The collection kept growing because expired prices weren’t being removed, and I needed to determine what to delete and how to do it without disrupting live traffic.

I clarified that expiration should depend on the date the room price applied to. A dry run estimated that 60% of records qualified for deletion. My initial approach using deleteMany would time out, so I switched to cursor-based batch deletion. I started with 100 records per batch and a 0.1-second pause, keeping both settings adjustable based on database performance. I also set up daily cleanup to prevent stale data from accumulating again.

We removed 1.5 billion records and reduced backend timeouts from 2% to 0.1%.

I learned that handling an ambiguous project starts with separating what I know from what I’m assuming. I clarify the requirements with the right people, validate assumptions through small experiments, and use the results to guide the next step.

## Perserverance

### Tell me a time that you face a tight deadline
I was migrating our server’s JSON APIs to Protobuf, with a target to deliver a major batch by the end of Q2. Older clients still depended on the existing JSON responses, so we needed to preserve compatibility despite differences such as Protobuf dropping zero-value fields.

I prioritized core APIs—including feed, content, user, and social—and tracked lower-priority APIs as follow-up work. To speed up validation, I built automated comparisons between the legacy and Protobuf paths in a sandbox environment, using a control group to distinguish normal feed variation from actual regressions. I prioritized compatibility-breaking differences and rolled out each endpoint gradually behind a gate.

I completed the prioritized batch of over 40 endpoints on schedule, with around 120 PRs merged. Replay tests parsed without errors, and the rollout caused no client-breaking field regressions. Lower-priority APIs remained tracked for later migration.

I learned to handle tight deadlines by defining what must be delivered first and finding ways to make essential checks more efficient. Prioritizing scope and automating validation helped me meet the deadline and still maintain compatibility.

## Conflict Resolution
While building our upload rate limiter, I wanted to run it in shadow mode first to check whether the rules would block legitimate traffic. Another engineer disagreed. He argued that the limiter was deterministic: any client exceeding the configured limit should be blocked.

I investigated the traffic, calculated the false-positive rate, and brought concrete examples to our discussion. Multiple legitimate users could share an IP, and internal scripts could also exceed the thresholds. I explained that the limiter could enforce a rule correctly while the rule still misclassified legitimate activity. I proposed logging decisions without blocking requests, then tuning the rules based on those observations. He agreed that shadow testing would help validate the policies before enforcement.

We agreed to start in shadow mode and enable blocking after validating and reducing false positives. This let us address legitimate traffic patterns before enforcing the rules.

I learned to resolve technical disagreements by separating implementation correctness from whether the design meets the intended goal, and using concrete evidence to build a shared understanding.