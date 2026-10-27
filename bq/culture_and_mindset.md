# Culture & Mindset — Practice Questions & Answers

Loop's interview overview describes a 30-minute conversation with cofounder and CTO Shaosu about your motivations, how you operate, and alignment with Loop's values. These are practice questions, not confirmed interview questions.

Past-experience answers use [stories.md](stories.md). Answers labeled **Personalize** are suggested framing, not established facts about your motivations or preferences. Replace anything that isn't true for you. Aim for 45–90 seconds per answer, leaving room for follow-up.

## Motivation and fit

### 1. Tell me about yourself.

> My experience has focused on backend engineering. At NewsBreak, I built the backend for Premium subscriptions and an upload rate limiter. I also worked with two other engineers on an AI assistant to reduce manual on-call work. Earlier, during my TikTok internship, I worked on cleaning up a large hotel-price database without disrupting live traffic. Across those projects, I've dealt with reliability, ambiguous requirements, and the impact technical decisions have on users.

**Personalize the ending:** Add one sentence about what you want next and how this opportunity connects to it.

### 2. Why do you want to join Loop?

**Personalize — possible answer based on the interview overview:**

> What interests me is the combination of a concrete business problem and engineering work where correctness matters. Loop's audit and payment workflows connect software directly to customers' operations. My subscription work gave me experience making sure payment-related events produce the right user outcome, and my on-call assistant project gave me experience applying AI to a real workflow. I'd like to bring those experiences to a new domain and learn from the people who understand it deeply.

**Before using:** Identify which part actually interests you. Add one specific detail from a Loop product explanation or engineering article you've personally reviewed, and explain why it matters to you.

### 3. Why are you looking for a new role?

**Personalize — your actual reason is not recorded in your stories:**

> I've gained experience in [what your current or previous role taught you]. For my next role, I'm looking for [your real next step: broader ownership, a different problem space, closer customer interaction, or another goal]. Loop interests me because [specific connection to that goal].

**Key point:** State the actual reason clearly and respectfully. Be ready to explain why that opportunity matters now.

### 4. Why a startup? What challenges do you expect?

**Personalize:**

> I'd like the opportunity to own work from understanding the problem through delivery and feedback. I'd also expect changing priorities, incomplete information, and work outside a narrow job description. My on-call assistant project is an example of taking initiative on a team problem, though I know that doesn't capture every part of startup life. I'd want to understand how the team sets priorities so I can put that initiative toward the most useful work.

**Likely follow-up:** What tradeoffs are you willing to accept? Answer honestly about your preferences rather than promising unlimited availability.

### 5. What motivates you as an engineer?

**Personalize — an example you can use if it reflects your motivation:**

> I enjoy solving a problem where I can connect the technical work to a visible improvement for someone. With Premium subscriptions, that meant ensuring users kept the access they paid for. With the on-call assistant, it meant helping engineers investigate incidents with less manual work. I find it rewarding when I understand the problem, make a sound technical decision, and see the result being useful.

### 6. What are you looking for in your next team?

**Personalize:**

> I'm looking for clear goals, room to take ownership, and teammates who share context and challenge ideas constructively. I value being able to ask questions early and get feedback before an assumption becomes an expensive mistake. I'd also like to understand how my work affects customers, so I can make better decisions about scope and reliability.

## Ownership, learning, and judgment

### 7. Tell me about a time you acted without being asked.

> During on-call shifts, engineers had to manually search logs, find troubleshooting guides, and run commands. Improving that workflow wasn't part of my assigned work, but it was a recurring problem. I worked with two other engineers to build an AI on-call assistant, designing its architecture and connecting its tools. We delivered an MVP in one month, and around 20 engineers used it. We also limited automatic actions to documented procedures and required approval for update and delete commands. For me, ownership meant identifying a useful improvement and following through to something people could use.

**Likely follow-ups:** How did you choose the scope? What did you personally build? How did you balance assigned work? Your source story records about an extra hour a day; don't invent a formal reprioritization agreement.

### 8. Tell me about a mistake you made.

> In the Premium subscription system, I initially used our server's processing time to decide whether an update was newer. That was the wrong assumption: a delayed notification could arrive later and overwrite a more recent state. I traced the logs, switched to the notification's original event time, and tested delayed and reordered messages. I also checked affected subscriptions against Apple's records and repaired their local states. It taught me to question assumptions about external systems and test failure cases that could affect customers' access.

**Likely follow-up:** Who did you inform, and when? Prepare the actual communication details; they aren't in the source story.

### 9. Tell me about a time you disagreed with someone.

> While building our upload rate limiter, another engineer felt we could enable it directly because it enforced the rules correctly. I wanted to observe its decisions first. His reasoning made sense from an implementation perspective, but I was concerned about whether the rules represented real abuse. I brought examples of legitimate users sharing an IP and internal scripts exceeding thresholds. We agreed to test without blocking requests and tune the rules before enforcement. I learned to understand the other person's reasoning and use evidence to build agreement around the shared goal.

**Value connection:** Assume positive intent.

**Preparation note:** Your Amazon notes describe a different rate-limiter rollout. This draft follows `stories.md`; confirm the sequence before using it.

### 10. Tell me about a time you handled ambiguity.

> At TikTok, I was asked to clean up a collection of 2.5 billion hotel-room price records. I needed to establish what counted as expired and how to remove it without disrupting live traffic. I clarified that expiration depended on the date the price applied to, then used a dry run to estimate the scope. A large deletion timed out, so I moved to small, adjustable batches and added daily cleanup. We removed 1.5 billion records, and backend timeouts fell from 2% to 0.1%. Breaking the uncertainty into smaller questions helped me make progress safely.

**Likely follow-up:** Who helped define expiration? Prepare the real person or role; don't invent domain-expert involvement.

### 11. How do you balance speed and quality?

> I try to identify which risks would hurt users and where we can reduce scope. During our API migration, we had a Q2 deadline and needed to preserve compatibility with existing apps. I prioritized the core APIs, automated response comparisons, and rolled out endpoints gradually. We completed over 40 endpoints on schedule without client-breaking field regressions. Lower-priority APIs stayed tracked for later. That experience showed me how reducing scope and improving validation can help us deliver sooner while keeping the important guarantees.

### 12. What would you simplify in something you built?

> In the subscription system, we used Redis to serialize updates and track duplicate notifications, along with a database version check. If I revisited it, I'd evaluate keeping the subscription state and duplicate-tracking information in one atomic database update. That could reduce coordination across systems. The tradeoff is that we'd handle conflicting updates through retries, so I'd validate the correctness and operational behavior before changing it. It's a possible redesign, not a change I've already shipped.

**Value connection:** From complexity, find simplicity.

**Likely follow-up:** Why didn't you start there? Explain your actual original reasoning; don't invent deadline or team constraints.

### 13. What is an area you're working to improve?

**Personalize — a possible answer grounded in the subscription mistake:**

> One area I'm working on is identifying hidden assumptions earlier, especially in integrations. In my subscription work, I initially treated arrival time as if it represented the order events happened. After finding the issue, I corrected it and added delayed and reordered notification tests. I want to make that questioning more systematic at the design stage: what assumptions am I making, how could they fail, and which failures would affect users?

**Key point:** Use this only if it reflects your current development area. Be ready with evidence of improvement beyond the original fix.

### 14. Tell me about difficult feedback you received.

**Personalize — no specific feedback event is recorded in your stories:**

> In [real situation], [person or role] told me that [specific feedback]. My initial reaction was [honest reaction]. I asked for an example so I understood the concern, then changed [specific behavior]. In [later situation], [observable result] showed the change was helping. I learned [what changed in your thinking].

**Key point:** Prepare a real feedback example. A mistake you found yourself doesn't answer who gave you feedback or how you responded to it.

### 15. What does “grow together” mean to you?

**Personalize:**

> To me, it means improving my own work while helping the people around me become more effective. The on-call assistant was one example: I worked with two engineers on a tool that around 20 engineers used. I'd also want to contribute through sharing context and asking for feedback. The important part is that learning and useful knowledge spread beyond one person.

**Likely follow-up:** Tell me about helping a particular teammate grow. Prepare a real example; tool adoption alone doesn't establish mentoring experience.

## Working at Loop

### 16. How would you learn the supply-chain domain?

> I'd start with a real customer workflow and ask a domain expert to walk me through it, including exceptions and costly mistakes. I'd summarize my understanding and validate it with them before turning it into software rules. Then I'd take on a focused task that lets me connect the terminology to actual data and user behavior. I'd expect to keep learning from support cases and customer feedback as I build.

**Value connection:** Respect the domain and accelerate progress.

### 17. How do you decide where AI is useful?

> I'd start with the task, the cost of a wrong answer, and how we can evaluate the result. In our on-call assistant, AI helped retrieve information and investigate issues, while automatic execution was limited to documented procedures. Updates and deletes required approval. For a new workflow, I'd compare an AI approach with simpler options and measure whether it improves the outcome. I'd want clear boundaries around actions where a mistake would be expensive.

**Likely follow-up:** What didn't work well in your assistant? Prepare an actual limitation or failure; the source story doesn't document one.

### 18. What would you do if you disagreed with me or another leader?

> I'd first make sure I understood the goal and context behind the decision. Then I'd explain my concern, the supporting evidence, and an alternative. If uncertainty is the main issue, I'd suggest a small experiment. Once the decision owner makes a choice, I'd support execution and watch the risks we identified. I'd bring it up again if new evidence materially changed the situation.

### 19. What would success in your first few months look like?

**Personalize:**

> I'd want to understand the customer workflow and the team's priorities, deliver a useful piece of work, and become someone teammates can rely on. I'd agree with my manager on what that means for the role rather than assume a fixed project before joining. I'd also want to be able to explain why my work matters and what evidence shows it's working.

## Questions to ask Shaosu

Pick two or three based on what you most want to learn:

- What distinguishes engineers who thrive at Loop?
- Can you share a recent decision where one of Loop's values changed the outcome?
- What engineering challenge would you most want this hire to help solve?
- How do engineers learn from customers and supply-chain domain experts?
- How do you decide where AI adds value and where deterministic software is a better fit?
- What would make you say this hire was successful after six months?

## Preparation priorities

1. Write your true answers to “Why Loop?”, “Why a new role?”, and “What do you want next?”
2. Practice ownership, mistake, disagreement, and ambiguity stories aloud.
3. Add a real feedback example and an example of helping a teammate.
4. Confirm any metrics and conflicting story timelines before using them.
5. Learn the structure of each answer rather than memorizing the wording.
