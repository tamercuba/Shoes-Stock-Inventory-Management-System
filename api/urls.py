from django.contrib import admin
from django.urls import path, include
from .routers import router
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.index, name='index'),
    path('', include(router.urls)),
]
