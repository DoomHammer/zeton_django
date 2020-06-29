from django.db import models

class Point(models.Model):
    ORIGIN = (
        ('home', 'home'),
        ('school', 'school'),
    )
    origin = models.CharField(max_length=100, null=True, choices=ORIGIN)
    value = models.IntegerField()

    def __str__(self):
        return self.origin
