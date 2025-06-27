from django.contrib import admin
from .models import Course, Video, Assessment, Question, AssessmentCompleted, Notification

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'progress')
    filter_horizontal = ('users',)

class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'start_date', 'end_date')  # Remove 'completed'

# Register your models here.
admin.site.register(Course)
admin.site.register(Video)
admin.site.register(Assessment, AssessmentAdmin)
admin.site.register(Question)
admin.site.register(AssessmentCompleted)
admin.site.register(Notification)