from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from decimal import Decimal
from .models import Usuario


class UsersAPITest(APITestCase):
    def test_register_user_success(self):
        # O Django usa o basename 'users' do seu router + o nome da action do método
        url = reverse('users-register')
        payload = {
            'nome': 'Elder',
            'email': 'elder@example.com',
            'senha': '123456',
        }
        resp = self.client.post(url, payload, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Usuario.objects.filter(email='elder@example.com').count(), 1)
        self.assertIn('message', resp.json())

    def test_register_user_invalid_fields(self):
        url = reverse('users-register')
        payload = {
            'nome': '   ',  # Nome inválido (apenas espaços)
            'email': 'elder2@example.com',
            'senha': '123456',
        }
        resp = self.client.post(url, payload, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_me_get_and_put_flow(self):
        # Cria usuário inicial no banco para testar o endpoint /me/
        u = Usuario.objects.create(
            nome='U1',
            email='U1@EXAMPLE.COM ',  # Testando a limpeza automática de string
            senha_hash='hash',
        )

        # Acessa a action customizada 'me' mapeada pelo router
        url_me = reverse('users-me')

        # 1. Testando o GET
        resp_get = self.client.get(url_me)
        self.assertEqual(resp_get.status_code, status.HTTP_200_OK)
        self.assertEqual(resp_get.json()['email'], 'u1@example.com')  # Verificando se normalizou para minúsculo

        # 2. Testando o PUT com valores válidos
        resp_put = self.client.put(
            url_me,
            {
                'nome': 'U1 Alterado',
                'saldo_fisico': '100.50',
                'saldo_online': '20.25',
            },
            format='json',
        )
        self.assertEqual(resp_put.status_code, status.HTTP_200_OK)
        self.assertEqual(resp_put.json()['nome'], 'U1 Alterado')
        self.assertEqual(Decimal(resp_put.json()['saldo_fisico']), Decimal('100.50'))
        self.assertEqual(Decimal(resp_put.json()['saldo_online']), Decimal('20.25'))

    def test_me_update_invalid_negative_balance(self):
        Usuario.objects.create(nome='Test User', email='test@example.com', senha_hash='hash')

        url_me = reverse('users-me')

        resp_put = self.client.put(
            url_me,
            {
                'saldo_fisico': '-50.00',
            },
            format='json',
        )
        self.assertEqual(resp_put.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('saldo_fisico', resp_put.json())