from django.db import models

class Quote(models.Model):
    text = models.CharField(max_length=500)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.text