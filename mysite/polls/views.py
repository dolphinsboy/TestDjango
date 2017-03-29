from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
# from django.template import loader,RequestContext
from .models import Question, Choice
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse

from django.views import generic
from django.views.decorators.http import require_http_methods

# def index(request):
#     question_list = Question.objects.all()
#     # template = loader.get_template('polls/index.html')
#     # context = RequestContext(request, {'question_list':question_list})
#     # return HttpResponse(template.render(context))
#     context = {'question_list': question_list}
#     return render(request, 'polls/index.html', context)


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'question_list'

    def get_queryset(self):
        return Question.objects.all()

# def detail(request, question_id):
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     #     context = {'question': question}
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exits")
#     question = get_object_or_404(Question, pk=question_id)
#     context = {'question': question}
#     return render(request, 'polls/detail.html', context)


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

@require_http_methods(["POST"])
def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except KeyError, Choice.DoesNotExist:
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "error"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})


class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'