Week 5 | 60 minutes

# Learning goals

-   Analyse stakeholders.
-   Distinguish functional and non-functional requirements.
-   Recognise ambiguity and unsupported requirements.
-   Define scope.
-   Develop user stories and acceptance criteria.
-   Critique AI-generated requirements.

# Activity 1 - Stakeholder Map

<table border="1" cellpadding="6" cellspacing="0" style="border-collapse:collapse; width:100%;">
<tr>
<th style="border:1px solid #888; padding:6px; text-align:left;">Stakeholder</th>
<th style="border:1px solid #888; padding:6px; text-align:left;">Need</th>
<th style="border:1px solid #888; padding:6px; text-align:left;">Potential conflict</th>
</tr>
<tr>
<td style="border:1px solid #888; padding:6px;">Patients</td>
<td style="border:1px solid #888; padding:6px;">Their appointment booked in reliably</td>
<td style="border:1px solid #888; padding:6px;">They want self serviced booking vs an staff booking in for them</td>
</tr>
<tr>
<td style="border:1px solid #888; padding:6px;">Reception</td>
<td style="border:1px solid #888; padding:6px;">Quickly find, cancel, and book appointments without conflicts</td>
<td style="border:1px solid #888; padding:6px;">Want fast, low-friction booking vs. stricter validation rules that slow them down</td>
</tr>
<tr>
<td style="border:1px solid #888; padding:6px;">Practitioners</td>
<td style="border:1px solid #888; padding:6px;">Accurate, up to date schedule and patient history</td>
<td style="border:1px solid #888; padding:6px;">Want full patient's history vs conflict of privacy concerns</td>
</tr>
<tr>
<td style="border:1px solid #888; padding:6px;">System maintainer</td>
<td style="border:1px solid #888; padding:6px;">Small, maintainable, organized codebase</td>
<td style="border:1px solid #888; padding:6px;">Wants simplicity vs stakeholders requesting scope growth</td>
</tr>
<tr>
<td style="border:1px solid #888; padding:6px;">owner</td>
<td style="border:1px solid #888; padding:6px;">Low running cost, reduced errors, increased efficiency</td>
<td style="border:1px solid #888; padding:6px;">Wants a small, cheap system vs other people wanting more features and complexity, costing more money</td>
</tr>
</table>

# Activity 2 - Functional or Non-Functional?

Functional - The system shall allow staff to cancel an appointment.

Non-functional The system should remain responsive for the course-scale
dataset.

Functional The system shall retain cancelled appointments.

Non-functional Core business logic should be independently testable.

□ Functional The system shall search for a patient by ID.

# Activity 3 - Repair Ambiguous Requirements

The system should be easy to use.

Problem: there is no way to track how "easy to use" the system
is. Clarification question: what
specific usability must be met (e.g. new receptionist can do X bookings
with no training under X minutes

Patient search should be fast.

Problem: fast has no defined
threshold. Clarification question:
what is the max acceptable response time for a patient
search

The system should securely manage data.

Problem: securely needs to specify which controls or which
threats. Clarification question:
what specific control are required (password, role-based
access)

Appointments should normally be easy to cancel.

Problem: there is no way to specify how measurable easy
is. Clarification question: are
there conditions that restrict cancellation (practitioner approval) and
what steps should the cancellation process
include

# Activity 4 - AI Requirements Audit

Classify each suggestion: Confirmed / Assumption requiring validation /
Unsupported / Out of scope.

<table border="1" cellpadding="6" cellspacing="0" style="border-collapse:collapse; width:100%;">
<tr>
<th style="border:1px solid #888; padding:6px; text-align:left;">AI suggestion</th>
<th style="border:1px solid #888; padding:6px; text-align:left;">Classification</th>
<th style="border:1px solid #888; padding:6px; text-align:left;">Evidence / reason</th>
</tr>
<tr>
<td style="border:1px solid #888; padding:6px;">Patients receive SMS reminders.</td>
<td style="border:1px solid #888; padding:6px;">Assumption requiring validation</td>
<td style="border:1px solid #888; padding:6px;">Plausible festure but not mentioned in the breief</td>
</tr>
<tr>
<td style="border:1px solid #888; padding:6px;">Facial recognition login.</td>
<td style="border:1px solid #888; padding:6px;">unsupported</td>
<td style="border:1px solid #888; padding:6px;">No evidence in brief but aligns with small, maintainable goal</td>
</tr>
<tr>
<td style="border:1px solid #888; padding:6px;">Receptionists create appointments.</td>
<td style="border:1px solid #888; padding:6px;">confirmed</td>
<td style="border:1px solid #888; padding:6px;">Brief states staff currently handle bookings</td>
</tr>
<tr>
<td style="border:1px solid #888; padding:6px;">Online payment.</td>
<td style="border:1px solid #888; padding:6px;">Out of scope</td>
<td style="border:1px solid #888; padding:6px;">Not mentioned, beyond the scope of booking/record system</td>
</tr>
<tr>
<td style="border:1px solid #888; padding:6px;">Practitioners view schedules.</td>
<td style="border:1px solid #888; padding:6px;">confirmed</td>
<td style="border:1px solid #888; padding:6px;">Directly implied by practitioner, patient, and appointment system</td>
</tr>
<tr>
<td style="border:1px solid #888; padding:6px;">AI recommends treatments.</td>
<td style="border:1px solid #888; padding:6px;">Out of scope</td>
<td style="border:1px solid #888; padding:6px;">Different kind of system, completely different to the brief</td>
</tr>
<tr>
<td style="border:1px solid #888; padding:6px;">Cancelled appointments remain in history.</td>
<td style="border:1px solid #888; padding:6px;">confirmed</td>
<td style="border:1px solid #888; padding:6px;">Brief directly names limited appointment history as a problem</td>
</tr>
</table>

# Exit question

Why is 'AI suggested it' not sufficient evidence for a requirement?

AI suggestions are not sufficient evidence for a requirement because an
AI suggestion isn't traceable to an actual stakeholder or towards the
client brief. The suggestion itself may sound plausible, but it is not
backed up by any evidence. A requirement needs evidence so it can be
verified and doesn't stray away from the project's scope. AI
suggestions should be used as a starting point but not as a complete and
concrete suggestion