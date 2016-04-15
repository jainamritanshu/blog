from django import forms
import re
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class Question(forms.Form):
	y_ques = forms.CharField(label='Ask Your Question', required=True, max_length='5000')

	def clean_ques(self):
		try:
			ques = Question.objects.get(self.cleaned_data['y_ques'])
		except Question.DoesNotExist:
			return self.cleaned_data['ques']
		raise forms.ValidationError(_("Kindly do not leave the field blank!"))		

class Answer(forms.Form):
	y_ans = forms.CharField(label='answer', required=True, max_length='5000')

	def clean_ans(self):
		try:
			ans = Answer.objects.get(self.cleaned_data['y_ans'])
		except Answer.DoesNotExist:
			return self.cleaned_data['ans']			
		raise forms.ValidationError(_("Kindly post your answer"))	