from django.shortcuts import render
from models import Domain
from django.contrib.auth.decorators import login_required
from django.shortcuts import  get_object_or_404

from lesson.models import Lesson

# Create your views here.

@login_required
def Domain(request, kind):
    domains = Domain.objects.all()
    page_domain = get_object_or_404(Domain, name=kind)
    lesson = Lesson.objects.all().filter(domain=page_domain,
                                             status=False).order_by(
                                                 '-id')
    return render(request, 'domain/domain.html', {
        'domain': domains,
        'kind': page_domain,

    },
                  )
