from datetime import date
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor.get("name", "Visitor")}"
                                     f" is not vaccinated.")

        vaccine = visitor["vaccine"]
        if vaccine["expiration_date"] < date.today():
            raise OutdatedVaccineError(f"{visitor.get("name", "Visitor")}"
                                       f" is outdated.")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(f"{visitor.get("name", "Visitor")}"
                                      f" is not wearing mask.")

        return f"Welcome to {self.name}"
