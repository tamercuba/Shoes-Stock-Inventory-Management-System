from django.contrib import admin
from .models import Calcado

class CalcadoAdmin(admin.ModelAdmin):
    '''
    MODEL ADMIN DE CALCADO

    Classe resposável por cadastrar
    o modelo calcado na interface de
    administrador nativa do Django.
    '''
    list_display  = ['descricao', 'quantidade', 'numeracao', 'preco_custo', 'preco_venda']
    search_fields = list_display
    ordering      = ['quantidade', 'descricao']

admin.site.register(Calcado, CalcadoAdmin)
