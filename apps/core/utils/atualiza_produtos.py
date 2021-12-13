from apps.core import models
from apps.core.utils import scraping


def atualizar_produtos():
    produtos = models.Produto.objects.filter(ativo=True)

    for produto in produtos:
        data = scraping.Lojas(produto).data()
        produto.atualiza_produto(**data)
