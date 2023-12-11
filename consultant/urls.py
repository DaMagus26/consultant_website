"""consultant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from query.views import search_page
from history.views import history_page
from documents.views import documents_page
from about.views import about_page
from authentication.views import SignUpView, LoginView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', search_page, name='search_page'),
    path('history/', history_page, name='history_page'),
    path('documents/', documents_page, name='documents_page'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='search_page'), name='logout'),
    path('about/', about_page, name='about_page'),
    path('', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
