from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def register_view(request):
    form = UserCreationForm(request.POST or None)
    context = { 'form': form }
    if form.is_valid():
        user = form.save()
        return redirect('/login')
    return render(request, 'accounts/register.html', context)

def login_view(request):
    form = AuthenticationForm(request, data=request.POST)
    context = { 'form': form }
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
        else:
            context['form'] = AuthenticationForm(request)
    return render(request, "accounts/login.html", context)
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/login/')
    return render(request, 'accounts/logout.html', {})
