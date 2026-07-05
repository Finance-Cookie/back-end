from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny

from .models import (
    Cliente,
    Produto,
    Item,
    TipoPagamento,
    FormaPagamento,
    Entrada,
    Saida,
    Compra,
    ItemCompra,
    Venda,
    ProdutoVenda,
)
from .serializers import (
    ClienteSerializer,
    ProdutoSerializer,
    ItemSerializer,
    TipoPagamentoSerializer,
    FormaPagamentoSerializer,
    EntradaSerializer,
    SaidaSerializer,
    CompraSerializer,
    ItemCompraSerializer,
    VendaSerializer,
    ProdutoVendaSerializer,
)


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all().order_by('id')
    serializer_class = ClienteSerializer
    permission_classes = [AllowAny]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nome','email','telefone','bairro','logradouro']
    ordering_fields = ['id','nome','bairro']
    ordering = ['nome']


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all().order_by('id')
    serializer_class = ProdutoSerializer
    permission_classes = [AllowAny]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nome','descricao']
    ordering_fields = ['id','nome','valor']
    ordering = ['nome']


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by('nome')
    serializer_class = ItemSerializer
    permission_classes = [AllowAny]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["nome"]
    ordering_fields = ["id","nome","valor"]
    ordering = ["nome"]


class TipoPagamentoViewSet(viewsets.ModelViewSet):
    queryset = TipoPagamento.objects.all().order_by('nome')
    serializer_class = TipoPagamentoSerializer
    permission_classes = [AllowAny]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["nome"]
    ordering_fields = ["id","nome"]
    ordering = ["nome"]


class FormaPagamentoViewSet(viewsets.ModelViewSet):
    queryset = FormaPagamento.objects.all().order_by('nome')
    serializer_class = FormaPagamentoSerializer
    permission_classes = [AllowAny]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["nome"]
    ordering_fields = ["id","nome"]
    ordering = ["nome"]


class EntradaViewSet(viewsets.ModelViewSet):
    queryset = Entrada.objects.all().order_by('-data')
    serializer_class = EntradaSerializer
    permission_classes = [AllowAny]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['descricao', 'formapagamento__nome', 'tipocategoria__nome']
    ordering_fields = ['data', 'valorTotal']
    ordering = ['-data']


class SaidaViewSet(viewsets.ModelViewSet):
    queryset = Saida.objects.all().order_by('-data')
    serializer_class = SaidaSerializer
    permission_classes = [AllowAny]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['descricao', 'formapagamento__nome', 'tipocategoria__nome']
    ordering_fields = ['data', 'valorTotal']
    ordering = ['-data']


class CompraViewSet(viewsets.ModelViewSet):
    queryset = Compra.objects.all().order_by('-data')
    serializer_class = CompraSerializer
    permission_classes = [AllowAny]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["descricao","formapagamento__nome","tipocategoria__nome"]
    ordering_fields = ["data","valorTotal","frete","desconto"]
    ordering = ["-data"]


class ItemCompraViewSet(viewsets.ModelViewSet):
    queryset = ItemCompra.objects.all()
    serializer_class = ItemCompraSerializer
    permission_classes = [AllowAny]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["item__nome", "compra__descricao"]
    ordering_fields = ["quantidade","valor_unitario"]
    ordering = ["item__nome"]


class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all().order_by('-data')
    serializer_class = VendaSerializer
    permission_classes = [AllowAny]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["cliente__nome","formapagamento__nome","tipocategoria__nome"]
    ordering_fields = ["data","valorTotal","frete","desconto"]
    ordering = ["-data"]


class ProdutoVendaViewSet(viewsets.ModelViewSet):
    queryset = ProdutoVenda.objects.all()
    serializer_class = ProdutoVendaSerializer
    permission_classes = [AllowAny]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["produto__nome","venda__cliente__nome"]
    ordering_fields = ["quantidade","valor_unitario"]
    ordering = ["produto__nome"]
