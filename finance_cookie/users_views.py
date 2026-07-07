from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Usuario
from .serializers import UsuarioSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all().order_by('id')
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny]

    def get_current_user(self):
        """
        Retorna ou cria o primeiro usuário do banco para simular a sessão
        enquanto o módulo de autenticação não é implementado.
        """
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
        """
        Endpoint customizado para gerenciar os dados do próprio perfil.
        Mapeia para /api/users/me/
        """
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
        """
        Endpoint customizado para registro simplificado de novos usuários.
        Mapeia para /api/users/register/
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Usuário cadastrado com sucesso!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)