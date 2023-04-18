from django.db import models


class Book(models.Model):
    """Class model for book"""
    title = models.CharField(max_length=30)
    rating = models.DecimalField(decimal_places=1, max_digits=2)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author = models.ManyToManyField('Author')

    def __str__(self):
        return self.title


class Category(models.Model):
    """Class model for category book"""
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Author(models.Model):
    """Class model for author book"""
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
