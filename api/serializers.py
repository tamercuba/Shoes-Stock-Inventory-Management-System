from rest_framework import serializers
from .models import Calcado

class CalcadoSerializer(serializers.ModelSerializer):
    ''' CALÇADO SERIALIZER '''
    class Meta:
        model = Calcado
        fields = '__all__'
