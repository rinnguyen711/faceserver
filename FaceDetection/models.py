from django.db import models
from django.contrib.postgres.fields import ArrayField



class FaceDetection(models.Model):
    image = models.ImageField()
    rects = ArrayField(ArrayField(models.FloatField(), max_length=4), null=True)
    image_link = models.CharField(max_length=100, null=True)



