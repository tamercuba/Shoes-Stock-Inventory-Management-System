from django.contrib import admin
from .models import Calcado, Estoque, File

class CalcadoAdmin(admin.ModelAdmin):
    '''
    MODEL ADMIN DE CALCADO

    Classe resposável por cadastrar
    o modelo calcado na interface de
    administrador nativa do Django.
    '''
    list_display  = ['descricao', 'preco_custo', 'preco_venda']
    search_fields = list_display
    ordering      = ['descricao']

class EstoqueAdmin(admin.ModelAdmin):
    list_display = ['_descricao', 'tamanho','quantidade' ,'_id']

admin.site.register(Calcado, CalcadoAdmin)
admin.site.register(Estoque, EstoqueAdmin)