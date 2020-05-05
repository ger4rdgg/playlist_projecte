from django.db import models


class song(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    length = models.IntegerField()

    def __str__(self):
        return "{0}".format(self.name)


class list(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    length = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    songs = models.ManyToManyField(song)

    def __str__(self):
        return "name:{0}, songs:{1}".format(self.name, self.songs)


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