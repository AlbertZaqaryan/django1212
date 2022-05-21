from django.db import models

# Create your models here.

class Bag(models.Model):
    name = models.CharField('Bag name', max_length=50)
    about = models.TextField('Bag about')
    price = models.IntegerField('Bag price')
    img = models.ImageField('Bag image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Bag'
        verbose_name_plural = 'Bags'