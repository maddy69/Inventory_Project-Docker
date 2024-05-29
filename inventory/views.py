from django.urls import get_resolver
from django.shortcuts import render

def url_list(request):
    host = request.get_host()
    base_url = f'http://{host}'
    url_patterns = [
        (f'{base_url}/api/products', 'List all products'),
        (f'{base_url}/api/products/<int:pk>', 'Retrieve a specific product by ID'),
    ]
    return render(request, 'url_list.html', {'url_patterns': url_patterns})



