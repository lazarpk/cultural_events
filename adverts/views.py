from django.shortcuts import render

from .models import Adverts;

from .forms import AdvertsCreateForm;

from django.shortcuts import redirect;
from .forms import AdvertsSearchForm;
# Create your views here.
def index (request):
    form = AdvertsSearchForm ( request.GET);
    query = Adverts.objects;

    if ( form.is_valid()):
        title = form.cleaned_data.get( 'title' );
        if (len (title) > 0):
            query = query.filter (
                title__contains = title
            )

    adverts = query.all();

    context = {
        'form': form,
        'adverts': adverts
    }

    return render (request,'adverts/index.html', context);

def create (request):
    form = AdvertsCreateForm ( );

    if(request.method == "POST"):
        form = AdvertsCreateForm (request.POST);
        if (form.is_valid()):
            form.save();
            return redirect( 'index');

    context = {
        'form': form
    }

    return render (request, 'adverts/create.html',context)

def edit(request):
    if (request.method == "GET"):
        id = request.GET.get('id');
        adverts = Adverts.objects.get (id=id );
        form = AdvertsCreateForm ( instance=adverts );

        context = {
            'id': id,
            'form':form
        };
        return render( request, 'adverts/edit.html', context);
    elif (request.method == 'POST'):
        form = AdvertsCreateForm (request.POST);
        id = request.POST.get ("id");
        if (form.is_valid()):
            advert = Adverts.objects.get (id=id);
            advert.title = form.cleaned_data.get ('title');
            advert.description = form.cleaned_data.get('description');
            advert.load_date = form.cleaned_data.get ('load_date');
            advert.expire_date = form.cleaned_data.get('expire_date');
            advert.save ();

            return redirect ('adverts:index')
        else:
            context = {
                "id": id,
                "form": form
            };
            return render ( request, "adverts/edit.html", context );