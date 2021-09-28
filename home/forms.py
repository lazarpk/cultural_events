from django import forms
from django.forms import ModelForm
from .models import AboutUs


class AboutUsForm (ModelForm):
    class Meta:
        model = AboutUs
        fields = ['content1', 'content2']
        widgets = {
            'content1': forms.Textarea (
                attrs= {
                    'class': 'form-control',
                    'rows': 16
                }
            ),
            'content2': forms.Textarea (
                attrs= {
                    'class': 'form-control',
                    'rows': 16
                }
            ),
        }
