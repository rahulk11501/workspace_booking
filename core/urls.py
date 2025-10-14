from django.urls import path
from core.views.user_views import UserCreateAPIView

urlpatterns = [
    path('users/', UserCreateAPIView.as_view(), name='user-create'),
]
