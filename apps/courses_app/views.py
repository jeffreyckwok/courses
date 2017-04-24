# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import Course
# Create your views here.
def index(request):
    context = {
     "courses": Course.objects.all(),
    }
    return render(request, "courses_app/index.html", context)

def addcourse(request):
    print request.POST
    Course.objects.create(course_name=request.POST['course'],description=request.POST['description'])
    return redirect('/')

def destroy(request, id):
    course_id = id
    context = {
    'id': Course.objects.get(id=course_id)
    }
    return render(request, 'courses_app/destroy.html', context)

def delete(request, id):
    delete_id = id
    Course.objects.get(id=delete_id).delete()
    return redirect('/')
