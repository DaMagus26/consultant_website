import json
from django.shortcuts import render
from query.models import UserQuery
from django.contrib.auth.decorators import login_required
# Create your views here.


def history_page(request, *args, **kwargs):
    queries = UserQuery.objects.filter(user=request.user).order_by('-created_at')
    queries = [{'query': q.query, 'response': json.loads(q.response)} for q in queries]
    print(queries)
    return render(request, 'history/history_content.html', {'queries': queries})
