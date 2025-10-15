from typing import Protocol
from core.domain.entities.user_entity import UserEntity
from .base_repository import BaseRepository

class UserRepository(BaseRepository[UserEntity], Protocol):
    pass
