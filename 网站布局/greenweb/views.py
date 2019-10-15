from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response


def index(request):
    return render_to_response('index.html',locals())
def contact(request):
    return render_to_response('contact.html', locals())
def joblist(request):
    return render_to_response('joblist.html',locals())
def jobwen(request):
    return render_to_response('jobwen.html',locals())
def list(request):
    return render_to_response('list.html',locals())
def list2(request):
    return render_to_response('list2.html',locals())
def newcontent(request):
    return render_to_response('newcontent.html',locals())
def newlist(request):
    return render_to_response('newlist.html',locals())
def qyjj(request):
    return render_to_response('qyjj.html',locals())
