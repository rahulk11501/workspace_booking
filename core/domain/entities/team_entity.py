from dataclasses import dataclass, field
from typing import List, Optional
from .user_entity import UserEntity

@dataclass(frozen=True)
class TeamEntity:
    name: str
    members: List[UserEntity] = field(default_factory=list)
    id: Optional[int] = None
