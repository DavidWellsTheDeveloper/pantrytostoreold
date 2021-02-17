from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth import get_user_model

# Create your views here.


class UserDetail(viewsets.ModelViewSet):
  permission_classes = [IsAuthenticated]
  authentication_classes = [SessionAuthentication, TokenAuthentication, JWTAuthentication]
  serializer_class = UserSerializer

  def get_queryset(self):
    user = self.request.user
    return User.objects.filter(username=user.username)

  def list(self, request, *args, **kwargs):
    instance = request.user
    serializer = self.get_serializer(instance)
    return Response(serializer.data)

class CreateUserView(CreateAPIView):
  permission_classes = [AllowAny]
  model = get_user_model()
  serializer_class = UserSerializer