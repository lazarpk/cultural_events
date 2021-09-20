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