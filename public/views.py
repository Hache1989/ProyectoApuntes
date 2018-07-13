from django.shortcuts import render


def landingPage(request):

    return render(request, 'public/landingPage.html', {})


