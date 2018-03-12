from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import contactForm
from contact.models import Information
from django.http import HttpResponse
# Create your views here.

def contact1(request):
    context={}
    template= 'contact2.html'
    return render(request,template,context)

   
    return render(request,template,context)

def contact(request):
    context={}
    template= 'contact1.html'
    return render(request,template,context)

def infosubmit(request):
    if request.method =='POST':
        name=request.POST['name']
        email=request.POST['email']
        mobile=request.POST['mobile']
        info=request.POST['info']
        cost=request.POST['cost']


        Information.objects.create(

        name = name,
        email = email,
        mobile = mobile,
        info = info,
        cost = cost

        )
        

        return HttpResponse('')

