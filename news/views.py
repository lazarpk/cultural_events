from django.shortcuts import render
from django.utils import timezone

from django.http import Http404
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required

# Create your views here.
from .models import Article, ArticleDeletionRequest
from .forms import ArticleForm

# Create your views here.

def news(request):
    articles = Article.objects.filter(ArchivedDate__isnull=True).order_by('-id')[:10]

    return render(request, "articles.html", {'articles': articles})


@permission_required('home.article_can_create', '/login')
def article_new(request):
    if (request.method == "GET"):
        form = ArticleForm()

        return render(request, "create_article.html", {'form': form})
    elif (request.method == "POST"):
        form = ArticleForm(request.POST)

        if (form.is_valid()):
            article = form.save(commit=False)
            article.Author = request.user
            article.save()

            #return redirect('/articles/{}'.format(article.id))
            return redirect('/articles')
        else:
            return render(request, "create_article.html", {'form': form})


def article(request, *args, **kwargs):
    id = kwargs['id']
    article = Article.objects.get(pk=id)

    if article is None:
        raise Http404
    else:
        return render(request, "article.html", {'article': article})


def article_archive(request, *args, **kwargs):
    id = kwargs['id']
    article = Article.objects.get(pk=id)

    if article is not None and article.ArchivedDate is None and request.user.id == article.Author.id:
        article.ArchivedDate = timezone.now()
        article.save()
        message = "Uspesno ste arhivirali vest."

        return render(request, "request_success.html", {'success_message': message})
    else:
        return HttpResponse(status=400)


def article_create_delete_request(request, *args, **kwargs):
    id = kwargs['id']
    article = Article.objects.get(pk=id)

    if article is not None and ArticleDeletionRequest.get_if_exists(article.id) is None and request.user.id == article.Author.id:
        article_delete_request = ArticleDeletionRequest()
        article_delete_request.User = request.user
        article_delete_request.Article = article
        article_delete_request.Reason = "Zahtevano od autora."
        article_delete_request.save()

        message = "Uspesno poslat zahtev za brisanje vesti."

        return render(request, "request_success.html", {'success_message': message})
    else:
        return HttpResponse(status=400)

def index(request):

    return render(request, "index.html")