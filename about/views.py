from django.shortcuts import render

# Create your views here.


def about_page(request, *args, **kwargs):
    return render(request, 'about/about_content.html', {})
