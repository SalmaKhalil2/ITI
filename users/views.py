from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from projects.models import Project
from django.contrib.auth import logout

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True  
            user.save()
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = RegistrationForm()
    
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile_view(request):
    return render(request, 'users/profile.html')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from projects.models import Project

@login_required
def profile_view(request):
    projects = Project.objects.filter(owner=request.user).order_by('-created_at')
    return render(request, 'users/profile.html', {'projects': projects})

def logout_view(request):
    logout(request)
    return redirect('landing')