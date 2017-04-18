from domain.models import Domain


def template_context(request):

    return {
        'domains_list': Domain.objects.all(),
        'user': request.user,
    }