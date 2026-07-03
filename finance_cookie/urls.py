from django.urls import path, include
from rest_framework import routers
from . import api_views

router = routers.DefaultRouter()
router.register(r'clients', api_views.ClienteViewSet, basename='clients')
router.register(r'products', api_views.ProdutoViewSet, basename='products')
router.register(r'items', api_views.ItemViewSet, basename='items')
router.register(r'tipos', api_views.TipoPagamentoViewSet, basename='tipospagamento')
router.register(r'formas', api_views.FormaPagamentoViewSet, basename='formaspagamento')
router.register(r'entradas', api_views.EntradaViewSet, basename='entradas')
router.register(r'saidas', api_views.SaidaViewSet, basename='saidas')
router.register(r'compras', api_views.CompraViewSet, basename='compras')
router.register(r'itemcompras', api_views.ItemCompraViewSet, basename='itemcompras')
router.register(r'vendas', api_views.VendaViewSet, basename='vendas')
router.register(r'produtovenda', api_views.ProdutoVendaViewSet, basename='produtovenda')

urlpatterns = [
	path('', include(router.urls)),
]