from django import forms
from .models import Events
from django.forms import ModelForm
from .models import CategoryEvents, SpaceCharacteristics
# from django.contrib.auth.forms import forms

class EventsForm (forms.ModelForm):
    class Meta:
        model = Events
        fields = ['event_name', 'text', 'category', 'place', 'time', 'age', 'space_characteristics', 'expiration_date']

        labels = {
            'event_name':'Naziv',
            'text':'Tekst',
            'category':'Vrsta',
            'place':'Mesto',
            'time':'Vreme',
            'age':'Uzrast',
            'space_characteristics':'Karakteristike prostora',
            'expiration_date':'Važi do',
        }

        widgets = {
            'event_name' : forms.TextInput (
                attrs = {
                    "class" : "form-control rounded-pill",
                    'data-toggle': 'tooltip',
                    'title': 'Unesite naziv događaja !'
                }
            ),
            'text' : forms.TextInput (
                 attrs = {
                     "class" : "form-control rounded-pill",
                     'data-toggle': 'tooltip',
                     'title': 'Unesite opis događaja !'
                 }
            ),
            'category' : forms.SelectMultiple (
                 attrs = {
                     "class" : "form-control",
                     'data-toggle': 'tooltip',
                     'title': 'Unesite kategoriju događaja !'
                }
            ),
            'place' : forms.TextInput (
                 attrs = {
                     "class": "form-control rounded-pill",
                     'data-toggle': 'tooltip',
                     'title': 'Unesite mesto gde se događaj održava !'
                 }
            ),
            'time' : forms.DateTimeInput (
                 # format = '%d%m%Y %H%M',
                 attrs = {
                     #"type": "datetime",
                     "type": "datetime-local",
                     "class": "form-control rounded-pill",
                     'data-toggle': 'tooltip',
                     'title': 'Unesite vreme održavanja događaja !'
                 }
            ),
            'age' : forms.SelectMultiple (
                 attrs = {
                     "class": "form-control rounded-pill",
                     'data-toggle': 'tooltip',
                     'title': 'Unesite uzrast koji važi za ovaj događaj !'
                     
                 }
            ),
            'space_characteristics' : forms.SelectMultiple (
                 attrs = {
                     "class": "form-control rounded-pill",
                     'data-toggle': 'tooltip',
                     'title': 'Unesite karakteristike prostora !'
                 }
            ),
            'expiration_date' : forms.DateTimeInput (
                 # format='%d%m%Y %H%M',
                 attrs = {
                     'type': 'datetime-local',
                     "class": "form-control rounded-pill",
                     'data-toggle': 'tooltip',
                     'title': 'Unesite datum do kada događaj važi !'
                 }
            ),
        }

class AddEventCategoryForm(ModelForm):
    class Meta:
        model = CategoryEvents
        fields = ['name']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class AddSpaceCharacteristicsForm(ModelForm):
    class Meta:
        model = SpaceCharacteristics
        fields = ['name', 'valid_from', 'valid_to']
        labels = {'name': 'Naziv', 'valid_from': 'Vazi od', 'valid_to': 'Vazi do'}
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'title': 'Unesite naziv stavke!'
                }
            ),
            'valid_from': forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',
                    'class': 'form-control rounded-pill',
                    'data-toggle': 'tooltip',
                    'title': 'Unesite datum!'
                }
            ),
            'valid_to': forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',
                    'class': 'form-control rounded-pill',
                    'data-toggle': 'tooltip',
                    'title': 'Unesite datum!'
                }
            )
        }



    # event_name = forms.CharField (
    #     label = 'Naziv',
    #     widget = forms.TextInput (
    #         attrs = {
    #             "class" : "form-control"
    #         }
    #     )
    # )
    #
    # text = forms.CharField (
    #     label = 'Tekst',
    #     widget = forms.TextInput (
    #         attrs = {
    #             "class" : "form-control"
    #         }
    #     )
    # )
    #
    # type = forms.CharField (
    #     label = 'Vrsta',
    #     widget = forms.TextInput (
    #         attrs = {
    #             "class" : "form-control"
    #         }
    #     )
    # )
    #
    # place = forms.CharField (
    #     label = 'Mesto',
    #     widget = forms.TextInput (
    #         attrs = {
    #             "class": "form-control"
    #         }
    #     )
    # )
    #
    # time = forms.DateTimeField (
    #     label = 'Vreme',
    #     widget = forms.DateTimeInput (
    #         # format = '%d%m%Y %H%M',
    #         attrs = {
    #             "type": "datetime",
    #             "class": "form-control"
    #         }
    #     )
    # )
    #
    # age = forms.IntegerField (
    #     label = 'Uzrast',
    #     widget = forms.NumberInput (
    #         attrs = {
    #             "class": "form-control"
    #         }
    #     )
    # )
    #
    # space_characteristics = forms.CharField (
    #     label = 'Karakteristike prostora',
    #     widget = forms.TextInput (
    #         attrs = {
    #             "class": "form-control"
    #         }
    #     )
    # )
    #
    # # date_published = forms.DateTimeField (
    # #     label = 'Datum i vreme objave',
    # #     widget = forms.DateTimeInput (
    # #         format='%d%m%Y %H%M',
    # #         attrs = {
    # #             "class": "form-control"
    # #         }
    # #     )
    # # )
    #
    # expiration_date = forms.DateTimeField (
    #     label = 'Važi do',
    #     widget = forms.DateTimeInput (
    #         # format='%d%m%Y %H%M',
    #         attrs = {
    #             "class": "form-control"
    #         }
    #     )
    # )
    #
    # author = forms.CharField (
    #     label = 'Autor',
    #     widget = forms.TextInput (
    #         attrs = {
    #             "class": "form-control"
    #         }
    #     )
    # )