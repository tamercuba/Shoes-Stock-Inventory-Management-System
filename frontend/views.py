from api.models import Calcado, Estoque
from django.shortcuts      import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    template_name = 'index.html'
    calcado_query = Calcado.objects.all()
    estoque_query = Estoque.objects.all()
    calcados      = []

    for instancia in calcado_query:
        temp               = {}
        temp['descricao']  = instancia.descricao
        temp['fornecedor'] = instancia.fornecedor
        temp['tipo']       = instancia.tipo
        temp['custo']      = instancia.preco_custo
        temp['venda']      = instancia.preco_venda

        for estoque in estoque_query.filter(id_calcado=instancia._id):
            temp[str(estoque.tamanho)] = estoque.quantidade

        temp['total'] = instancia.quantidade_total()
        calcados.append(temp)

    page      = request.GET.get('page')
    paginator = Paginator(calcados, 10)
    try:
        content = paginator.get_page(page)
    except  PageNotAnInteger:
        content = paginator.page(1)
    except EmptyPage:
        content.paginator.page(paginator.num_pages)
    context     = {
        'calcados': content,
    }
    return render(request, template_name, context)
