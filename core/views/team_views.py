from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from typing import List

# Entities
from core.domain.entities.team_entity import TeamEntity
from core.domain.entities.user_entity import UserEntity

# Services
from core.domain.usecases.team_service import TeamService

# Repository implementation
from core.infrastructure.repositories.team_repository import DjangoTeamRepository

# Schemas
from core.domain.schemas.team_schema import TeamSchema

# Inject repository into service
team_service = TeamService(repository=DjangoTeamRepository())


@extend_schema(tags=["Teams"])
class TeamListCreateAPIView(APIView):
    def get(self, request):
        teams: List[TeamEntity] = team_service.list_teams()
        return Response([TeamSchema.model_validate(t).model_dump() for t in teams])

    def post(self, request):
        try:
            team_data = TeamSchema.model_validate(request.data)
            members = [UserEntity(**m.model_dump()) for m in team_data.members]
            team_entity = TeamEntity(name=team_data.name, members=members)
            created_team = team_service.create_team(team_entity)
            return Response(
                TeamSchema.model_validate(created_team).model_dump(),
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=["Teams"])
class TeamRetrieveUpdateDeleteAPIView(APIView):
    def get(self, request, pk: int):
        team = team_service.get_team(pk)
        if not team:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(TeamSchema.model_validate(team).model_dump())

    def put(self, request, pk: int):
        try:
            team_data = TeamSchema.model_validate(request.data)
            members = [UserEntity(**m.model_dump()) for m in team_data.members]
            team_entity = TeamEntity(id=pk, name=team_data.name, members=members)
            updated_team = team_service.update_team(team_entity)
            return Response(TeamSchema.model_validate(updated_team).model_dump())
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk: int):
        team_service.delete_team(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
