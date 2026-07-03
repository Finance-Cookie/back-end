import json
from decimal import Decimal

from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError

from .models import Cliente, Produto


def serialize_cliente(c: Cliente):
    return {
        'id': c.id,
        'nome': c.nome,
        'email': c.email,
        'telefone': c.telefone,
        'bairro': c.bairro,
        'logradouro': c.logradouro,
        'numero': c.numero,
    }


def serialize_produto(p: Produto):
    return {
        'id': p.id,
        'nome': p.nome,
        'valor': float(p.valor) if p.valor is not None else 0,
        'descricao': p.descricao,
    }


@csrf_exempt
def clients_list_create(request):
    if request.method == 'GET':
        qs = Cliente.objects.all()
        data = [serialize_cliente(c) for c in qs]
        return JsonResponse(data, safe=False)

    if request.method == 'POST':
        try:
            payload = json.loads(request.body.decode('utf-8') or '{}')
        except Exception:
            return HttpResponseBadRequest('Invalid JSON')

        try:
            c = Cliente.objects.create(
                nome=payload.get('nome', ''),
                email=payload.get('email', ''),
                telefone=payload.get('telefone', ''),
                bairro=payload.get('bairro', ''),
                logradouro=payload.get('logradouro', ''),
                numero=payload.get('numero', ''),
            )
            return JsonResponse(serialize_cliente(c), status=201)
        except ValidationError as e:
            return JsonResponse({'errors': e.message_dict}, status=400)

    return HttpResponseBadRequest('Method not allowed')


@csrf_exempt
def products_list_create(request):
    if request.method == 'GET':
        qs = Produto.objects.all()
        data = [serialize_produto(p) for p in qs]
        return JsonResponse(data, safe=False)

    if request.method == 'POST':
        try:
            payload = json.loads(request.body.decode('utf-8') or '{}')
        except Exception:
            return HttpResponseBadRequest('Invalid JSON')

        try:
            valor = payload.get('valor')
            if valor is None:
                valor = 0
            # ensure Decimal
            valor = Decimal(str(valor))

            p = Produto.objects.create(
                nome=payload.get('nome', ''),
                valor=valor,
                descricao=payload.get('descricao', ''),
            )
            return JsonResponse(serialize_produto(p), status=201)
        except ValidationError as e:
            return JsonResponse({'errors': e.message_dict}, status=400)
        except Exception as ex:
            return JsonResponse({'errors': str(ex)}, status=400)

    return HttpResponseBadRequest('Method not allowed')
