from dataclasses import dataclass

@dataclass
class Stato:
    StateAbb: str
    CCode: int
    StateNme: str

    @property
    def StateAbb(self):
        return self.StateAbb

    @property
    def CCode(self):
        return self.CCode

    @property
    def StateNme(self):
        return self.StateNme

    def __hash__(self):
        return hash(self.CCode)

    def __str__(self):
        return f"{self.StateNme}"