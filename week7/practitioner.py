#  Practitioner; stage 4 lab, step C

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


# quick check -> only runs when this file is run directly
if __name__ == "__main__":
    practitioner: Practitioner = Practitioner("D001", "Dr Lee", "GP")
    print(f"{practitioner.practitioner_id = }")
    print(f"{practitioner.name = }")
    print(f"{practitioner.specialty = }")