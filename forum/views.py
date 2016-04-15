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

def a_ques(request):
	if request.method == 'POST':
		pub_date = Question.pub_date.objects.get()
		user = Question.author.objects.get()
		t = Question.title.objects.get()
		a = Question()
		a.text = request.POST['a']
		a.author = 	User.objects.get()
		a.pub_date = pub_date
		a.title = t
		a.save()
		context = {'User' : user,
				   'pub_date' : pub_date,
				   'title' : t,
				   'text' : text,
				   }
		return render(request, 'forum/create.html', context)

def a_answer(request):		
	if request.method == 'POST':
		pub_date = Answer.pub_date.objects.get()
		user = User.objects.get()
		t = Answer.title.objects.get()
		a = Answer()
		a.text = request.POST['a']
		a.pub_date = pub_date
		a.title = t
		a.save()
		context = {'user' : User,
				   'text' : text,
				  }
		return render(request, 'forum/detail.html', context)		  