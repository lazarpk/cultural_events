from django.forms import ModelForm

from django import forms


class EmailForm(forms.Form):
    subject = forms.CharField( label ='Naslov poruke', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(label='Ime i prezime', widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label= 'Poruka', widget=forms.Textarea(attrs={'class': 'form-control'}))


'''
class ArticleForm(ModelForm):

    class Meta:
        model = Article
        fields = ['Title', 'Content', 'Category']
'''
