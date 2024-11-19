from django.contrib import admin
from .models import Attendance


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'date', 'status')
    list_filter = ('course', 'status')
    search_fields = ('student__name', 'course__name')


admin.site.register(Attendance, AttendanceAdmin)
