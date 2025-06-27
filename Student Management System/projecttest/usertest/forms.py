# forms.py
from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea)
