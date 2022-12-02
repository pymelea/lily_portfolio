from django.shortcuts import render

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


def about(request):
    return render(request, 'core/about.html')


def skill(request):
    return render(request, 'core/skill.html')


def portfolio(request):
    return render(request, 'core/portfolio.html')


def contact(request):
    # Home
    home = Home.objects.latest('updated')
    # About
    about = About.objects.latest('updated')
    # Profile
    profiles = Profile.objects.filter(about=about)
    context = {
        'home': home,
        'profiles': profiles,
        'about': about,
    }
    return render(request, 'core/contact.html', context)