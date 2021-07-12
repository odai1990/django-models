from django.urls import path
from django.urls import path
from .views import SnacksList,SnacksDetials

urlpatterns=[
    path('',SnacksList.as_view(),name='snacklist'),
    path('<int:pk>/',SnacksDetials.as_view(),name='snacksdetial'),
]
