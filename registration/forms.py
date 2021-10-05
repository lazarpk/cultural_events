from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
                'class': 'form-control rounded-pill',
                'data-toggle': 'tooltip',
                'title': 'Šifra mora da sadrži 8 karaktera, veliko slovo i specijalni znak!'
            }
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
                'class': 'form-control rounded-pill',
                'data-toggle': 'tooltip',
                'title': 'Ponovite istu šifru!'
            }
        ),
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username"]
        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control rounded-pill",
                    'data-toggle': 'tooltip',
                    'title': 'Unesite svoje ime, tako da početno slovo bude veliko!'
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    'class': 'form-control rounded-pill',
                    'data-toggle': 'tooltip',
                    'title': 'Unesite svoje prezime!'
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    'class': 'form-control rounded-pill',
                    'data-toggle': 'tooltip',
                    'title': 'Unesite email u formatu example@example.com !'
                }
            ),
            "username": forms.TextInput(
                attrs={
                    'class': 'form-control rounded-pill',
                    'data-toggle': 'tooltip',
                    'title': 'Unesite svoje korisničko ime !'
                }
            )
        }

    def clean_email(self):
        email = self.cleaned_data.get("email")
        user = User.objects.filter(email__exact=email).all()

        if (len(user) != 0):
            raise forms.ValidationError("Email already taken!")

        return email


class RegisterFormOrg(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "email", "username"]
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "class": "form-control rounded-pill"
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    'class': 'form-control rounded-pill'
                }
            ),
            "first_name": forms.TextInput(
                attrs={
                    'class': 'form-control rounded-pill'
                }
            )
        }

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
                'class': 'form-control rounded-pill'
            }
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
                'class': 'form-control rounded-pill'
            }
        ),
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )
    address = forms.CharField(
        label="Address",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control rounded-pill'
            }
        ),
        help_text='Enter your address.',
    )
    number = forms.IntegerField(
        label='Number',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control rounded-pill'
            }
        ),
        help_text='Address number.',
    )
    city = forms.CharField(
        label="City.",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control rounded-pill'
            }
        ),
        help_text='City.',
    )
    contact_person = forms.CharField(
        label="Contact person.",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control rounded-pill'
            }
        ),
        help_text='Contact person.',
    )

    phone = forms.CharField(
        label="Phone.",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control rounded-pill'
            }
        ),
        help_text='Phone',
    )
    description = forms.CharField(
        label="Description.",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control rounded-pill'
            }
        ),
        help_text='Description',
    )

    work_area = forms.CharField(
        label="The area of work.",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control rounded-pill'
            }
        ),
        help_text='The area of work.',
    )
    web_site = forms.CharField(
        label="Web site.",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control rounded-pill'
            }
        ),
        help_text='Web site.',
    )


    def clean_email(self):
        email = self.cleaned_data.get("email")
        user = User.objects.filter(email__exact=email).all()

        if (len(user) != 0):
            raise forms.ValidationError("Email already taken!")

        return email
