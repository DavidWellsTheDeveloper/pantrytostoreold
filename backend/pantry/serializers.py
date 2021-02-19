# Create your views here.
from .models import GroceryListItem, Recipe, Ingredient, Instruction
from rest_framework import serializers


class GroceryListSerializer(serializers.ModelSerializer):
  class Meta:
    model = GroceryListItem
    fields = '__all__'


class IngredientSerializer(serializers.ModelSerializer):
  class Meta:
    model = Ingredient
    fields = '__all__'


class InstructionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Instruction
    fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Recipe
    fields = '__all__'
