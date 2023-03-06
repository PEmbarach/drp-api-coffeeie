from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


RATE_CHOICES = [
    (1, '1 - Very Poor'),
    (2, '2 - Poor'),
    (3, '3 - Fair'),
    (4, '4 - Good'),
    (5, '5 - Excellent'),
]


class Rate(models.Model):
    """
    Rate model, related to 'owner', i.e. a User instance.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)

    class Meta:
        ordering = ['rate']

    def __str__(self):
        return f'{self.id} {self.rate}'
