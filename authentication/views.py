from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomUserCreationForm
from .forms import CustomAuthenticationForm
from django.contrib.auth import authenticate, login


class SignUpView(View):
    def get(self, request, *args, **kwargs):
        form = CustomUserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')  # Log the user in
            return redirect('search_page')  # Adjust as needed
        return render(request, 'registration/signup.html', {'form': form})



class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = CustomAuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user:
                login(request, user)
                return redirect('search_page')  # Adjust as needed
            else:
                form.add_error(None, 'Invalid email or password.')
        return render(request, 'registration/login.html', {'form': form})
