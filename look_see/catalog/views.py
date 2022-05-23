from django.http import HttpResponse

from .models import Course


def index(request):

    course_list = Course.objects.all()
    return HttpResponse(course_list)
