from django.contrib import admin
from .models import *

admin.site.register(Cliente)
admin.site.register(Produto)
admin.site.register(TipoPagamento)
admin.site.register(Item)
admin.site.register(FormaPagamento)
admin.site.register(Saida)
admin.site.register(Entrada)
admin.site.register(Compra)
admin.site.register(ItemCompra)
admin.site.register(Venda)
admin.site.register(ProdutoVenda)