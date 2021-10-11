from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from .forms import UserSearchForm, NewsCategorySearchForm, EventsCategorySearchForm, ReportsCreateForm, GetTheReport, WorkAreaSearchForm, SpaceCharacteristicsSearchForm
from user_profile.forms import UpdateUserForm, UpdateProfileForm
from registration.models import Profile
from news.models import Category
from news.forms import AddCategoryForm
from django.shortcuts import redirect
from events.models import CategoryEvents, SpaceCharacteristics
from events.forms import AddEventCategoryForm, AddSpaceCharacteristicsForm
from events.models import Events
from news.models import Article
from adverts.models import Adverts
from polls.models import Poll
from home.forms import AboutUsForm
from home.models import AboutUs
from registration.models import WorkArea
from registration.forms import AddWorkAreaForm
import datetime
from django.utils import timezone
from .models import Reports
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
        form1 = None
        obj = None
        try:
            obj = Profile.objects.get(user_id=user.id)
            form1 = UpdateProfileForm(request.POST, instance=obj)
            if form1.is_valid():
                print('uso u if form1 is valid')
                obj.address = form1.cleaned_data.get('address')
                obj.number = form1.cleaned_data.get('number')
                obj.city = form1.cleaned_data.get('city')
                obj.contact_person = form1.cleaned_data.get('contact_person')
                obj.phone = form1.cleaned_data.get('phone')
                obj.description = form1.cleaned_data.get('description')
                obj.work_area = form1.cleaned_data.get('work_area')
                obj.web_site = form1.cleaned_data.get('web_site')
                obj.save()
        except Profile.DoesNotExist:
            obj = False
            form1 = False

        form = UpdateUserForm(request.POST, instance=user)
        if (form.is_valid()):

            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.username = form.cleaned_data.get('username')
            user.email = form.cleaned_data.get('email')
            user.save()

            return render(request, 'index-admin.html')
        else:
            form = UpdateUserForm(request.POST, instance=user)
            context = {
                'form': form,
            }
            print('greska 2')
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
            category.valid_from = form.cleaned_data.get('valid_from')
            category.valid_to = form.cleaned_data.get('valid_to')
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
            category.valid_from = form.cleaned_data.get ('valid_from')
            category.valid_to = form.cleaned_data.get('valid_to')
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

def aboutUsEdit (request):
    if(request.method=="GET"):
        obj = AboutUs.objects.last()
        form = AboutUsForm(instance=obj)
        context = {
            'form': form
        }
        return render(request, 'about-us-edit.html', context)
    elif (request.method == "POST"):
        form = AboutUsForm(request.POST)
        obj = AboutUs.objects.last()

        if (form.is_valid()):
            content1 = form.cleaned_data.get('content1')
            content2 = form.cleaned_data.get('content2')
            obj.content1 = content1
            obj.content2 = content2
            obj.save()
            return redirect('/about')

        else:
            context = {
                'form':form
            }
            return render(request, 'about-us-edit.html', context)

def reports (request):
    if (request.method == "GET"):
        form = ReportsCreateForm(request.GET)
        context = {
            'form': form
        }
        return render(request, 'reports.html', context)
    elif (request.method == "POST"):
        form = ReportsCreateForm (request.POST)
        if (form.is_valid()):
            title = form.cleaned_data.get ('title')
            dateStart = form.cleaned_data.get('date_from')
            dateEnd = form.cleaned_data.get('date_to')
            num_users = User.objects.filter(date_joined__range=(dateStart, dateEnd)).count()
            num_events = Events.objects.filter(date_published__range=(dateStart, dateEnd)).count()
            num_adverts = Adverts.objects.filter(load_date__range=(dateStart, dateEnd)).count()
            num_articles = Article.objects.filter(CreationDate__range=(dateStart, dateEnd)).count()
            report = Reports()
            report.title = title
            report.date_from = dateStart
            report.date_to = dateEnd
            report.num_users = num_users
            report.num_events = num_events
            report.num_adverts = num_adverts
            report.num_articles = num_articles
            report.save()
            form1 = GetTheReport(instance=report)
        context = {
            'form': form,
            'form1': form1
        }
        return render(request, 'reports.html', context)


def codebooksEdit (request):
    curently_user = User.objects.get(id=request.user.id)
    if curently_user.is_superuser:
        return render(request, 'codebooks-edit.html')
    else:
        raise Http404


def workArea (request):
    workareas = WorkArea.objects.all()
    form = WorkAreaSearchForm(request.GET)
    if (form.is_valid()):
        name = form.cleaned_data.get('name')
        workareas = workareas.filter(name__icontains = name)
    context = {
        'form':form,
        'workareas': workareas
    }
    return render (request, 'workarea.html', context)


def workAreaEdit (request):
    if (request.method == "GET"):
        id = request.GET.get('id')
        work_area = WorkArea.objects.get(id=id)
        form = AddWorkAreaForm(instance=work_area)
        context = {
            'form': form,
            'id': id
        }
        return render(request, 'workarea-edit.html', context)
    elif (request.method == "POST"):
        id = request.POST.get("id")
        form = AddWorkAreaForm(request.POST)
        if (form.is_valid()):
            work_area = WorkArea.objects.get(id=id)
            name = form.cleaned_data.get('name')
            work_area.name = name
            work_area.valid_from = form.cleaned_data.get('valid_from')
            work_area.valid_to = form.cleaned_data.get('valid_to')
            work_area.save()
            return redirect('/administration/workareas')
        else:
            context = {
                'form': form,
                'id': id
            }
            return render(request, 'workarea-edit.html', context)


def spaceCharacteristic (request):
    spacecharacteristics = SpaceCharacteristics.objects.all()
    form = SpaceCharacteristicsSearchForm(request.GET)
    if (form.is_valid()):
        name = form.cleaned_data.get('name')
        spacecharacteristics = spacecharacteristics.filter(name__icontains = name)
    context = {
        'form':form,
        'spacecharacteristics': spacecharacteristics
    }
    return render (request, 'spacecharacteristics.html', context)


def spaceCharacteristicsEdit (request):
    if (request.method == "GET"):
        id = request.GET.get('id')
        space_characteristics = SpaceCharacteristics.objects.get(id=id)
        print(space_characteristics)
        form = AddSpaceCharacteristicsForm(instance=space_characteristics)
        context = {
            'form': form,
            'id': id
        }
        return render(request, 'spacecharacteristics-edit.html', context)
    elif (request.method == "POST"):
        id = request.POST.get("id")
        form = AddWorkAreaForm(request.POST)
        if (form.is_valid()):
            space_characteristics = SpaceCharacteristics.objects.get(id=id)
            name = form.cleaned_data.get('name')
            space_characteristics.name = name
            space_characteristics.valid_from = form.cleaned_data.get('valid_from')
            space_characteristics.valid_to = form.cleaned_data.get('valid_to')
            space_characteristics.save()
            return redirect('/administration/spacecharacteristics')
        else:
            context = {
                'form': form,
                'id': id
            }
            return render(request, 'spacecharacteristics-edit.html', context)

def eventsCategoriesDelete (request):
    id = request.GET.get ('id')
    category = CategoryEvents.objects.get(id=id)
    category.delete()
    return redirect('/administration/categories-events')
def newsCategoriesDelete (request):
    id = request.GET.get('id')
    category = Category.objects.get(id=id)
    category.delete()
    return redirect('/administration/categories-news')
def workAreaDelete (request):
    id = request.GET.get('id')
    category = WorkArea.objects.get(id=id)
    category.delete()
    return redirect('/administration/workareas')
def spaceCharacteristicsDelete(request):
    id = request.GET.get('id')
    category = SpaceCharacteristics.objects.get(id=id)
    category.delete()
    return redirect('/administration/spacecharacteristics')

def codebooksRequests(request):
    return render(request, 'codebooks-requests.html')

def codebooksRequestsEvents(request):
    categories = CategoryEvents.objects.all().filter(approved=0)
    context = {
        'categories': categories
    }
    return render(request, 'codebooks-requests-events.html', context)

def codebooksRequestsEventsApprove(request):
    id = request.GET.get('id')
    category = CategoryEvents.objects.get(id=id)
    category.approved = 1
    category.save()
    return redirect('/administration/codebooks-requests/events')

def codebooksRequestsNews(request):
    categories = Category.objects.all().filter(approved=0)
    context = {
        'categories': categories
    }
    return render(request, 'codebooks-requests-news.html', context)

def codebooksRequestsNewsApprove (request):
    id = request.GET.get ('id')
    category = Category.objects.get(id=id)
    category.approved = 1
    category.save()
    return redirect('/administration/codebooks-requests/news')