from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from .forms import LoginForm, JoinForm

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        user =form.authenticate()
        if user is not None:
            login(request, user)
            return redirect("/")

    context = {
        "form": form,
        "title": "Login",
    }
    return render(request, 'forms.html', context)

def register_view(request):
    form = JoinForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()

        #login
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("/")
    context = {
        "form": form,
        "title": "Join",
    }
    return render(request, 'forms.html', context)

def logout_view(request):
    logout(request)
    return redirect("/")
