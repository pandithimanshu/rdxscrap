from django.db import models
from rest_framework import serializers


# Create your models here.

class Quote(models.Model):

    title = models.CharField(max_length=100,default="defaulttitle")
    token = models.CharField(max_length=100,default="defaulttoken")
    url = models.CharField(max_length=100,default="defaulturl")

    def __str__(self):
        return self.title

class QuoteSerializers(serializers.Serializer):

    title = serializers.CharField(max_length=100)
    token = serializers.CharField(max_length=100)
    url = serializers.CharField(max_length=100)
    id = serializers.IntegerField()