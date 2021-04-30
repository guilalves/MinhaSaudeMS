from django.db import models
from datetime import datetime as DT

class Produtos(models.Model):

    quantidade = models.IntegerField()
    nome = models.CharField(max_length=200)
    qtde_carboidrato = models.TextField()
    # mlg_insulina = models.CharField(max_length=200)
    data_atual = models.DateTimeField(default=DT.now, blank=True)
