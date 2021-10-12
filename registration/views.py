from django.contrib.auth.models import Permission
from django.shortcuts import render
from django.shortcuts import HttpResponse
from .forms import RegisterForm, RegisterFormOrg, User, AddWorkAreaForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .models import Profile
from events.forms import AddEventCategoryForm, AddSpaceCharacteristicsForm
from news.forms import AddCategoryForm
from events.models import CategoryEvents

# Create your views here.
def registration (request):
    return render(request, 'registration.html')


def register (request):
    if (request.method == "GET"):
        form = RegisterForm()
        context = {
            'form':form
        }

        return render (request, 'reg_guest.html', context)
    elif (request.method == "POST"):
        form = RegisterForm(request.POST)

        if (form.is_valid()):
            if request.user.is_superuser:
                # user = form.save (commit = False)
                # user.is_superuser = 1
                # user.save()
                form.save()
                user = User.objects.last()
                user.is_superuser = 1
                user.save()
                return render(request, 'index-admin.html')
            else:
                form.save()

                username = form.cleaned_data.get ("username")
                password = form.cleaned_data.get ("password1")

                user = authenticate(username= username, password= password)
                login (request, user)
                return redirect('index')
        else:
            context = {
                'form': form
            }
            return render ( request, 'reg_guest.html', context)

def register_org (request):
    if (request.method == "GET"):
        form = RegisterFormOrg()
        context = {
            'form': form
        }
        return render(request, 'reg_org.html', context)
    elif (request.method == "POST"):
        form = RegisterFormOrg (request.POST)

        if (form.is_valid()):
            info = Profile()
            #info.city.set (form.cleaned_data.get('city'))
            #info.address.set(form.cleaned_data.get('address'))
            info.number = form.cleaned_data.get('number')
            info.contact_person = form.cleaned_data.get("contact_person")
            info.phone = form.cleaned_data.get('phone')
            info.description = form.cleaned_data.get ('description')
            #info.work_area.set(form.cleaned_data.get('work_area'))
            info.web_site = form.cleaned_data.get("web_site")
            form.save()
            info.user = User.objects.last()
            info.save()
            info = Profile.objects.last()
            info.city.set(form.cleaned_data.get('city'))
            info.address.set(form.cleaned_data.get('address'))
            info.work_area.set(form.cleaned_data.get('work_area'))
            info.save()

            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")

            user = authenticate(username=username, password=password)
            permission = Permission.objects.get(codename='article_can_create')
            user.user_permissions.add(permission)
            permission = Permission.objects.get(codename='advert_can_create')
            user.user_permissions.add(permission)
            permission = Permission.objects.get(codename='poll_can_create')
            user.user_permissions.add(permission)
            permission = Permission.objects.get(codename='event_can_create')
            user.user_permissions.add(permission)
            login(request, user)

            return redirect('index')
        else:
            context = {
                'form':form
            }
            return render (request, 'reg_org.html', context)

def login_success (request):
    try:
        curently_user = Profile.objects.get(user_id = request.user)
    except Profile.DoesNotExist:
        curently_user = None

    if curently_user == None:
        return redirect('/')
    else:
        return redirect('/profile')



#TODO: ***POGLEDATI ZASTO NE PREPOZNAJE NAVEDENE VARIJABLE (SIVE)***

def AddEventsCategory (request):
    if request.method == "GET":
        form = AddEventCategoryForm()
        return render(request, 'categories-events-new.html', {'form': form})
    elif request.method == "POST":
        form = AddEventCategoryForm(request.POST)

        if (form.is_valid()):
            CategoryEvents = form.save(commit=False)
            CategoryEvents.name = form.cleaned_data.get('name')
            CategoryEvents.valid_from = form.cleaned_data.get('valid_from')
            CategoryEvents.valid_to = form.cleaned_data.get('valid_to')
            if request.user.is_superuser:
                CategoryEvents.approved = 1
            else:
                CategoryEvents.approved = 0
            CategoryEvents.save()
            if request.user.is_superuser:
                return redirect('/administration/categories-events')
            else:
                return redirect('/profile/categories-events')
        else:
            return render(request, 'categories-events-new.html', {'form': form})


def AddNewsCategory (request):
    if request.method == "GET":
        form = AddCategoryForm()
        return render(request, 'categories-news-new.html', {'form': form})
    elif request.method == "POST":
        form = AddCategoryForm(request.POST)

        if (form.is_valid()):
            Category = form.save(commit=False)
            Category.Name = form.cleaned_data.get('Name')
            Category.Valid_from = form.cleaned_data.get('valid_from')
            Category.Valid_to = form.cleaned_data.get('valid_to')
            if request.user.is_superuser:
                Category.approved = 1
            else:
                Category.approved = 0
            Category.save()
            if request.user.is_superuser:
                return redirect('/administration/categories-news')
            else:
                return redirect('/profile/categories-news')
        else:
            return render(request, 'categories-news-new.html', {'form': form})


def AddWorkArea (request):
    if request.method == "GET":
        form = AddWorkAreaForm()
        return render(request, 'workareas-new.html', {'form': form})
    elif request.method == "POST":
        form = AddWorkAreaForm(request.POST)

        if (form.is_valid()):
            WorkArea = form.save(commit=False)
            WorkArea.name = form.cleaned_data.get('name')
            WorkArea.valid_from = form.cleaned_data.get('valid_from')
            WorkArea.valid_to = form.cleaned_data.get('valid_to')
            if request.user.is_superuser:
                WorkArea.approved = 1
            else:
                WorkArea.approved = 0
            WorkArea.save()
            if request.user.is_superuser:
                return redirect('/administration/workareas/')
            else:
                return redirect('/profile/workareas')
        else:
            return render(request, 'workareas-new.html', {'form': form})


def AddSpaceCharacteristic (request):
    if request.method == "GET":
        form = AddSpaceCharacteristicsForm()
        return render(request, 'spacecharacteristics-new.html', {'form': form})
    elif request.method == "POST":
        form = AddSpaceCharacteristicsForm(request.POST)

        if (form.is_valid()):
            SpaceCharacteristics = form.save(commit=False)
            SpaceCharacteristics.name = form.cleaned_data.get('name')
            SpaceCharacteristics.valid_from = form.cleaned_data.get('valid_from')
            SpaceCharacteristics.valid_to = form.cleaned_data.get('valid_to')
            if request.user.is_superuser:
                SpaceCharacteristics.approved = 1
            else:
                SpaceCharacteristics.approved = 0
            SpaceCharacteristics.save()
            if request.user.is_superuser:
                return redirect('/administration/spacecharacteristics')
            else:
                return redirect('/profile/spacecharacteristics')
        else:
            return render(request, 'spacecharacteristics-new.html', {'form': form})