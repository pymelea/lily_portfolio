from django.http import HttpResponse, BadHeaderError
from django.shortcuts import render, redirect
from django.core.mail import send_mail

import json 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

from core.forms import ContactForm
from core.models import Home, About, Profile, Category, Portfolio, Education


# Create your views here.


def index(request):
    # Home
    home = Home.objects.latest('updated')

    # About
    about = About.objects.latest('updated')

    # Profile
    profiles = Profile.objects.filter(about=about)

    # Skill
    categories = Category.objects.all()

    # Portfolio
    portfolios = Portfolio.objects.all()

    # Education
    educations = Education.objects.all()

    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'portfolios': portfolios,
        'educations': educations,
    }
    return render(request, 'core/index.html', context)


# Corpo da mensagem do email #
# msg = MIMEMultipart()
# message = "Você recebeu um email da Pycodebr :)"
#
# # Credenciais e assunto do email #
# password = "Whittaker*86"
# msg['From'] = "lilycapetillo86@gmail.com"
# msg['To'] = "lilycapetillo86@gmail.com"
# msg['Subject'] = "Enviando gmail com Python" # Assunto do email
#
# # Monta conexão e envia o email #
# msg.attach(MIMEText(message, 'plain'))
# server = smtplib.SMTP('smtp.gmail.com', port=587)
# server.starttls()
# server.login(msg['From'], password)
# server.sendmail(msg['From'], msg['To'], msg.as_string())
# server.quit()



# def contactView(request):
#     if request.method == "POST":
#         form = ContactForm()
#     else:
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             msg['To'] = form.cleaned_data["subject"]
#             msg['From'] = form.cleaned_data["from_email"]
#             message = form.cleaned_data['message']
#             try:
#                 msg.attach(MIMEText(message, 'plain'))
#                 server = smtplib.SMTP('smtp.gmail.com', port=587)
#                 server.starttls()
#                 server.login(msg['From'], password)
#                 server.sendmail(msg['From'], msg['To'], msg.as_string())
#                 server.quit()
#                 send_mail(msg['From'], message,  msg['From'], ["lilycapetillo86@gmail.com"])
#             except BadHeaderError:
#                 return HttpResponse("Invalid header found.")
#             return redirect("success")
#     return render(request, "core/contact.html", {"form": form})

# def successView(request):
#     return HttpResponse("Success! Thank you for your message.")

def contactview(request):
    if request.method == "POST":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"] #'Asunto del correo'
            message = form.cleaned_data['message'] #'Contenido del correo'
            from_email = form.cleaned_data["from_email"]  #'tu@correo.com'
            recipient_list = ['djangopruebalo@gmail.com', 'djangopruebalo@gmail.com']

    return send_mail(subject, message, from_email, recipient_list)


def successview(request):
    contactview()
    return render(request, 'core/contact.html', {"form": form})
