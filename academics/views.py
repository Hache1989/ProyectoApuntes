from django.shortcuts import render
from . models import Study

def main(request):
    studies = Study.objects.all()
    return render(request, 'academics/mainPage.html',{'studies':studies})