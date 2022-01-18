from django.db import models

# Create your models here.
class profile(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    skill = models.TextField(max_length=100)
    about_you = models.TextField(max_length=100)
    previous_work = models.TextField(max_length=100)

    def __str__(self):
        return self.name