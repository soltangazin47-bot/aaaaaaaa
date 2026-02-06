from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("groups/", views.group_list, name="groups"),
    path("groups/<int:group_id>/", views.group_detail, name="group_detail"),
    path("student/<int:student_id>/", views.student_detail, name="student_detail"),
]
