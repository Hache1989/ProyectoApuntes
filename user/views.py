from django.shortcuts import render,redirect
from .forms import signupForm, loginForm
from django.contrib.auth import login, authenticate


def signupPage(request):
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('landingPage')
    else:
        form = signupForm()
    return render(request, 'user/signupPage.html', {'form': form})

def profilePage(request):
    return render(request, 'user/profilePage.html', {})



