from django.shortcuts import render
from django.utils import timezone
from .models import *
from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseRedirect
from forum.forms import *

def ques_list(request):
	latest_question_list = Question.objects.order_by('pub_date')
	context = {'latest_question_list': latest_question_list}
	return render(request, 'forum/your_ques.html', context)

def detail(request, q_id):
	try:
		ques = Question.objects.get(pk=q_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	return render(request, 'forum/detail.html', {'ques': ques})		

def ans_list(request):
	latest_ans_list = Answer.objects.order_by('pub_date')	
	a = {'latest_ans_list': latest_ans_list}
	return render(request, 'forum/ans.html', a)

def q_form(request):
	if request.method == 'POST':
		form = Question(request.POST)
		if form.is_valid():
			a = Question()
			a.text = form.cleaned_data.get('y_ques', 'default1')
			a.save()

	else:
		form = Question()
	c_data = {'form': form}
	return HttpResponseRedirect('ques_list.html', c_data)			
