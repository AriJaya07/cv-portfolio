from django.db import models

class Profile(models.Model): 
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='profile/', blank=True, null=True)
    description = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
    
class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()
    start_year = models.IntegerField()
    end_year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} at {self.company}"
    
class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=50, blank=True) # contoh: biginner, intermediate, advanced

    def __str__(self):
        return self.name
    
class SocialMedia(models.Model):
    platform = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return self.platform