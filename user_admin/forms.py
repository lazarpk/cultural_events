from django import forms

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