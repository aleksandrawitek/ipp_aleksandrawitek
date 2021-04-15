from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Meetings(models.Model):
    day = models.IntegerField(validators =[MinValueValidator(1), MaxValueValidator(31)], null = True)
    month = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(12)],null = True)
    year = models.IntegerField(validators = [MinValueValidator(2021)],null = True)
    user = models.CharField(max_length=50, null = True)
    hour_start = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(24)],null = True)
    hour_stop = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(24)],null = True)
    minute_start = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(60)],null = True)
    minute_stop = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(60)],null = True)
    comment = models.TextField(null = True)