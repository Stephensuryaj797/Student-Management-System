from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    progress = models.PositiveIntegerField(default=0, blank=True, null=True)
    users = models.ManyToManyField(User, related_name='courses')

    def __str__(self):
        return self.title

    def add_user(self, user):
        self.users.add(user)

    def remove_user(self, user):
        self.users.remove(user)

class Video(models.Model):
    course = models.ForeignKey(Course, related_name='videos', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_url = models.URLField()

    def __str__(self):
        return self.title

class Assessment(models.Model):
    course = models.ForeignKey(Course, related_name='assessments', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='questions')
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    image = models.ImageField(upload_to='question_images/', null=True, blank=True)
    option_1 = models.CharField(max_length=100)
    option_2 = models.CharField(max_length=100)
    option_3 = models.CharField(max_length=100)
    option_4 = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=1, choices=[('1', 'Option 1'), ('2', 'Option 2'), ('3', 'Option 3'), ('4', 'Option 4')])

    def __str__(self):
        return self.text

class AssessmentCompleted(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    time_submitted = models.TimeField(default=timezone.now)
    date_submitted = models.DateField(default=timezone.now)
    percentage_secured = models.DecimalField(max_digits=5, decimal_places=2)
    mark = models.PositiveIntegerField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.assessment.name} - {self.course.title}"
    
class Notification(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    notifi_name = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.notifi_name}"
