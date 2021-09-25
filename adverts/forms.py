from django import forms;

from .models import Adverts;

class AdvertsCreateForm (forms.ModelForm):
    class Meta:
        model = Adverts;
        fields = [ 'title', 'description', 'load_date', 'expire_date'];

        widgets = {
            'title': forms.TextInput (
                attrs = {
                    'class': "form-control"
                }
            ),
            'description': forms.Textarea (
                attrs={
                    'class': "form-control",
                    'rows': "5"
                }
            ),
            'load_date': forms.DateInput(
                format=('%m/%d/%Y'),
                attrs={
                    'class': 'form-control', 'placeholder': 'Izaberite datum', 'type': 'date'
                }
            ),
            'expire_date': forms.DateInput(
                format=('%m/%d/%Y'),
                attrs={
                    'class': 'form-control', 'placeholder': 'Izaberite datum', 'type': 'date'
                }
        ),
        };

class AdvertsSearchForm ( forms.Form):
    title = forms.CharField (
        required= False,
        widget= forms.TextInput (
            attrs={
                'class':'form-control'
            }
        )
    );