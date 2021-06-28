from django.db import models


# Create your models here.
class Investment(models.Model):
    username = models.CharField(max_length=100)
    amount = models.IntegerField()
    investmentReturns = models.IntegerField(blank=True, null=True,editable=False, default=0)
    duration = models.IntegerField()

    def __str__(self):
        return self.username

    def calc_returns(self):
        return self.amount * self.duration * .3

    def save(self, *args, **kwargs):
        self.investmentReturns = self.calc_returns()
        super(Investment, self).save(*args, **kwargs)
