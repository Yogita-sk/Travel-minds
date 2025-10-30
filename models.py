from django.db import models

class PlaceImage(models.Model):
    place_name = models.CharField(max_length=255)
    image_url = models.CharField(max_length=10204)

    def __str__(self):
        return self.place_name
