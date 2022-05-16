from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from .forms import ContactForm
from .utils import send_html_mail
import time

def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
        form_anchor = ''
        message = 'blank'
    if request.method == 'POST':
        data = request.POST.copy()
        if 'h-captcha-response' in data:
            data['captcha'] = data['h-captcha-response']
        form = ContactForm(data)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                text = "<h2 style='color: red;'> <small>New message from the sancristocafe.com contact-us form! </small><br></h2>\
                            <p>************************************************************</p>\
                            <p><b>Name:</b> {0}</p> \
                            <p><b>Email:</b> {2}</p>   \
                            <p><b>Message Content: </b> <br>{3}<br></p> \
                            <p>************************************************************</p>\
                                <p><small> This contact form was submitted at {1} <br> \
                                <b>be sure to follow-up and have a great day! <br>--your sancristocafe.com site </small> </b></p> \
                                     ".format(name, time.ctime(), email, message)
                send_html_mail("[NOTICE] sancristocafe.com contact-us submission: {}".format(name), text, settings.CONTACT_US_NOTIFICATION_EMAIL_LIST, settings.EMAIL_HOST_USER)
                form.save()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, "contact/success.html")
        else:
            # there is an issue with the captcha form
           form_anchor = "contact_form"
           message = "failed"
    return render(request, "contact/contact-us.html", {'form': form, 'form_anchor':form_anchor, 'message':message})

def successView(request):
    return render(request, "contact/success.html")