from django.db import models

class Img(models.Model):
    img_url = models.ImageField(upload_to = 'img')
# Create your models here.
