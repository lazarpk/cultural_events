from django import forms

class EventsForm (forms.Form):
    event_name = forms.CharField (
        label = 'Naziv',
        widget = forms.TextInput (
            attrs = {
                "class" : "form-control"
            }
        )
    )

    text = forms.CharField (
        label = 'Tekst',
        widget = forms.TextInput (
            attrs = {
                "class" : "form-control"
            }
        )
    )

    type = forms.CharField (
        label = 'Vrsta',
        widget = forms.TextInput (
            attrs = {
                "class" : "form-control"
            }
        )
    )

    place = forms.CharField (
        label = 'Mesto',
        widget = forms.TextInput (
            attrs = {
                "class": "form-control"
            }
        )
    )

    time = forms.DateTimeField (
        label = 'Vreme',
        widget = forms.DateTimeInput (
            attrs = {
                "class": "form-control"
            }
        )
    )

    age = forms.IntegerField (
        label = 'Uzrast',
        widget = forms.NumberInput (
            attrs = {
                "class": "form-control"
            }
        )
    )

    space_characteristics = forms.CharField (
        label = 'Karakteristike prostora',
        widget = forms.TextInput (
            attrs = {
                "class": "form-control"
            }
        )
    )

    date_published = forms.DateTimeField (
        label = 'Datum i vreme objave',
        widget = forms.DateTimeInput ( #pronadji kako da stavi trenutno vreme unosenja dogadjaja!!!
            attrs = {
                "class": "form-control"
            }
        )
    )

    expiration_date = forms.DateTimeField (
        label = 'Važi do',
        widget = forms.DateTimeInput (
            attrs = {
                "class": "form-control"
            }
        )
    )

    author = forms.CharField (
        label = 'Autor',
        widget = forms.TextInput (
            attrs = {
                "class": "form-control"
            }
        )
    )