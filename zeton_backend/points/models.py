from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Point(models.Model):
    ORIGIN = (
        ('home', 'home'),
        ('school', 'school'),
    )
    origin = models.CharField(max_length=100, null=True, choices=ORIGIN)
    value = models.IntegerField(default=0,
                                validators=[MaxValueValidator(500),
                                            MinValueValidator(-500)])

    def __str__(self):
        return self.origin
