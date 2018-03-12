from django.shortcuts import render
from django.conf import settings
# Create your views here.
def about(request):
    context={}
    template= 'about.html'
    return render(request,template,context)

def home(request):
    context={}
    template= 'home.html'
    return render(request,template,context)