from django import forms
from django.forms import ModelForm
from .models import AboutUs
from django.forms import ModelForm

from django import forms


class EmailForm(forms.Form):
    subject = forms.CharField( label ='Naslov poruke', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(label='Ime i prezime', widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label= 'Poruka', widget=forms.Textarea(attrs={'class': 'form-control'}))


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
