from django.contrib.auth.models import Permission
from django.shortcuts import render
from django.shortcuts import HttpResponse
from .forms import RegisterForm, RegisterFormOrg, User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .models import Profile

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
            info.city = form.cleaned_data.get('city')
            info.address = form.cleaned_data.get('address')
            info.number = form.cleaned_data.get('number')
            info.contact_person = form.cleaned_data.get("contact_person")
            info.phone = form.cleaned_data.get('phone')
            info.description = form.cleaned_data.get ('description')
            info.work_area = form.cleaned_data.get('work_area')
            info.web_site = form.cleaned_data.get("web_site")
            form.save()
            info.user = User.objects.last()
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