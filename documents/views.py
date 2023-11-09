from django.shortcuts import render

# Create your views here.


def documents_page(request, *args, **kwargs):
    return render(request, 'documents/documents_content.html', {})
