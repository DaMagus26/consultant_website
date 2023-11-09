from django.shortcuts import render

# Create your views here.


def search_page(request, *args, **kwargs):
    return render(request, 'search/search_content.html', {})
