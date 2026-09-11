Week 5 \| 60 minutes

# Learning goals

-   Analyse stakeholders.

-   Distinguish functional and non-functional requirements.

-   Recognise ambiguity and unsupported requirements.

-   Define scope.

-   Develop user stories and acceptance criteria.

-   Critique AI-generated requirements.

# Activity 1 - Stakeholder Map

  -----------------------------------------------------------------------
  Stakeholder             Need                    Potential conflict
  ----------------------- ----------------------- -----------------------
  Patients                Their appointment       They want self serviced
                          booked in reliably      booking vs an staff
                                                  booking in for them

  Reception               Quickly find, cancel,   Want fast, low-friction
                          and book appointments   booking vs. stricter
                          without conflicts       validation rules that
                                                  slow them down

  Practitioners           Accurate, up to date    Want full patient's
                          schedule and patient    history vs conflict of
                          history                 privacy concerns

  System maintainer       Small, maintainable,    Wants simplicity vs
                          organized codebase      stakeholders requesting
                                                  scope growth

  owner                   Low running cost,       Wants a small, cheap
                          reduced errors,         system vs other people
                          increased efficiency    wanting more features
                                                  and complexity, costing
                                                  more money
  -----------------------------------------------------------------------

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
with no training under X minutes)

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

  -----------------------------------------------------------------------
  AI suggestion           Classification          Evidence / reason
  ----------------------- ----------------------- -----------------------
  Patients receive SMS    Assumption requiring    Plausible festure but
  reminders.              validation              not mentioned in the
                                                  breief

  Facial recognition      unsupported             No evidence in brief
  login.                                          but aligns with small,
                                                  maintainable goal

  Receptionists create    confirmed               Brief states staff
  appointments.                                   currently handle
                                                  bookings

  Online payment.         Out of scope            Not mentioned, beyond
                                                  the scope of
                                                  booking/record system

  Practitioners view      confirmed               Directly implied by
  schedules.                                      practitioner, patient,
                                                  and appointment system

  AI recommends           Out of scope            Different kind of
  treatments.                                     system, completely
                                                  different to the brief

  Cancelled appointments  confirmed               Brief directly names
  remain in history.                              limited appointment
                                                  history as a problem
  -----------------------------------------------------------------------

# Exit question

Why is \'AI suggested it\' not sufficient evidence for a requirement?

AI suggestions are not sufficient evidence for a requirement because an
AI suggestion isn\'t traceable to an actual stakeholder or towards the
client brief. The suggestion itself may sound plausible, but it is not
backed up by any evidence. A requirement needs evidence so it can be
verified and doesn\'t stray away from the project's scope. AI
suggestions should be used as a starting point but not as a complete and
concrete suggestion