from django.contrib.auth import logout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})

@login_required
def user_logout(request):
    logout(request)
    return render(request, 'registration/logged_out.html', {})