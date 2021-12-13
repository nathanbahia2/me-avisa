from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from apps.core.forms import ProdutoForm
from apps.core.models import Produto
from apps.core import tasks


@login_required
def index(request):
    form = ProdutoForm()
    produtos = Produto.objects.filter(usuario=request.user, ativo=True)

    if request.method == 'POST':
        form = ProdutoForm(request.POST)

        if form.is_valid():
            # todo: deixar os campos nome preco e imagem com valores padrão, que ao final da tarefa do celery serão sobrescritos com os valores reais
            produto = form.save(commit=False)
            produto.nome = 'Analisando...'
            produto.preco = '..'
            produto.imagem = 'https://greenvolt.com.br/wp-content/uploads/2018/05/ef3-placeholder-image.jpg'
            produto.usuario = request.user
            produto.save()

            tasks.task_atualizar_produtos.delay(produto_id=produto.id)
            return redirect('core:index')


    context = {
        'form': form,
        'produtos': produtos
    }
    return render(request, 'core/index.html', context)
