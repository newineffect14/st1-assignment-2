# stage 4 lab, step F
# manual behaviour checks
# 1 -> create valid objects
# 2 -> test invalid input
# 3 -> cancel a scheduled appointment
# 4 -> attempt an illegal repeated transition (cancel twice)
# 5 -> duplicate check (cancelled appointment should not block the slot)
# 6 -> try to change status directly (should not be allowed)

from datetime import datetime

from patient import Patient
from practitioner import Practitioner
from appointment import Appointment, AppointmentStatus, InvalidTransitionError


print("Test 1 - create valid objects")
print("__" * 20)
patient: Patient = Patient("P001", "Anna Smith")
practitioner: Practitioner = Practitioner("D001", "Dr Lee", "GP")
booking_time: datetime = datetime(2026, 10, 1, 9, 0)
appointment: Appointment = Appointment("A001", patient, practitioner, booking_time)
print(f"{patient.name = }")
print(f"{practitioner.specialty = }")
print(f"{appointment.status = }")
print()

print("Test 2 - invalid input")
print("__" * 20)
try:
    Patient("P002", "   ") # empty name
    print("FAIL - empty name was accepted")
except ValueError as error:
    print(f"PASS - {error}")

try:
    Practitioner("D002", "Dr Kim", "") # empty specialty
    print("FAIL - empty specialty was accepted")
except ValueError as error:
    print(f"PASS - {error}")

try:
    Appointment("A002", patient, practitioner, "1st October") # date as text, not datetime
    print("FAIL - text date was accepted")
except TypeError as error:
    print(f"PASS - {error}")
print()

print("Test 3 - cancel a scheduled appointment")
print("__" * 20)
print(f"{appointment.is_duplicate(practitioner, booking_time) = }") # True before cancelling
appointment.cancel()
print(f"{appointment.status = }")
if appointment.status == AppointmentStatus.CANCELLED:
    print("PASS - appointment cancelled and object still exists")
else:
    print("FAIL - status did not change")
print()

print("Test 4 - illegal repeated transition (cancel twice)")
print("__" * 20)
try:
    appointment.cancel()
    print("FAIL - appointment was cancelled twice")
except InvalidTransitionError as error:
    print(f"PASS - {error}")
print()

print("Test 5 - duplicate check after cancelling")
print("__" * 20)
print(f"{appointment.is_duplicate(practitioner, booking_time) = }")
if not appointment.is_duplicate(practitioner, booking_time):
    print("PASS - cancelled appointment does not block the slot")
else:
    print("FAIL - cancelled appointment still blocks the slot")
print()

print("Test 6 - change status directly")
print("__" * 20)
try:
    appointment.status = AppointmentStatus.SCHEDULED # should not be allowed
    print("FAIL - status was changed from outside")
except AttributeError:
    print("PASS - status is read only")