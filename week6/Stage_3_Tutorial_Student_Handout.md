

# Candidate Concepts

  ----------------------------------------------------------------------------
  Candidate               Class?                  Reason
  ----------------------- ----------------------- ----------------------------
  Patient                 Yes                     Own identity/state, direct
                                                  FR support (FR-02, FR-07,
                                                  FR-09)

  Practitioner            Yes                     Own identity/state, direct
                                                  FR support (FR-05, FR-10)

  Appointment             Yes                     Owns booking, status,
                                                  duplicate check (FR-01,
                                                  FR-03, FR-04, FR-08, FR-11)

  Name                    No                      An attribute of
                                                  Patient/Practitioner, not a
                                                  concept with its own
                                                  responsibilities

  Clinic                  No                      Single-location system; no
                                                  FR gives it distinct state
                                                  or behaviour

  Database                No                      Implementation/persistence
                                                  concern, not a domain
                                                  concept

  Cancellation            No                      A state change on
                                                  Appointment (status →
                                                  cancelled), not its own
                                                  class

  Status                  No                      An attribute of Appointment,
                                                  not its own class
  ----------------------------------------------------------------------------

# CRC Cards

## Patient

  -----------------------------------------------------------------------
  Responsibilities                    Collaborators
  ----------------------------------- -----------------------------------
  Know own identity (ID, name):       Appointment
  FR-02, FR-07, FR-09                 

  Basic self-validation: FR-09        
  -----------------------------------------------------------------------

## Practitioner

  -----------------------------------------------------------------------
  Responsibilities                    Collaborators
  ----------------------------------- -----------------------------------
  Know own identity/specialty: FR-10  Appointment

  Know own availability via its       
  Appointments: FR-05                 
  -----------------------------------------------------------------------

## Appointment

  -----------------------------------------------------------------------
  Responsibilities                    Collaborators
  ----------------------------------- -----------------------------------
  Know patient, practitioner,         Patient, Practitioner
  timeslot, status: FR-01, FR-08      

  Change status (cancel) without      
  deleting the record: FR-03, FR-04,  
  FR-11                               
  -----------------------------------------------------------------------

# Relationship Reasoning

Patient to Appointment: which relationship and why?

Association, not composition. An Appointment must withstand the action
of cancellation and remain in history (FR-04, FR-11), so its lifecycle
isn\'t owned by Patient, if we did composition, it would wrongly imply
the appointment can\'t exist independently of the patient\'s own
lifecycle management.

Practitioner to Appointment: what multiplicity?

1 ↔ 0..\* because one Practitioner can have 0 or many Appointments; each
Appointment has exactly one Practitioner.

Should Appointment inherit from Patient?

No. There\'s no is-a relationship: an Appointment is not a kind of
Patient, it\'s a booking that references one. Inheritance here wouldn't
a genuine domain relationship.

Does Clinic need to own every object?

No. No FR requires a Clinic entity at all (single-location scope), so
there\'s nothing for it to own. Adding it would be unjustified
complexity.

# AI Model Critique

Critique AI proposals: PatientManager, PractitionerManager,
AppointmentManager, ClinicController, NotificationManager,
ScheduleEngine.

I will reject them all because there is nothing in the requirements that
says we need these classes. None of the functional requirements mention
managers, controllers, notifications or a scheduling engine.

These classes are examples of AI over-design, where AI creates extra
classes just because they sound useful. Adding them would also make the
system more complicated, which goes against NFR-04, which focuses on
keeping the system simple and maintainable.

If we need extra functionality later, such as checking for duplicate
bookings across all appointments, we can add a separate service if a
requirement supports it. For now, there is no clear reason to include
these classes.