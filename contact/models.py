from django.db import models


class Contact(models.Model):
    address = models.CharField(max_length=250, verbose_name='')
   