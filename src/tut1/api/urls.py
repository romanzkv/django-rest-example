from django.urls import path, include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'people', views.PeopleViewSet)

urlpatterns = [
    # path('', views.getPeople),
    # path('create/', views.addPeople),
    path('', include(router.urls)),
]
