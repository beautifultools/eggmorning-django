from django.db import models


class RankCategory(models.Model):
    cat_no = models.IntegerField('category number')
    cat_type = models.CharField('category type', max_length=8)
    cat_name = models.CharField('category name', max_length=32)
    cat_code = models.CharField('category code', max_length=16)

