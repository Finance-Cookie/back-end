from rest_framework import viewsets, status, filters
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
    VendaSerializer, ProdutoVendaSerializer, HistoricoSerializer, UsuarioSerializer
)

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all().order_by('id')
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny]

    def get_current_user(self):
        user = Usuario.objects.first()
        if not user:
            user = Usuario.objects.create(
                nome="Usuário Padrão",
                email="padrao@cookie.com",
                senha_hash="hash_provisoria",
                saldo_fisico=0.0,
                saldo_online=0.0
            )
        return user

    @action(detail=False, methods=['get', 'put', 'patch'])
    def me(self, request):
        user = self.get_current_user()
        if request.method == 'GET':
            serializer = self.get_serializer(user)
            return Response(serializer.data)
        elif request.method in ['PUT', 'PATCH']:
            serializer = self.get_serializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path='register')
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Usuário cadastrado com sucesso!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

def atualizar_saldo_usuario(forma_pagamento, valor, operacao):
    usuario = Usuario.objects.first()
    if not usuario:
        return
    nome_forma = forma_pagamento.nome.upper()
    is_online = "ONLINE" in nome_forma or "PIX" in nome_forma or "CARTÃO" in nome_forma or "TESTE" in nome_forma

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

class HistoricoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Historico.objects.all().order_by("-data")
    serializer_class = HistoricoSerializer
    permission_classes = [AllowAny]

class RelatorioViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]
    @action(detail=False, methods=["get"])
    def faturamento_por_mes(self, request):
        return Response({"vendas_por_mes": []})
    @action(detail=False, methods=["get"])
    def financeiro_por_categoria(self, request):
        return Response({"entradas": [], "saidas": []})