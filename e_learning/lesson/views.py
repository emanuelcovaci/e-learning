from django.shortcuts import render
from models import Domain
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import  get_object_or_404
from django.shortcuts import redirect
from .forms import CreateLessonForm
from lesson.models import Lesson
from django.contrib.auth.models import User

# Create your views here.
@login_required
def lesson(request,name,slug):
    domain = get_object_or_404(Domain, name=name)
    lesson = Lesson.objects.all().filter(slug=slug)
    context = {
        'domain':domain,
        'title':lesson[0].title,
        'image': lesson[0].image,
        'image2':lesson[0].image2,
        'image3':lesson[0].image3,
        'description': lesson[0].description,
        'author':lesson[0].author,
        'title_1':lesson[0].title_paragraf_1,
        'description_1':lesson[0].paragraf_1,
        'title_2': lesson[0].title_paragraf_2,
        'description_2': lesson[0].paragraf_2,
    }
    return render(request,'lesson/lectie.html',context)


@login_required
def create_lesson(request):
    current_user = request.user
    form = CreateLessonForm(request.POST or None, request.FILES or None,user=current_user)
    if request.method == 'POST':
        if form.is_valid():
            post = form.instance
            post.author = current_user
            form.save()
            return redirect('/'+post.domain.name)
    return render(request,'lesson/create_lesson.html',{
        'form':form,
    })

@login_required
def edit_lesson(request,slug):
    lesson = get_object_or_404(Lesson,slug=slug)
    domain = lesson.domain.name
    if lesson.author != request.user:
        return HttpResponseForbidden()
    form = CreateLessonForm(request.POST or None, request.FILES or None,
                        instance=lesson, user=request.user)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/lesson/'+domain+'/'+lesson.slug)
    return render (request,'lesson/create_lesson.html',{
        'form':form,
    })



@login_required
def list(request):
    current_user = request.user
    lessons = Lesson.objects.filter(author=current_user)
    domains = Domain.objects.all()
    print domains
    return render(request,'lesson/lessons_list.html',{
        'lessons':lessons,
        'domains':domains,
    })