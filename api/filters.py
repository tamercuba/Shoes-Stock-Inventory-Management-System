import django_filters.rest_framework as filters
from .models import Calcado

class CalcadoFilter(filters.FilterSet):
    '''
    FILTRO CALCADO

    ll      : looks like
    gt/lt   : greater/lesser than
    gte/lte : greater/lesser than or equal
    '''
    fornecedor__ll = filters.CharFilter(field_name='fornecedor', lookup_expr='icontains')
    descricao__ll  = filters.CharFilter(field_name='descricao', lookup_expr='icontains')
    class Meta:
        model  = Calcado
        fields = {
            'descricao':    ['exact', 'll'],
            'fornecedor':   ['exact', 'll'],
            'preco_custo':  ['exact', 'lt', 'lte', 'gt', 'gte'],
            'preco_venda':  ['exact', 'lt', 'lte', 'gt', 'gte'],
            'tipo':         ['exact'],
        }
