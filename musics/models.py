from django.db import models
from django.urls import reverse


class Music(models.Model):
    album_title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    date = models.DateField()
    genre = models.CharField(max_length=50)


    def get_detail_url(self):
        return reverse('musics:music_detail', args=[self.pk])


    def get_delete_url(self):
        return reverse('musics:music_delete', args=[self.pk])


    def get_update_url(self):
        return reverse('musics:update_music', args=[self.pk])