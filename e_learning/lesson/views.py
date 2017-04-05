from django.shortcuts import render
from models import Domain
from django.contrib.auth.decorators import login_required
from django.shortcuts import  get_object_or_404

from lesson.models import Lesson

# Create your views here.
@login_required
def lesson(request,name,slug):
    domain = get_object_or_404(Domain, name=name)
    lesson = Lesson.objects.values('title', 'image', 'image2','image3','image4','description','author',
                                   'creation_date','timePost','domain','title_paragraf_1',
                                   'paragraf_1','title_paragraf_2','paragraf_2',
                                  ).filter(slug=slug)

    context = {
        'domain':domain,
        'title':lesson[0].get('title'),
        'image':"/media/" +lesson[0].get('image'),
        'image2':"/media/" +lesson[0].get('image2'),
        'image3':"/media/" + lesson[0].get('image3'),
        'image4':"/media/" + lesson[0].get('image4'),
        'description': lesson[0].get('description'),
        'author':lesson[0].get('author'),
        'title_1':lesson[0].get('title_paragraf_1'),
        'description_1':lesson[0].get('paragraf_1'),
        'title_2': lesson[0].get('title_paragraf_2'),
        'description_2': lesson[0].get('paragraf_2'),

    }
    return render(request,'lesson/lectie.html',context)