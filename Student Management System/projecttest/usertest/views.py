from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Video, Course, Assessment, Question, AssessmentCompleted, Notification
from .forms import FeedbackForm
from django.contrib import messages
import csv
from django.http import HttpResponse
from django.utils import timezone

@login_required
def home(request):
    # Get notifications for the current user's courses
    user_courses = request.user.courses.all()
    course_ids = user_courses.values_list('id', flat=True)
    user_notifications = Notification.objects.filter(course_id__in=course_ids)

    user = request.user
    videos = Video.objects.all()
    assigned_courses = user.courses.all()
    return render(request, 'registration/home.html', {'user': user, 'courses': assigned_courses, 'videos': videos, 'notifications': user_notifications})



def custom_logout(request):
    logout(request)
    return redirect('login')

def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    videos = course.videos.all()
    return render(request, 'registration/course.html', {'course': course, 'videos': videos})

def watch_video(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    return render(request, 'registration/watch_video.html', {'video': video})

@login_required
def assessment(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    assessments = Assessment.objects.filter(course=course)
    current_user = request.user

    assessment_data = []
    completed_assessments = AssessmentCompleted.objects.filter(user=current_user)

    total_score = 0
    completed_count = 0

    for assessment in assessments:
        completed_assessment = completed_assessments.filter(assessment=assessment).first()
        if completed_assessment:
            completed_count += 1
            total_score += completed_assessment.percentage_secured
            assessment_data.append({'assessment': assessment, 'completed': True, 'completed_assessment': completed_assessment})
        else:
            assessment_data.append({'assessment': assessment, 'completed': False})

    overall_percentage = total_score / completed_count if completed_count > 0 else 0

    return render(request, 'registration/assessment.html', {'course': course, 'assessment_data': assessment_data, 'overall_percentage': overall_percentage})

def logout_page(request):
    logout(request)
    return redirect('login')

def about(request):
    return render(request, 'registration/about.html')


def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            feedback = form.cleaned_data['feedback']
            with open('feedback.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([name, email, feedback])
            return redirect('home')
@login_required
def question(request, course_id, assessment_id=None):
    course = get_object_or_404(Course, pk=course_id)
    
    if assessment_id:
        assessment = get_object_or_404(Assessment, pk=assessment_id)
        questions = Question.objects.filter(course=course, assessment=assessment)
    else:
        assessment = Assessment.objects.filter(course=course).first()
        if not assessment:
            return HttpResponse("No assessment found for this course.")
        questions = assessment.questions.filter(course=course)

    total_questions = questions.count()
    user_score = 0

    if request.method == 'POST':
        if AssessmentCompleted.objects.filter(user=request.user, assessment=assessment).exists():
            messages.error(request, "You have already completed this assessment.")
            return redirect('home')
        
        for question in questions:
            selected_option = request.POST.get(f'question_{question.id}')
            correct_option = question.correct_option
            if selected_option == correct_option:
                user_score += 1

        assessment.user_score = user_score
        assessment.save()

        percentage_secured = (user_score / total_questions) * 100
        mark = int((user_score / total_questions) * 100)  # Assuming the maximum mark is 100
        submission = AssessmentCompleted.objects.create(user=request.user, assessment=assessment, course=course, time_submitted=timezone.now(), date_submitted=timezone.now(), percentage_secured=percentage_secured, mark=mark)
        
        # Mark the completed field as True for the current user
        submission.completed = True
        submission.save()
        
        return redirect('home')

    return render(request, 'registration/question.html', {'course': course, 'questions': questions, 'total_questions': total_questions, 'user_score': user_score})



