from rest_framework import viewsets, filters
from .models import Produto
from .serializers import ProdutoSerializer

class ProdutoViewSet(viewsets.ModelViewSet):

    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nome', 'descricao']
    ordering_fields = ['nome', 'valor']
    ordering = ['nome']