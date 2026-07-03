from rest_framework.routers import DefaultRouter
from .views import ProdutoViewSet, ClienteViewSet

router.register(r'produtos', ProdutoViewSet, basename='produto')
router.register(r'clientes', ClienteViewSet, basename='cliente')

urlpatterns = router.urls