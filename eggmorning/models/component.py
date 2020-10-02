from django.db import models


class MainSlide(models.Model):
    title = models.CharField(max_length=128, default='')
    image = models.CharField(max_length=1024, default='')
    username = models.CharField(max_length=64, default='')
    desc = models.CharField(max_length=256, default='')
    priority = models.IntegerField()
    start_date = models.DateTimeField('start display datetime')
    end_date = models.DateTimeField('end display datetime')
    mod_date = models.DateTimeField(auto_now=True)
    reg_date = models.DateTimeField(auto_now_add=True)

