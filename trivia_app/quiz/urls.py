from django.urls import path
from . import views
urlpatterns = [
    path('', views.quiz_home, name='quiz_home'),
    path('fetch/', views.fetch_questions, name='fetch_questions'),
]
