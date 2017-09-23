from django.db import models
from django.core.urlresolvers import reverse


class Filter(models.Model):
    filter_title = models.CharField(max_length=250)
    filter_description = models.CharField(max_length=500)
    filter_script = models.CharField(max_length=10000, default="")
    date_created = models.CharField(max_length=50)
    is_favorite = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('miner:detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.filter_title


class Result(models.Model):
    filter = models.ForeignKey(Filter, on_delete=models.CASCADE)
    result_title = models.CharField(max_length=250)
    result_url = models.CharField(max_length=250)
    result_image_url = models.CharField(max_length=250)
    date_found = models.CharField(max_length=50)
    time_left = models.CharField(max_length=20)
    price = models.CharField(max_length=15)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.result_title
