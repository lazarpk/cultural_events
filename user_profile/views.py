from django.shortcuts import render
from django.shortcuts import HttpResponse
from registration.models import Profile
from .forms import UpdateUserForm, UpdateProfileForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
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
        return HttpResponse("<h1>Niste organizacija. Dopuniti izgled ove strane</h1>")
    else:
        return render(request, 'details.html')






def edit (request):
    form = UpdateUserForm(instance=request.user)
    form1 = UpdateProfileForm(instance=Profile.objects.get(user_id = request.user.id))
    context = {
        'form': form,
        'form1': form1
    }
    return render (request, 'edit.html', context)