from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from .forms import ContactForm


def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
        form_anchor = ''
        message = 'blank'
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail("New message from - {}".format(name), message, email, ['admin@example.com'])
                form.save()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, "contact/success.html")
        else:
            # there is an issue with the captcha form
           form_anchor = "fail_anchor"
           message = "failed"
    return render(request, "contact/contact-us.html", {'form': form, 'form_anchor':form_anchor, 'message':message})

def successView(request):
    return render(request, "contact/success.html")