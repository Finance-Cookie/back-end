from rest_framework import serializers
from .models import Produto

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"

    def validate_valor(self, value):
        if value <= 0:
            raise serializers.ValidationError("O valor do produto deve ser maior que zero.")
        return value