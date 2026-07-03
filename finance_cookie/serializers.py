from rest_framework import serializers
from .models import Cliente

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