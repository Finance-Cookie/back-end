from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    bairro = models.CharField(max_length=100)
    logradouro = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)

    def __str__(self):
        return self.nome
    
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()

    def __str__(self):
        return self.nome
    
class TipoPagamento(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
class Item(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome
    
class FormaPagamento(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Saida(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField()
    valorTotal = models.DecimalField(max_digits=10, decimal_places=2)
    formapagamento = models.ForeignKey(FormaPagamento, on_delete=models.CASCADE)
    tipocategoria = models.ForeignKey(TipoPagamento, on_delete=models.CASCADE)

    def __str__(self):
        return f"Saída em {self.data.strftime('%Y-%m-%d %H:%M:%S')} - Valor Total: {self.valorTotal}"
    
class Entrada(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField()
    valorTotal = models.DecimalField(max_digits=10, decimal_places=2)
    formapagamento = models.ForeignKey(FormaPagamento, on_delete=models.CASCADE)
    tipocategoria = models.ForeignKey(TipoPagamento, on_delete=models.CASCADE)

    def __str__(self):
        return f"Entrada em {self.data.strftime('%Y-%m-%d %H:%M:%S')} - Valor Total: {self.valorTotal}"

class Compra(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField()
    valorTotal = models.DecimalField(max_digits=10, decimal_places=2)
    formapagamento = models.ForeignKey(FormaPagamento, on_delete=models.CASCADE)
    tipocategoria = models.ForeignKey(TipoPagamento, on_delete=models.CASCADE)
    desconto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    frete = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class ItemCompra(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantidade} x {self.item.nome} - Valor Unitário: {self.valor_unitario}"

class Venda(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    valorTotal = models.DecimalField(max_digits=10, decimal_places=2)
    formapagamento = models.ForeignKey(FormaPagamento, on_delete=models.CASCADE)
    tipocategoria = models.ForeignKey(TipoPagamento, on_delete=models.CASCADE)
    desconto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    frete = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"Venda em {self.data.strftime('%Y-%m-%d %H:%M:%S')} - Valor Total: {self.valorTotal}"
    
class ProdutoVenda(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantidade} x {self.produto.nome} - Valor Unitário: {self.valor_unitario}"