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
    Historico,
)

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
                if not valor and not self.partial:  # Só barra se não for um update parcial (PATCH)
                    raise serializers.ValidationError({
                        campo: 'Este campo é obrigatório.'
                    })
                if valor:
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


class HistoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historico
        fields = "__all__"
        

class UsuarioSerializer(serializers.ModelSerializer):
    senha = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'email', 'saldo_fisico', 'saldo_online', 'criado_em', 'senha']
        read_only_fields = ['id', 'criado_em']

    def validate_nome(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("O nome não pode ser composto apenas por espaços.")
        return value.strip()

    def validate_saldo_fisico(self, value):
        if value < 0:
            raise serializers.ValidationError("O saldo físico não pode ser negativo.")
        return value

    def validate_saldo_online(self, value):
        if value < 0:
            raise serializers.ValidationError("O saldo online não pode ser negativo.")
        return value

    def create(self, validated_data):
        senha_pura = validated_data.pop('senha', 'hash_provisoria')
        validated_data['senha_hash'] = senha_pura
        return super().create(validated_data)