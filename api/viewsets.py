from rest_framework import viewsets
from .models import Calcado
from .serializers import CalcadoSerializer, EstoqueSerializer, EstoquePostSerializer
from .filters import CalcadoFilter
from rest_framework.response import Response
from rest_framework import status

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

    def custom_create(self, request, *args, **kwargs):
        data = {}

        data['tamanho'] = request.data.get('tamanho')
        data['quantidade'] = request.data.get('quantidade')
        data['id_calcado'] = kwargs['pk']

        custom_serializer = EstoquePostSerializer(data=data)
        custom_serializer.is_valid(raise_exception=True)
        self.perform_create(custom_serializer)
        headers = self.get_success_headers(custom_serializer.data)
        return Response(custom_serializer.data, status=status.HTTP_201_CREATED, headers=headers)
