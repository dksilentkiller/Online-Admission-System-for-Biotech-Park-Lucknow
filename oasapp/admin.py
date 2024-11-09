from django.contrib import admin
from .models import AdminLogin,Enquiry,tblSession,tbl_course,Student

# Register your models here.
admin.site.register(Enquiry)
admin.site.register(AdminLogin)
admin.site.register(tblSession)
admin.site.register(tbl_course)
admin.site.register(Student)


