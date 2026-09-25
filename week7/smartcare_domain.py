from datetime import datetime # used for the appointment date and time
from enum import Enum # used for the appointment status


# B - Patient

class Patient:
    """
    A patient at the SmartCare clinic
    :param patient_id: unique id for the patient
    :param name: patient's name, must not be empty
    """

    def __init__(self, patient_id: str, name: str) -> None:
        # input validation -> id must be text and not empty
        if not isinstance(patient_id, str) or patient_id.strip() == "":
            raise ValueError("patient_id must be a non-empty string")

        self._patient_id: str = patient_id # private, set once at creation
        self._name: str = name # private, checked by validate()

        if not self.validate(): # stop the object being made with a bad name
            raise ValueError("name must be a non-empty string")

    @property
    def patient_id(self) -> str:
        return self._patient_id # read only, no setter

    @property
    def name(self) -> str:
        return self._name # read only, no setter

    def validate(self) -> bool:
        """
        Check the patient's name is valid
        :return: True if name is a non-empty string, otherwise False
        """
        return isinstance(self._name, str) and self._name.strip() != ""


# C - Practitioner

class Practitioner:
    """
    A practitioner (e.g. doctor) at the SmartCare clinic
    :param practitioner_id: unique id for the practitioner
    :param name: practitioner's name
    :param specialty: area the practitioner works in, e.g. "GP"
    """

    def __init__(self, practitioner_id: str, name: str, specialty: str) -> None:
        # input validation -> all 3 fields must be text and not empty
        if not isinstance(practitioner_id, str) or practitioner_id.strip() == "":
            raise ValueError("practitioner_id must be a non-empty string")
        if not isinstance(name, str) or name.strip() == "":
            raise ValueError("name must be a non-empty string")
        if not isinstance(specialty, str) or specialty.strip() == "":
            raise ValueError("specialty must be a non-empty string")

        # private, set once and never changed (no setters)
        self._practitioner_id: str = practitioner_id
        self._name: str = name
        self._specialty: str = specialty

    @property
    def practitioner_id(self) -> str:
        return self._practitioner_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def specialty(self) -> str:
        return self._specialty


# D - Appointment

class AppointmentStatus(Enum):
    # enum instead of a raw string like "cancelled" -> no typos possible
    SCHEDULED = "scheduled"
    CANCELLED = "cancelled"


class InvalidTransitionError(Exception):
    """Raised when an appointment status change is not allowed"""


class Appointment:
    """
    A booking between a Patient and a Practitioner (association, not inheritance)
    Cancelled appointments stay as objects, they are never deleted
    :param appointment_id: unique id for the appointment
    :param patient: the Patient being booked
    :param practitioner: the Practitioner being booked
    :param date_time: date and time of the appointment
    """

    def __init__(self, appointment_id: str, patient: Patient,
                 practitioner: Practitioner, date_time: datetime) -> None:
        # input validation -> check each value is the right type
        if not isinstance(appointment_id, str) or appointment_id.strip() == "":
            raise ValueError("appointment_id must be a non-empty string")
        if not isinstance(patient, Patient):
            raise TypeError("patient must be a Patient")
        if not isinstance(practitioner, Practitioner):
            raise TypeError("practitioner must be a Practitioner")
        if not isinstance(date_time, datetime):
            raise TypeError("date_time must be a datetime")

        self._appointment_id: str = appointment_id
        self._patient: Patient = patient
        self._practitioner: Practitioner = practitioner
        self._date_time: datetime = date_time
        self._status: AppointmentStatus = AppointmentStatus.SCHEDULED # every new booking starts as scheduled

    @property
    def appointment_id(self) -> str:
        return self._appointment_id

    @property
    def patient(self) -> Patient:
        return self._patient

    @property
    def practitioner(self) -> Practitioner:
        return self._practitioner

    @property
    def date_time(self) -> datetime:
        return self._date_time

    @property
    def status(self) -> AppointmentStatus:
        return self._status # read only -> status can only change inside cancel()

    def cancel(self) -> None:
        """
        Cancel the appointment
        Only SCHEDULED -> CANCELLED is allowed
        :return: None
        """
        if self._status != AppointmentStatus.SCHEDULED: # e.g. already cancelled
            raise InvalidTransitionError(
                f"Cannot cancel appointment {self._appointment_id}, status is {self._status.name}"
            )
        self._status = AppointmentStatus.CANCELLED # object is kept, just marked cancelled

    def is_duplicate(self, practitioner: Practitioner, date_time: datetime) -> bool:
        """
        Check if this appointment already books the practitioner at that time
        :param practitioner: practitioner for the new booking
        :param date_time: date and time for the new booking
        :return: True if it clashes, otherwise False (cancelled ones don't clash)
        """
        same_practitioner: bool = self._practitioner.practitioner_id == practitioner.practitioner_id
        same_time: bool = self._date_time == date_time
        still_scheduled: bool = self._status == AppointmentStatus.SCHEDULED

        return same_practitioner and same_time and still_scheduled


# quick check -> only runs when this file is run directly, not when imported
if __name__ == "__main__":
    patient: Patient = Patient("P001", "Anna Smith")
    practitioner: Practitioner = Practitioner("D001", "Dr Lee", "GP")
    booking_time: datetime = datetime(2026, 10, 1, 9, 0)

    appointment: Appointment = Appointment("A001", patient, practitioner, booking_time)
    print(f"{appointment.status = }")
    print(f"{appointment.is_duplicate(practitioner, booking_time) = }")

    appointment.cancel()
    print(f"{appointment.status = }")
    print(f"{appointment.is_duplicate(practitioner, booking_time) = }")