from rest_framework import viewsets
from .models import Calcado, Estoque
from .serializers import CalcadoSerializer, EstoqueSerializer, EstoquePostSerializer
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

    custom_create:
    Adiciona uma instancia ao estoque (Verbo CREATE)

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
    filter_class = CalcadoFilter

    def get_serializer_class(self):
        if self.action == 'custom_create':
            return EstoquePostSerializer
        else:
            return CalcadoSerializer

    def custom_create(self, request, *args, **kwargs):
        data = {}

        data['id_calcado'] = kwargs['pk']
        data['tamanho'] = request.data.get('tamanho')
        data['quantidade'] = request.data.get('quantidade')

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        calcado_serializer = CalcadoSerializer(instance=self.get_object())
        #calcado_serializer = CalcadoSerializer(data=instance)
        # response_serializer.is_valid()
        return Response(calcado_serializer.data, status=status.HTTP_201_CREATED, headers=headers)
