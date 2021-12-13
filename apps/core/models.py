from django.db import models

from django.contrib.auth import get_user_model
from django.utils import timezone


class Produto(models.Model):
    data = models.DateTimeField('Criação', auto_now_add=True)
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    url = models.URLField('URL do produto', max_length=512)
    consultas = models.TextField(blank=True, null=True)
    ativo = models.BooleanField('Ativo', default=True)
    nome = models.CharField(max_length=1000, blank=True, null=True)
    preco = models.CharField(max_length=10, blank=True, null=True)
    imagem = models.URLField(max_length=512, blank=True, null=True)
    consultas = models.JSONField(blank=True, null=True)
    ultima_consulta = models.DateTimeField(blank=True, null=True)

    def atualiza_produto(self, nome, preco, imagem):
        self.nome = nome
        self.preco = preco
        self.imagem = imagem
        self.ultima_consulta = timezone.now()
        self.save()
