from django.contrib import admin
from .models import Sapato

class SapatoAdmin(admin.ModelAdmin):
    list_display  = ['descricao', 'quantidade', 'numeracao', 'preco_custo', 'preco_venda']
    search_fields = list_display
    ordering      = ['quantidade', 'descricao']

admin.site.register(Sapato, SapatoAdmin)
