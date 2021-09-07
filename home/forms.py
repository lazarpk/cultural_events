from django.forms import ModelForm
from home.models import Category, Article, ArticleDeletionRequest


class ArticleForm(ModelForm):

    class Meta:
        model = Article
        fields = ['Title', 'Content', 'Category']