from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url('signup', views.signupPage, name="signupPage"),
    url('profile', login_required(views.profilePage), name="profilePage"),
    url('login', auth_views.login, {'template_name': 'user/loginPage.html'}, name="loginPage"),
    url('logout', auth_views.logout, name="logoutPage"),
]

