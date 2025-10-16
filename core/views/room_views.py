from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from typing import List

# Entities
from core.domain.entities.room_entity import RoomEntity

# Services
from core.domain.usecases.room_service import RoomService

# Repository implementation
from core.infrastructure.repositories.room_repository import DjangoRoomRepository

# Schemas
from core.domain.schemas.room_schema import RoomSchema

# Inject repository into service
room_service = RoomService(repository=DjangoRoomRepository())

@extend_schema(tags=["Rooms"])
class RoomListCreateAPIView(APIView):
    def get(self, request):
        rooms: List[RoomEntity] = room_service.list_rooms()
        return Response([RoomSchema.model_validate(r).model_dump() for r in rooms])

    def post(self, request):
        try:
            room_data = RoomSchema.model_validate(request.data)
            room_entity = RoomEntity(**room_data.model_dump())
            created_room = room_service.create_room(room_entity)
            return Response(RoomSchema.model_validate(created_room).model_dump(), status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

@extend_schema(tags=["Rooms"])
class RoomRetrieveUpdateDeleteAPIView(APIView):
    def get(self, request, pk: int):
        room = room_service.get_room(pk)
        if not room:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(RoomSchema.model_validate(room).model_dump())

    def put(self, request, pk: int):
        try:
            room_data = RoomSchema.model_validate(id=pk, **request.data)
            room_entity = RoomEntity(room_data.model_dump())
            updated_room = room_service.update_room(room_entity)
            return Response(RoomSchema.model_validate(updated_room).model_dump(), status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, request, pk: int):
        room_service.delete_room(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
