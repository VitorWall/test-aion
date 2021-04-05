from django import forms
from .models import *

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = "__all__"

class ProdutoPosicaoForm(forms.ModelForm):
    class Meta:
        model = Produto_posicao
        fields = "__all__"

class PedidoItemForm(forms.ModelForm):
    class Meta:
        model = Pedido_item
        fields = ['produto', 'endereco_destino']

class PedidoItemEdit(forms.ModelForm):
    class Meta:
        model = Pedido_item
        fields = ['status']

