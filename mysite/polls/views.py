from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
# from django.template import loader,RequestContext
from .models import Question
from django.shortcuts import render
from django.http import Http404


def index(request):
    question_list = Question.objects.all()
    # template = loader.get_template('polls/index.html')
    # context = RequestContext(request, {'question_list':question_list})
    # return HttpResponse(template.render(context))
    context = {'question_list': question_list}
    return render(request,'polls/index.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        context = {'question': question}
    except Question.DoesNotExist:
        raise Http404("Question does not exits")
    return render(request, 'polls/detail.html', context)