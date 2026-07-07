from decimal import Decimal
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import (
    Cliente,
    Produto,
    Item,
    TipoPagamento,
    FormaPagamento,
)


class ClientsProductsAPITest(APITestCase):
    def test_list_clients(self):
        Cliente.objects.create(nome='A', email='a@example.com', telefone='1', bairro='X', logradouro='Y', numero='10')
        url = reverse('clientes-list')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        data = resp.json()
        self.assertIn('results', data)
        self.assertIsInstance(data['results'], list)

    def test_create_client(self):
        url = reverse('clientes-list')
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
        url = reverse('produtos-list')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        data = resp.json()
        self.assertIn('results', data)
        self.assertIsInstance(data['results'], list)

    def test_create_product(self):
        url = reverse('produtos-list')
        payload = {'nome': 'Prod', 'valor': '12.5', 'descricao': 'desc'}
        resp = self.client.post(url, payload, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Produto.objects.filter(nome='Prod').count(), 1)

    def test_item_and_tipo_and_forma_endpoints(self):
        # Item
        url_item = reverse('items-list')
        payload_item = {'nome': 'Serviço A', 'valor': '15.00'}
        resp_item = self.client.post(url_item, payload_item, format='json')
        self.assertEqual(resp_item.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Item.objects.exists())

        # TipoPagamento
        url_tipo = reverse('tipospagamento-list')
        payload_tipo = {'nome': 'OperaçãoTeste'}
        resp_tipo = self.client.post(url_tipo, payload_tipo, format='json')
        self.assertEqual(resp_tipo.status_code, status.HTTP_201_CREATED)

        # FormaPagamento
        url_forma = reverse('formaspagamento-list')
        payload_forma = {'nome': 'Dinheiro'}
        resp_forma = self.client.post(url_forma, payload_forma, format='json')
        self.assertEqual(resp_forma.status_code, status.HTTP_201_CREATED)

    def test_entrada_saida_flow(self):
        tipo = TipoPagamento.objects.create(nome='TesteEntrada')
        forma = FormaPagamento.objects.create(nome='PIX')

        # Entrada
        url_ent = reverse('entradas-list')
        payload_ent = {
            'descricao': 'Entrada X',
            'valorTotal': '100.00',
            'formapagamento': forma.id,
            'tipocategoria': tipo.id,
        }
        resp_ent = self.client.post(url_ent, payload_ent, format='json')
        self.assertEqual(resp_ent.status_code, status.HTTP_201_CREATED)

        # Saida
        url_sai = reverse('saidas-list')
        payload_sai = {
            'descricao': 'Saida X',
            'valorTotal': '50.00',
            'formapagamento': forma.id,
            'tipocategoria': tipo.id,
        }
        resp_sai = self.client.post(url_sai, payload_sai, format='json')
        self.assertEqual(resp_sai.status_code, status.HTTP_201_CREATED)

    def test_compra_and_itemcompra_flow(self):
        forma = FormaPagamento.objects.create(nome='PIX2')
        tipo = TipoPagamento.objects.create(nome='CompraTipo')

        url_compra = reverse('compras-list')
        payload_compra = {
            'descricao': 'Compra Teste',
            'valorTotal': '0',
            'formapagamento': forma.id,
            'tipocategoria': tipo.id,
            'desconto': '0',
            'frete': '0',
        }
        resp_compra = self.client.post(url_compra, payload_compra, format='json')
        self.assertEqual(resp_compra.status_code, status.HTTP_201_CREATED)

        compra_id = resp_compra.json()['id']

        # Criar ItemCompra
        item = Item.objects.create(nome='ItemComp', valor=5.00)
        url_itemcomp = reverse('itemcompras-list')
        payload_itemcomp = {
            'item': item.id,
            'compra': compra_id,
            'quantidade': 2,
            'valor_unitario': '5.00',
        }
        resp_itemcomp = self.client.post(url_itemcomp, payload_itemcomp, format='json')
        self.assertEqual(resp_itemcomp.status_code, status.HTTP_201_CREATED)

    def test_venda_and_produtovenda_flow(self):
        forma = FormaPagamento.objects.create(nome='CartaoTeste')
        tipo = TipoPagamento.objects.create(nome='VendaTipo')
        cliente = Cliente.objects.create(nome='C V', email='cv@example.com', telefone='1', bairro='B', logradouro='L', numero='1')
        produto = Produto.objects.create(nome='P1', valor=10.00, descricao='d')

        url_venda = reverse('vendas-list')
        payload_venda = {
            'valorTotal': '0',
            'formapagamento': forma.id,
            'tipocategoria': tipo.id,
            'desconto': '0',
            'frete': '0',
            'cliente': cliente.id,
        }
        resp_venda = self.client.post(url_venda, payload_venda, format='json')
        self.assertEqual(resp_venda.status_code, status.HTTP_201_CREATED)

        venda_id = resp_venda.json()['id']

        url_prodv = reverse('produtovenda-list')
        payload_prodv = {
            'produto': produto.id,
            'venda': venda_id,
            'quantidade': 1,
            'valor_unitario': '10.00',
        }
        resp_prodv = self.client.post(url_prodv, payload_prodv, format='json')
        self.assertEqual(resp_prodv.status_code, status.HTTP_201_CREATED)