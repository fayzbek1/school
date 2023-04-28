from django.shortcuts import render
from .models import *
# Create your views here.

def test(request):
    return render(request,'mainapp/test.html')

def index(request):
    books = Kitoblar.objects.all()
    context = {
        'books' : books
    }

    return render(request,'mainapp/mainpage.html',context)

def teacher_table(request):
    teachers = Teachers.objects.all()
    context = {
        'teacher' : teachers
    }

    return render(request,'mainapp/teacher_table.html',context)