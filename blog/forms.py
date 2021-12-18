from django import forms 

from .models import Comment, Post, Course, Contact

class CommentForm(forms.ModelForm):
	content  = forms.CharField(label='', widget=forms.Textarea(attrs={
		'class': 'form-control',
		'placeholder': 'Type your comment',
		'id': 'username',
		'rows':'6'
		}))
	class Meta:
		model = Comment
		fields = ['content']

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title','image','body','categories',]


class CourseForm(forms.ModelForm):
	class Meta:
		model = Course
		fields = ['title','body','categories','image']


class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ['name','email','subject','message']