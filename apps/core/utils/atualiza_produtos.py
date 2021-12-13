from apps.core import models
from apps.core.utils import scraping


def atualizar_produtos(produto_id=None):
    if produto_id:
        produtos = models.Produto.objects.filter(pk=produto_id, ativo=True)

    else:
        produtos = models.Produto.objects.filter(ativo=True)


    for produto in produtos:
        data = scraping.Lojas(produto).data()
        produto.atualiza_produto(**data)
