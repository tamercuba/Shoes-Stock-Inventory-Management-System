from rest_framework import serializers
from .models import Calcado, Estoque

class EstoqueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Estoque
        fields = ['tamanho', 'quantidade']

class CalcadoSerializer(serializers.ModelSerializer):
    '''
    CALÇADO SERIALIZER

    Responsável por traduzir as informações do
    modelo Django para dados tipo Python nativo,
    para depois serem convertidos em formato JSON.
    '''

    estoque = EstoqueSerializer(many=True)
    #numeracao = NumeracaoSerializer(many=True, queryset=Numeracao.objects.all())
    #numeracao = serializers.ReadOnlyField()
    #numeracao = serializers.RelatedField(many=True, read_only=True)

    class Meta:
        model = Calcado
        fields = ['_id','descricao', 'fornecedor', 'tipo', 'quantidade_total', 'estoque']
