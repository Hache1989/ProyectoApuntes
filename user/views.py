from django.shortcuts import render,redirect
from .forms import signupForm, loginForm, userForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User



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

def settingsPage(request):
    if request.method == 'POST':
        form = userForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=request.user.username)
            user.profile.bio = request.POST['bio']
            print (user.profile.bio)
            user.profile.save()
            return redirect('profilePage')
    else:
        form = userForm(instance=request.user.profile)
    return render(request, 'user/settingsPage.html',{'form':form})



