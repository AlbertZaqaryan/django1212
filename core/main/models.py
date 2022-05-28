from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField('Category name', max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Shoose(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_shoose')
    name = models.CharField('Shoose name', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Shoose'
        verbose_name_plural = 'Shooses'

class Brend(models.Model):
    shoose = models.ForeignKey(Shoose, on_delete=models.CASCADE, related_name='shoose_brend')
    name = models.CharField('Brend name', max_length=50)
    img = models.ImageField('Brend image', upload_to='media')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Brend'
        verbose_name_plural = 'Brends'