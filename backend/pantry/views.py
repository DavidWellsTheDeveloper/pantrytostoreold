from rest_framework import viewsets, mixins, views, generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse, HttpResponse
from url_filter.integrations.drf import DjangoFilterBackend
import urllib
import requests
import scrape_schema_recipe

import json
from bs4 import BeautifulSoup

from .serializers import (
  GroceryListSerializer, 
  RecipeSerializer,
  IngredientSerializer,
  InstructionSerializer,
  ExtractSerializer,
)
from .models import (
  GroceryListItem, 
  Recipe,
  Ingredient,
  Instruction,
)

# Create your views here.
class GroceryListViewSet(viewsets.ModelViewSet):
  authentication_classes = [SessionAuthentication, TokenAuthentication, JWTAuthentication]
  serializer_class = GroceryListSerializer
  def get_queryset(self):
    user = self.request.user
    return GroceryListItem.objects.filter(user=user)

class RecipeViewSet(viewsets.ModelViewSet):
  authentication_classes = [SessionAuthentication, TokenAuthentication, JWTAuthentication]
  serializer_class = RecipeSerializer
  def get_queryset(self):
    user = self.request.user
    return Recipe.objects.filter(user=user)

class IngredientViewset(viewsets.ModelViewSet):
  authentication_classes = [SessionAuthentication, TokenAuthentication, JWTAuthentication]
  serializer_class = IngredientSerializer
  filter_backends = [DjangoFilterBackend]
  filter_fields = ['recipe', 'name']
  def get_queryset(self):
    return Ingredient.objects.all()

class InstructionViewset(viewsets.ModelViewSet):
  authentication_classes = [SessionAuthentication, TokenAuthentication, JWTAuthentication]
  serializer_class = InstructionSerializer
  filter_backends = [DjangoFilterBackend]
  filter_fields = ['recipe', 'instruction', 'step']
  def get_queryset(self):
    return Instruction.objects.all()

class SearchViewset(viewsets.GenericViewSet):
  authentication_classes = []
  def list(self, request):
    url = 'https://api.spoonacular.com/recipes/complexSearch'
    apiKey = '5e819bee625f4a3b8572dde36611f257'

    # build url params
    queryDict = {}
    queryDict['apiKey'] = apiKey
    queryDict['query'] = self.request.GET.get('query', '')
    queryDict['addRecipeInformation'] = self.request.GET.get('addRecipeInformation', True)
    queryDict['addRecipeNutrition'] = self.request.GET.get('addRecipeNutrition', False)
    queryDict['offset'] = self.request.GET.get('offset', '0')
    url_parse = urllib.parse.urlencode(queryDict)

    # Perform request
    response = requests.get(url, params=queryDict)
    return JsonResponse(response.json())


class ExtractRecipe(views.APIView):
  # @classmethod
  # def get_extra_actions(cls):
  #   return []
  
  authentication_classes = []
  def get(self, request):
    recipe_url = request.GET.get('url', None)
    if has_ld_json(recipe_url) == False:
      print('Recipe data not found')
      return HttpResponse('Recipe data not found')
    recipe_list = []
    try:
      recipe_list = scrape_schema_recipe.scrape_url(recipe_url, python_objects=True)
    except:
      return
    if len(recipe_list) != 1:
      return HttpResponse('Recipe data not found')
    recipe = recipe_list[0]
    return JsonResponse(recipe)

  def get_queryset(self):
    return Recipe.objects.all()

def has_ld_json(url: str) -> dict:
  parser = "html.parser"
  req = None
  try:
    req = requests.get(url, timeout=0.5)
  except requests.exceptions.RequestException as e:
    print(e)
    return False
  if req == None:
    return False
  soup = BeautifulSoup(req.text, parser)
  try:
    p = soup.find('script', type='application/ld+json')
  except:
    print(f'Exception')
  return p != None