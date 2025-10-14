from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models.user import User
from core.serializers.user_serializer import UserSerializer

class UserCreateAPIView(APIView):
    """
    post:
    Create a new user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
