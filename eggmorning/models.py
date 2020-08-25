from django.db import models


# Create your models here.
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


class Hotel(models.Model):
    hotel_no = models.IntegerField()
    addr = models.CharField(max_length=256)


class HotelProp(models.Model):
    hotel_no = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    prop_name = models.CharField(max_length=64)
    prop_value = models.IntegerField()


class RankCat(models.Model):
    cat_no = models.IntegerField('category number')
    cat_name = models.CharField('category name', max_length=32)
    cat_code = models.CharField('category code', max_length=16)


class HotelRank(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    category = models.ForeignKey(RankCat, on_delete=models.CASCADE)
    rank = models.FloatField()


class User(models.Model):
    user_id = models.CharField(max_length=128, default='')
    password = models.CharField(max_length=128, default='')
    name = models.CharField(max_length=64, default='')
    phone = models.CharField(max_length=32, default='')
    birth = models.DateField()
    gender = models.CharField(max_length=1, default='')
    mod_data = models.DateField(auto_now=True)
    reg_date = models.DateField(auto_now_add=True)


