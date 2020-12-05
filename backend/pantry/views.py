from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
import urllib
import requests
from .serializers import (
  GroceryListSerializer, 
  SavedRecipesSerializer,
)
from .models import (
  GroceryListItem, 
  SavedRecipes,
)

# Create your views here.
class GroceryListViewSet(viewsets.ModelViewSet):
  authentication_classes = [SessionAuthentication, TokenAuthentication, JWTAuthentication]
  serializer_class = GroceryListSerializer
  def get_queryset(self):
    user = self.request.user
    return GroceryListItem.objects.filter(user=user)

class SavedRecipesViewSet(viewsets.ModelViewSet):
  # permission_classes = [IsAuthenticated]
  authentication_classes = [SessionAuthentication, TokenAuthentication, JWTAuthentication]
  serializer_class = SavedRecipesSerializer
  def get_queryset(self):
    user = self.request.user
    if user.is_staff and self.request.GET.get('results') == "all":
      return SavedRecipes.objects.all()
    else:
      return SavedRecipes.objects.filter(user=user)
  def list(self, request):
    user = self.request.user
    ids = []
    url = 'https://api.spoonacular.com/recipes/informationBulk'
    apiKey = '5e819bee625f4a3b8572dde36611f257'
    recipes = SavedRecipes.objects.filter(user=user)
    for recipe in recipes:
      ids.append(recipe.recipe_id)
    idstring = ','.join(ids)
    print(idstring)
    queryDict = {}
    queryDict['apiKey'] = apiKey
    queryDict['ids'] = idstring
    print(type(queryDict))
    response = requests.get(url, params=queryDict)
    return JsonResponse(response.json(), safe=False)



class SearchViewset(viewsets.GenericViewSet):

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
