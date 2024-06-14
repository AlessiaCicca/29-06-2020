from dataclasses import dataclass

@dataclass
class Partita:
    MatchID: int
    TeamHomeID: int
    TeamAwayID: int
    TeamHomeFormation: int
    TeamAwayFormation: int
    ResultOfTeamHome: int
    Date: str



    def __hash__(self):
            return hash(self.MatchID)
    def __str__(self):
        return f"[{self.MatchID}] {self.TeamHomeID} vs {self.TeamAwayID}"