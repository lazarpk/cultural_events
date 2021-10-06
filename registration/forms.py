from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label="Lozinka",
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
        label="Potvrda Lozinke",
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
                'class': 'form-control rounded-pill'
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
                    "class": "form-control rounded-pill"
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    'class': 'form-control rounded-pill'
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    'class': 'form-control rounded-pill'
                }
            ),
            "username": forms.TextInput(
                attrs={
                    'class': 'form-control rounded-pill'
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
        labels = {"first_name": "Ime", "email": "Email adresa", "username": "Korisnicko ime"}
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
        label="Lozinka",
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
        label="Potvrda Lozinke",
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
                'class': 'form-control rounded-pill'
            }
        ),
        strip=False,
        help_text="Unesite prethodnu lozinku, zbog verifikacije.",
    )
    address = forms.MultipleChoiceField(
        label="Adresa",
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-control'
            }
        ),
        help_text='Unesite Vasu adresu.',
    )
    number = forms.IntegerField(
        label='Broj',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control rounded-pill'
            }
        ),
        help_text='Broj (adresa).',
    )
    city = forms.MultipleChoiceField(
        label="Grad.",
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-control'
            }
        ),
        help_text='Grad.',
    )
    contact_person = forms.CharField(
        label="Kontakt osoba.",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control rounded-pill'
            }
        ),
        help_text='Kontakt osoba.',
    )

    phone = forms.CharField(
        label="Telefon.",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control rounded-pill'
            }
        ),
        help_text='Telefon',
    )
    description = forms.CharField(
        label="Opis.",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control rounded-pill'
            }
        ),
        help_text='Opis',
    )

    work_area = forms.MultipleChoiceField(
        label="Oblast delovanja.",
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-control'
            }
        ),
        help_text='Oblast delovanja.',
    )
    web_site = forms.CharField(
        label="Web stranica.",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control rounded-pill'
            }
        ),
        help_text='Web stranica.',
    )


    def clean_email(self):
        email = self.cleaned_data.get("email")
        user = User.objects.filter(email__exact=email).all()

        if (len(user) != 0):
            raise forms.ValidationError("Email already taken!")

        return email


