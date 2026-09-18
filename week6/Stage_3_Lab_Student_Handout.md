# STEPS A-F were done in the tutorial and domain model handout md file

# A - Requirements Review

Highlight nouns, verbs and business rules in SmartCare v0.2.

# B - Candidate Classes

Record candidate concepts, supporting requirements, state and behaviour.

# C - CRC Cards

Create CRC cards for Patient, Practitioner and Appointment.

# D - UML Model

Draw classes, attributes, operations, associations and multiplicities.

# E - AI Design Review

Ask AI to suggest classes and relationships using only confirmed
requirements; require supporting requirement IDs.

# F - Compare and Decide

Record at least one accepted, modified and rejected AI suggestion.

# G - Python Skeletons

Create simple Patient, Practitioner and Appointment class skeletons.

# H - Consistency Check

Check model-code consistency; do not implement full behaviour yet.

 **Class names align with UML:** Patient, Practitioner and Appointment
match the class diagram exactly. No extra classes (no
Manager/Controller/Clinic) were added during coding.

 **Attributes reflect modelled state:** Patient (patient_id, name),
Practitioner (practitioner_id, name, specialty) and Appointment
(appointment_id, patient, practitioner, date_time, status) match the CRC
cards and UML attributes.

 **Methods reflect responsibilities:** validate() on Patient matches
its \"basic self-validation\" responsibility; cancel() and
is_duplicate() on Appointment match its \"change status\" and
\"duplicate check\" responsibilities from the CRC card.

 **Relationships represented consistently:** Appointment holds a direct
reference to one Patient and one Practitioner, matching the 1--0..\*
associations in the UML diagram (Patient/Practitioner side is not stored
on the objects themselves, since neither FR requires them to track their
own appointment list yet).

 **No unsupported classes/features appeared during coding:**
AppointmentStatus stayed a plain attribute (not a class), and no
Manager/Controller/notification code was added - consistent with the AI
Design Review decisions.

 **Full behaviour intentionally not implemented:** is_duplicate() only
compares against a single Appointment\'s own slot. Checking a proposed
booking against *every* existing appointment for a practitioner needs a
repository/collection that doesn\'t exist at this stage, so it is left
as a stub rather than guessed at.

# Reflection

**What modelling decision was hardest?** Deciding where the
duplicate-booking responsibility belongs. It was tempting to put it on
Practitioner (since a practitioner \"owns\" their schedule), but
FR-01/NFR-01 are really about the appointment slot itself, so it stayed
on Appointment.

**Where did AI over-design?** AI proposed PatientManager,
PractitionerManager, AppointmentManager, ClinicController,
ScheduleEngine and NotificationManager, but none supported by any
FR/NFR. It also proposed a separate AppointmentStatus class where a
plain attribute was enough.

**What evidence supported your final choices?** NFR-04 (simple,
maintainable) justified rejecting every unsupported class. FR-04/FR-11
(appointments must remain in history after cancellation) justified using
association instead of composition between Patient/Practitioner and
Appointment.