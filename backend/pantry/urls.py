from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'grocery', views.GroceryListViewSet, basename='Grocery')
router.register(r'myrecipes', views.RecipeViewSet, basename='MyRecipes')
router.register(r'ingredients', views.IngredientViewset, basename='Ingredients')
router.register(r'instructions', views.InstructionViewset, basename='Instructions')
urlpatterns = router.urls
urlpatterns.append(path(r'extractrecipe/', views.ExtractRecipe.as_view()))