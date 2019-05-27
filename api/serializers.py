from rest_framework import serializers
from .models import Calcado, Estoque

class EstoqueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Estoque
        fields = ['tamanho', 'quantidade']

class EstoquePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Estoque
        fields = ['id_calcado','tamanho', 'quantidade']

class CalcadoSerializer(serializers.ModelSerializer):
    '''
    CALÇADO SERIALIZER

    Responsável por traduzir as informações do
    modelo Django para dados tipo Python nativo,
    para depois serem convertidos em formato JSON.
    '''
    estoque = EstoqueSerializer(many=True, read_only=True)

    class Meta:
        model = Calcado
        fields = ['_id','descricao', 'fornecedor', 'tipo', 'preco_custo','preco_venda','quantidade_total', 'estoque']
