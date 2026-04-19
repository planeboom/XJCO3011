from django.db import models

class Beverage(models.Model):
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    preparation = models.CharField(max_length=100)
    calories = models.IntegerField()
    total_fat_g = models.FloatField(null=True, blank=True)
    sugar_g = models.IntegerField(null=True, blank=True)
    caffeine_mg = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.preparation}"
