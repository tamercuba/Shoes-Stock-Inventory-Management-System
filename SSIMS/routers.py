from rest_framework import routers
from api.viewsets import CalcadoViewSet

router = routers.DefaultRouter()
router.register(r'resources', CalcadoViewSet)
