from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializers import UserSerializer

# Create your views here.


class UserDetail(viewsets.ModelViewSet):
  permission_classes = [IsAuthenticated]
  serializer_class = UserSerializer

  def get_queryset(self):
    user = self.request.user
    return User.objects.filter(username=user.username)

  def list(self, request, *args, **kwargs):
    instance = request.user
    serializer = self.get_serializer(instance)
    return Response(serializer.data)