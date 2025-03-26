from django.shortcuts import render
from django.http import HttpResponse
def quiz_home(request):
    return HttpResponse("<h1>Welcome to the Quiz!</h1>")
# Create your views here.
