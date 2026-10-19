# 自我介绍

Hi, I’m Xinyao. I recently graduated with my Master’s in Computer Science from the University of Illinois. I interned at TikTok, Ablibaba Cloud, Tesla and UMTRI. During my studies and my recent internships, I have focused on building reliable, large-scale backend systems.

I really enjoy solving technical challenges and working with teams to build software that makes an impact. I am excited to bring my skills and my collaborative mindset to the engineering team at Google.

# 主要项目

During my internship at TikTok on the Open Platform team, I worked on two major projects to improve how we manage travel data from partners like Booking.com.

My primary project was a "data dump" service to clean up a MongoDB database containing 2.5 billion documents. The massive data volume was causing high timeout rates and system instability. I built an asynchronous service in Go to delete expired price records in batches. To make it efficient, I used a method to skip already-scanned data and automated the process to run every hour with a real-time monitoring dashboard. This removed 1.5 billion records and reduced our timeout rate from 2% to 0.1%.

I also developed a "data diff" pipeline to keep the downstream team’s database synchronized with partners. When a partner change its data update strategy, from whole updates to append-only, the database grew too large because old data wasn't being removed. I created a solution that compares incoming data with existing records to get the diff and uses a message queue to delete old entries in the background. This reduced the database size by 30% and lowered query overhead by 25% without requiring any changes to the existing production code.

# 1. 团队合作

## 满足多样需求 - Tesla

**Situation**: While interning on the Range Test Team at Tesla, I developed a task management system for over 1,000 internal vehicle engineers.

**Task**: The challenge was reconciling the needs of a highly diverse group, ranging from hardware-focused test drivers who preferred manual spreadsheets to software engineers requiring automated data tracking.

**Action**: To bridge these different working styles, I conducted "ride-along" sessions with vehicle engineers to understand their pain points with existing tools. I realized the friction wasn't technical, but a matter of UI complexity. I simplified the interface using a React-based Gantt chart while ensuring the backend remained robust by contributing to an event-driven microservices architecture using Kafka. I acted as a translator between the technical constraints of the platform team and the usability needs of the field engineers.

**Result**: This empathetic approach led to 1,000+ engineers adopting the platform within three months and a 60% improvement in system latency. It taught me that technical excellence only matters if you first listen to your diverse stakeholders.

## 不同工作态度 - TikTok data-dump

**Situation**: During my TikTok internship, I developed a data-dump service to clean up 1.5 billion hotel records. I worked closely with a senior engineer who prioritized manual data verification and long-term stability over my preference for rapid, automated deployment.

**Task**: We needed to reconcile our different working styles to ensure the deletion service didn't accidentally disrupt live partner data while meeting a tight deadline.

**Action:** Instead of viewing his caution as a bottleneck, I held a technical deep dive to understand the historical context of his concerns. I realized he had seen manual data entry errors that my automated scripts wouldn't catch. I adapted my design to include a **staged rollout and a validation 'dry-run' dashboard** using Go and Internal Tools. This allowed him to perform the manual spot-checks he trusted, while I maintained the deployment velocity I needed.

**Result:** We successfully purged 1.5 billion records, reducing database size by 30% with **zero production incidents**. This taught me that "slowing down to speed up" is often the most efficient path in high-stakes engineering.

## 帮助别人1 - Alibaba Cloud

**Situation:** During my internship at Alibaba Cloud, our team was finishing a multi-tier data lake project on AWS. A fellow intern was struggling to containerize their Spark jobs, which was delaying our integration phase.

**Task:** I recognized that if their component wasn't ready, our entire pipeline would fail. I wanted to help them get back on track without overstepping or neglecting my own tasks.

**Action:** I set aside an hour each afternoon for a "pair programming" session. Instead of just doing the work for them, I shared my experience with Docker and Kubernetes to help them debug their configuration errors. We also simplified their deployment script together to make it more manageable.

**Result:** My peer successfully deployed their Spark jobs, and we met our project deadline ahead of schedule. This collaboration not only strengthened our team’s output but also built a culture of mutual support that lasted throughout the internship.

## 帮助别人2 - UMTRI

**Situation:** As a Research Intern at the University of Michigan Transportation Research Institute, our team built an AI pipeline to model aircraft taxi times.

**Task:** A teammate handling the weather and airport layout integration became unexpectedly unavailable. I needed to take over his unfinished work to keep the team on schedule, while ensuring my own deliverables did not slip.

**Action:** I immediately synced with my project lead to reprioritize my existing tasks. Because my teammate's code was incomplete and undocumented, I reviewed his Git commit history to reverse-engineer their logic. Once I understood their approach, I stepped in to collect, clean, and align the multi-source geospatial and time-series data using Python and Pandas. This allowed me to cleanly integrate the flight movements and weather conditions into our modular data pipeline.

**Result:** By actively managing my workload and diving into unfamiliar code, we avoided project delays and enabled accurate modeling of aircraft taxi and wait times. Finally, our model successfully influenced four major airports to adapt their queuing strategies.

## 依靠别人 - TikTok data-diff

**Situation:** During my software engineering internship at TikTok , I needed to keep the database syncronized with partner’s ingested data.

**Task:** My goal was to safely remove old data and ensure continueing deletion in the future. Because I did not have direct access to local service team's  services and databases, I had to rely entirely on them to complete the final data sync.

**Action:** I built a new microservice and a data-diff solution using message queues to safely broadcast the deletions. To ensure the partner teams could successfully integrate this, I worked closely with them to align our technical requirements. I provided them with a reliable data stream and trusted their operational expertise to consume the messages and update their systems safely, ensuring our time-sensitive hotel data remained consistent.

**Result:** By relying on strong communication and the execution of local service team, we successfully reduced their database size by over 30% and cut their query overhead by roughly 25%.

## 难相处的同事 - TikTok data-dump

**Situation:** During my internship at TikTok, I worked with a senior engineer who was very protective of our MongoDB production environment and initially dismissed my proposal for a new batch-deletion service.

**Task:** I needed to build rapport and gain his trust to safely remove 1.5 billion expired records without affecting system stability.

**Action:** Instead of arguing for my design, I asked him to mentor me on the edge cases he had seen in the past. I shifted from "selling my idea" to "seeking his expertise." I incorporated his feedback by adding a gradual "canary" rollout and detailed monitoring dashboards. By showing I valued his experience over my own ego, he began to see me as a partner rather than a risk.

**Result:** We successfully deployed the service, reducing backend timeouts from 2% to 0.1%. More importantly, we developed a strong professional relationship where he eventually invited me to contribute to other core backend projects.

## 别人的贡献 - Tesla

**Situation:** During my internship at Tesla, I developed a task management platform that used a distributed Gantt chart system to help vehicle engineers track their testing workflows.

**Task:** While I wrote the core backend and UI, the project’s success relied heavily on a senior engineer who helped me navigate the complex Kubernetes deployment and an infrastructure lead who optimized our Kafka streams.

**Action:** When I presented the final results to leadership—highlighting the 60% latency improvement and 1,000+ active users—I made sure to explicitly credit my colleagues. I created a "Technical Acknowledgments" slide detailing how the senior engineer’s architectural advice and the infra lead’s scaling expertise were essential to reaching those metrics.

**Result:** Sharing the spotlight strengthened our team's trust and led the senior engineer to mentor me on more advanced system design. I learned that at Google’s scale, no major achievement is a solo effort; acknowledging peers builds the culture needed for long-term success.

# 2. 冲突

## 冲突 - TikTok data-dump

**Situation:** During my internship at TikTok, I was developing an asynchronous batch-deletion service to clean up 1.5 billion hotel records. A senior engineer on the team was concerned that my automated Go service might put too much load on our production MongoDB cluster and cause a system outage.

**Task:** I needed to address his valid safety concerns without stalling the project or missing our deadline to reduce database overhead.

**Action:** I organized a technical review to listen to his specific worries. Instead of just defending my code, I proposed a compromise: I added a dynamic rate-limiter and a "kill switch" that allowed us to pause the service instantly if latency spiked. I also implemented a canary rollout, starting with only 1% of the data to prove system stability.

**Result:** By incorporating his feedback, we successfully deleted the records and reduced timeouts from 2% to 0.1%. This resolved the conflict and turned him into a mentor who eventually supported my full deployment.

## 接到负反馈 - Alibaba Cloud

**Situation:** During my internship at Alibaba Cloud, I proposed using a specific caching strategy for our multi-tier data lake to reduce S3 latency. My mentor provided critical feedback, suggesting my approach was too complex and potentially unreliable for our scale.

**Task:** Initially, I disagreed because my local tests showed significant speed improvements. However, I needed to handle the feedback professionally and ensure the project’s long-term stability.

**Action:** Instead of dismissing his view, I asked for a follow-up to understand his concerns about edge cases. I realized I hadn't fully considered the maintenance overhead for the SRE team. I pivoted by developing a simplified version of the cache that used standard AWS configurations, which addressed his reliability concerns while still improving performance.

**Result:** This adjusted approach reduced latency by 40% without increasing system complexity. It taught me that "better" isn't just about speed, but about team-wide maintainability—a core value I know Google prizes.

## 想法被否决 - Tesla

**Situation:** During my internship at Tesla, I proposed migrating our task management platform’s data storage to a NoSQL database to handle the rapid growth of vehicle engineering logs, believing it would offer better horizontal scaling.

**Task:** My lead rejected the proposal, favoring our existing MySQL setup. I needed to handle this professionally while ensuring the system could still meet our performance goals.

**Action:** Instead of pushing back, I asked for a deep-dive meeting to understand the rejection. I realized the team prioritized data consistency and existing maintenance expertise over raw scalability. I pivoted my focus to optimizing our current schema and implementing a Redis caching layer to alleviate the load. I documented these trade-offs to show I understood the long-term operational costs.

**Result:** This approach improved system latency by 60% using the approved stack. I learned that a "perfect" technical solution is only successful if it aligns with the team’s operational reality and long-term goals.

# **3. 模糊 & 解决问题**

## 模糊 - TikTok data-dump

**Situation:** During my internship at TikTok, I was tasked with cleaning up "stale data" from a 2.5-billion-document MongoDB collection. I received no specific guidance on what defined "stale" or how to safely delete records at that scale without impacting live traffic.

**Task:** I had to define the deletion criteria and build a safe execution plan from scratch to ensure system stability for our partners.

**Action:** I began by analyzing data access patterns and interviewing senior engineers to define "expired metadata." To handle the ambiguity of the technical implementation, I researched similar industry patterns and proposed an asynchronous Go service with a built-in rate limiter. I presented a detailed design doc that included a "dry-run" mode to validate my logic before any real data was touched.

**Result:** This proactive approach allowed us to safely remove 1.5 billion records, reducing backend timeouts from 2% to 0.1% and improving overall system reliability.

## Describe a situation where the requirements of a project changed drastically halfway through.

**Situation:** During my TikTok internship, I was building a pipeline to ingest hotel data from external partners.

**Task:** Halfway through, a major partner changed their data-feed logic to send only new updates rather than full datasets. This meant our existing system would stop removing old information, causing the database to grow too large.

**Action:** I pivoted to design a "data-diff" solution. I added a filter to compare incoming updates with existing records and used a message queue to handle deletions asynchronously. This allowed us to adapt to the partner's change without making risky modifications to our core production services.

**Result:** The updated pipeline successfully kept the data synchronized, reducing the partner's database size by 30% and cutting query overhead by 25%. This experience taught me how to stay flexible and find low-risk solutions when project requirements shift.

# 4. Failure, Adaptability, & Growth

## （Tell me about your biggest professional failure.）

## Describe a time you missed a critical deadline. What happened?

**Situation** During my internship at TikTok, I was tasked with deleting 1.5 billion expired records from a massive MongoDB collection to improve system stability.

**Task** I initially estimated and committed to completing the primary cleanup within **48 hours** to meet a storage reduction goal.

**Action** As the process began, I monitored the logs and noticed that the deletion load was causing a slight increase in backend timeouts. I realized that meeting the original deadline would require a speed that risked a system outage. I chose to prioritize **production health**. I immediately informed my manager of the delay, explained the technical risk, and implemented a **rate-limiter** to slow the process down to a safe speed.

**Result** We missed the 48-hour deadline, as the cleanup ultimately took **three days**. However, the system remained stable, and we successfully reduced the timeout rate from **2% to 0.1%**. This experience taught me the importance of early communication and that technical reliability must always come before a calendar date.

## Tell me about a time you introduced a bug into production. How did you handle it?

**Situation:** During my TikTok internship, I deployed a Go service to delete 1.5 billion expired hotel records from our MongoDB collection.

**Task:** My goal was to improve system stability while ensuring live user traffic remained unaffected.

**Action:** Shortly after launch, I noticed a minor spike in database latency because my batch size was slightly too high for peak traffic hours. I immediately used the "kill switch" I had implemented to pause the service. I then analyzed our internal metrics, tuned the batch parameters, and added a dynamic rate-limiter to automatically adjust the deletion speed based on system load.

**Result:** After these adjustments, the service ran smoothly, successfully reducing backend timeouts from 2% to 0.1%. This experience taught me that building safety features like "kill switches" and rate-limiters is just as important as the core logic when working at a massive scale.

## Tell me about a time you felt overwhelmed by your workload. What steps did you take?

# 5. Initiative, Ownership, & "Googleyness”

## Tell me about a time you went above and beyond your job description.

**Situation:** During my internship at **Tesla**, I developed a task management platform used by over 1,000 internal vehicle engineers.

**Task:** While the core system was functional, it lacked a secure way for employees to log in. I was tasked with integrating a robust authentication layer to protect sensitive internal data.

**Action:** I decided to implement **Microsoft OAuth** to allow engineers to use their existing company credentials. To ensure a secure and standard implementation, I spent several days studying official documentation and security best practices. I then integrated the OAuth flow into our **Spring Boot** and **React** stack, carefully handling token exchange and session management.

**Result:** This added a critical layer of security while making the user experience much smoother. The seamless login process contributed to the platform's rapid adoption and high reliability, ensuring that our internal engineering data remained protected.

## Describe a time you saw something broken and fixed it without being asked.

## Describe a situation where you took the lead on a project, even though you weren't the manager.