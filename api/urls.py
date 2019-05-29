from django.contrib import admin
from django.urls import path, include
from .routers import router

app_name = 'api'

urlpatterns = [
    path('', include(router.urls))
]
