from rest_framework import viewsets
from .models import Calcado, Estoque
from .serializers import CalcadoSerializer, EstoqueSerializer
from .filters import CalcadoFilter
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import action

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

    destroy:
    Deleta os dados de uma instância de calçado (Verbo DELETE)
    '''

    queryset = Calcado.objects.all()
    serializer_class = CalcadoSerializer
    filter_class = CalcadoFilter
