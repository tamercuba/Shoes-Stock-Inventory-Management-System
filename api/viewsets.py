from rest_framework          import viewsets
from .models                 import Calcado, File
from .serializers            import CalcadoSerializer, FileSerializer
from .filters                import CalcadoFilter
from rest_framework.response import Response

import csv
import os
from rest_framework.parsers import FileUploadParser
from rest_framework.views   import APIView
from rest_framework import status
from datetime import datetime


NUMERACAO_CHOICES = [num for num in range(35,46,1)]

class FileUploadView(APIView):

    '''
    Recebe via POST um arquivo CSV com dados para inserção,
    estruturados da seguinte maneira:

    Descrição,Fornecedor,Tipo,Preco de Custo,Preco de Venda,
    Total,35,36,37,38,39,40,41,42,43,44,45, (Porcentagem em estoque referente ao Total)
    
    O ARQUIVO DEVE TER O NOME 'data.csv'!
    '''

    parser_class = (FileUploadParser,)
    
    def post(self, request, *args, **kwargs):
        
        try:
            file_serializer = FileSerializer(data=request.data)
            if file_serializer.is_valid():
                file_serializer.save()
                self.adiciona_items()
                self.remove_arquivo()
                return Response(
                    file_serializer.data, status=status.HTTP_201_CREATED
                    )
            else:
                self.remove_arquivo()
                return Response(
                    file_serializer.errors, status=status.HTTP_400_BAD_REQUEST
                    )
        except Exception as e:
            return(Response(str(e)))


    def adiciona_items(self):
        
        '''
        Lê cada linha do arquivo csv e adiciona ao banco de dados
        '''

        with open('static/TEMP/data.csv', 'r+') as file:
            for row in csv.DictReader(file):
                data = {}
                data['descricao']   = row['descricao']
                data['fornecedor']  = row['fornecedor']
                data['tipo']        = row['tipo']
                data['preco_custo'] = row['preco_custo']
                data['preco_venda'] = row['preco_venda']
                if row['total'] != 0:
                    estoque = []
                    for num in NUMERACAO_CHOICES:
                        quantidade = round( 
                                float(row[str(num)]) * float(row['total'])
                            )
                        if quantidade != 0:
                            instancia = {
                                'tamanho': num,
                                'quantidade': quantidade
                            }
                            estoque.append(instancia)
                data['estoque'] = estoque
                serializer = CalcadoSerializer(data=data)
                serializer.is_valid(raise_exception=True)
                serializer.save()

    def remove_arquivo(self):
        '''
        Deleta o arquivo da maquina e do db
        '''
        os.remove('static/TEMP/data.csv')
        File.objects.all().get().delete()

            

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
        