from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from website.models import Contact
from website.forms import NameForm,ContactForm,NewsletterForm
from django.contrib import messages


def index_view(request):
    return render(request,'website/index.html')

def about_view(request):
    return render(request,'website/about.html')




def contact_view(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            new_name=form.save(commit=False)
            new_name.name='unknown'
            new_name.save()
            messages.add_message(request,messages.SUCCESS,"your ticket submited successfully")
        else:
            messages.add_message(request,messages.ERROR,"your ticket didnt submited")
    form=ContactForm()
    return render(request,'website/contact.html',{'form':form})

def newsletter_view(request):
    if request.method=='POST':
        form=NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    
    else:
        return HttpResponseRedirect('/')


def coming_soon_view(request):
    return render(request,'website/coming_soon.html')

# def handler404(request, *args, **kwargs):
#     return HttpResponseRedirect('/coming_soon')