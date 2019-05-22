from rest_framework import serializers
from .models import Sapato

class SapatoSerializer(serializers.ModelSerializer):
    ''' SAPATO SERIALIZER '''
    class Meta:
        model = Sapato
        fields = '__all__'
