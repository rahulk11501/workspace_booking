from typing import List, Optional
from core.domain.entities.user_entity import UserEntity
from core.domain.repositories.user_repository import UserRepository

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def get_user(self, user_id: int) -> Optional[UserEntity]:
        return self.repository.get(user_id)

    def list_users(self) -> List[UserEntity]:
        return self.repository.list()

    def create_user(self, user: UserEntity) -> UserEntity:
        return self.repository.create(user)

    def update_user(self, user: UserEntity) -> UserEntity:
        return self.repository.update(user)

    def delete_user(self, user_id: int) -> None:
        self.repository.delete(user_id)
