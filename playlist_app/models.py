from django.db import models


class song(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    length = models.IntegerField()

    def __str__(self):
        return "name:{0}, length:{1}".format(self.name, self.length)


class list(models.Model)
    name = models.CharField(max_length=20, blank=True, null=True)
    length = models.IntegerField()
    songs = models.ManyToManyField(song)

    def __str__(self):
        return "name:{0}, length:{1}".format(self.name, self.length)


class artist(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    songs = models.ManyToManyField(song)

    def __str__(self):
        return "name:{0}".format(self.name)


class tag(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    songs = models.ManyToManyField(song)
    lists = models.ManyToManyField(list)

    def __str__(self):
        return "name:{0}".format(self.name)