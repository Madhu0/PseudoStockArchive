from django.db import models
from django.utils import timezone


class Company(models.Model):

    symbol = models.CharField(max_length=6, unique=True, null=False)
    id = models.AutoField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100, null=False)
    marketCap = models.DecimalField(default=0, decimal_places=5, max_digits=25)
    sector = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ' (' + self.symbol + ')'


class TradingData(models.Model):

    timestamp = models.DateTimeField(null=False, default=timezone.now())
    open = models.FloatField(null=False)
    close = models.FloatField(null=False)
    low = models.FloatField(null=False)
    high = models.FloatField(null=False)
    volume = models.FloatField(null=False)
    company = models.ForeignKey(Company, related_name="company", on_delete=models.CASCADE)