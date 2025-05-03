from django.shortcuts import render
from .models import Profile, Experience, Skill, SocialMedia

def home(request):
    profile = Profile.objects.first()
    experiences = Experience.objects.all()
    skills = Skill.objects.all()
    socials = SocialMedia.objects.all()

    context = {
        'profile': profile,
        'experiences': experiences,
        'skills': skills,
        'socials': socials
    }

    return render(request, 'index.html', context)
