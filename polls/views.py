from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import CreatePollForm
from .models import Polls

def home(request):
    polls = Polls.objects.all()
    context = {
        'polls' : polls
    }
    return render(request, 'polls/home.html', context)

def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreatePollForm()
    context = {
        'form' : form
    }
    return render(request, 'polls/create.html', context)

def vote(request, poll_id):
    poll = Polls.objects.get(pk=poll_id)

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

        return redirect('results', poll.id)

    context = {
        'poll' : poll
    }
    return render(request, 'polls/vote.html', context)

def results(request, poll_id):
    poll = Polls.objects.get(pk=poll_id)
    context = {
        'poll' : poll
    }
    return render(request, 'polls/results.html', context)