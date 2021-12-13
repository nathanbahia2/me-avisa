from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from apps.core.forms import ProdutoForm
from apps.core.models import Produto
from apps.core.utils.scrapping import Lojas


@login_required
def index(request):
    form = ProdutoForm()
    produtos = Produto.objects.filter(usuario=request.user, ativo=True)

    if request.method == 'POST':
        form = ProdutoForm(request.POST)

        if form.is_valid():
            produto = form.save(commit=False)
            produto.usuario = request.user
            produto.save()

            # todo: essa consulta deverá ser realizada via celery
            consulta = Lojas(produto).data()
            produto.atualiza_produto(**consulta)

            return redirect('core:index')


    context = {
        'form': form,
        'produtos': produtos
    }
    return render(request, 'core/index.html', context)
