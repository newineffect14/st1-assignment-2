# Patient; stage 4 lab, step B

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


# quick check -> only runs when this file is run directly
if __name__ == "__main__":
    patient: Patient = Patient("P001", "Anna Smith")
    print(f"{patient.patient_id = }")
    print(f"{patient.name = }")
    print(f"{patient.validate() = }")