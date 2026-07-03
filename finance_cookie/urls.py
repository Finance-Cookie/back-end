from rest_framework.routers import DefaultRouter
from .views import ProdutoViewSet, ClienteViewSet, SaidaViewSet

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet, basename='produto')
router.register(r'clientes', ClienteViewSet, basename='cliente')
router.register(r'saidas', SaidaViewSet, basename='saida')

urlpatterns = router.urls