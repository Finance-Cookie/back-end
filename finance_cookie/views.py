from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import transaction
from django.shortcuts import get_object_or_404
from .models import (
    Cliente, Produto, Item, TipoPagamento, FormaPagamento,
    Entrada, Saida, Compra, ItemCompra, Venda, ProdutoVenda, Historico, Usuario
)
from .serializers import (
    ClienteSerializer, ProdutoSerializer, ItemSerializer,
    TipoPagamentoSerializer, FormaPagamentoSerializer, EntradaSerializer,
    SaidaSerializer, CompraSerializer, ItemCompraSerializer,
    VendaSerializer, ProdutoVendaSerializer, HistoricoSerializer, UsuarioSerializer
)

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all().order_by('id')
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny]

    @action(detail=True, methods=['get'])
    def saldos(self, request, pk=None):
        usuario = self.get_object()
        return Response({
            'saldo_fisico': usuario.saldo_fisico,
            'saldo_online': usuario.saldo_online,
            'saldo_total': usuario.saldo_fisico + usuario.saldo_online
        })

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all().order_by('id')
    serializer_class = ClienteSerializer
    permission_classes = [AllowAny]

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all().order_by('id')
    serializer_class = ProdutoSerializer
    permission_classes = [AllowAny]

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by('id')
    serializer_class = ItemSerializer
    permission_classes = [AllowAny]

class TipoPagamentoViewSet(viewsets.ModelViewSet):
    queryset = TipoPagamento.objects.all().order_by('nome')
    serializer_class = TipoPagamentoSerializer
    permission_classes = [AllowAny]

class FormaPagamentoViewSet(viewsets.ModelViewSet):
    queryset = FormaPagamento.objects.all().order_by('id')
    serializer_class = FormaPagamentoSerializer
    permission_classes = [AllowAny]

# --- ENTIDADES COM REGRAS DE NEGÓCIO DE SALDO ---

def atualizar_saldo_usuario(forma_pagamento, valor, operacao):
    """
    Operacao: 'soma' ou 'subtracao'
    Determina se vai mexer no saldo online ou físico baseado na forma de pagamento.
    """
    usuario = Usuario.objects.first() # Pega o usuário do sistema
    if not usuario:
        return

    nome_forma = forma_pagamento.nome.upper()
    is_online = "ONLINE" in nome_forma or "PIX" in nome_forma or "CARTÃO" in nome_forma

    if operacao == 'soma':
        if is_online:
            usuario.saldo_online += valor
        else:
            usuario.saldo_fisico += valor
    elif operacao == 'subtracao':
        if is_online:
            usuario.saldo_online -= valor
        else:
            usuario.saldo_fisico -= valor
            
    usuario.save()

class EntradaViewSet(viewsets.ModelViewSet):
    queryset = Entrada.objects.all().order_by('-id')
    serializer_class = EntradaSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        with transaction.atomic():
            entrada = serializer.save()
            atualizar_saldo_usuario(entrada.formapagamento, entrada.valorTotal, 'soma')

    def perform_destroy(self, instance):
        with transaction.atomic():
            atualizar_saldo_usuario(instance.formapagamento, instance.valorTotal, 'subtracao')
            instance.delete()

class SaidaViewSet(viewsets.ModelViewSet):
    queryset = Saida.objects.all().order_by('-id')
    serializer_class = SaidaSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        with transaction.atomic():
            saida = serializer.save()
            atualizar_saldo_usuario(saida.formapagamento, saida.valorTotal, 'subtracao')

    def perform_destroy(self, instance):
        with transaction.atomic():
            atualizar_saldo_usuario(instance.formapagamento, instance.valorTotal, 'soma')
            instance.delete()

class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all().order_by('-id')
    serializer_class = VendaSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        with transaction.atomic():
            venda = serializer.save()
            atualizar_saldo_usuario(venda.formapagamento, venda.valorTotal, 'soma')

    def perform_destroy(self, instance):
        with transaction.atomic():
            atualizar_saldo_usuario(instance.formapagamento, instance.valorTotal, 'subtracao')
            instance.delete()

class CompraViewSet(viewsets.ModelViewSet):
    queryset = Compra.objects.all().order_by('-id')
    serializer_class = CompraSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        with transaction.atomic():
            compra = serializer.save()
            atualizar_saldo_usuario(compra.formapagamento, compra.valorTotal, 'subtracao')

    def perform_destroy(self, instance):
        with transaction.atomic():
            atualizar_saldo_usuario(instance.formapagamento, instance.valorTotal, 'soma')
            instance.delete()

class ItemCompraViewSet(viewsets.ModelViewSet):
    queryset = ItemCompra.objects.all()
    serializer_class = ItemCompraSerializer
    permission_classes = [AllowAny]

class ProdutoVendaViewSet(viewsets.ModelViewSet):
    queryset = ProdutoVenda.objects.all()
    serializer_class = ProdutoVendaSerializer
    permission_classes = [AllowAny]

class HistoricoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Historico.objects.all().order_by("-data")
    serializer_class = HistoricoSerializer
    permission_classes = [AllowAny]