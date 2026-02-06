from django.shortcuts import render, get_object_or_404
from django.db.models import Avg
from .models import Group, Student

def index(request):
    return render(request, "app/index.html")


def group_list(request):
    groups = Group.objects.all()
    return render(request, "app/groups.html", {"groups": groups})


def group_detail(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    return render(request, "app/group_detail.html", {"group": group})


def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    grades = student.grades.all()
    avg = grades.aggregate(avg=Avg("value"))["avg"]
    return render(
        request,
        "app/student_detail.html",
        {"student": student, "grades": grades, "avg": avg},
    )
