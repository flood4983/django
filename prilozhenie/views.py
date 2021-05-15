from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Question
from django.template import loader

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template("index.html")
    context = {
        'quest_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse("Ты ищешь вопрос номер %s." % question_id)

def results(request, question_id):
    response = "Ты ищешь результаты вопроса номер %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Вы проголосовали за вопрос номер %s" % question_id)
