from django import forms
class post_f(forms.Form):
	author=forms.CharField(label="Enter your name")
	title=forms.CharField(label="Enter title of post")
	text=forms.CharField(label="Enter text")
	created_date=forms.CharField(label="Enter Date")
