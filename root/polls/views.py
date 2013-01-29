# Create your views here.
from polls.models import Poll, Choice
from django.http import HttpResponse  #only needed for indexOLD
from django.template import Context, loader #only needed for indexOLD
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django.core.urlresolvers import reverse

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render_to_response('polls/index.html', {'latest_poll_list': latest_poll_list})

def indexOLD(request):
    #return HttpResponse('Hello, world. Youre at the poll index, player 1.')
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    t = loader.get_template('polls/index.html')
    c = Context({
        'latest_poll_list': latest_poll_list,
    })
    #output = ', '.join ([p.question for p in latest_poll_list])
    #return HttpResponse(output)
    return HttpResponse(t.render(c))

def detail(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/detail.html', {'poll': p},
            context_instance = RequestContext(request))

def detailWOShortcut(request, poll_id):
    try:
        p = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404
    return render_to_response('polls/detail.html', {'poll': p})

def detailOLD(request, poll_id):
    return HttpResponse('Youre looking at the detail page of poll %s, player 1.' % poll_id)

def resultsTRY(request, poll_id):
    return render_to_response('New results page with the shortcut, used by player 1 on poll id %s')

def results(request, poll_id):
    #return HttpResponse('Youre looking at the results page of poll %s, player 1.' % poll_id)
    p = get_object_or_404(Poll, pk = poll_id)
    return render_to_response('polls/results.html', {'poll': p})

def vote(request, poll_id):
    #return HttpResponse('Youre voting on poll %s, player 1.' % poll_id)
    p = get_object_or_404(Poll, pk = poll_id)
    try:
        selected_choice = p.choice_set.get(pk = request.POST ['choice'])
    except (KeyError, Choice.DoesNotExist):
        #Redisplay the poll voting form.
        return render_to_response('polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        }, context_instance = RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        #Always return an HttpResponseRedirect after successfully dealing
        #with POST data. This prevents data from being posted twisce if a
        #user hits the Back button
        return HttpResponseRedirect(reverse('polls.views.results', args = (p.id,)))

