from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ClienteViewSet, ProdutoViewSet, ItemViewSet, TipoPagamentoViewSet,
    FormaPagamentoViewSet, EntradaViewSet, SaidaViewSet, CompraViewSet,
    ItemCompraViewSet, VendaViewSet, ProdutoVendaViewSet, HistoricoViewSet, UsuarioViewSet
)

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuarios')
router.register(r'clientes', ClienteViewSet, basename='clientes')
router.register(r'produtos', ProdutoViewSet, basename='produtos')
router.register(r'itens', ItemViewSet, basename='itens')
router.register(r'tipos-pagamento', TipoPagamentoViewSet, basename='tipos-pagamento')
router.register(r'formas-pagamento', FormaPagamentoViewSet, basename='formas-pagamento')
router.register(r'entradas', EntradaViewSet, basename='entradas')
router.register(r'saidas', SaidaViewSet, basename='saidas')
router.register(r'compras', CompraViewSet, basename='compras')
router.register(r'itens-compra', ItemCompraViewSet, basename='itens-compra')
router.register(r'vendas', VendaViewSet, basename='vendas')
router.register(r'produtos-venda', ProdutoVendaViewSet, basename='produtos-venda')
router.register(r'historicos', HistoricoViewSet, basename='historicos')

urlpatterns = [
    path('', include(router.urls)),
]