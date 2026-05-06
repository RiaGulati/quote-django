from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Quote
import random
import json

# ============ TEMPLATE VIEWS ============

def home(request):
    quotes = Quote.objects.all()
    quote = random.choice(list(quotes))
    return render(request, 'quotes/home.html', {'quote': quote})

def all_quotes(request):
    quotes = Quote.objects.all()
    return render(request, 'quotes/all_quotes.html', {'quotes': quotes})


# ============ API VIEWS ============

def random_quote_api(request):
    quotes = Quote.objects.all()
    quote = random.choice(list(quotes))
    return JsonResponse({'id': quote.id, 'text': quote.text, 'author': quote.author})

@csrf_exempt
def quotes_api(request):
    if request.method == 'GET':
        quotes = Quote.objects.all()
        data = [{'id': q.id, 'text': q.text, 'author': q.author} for q in quotes]
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        quote = Quote.objects.create(text=data['text'], author=data['author'])
        return JsonResponse({'id': quote.id, 'text': quote.text, 'author': quote.author}, status=201)

@csrf_exempt
def quote_detail_api(request, id):
    try:
        quote = Quote.objects.get(id=id)
    except Quote.DoesNotExist:
        return JsonResponse({'error': 'Quote not found'}, status=404)
    
    if request.method == 'GET':
        return JsonResponse({'id': quote.id, 'text': quote.text, 'author': quote.author})
    elif request.method == 'PUT':
        data = json.loads(request.body)
        if 'text' in data:
            quote.text = data['text']
        if 'author' in data:
            quote.author = data['author']
        quote.save()
        return JsonResponse({'id': quote.id, 'text': quote.text, 'author': quote.author})
    elif request.method == 'DELETE':
        quote.delete()
        return JsonResponse({'message': 'Quote deleted'})