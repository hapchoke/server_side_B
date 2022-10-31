from django.db import models

class Text(models.Model):
    text = models.TextField(null=False, blank=False)
    def __str__(self):
        return self.text
