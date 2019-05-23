from rest_framework import viewsets
from .models import Calcado
from .serializers import CalcadoSerializer
from .filters import CalcadoFilter

class CalcadoViewSet(viewsets.ModelViewSet):
    ''' VIEWSET CALÇADO '''

    queryset = Calcado.objects.all()
    serializer_class = CalcadoSerializer
    filter_class = CalcadoFilter
