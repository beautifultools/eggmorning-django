from django.db import models
from .common import RankCategory


class Hotel(models.Model):
    hotel_no = models.IntegerField()
    addr = models.CharField(max_length=256)


class HotelScore(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    category = models.ForeignKey(RankCategory, on_delete=models.CASCADE)
    score = models.FloatField()

