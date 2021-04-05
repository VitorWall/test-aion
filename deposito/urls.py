from django.urls import path
from . import views

app_name = "deposito"

urlpatterns = [
    path('', views.InitPicking.as_view(), name="picking"),
    path('pedidos', views.PedidoListView.as_view(), name="pedidos"),
    path('produtos', views.ProdutoListView.as_view(), name="produtos"),
    path('estoque', views.PosicaoListView.as_view(), name="estoque"),
    path('novo-produto', views.createProduto, name='createProduto'),
    path('editar-produto/<int:pk>', views.editProduto, name='editProduto'),
    path('nova-posicao', views.createPosicao, name='createPosicao'),
    path('editar-posicao/<int:pk>', views.editPosicao, name='editPosicao'),
    path('novo-pedido', views.createPedido, name='createPedido'),
    path('editar-pedido/<int:pk>', views.editPedido, name='editPedido'),
    path('peguei-pedido/<int:pk>', views.pegueiPedido, name='pegueiPedido'),
    path('nao-encontrei/<int:pk>', views.naoEncontrei, name='naoEncontrei')
]