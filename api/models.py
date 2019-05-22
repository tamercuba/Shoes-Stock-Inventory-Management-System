from django.db import models

class Sapato(models.Model):
    ''' MODELO SAPATO PARA ESTOQUE '''

    #    TIPOS DE SAPATOS
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

    #    NUMERACOES
    NUMERACAO_CHOCES = [(num, str(num)) for num in range(35,46,1)]

    #    CAMPOS
    _id         = models.AutoField(primary_key=True)
    descricao   = models.CharField(max_length=100, null=False, blank = False)
    fornecedor  = models.CharField(max_length=100, null=False, blank=False)
    tipo        = models.CharField(max_length=2, choices=TIPO_CHOICES, null=False, blank=False)
    numeracao   = models.IntegerField(choices=NUMERACAO_CHOCES, null=False, blank=False)
    quantidade  = models.IntegerField(null = False, blank = False, default = 0)
    preco_custo = models.DecimalField(
        max_digits=6, decimal_places=2,
        verbose_name='Preco de Custo', null=False, blank=False
        )
    preco_venda = models.DecimalField(
        max_digits=6, decimal_places=2,
        verbose_name='Preco de Custo', null=False, blank=False
        )

    def __str__(self):
        return str(self.descricao) + '-' + str(self.numeracao)
