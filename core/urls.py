from django.urls import path

# User Views
from core.views.user_views import (
    UserListCreateAPIView,
    UserRetrieveUpdateDeleteAPIView
)

# Team Views
from core.views.team_views import (
    TeamListCreateAPIView,
    TeamRetrieveUpdateDeleteAPIView
)

# Room Views
from core.views.room_views import (
    RoomListCreateAPIView,
    RoomRetrieveUpdateDeleteAPIView
)

# Booking Views
from core.views.booking_views import (
    BookingListCreateAPIView,
    BookingRetrieveUpdateDeleteAPIView
)

urlpatterns = [
    # User URLs
    path('users/', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDeleteAPIView.as_view(), name='user-detail'),

    # Team URLs
    path('teams/', TeamListCreateAPIView.as_view(), name='team-list-create'),
    path('teams/<int:pk>/', TeamRetrieveUpdateDeleteAPIView.as_view(), name='team-detail'),

    # Room URLs
    path('rooms/', RoomListCreateAPIView.as_view(), name='room-list-create'),
    path('rooms/<int:pk>/', RoomRetrieveUpdateDeleteAPIView.as_view(), name='room-detail'),

    # Booking URLs
    path('bookings/', BookingListCreateAPIView.as_view(), name='booking-list-create'),
    path('bookings/<int:pk>/', BookingRetrieveUpdateDeleteAPIView.as_view(), name='booking-detail'),
]
