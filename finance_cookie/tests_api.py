from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from decimal import Decimal
from .models import FormaPagamento, TipoPagamento, Usuario, Cliente, Entrada, Saida, Venda, Compra

class FinanceCookieAPITestCase(APITestCase):
    def setUp(self):
        Usuario.objects.all().delete()
        Cliente.objects.all().delete()
        FormaPagamento.objects.all().delete()
        TipoPagamento.objects.all().delete()

        self.usuario = Usuario.objects.create(
            nome="Pedro Vitor",
            email="pedrovitor@cookie.com",
            senha_hash="hash_teste",
            saldo_fisico=Decimal("1000.00"),
            saldo_online=Decimal("1000.00")
        )
        self.forma_dinheiro = FormaPagamento.objects.create(nome="Dinheiro Físico")
        self.forma_pix = FormaPagamento.objects.create(nome="Pix Online")
        self.categoria = TipoPagamento.objects.create(nome="Geral Operacional")
        self.cliente = Cliente.objects.create(
            nome="Cliente Teste", email="cliente@teste.com", telefone="123",
            bairro="Centro", logradouro="Rua A", numero="10"
        )

    # --- CRUD COMPLETO: ENTRADAS ---
    def test_crud_completo_entrada(self):
        url_list = reverse('entradas-list')
        payload = {
            'valorTotal': '200.00',
            'descricao': 'Entrada Teste',
            'formapagamento': self.forma_dinheiro.id,
            'tipocategoria': self.categoria.id
        }
        
        # 1. CREATE (POST)
        response = self.client.post(url_list, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        entrada_id = response.data['id']

        # 2. READ (GET DETAIL)
        url_detail = reverse('entradas-detail', args=[entrada_id])
        response = self.client.get(url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['descricao'], 'Entrada Teste')

        # 3. UPDATE (PUT)
        payload['descricao'] = 'Entrada Alterada'
        response = self.client.put(url_detail, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['descricao'], 'Entrada Alterada')

        # 4. DELETE
        response = self.client.delete(url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # --- CRUD COMPLETO: SAÍDAS ---
    def test_crud_completo_saida(self):
        url_list = reverse('saidas-list')
        payload = {
            'valorTotal': '50.00',
            'descricao': 'Saida Teste',
            'formapagamento': self.forma_pix.id,
            'tipocategoria': self.categoria.id
        }

        # 1. CREATE
        response = self.client.post(url_list, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        saida_id = response.data['id']

        # 2. READ
        url_detail = reverse('saidas-detail', args=[saida_id])
        response = self.client.get(url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # 3. UPDATE
        payload['descricao'] = 'Saida Alterada'
        response = self.client.put(url_detail, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # 4. DELETE
        response = self.client.delete(url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # --- CRUD COMPLETO: VENDAS ---
    def test_crud_completo_venda(self):
        url_list = reverse('vendas-list')
        payload = {
            'valorTotal': '100.00',
            'formapagamento': self.forma_pix.id,
            'tipocategoria': self.categoria.id,
            'desconto': '0.00',
            'frete': '0.00',
            'cliente': self.cliente.id
        }

        # 1. CREATE
        response = self.client.post(url_list, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        venda_id = response.data['id']

        # 2. READ
        url_detail = reverse('vendas-detail', args=[venda_id])
        response = self.client.get(url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # 3. UPDATE
        payload['valorTotal'] = '120.00'
        response = self.client.put(url_detail, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # 4. DELETE
        response = self.client.delete(url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # --- CRUD COMPLETO: COMPRAS ---
    def test_crud_completo_compra(self):
        url_list = reverse('compras-list')
        payload = {
            'valorTotal': '0.00',
            'formapagamento': self.forma_dinheiro.id,
            'tipocategoria': self.categoria.id,
            'descricao': 'Compra Teste',
            'desconto': '0.00',
            'frete': '80.00'
        }

        # 1. CREATE
        response = self.client.post(url_list, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        compra_id = response.data['id']

        # 2. READ
        url_detail = reverse('compras-detail', args=[compra_id])
        response = self.client.get(url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # 3. UPDATE
        payload['descricao'] = 'Compra Alterada'
        response = self.client.put(url_detail, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # 4. DELETE
        response = self.client.delete(url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)