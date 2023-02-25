import sweetify
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.views import View

from core.models import Home, About, Profile, Category, Portfolio, Education
from portfolio import settings


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


class Contact(View):

    def get(self, request):
        # home = Home.objects.latest('updated')
        home = Home.objects.all()
        # about = About.objects.latest('updated')
        about = About.objects.all()
        profiles = Profile.objects.filter(about=about)

        context = {
            'home': home,
            'about': about,
            'profiles': profiles,
        }
        return render(request, 'core/contact.html', context)

    def post(self, request):
        email = request.POST.get('email')
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        # print(email)

        template = get_template('core/success_email.html')

        # Se renderiza el template y se envias parametros
        content = template.render({'email': email, 'name': name, 'subject': subject})
        # Se crea el correo (titulo, mensaje, emisor, destinatario)
        msg = EmailMultiAlternatives(
            'Mensaje desde el Portafolio ',
            'Este un mensaje para usted desde :',
            email,
            [settings.EMAIL_HOST_USER]
        )
        msg.attach_alternative(content, 'text/html', )
        msg.send()
        return redirect("/contact/")

        return render(request, 'core/contact.html')


# Funcion de portafolio para mostrar los parametros necesarios
def portfolio(request):
    port = Portfolio.objects.all()
    # home = Home.objects.latest("updated")
    home = Home.objects.all()
    print(home)
    context = {
        "portfolio": port,
        "home": home
    }
    return render(request, 'core/portfolio.html', context)
