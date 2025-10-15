from typing import List, Optional
from core.domain.entities.user_entity import UserEntity
from core.domain.repositories.user_repository import UserRepository
from core.models.user import User as UserModel

class DjangoUserRepository(UserRepository):
    def get(self, obj_id: int) -> Optional[UserEntity]:
        obj = UserModel.objects.filter(id=obj_id).first()
        if not obj:
            return None
        return UserEntity(id=obj.id, name=obj.name, age=obj.age, gender=obj.gender)

    def list(self) -> List[UserEntity]:
        return [UserEntity(id=u.id, name=u.name, age=u.age, gender=u.gender) for u in UserModel.objects.all()]

    def create(self, entity: UserEntity) -> UserEntity:
        obj = UserModel.objects.create(name=entity.name, age=entity.age, gender=entity.gender)
        return UserEntity(id=obj.id, name=obj.name, age=obj.age, gender=obj.gender)

    def update(self, entity: UserEntity) -> UserEntity:
        obj = UserModel.objects.get(id=entity.id)
        obj.name, obj.age, obj.gender = entity.name, entity.age, entity.gender
        obj.save()
        return UserEntity(id=obj.id, name=obj.name, age=obj.age, gender=obj.gender)

    def delete(self, obj_id: int) -> None:
        UserModel.objects.filter(id=obj_id).delete()
