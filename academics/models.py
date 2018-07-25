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


class References(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    id = models.IntegerField(auto_created=True, unique=True, primary_key=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Modul(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.name)