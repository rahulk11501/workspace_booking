from typing import Protocol
from core.domain.entities.team_entity import TeamEntity
from .base_repository import BaseRepository

class TeamRepository(BaseRepository[TeamEntity], Protocol):
    pass
