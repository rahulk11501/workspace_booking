from typing import List, Optional
from core.domain.entities.team_entity import TeamEntity
from core.domain.repositories.team_repository import TeamRepository

class TeamService:
    def __init__(self, repository: TeamRepository):
        self.repository = repository

    def get_team(self, team_id: int) -> Optional[TeamEntity]:
        return self.repository.get(team_id)

    def list_teams(self) -> List[TeamEntity]:
        return self.repository.list()

    def create_team(self, team: TeamEntity) -> TeamEntity:
        return self.repository.create(team)

    def update_team(self, team: TeamEntity) -> TeamEntity:
        return self.repository.update(team)

    def delete_team(self, team_id: int) -> None:
        self.repository.delete(team_id)
