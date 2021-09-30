from django.db import models


class Starter(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)


class Salad(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)


class Specialty(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)


class Table(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    date = models.DateTimeField()
    persons = models.IntegerField()
    message = models.TextField()


class Response(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    subjects = models.CharField(max_length=40)
    message = models.TextField()


class Program(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    date = models.DateTimeField()
    events = models.TextField()
    persons = models.IntegerField()