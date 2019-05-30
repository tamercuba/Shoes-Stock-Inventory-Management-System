from .viewsets import CalcadoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'resources', CalcadoViewSet)
