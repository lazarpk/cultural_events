from django.forms import ModelForm
from .models import Article
from django.contrib.auth.forms import forms

class ArticleForm(ModelForm):

    class Meta:
        model = Article
        fields = ['Title', 'Content', 'Category']
        widgets = {
            "Title": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),
            "Content": forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            "Category": forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            )
        }