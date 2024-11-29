from django.shortcuts import render
from .models import Student


def students_list(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    if title is not None and content is not None:
        Student.objects.create(
            title=title,
            content=content
        )
    posts = Student.objects.all()
    ctx = {'students': posts}
    return render(request, 'posts/students_list.html', ctx)
