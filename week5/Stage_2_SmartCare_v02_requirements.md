# Problem and Scope

SmartCare is a small community clinic currently using spreadsheets,
paper records and manual processes to manage patients, practitioners and
appointments. This causes duplicate bookings, difficulty locating
patient records, inconsistent appointment status, limited visibility of
practitioner availability, manual cancellations, no reliable appointment
history, and difficulty producing operational reports. Management wants
the system to not be complex but rather a simple system for patient,
practitioner and appointment management.

# 2. Stakeholders {#stakeholders .unnumbered}

+-----------------------+-----------------------+-----------------------+
| Stakeholder           | Need                  | Evidence              |
+=======================+=======================+=======================+
| patient               | Their appointment     | Case study has lack   |
|                       | booked in reliably    | of reliable           |
|                       | and accurately        | appointment history   |
|                       |                       | as a current problem  |
+-----------------------+-----------------------+-----------------------+
| Reception staff       | Book, find, and       | Case study has        |
|                       | cancel appointments   | duplicate appointment |
|                       | quickly without       | bookings and manual   |
|                       | creating duplicates   | cancellation          |
|                       |                       | processes as current  |
|                       |                       | problems              |
+-----------------------+-----------------------+-----------------------+
| practitioners         | Accurate, up to date  | Case study has lack   |
|                       | schedule and patient  | of reliable           |
|                       | history               | appointment history,  |
|                       |                       | difficulty locating   |
|                       |                       | patient records, and  |
|                       |                       | inconsistent          |
|                       |                       | appointment status    |
|                       |                       | information as        |
|                       |                       | current problems      |
+-----------------------+-----------------------+-----------------------+
| System maintainer     | Small, maintainable,  | Case study has        |
|                       | organized system      | "management wants a   |
|                       |                       | simple software       |
|                       |                       | system that can       |
|                       |                       | initially support     |
|                       |                       | patient,              |
|                       |                       |                       |
|                       |                       | practitioner and      |
|                       |                       | appointment           |
|                       |                       | management"           |
+-----------------------+-----------------------+-----------------------+
| owner                 | Low running cost,     | Tutorial handout      |
|                       | reduced errors,       | identifies these as   |
|                       | increased efficiency  | the owner\'s needs.   |
+-----------------------+-----------------------+-----------------------+

### In Scope {#in-scope .unnumbered}

-   Patient management and patient records

-   Practitioner management

-   Creating and booking appointments

-   Searching for patients by name or ID

-   Viewing practitioner schedules and availability

-   Cancelling appointments

-   Preventing duplicate/double bookings

-   Retaining cancelled appointments in appointment history

-   Viewing appointment history

-   Simple, maintainable system design

### Out of Scope {#out-of-scope .unnumbered}

-   Online payments

-   AI treatment recommendations

-   Facial recognition login

-   Complex AI features

-   Other features not directly related to patient, practitioner and
    appointment management

### Provisional / Uncertain {#provisional-uncertain .unnumbered}

-   **SMS appointment reminders** (provisional). This is a plausible
    feature, but the case study does not explicitly state that the
    clinic requires SMS reminders, so this would need to be validated
    with the stakeholders.

# 3. Functional Requirements {#functional-requirements .unnumbered}

FR-01: The system should allow reception staff to create new
appointments for patients selected with a practitioner and a timeslot,
not allowing duplicate bookings.

FR-02: The system shall allow reception staff to search for a patient by
name or ID.

FR-03: The system shall allow reception staff to cancel an appointment.

FR-04: The system shall retain cancelled appointments in the appointment
history.

FR-05: The system shall allow practitioners to view their current
appointment schedule.

FR-06: The system shall allow practitioners to view relevant patient
history.

FR-07: The system shall allow staff to locate patient records.

FR-08: The system shall record and display the status of an appointment.

FR-09: The system shall manage patient records.

FR-10: The system shall manage practitioner records and availability.

FR-11: The system shall provide reliable appointment history.

FR-12: The system shall support the production of operational reports.

# 4. Non-Functional Requirements {#non-functional-requirements .unnumbered}

NFR-01: The system shall prevent a practitioner\'s time slot from being
double-booked, to preserve appointment data integrity.

NFR-02: The system should remain responsive when handling the
course-scale dataset.

NFR-03: Core business logic should be independently testable.

NFR-04: The system should be simple and maintainable so that it does not
become unnecessarily complex.

NFR-05: The system should maintain an organised codebase to support
ongoing maintenance.

NFR-06: The system should reliably store and display appointment
information without inconsistent appointment statuses.

# 5. User Stories {#user-stories .unnumbered}

US-01: As a receptionist, I want to search for a patient by name or ID,
so that I can quickly locate their record without checking multiple
spreadsheets.

US-02: As a receptionist, I want to book an appointment for a patient
with a practitioner and timeslot, so that appointments are recorded
reliably without duplicate bookings.

US-03: As a receptionist, I want to cancel an appointment, so that
appointment changes can be managed without relying on manual processes.

US-04: As a practitioner, I want to view my appointment schedule, so
that I know when I am available and who I am seeing.

US-05: As a practitioner, I want to view patient history, so that I can
access relevant information about previous appointments.

US-06: As a system maintainer, I want the system to be simple and
maintainable, so that it can support patient, practitioner and
appointment management without unnecessary complexity.

# 6. Acceptance Criteria {#acceptance-criteria .unnumbered}

GIVEN a patient, practitioner, and timeslot are selected\
WHEN reception staff create an appointment\
THEN the system records the appointment and prevents a duplicate booking
for the same practitioner and timeslot.

GIVEN an existing appointment\
WHEN reception staff cancel the appointment\
THEN the appointment is marked as cancelled and remains in the
appointment history.

GIVEN a receptionist needs to locate a patient\
WHEN they search using the patient\'s name or ID\
THEN the system displays the matching patient record.

# 7. Assumptions and Open Questions Assumptions: • Reception staff are responsible for creating, finding and cancelling appointments. • Practitioners need access to their schedules and relevant patient history. • The first version should remain small and focused on patient, practitioner and appointment management. • Cancelled appointments should remain available as historical records.  Open Questions: • What specific response time should be required for patient searches? • What specific security and access controls are required for patient data? • Should patients be able to book appointments themselves, or should booking remain staff-managed? {#assumptions-and-open-questions-assumptions-reception-staff-are-responsible-for-creating-finding-and-cancelling-appointments.-practitioners-need-access-to-their-schedules-and-relevant-patient-history.-the-first-version-should-remain-small-and-focused-on-patient-practitioner-and-appointment-management.-cancelled-appointments-should-remain-available-as-historical-records.-open-questions-what-specific-response-time-should-be-required-for-patient-searches-what-specific-security-and-access-controls-are-required-for-patient-data-should-patients-be-able-to-book-appointments-themselves-or-should-booking-remain-staff-managed .unnumbered}

# 8. AI Requirements Review Record {#ai-requirements-review-record .unnumbered}

  ---------------------------------------------------------------------------
  AI suggestion   Evidence?      Decision       Reason         Verification
  --------------- -------------- -------------- -------------- --------------
  Add SMS         No             Rejected       Plausible      Confirm with
  appointment                                   feature but    the client
  reminders for                                 not mentioned  whether SMS
  patients                                      in the brief.  reminders are
                                                               required
                                                               before
                                                               including
                                                               them.

  Facial          No             Unsupported    There is no    Do not include
  recognition                                   evidence for   unless a
  login                                         facial         stakeholder
                                                recognition in provides
                                                the brief, and evidence and a
                                                it conflicts   clear need.
                                                with the goal  
                                                of a small,    
                                                maintainable   
                                                system.        

  Receptionists   Yes            Confirmed      The brief      Keep as a
  create                                        identifies     functional
  appointments                                  reception      requirement.
                                                staff as       
                                                needing to     
                                                book           
                                                appointments   
                                                and the        
                                                current        
                                                process has    
                                                booking        
                                                problems.      

  Online payment  No             Out of scope   Online payment Exclude unless
                                                is not         the project
                                                mentioned and  scope is
                                                is beyond the  formally
                                                stated         expanded.
                                                patient,       
                                                practitioner   
                                                and            
                                                appointment    
                                                management     
                                                scope.         

  Practitioners   Yes            Confirmed      The            Keep as a
  view schedules                                stakeholder    functional
                                                analysis       requirement.
                                                identifies an  
                                                accurate,      
                                                up-to-date     
                                                practitioner   
                                                schedule as a  
                                                need.          

  AI recommends   No             Out of scope   This is a      Exclude from
  treatments                                    different type SmartCare.
                                                of system and  
                                                is not part of 
                                                the stated     
                                                clinic         
                                                management     
                                                problem.       

                                                               
  ---------------------------------------------------------------------------

Reflection:\
AI showed that my requirements were still a bit too vague to test. For
example, words such as \"fast\" and \"easy to use\" sound reasonable but
there would be no way to measure how the requirement would be met. AI
also highlighted that the exact staff role responsible for creating
appointments and the exact reports required by management still need
clarification. However, AI could also overreach and invent new things by
suggesting features such as SMS appointment reminders or online
payments. Despite being possible suggestions, they are not backed up by
the SmartCare client brief, so I rejected them rather than treating them
as requirements. After the review, I changed the reporting requirement
so that it only says the system should provide basic operational
appointment reports, while the exact report types remain an open
question. This avoids inventing details that the client has not
confirmed. Requirements need evidence because the software should be
based on real client and stakeholder needs. Without evidence,
assumptions can increase the scope and lead to building features that
the client did not request.