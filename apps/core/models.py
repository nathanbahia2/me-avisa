from django.db import models

from django.contrib.auth import get_user_model
from django.utils import timezone


class Produto(models.Model):
    data = models.DateTimeField('Criação', auto_now_add=True)
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    url = models.URLField('URL do produto', max_length=512)
    ativo = models.BooleanField('Ativo', default=True)
    nome = models.CharField(max_length=1000, blank=True, null=True)
    preco = models.CharField(max_length=10, blank=True, null=True)
    imagem = models.URLField(max_length=512, blank=True, null=True)
    consultas = models.JSONField(blank=True, null=True)
    ultima_consulta = models.DateTimeField(blank=True, null=True)

    def atualiza_produto(self, nome, preco, imagem):
        if nome and preco and imagem:
            self.nome = nome
            self.preco = preco
            self.imagem = imagem
            self.ultima_consulta = timezone.now()
            self.atualiza_consultas(nome, preco, imagem)

    def atualiza_consultas(self, nome, preco, imagem):
        consultas = self.consultas or []
        consultas.append({
            'data': timezone.now().isoformat(),
            'nome': nome,
            'preco': preco,
            'imagem': imagem
        })
        self.consultas = consultas
        self.save()
