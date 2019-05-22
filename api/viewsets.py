from rest_framework import viewsets
from .models import Sapato
from .serializers import SapatoSerializer

class SapatoViewSet(viewsets.ModelViewSet):
    ''' VIEWSET SAPATO '''
    queryset = Sapato.objects.all()
    serializer_class = SapatoSerializer
    search_fields = '__all__'
