from django import forms;
from registration.models import Profile
from django.contrib.auth.models import User

class UpdateUserForm (forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }
    '''
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    );
    number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    );
    city = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    );
    contact_person = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    );
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    );
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    );
    work_area = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    );
    web_site = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    );
    '''
class UpdateProfileForm (forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'number', 'city', 'contact_person', 'phone', 'description', 'work_area', 'web_site']
        widgets = {
            'address': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'number': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'city': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'contact_person': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'work_area': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'web_site': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

        }