from django.shortcuts import render
from models import Domain
from django.contrib.auth.decorators import login_required
from django.shortcuts import  get_object_or_404
from django.shortcuts import redirect
from .forms import CreateLessonForm
from lesson.models import Lesson
from django.contrib.auth.models import User

# Create your views here.
@login_required
def lesson(request,name,slug):
    domain = get_object_or_404(Domain, name=name)
    lesson = Lesson.objects.values('title', 'image', 'image2','image3','description','author',
                                   'creation_date','domain','title_paragraf_1',
                                   'paragraf_1','title_paragraf_2','paragraf_2',
                                  ).filter(slug=slug)
    author_id = lesson[0].get('author')
    author = list(User.objects.values('username').filter(id=author_id))

    context = {
        'domain':domain,
        'title':lesson[0].get('title'),
        'image':"/media/" +lesson[0].get('image'),
        'image2':"/media/" +lesson[0].get('image2'),
        'image3':"/media/" + lesson[0].get('image3'),
        'description': lesson[0].get('description'),
        'author':author[0].get('username'),
        'title_1':lesson[0].get('title_paragraf_1'),
        'description_1':lesson[0].get('paragraf_1'),
        'title_2': lesson[0].get('title_paragraf_2'),
        'description_2': lesson[0].get('paragraf_2'),

    }
    return render(request,'lesson/lectie.html',context)


@login_required
def create_lesson(request):
    current_user = request.user
    print current_user
    form = CreateLessonForm(request.POST or None, request.FILES or None,user=current_user)
    if request.method == 'POST':
        if form.is_valid():
            post = form.instance
            post.author = current_user
            form.save()
            return redirect('/')
    return render(request,'lesson/create_lesson.html',{
        'form':form,
    })