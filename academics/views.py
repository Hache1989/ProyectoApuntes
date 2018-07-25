from django.shortcuts import render
from . models import Study,Subject
from django.http import Http404, HttpResponse
from django.contrib.staticfiles.templatetags.staticfiles import static
import os
from django.conf import settings


def main(request):
    subjects1 = Subject.objects.filter(semester=1).order_by('course','code')
    subjects2 = Subject.objects.filter(semester=2).order_by('course','code')
    return render(request, 'academics/mainPage.html',{'subjects1':subjects1, 'subjects2':subjects2})

def subject(request,subject_code):
    try:
        subject = Subject.objects.get(code=subject_code)
    except:
        raise Http404("Ups, esa asignatura no existe.")
    references = subject.references_set.all()
    moduls = subject.modul_set.all()
    return render(request, 'academics/subjectPage.html',
                  {'subject' : subject,
                   'references':references,
                   'moduls': moduls})

def prueba(request):
    return render(request,'academics/pruebaPage.html',{})

def verPdf(request):
    url = static('DJANGO.pdf')
    print(url)
    with open(os.path.join(settings.STATIC_ROOT, url), 'r') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response
    pdf.closed