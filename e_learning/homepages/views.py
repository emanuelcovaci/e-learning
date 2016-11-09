
from django.shortcuts import render_to_response

# Create your views here.
from domain.models import Domain


def home(request):
    domain = Domain.objects.all()
    if request.user.is_authenticated():
        template = 'homepages/home.html'
    else:
        template = 'homepages/index.html'
    return render_to_response(template,{
            'user': request.user,
             'domain':domain,
            })
