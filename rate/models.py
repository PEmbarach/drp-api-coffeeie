from django.db import models
from django.contrib.auth.models import User


class Rate(models.Model):
    """
    Rate model, related to 'owner', i.e. a User instance.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.TextField(max_length=50, blank=True)

    class Meta:
        ordering = ['rate']

    def __str__(self):
        return f'{self.id} {self.rate}'
