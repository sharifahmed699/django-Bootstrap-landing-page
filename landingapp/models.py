from django.db import models
from fontawesome_5.fields import IconField

# Create your models here.
class IconGrid(models.Model):
    icon = IconField()
    title = models.CharField(max_length = 50)
    desc = models.TextField()

class ImageShowCase(models.Model):
    title = models.CharField(max_length = 50)
    desc = models.TextField()
    img = models.ImageField(upload_to = 'pics')
    show = models.BooleanField(default=False)

class Testimonial(models.Model):
    title = models.CharField(max_length = 50)
    img = models.ImageField(upload_to = 'pics')
    name = models.CharField(max_length = 30)
    desc = models.TextField()

