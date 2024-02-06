from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=250, verbose_name='')
    slug = models.SlugField(max_length=250, unique=True, verbose_name='')

    def __str__(self):
        return f"{self.category_name}"

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''


class Catalog(models.Model):
    catalog_name = models.CharField(max_length=250)
    description = models.TextField(verbose_name='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='')
    image = models.ImageField(upload_to='catalog/%Y/%m/%d/', verbose_name='')
    create_at = models.DateField(auto_now_add=True, verbose_name='')

    def __str__(self):
        return f"{self.catalog_name}"

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''
