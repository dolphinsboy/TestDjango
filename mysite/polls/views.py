from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader,RequestContext
from .models import Question


def index(request):
    question_list = Question.objects.all()
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {'question_list':question_list})
    return HttpResponse(template.render(context))
