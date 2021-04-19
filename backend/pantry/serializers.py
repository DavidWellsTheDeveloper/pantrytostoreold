# Create your views here.
from .models import GroceryListItem, Recipe, Ingredient, Instruction
from rest_framework import serializers
import scrape_schema_recipe


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

class ExtractSerializer(serializers.Serializer):

  
  def getRecipe(recipe_url):
    
    recipe_list = scrape_schema_recipe.scrape_url(recipe_url, python_objects=True)
    if len(recipe_list) != 1:
      raise serializers.UnsupportedMediaType
    recipe = recipe_list[0]
    print(recipe)
    return recipe

  def get(self, validated_data):
    user = self.request.user
    recipe = getRecipe(self.context['url'])
    # recipe_req_data = {'user':user, 'title':recipe['title']}

    # if recipe_serializer.is_valid():
    #   recipe_serializer.save()

    return recipe
