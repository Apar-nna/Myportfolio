# profiles/models.py

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    skills = models.CharField(max_length=100, blank=True)
    contact = models.EmailField(blank=True)

    def __str__(self):
        return self.user.username

class PortfolioItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio_images/', blank=True)
    link = models.URLField(blank=True)
    project_description = models.TextField()
    project_image = models.ImageField(upload_to='project_images/', blank=True)
    project_link = models.URLField(blank=True)

    def __str__(self):
        return self.title
