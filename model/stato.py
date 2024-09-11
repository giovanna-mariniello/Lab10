from dataclasses import dataclass


@dataclass
class Stato:
    StateAbb: str
    CCode: int
    StateNme: str

    def __hash__(self):
        return hash(self.CCode)

    def __str__(self):
        return self.StateNme