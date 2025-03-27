from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.http import JsonResponse
def quiz_home(request):
    return HttpResponse("<h1>Welcome to the Quiz!</h1>")
# Create your views here.
def fetch_questions(request):
    url = "https://opentdb.com/api.php?amount=10&type=multiple"
    response = requests.get(url)
    data = response.json()
    return JsonResponse(data)
