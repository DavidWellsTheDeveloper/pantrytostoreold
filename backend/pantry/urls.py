from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'grocery', views.GroceryListViewSet, basename='Grocery')
router.register(r'myrecipes', views.SavedRecipesViewSet, basename='MyRecipes')
router.register(r'search', views.SearchViewset, basename='search')
urlpatterns = router.urls