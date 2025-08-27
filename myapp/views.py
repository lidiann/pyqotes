from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages

from .forms import RegisterForm


@login_required
def dashboard(request):
    return render(request, 'myapp/dashboard.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            messages.success(request, 'Account created and logged in successfully.')
            return redirect('dashboard')  # Redirect to dashboard
    else:
        form = RegisterForm()
    return render(request, 'myproject/myapp/templates/registration/register.html', {'form': form})
