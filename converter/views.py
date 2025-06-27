from django.shortcuts import render
import requests
from django.core.cache import cache


def converter_curracy(request):
    if request.method == 'POST':
        amount = float(request.POST['amount'])
        from_currency = request.POST['from_currency']
        to_currency = request.POST['to_currency']
        
        cache_key = f"exchange_rate_{from_currency}_{to_currency}"
        rate = cache.get(cache_key)
        
        if rate is None:
            url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
            response = requests.get(url)
            data = response.json()
            
            rate = data['rates'][to_currency]
        
            if rate is None:
                return render(request, 'converter/convert.html',
                            {
                                'error': 'Moeda de destino inválida ou não disponível.'
                            }
                            )
                #salva o cache por 12h
            cache.set(cache_key, rate, timeout=43200)
            
        converted_amount = amount * rate
        
        context = {
            'amount': amount,
            'from_currency': from_currency,
            'to_currency': to_currency,
            'converted_amount': round(converted_amount, 2)
        }
        
        return render(request, 'converter/result.html', context)

    return render(request, 'converter/convert.html')