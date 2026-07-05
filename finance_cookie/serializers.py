from rest_framework import serializers
from .models import (
    Produto,
    Cliente,
    Item,
    TipoPagamento,
    FormaPagamento,
    Entrada,
    Saida,
    Compra,
    ItemCompra,
    Venda,
    ProdutoVenda,
    Usuario,
)

from django.contrib.auth.hashers import make_password

# US01 - Sem segurança/autenticação: não usada aqui por enquanto.





class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"

    def validate_valor(self, value):
        if value <= 0:
            raise serializers.ValidationError("O valor do produto deve ser maior que zero.")
        return value


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = [
            'id',
            'nome',
            'email',
            'telefone',
            'bairro',
            'logradouro',
            'numero',
        ]

    def validate(self, attrs):
        campos_texto = ['nome', 'telefone', 'bairro', 'logradouro', 'numero']

        for campo in campos_texto:
            valor = attrs.get(campo)
            if valor is not None:
                valor = str(valor).strip()
                if not valor:
                    raise serializers.ValidationError({
                        campo: 'Este campo é obrigatório.'
                    })

                attrs[campo] = valor

        email = attrs.get('email')
        if email is not None:
            attrs['email'] = email.strip().lower()

        return attrs


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

    def validate_valor(self, value):
        if value is None or value <= 0:
            raise serializers.ValidationError('O valor do item deve ser maior que zero.')
        return value


class TipoPagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPagamento
        fields = '__all__'


class FormaPagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormaPagamento
        fields = '__all__'


class EntradaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrada
        fields = '__all__'


class SaidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saida
        fields = '__all__'


class ItemCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCompra
        fields = '__all__'


class CompraSerializer(serializers.ModelSerializer):
    itens = ItemCompraSerializer(many=True, source='itemcompra_set', required=False, read_only=True)

    class Meta:
        model = Compra
        fields = '__all__'


class ProdutoVendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdutoVenda
        fields = '__all__'


class VendaSerializer(serializers.ModelSerializer):
    itens = ProdutoVendaSerializer(many=True, source='produtovenda_set', required=False, read_only=True)

    class Meta:
        model = Venda
        fields = '__all__'
