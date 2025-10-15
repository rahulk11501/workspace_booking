from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from typing import List
from datetime import datetime

# Entities
from core.domain.entities.booking_entity import BookingEntity
from core.domain.entities.user_entity import UserEntity
from core.domain.entities.team_entity import TeamEntity
from core.domain.entities.room_entity import RoomEntity

# Services
from core.domain.usecases.booking_service import BookingService

# Repository implementation
from core.infrastructure.repositories.booking_repository import DjangoBookingRepository

# Schemas
from core.domain.schemas.booking_schema import BookingSchema

# Inject repository into service
booking_service = BookingService(repository=DjangoBookingRepository())

@extend_schema(tags=["Bookings"])
class BookingListCreateAPIView(APIView):
    def get(self, request):
        bookings: List[BookingEntity] = booking_service.list_bookings()
        return Response([BookingSchema.model_validate(b).model_dump() for b in bookings])

    def post(self, request):
        data = request.data

        user = UserEntity(**data["user"]) if data.get("user") else None
        team = TeamEntity(**data["team"]) if data.get("team") else None
        room = RoomEntity(**data["room"])

        booking_entity = BookingEntity(
            id=None,
            room=room,
            user=user,
            team=team,
            slot_start=datetime.fromisoformat(data["slot_start"]),
            slot_end=datetime.fromisoformat(data["slot_end"]),
            created_at=datetime.fromisoformat(data["created_at"]) if data.get("created_at") else None
        )

        created_booking = booking_service.create_booking(booking_entity)
        return Response(BookingSchema.model_validate(created_booking).model_dump(), status=status.HTTP_201_CREATED)

@extend_schema(tags=["Bookings"])
class BookingRetrieveUpdateDeleteAPIView(APIView):
    def get(self, request, pk: int):
        booking = booking_service.get_booking(pk)
        if not booking:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(BookingSchema.model_validate(booking).model_dump())

    def put(self, request, pk: int):
        data = request.data

        user = UserEntity(**data["user"]) if data.get("user") else None
        team = TeamEntity(**data["team"]) if data.get("team") else None
        room = RoomEntity(**data["room"])

        booking_entity = BookingEntity(
            id=pk,
            room=room,
            user=user,
            team=team,
            slot_start=datetime.fromisoformat(data["slot_start"]),
            slot_end=datetime.fromisoformat(data["slot_end"]),
            created_at=datetime.fromisoformat(data["created_at"]) if data.get("created_at") else None
        )

        updated_booking = booking_service.update_booking(booking_entity)
        return Response(BookingSchema.model_validate(updated_booking).model_dump())

    def delete(self, request, pk: int):
        booking_service.delete_booking(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
