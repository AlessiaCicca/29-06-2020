from dataclasses import dataclass

@dataclass
class Connessione:
    m1:int
    m2:int
    peso: int



    def __str__(self):
        return f"{self.m1} - {self.m2}"