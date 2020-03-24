# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from playlist_app import models

# Register your models here.
admin.site.register(models.song)
admin.site.register(models.tag)
admin.site.register(models.artist)
admin.site.register(models.list)


