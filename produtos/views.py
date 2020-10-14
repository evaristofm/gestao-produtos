from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Produto
from .forms import ProdutoForm


@login_required
def home(request):
    produtos = Produto.objects.all()
    return render(request, 'produto_list.html', {'produtos': produtos})

@login_required
def produto_new(request):
    form = ProdutoForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('produto_list')

    return render(request, 'produto_form.html', {'form': form})


@login_required
def produto_update(request, id):
    produto = get_object_or_404(Produto, pk=id)
    form = ProdutoForm(request.POST or None, instance=produto)

    if form.is_valid():
        form.save()
        return redirect('produto_list')

    return render(request, 'produto_edit.html', {'form': form})

@login_required
def produto_delete(request, id):
    produto = get_object_or_404(Produto, pk=id)
    form = ProdutoForm(request.POST or None, instance=produto)

    if request.method == 'POST':
        produto.delete()
        return redirect('produto_list')

    return render(request, 'produto_delete.html', {'produto': produto})