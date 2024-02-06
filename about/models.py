from django.db import models


class About(models.Model):
    about_description = models.TextField(verbose_name='')
    image = models.ImageField(upload_to='about/%Y/%m/%d/', verbose_name='')