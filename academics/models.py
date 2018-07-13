from django.db import models

class Subject(models.Model):

    name = models.CharField(max_length=100)
    code = models.IntegerField(unique=True, blank=False)
    course = models.IntegerField()
    semester = models.IntegerField()
    itinerary = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

class Study(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField(unique=True, blank=False)
    location = models.CharField(max_length=100)
    subject = models.ManyToManyField(Subject)

    def __str__(self):
        return str(self.name)
