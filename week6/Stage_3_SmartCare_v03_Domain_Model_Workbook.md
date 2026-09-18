

# Requirement-to-Concept Trace

  --------------------------------------------------------------------------------------
  Requirement             Concept           State/behaviour      Decision
  ----------------------- ----------------- -------------------- -----------------------
  FR-01 (create           Appointment       patient,             Confirmed ---
  appointment, no                           practitioner,        Appointment
  duplicate booking)                        timeslot, status;    
                                            booking              
                                            responsibility       

  FR-02 (search patient   Patient           patient ID, name     Confirmed --- Patient
  by name/ID)                                                    

  FR-03 (cancel           Appointment       status change        Confirmed ---
  appointment)                              (cancel)             Appointment

  FR-04 (retain cancelled Appointment       status = cancelled,  Confirmed ---
  appointments in                           not deleted          Appointment (no
  history)                                                       separate History class;
                                                                 history is the set of
                                                                 Appointment records)

  FR-05 (practitioner     Practitioner,     Practitioner         Confirmed ---
  views schedule)         Appointment       collaborates with    Practitioner ↔
                                            its Appointments     Appointment

  FR-06 (practitioner     Practitioner,     Practitioner         Confirmed --- no direct
  views patient history)  Patient,          collaborates with    Practitioner--Patient
                          Appointment       Patient via shared   link needed, reached
                                            Appointments         through Appointment

  FR-07 (locate patient   Patient           identity/state       Confirmed --- Patient
  records)                                                       

  FR-08 (record/display   Appointment       status attribute     Confirmed ---
  appointment status)                                            Appointment

  FR-09 (manage patient   Patient           identity/state,      Confirmed --- Patient
  records)                                  basic validation     

  FR-10 (manage           Practitioner      identity/specialty   Confirmed ---
  practitioner                                                   Practitioner
  records/availability)                                          

  FR-11 (reliable         Appointment       status, not deleted  Confirmed ---
  appointment history)                      on cancel            Appointment

  FR-12 (support                            no state/behaviour   Deferred --- reporting
  operational reports)                      justified yet        is a cross-object
                                                                 concern
                                                                 (service/repository),
                                                                 not a domain concept;
                                                                 no dedicated class at
                                                                 this stage
  --------------------------------------------------------------------------------------

# CRC Cards

## Patient

  -----------------------------------------------------------------------
  Responsibilities                    Collaborators
  ----------------------------------- -----------------------------------
  Know own identity (patient ID,      Appointment
  name) --- FR-02, FR-07, FR-09       

  Provide basic validation of own     
  state (e.g. required ID/name        
  present) --- FR-09                  
  -----------------------------------------------------------------------

## Practitioner

  -----------------------------------------------------------------------
  Responsibilities                    Collaborators
  ----------------------------------- -----------------------------------
  Know own identity and specialty --- Appointment
  FR-10                               

  Know own availability/schedule (via 
  its Appointments) --- FR-05, FR-10  
  -----------------------------------------------------------------------

## Appointment

  -----------------------------------------------------------------------
  Responsibilities                    Collaborators
  ----------------------------------- -----------------------------------
  Know its patient, practitioner,     Patient
  date/time and status --- FR-01,     
  FR-08                               

  Validate it is not a duplicate      
  booking for its                     
  practitioner/timeslot: FR-01,       
  NFR-01                              

  Change own status (e.g. cancel)     Practitioner
  while preserving the record ---     
  FR-03, FR-04, FR-11                 
  -----------------------------------------------------------------------

## Optional class

  -----------------------------------------------------------------------
  Responsibilities                    Collaborators
  ----------------------------------- -----------------------------------
                                      

                                      
  -----------------------------------------------------------------------

# UML Class Diagram

Insert/draw UML here. Include defensible relationships and
multiplicities.! ![UML Class Diagram](images/week6pict.png)

# Design Rationale

Explain class selection, responsibility allocation and key
relationships.

### Class selection

Patient, Practitioner and Appointment are the main classes because all
the functional requirements (FR-01--FR-11) relate directly to one of
these three. I considered having a Clinic class, but the system is only
designed for one clinic location. Since there are no requirements that
give the Clinic its own information or behaviour, it would not add much
to the system. I would only add it later if requirements such as
supporting multiple clinics were introduced.

### Responsibility allocation

Patient and Practitioner are responsible for their own personal
information and basic validation, based on FR-02, FR-07, FR-09 and
FR-10. Appointment is responsible for creating bookings, managing
appointment status and checking for duplicate bookings. This is because
FR-01, FR-03, FR-04 and FR-08 mainly describe what an appointment does.
Keeping these responsibilities separate makes the system easier to
understand and prevents one class from doing too many different jobs.

### Relationships

Patient--Appointment and Practitioner--Appointment are simple
associations, with each Patient or Practitioner being able to have 0 or
more appointments**.** We did not use composition because appointments
need to remain in the system even after they are cancelled. FR-04 and
FR-11 require cancelled appointments to stay in the appointment history.
Each appointment is linked to one Patient and one Practitioner, as there
are no requirements for group or multiple-patient appointments.

# AI Design Review Record

  ----------------------------------------------------------------------------------------------------------------
  AI suggestion                        Evidence               Decision   Reason                Model change
  ------------------------------------ ---------------------- ---------- --------------------- -------------------
  Treat Patient--Appointment and       FR-04/FR-11 require    Accepted   Matches the           None --- confirms
  Practitioner--Appointment as plain   cancelled appointments            requirement that      the diagram above
  associations, not composition        to persist                        appointment history   
                                       independently of                  continues beyond the  
                                       ongoing                           action of             
                                       patient/practitioner              cancellation          
                                       state                                                   

  Add a separate AppointmentStatus     No FR requires status  Modified   to keep it simple, a  Reduced
  class                                to have its own                   plain status          AppointmentStatus
                                       behaviour beyond being            attribute on          from a class to an
                                       recorded and displayed            Appointment would     attribute on
                                       (FR-08)                           already satisfy FR-08 Appointment
                                                                         without having the    
                                                                         complexity of a full  
                                                                         class                 

  Add AppointmentManager,              None --- no FR         Rejected   Classic AI            None
  PatientManager, ScheduleEngine,      describes a                       over-design pattern   
  ClinicController,                    coordinating                      (manager/controller   
  NotificationManager                  \"manager\" or                    classes with no       
                                       notification feature              requirement support)  
                                                                         it conflicts with     
                                                                         NFR-04\'s \"simple    
                                                                         and maintainable\"    
                                                                         goal and introduces   
                                                                         unsupported scope     
                                                                         (notifications        
                                                                         aren\'t in the        
                                                                         confirmed             
                                                                         requirements)         

  Add a Clinic class owning            None --- system is     Rejected   No requirement        None
  Patients/Practitioners/Appointment   scoped to a single                support and would add 
                                       clinic location, no FR            an unjustified        
                                       gives Clinic its own              top-level container   
                                       state                                                   

                                                                                               
  ----------------------------------------------------------------------------------------------------------------