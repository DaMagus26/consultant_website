from django.shortcuts import render

# Create your views here.


def history_page(request, *args, **kwargs):
    return render(request, 'history/history_content.html', {})
