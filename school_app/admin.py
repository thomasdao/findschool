from django.contrib import admin

from .models import School, Course, Enquiry

admin.site.register(School)
admin.site.register(Course)
admin.site.register(Enquiry)
