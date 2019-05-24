from django.db import models

class Calcado(models.Model):
    '''
    MODELO CALÇADO
    '''
    #    TIPOS DE CALÇADOS
    BOTA        = 'BT'
    CASUAL      = 'CS'
    CHINELO     = 'CH'
    ESPORTIVO   = 'ES'
    SANDALIA    = 'SD'
    SOCIAL      = 'SC'

    TIPO_CHOICES = [
        (BOTA, 'Bota'),
        (CASUAL, 'Casual'),
        (CHINELO, 'Chinelo'),
        (ESPORTIVO, 'Esportivo'),
        (SANDALIA, 'Sandália'),
        (SOCIAL, 'Social'),
    ]

    _id         = models.AutoField(primary_key=True)
    descricao   = models.CharField(max_length=100, null=False, blank=False)
    fornecedor  = models.CharField(max_length=100, null=False, blank=False)
    tipo        = models.CharField(max_length=2, choices=TIPO_CHOICES, null=False, blank=False)
    preco_custo = models.DecimalField(
            max_digits=6, decimal_places=2, verbose_name = 'Preço de Custo',
            null=False, blank=False
            )
    preco_venda = models.DecimalField(
            max_digits=6, decimal_places=2, verbose_name = 'Preço de Venda',
            null=False, blank=False
            )

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name: 'Calçado'
        verbose_name_plural: 'Calçados'
        ordering = ['descricao']

class Numeracao(models.Model):
    '''
    NUMERACAO E QUANTIDADE DISPONIVEL EM ESTOQUE
    '''

    NUMERACAO_CHOICES = [(num, str(num)) for num in range(35,46,1)]

    _id        = models.AutoField(primary_key=True)
    id_calcado = models.ForeignKey(
            Calcado, on_delete = models.CASCADE, verbose_name = 'calcado', related_name = 'numeracao')
    tamanho    = models.IntegerField(choices=NUMERACAO_CHOICES, null=False, blank=False, unique=True)
    quantidade = models.IntegerField(null=False, default=0)

    def __str__(self):
        return str(self.tamanho)

    def _descricao(self):
        return self.id_calcado.descricao

    class Meta:
        verbose_name = 'Numeração'
        verbose_name_plural = 'Numerações'
        ordering = ['-quantidade']
