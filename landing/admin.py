from django.contrib import admin
from .models import Profile, Experience, Skill, SocialMedia

admin.site.register(Profile)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(SocialMedia)