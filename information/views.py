from django.shortcuts import render
from information.models import Course
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    mymembers = Course.objects.all().values()
    context = {'lastname' : 'Aryan FIrazz',
               'mymembers': mymembers,
               'greeting' : 1,}
    return render (request,"index.html",context)

def course(request):
    if request.method == 'POST':
        c_code = request.POST['code' ]
        c_desc = request.POST[ 'desc' ]
        data=Course(code=c_code, description=c_desc)
        data. save()
        mymembers = Course.objects.all().values()
        dict = {
        'message' : 'Data Save',
        'mymembers': mymembers,
    }
    else:
        mymembers = Course.objects.all().values()
        dict = {
    'message':'Unsuccess',
    'mymembers': mymembers,
    }
        
    return render (request , "course.html", dict)

