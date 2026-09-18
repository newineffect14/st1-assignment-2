# SmartCare v0.3 - Domain model skeletons (Week 6)
# structural skeletons only - Part H says do not implement full behaviour yet
# type hints, docstrings and constants follow the same style used in the
# weekly tutorials (input/operators, conditions, loops, functions)

from typing import Final

BOOKED: Final[str] = "booked"       # constant instead of magic string
CANCELLED: Final[str] = "cancelled"


class Patient:
    """Owns patient identity and basic self-validation. FR-02, FR-07, FR-09."""

    def __init__(self, patient_id: str, name: str) -> None:
        self.patient_id: str = patient_id
        self.name: str = name

    def validate(self) -> bool:
        """
        Check that required identity fields are present.
        :return: True if patient_id and name are both non-empty
        """
        return bool(self.patient_id) and bool(self.name)


class Practitioner:
    """Owns practitioner identity and specialty. FR-10."""

    def __init__(self, practitioner_id: str, name: str, specialty: str) -> None:
        self.practitioner_id: str = practitioner_id
        self.name: str = name
        self.specialty: str = specialty


class Appointment:
    """
    Owns the booking relationship, status and duplicate check.
    FR-01, FR-03, FR-04, FR-08, FR-11, NFR-01.
    """

    def __init__(
        self,
        appointment_id: str,
        patient: Patient,
        practitioner: Practitioner,
        date_time: str,
        status: str = BOOKED,
    ) -> None:
        self.appointment_id: str = appointment_id
        self.patient: Patient = patient
        self.practitioner: Practitioner = practitioner
        self.date_time: str = date_time
        self.status: str = status

    def cancel(self) -> None:
        """
        Mark the appointment cancelled without deleting the record.
        :return: None
        """
        self.status = CANCELLED

    def is_duplicate(self, practitioner: Practitioner, date_time: str) -> bool:
        """
        Check whether this appointment clashes with a proposed practitioner/timeslot.
        :param practitioner: the practitioner being checked against
        :param date_time: the proposed date/time being checked against
        :return: True if this is an active booking for the same practitioner and time
        """
        return (
            self.practitioner is practitioner
            and self.date_time == date_time
            and self.status != CANCELLED
        )


# quick manual check - not full behaviour, just confirms the skeleton runs
if __name__ == "__main__":
    patient: Patient = Patient(patient_id="P001", name="Jane Doe")
    practitioner: Practitioner = Practitioner(
        practitioner_id="PR001", name="Dr Smith", specialty="GP"
    )
    appointment: Appointment = Appointment(
        appointment_id="A001",
        patient=patient,
        practitioner=practitioner,
        date_time="2026-09-20 10:00",
    )

    print(patient.validate())
    print(appointment.status)
    appointment.cancel()
    print(appointment.status)