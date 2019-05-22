from rest_framework import routers
from api.viewsets import SapatoViewSet

router = routers.DefaultRouter()
router.register(r'resources', SapatoViewSet)
