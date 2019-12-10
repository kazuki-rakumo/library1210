from django.db import models
from django.utils import timezone

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Shelf_number(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Models):
    author=models.ForeignKey('Author',on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    published_date=models.DateField(blank=True,null=True)
    registed_date=models.DateTimeField(default=timezone.now)
    publisher=models.ForeignKey('Publisher',on_delete=models.CASCADE)
    shelf_number=models.ForeignKey('Shelf_number',on_delete=models.CASCADE)
    category=models.ForeignKey('Category',on_delete=models.CASCADE)


    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title
