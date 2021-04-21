<<<<<<< HEAD
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
=======
<<<<<<< HEAD
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Question, Choice
from django.http import JsonResponse

from django.contrib.auth.decorators import login_required

# Get questions and display them
# @login_required
def index(request):
    current_questions = Question.objects.order_by('-pub_date')[:5]
    context = {'current_questions': current_questions}
    return render(request, 'polls/index.html', context)

# Show specific question and choices
@login_required
def detail(request, question_id):
  try:
    question = Question.objects.get(pk=question_id)
  except Question.DoesNotExist:
    raise Http404("Question does not exist")
  return render(request, 'polls/detail.html', { 'question': question })

# Get question and display results
# @login_required
def results(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls/results.html', { 'question': question })

# Vote for a question choice
@login_required
def vote(request, question_id):
    # print(request.POST['choice'])
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

@login_required
def resultsData(request, obj):
    votedata = []

    question = Question.objects.get(id=obj)
    votes = question.choice_set.all()

    for i in votes:
        votedata.append({i.choice_text:i.votes})

    return JsonResponse(votedata, safe=False)
=======
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
>>>>>>> c915ff6c59d82525151f3696c383766d57fd83e2
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
<<<<<<< HEAD
    return render(request, 'polls/results.html', context)
=======
    return render(request, 'polls/results.html', context)
>>>>>>> dd8e683bf902422332c15d70d55d3d53b3553e2d
>>>>>>> c915ff6c59d82525151f3696c383766d57fd83e2
