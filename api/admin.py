from django.contrib import admin
from .models import Calcado

class CalcadoAdmin(admin.ModelAdmin):
    list_display  = ['descricao', 'quantidade', 'numeracao', 'preco_custo', 'preco_venda']
    search_fields = list_display
    ordering      = ['quantidade', 'descricao']

admin.site.register(Calcado, CalcadoAdmin)
