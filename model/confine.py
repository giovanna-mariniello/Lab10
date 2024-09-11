from dataclasses import dataclass
from model.stato import Stato

@dataclass
class Confine:
    s1: Stato
    s2: Stato

    @property
    def get_s1(self):
        return self.s1

    @property
    def get_s2(self):
        return self.s2

    def __hash__(self):
        return hash((self.s1.CCode, self.s2.CCode))

    def __str__(self):
        return f"Confine: {self.s1} - {self.s2}"

