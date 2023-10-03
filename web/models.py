from django.db import models


class EmergingDJ(models.Model):
    dj_name = models.CharField(max_length=100)
    music_genre = models.CharField(max_length=100)
    bio = models.TextField()
    soundcloud_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to="dj_images/", blank=True)

    def __str__(self):
        return self.dj_name
