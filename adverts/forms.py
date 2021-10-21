from django import forms;

from .models import Adverts;

class AdvertsCreateForm (forms.ModelForm):
    class Meta:
        model = Adverts;
        fields = [ 'title', 'description', 'load_date', 'expire_date'];

        widgets = {
            'title': forms.TextInput (
                attrs = {
                    'class': "form-control",
                    'data-toggle': 'tooltip',
                    'title': 'Unesite naziv oglasa !'
                }
            ),
            'description': forms.Textarea (
                attrs={
                    'class': "form-control",
                    'rows': "5",
                    'data-toggle': 'tooltip',
                    'title': 'Unesite tekst oglasa !'
                }
            ),
            'load_date': forms.DateTimeInput(
                format=('%m/%d/%Y'),
                attrs={
                    'class': 'form-control', 'placeholder': 'Izaberite datum', 'type': 'date',
                    'data-toggle': 'tooltip',
                    'title': 'Unesite datum od kad oglas važi !'
                }
            ),
            'expire_date': forms.DateTimeInput(
                format=('%m/%d/%Y'),
                attrs={
                    'class': 'form-control', 'placeholder': 'Izaberite datum', 'type': 'date',
                    'data-toggle': 'tooltip',
                    'title': 'Unesite datum do kad oglas važi !'
                }
        ),
        };

class AdvertsSearchForm (forms.Form):
    title = forms.CharField (
        required= False,
        widget= forms.TextInput (
            attrs={
                'class':'form-control rounded-pill',
                'placeholder': 'Pretražite oglase'
            }
        )
    );