from django.shortcuts import render
from django.utils import timezone
from .models import *
from django.http import HttpResponse
from django.http import Http404

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
	return render(request, 'forum/detail.html', a)