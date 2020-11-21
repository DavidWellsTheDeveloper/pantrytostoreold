# Create your views here.
from .models import GroceryListItem, SavedRecipes
from rest_framework import serializers

class GroceryListSerializer(serializers.ModelSerializer):
  class Meta:
    model = GroceryListItem
    fields = '__all__'

class SavedRecipesSerializer(serializers.ModelSerializer):
  class Meta:
    model = SavedRecipes
    fields = '__all__'