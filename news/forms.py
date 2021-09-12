from django.forms import ModelForm
from .models import Article
from django.contrib.auth.forms import forms

class ArticleForm(ModelForm):

    class Meta:
        model = Article
        fields = ['Title', 'Content', 'Category']
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),
            "content": forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            "category": forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }