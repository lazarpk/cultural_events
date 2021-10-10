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
                    "class": "form-control rounded-pill",
                    'data-toggle': 'tooltip',
                    'title': 'Unesite naslov vesti !'
                }
            ),
            "Content": forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'data-toggle': 'tooltip',
                    'title': 'Unesite opis vesti !'
                }
            ),
            "Category": forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                    'data-toggle': 'tooltip',
                    'title': 'Izaberite kategoriju vesti !'
                },
                #choices = [(item.id, item.Name) for item in Category.objects.all()],
            )

        }


class AddCategoryForm (ModelForm):
    class Meta:
        model = Category
        fields = ['Name', 'valid_from', 'valid_to']
        labels = {'Name': 'Naziv', 'valid_from': 'Vazi od', 'valid_to': 'Vazi do'}
        widgets = {
            'Name': forms.TextInput (
                attrs = {
                    'class': 'form-control',
                    'title': 'Unesite naziv stavke!'
                }
            ),
            'valid_from' : forms.DateTimeInput (
                attrs = {
                    'type': 'date',
                    'class': 'form-control rounded-pill',
                    'data-toggle': 'tooltip',
                    'title': 'Unesite datum!'
                }
            ),
            'valid_to': forms.DateTimeInput (
                attrs = {
                    'type': 'date',
                    'class': 'form-control rounded-pill',
                    'data-toggle': 'tooltip',
                    'title': 'Unesite datum!'
                }
            )
        }