# 13 — Core CS Theory Revision Track (research-backed, from TODAY)

**Why it exists (researched, not guessed):** interview-prep sources are consistent that
coding + aptitude is only half the battle. Technical rounds test **DBMS, Operating
Systems, Computer Networks, OOP, and sometimes Software Engineering**, and freshers
who "only did DSA" get caught here (source: Knowledge Gate placement-prep analysis;
topic distribution follows GeeksforGeeks' official "21 Days to Prepare CS Core
Subjects" plan, last updated Nov 2025).

**When you do it:** these exact subjects are in your college timetable in Sem 5.
This sprint is *revision on top of classes*: **30–40 min/day in the evening Focus
slot** for 26 study days, then a light weekly maintenance pass forever.

**The classic questions every fresher gets asked (memorise these 12 first):**

```
OS    — deadlock (4 conditions + prevention), CPU scheduling algos, paging vs segmentation
DBMS  — normalization 1NF→3NF, ACID + one real example each, INNER vs LEFT vs FULL joins
CN    — OSI vs TCP/IP layers, TCP vs UDP (3 differences), HTTP vs HTTPS, DNS query
OOP   — the 4 pillars + one example each (Java), abstract class vs interface, overloading vs overriding
```

---

## Sprint calendar (Day 1 = Mon 10 Aug 2026, Sundays off)

| Study days | Dates | Subject | Sections (topic links below) |
|-----------|-------|---------|-------------------------------|
| 1–5 | **10–14 Aug** | **DBMS** | Architecture, ER model, keys, relational algebra, joins, normalization 1NF–3NF, ACID, concurrency, deadlock, SQL revision |
| 6–12 | **15 + 17–22 Aug** | **OS** | Types, process mgmt (PCB), CPU scheduling, process sync (semaphores), deadlock, memory mgmt (paging/segmentation/virtual memory), page replacement |
| 13–16 | **24–27 Aug** | **CN** | OSI/TCP-IP, IP addressing, TCP vs UDP, congestion control, DNS/HTTP/HTTPS/SMTP/FTP/DHCP |
| 17–21 | **28–29 + 31 Aug, 1–2 Sep** | **Software Engg** | SDLC + models, COCOMO, SRS, testing (black/white box), coupling & cohesion |
| 22–26 | **3–9 Sep** | **OOP** | 4 pillars, class/object, abstract vs interface, overloading vs overriding, GC in Java |

> **Weekly cadence after the sprint (from 12 Sep):** every **Sunday streak session**
> 45 min — one subject's Question Bank (quiz links below) + 2 classic questions out loud.
> That keeps theory alive until placement season without blocking your project time.

---

## 1. DBMS (Days 1–5) — the #2 subject after DSA

- [Introduction of DBMS](https://www.geeksforgeeks.org/dbms/introduction-of-dbms-database-management-system-set-1/) · [3-level architecture](https://www.geeksforgeeks.org/dbms/dbms-architecture-2-level-3-level/)
- [ER Model](https://www.geeksforgeeks.org/dbms/introduction-of-er-model/) · [Types of Keys](https://www.geeksforgeeks.org/dbms/types-of-keys-in-relational-model-candidate-super-primary-alternate-and-foreign/)
- [Relational Algebra basics](https://www.geeksforgeeks.org/dbms/introduction-of-relational-algebra-in-dbms/) · [Inner vs Outer Join](https://www.geeksforgeeks.org/dbms/inner-join-vs-outer-join/)
- [Normalization intro](https://www.geeksforgeeks.org/dbms/introduction-of-database-normalization/) · [Normal Forms](https://www.geeksforgeeks.org/dbms/normal-forms-in-dbms/)
- [ACID Properties](https://www.geeksforgeeks.org/dbms/acid-properties-in-dbms/) · [Concurrency Control](https://www.geeksforgeeks.org/dbms/concurrency-control-in-dbms/) · [Locking](https://www.geeksforgeeks.org/dbms/implementation-of-locking-in-dbms/) · [Deadlock in DBMS](https://www.geeksforgeeks.org/dbms/deadlock-in-dbms/)
- SQL (practise via `04_SQL_TOP_50.md`) · [SQL Quiz](https://www.geeksforgeeks.org/quizzes/sql-gq/)

## 2. Operating Systems (Days 6–12) — biggest volume, highest recall value

- [Types of OS](https://www.geeksforgeeks.org/types-of-operating-systems/) · [Functions of OS](https://www.geeksforgeeks.org/operating-systems/functions-of-operating-system/)
- [Process Management](https://www.geeksforgeeks.org/operating-systems/introduction-of-process-management/) · [PCB](https://www.geeksforgeeks.org/operating-systems/process-table-and-process-control-block-pcb/) · [Context Switch](https://www.geeksforgeeks.org/operating-systems/context-switch-in-operating-system/)
- [CPU Scheduling](https://www.geeksforgeeks.org/operating-systems/cpu-scheduling-in-operating-systems/) · [FCFS/SJF/Priority/RR criteria](https://www.geeksforgeeks.org/operating-systems/cpu-scheduling-criteria/)
- [Process Synchronization](https://www.geeksforgeeks.org/operating-systems/introduction-of-process-synchronization/) · [Semaphores](https://www.geeksforgeeks.org/operating-systems/semaphores-in-process-synchronization/) · [Producer-Consumer](https://www.geeksforgeeks.org/operating-systems/producer-consumer-problem-using-semaphores-set-1/)
- [Deadlock conditions](https://www.geeksforgeeks.org/operating-systems/conditions-for-deadlock-in-operating-system/) · [Banker's Algorithm](https://www.geeksforgeeks.org/operating-systems/bankers-algorithm-in-operating-system-2/) · [Handling deadlocks](https://www.geeksforgeeks.org/operating-systems/handling-deadlocks/)
- [Paging](https://www.geeksforgeeks.org/operating-systems/paging-in-operating-system/) · [Segmentation](https://www.geeksforgeeks.org/operating-systems/segmentation-in-operating-system/) · [Virtual Memory](https://www.geeksforgeeks.org/operating-systems/virtual-memory-in-operating-system/) · [Page Replacement](https://www.geeksforgeeks.org/operating-systems/page-replacement-algorithms-in-operating-systems/)
- [Get Last-Minute OS Notes](https://www.geeksforgeeks.org/operating-systems/last-minute-notes-operating-systems/) · [OS Interview Questions](https://www.geeksforgeeks.org/operating-systems/operating-systems-interview-questions/)

## 3. Computer Networks (Days 13–16) — smaller net, easy marks

- [Networking basics](https://www.geeksforgeeks.org/computer-networks/basics-computer-networking/) · [LAN/MAN/WAN](https://www.geeksforgeeks.org/types-of-area-networks-lan-man-and-wan/)
- [OSI Model](https://www.geeksforgeeks.org/computer-networks/open-systems-interconnection-model-osi/) · [TCP/IP Model](https://www.geeksforgeeks.org/computer-networks/tcp-ip-model/)
- [IP addressing](https://www.geeksforgeeks.org/computer-networks/introduction-of-classful-ip-addressing/) · [IPv4 vs IPv6](https://www.geeksforgeeks.org/computer-networks/differences-between-ipv4-and-ipv6/)
- [TCP connection (3-way handshake)](https://www.geeksforgeeks.org/computer-networks/tcp-connection-establishment/) · [UDP](https://www.geeksforgeeks.org/computer-networks/user-datagram-protocol-udp/) · [Congestion Control](https://www.geeksforgeeks.org/computer-networks/congestion-control-in-computer-networks/)
- [DNS](https://www.geeksforgeeks.org/computer-networks/domain-name-system-dns-in-application-layer/) · [HTTP vs HTTPS](https://www.geeksforgeeks.org/computer-networks/difference-between-http-and-https/) · [SMTP](https://www.geeksforgeeks.org/computer-networks/simple-mail-transfer-protocol-smtp/) · [DHCP](https://www.geeksforgeeks.org/computer-networks/dynamic-host-configuration-protocol-dhcp/)
- Quizzes: [Data Link](https://www.geeksforgeeks.org/quizzes/data-link-layer-gq/) · [Network](https://www.geeksforgeeks.org/quizzes/network-layer-gq/) · [IP](https://www.geeksforgeeks.org/quizzes/ip-addressing-57/) · [Transport](https://www.geeksforgeeks.org/quizzes/transport-layer-gq/) · [Application](https://www.geeksforgeeks.org/quizzes/application-layer-gq/)

## 4. Software Engineering (Days 17–21) — quick win

- [SDLC intro](https://www.geeksforgeeks.org/software-engineering/software-engineering-introduction-to-software-engineering/) · [Waterfall](https://www.geeksforgeeks.org/software-engineering/waterfall-model/) · [Agile models](https://www.geeksforgeeks.org/software-engineering/software-engineering-agile-development-models/)
- [COCOMO Model](https://www.geeksforgeeks.org/software-engineering/software-engineering-cocomo-model/) · [SRS writing](https://www.geeksforgeeks.org/software-engineering/how-to-write-a-good-srs-for-your-project/)
- [Testing principles](https://www.geeksforgeeks.org/software-engineering/software-engineering-seven-principles-of-software-testing/) · [Black box](https://www.geeksforgeeks.org/software-testing/software-engineering-black-box-testing/) · [White box](https://www.geeksforgeeks.org/software-testing/software-engineering-white-box-testing/) · [Coupling & Cohesion](https://www.geeksforgeeks.org/software-engineering/software-engineering-coupling-and-cohesion/)

## 5. OOP (Days 22–26) — always asked, even in service companies

- Learn in **Java** (JDK 21 already installed — write + run small demos in VS Code).
- Topics: **Encapsulation, Abstraction, Inheritance, Polymorphism** — one 2-line demo
  each; `public/private/protected`, constructor vs method, `abstract class` vs
  `interface`, overloading vs overriding, `this`/`super`, garbage collection.
- Resources: GFG OOPs tutorial (link below) + give each pillar a real example in your
  own project code — that example is your interview answer.

---

## 6. Research-backed sources you can trust

- GeeksforGeeks "21 Days to Prepare CS Core Subjects For Placements" — the exact
  breakdown above (Nov 2025): https://www.geeksforgeeks.org/blogs/prepare-cs-core-subjects-for-placements/
- Knowledge Gate "Technical Interview: OS, DBMS, CN and OOP" — the 12 classic
  fresher questions: https://www.knowledgegate.ai/blog/technical-interview-cs-subjects-for-freshers
- GFG Crash/intuition videos for OS/DBMS/CN (search **Vivek Gupta "Core CS for Placements"**)
- Deep-dive video crash course: "Complete Core CS Explained in 60 Mins | OS, DBMS, CN"
  (Vivek Gupta, ~1h) — watch once before Day 1 for the big picture.

**Verification when done (Sep 9):** you should be able to answer all 12 classics
above out loud in 60 seconds each, and score ≥70% on the GFG subject quizzes.