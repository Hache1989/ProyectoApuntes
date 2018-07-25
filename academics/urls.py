from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.main, name="academyMainPage"),
    url(r'^subject/(?P<subject_code>\d+)$', views.subject, name="subject"),
    url('prueba', views.prueba, name="prueba"),
    url('verpdf', views.verPdf, name="verpdf"),

]

