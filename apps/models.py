from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=150)
    number = models.CharField(max_length=100)
    email = models.EmailField()
    promo = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.name}'

class Syrfull(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    video = models.FileField(upload_to='uploads/%Y/%m/%d/',blank=True)

