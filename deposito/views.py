from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DeleteView, ListView
from .models import *
from .forms import *

class PedidoListView (ListView):
    # model = Pedido_item
    # queryset = Pedido_item.objects.order_by('-id')
    def get(self, request, *args, **kwargs):
        pedidos = Pedido_item.objects.all().order_by('-id')
        for pedido in pedidos:
            posicao = Produto_posicao.objects.filter(produto=pedido.produto).exclude(quantidade=0).order_by('posicao').first()
            pedido.posicao = posicao
        context = {'pedidos': pedidos}
        return render(request, "deposito/pedido_item_list.html", context=context)
    
    # def get_context_data(self,**kwargs):
    #     context = super(PedidoListView,self).get_context_data(**kwargs)
    #     context['posicao'] = Produto_posicao.objects.filter()
    #     return context

class InitPicking (ListView):
    # model = Pedido_item
    # template_name = 'deposito/picking.html'
    # queryset = Pedido_item.objects.filter(status = '0')
    def get(self, request, *args, **kwargs):
        pedidos = Pedido_item.objects.all().order_by('id').filter(status = '0')
        for pedido in pedidos:
            posicao = Produto_posicao.objects.filter(produto=pedido.produto).exclude(quantidade=0).order_by('posicao').first()
            pedido.posicao = posicao
        context = {'pedidos': pedidos}
        return render(request, "deposito/picking.html", context=context)

class ProdutoListView (ListView):
    model = Produto

class PosicaoListView (ListView):
    model = Produto_posicao
    queryset = Produto_posicao.objects.order_by('produto')


def createProduto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('deposito:produtos')
    form = ProdutoForm()

    return render(request,'novo_produto.html',{'form': form})

def editProduto (request, pk, template_name='deposito/edit_produto.html'):
    produto = get_object_or_404(Produto, id=pk)
    form = ProdutoForm(request.POST or None, instance=produto)
    if form.is_valid():
        form.save()
        return redirect('deposito:produtos')
    return render(request, template_name, {'form':form})

def createPosicao(request):
    if request.method == 'POST':
        form = ProdutoPosicaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('deposito:estoque')
    form = ProdutoPosicaoForm()

    return render(request,'nova_posicao.html',{'form': form})

def editPosicao (request, pk, template_name='deposito/edit_posicao.html'):
    posicao = get_object_or_404(Produto_posicao, id=pk)
    form = ProdutoPosicaoForm(request.POST or None, instance=posicao)
    if form.is_valid():
        form.save()
        return redirect('deposito:estoque')
    return render(request, template_name, {'form':form})

def createPedido(request):
    if request.method == 'POST':
        form = PedidoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('deposito:pedidos')
    form = PedidoItemForm()

    return render(request,'novo_pedido.html',{'form': form})

def editPedido (request, pk, template_name='deposito/edit_pedido.html'):
    pedido = get_object_or_404(Pedido_item, id=pk)
    form = PedidoItemEdit(request.POST or None, instance=pedido)
    if form.is_valid():
        form.save()
        return redirect('deposito:pedidos')
    return render(request, template_name, {'form':form})

def pegueiPedido (request, pk, template_name='blank.html'):
    pedido = get_object_or_404(Pedido_item, id=pk)
    pedido.status = '1'
    posicao = Produto_posicao.objects.filter(produto=pedido.produto).exclude(quantidade=0).order_by('posicao').first()
    posicao.quantidade -= 1
    posicao.save()
    pedido.save()
    return redirect('/')

def naoEncontrei (request, pk, template_name='blank.html'):
    pedido = get_object_or_404(Pedido_item, id=pk)
    posicao = Produto_posicao.objects.filter(produto=pedido.produto).exclude(quantidade=0).order_by('posicao').first()
    posicao.quantidade = 0
    posicao.save()
    estoque = Produto_posicao.objects.filter(produto=pedido.produto).exclude(quantidade=0).order_by('posicao')
    if not estoque:
        pedido.status = '2'
        pedido.save()
    return redirect('/')
