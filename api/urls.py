from django.contrib import admin
from django.urls import path, include
from .routers import router
from .viewsets import FileUploadView

app_name = 'api'

urlpatterns = [
    path('resources/csv_import/', FileUploadView.as_view()),
    path('', include(router.urls))
]
