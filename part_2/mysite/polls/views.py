from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from polls.models import Choice, Question, Task

import python_matlab
import datetime

def hello(request):
	task = Task()
	return render(request, 'polls/hello.html', {'task': task})

def current_datetime(request):
	now = datetime.datetime.now()
	html = "<html><body>It is now %s.</body></html>" % now
	return HttpResponse(html)

def just_for_fun(request, str0):
	return HttpResponse(python_matlab.method1())
#	return render(request, 'polls/just_for_fun.html', {'str': str0})

	
class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		"""Return the last five published questions."""
		return Question.objects.order_by('-pub_date')[:5]
	
class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'
	
class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'

def vote(request, question_id):
	p = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
