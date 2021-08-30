from django.shortcuts import render
from django.shortcuts import HttpResponse
from .forms import RegisterForm, RegisterFormOrg, User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

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
            form.save()

            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
        else:
            context = {
                'form':form
            }
            return render (request, 'reg_org.html', context)