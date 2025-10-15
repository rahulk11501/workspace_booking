from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from typing import List

# Entities
from core.domain.entities.user_entity import UserEntity

# Services
from core.domain.usecases.user_service import UserService

# Repository implementation
from core.infrastructure.repositories.user_repository import DjangoUserRepository

# Schemas
from core.domain.schemas.user_schema import UserSchema

# Inject repository into service
user_service = UserService(repository=DjangoUserRepository())

@extend_schema(tags=["Users"])
class UserListCreateAPIView(APIView):
    def get(self, request):
        users: List[UserEntity] = user_service.list_users()
        return Response([UserSchema.model_validate(u).model_dump() for u in users])

    def post(self, request):
        data = request.data
        user_entity = UserEntity(
            id=None,
            name=data["name"],
            age=data["age"],
            gender=data["gender"]
        )
        created_user = user_service.create_user(user_entity)
        return Response(UserSchema.model_validate(created_user).model_dump(), status=status.HTTP_201_CREATED)

@extend_schema(tags=["Users"])
class UserRetrieveUpdateDeleteAPIView(APIView):
    def get(self, request, pk: int):
        user = user_service.get_user(pk)
        if not user:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(UserSchema.model_validate(user).model_dump())

    def put(self, request, pk: int):
        data = request.data
        user_entity = UserEntity(
            id=pk,
            name=data["name"],
            age=data["age"],
            gender=data["gender"]
        )
        updated_user = user_service.update_user(user_entity)
        return Response(UserSchema.model_validate(updated_user).model_dump())

    def delete(self, request, pk: int):
        user_service.delete_user(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
