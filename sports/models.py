from django.db import models
from django.shortcuts import reverse


class Sport(models.Model):
    name = models.CharField(max_length=100)
    location = models.TextField()
    date = models.DateField()
    sport_type = models.CharField(max_length=50)


    def get_detail_url(self):
        return reverse('sports:sport_detail', args=[self.pk])


    def get_delete_url(self):
        return reverse('sports:sport_delete', args=[self.pk])


    def get_update_url(self):
        return reverse('sports:update_sport', args=[self.pk])
