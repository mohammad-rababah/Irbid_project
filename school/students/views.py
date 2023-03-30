from django.http import HttpResponse
from django.shortcuts import render

# show page to front end
# Create your views here.
from django.template import loader
from .models import Student


def hello(request):
    student = Student(first_name="ahmad", last_name="khalid", avg=70.0, age=21)
    student.save()
    return HttpResponse("HEllo")


def hi(request):
    data = Student.objects.all()  # array 0 --- len
    return HttpResponse(data[1].first_name + "\t" + data[1].last_name + "\t" +
                        str(data[1].avg) + "\t" + str(data[1].age)
                        )


def stdlist(request):
    t = loader.get_template('first.html')
    return HttpResponse(t.render())


def second(request):
    template = loader.get_template('second.html')
    return HttpResponse(template.render())


def newLsit(request):
    data = Student.objects.all()
    template = loader.get_template('table.html')
    ctx = {
        'data': data,
        'test': 'hello'
    }

    return HttpResponse(template.render(ctx, request))
