from rest_framework import serializers
from .models import Calcado

class CalcadoSerializer(serializers.ModelSerializer):
    '''
    CALÇADO SERIALIZER

    Responsável por traduzir as informações do
    modelo Django para dados tipo Python nativo,
    para depois serem convertidos em formato JSON.
    '''
    class Meta:
        model = Calcado
        fields = '__all__'
