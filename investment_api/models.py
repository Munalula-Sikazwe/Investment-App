from django.db import models

# Create your models here.
class Investment(models.Model):
    user_name = models.CharField(max_length=100)
    amount = models.IntegerField()
    investment_returns = models.IntegerField()
    duration = models.IntegerField()
    def __str__(self):
        return self.user_name