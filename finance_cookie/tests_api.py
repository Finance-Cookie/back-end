from decimal import Decimal

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Cliente, Produto


class ClientsProductsAPITest(APITestCase):
    def test_list_clients(self):
        Cliente.objects.create(nome='A', email='a@example.com', telefone='1', bairro='X', logradouro='Y', numero='10')
        url = '/api/clients/'
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertIsInstance(resp.json(), list)

    def test_create_client(self):
        url = '/api/clients/'
        payload = {
            'nome': 'Novo',
            'email': 'novo@example.com',
            'telefone': '99',
            'bairro': 'B',
            'logradouro': 'L',
            'numero': '1'
        }
        resp = self.client.post(url, payload, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cliente.objects.filter(email='novo@example.com').count(), 1)

    def test_list_products(self):
        Produto.objects.create(nome='P', valor=Decimal('9.99'), descricao='d')
        url = '/api/products/'
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertIsInstance(resp.json(), list)

    def test_create_product(self):
        url = '/api/products/'
        payload = {'nome': 'Prod', 'valor': '12.5', 'descricao': 'desc'}
        resp = self.client.post(url, payload, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Produto.objects.filter(nome='Prod').count(), 1)
