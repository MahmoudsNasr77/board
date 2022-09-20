from multiprocessing import context
from django.shortcuts import render,redirect

from course import urls
from .models import courses,comments
from django.views.generic import ListView
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required    
from django.contrib.auth.models import User
from .forms import commentForm

class CoursesList(ListView):
    model = courses
@login_required
def addComment(request,slug):
    if request.method=='POST':
      comment_form=commentForm(request.POST)
      if comment_form.is_valid():
            myform=comment_form.save(commit=False)
            myform.user=request.user
            myform.save()
            return redirect('/')
    else:
        comment_form=commentForm()   
    return render(request,'course/add_comment.html',{'comment_form':comment_form})

def single_course(request,slug):
    course=courses.objects.get(slug=slug)
    commentans=comments.objects.all()
    context={'course':course,'commentans':commentans}
    return render(request,'course/courses_detail.html',context)
'''


def add_job(request):
    if request.method=='POST':
      Job_form=Addjob(request.POST,request.FILES)
      if Job_form.is_valid():
            myform=Job_form.save(commit=False)
            myform.user=request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))
    else:
        Job_form=Addjob()   
    return render(request,'job/add_jobs.html',{'Job_form':Job_form})
'''