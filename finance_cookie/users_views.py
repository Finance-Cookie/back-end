from decimal import Decimal

from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Usuario


def _serialize_me(u: Usuario) -> dict:
    return {
        "id": u.id,
        "nome": u.nome,
        "email": u.email,
        "criado_em": u.criado_em,
        "saldo_fisico": str(u.saldo_fisico),
        "saldo_online": str(u.saldo_online),
    }


class UsersViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def create(self, request):
        # POST /api/users/register/
        nome = (request.data.get("nome") or "").strip()
        email = (request.data.get("email") or "").strip().lower()
        senha = request.data.get("senha")

        if not nome or not email or not senha:
            return Response({"detail": "Informações incorretas, tente novamente!"}, status=status.HTTP_400_BAD_REQUEST)

        if Usuario.objects.filter(email__iexact=email).exists():
            return Response({"detail": "Informações incorretas, tente novamente!"}, status=status.HTTP_400_BAD_REQUEST)

        u = Usuario.objects.create(
            nome=nome,
            email=email,
            senha_hash=make_password(str(senha)),
        )

        return Response({
            **_serialize_me(u),
            "message": "Cadastro realizado com sucesso!",
        }, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=["get"], url_path="me")
    def me_get(self, request):
        # GET /api/users/me/
        # Sem login, “me” = primeiro usuário criado.
        u = Usuario.objects.order_by("-criado_em").first()
        if not u:
            return Response({"detail": "Nenhum usuário cadastrado"}, status=status.HTTP_404_NOT_FOUND)
        return Response(_serialize_me(u), status=status.HTTP_200_OK)

    @action(detail=False, methods=["put"], url_path="me")
    def me_put(self, request):
        # PUT /api/users/me/
        u = Usuario.objects.order_by("-criado_em").first()
        if not u:
            return Response({"detail": "Nenhum usuário cadastrado"}, status=status.HTTP_404_NOT_FOUND)

        nome = request.data.get("nome")
        email = request.data.get("email")
        senha = request.data.get("senha")
        saldo_fisico = request.data.get("saldo_fisico")
        saldo_online = request.data.get("saldo_online")

        if nome is not None:
            nome = str(nome).strip()
            if not nome:
                return Response({"detail": "Informações incorretas, tente novamente!"}, status=status.HTTP_400_BAD_REQUEST)
            u.nome = nome

        if email is not None:
            email = str(email).strip().lower()
            if not email:
                return Response({"detail": "Informações incorretas, tente novamente!"}, status=status.HTTP_400_BAD_REQUEST)
            if Usuario.objects.exclude(pk=u.pk).filter(email__iexact=email).exists():
                return Response({"detail": "Informações incorretas, tente novamente!"}, status=status.HTTP_400_BAD_REQUEST)
            u.email = email

        if senha is not None and str(senha).strip() != "":
            u.senha_hash = make_password(str(senha))

        try:
            if saldo_fisico is not None:
                u.saldo_fisico = Decimal(str(saldo_fisico))
            if saldo_online is not None:
                u.saldo_online = Decimal(str(saldo_online))
        except Exception:
            return Response({"detail": "Informações incorretas, tente novamente!"}, status=status.HTTP_400_BAD_REQUEST)

        u.save()

        return Response({
            **_serialize_me(u),
            "message": "Dados salvos com sucesso!",
        }, status=status.HTTP_200_OK)

