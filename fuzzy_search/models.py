from django.db import models


class WordData(models.Model):
    word_id = models.IntegerField()
    name = models.CharField(max_length=50)