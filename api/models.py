from django.db import models

class File(models.Model):
    file = models.FileField(upload_to='static/TEMP/',blank=False, null=False)
    def __str__(self):
        return self.file.name

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
    descricao   = models.CharField(max_length=100, null=False, blank=False, unique=True)
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

    def quantidade_total(self):
        total = Estoque.objects.filter(id_calcado=self._id).aggregate(models.Sum('quantidade'))
        return total['quantidade__sum'] or 0

    class Meta:
        verbose_name: 'Calçado'
        verbose_name_plural: 'Calçados'
        ordering = ['descricao']

class Estoque(models.Model):
    '''
    NUMERACAO E QUANTIDADE DISPONIVEL EM ESTOQUE
    '''

    NUMERACAO_CHOICES = [(num, str(num)) for num in range(35,46,1)]

    _id        = models.AutoField(primary_key=True)
    id_calcado = models.ForeignKey(
            Calcado, on_delete = models.CASCADE, verbose_name = 'calcado', related_name = 'estoque')
    tamanho    = models.IntegerField(choices=NUMERACAO_CHOICES, null=False, blank=False)
    quantidade = models.IntegerField(null=False, default=0)

    def __str__(self):
        return str(self.tamanho)

    def _descricao(self):
        return self.id_calcado.descricao

    class Meta:
        verbose_name        = 'Estoque'
        verbose_name_plural = 'Estoque'
        unique_together     = ('id_calcado', 'tamanho')
        constraints         = [
            models.CheckConstraint(check=models.Q(quantidade__gte=0), name='quantidade_gte_0'),
        ]
        ordering            = ['-quantidade']
