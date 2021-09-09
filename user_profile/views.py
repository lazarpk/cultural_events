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