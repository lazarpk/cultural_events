from django import forms
from .models import Poll
from django.forms import ModelForm

class CreatePollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['question', 'option_one', 'option_two', 'option_three', 'public']
        widgets = {
            'question': forms.Textarea(
                attrs={
                    'class': "form-control",
                    'rows':'2'
                }
            ),
            'option_one': forms.Textarea(
                attrs={
                    'class': "form-control",
                    'rows': "1"
                }
            ),
            'option_two': forms.Textarea(
                attrs={
                    'class': "form-control",
                    'rows': "1"
                }
            ),
            'option_three': forms.Textarea(
                attrs={
                    'class': "form-control",
                    'rows': "1",


        }
            ),
            'public':forms.CheckboxInput(
                attrs={
                    'class': "form-check-label mt-3",
                }
            )
        };