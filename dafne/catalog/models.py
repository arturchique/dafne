from django.db import models
from django.urls import reverse


class Material(models.Model):
    name = models.CharField(max_length=50, verbose_name="материал")

    def __str__(self):
        return self.name


class Size(models.Model):
    SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=1, choices=SIZES)

    def __str__(self):
        return self.name


class Bag(models.Model):
    title = models.CharField(max_length=50, verbose_name="название")
    summary = models.CharField(max_length=1000, verbose_name="описание")
    size = models.ManyToManyField(Size, verbose_name="размер")
    price = models.FloatField(verbose_name="цена")
    qrcode = models.CharField(max_length=300, verbose_name="штрихкод")
    materials = models.ManyToManyField(Material, verbose_name="материал")

    def get_absolute_url(self):
        return reverse('bag-detail', args=[str(self.id)])

    def __str__(self):
        return self.title