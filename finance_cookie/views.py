from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum, Avg, Count, F
from django.db.models.functions import TruncMonth

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
    Historico,
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
    HistoricoSerializer,
)


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all().order_by('id')
    serializer_class = ClienteSerializer
    permission_classes = [AllowAny]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nome','email','telefone','bairro','logradouro']
    ordering_fields = ['id','nome','bairro']
    ordering = ['nome']

    def perform_create(self, serializer):
        cliente = serializer.save()

        Historico.objects.create(
            tipo="CLIENTE",
            descricao=f"Cliente criado: {cliente.nome}",
            referencia_id=cliente.id
        )


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all().order_by('id')
    serializer_class = ProdutoSerializer
    permission_classes = [AllowAny]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nome','descricao']
    ordering_fields = ['id','nome','valor']
    ordering = ['nome']

    def perform_create(self, serializer):
        produto = serializer.save()

        Historico.objects.create(
            tipo="PRODUTO",
            descricao=f"Produto criado: {produto.nome}",
            referencia_id=produto.id
        )


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by('nome')
    serializer_class = ItemSerializer
    permission_classes = [AllowAny]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["nome"]
    ordering_fields = ["id","nome","valor"]
    ordering = ["nome"]

    def perform_create(self, serializer):
        item = serializer.save()

        Historico.objects.create(
            tipo="PRODUTO",
            descricao=f"Item criado: {item.nome}",
            referencia_id=item.id
        )


class TipoPagamentoViewSet(viewsets.ModelViewSet):
    queryset = TipoPagamento.objects.all().order_by('nome')
    serializer_class = TipoPagamentoSerializer
    permission_classes = [AllowAny]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["nome"]
    ordering_fields = ["id","nome"]
    ordering = ["nome"]

    def perform_create(self, serializer):
        tp = serializer.save()

        Historico.objects.create(
            tipo="COMPRA",
            descricao=f"Tipo de pagamento criado: {tp.nome}",
            referencia_id=tp.id
        )

class FormaPagamentoViewSet(viewsets.ModelViewSet):
    queryset = FormaPagamento.objects.all().order_by('nome')
    serializer_class = FormaPagamentoSerializer
    permission_classes = [AllowAny]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["nome"]
    ordering_fields = ["id","nome"]
    ordering = ["nome"]

    def perform_create(self, serializer):
        fp = serializer.save()

        Historico.objects.create(
            tipo="COMPRA",
            descricao=f"Forma de pagamento criada: {fp.nome}",
            referencia_id=fp.id
        )


class EntradaViewSet(viewsets.ModelViewSet):
    queryset = Entrada.objects.all().order_by('-data')
    serializer_class = EntradaSerializer
    permission_classes = [AllowAny]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['descricao', 'formapagamento__nome', 'tipocategoria__nome']
    ordering_fields = ['data', 'valorTotal']
    ordering = ['-data']

    def perform_create(self, serializer):
        entrada = serializer.save()

        Historico.objects.create(
            tipo="ENTRADA",
            descricao=f"Entrada registrada: {entrada.descricao}",
            referencia_id=entrada.id
        )


class SaidaViewSet(viewsets.ModelViewSet):
    queryset = Saida.objects.all().order_by('-data')
    serializer_class = SaidaSerializer
    permission_classes = [AllowAny]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['descricao', 'formapagamento__nome', 'tipocategoria__nome']
    ordering_fields = ['data', 'valorTotal']
    ordering = ['-data']

    def perform_create(self, serializer):
        saida = serializer.save()

        Historico.objects.create(
            tipo="SAIDA",
            descricao=f"Saída registrada: {saida.descricao}",
            referencia_id=saida.id
        )


class CompraViewSet(viewsets.ModelViewSet):
    queryset = Compra.objects.all().order_by('-data')
    serializer_class = CompraSerializer
    permission_classes = [AllowAny]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["descricao","formapagamento__nome","tipocategoria__nome"]
    ordering_fields = ["data","valorTotal","frete","desconto"]
    ordering = ["-data"]

    def perform_create(self, serializer):
        compra = serializer.save()

        Historico.objects.create(
            tipo="COMPRA",
            descricao=f"Compra registrada: {compra.descricao}",
            referencia_id=compra.id
        )


class ItemCompraViewSet(viewsets.ModelViewSet):
    queryset = ItemCompra.objects.all()
    serializer_class = ItemCompraSerializer
    permission_classes = [AllowAny]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["item__nome", "compra__descricao"]
    ordering_fields = ["quantidade","valor_unitario"]
    ordering = ["item__nome"]

    def perform_create(self, serializer):
        ic = serializer.save()

        Historico.objects.create(
            tipo="COMPRA",
            descricao=f"Item adicionado na compra ID {ic.compra.id}",
            referencia_id=ic.id
        )


class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all().order_by('-data')
    serializer_class = VendaSerializer
    permission_classes = [AllowAny]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["cliente__nome","formapagamento__nome","tipocategoria__nome"]
    ordering_fields = ["data","valorTotal","frete","desconto"]
    ordering = ["-data"]

    def perform_create(self, serializer):
        venda = serializer.save()

        Historico.objects.create(
            tipo="VENDA",
            descricao=f"Venda registrada para {venda.cliente.nome}",
            referencia_id=venda.id
        )


class ProdutoVendaViewSet(viewsets.ModelViewSet):
    queryset = ProdutoVenda.objects.all()
    serializer_class = ProdutoVendaSerializer
    permission_classes = [AllowAny]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["produto__nome","venda__cliente__nome"]
    ordering_fields = ["quantidade","valor_unitario"]
    ordering = ["produto__nome"]

    def perform_create(self, serializer):
        pv = serializer.save()

        Historico.objects.create(
            tipo="VENDA",
            descricao=f"Produto adicionado na venda ID {pv.venda.id}",
            referencia_id=pv.id
        )


class RelatorioViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def list(self, request):
        return Response({
            "message": "Relatórios disponíveis",
            "endpoints": {
                "geral": request.build_absolute_uri("geral/"),
                "financeiro": request.build_absolute_uri("financeiro/"),
                "clientes": request.build_absolute_uri("clientes/"),
                "vendas": request.build_absolute_uri("vendas/"),
                "compras": request.build_absolute_uri("compras/"),
                "produtos_mais_vendidos": request.build_absolute_uri("produtos_mais_vendidos/"),
                "clientes_mais_compraram": request.build_absolute_uri("clientes_mais_compraram/"),
                "vendas_por_periodo": request.build_absolute_uri("vendas_por_periodo/"),
                "compras_por_forma_pagamento": request.build_absolute_uri("compras_por_forma_pagamento/"),
                "financeiro_por_categoria": request.build_absolute_uri("financeiro_por_categoria/"),
            }
        })

    @action(detail=False, methods=["get"])
    def geral(self, request):
        entradas = Entrada.objects.aggregate(total=Sum("valorTotal"))["total"] or 0
        saidas = Saida.objects.aggregate(total=Sum("valorTotal"))["total"] or 0

        return Response({
            "clientes": Cliente.objects.count(),
            "produtos": Produto.objects.count(),
            "compras": Compra.objects.count(),
            "vendas": Venda.objects.count(),
            "entradas": Entrada.objects.count(),
            "saidas": Saida.objects.count(),
            "saldo": entradas - saidas,
        })

    @action(detail=False, methods=["get"])
    def financeiro(self, request):
        total_entradas = Entrada.objects.aggregate(total=Sum("valorTotal"))["total"] or 0
        total_saidas = Saida.objects.aggregate(total=Sum("valorTotal"))["total"] or 0

        return Response({
            "quantidade_entradas": Entrada.objects.count(),
            "valor_entradas": total_entradas,
            "quantidade_saidas": Saida.objects.count(),
            "valor_saidas": total_saidas,
            "saldo": total_entradas - total_saidas,
        })

    @action(detail=False, methods=["get"])
    def clientes(self, request):
        clientes = Cliente.objects.order_by("nome")

        return Response({
            "total_clientes": clientes.count(),
            "clientes": [
                {
                    "id": c.id,
                    "nome": c.nome,
                    "email": c.email,
                    "telefone": c.telefone,
                }
                for c in clientes
            ]
        })

    @action(detail=False, methods=["get"])
    def vendas(self, request):
        vendas = Venda.objects.select_related("cliente").order_by("-data")

        return Response({
            "quantidade": vendas.count(),
            "valor_total": vendas.aggregate(total=Sum("valorTotal"))["total"] or 0,
            "valor_medio": vendas.aggregate(media=Avg("valorTotal"))["media"] or 0,
            "vendas": [
                {
                    "id": v.id,
                    "cliente": v.cliente.nome,
                    "data": v.data,
                    "valor": v.valorTotal,
                }
                for v in vendas
            ]
        })

    @action(detail=False, methods=["get"])
    def compras(self, request):
        compras = Compra.objects.order_by("-data")

        return Response({
            "quantidade": compras.count(),
            "valor_total": compras.aggregate(total=Sum("valorTotal"))["total"] or 0,
            "valor_medio": compras.aggregate(media=Avg("valorTotal"))["media"] or 0,
            "compras": [
                {
                    "id": c.id,
                    "descricao": c.descricao,
                    "data": c.data,
                    "valor": c.valorTotal,
                }
                for c in compras
            ]
        })
    
    @action(detail=False, methods=["get"])
    def produtos_mais_vendidos(self, request):
        produtos = (ProdutoVenda.objects.values("produto__id", "produto__nome").annotate(total_vendido=Sum("quantidade")).order_by("-total_vendido"))

        return Response({
            "produtos": [
                {
                    "id": p["produto__id"],
                    "nome": p["produto__nome"],
                    "quantidade_vendida": p["total_vendido"],
                }
                for p in produtos
            ]
        })
    
    @action(detail=False, methods=["get"])
    def clientes_mais_compraram(self, request):
        clientes = (Venda.objects.values("cliente__id", "cliente__nome").annotate(total_compras=Count("id"), valor_total=Sum("valorTotal")).order_by("-valor_total"))

        return Response({
            "clientes": [
                {
                    "id": c["cliente__id"],
                    "nome": c["cliente__nome"],
                    "quantidade_vendas": c["total_compras"],
                    "valor_total": c["valor_total"],
                }
                for c in clientes
            ]
        })
    
    @action(detail=False, methods=["get"])
    def vendas_por_periodo(self, request):
        vendas = (Venda.objects.annotate(mes=TruncMonth("data")).values("mes").annotate(total=Sum("valorTotal"), quantidade=Count("id")).order_by("mes"))

        return Response({
            "vendas_por_mes": [
                {
                    "mes": v["mes"],
                    "quantidade": v["quantidade"],
                    "total": v["total"],
                }
                for v in vendas
            ]
        })
    
    @action(detail=False, methods=["get"])
    def compras_por_forma_pagamento(self, request):
        dados = (Compra.objects.values("formapagamento__nome").annotate(total=Sum("valorTotal"), quantidade=Count("id")).order_by("-total"))

        return Response({
            "formas_pagamento": [
                {
                    "forma": d["formapagamento__nome"],
                    "quantidade": d["quantidade"],
                    "total": d["total"],
                }
                for d in dados
            ]
        })
    
    @action(detail=False, methods=["get"])
    def financeiro_por_categoria(self, request):
        entradas = (Entrada.objects.values("tipocategoria__nome").annotate(total=Sum("valorTotal")).order_by("-total"))
        saidas = (Saida.objects.values("tipocategoria__nome").annotate(total=Sum("valorTotal")).order_by("-total"))

        return Response({
            "entradas": [
                {
                    "categoria": e["tipocategoria__nome"],
                    "total": e["total"],
                }
                for e in entradas
            ],
            "saidas": [
                {
                    "categoria": s["tipocategoria__nome"],
                    "total": s["total"],
                }
                for s in saidas
            ]
        })
    

class HistoricoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Historico.objects.all().order_by("-data")
    serializer_class = HistoricoSerializer
    permission_classes = [AllowAny]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["tipo", "descricao"]
    ordering_fields = ["data"]