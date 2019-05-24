from rest_framework import viewsets
from .models import Calcado, Numeracao
from .serializers import CalcadoSerializer, NumeracaoSerializer
from .filters import CalcadoFilter

class CalcadoViewSet(viewsets.ModelViewSet):
    '''
    VIEWSET CALÇADO

    Viewset responsável pela endpoint /resources, supre
    todos os verbos HTTP utilizando os seguintes métodos:

    create:
    Adiciona um novo calçado (Verbo CREATE)

    list:
    Retorna uma lista de todos os calçados (Verbo GET)

    partial_update:
    Atualiza parcialmente uma instância de calçado (Verbo PATCH)

    retrieve:
    Retorna uma instância de calçado, dado um id (Verbo GET)

    update:
    Atualiza os dados de uma instância de calçado (Verbo UPDATE)
    '''

    queryset = Calcado.objects.all()
    serializer_class = CalcadoSerializer
    filter_class = CalcadoFilter
