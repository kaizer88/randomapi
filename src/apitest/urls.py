from django.urls import path, include
from .views import Randomapi

urlpatterns = [

    path('', Randomapi.as_view(), name='aaa'),
]