from django.urls import path
from .views import home, custom_logout, watch_video, course_detail, submit_feedback,assessment, question, about, logout_page
from django.contrib.auth import views as auth_views
 

urlpatterns = [
    path("", auth_views.LoginView.as_view(), name="login"),
    path('logout/', custom_logout, name='logout'),
    path('home/',home,name='home'),
     path('course/<int:course_id>/',course_detail, name='course_detail'),
    path('watch/<int:video_id>/', watch_video, name='watch_video'),
    path('submit-feedback/',submit_feedback, name='submit_feedback'),
    path('course/<int:course_id>/assessment/', assessment, name='assessment'),
   path('course/<int:course_id>/assessment/<int:assessment_id>/question/', question, name='question'),
   path('about/', about, name='about'),
    path('logout/', logout_page, name='logout'),

]
