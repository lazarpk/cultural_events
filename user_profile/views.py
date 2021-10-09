from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse, Http404
from registration.models import Profile, StreetAddress
from .forms import UpdateUserForm, UpdateProfileForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from news.models import Article
from .forms import OrgSearchForm
from polls.models import Poll
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
        profile = Profile.objects.get(user_id = request.user)
        addresses = profile.address.all()
        cities = profile.city.all()
        work_areas = profile.work_area.all()
        profile_work_area = ''
        profile_city = ''
        profile_adress = ''
        for address in addresses:
            profile_adress = address.name
        for city in cities:
            profile_city = city.name
        for work_area in work_areas:
            profile_work_area = work_area
        context = {
            'articles': articles,
            'polls': polls,
            'profile_adress': profile_adress,
            'profile_city': profile_city,
            'profile_work_area': profile_work_area
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

        #for field in form1:
        #    print("Field Error:", field.errors)
        if (form.is_valid() and form1.is_valid()):
            user = User.objects.get(id = request.user.id)
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.username = form.cleaned_data.get('username')
            user.email = form.cleaned_data.get('email')
            user.save()

            profile = Profile.objects.get(user_id = request.user.id)
            #profile.address = form1.cleaned_data.get('address')
            profile.address.set(form1.cleaned_data.get('address'))

            profile.number = form1.cleaned_data.get('number')
            #profile.city = form1.cleaned_data.get('city')
            profile.city.set(form1.cleaned_data.get('city'))

            profile.contact_person = form1.cleaned_data.get('contact_person')
            profile.phone = form1.cleaned_data.get('phone')
            profile.description = form1.cleaned_data.get('description')
            #profile.work_area = form1.cleaned_data.get('work_area')
            profile.work_area.set(form1.cleaned_data.get('work_area'))

            profile.web_site = form1.cleaned_data.get('web_site')
            profile.save()

            #return render(request, 'details.html')
            return redirect('/profile')
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
    profile = Profile.objects.get(user_id=id)
    addresses = profile.address.all()
    cities = profile.city.all()
    work_areas = profile.work_area.all()
    profile_work_area = ''
    profile_city = ''
    profile_adress = ''
    for address in addresses:
        profile_adress = address.name
    for city in cities:
        profile_city = city.name
    for work_area in work_areas:
        profile_work_area = work_area
    context = {
        'user': user,
        'profile_adress': profile_adress,
        'profile_city': profile_city,
        'profile_work_area': profile_work_area
    }
    return render(request, 'profile-user.html', context)