import requests.cookies
import json
from django.shortcuts import render
from query.apps import model
from .models import UserQuery

# Create your views here.


def search_page(request, *args, **kwargs):
    query = request.GET.get('query', None)
    if query:
        response = model.find(query)
    else:
        response = None

    if response and request.user.is_authenticated:
        UserQuery.objects.create(
            user=request.user,
            query=query,
            response=json.dumps(response, ensure_ascii=False),
        )

    return render(request, 'search/search_content.html', {'response': response, 'query': query})
