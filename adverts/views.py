from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect, Http404
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required
from .models import Adverts, AdvertDeleteRequest;

from .forms import AdvertsCreateForm;
from .forms import AdvertsSearchForm;


# Create your views here.
def index(request):
    form = AdvertsSearchForm(request.GET);
    query = Adverts.objects.filter(date_archived__isnull=True).order_by('load_date')[:10];
    for advert in query:
        if advert.expire_date < datetime.date.today():
            advert.date_archived = timezone.now()
            advert.save()
    if (form.is_valid()):
        title = form.cleaned_data.get('title');
        if (len(title) > 0):
            query = query.filter(
                title__contains=title
            )

    adverts = query.all();

    context = {
        'form': form,
        'adverts': adverts
    }

    return render(request, 'adverts/index.html', context);


@permission_required('adverts.advert_can_create', '/login')
def create(request):
    if request.method == 'GET':
        form = AdvertsCreateForm();
        return render(request, 'adverts/create.html', {'form': form})

    elif request.method == "POST":
        form = AdvertsCreateForm(request.POST)

        if (form.is_valid()):
            advert = form.save(commit=False);
            current_user = request.user

            advert.author = current_user
            advert.save()

            return redirect('adverts:index');
        else:
            return render(request, 'adverts/create.html', {"form": form})


def edit(request):
    if (request.method == "GET"):
        id = request.GET.get('id');
        adverts = Adverts.objects.get(id=id);
        form = AdvertsCreateForm(instance=adverts);

        context = {
            'id': id,
            'form': form
        };
        return render(request, 'adverts/edit.html', context);
    elif (request.method == 'POST'):
        form = AdvertsCreateForm(request.POST);
        id = request.POST.get("id");
        if (form.is_valid()):
            advert = Adverts.objects.get(id=id);
            advert.title = form.cleaned_data.get('title');
            advert.description = form.cleaned_data.get('description');
            advert.load_date = form.cleaned_data.get('load_date');
            advert.expire_date = form.cleaned_data.get('expire_date');
            advert.save();

            return redirect('adverts:index')
        else:
            context = {
                "id": id,
                "form": form
            };
            return render(request, "adverts/edit.html", context);


def detail(request, *args, **kwargs):
    id = kwargs['id']
    advert = Adverts.objects.get(pk=id)

    if advert is None:
        raise Http404
    else:
        return render(request, 'adverts/detail.html', {'advert': advert})


def archive_advert(request, *args, **kwargs):
    id = kwargs['id']
    advert = Adverts.objects.get(pk=id)

    if advert is not None and advert.date_archived is None and request.user.id == advert.author.id:
        advert.date_archived = timezone.now()
        advert.save()
        message = 'Oglas je arhiviran.'

        return render(request, 'events/request_success.html', {'success_message': message})
    else:
        return HttpResponse(status=400)


def delete_advert_request(request, *args, **kwargs):
    id = kwargs['id']
    advert = Adverts.objects.get(pk=id)

    if advert is not None and AdvertDeleteRequest.get_if_exists(
            advert.id) is None and request.user.id == advert.author.id:
        delete_advert_request = AdvertDeleteRequest()
        delete_advert_request.User = request.user
        delete_advert_request.Advert = advert
        delete_advert_request.save()
        message = 'Zahtev za brisanje oglasa je poslat administratoru.'

        return render(request, 'adverts/request_success.html', {'success_message': message})
    else:
        message = 'Zahtev za brisanje oglasa je već prosleđen administratoru!'
        return render(request, 'adverts/request_success.html', {'success_message': message})


def delete_request_admin(request):
    queryset = AdvertDeleteRequest.objects.all();
    if not queryset:
        message = 'Nema zahteva za brisanje oglasa.'
        return render(request, "adverts/request_success.html", {'success_message': message})
    else:
        context = {
            'object_list': queryset
        }

    return render(request, 'adverts/delete_request.html', context);


def delete_advert(request, id):
    obj = AdvertDeleteRequest.objects.get(Advert_id=id)
    obj2 = Adverts.objects.get(pk=id)
    obj.delete()
    obj2.delete()
    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)
