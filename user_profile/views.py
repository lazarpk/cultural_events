from django.shortcuts import render
from django.shortcuts import HttpResponse, Http404
from registration.models import Profile, WorkArea
from .forms import UpdateUserForm, UpdateProfileForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from news.models import Article
from .forms import OrgSearchForm
from polls.models import Poll
from events.models import CategoryEvents, SpaceCharacteristics
from user_admin.forms import EventsCategorySearchForm, NewsCategorySearchForm, WorkAreaSearchForm, SpaceCharacteristicsSearchForm
from news.models import Category
# Create your views here.
def details (request):

    # Baca Gresku 404
    '''
    curently_user = get_object_or_404(Profile, user_id = request.user.id)
    if curently_user:
        return render(request, 'details.html')

    '''

    curently_user = ''
    try:
        curently_user = Profile.objects.get(user_id = request.user)
    except Profile.DoesNotExist:
        curently_user = None

    if curently_user == None :
        raise Http404
    else:
        articles = Article.objects.filter(ArchivedDate__isnull=True, Author=request.user).order_by('-id')[:10]
        polls = Poll.objects.filter (author=request.user)
        context = {
            'articles': articles,
            'polls': polls
        }
        return render(request, 'details.html', context)






def edit (request):
    if (request.method == 'GET'):
        form = UpdateUserForm(instance=request.user)
        form1 = UpdateProfileForm(instance=Profile.objects.get(user_id = request.user.id))
        context = {
            'form': form,
            'form1': form1
        }
        return render (request, 'edit.html', context)
    elif (request.method == "POST"):
        form = UpdateUserForm(request.POST, instance=request.user)
        form1 = UpdateProfileForm(request.POST)
        if (form.is_valid() and form1.is_valid()):
            user = User.objects.get(id = request.user.id)
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.username = form.cleaned_data.get('username')
            user.email = form.cleaned_data.get('email')
            user.save()

            profile = Profile.objects.get(user_id = request.user.id)
            profile.address = form1.cleaned_data.get('address')
            profile.number = form1.cleaned_data.get('number')
            profile.city = form1.cleaned_data.get('city')
            profile.contact_person = form1.cleaned_data.get('contact_person')
            profile.phone = form1.cleaned_data.get('phone')
            profile.description = form1.cleaned_data.get('description')
            profile.work_area = form1.cleaned_data.get('work_area')
            profile.web_site = form1.cleaned_data.get('web_site')
            profile.save()

            return render(request, 'details.html')
        else:
            form = UpdateUserForm(instance=request.user)
            form1 = UpdateProfileForm(instance=Profile.objects.get(user_id = request.user.id))
            context = {
                'form': form,
                'form1': form1
            }
            return render (request, 'edit.html', context)


def searchOrg (request):
    form = OrgSearchForm(request.GET)
    orgs = Profile.objects.all()

    if (form.is_valid()):
        username = form.cleaned_data.get('username')
        orgs = orgs.filter(user__username__icontains=username)

    context = {
        'form': form,
        'orgs': orgs
    }
    return render(request, 'search-organisations.html', context)

def profileUser (request):
    id = request.GET.get('id')
    user = User.objects.get(id=id)
    context = {
        'user': user
    }
    return render(request, 'profile-user.html', context)

def codebooksEdit (request):
    return render(request, 'codebooks-edit-org.html')

def eventsCategoriesOrg (request):
    categories = CategoryEvents.objects.all()
    form = EventsCategorySearchForm(request.GET)
    if (form.is_valid()):
        name = form.cleaned_data.get('name')
        categories = categories.filter(name__icontains=name)
    context = {
        'form': form,
        'categories': categories
    }
    return render(request, 'categories-events-org.html', context)

def newsCategoriesOrg (request):
    categories = Category.objects.all()
    form = NewsCategorySearchForm(request.GET)
    if (form.is_valid()):
        name = form.cleaned_data.get('name')
        categories = categories.filter(Name__icontains=name)
    context = {
        'form': form,
        'categories': categories
    }
    return render(request, 'categories-news-org.html', context)

def workAreaOrg(request):
    workareas = WorkArea.objects.all()
    form = WorkAreaSearchForm(request.GET)
    if (form.is_valid()):
        name = form.cleaned_data.get('name')
        workareas = workareas.filter(name__icontains = name)
    context = {
        'form':form,
        'workareas': workareas
    }
    return render (request, 'workarea-org.html', context)

def spaceCharacteristicOrg(request):
    spacecharacteristics = SpaceCharacteristics.objects.all()
    form = SpaceCharacteristicsSearchForm(request.GET)
    if (form.is_valid()):
        name = form.cleaned_data.get('name')
        spacecharacteristics = spacecharacteristics.filter(name__icontains=name)
    context = {
        'form': form,
        'spacecharacteristics': spacecharacteristics
    }
    return render(request, 'spacecharacteristics-org.html', context)