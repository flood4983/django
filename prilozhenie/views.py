from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Question

def index(request):
    return render(request, "prilozhenie/index.html", {"quest_list": Question.objects})

def detail(request, question_id):
    return HttpResponse("Ты ищешь вопрос номер %s." % question_id)

def results(request, question_id):
    response = "Ты ищешь результаты вопроса номер %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Вы проголосовали за вопрос номер %s" % question_id)
