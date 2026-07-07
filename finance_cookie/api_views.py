from rest_framework import viewsets
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


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all().order_by('id')
    serializer_class = ProdutoSerializer
    permission_classes = [AllowAny]


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by('nome')
    serializer_class = ItemSerializer
    permission_classes = [AllowAny]


class TipoPagamentoViewSet(viewsets.ModelViewSet):
    queryset = TipoPagamento.objects.all().order_by('nome')
    serializer_class = TipoPagamentoSerializer
    permission_classes = [AllowAny]


class FormaPagamentoViewSet(viewsets.ModelViewSet):
    queryset = FormaPagamento.objects.all().order_by('nome')
    serializer_class = FormaPagamentoSerializer
    permission_classes = [AllowAny]


class EntradaViewSet(viewsets.ModelViewSet):
    queryset = Entrada.objects.all().order_by('-data')
    serializer_class = EntradaSerializer
    permission_classes = [AllowAny]


class SaidaViewSet(viewsets.ModelViewSet):
    queryset = Saida.objects.all().order_by('-data')
    serializer_class = SaidaSerializer
    permission_classes = [AllowAny]


class CompraViewSet(viewsets.ModelViewSet):
    queryset = Compra.objects.all().order_by('-data')
    serializer_class = CompraSerializer
    permission_classes = [AllowAny]


class ItemCompraViewSet(viewsets.ModelViewSet):
    queryset = ItemCompra.objects.all()
    serializer_class = ItemCompraSerializer
    permission_classes = [AllowAny]


class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all().order_by('-data')
    serializer_class = VendaSerializer
    permission_classes = [AllowAny]


class ProdutoVendaViewSet(viewsets.ModelViewSet):
    queryset = ProdutoVenda.objects.all()
    serializer_class = ProdutoVendaSerializer
    permission_classes = [AllowAny]

