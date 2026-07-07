from rest_framework import viewsets, filters, status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import transaction
from django.db.models import Sum
from django.shortcuts import get_object_or_404
from .models import (
    Cliente, Produto, Item, TipoPagamento, FormaPagamento,
    Entrada, Saida, Compra, ItemCompra, Venda, ProdutoVenda, Historico, Usuario
)
from .serializers import (
    ClienteSerializer, ProdutoSerializer, ItemSerializer,
    TipoPagamentoSerializer, FormaPagamentoSerializer, EntradaSerializer,
    SaidaSerializer, CompraSerializer, ItemCompraSerializer,
    VendaSerializer, ProdutoVendaSerializer, HistoricoSerializer
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

# --- ATUALIZAÇÃO AUTOMÁTICA DE SALDO DE ACORDO COM AS USER STORIES ---
def atualizar_saldo_usuario(forma_pagamento, valor, operacao):
    # Usa select_for_update para travar a linha no banco e garantir consistência atômica
    usuario = Usuario.objects.select_for_update().first()
    if not usuario:
        return
    
    nome_forma = forma_pagamento.nome.upper()
    is_online = any(termo in nome_forma for termo in ["ONLINE", "PIX", "CARTÃO", "CARTAO", "TESTE"])

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
    queryset = ItemCompra.objects.all().order_by('id')
    serializer_class = ItemCompraSerializer
    permission_classes = [AllowAny]

class ProdutoVendaViewSet(viewsets.ModelViewSet):
    queryset = ProdutoVenda.objects.all().order_by('id')
    serializer_class = ProdutoVendaSerializer
    permission_classes = [AllowAny]

class RelatorioViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    @action(detail=False, methods=["get"])
    def faturamento_por_mes(self, request):
        return Response({"vendas_por_mes": []})

    @action(detail=False, methods=["get"])
    def financeiro_por_categoria(self, request):
        entradas = Entrada.objects.values("tipocategoria__nome").annotate(total=Sum("valorTotal")).order_by("-total")
        saidas = Saida.objects.values("tipocategoria__nome").annotate(total=Sum("valorTotal")).order_by("-total")
        return Response({
            "entradas": [{"categoria": e["tipocategoria__nome"], "total": e["total"]} for e in entradas],
            "saidas": [{"categoria": s["tipocategoria__nome"], "total": s["total"]} for e in saidas]
        })

class HistoricoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Historico.objects.all().order_by("-data")
    serializer_class = HistoricoSerializer
    permission_classes = [AllowAny]