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
        y = self.user + ' - ' + str(self.day) + '.' + x + '.' + str(self.year) + ', ' + str(self.hour_start) + ':' + str(self.minute_start) + '-' + str(self.hour_stop) + ':' + str(self.minute_stop)
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
            y = 'Blokada czasu: ' + str(self.day) + '.' + x + '.' + str(self.year) + ', ' + str(self.hour_start) + ':' + str(self.minute_start) + '-' + str(self.hour_stop) + ':' + str(self.minute_stop)
        return y
