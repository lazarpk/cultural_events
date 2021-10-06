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
    '''
    def save(self, commit = True):
        user = super(UpdateProfileForm, self).save(commit)
        print(user)
        address = self.cleaned_data.get('address')
        number = self.cleaned_data.get('number')
        city = self.cleaned_data.get('city')
        contact_person = self.cleaned_data.get('contact_person')
        phone = self.cleaned_data.get('phone')
        description = self.cleaned_data.get('description')
        work_area = self.cleaned_data.get('work_area')
        web_site = self.cleaned_data.get('web_site')

        account = Profile(user_id = user, address=address, number=number, city=city, contact_person=contact_person, phone=phone,
                          description=description, work_area=work_area,web_site=web_site)
        if (commit):
            account.save()

        return user;
    '''

class OrgSearchForm ( forms.Form ):
    username = forms.CharField (
        required= False,
        widget= forms.TextInput (
            attrs= {
                'class': 'form-control rounded-pill',
                'placeholder': 'Pretražite organizacije po username'
            }
        )
    )
