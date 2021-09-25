from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from .forms import UserSearchForm
from user_profile.forms import UpdateUserForm, UpdateProfileForm
from registration.models import Profile
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
