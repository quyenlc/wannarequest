from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=50)


class Product(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=50)
