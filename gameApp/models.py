from django.db import models


from datetime import date

class GameDetails(models.Model):
    name           = models.CharField(max_length=50, null=False, blank=False)
    url            = models.URLField(max_length=256)
    author         = models.CharField(max_length=50, null=False, blank=False)
    published_date = models.DateField()
    created_at     = models.DateTimeField(auto_now_add=True)
    modified_at     = models.DateTimeField(auto_now=True)

