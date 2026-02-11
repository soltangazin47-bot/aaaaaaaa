from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Group, Student, Subject, Grade


class SchoolAdminSite(AdminSite):
    site_header = "🎓 School Management Admin"
    site_title = "School Admin"
    index_title = "Administration"

    def each_context(self, request):
        context = super().each_context(request)
        context["extra_css"] = "/static/app/admin.css"
        return context


admin_site = SchoolAdminSite(name="school_admin")

admin_site.register(Group)
admin_site.register(Student)
admin_site.register(Subject)
admin_site.register(Grade)
