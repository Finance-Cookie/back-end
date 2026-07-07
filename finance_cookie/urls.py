from django.urls import path, include
from rest_framework import routers
from . import views
from .users_views import UsersViewSet

router = routers.DefaultRouter()
router.register(r'clientes', views.ClienteViewSet, basename='clientes')
router.register(r'produtos', views.ProdutoViewSet, basename='produtos')
router.register(r'items', views.ItemViewSet, basename='items')
router.register(r'tipos', views.TipoPagamentoViewSet, basename='tipospagamento')
router.register(r'formas', views.FormaPagamentoViewSet, basename='formaspagamento')
router.register(r'entradas', views.EntradaViewSet, basename='entradas')
router.register(r'saidas', views.SaidaViewSet, basename='saidas')
router.register(r'compras', views.CompraViewSet, basename='compras')
router.register(r'itemcompras', views.ItemCompraViewSet, basename='itemcompras')
router.register(r'vendas', views.VendaViewSet, basename='vendas')
router.register(r'produtovenda', views.ProdutoVendaViewSet, basename='produtovenda')
router.register(r'relatorios', views.RelatorioViewSet, basename='relatorios')
router.register(r"historico", views.HistoricoViewSet, basename="historico")
router.register(r'usuarios', UsersViewSet, basename='usuarios')

urlpatterns = [
    path('', include(router.urls)),
]