from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from .forms import UserSearchForm, NewsCategorySearchForm, EventsCategorySearchForm
from user_profile.forms import UpdateUserForm, UpdateProfileForm
from registration.models import Profile
from news.models import Category
from news.forms import AddCategoryForm
from django.shortcuts import redirect
from events.models import CategoryEvents
from events.forms import AddEventCategoryForm
from events.models import Events
from news.models import Article
from adverts.models import Adverts
from polls.models import Poll
# Create your views here.
def index (request):
    curently_user = User.objects.get(id=request.user.id)
    if curently_user.is_superuser:
        return render(request, 'index-admin.html')
    else:
        raise Http404


def search (request):
    form = UserSearchForm(request.GET)
    query = User.objects

    if (form.is_valid()):
        username = form.cleaned_data.get ('username')
        if (len (username) > 0):
            query = query.filter(
                username__icontains = username
            )

    users = query.all()
    context = {
        'form':form,
        'users': users
    }
    return render(request, 'search-users.html', context)

def editUsers (request):
    if(request.method == "GET"):
        id = request.GET.get ('id')
        user = User.objects.get (id = id)
        form = UpdateUserForm (instance = user)

        try:
            form1 = UpdateProfileForm (instance=Profile.objects.get(user_id = user.id))
            context = {
                'form': form,
                'form1': form1
            }
        except Profile.DoesNotExist:
            context = {
                'form': form
            }
        return render(request, 'edit-users.html', context)
    elif (request.method == "POST"):

        username = request.POST.get ('username')
        user = User.objects.get (username = username)

        form = UpdateUserForm(request.POST, instance=user)
        if (form.is_valid()):

            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.username = form.cleaned_data.get('username')
            user.email = form.cleaned_data.get('email')
            user.save()
            try:
                form1 = UpdateProfileForm(instance=Profile.objects.get(user_id = user.id))
                if (form1.is_valid()):
                    profile = Profile.objects.get(user_id=user.id)
                    profile.address = form1.cleaned_data.get('address')
                    profile.number = form1.cleaned_data.get('number')
                    profile.city = form1.cleaned_data.get('city')
                    profile.contact_person = form1.cleaned_data.get('contact_person')
                    profile.phone = form1.cleaned_data.get('phone')
                    profile.description = form1.cleaned_data.get('description')
                    profile.work_area = form1.cleaned_data.get('work_area')
                    profile.web_site = form1.cleaned_data.get('web_site')
                    profile.save()
            except:
                return render(request, 'index-admin.html')
            return render(request, 'index-admin.html')
        else:
            form = UpdateUserForm(request.POST, instance=user)
            context = {
                'form': form,
            }
            print('greska')
            try:
                form1 = UpdateProfileForm (instance=Profile.objects.get(user_id = user.id))
                context = {
                    'form': form,
                    'form1': form1
                }
            except:
                pass
            return render(request, 'edit-users.html', context)


def newsCategories (request):
    categories = Category.objects.all()
    form = NewsCategorySearchForm(request.GET)
    if (form.is_valid()):
        name = form.cleaned_data.get('name')
        categories = categories.filter(Name__icontains = name)
    context = {
        'form':form,
        'categories': categories
    }
    return render(request, 'categories-news.html', context)

def newsCategoriesEdit (request):
    if (request.method == "GET"):
        id = request.GET.get ('id')
        category = Category.objects.get (id = id)
        form = AddCategoryForm(instance=category)
        context = {
            'form': form,
            'id': id
        }
        return render(request, 'categories-news-edit.html', context)
    elif (request.method == "POST"):
        id = request.POST.get ("id")
        form = AddCategoryForm(request.POST)
        if (form.is_valid()):
            category = Category.objects.get(id=id)
            name = form.cleaned_data.get ('Name')
            category.Name = name
            category.save()
            #return render(request, 'index-admin.html')
            return redirect ('/administration/categories-news')
        else:
            context = {
                'form': form,
                'id': id
            }
            return render(request, 'categories-news-edit.html', context)

def eventsCategories(request):
    categories = CategoryEvents.objects.all()
    form = EventsCategorySearchForm(request.GET)
    if (form.is_valid()):
        name = form.cleaned_data.get('name')
        categories = categories.filter(name__icontains = name)
    context = {
        'form':form,
        'categories': categories
    }
    return render(request, 'categories-events.html', context)

def eventsCategoriesEdit (request):
    if (request.method == "GET"):
        id = request.GET.get ('id')
        category = CategoryEvents.objects.get (id = id)
        form = AddEventCategoryForm(instance=category)
        context = {
            'form': form,
            'id': id
        }
        return render(request, 'categories-events-edit.html', context)
    elif (request.method == "POST"):
        id = request.POST.get ("id")
        form = AddEventCategoryForm(request.POST)
        if (form.is_valid()):
            category = CategoryEvents.objects.get(id=id)
            name = form.cleaned_data.get ('name')
            category.name = name
            category.save()
            return redirect ('/administration/categories-events')
        else:
            context = {
                'form': form,
                'id': id
            }
            return render(request, 'categories-events-edit.html', context)

def statistics (request):
    form = UserSearchForm(request.GET)
    query = User.objects

    if (form.is_valid()):
        username = form.cleaned_data.get('username')
        if (len(username) > 0):
            query = query.filter(
                username__icontains=username
            )

    users = query.all()
    context = {
        'form': form,
        'users': users
    }
    return render(request, 'statistics.html', context)

def statisticsUser (request):
    id = request.GET.get('id')
    requested_user = User.objects.get(id=id)
    events = Events.objects.filter(author_id=id).count()
    news = Article.objects.filter(Author_id = id).count()
    adverts = Adverts.objects.filter(author_id = id).count()
    polls = Poll.objects.filter(author_id = id).count()
    context ={
        'id':id,
        'events': events,
        'news': news,
        'adverts': adverts,
        'polls': polls,
        'requested_user': requested_user
    }
    return render(request, 'statistics-user.html', context)