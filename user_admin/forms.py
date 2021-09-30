from django import forms
from .models import Reports

class UserSearchForm ( forms.Form ):
    username = forms.CharField (
        required= False,
        widget= forms.TextInput (
            attrs= {
                'class': 'form-control rounded-pill'
            }
        )
    )

class NewsCategorySearchForm ( forms.Form ):
    name = forms.CharField (
        required= False,
        widget= forms.TextInput (
            attrs= {
                'class': 'form-control rounded-pill'
            }
        )
    )

class EventsCategorySearchForm ( forms.Form ):
    name = forms.CharField (
        required= False,
        widget= forms.TextInput (
            attrs= {
                'class': 'form-control rounded-pill'
            }
        )
    )

class ReportsCreateForm (forms.Form):
    title = forms.CharField(
        label="Naslov izvestaja",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control rounded-pill'
            }
        )
    )
    date_from = forms.CharField(
        label="Datum od",
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control rounded-pill',
                "type": "date"
            }
        )
    )
    date_to = forms.CharField(
        label="Datum do",
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control rounded-pill',
                "type": "date"
            }
        )
    )

class GetTheReport (forms.ModelForm):
    class Meta:
        model = Reports
        fields = ['title', 'date_from', 'date_to', 'num_users', 'num_events', 'num_adverts', 'num_articles']
        labels = {
            'title': 'Naslov izvestaja',
            'date_from': 'Datum od',
            'date_to': 'Datum do',
            'num_users': 'Broj registrovanih korisnika',
            'num_events': 'Broj kreiranih dogadjaja',
            'num_adverts': 'Broj kreiranih oglasa',
            'num_articles': 'Broj kreiranih vesti'
        }
        widgets = {
            'title':forms.TextInput (
                attrs= {
                    'class': 'form-control rounded-pill',
                    'disabled': True
                }
            ),
            'date_from':forms.DateTimeInput (
                attrs= {
                    'class': 'form-control rounded-pill',
                    'type': 'datetime',
                    'disabled': True
                }
            ),
            'date_to':forms.DateTimeInput (
                attrs= {
                    'class': 'form-control rounded-pill',
                    'type': 'datetime',
                    'disabled': True
                }
            ),
            'num_users':forms.TextInput (
                attrs= {
                    'class': 'form-control rounded-pill',
                    'disabled': True
                }
            ),
            'num_events':forms.TextInput (
                attrs= {
                    'class': 'form-control rounded-pill',
                    'disabled': True
                }
            ),
            'num_adverts':forms.TextInput (
                attrs= {
                    'class': 'form-control rounded-pill',
                    'disabled': True
                }
            ),
            'num_articles':forms.TextInput (
                attrs= {
                    'class': 'form-control rounded-pill',
                    'disabled': True
                }
            )
        }