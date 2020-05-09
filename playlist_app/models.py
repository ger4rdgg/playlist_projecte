from django.db import models
from django.urls.base import reverse


class song(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    length = models.IntegerField()

    def get_absolute_url(self):
        return reverse('song_detail', args=[self.id])

    def __str__(self):
        return "name:{0}, length:{1}".format(self.name, self.length)

    # def get_absolute_url(self):
    #     return reverse('playlist_app:')


class list(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    length = models.IntegerField()
    songs = models.ManyToManyField(song)

    def __str__(self):
        return "name:{0}, description:{1}, length:{2}".format(self.name,self.description, self.length)


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
