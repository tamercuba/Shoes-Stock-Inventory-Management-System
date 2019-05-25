from rest_framework import routers
from .viewsets import CalcadoViewSet

router = routers.DefaultRouter()
router.register(r'resources', CalcadoViewSet)
