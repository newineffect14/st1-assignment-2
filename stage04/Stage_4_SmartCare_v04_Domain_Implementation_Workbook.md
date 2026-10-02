# 1. UML-to-Code Trace

| UML element                                 | Python element                                           | Implemented? | Notes                                      |
|---------------------------------------------|----------------------------------------------------------|--------------|--------------------------------------------|
| Patient (class)                             | class Patient                                            | Yes          | Written manually (Lab step B, AI OFF)      |
| Patient.patient_id                          | private attr \_patient_id                                | Yes          | set once at creation                       |
| Patient.name                                | private attr \_name                                      | Yes          | Checked by validate()                      |
| Patient.validate()                          | def validate(self) -\> bool                              | Yes          | Confirms name is valid (not empty)         |
| Practitioner (class)                        | class Practitioner                                       | Yes          | Written manually (Lab step C, AI OFF)      |
| Practitioner.practitioner_id/name/specialty | private attrs                                            | Yes          | No behaviour required currently            |
| Appointment (class)                         | class Appointment                                        | Yes          | AI-generated then reviewed (Lab steps D–G) |
| Appointment.appointment_id/date_time/status | private attrs + AppointmentStatus enum                   | Yes          | Status uses an enum, not a raw string      |
| Appointment.cancel()                        | def cancel(self)                                         | Yes          | Only allows legal status transitions       |
| Appointment.is_duplicate()                  | def is_duplicate(self, practitioner, date_time) -\> bool | Yes          | Checked before a new booking is created    |

# 2. Domain Invariants

| Class        | Invariant / rule                                                                                      | How protected                                                    |
|--------------|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| Patient      | Name must be valid before use                                                                         | Private attribute + validate(), nothing else can set it directly |
| Practitioner | Identity fields set once, not changed later                                                           | Private attributes, no public mutators                           |
| Appointment  | Status can only move through legal transitions; cancelled appointments stay as records, never deleted | status kept private, changed only inside cancel()                |
| Appointment  | A practitioner can't be double-booked at the same time                                                | Enforced by is_duplicate() before a booking is confirmed         |
|              |                                                                                                       |                                                                  |
|              |                                                                                                       |                                                                  |

# 3. Composition / Inheritance Decisions

| Relationship               | Decision    | Rationale                                                                              |
|----------------------------|-------------|----------------------------------------------------------------------------------------|
| Patient – Appointment      | Association | A patient can exist without appointments, and an appointment must outlive cancellation |
| Practitioner – Appointment | Association | Same reason, appointment history must persist independently                            |
|                            |             |                                                                                        |
|                            |             |                                                                                        |
|                            |             |                                                                                        |

# 4. AI Pair-Programming Record

| AI contribution                                        | Conforms? | Decision                                            | Reason                                                                            | Verification             |
|--------------------------------------------------------|-----------|-----------------------------------------------------|-----------------------------------------------------------------------------------|--------------------------|
| Public attributes for id/status/date_time              | No        | Rejected — made private with properties             | Public state let any caller mutate status directly, bypassing the transition rule | Code review (step E)     |
| cancel() with no guard                                 | No        | Rejected because added InvalidTransitionError check | Needed to protect the invariant that cancelled → cancelled is illegal             | Test 2 (double cancel)   |
| is_duplicate() comparing practitioner + date_time only | Partially | Modified, I added status == SCHEDULED condition     | A cancelled appointment shouldn't block rebooking the same slot                   | Test 4 (duplicate check) |
|                                                        |           |                                                     |                                                                                   |                          |
|                                                        |           |                                                     |                                                                                   |                          |

# 5. Updated UML

Insert updated UML only if implementation revealed a justified design change. Explain every change.