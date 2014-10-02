# Create your views here.

#3 from django.template import Context, loader

from django.shortcuts import render_to_response
from polls.models import Poll, Choice
from django.http import HttpResponse

# from django.http import Http404
from django.shortcuts import get_object_or_404

#5 

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext


def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]

    #3 t = loader.get_template('polls/index.html')
    #3 c = Context({
        #     'latest_poll_list': latest_poll_list,
         #   })

    #2 output = ', '.join([p.question for p in latest_poll_list])
    #1 return HttpResponse("Hello World. You are at the poll index.")
    #2 return HttpResponse(output)
    
    #3 return HttpResponse(t.render(c))

    #adding shortcut to load a template, fill a context and return an HttpResponse object with the result of the rendered template

    return render_to_response('polls/index.html', {'latest_poll_list': latest_poll_list})



def detail(request, poll_id):
    #return HttpResponse("You are looking at poll %s." % poll_id)

#    try:
#        p = Poll.objects.get(pk=poll_id)
#    except Poll.DoesNotExist:
#        raise Http404
#    return render_to_response('polls/detail.html', {'poll': p})

    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/detail.html', {'poll': p}, context_instance=RequestContext(request))


#5 

def vote(request, poll_id):
    #5 return HttpResponse("You are voting on poll %s." % poll_id)
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render_to_response('polls/detail.html', {
                'poll': p,
                'error_message': "You didn't select a choice.",
                }, context_instance=RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always retun an HttpResponseRedirect after successfully dealing 
        # with a POST data. This prevents date from being posted twice if a 
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls.views.results', args=(p.id,)))


def results(request, poll_id):
    #6return HttpResponse("You are looking at the results of poll %s." % poll_id)

    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/results.html', {'poll':p})

