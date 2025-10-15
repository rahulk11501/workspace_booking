from typing import List, Optional
from core.domain.entities.team_entity import TeamEntity
from core.domain.entities.user_entity import UserEntity
from core.domain.repositories.team_repository import TeamRepository
from core.models.team import Team as TeamModel

class DjangoTeamRepository(TeamRepository):
    def get(self, obj_id: int) -> Optional[TeamEntity]:
        obj = TeamModel.objects.filter(id=obj_id).first()
        if not obj:
            return None
        members = [UserEntity(id=m.id, name=m.name, age=m.age, gender=m.gender) for m in obj.members.all()]
        return TeamEntity(id=obj.id, name=obj.name, members=members)

    def list(self) -> List[TeamEntity]:
        teams = []
        for obj in TeamModel.objects.all():
            members = [UserEntity(id=m.id, name=m.name, age=m.age, gender=m.gender) for m in obj.members.all()]
            teams.append(TeamEntity(id=obj.id, name=obj.name, members=members))
        return teams

    def create(self, entity: TeamEntity) -> TeamEntity:
        obj = TeamModel.objects.create(name=entity.name)
        obj.members.set([m.id for m in entity.members])
        obj.save()
        members = [UserEntity(id=m.id, name=m.name, age=m.age, gender=m.gender) for m in obj.members.all()]
        return TeamEntity(id=obj.id, name=obj.name, members=members)

    def update(self, entity: TeamEntity) -> TeamEntity:
        obj = TeamModel.objects.get(id=entity.id)
        obj.name = entity.name
        obj.members.set([m.id for m in entity.members])
        obj.save()
        members = [UserEntity(id=m.id, name=m.name, age=m.age, gender=m.gender) for m in obj.members.all()]
        return TeamEntity(id=obj.id, name=obj.name, members=members)

    def delete(self, obj_id: int) -> None:
        TeamModel.objects.filter(id=obj_id).delete()
