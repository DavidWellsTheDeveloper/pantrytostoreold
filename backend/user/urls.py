from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserDetail, basename='Users')
urlpatterns = router.urls
urlpatterns.append(path('create/', views.CreateUserView.as_view(), name='user-create'))