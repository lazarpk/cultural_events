from django import forms
from .models import Poll
from django.forms import ModelForm

class CreatePollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['question', 'option_one', 'option_two', 'option_three']
        widgets = {
            'question': forms.Textarea(
                attrs={
                    'class': "form-control",
                    'rows':'2',
                    'data-toggle': 'tooltip',
                    'title': 'Unesite naziv pitanja !'
                }
            ),
            'option_one': forms.Textarea(
                attrs={
                    'class': "form-control",
                    'rows': "1",
                    'data-toggle': 'tooltip',
                    'title': 'Unesite prvi odgovor !'
                }
            ),
            'option_two': forms.Textarea(
                attrs={
                    'class': "form-control",
                    'rows': "1",
                    'data-toggle': 'tooltip',
                    'title': 'Unesite drugi odgovor !'
                }
            ),
            'option_three': forms.Textarea(
                attrs={
                    'class': "form-control",
                    'rows': "1",
                    'data-toggle': 'tooltip',
                    'title': 'Unesite treći odgovor !'
                }
            ),
        };