# SmartCare v0.1 - Initial Engineering Brief and AI Activity Card

## 1. Problem summary

SmartCare Community Clinic currently manages patients and appointments using spreadsheets and paper records. This makes it hard to see the avaliability of a practitioner, which then leads to duplicate bookings and lost patient records, and additionally means that patient information is spread across multiple places with no organisation. More operational issues include having inconsistent appointment status info, a lack of reliable appointment history, manual cancellation processes, and difficulty producing basic operational reports. The client has asked for a simple software to help manage patients, practitioners and appointments, and for it to be a concise application suitable for a small clinic. 
## 2. Initial stakeholders

| Stakeholder | Possible need |
|---|---|
| Receptionist | Quickly book, view, change and cancel appointments without double-booking |
| Practitioner (doctor/nurse) | See their daily schedule and which patient is next |
| Patient | Get a confirmed appointment time and not be double-booked or lost in the system |
| Clinic manager | Reports on appointment volume, no-shows and practitioner workload; control costs |
| IT / system administrator | Secure, maintainable system with backups and user access control |

## 3. Initial features

| Feature | Confirmed or provisional? | Why? |
|---|---|---|
| Book an appointment (patient, practitioner, time) | Confirmed | Client explicitly mentions managing appointments |
| Store patient records | Confirmed | Client explicitly mentions managing patients |
| Store practitioner details | Confirmed | Client explicitly mentions practitioners |
| View practitioner schedule | Provisional | Logical need, but not stated by the client |
| Prevent double bookings | Provisional | Likely problem with spreadsheets, needs confirming |
| Cancel/reschedule appointments | Provisional | Common need, not yet stated |

## 4. Questions for the client

1. Who will use the system; reception only, or practitioners and patients too?
2. How long is a standard appointment, and are there different appointment types?
3. What are each practitioner's working hours and days?
4. What patient details must be recorded (contact info, date of birth, Medicare number)?
5. Should appointments be cancellable or reschedulable, and should patients be notified?

## 5. What we do not yet know

1. What privacy and security requirements apply to patient health information.
2. How many patients, practitioners and appointments per day the system must handle.
3. Whether existing spreadsheet data must be imported into the new system.