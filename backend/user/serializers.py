from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'username', 'first_name', 'last_name', 'email']
    
class UserSerializer(serializers.ModelSerializer):

  def create(self, validated_data):
    username = validated_data['username']
    password = validated_data['password']
    email = validated_data['email']
    first_name = validated_data['first_name']
    last_name = validated_data['last_name']
    user = User.objects.create_user(
      username, 
      email, 
      password, 
      first_name=first_name, 
      last_name=last_name
    )
    # user.set_password(validated_data['password'])
    user.save()

    return user

  class Meta:
    model = User
    # Tuple of serialized model fields (see link [2])
    fields = '__all__'
