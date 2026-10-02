# Activity 1 - Encapsulation Review

| Class        | Protected state / invariant                                                                                                                                                                 | Public operations                                      |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| Patient      | Patient_id and name must be kept protected, and then invariant is that name must be valid (non-empty) before a booking can proceed                                                          | validate() : bool                                      |
| Practitioner | practitioner_id, name should be protected, no invariant enforced                                                                                                                            | none defined at this stage                             |
| Appointment  | appointment_id, date_time, status is protected; invariant is that a practitioner can't hold two appointments at the same date_time, and cancelled appointments stay as records, not deleted | cancel(), is_duplicate(practitioner, date_time) : bool |

# Activity 2 - Composition or Inheritance?

Appointment and Patient -\> association Reason: \_ A Patient can exist with zero appointments and an Appointment must keep existing (as history) even after cancellation, so neither owns the other's lifecycle.\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Appointment and Practitioner -\> association Reason: \_\_ the same reasoning, a cancelled appointment must persist independent of the practitioner.\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Doctor and Practitioner (hypothetical) -\> Inheritance Reason: A Doctor is a Practitioner, just a more specific one, so it should extend the class, not just reference it..\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Clinic and Appointment -\> Composition Reason: \_\_ if the Clinic didn't exist, the appointment wouldn’t exist either. There needs to be a Clinic in order to have an appointment.\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

# Activity 3 - Responsibility Allocation

Who decides whether SCHEDULED can become CANCELLED?

Appointment because it owns its own status, so it's the one that should control how that status changes.

Who validates a patient name?

Patient as since the name belongs to Patient via validate(). Checking it should happen there too.

Should Appointment execute SQL? Why?

No because Appointment should just handle appointment rules, not talk to the database, that's a separate job. Should the UI decide whether a status transition is legal?

Should the UI decide if a status transition is legal?

No. The UI should just ask Appointment to cancel and show the result, not make the rule itself, or it would have to repeat that logic everywhere and could get it wrong.

# Activity 4 - AI Code Critique

AI generates an Appointment class with public status mutation, SQL inside cancel(), a NotificationManager dependency and inheritance from PatientRecord. Identify at least five design problems and corrections.

# Exit question

Why can code be object-oriented syntactically but still have poor object-oriented design?

Code can look object-oriented using classes, maybe inheritance but still be badly designed if the responsibilities are in the wrong place. For example, if any part of the program can change an appointment's status directly, or if the database logic sits inside the Appointment class instead of somewhere separate. Good design is about which class is responsible for what.