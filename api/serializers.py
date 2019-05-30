from rest_framework import serializers
from .models import Calcado, Estoque, File

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File 
        fields = ['file']

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

    def create(self, validated_data):
        estoque_data = validated_data.pop('estoque')
        calcado      = Calcado.objects.create(**validated_data)
        for data in estoque_data:
            calcado.estoque.create(**data)
        return calcado


    def update(self, instance, validated_data):
        instance.descricao   = validated_data.get(
            'descricao', instance.descricao)
        instance.fornecedor  = validated_data.get(
            'fornecedor', instance.fornecedor)
        instance.tipo        = validated_data.get('tipo', instance.tipo)
        instance.preco_custo = validated_data.get(
            'preco_custo', instance.preco_custo)
        instance.preco_venda = validated_data.get(
            'preco_venda', instance.preco_venda)

        estoque      = instance.estoque.all()
        estoque_data = validated_data.get('estoque', [])

        for item_data in estoque_data:
            item_tamanho = item_data.get('tamanho', None)
            if estoque.filter(tamanho=item_tamanho):
                item_db            = estoque.get(tamanho=item_tamanho)
                item_db.tamanho    = item_data.get('tamanho', item_db.tamanho)
                item_db.quantidade = item_data.get('quantidade',item_db.quantidade)
                if item_db.quantidade == 0:
                    item_db.delete()
                else:
                    item_db.save()
            else:
                Estoque.objects.create(
                    id_calcado = instance,
                    tamanho    = item_data['tamanho'],
                    quantidade = item_data['quantidade']
                )
        instance.save()
        return instance

    class Meta:
        model = Calcado
        fields = ['_id','descricao', 'fornecedor', 'tipo', 'preco_custo','preco_venda','quantidade_total', 'estoque']
