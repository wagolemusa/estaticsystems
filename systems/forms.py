from django import forms
from .models import Category, Post, Postjob, Contact


class PostForm(forms.ModelForm):
	content = forms.CharField(widget=forms.Textarea(attrs={
		'class': 'form-control'
		}))

	class Meta:
		model = Post
		fields = [
			"category",
			"content",
			"image",
		]
		
class PostjobForm(forms.ModelForm):
	firstname = forms.CharField(widget=forms.TextInput(attrs={
		'class' : 'form-control'
		}))
	lastname = forms.CharField(widget=forms.TextInput(attrs={
		'class' : 'form-control'
		}))
	email = forms.CharField(widget=forms.TextInput(attrs={
		'class' : 'form-control'
		}))
	company = forms.CharField(widget=forms.TextInput(attrs={
		'class' : 'form-control'
		}))

	phone = forms.CharField(widget=forms.NumberInput(attrs={
		'class': 'form-control'
	}))

	content = forms.CharField(widget=forms.Textarea(attrs={
		'class': 'form-control'
		}))

	class Meta:
		model = Postjob
		fields = [
			"firstname",
			"lastname",
			"email",
			"company",
			"phone",
			"content",
		]

class CantactForms(forms.ModelForm):
	full_name = forms.CharField(widget=forms.TextInput(attrs={
		'class': 'form-control'
		}))
	phone = forms.CharField(widget=forms.NumberInput(attrs={
		'class': 'form-control'
	}))

	email = forms.CharField(widget=forms.TextInput(attrs={
		'class': 'form-control'
		}))
	subject = forms.CharField(widget=forms.TextInput(attrs={
		'class': 'form-control'
		}))
	message = forms.CharField(widget=forms.Textarea(attrs={
		'class': 'form-control'
		}))

	class Meta:
		model = Contact
		fields = [
			"full_name",
			"phone",
			"email",
			"subject",
			"message",
		]
