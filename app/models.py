from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ProfileUserInfoModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    portfoliowebsite = models.URLField(blank=True)
    photo = models.ImageField(upload_to='uploaded_pics/', blank=True)

    def __str__(self):
        return self.user.username
