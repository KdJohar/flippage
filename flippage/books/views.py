from django.shortcuts import render_to_response, RequestContext

# Create your views here.


def home(request):
    return render_to_response('ecommerce/index2.html', context_instance=RequestContext(request))

def bookdetail(request):
    return render_to_response('ecommerce/bookdetail.html', context_instance=RequestContext(request))
