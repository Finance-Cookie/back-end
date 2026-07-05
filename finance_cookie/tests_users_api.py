from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Usuario


class UsersAPITest(APITestCase):
    def test_register_user_success(self):
        url = '/api/users/register'
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
        url = '/api/users/register'
        payload = {

            'nome': '',
            'email': 'elder2@example.com',
            'senha': '123456',
        }
        resp = self.client.post(url, payload, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_me_get_and_put_flow(self):
        # cria usuário via model (sem segurança/autenticação)
        u = Usuario.objects.create(
            nome='U1',
            email='u1@example.com',
            senha_hash='hash',
        )

        resp_get = self.client.get('/api/users/me/')

        self.assertEqual(resp_get.status_code, status.HTTP_200_OK)
        self.assertEqual(resp_get.json()['email'], 'u1@example.com')

        resp_put = self.client.put(
            '/api/users/me/',
            {
                'saldo_fisico': '100.50',
                'saldo_online': '20.25',
            },
            format='json',
        )
        self.assertEqual(resp_put.status_code, status.HTTP_200_OK)
        self.assertEqual(float(resp_put.json()['saldo_fisico']), 100.50)
        self.assertEqual(float(resp_put.json()['saldo_online']), 20.25)


