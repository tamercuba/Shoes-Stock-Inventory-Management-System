# from rest_framework import routers
from .viewsets import CalcadoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'resources', CalcadoViewSet)
