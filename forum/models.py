from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Question(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	pub_date = models.DateTimeField()

	def publish(self):
		self.pub_date = timezone.now()
		self.save

	def __str__(self):
		return self.title

def get_ques():
	return Question.objects.get(id=1)		

class Answer(models.Model):
	author = models.ForeignKey('auth.User')
	text = models.TextField()
	pub_date = models.DateTimeField()
	q_a = models.ForeignKey(Question, default=get_ques)

	def publish(self):
		self.pub_date = timezone.now()
		self.save

	def __str__(self):
		return self.text		
