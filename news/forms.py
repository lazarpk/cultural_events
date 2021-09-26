from django.forms import ModelForm
from .models import Article
from django.contrib.auth.forms import forms
from news.models import Category

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
                },
                #choices = [(item.id, item.Name) for item in Category.objects.all()],
            )

        }


class AddCategoryForm (ModelForm):
    class Meta:
        model = Category
        fields = ['Name']
        widgets = {
            'Name':forms.TextInput (
                attrs = {
                    'class': 'form-control'
                }
            ),
        }