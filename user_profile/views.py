from django.shortcuts import render
from django.shortcuts import HttpResponse
from registration.models import Profile
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