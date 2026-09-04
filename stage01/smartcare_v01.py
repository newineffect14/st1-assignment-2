#quick notes
#Data to store: patient name, appointmet time, practitioner name, 
#useful functions: something to add an appointment, something to list them
#what could go wrong: duplicate bookings, missing fields, typos in names
#unclear requirements: no cancellation or reschedule appointment? no practioner ID?

# task1

print("Welcome to SmartCare: Community Clinic Appointment Booking System!")

# First Appointment
patient1_name = 'Alice Smith'
practitioner1_name = 'Dr. John Doe'
appointment1_time = '2024-07-20 10:00 AM'
print(f"Patient: {patient1_name} | Practitioner: {practitioner1_name} | Time: {appointment1_time}")

# Second Appointment
patient2_name = 'Bob Johnson'
practitioner2_name = 'Dr. Jane Roe'
appointment2_time = '2024-07-20 11:30 AM'
print(f"Patient: {patient2_name} | Practitioner: {practitioner2_name} | Time: {appointment2_time}")

#task1enhanced
# Use lists, dictionaries and functions to enhance the Python file

# Human-written version (PART G))

appointments = []

def book_appointment(patient_name, practitioner_name, appointment_time):
    if not patient_name:
        raise ValueError("Patient name cannot be empty")
    if not practitioner_name:
        raise ValueError("Practitioner name cannot be empty")

    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }
    appointments.append(appointment)

def display_appointments():
    if not appointments:
        print("No appointments recorded.")
        return
    for appointment in appointments:
        print(f"Patient: {appointment['patient']} | Practitioner: {appointment['practitioner']} | Time: {appointment['time']}")

print("Welcome to SmartCare: The Clinical Appointment Booking System!")
book_appointment('Alice Smith', 'Dr. John Doe', '2024-07-20 10:00 AM')
book_appointment('Bob Johnson', 'Dr. Jane Roe', '2024-07-20 11:30 AM')
display_appointments()


# 5 limitations of the Part A programs
# unlike the second, the first one doesnt have proper error messages
# theres no time clash check
# theres no check if a appointment is clashed at the same time as another
#  no input validation on the time format
#  no way to cancel an appointment
