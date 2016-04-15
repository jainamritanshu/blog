from django.shortcuts import render
from django.utils import timezone
from .models import *
from django.http import HttpResponse
from django.http import Http404
<<<<<<< HEAD
=======
from django.http import HttpResponseRedirect
from forum.forms import *
>>>>>>> 49d159457189cba0417039dea6e5a726ace31e73

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
<<<<<<< HEAD
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
=======
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

def a_form(request):
	if request.method == 'POST':
		form = Question(request.POST)
		if form.is_valid():
			a = Answer()
			a.text = form.cleaned_data.get('y_ans', 'default1')
			a.save()

	else:
		form = Answer()
	c_data = {'form': form}
	return HttpResponseRedirect('your_ques.html', c_data)	
>>>>>>> 49d159457189cba0417039dea6e5a726ace31e73
