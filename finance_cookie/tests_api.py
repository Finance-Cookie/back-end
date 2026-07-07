from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from decimal import Decimal
from .models import FormaPagamento, TipoPagamento, Usuario, Cliente

class FinanceCookieAPITestCase(APITestCase):
    def setUp(self):
        Usuario.objects.all().delete()
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

    def test_crud_usuario_saldos_endpoint(self):
        url = reverse('usuarios-saldos', args=[self.usuario.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(float(response.data['saldo_total']), 2000.00)

    def test_criar_e_deletar_entrada_modifica_saldo_fisico(self):
        url_list = reverse('entradas-list')
        payload = {
            'valorTotal': '250.00',
            'descricao': 'Entrada em Espécie',
            'formapagamento': self.forma_dinheiro.id,
            'tipocategoria': self.categoria.id
        }
        response = self.client.post(url_list, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.usuario.refresh_from_db()
        self.assertEqual(self.usuario.saldo_fisico, Decimal("1250.00"))

        url_detail = reverse('entradas-detail', args=[response.data['id']])
        response_del = self.client.delete(url_detail)
        self.assertEqual(response_del.status_code, status.HTTP_204_NO_CONTENT)
        self.usuario.refresh_from_db()
        self.assertEqual(self.usuario.saldo_fisico, Decimal("1000.00"))

    def test_criar_saida_debitando_do_saldo_online(self):
        url = reverse('saidas-list')
        payload = {
            'valorTotal': '100.00',
            'descricao': 'Assinatura Cloud',
            'formapagamento': self.forma_pix.id,
            'tipocategoria': self.categoria.id
        }
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.usuario.refresh_from_db()
        self.assertEqual(self.usuario.saldo_online, Decimal("900.00"))

    def test_venda_adiciona_ao_saldo_online(self):
        url = reverse('vendas-list')
        payload = {
            'valorTotal': '350.00',
            'formapagamento': self.forma_pix.id,
            'tipocategoria': self.categoria.id,
            'desconto': '0.00',
            'frete': '0.00',
            'cliente': self.cliente.id
        }
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.usuario.refresh_from_db()
        self.assertEqual(self.usuario.saldo_online, Decimal("1350.00"))

    def test_compra_subtrai_do_saldo_fisico(self):
        url = reverse('compras-list')
        payload = {
            'valorTotal': '150.00',
            'formapagamento': self.forma_dinheiro.id,
            'tipocategoria': self.categoria.id,
            'descricao': 'Compra de Insumos'
        }
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.usuario.refresh_from_db()
        self.assertEqual(self.usuario.saldo_fisico, Decimal("850.00"))