from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from .forms import CreatePollForm
from .models import Poll

def index(request):
    polls = Poll.objects.all()
    context = {
        'polls' : polls
    }
    return render(request, 'polls/index.html', context)

@permission_required('poll_can_create', '/login')
def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            poll = form.save(commit=False);
            current_user = request.user

            poll.author = current_user
            poll.save()
            return redirect('polls:index')
    else:
        form = CreatePollForm()
    context = {
        'form' : form
    }
    return render(request, 'polls/create.html', context)

def vote(request, id):
    poll = Poll.objects.get(pk=id)

    if request.method == 'POST':

        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count += 1
        else:
            return HttpResponse(400, 'Invalid form')

        poll.save()


        return redirect('polls:index')

    context = {
        'poll' : poll
    }
    return render(request, 'polls/vote.html', context)

def results(request, id):
    poll = Poll.objects.get(pk=id)
    context = {
        'poll' : poll
    }
    return render(request, 'polls/results.html', context)