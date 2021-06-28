from django.db import models

# Create your models here.
class Investment(models.Model):
    username = models.CharField(max_length=100)
    amount = models.IntegerField()
    investmentReturns = models.IntegerField()
    duration = models.IntegerField()
    def __str__(self):
        return self.username
   