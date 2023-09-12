from django.db.models import Count, Q

from compe.models import Problem, Choice

def common(request):
    context = {
        "problems": Problem.objects.all(),
        "choice": Choice.objects.all(),
    }
    return context
