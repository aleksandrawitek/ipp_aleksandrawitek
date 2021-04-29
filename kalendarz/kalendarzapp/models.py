from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Meeting(models.Model):
    day = models.IntegerField(validators =[MinValueValidator(1), MaxValueValidator(31)], null = True)
    month = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(12)],null = True)
    year = models.IntegerField(validators = [MinValueValidator(2021)],null = True)
    user = models.CharField(max_length=50, null = True)
    hour_start = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(24)],null = True)
    hour_stop = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(24)],null = True)
    minute_start = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(60)],null = True)
    minute_stop = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(60)],null = True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        if (self.month < 10):
            x = '0'+str(self.month)
        else:
            x = str(self.month)
        if (self.day < 10):
            d = '0'+str(self.day)
        else:
            d = str(self.day)
        if (self.hour_start < 10):
            hs = '0'+str(self.hour_start)
        else:
            hs = str(self.hour_start)
        if (self.hour_stop < 10):
            hst = '0'+str(self.hour_stop)
        else:
            hst = str(self.hour_stop)
        if (self.minute_start < 10):
            ms = '0'+str(self.minute_start)
        elif (self.minute_start == 0):
            ms = '00'
        else:
            ms = str(self.minute_start)
        if (self.minute_stop < 10):
            mst = '0'+str(self.minute_stop)
        elif (self.minute_stop == 0):
            mst = '00'
        else:
            mst = str(self.minute_stop)
        
        y = self.user + ' - ' + d + '.' + x + '.' + str(self.year) + ', ' + hs + ':' + ms + '-' + hst + ':' + mst
        return y

class Historie(models.Model):
    user = models.CharField(max_length=50, null = True)
    history = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user

class Block(models.Model):
    day = models.IntegerField(validators =[MinValueValidator(1), MaxValueValidator(31)], null = True)
    month = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(12)],null = True)
    year = models.IntegerField(validators = [MinValueValidator(2021)],null = True)
    hour_start = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(24)],null = True)
    hour_stop = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(24)],null = True)
    minute_start = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(60)],null = True)
    minute_stop = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(60)],null = True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        if (self.month < 10):
            x = '0'+str(self.month)
        else:
            x = str(self.month)
        if (self.day < 10):
            d = '0'+str(self.day)
        else:
            d = str(self.day)
        if (self.hour_start < 10):
            hs = '0'+str(self.hour_start)
        else:
            hs = str(self.hour_start)
        if (self.hour_stop < 10):
            hst = '0'+str(self.hour_stop)
        else:
            hst = str(self.hour_stop)
        if (self.minute_start < 10):
            ms = '0'+str(self.minute_start)
        elif (self.minute_start == 0):
            ms = '00'
        else:
            ms = str(self.minute_start)
        if (self.minute_stop < 10):
            mst = '0'+str(self.minute_stop)
        elif (self.minute_stop == 0):
            mst = '00'
        else:
            mst = str(self.minute_stop)
        y = d + '.' + x + '.' + str(self.year) + ', ' + hs + ':' + ms + '-' + hst + ':' + mst
        return y
