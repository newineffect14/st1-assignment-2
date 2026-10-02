# Stage 1 Tutorial – Introducing Software Technology Case Study

## Activity 1 – Think-Pair-Share

If AI can produce a 100-line Python application quickly, what knowledge does a software engineer still need?

1. **Requirements analysis** : understanding what the client actually needs and asking the right questions; AI only builds what it's told.
2. **Testing and verification** ; knowing how to design test cases (normal, edge, invalid) to prove the code works rather than just looks right.
3. **Judgement about scope, security and maintainability** ; deciding what should and shouldn't be built, protecting sensitive data, and making sure the code can be understood and maintained by a team.

## Activity 2 – Is This Software Engineering?

| Scenario | Programming? | Software engineering? | Why? |
|---|---|---|---|
| A – 50-line calculator | Yes | No / minimal | Small, single user, no formal requirements, testing or maintenance process |
| B – Payroll for 5,000 employees | Yes | Yes | Many stakeholders, legal/financial requirements, needs design, testing, security, team work and long-term maintenance |
| C – AI-generated app from one prompt | Yes (code was produced) | No | No requirements gathering, verification, design decisions or accountability – it becomes engineering only when a human analyses, tests and takes responsibility for it |

## Activity 3 – SmartCare Problem Analysis

### Task 1 – Identify stakeholders

| Stakeholder | What do they need? |
|---|---|
| Receptionist | Fast booking and rescheduling without double-booking |
| Practitioner | A clear view of their daily schedule |
| Patient | Reliable appointments and privacy of their information |
| Clinic manager | Reports on bookings, no-shows and staff workload |

### Task 2 – Identify current problems

1. Double bookings because spreadsheets don't check availability.
2. Paper records can be lost, damaged or unreadable.
3. Data is duplicated across spreadsheets and paper, causing inconsistencies.
4. Patient information isn't secure; anyone with the file or paper can see it.

### Task 3 – Ask client questions

1. Who will use the system and what should each user be allowed to do?
2. How long are appointments and are there different types?
3. What are practitioners' working hours?
4. What patient information must be stored?
5. Do patients need to book online or receive reminders?

## Activity 4 – Critique an AI Response

| Suggestion | Client evidence? | In scope? | Decision |
|---|---|---|---|
| Appointment management | Yes, client mentions appointments | Yes | **Accept** |
| Facial recognition login | No | No – complex, privacy risk | **Reject** |
| AI diagnosis recommendations | No | No – clinical/legal risk, not a booking task | **Reject** |
| Patient search | Implied as managing patients | Yes | **Accept (provisional)** |
| Online payment | No | Not yet | **Defer: ask client** |
| Practitioner schedule view | Implied as managing practitioners | Yes | **Accept (provisional)** |
| Insurance processing | No | No | **Reject** |
| Treatment-plan generation | No | No – clinical decision, high risk | **Reject** |

## Exit question

Verifying that the software meets the client's real requirements and is safe to use. For example, testing the booking system with realistic and invalid inputs and confirming with the clinic that it handles patient data correctly. AI can suggest tests, but human engineers must decide what "correct" means and have the final say.