from django.db import models
from django.contrib.auth.models import User


class Details(models.Model):
    location_filter_choices = [
        ('temple_bar', 'Temple Bar'),
        ('sandymount', 'Sandymount'),
        ('rathmines', 'Rathmines'),
        ('portobello', 'Portobello'),
        ('ballsbridge', 'Ballsbridge'),
        ('dublin_docklands', 'Dublin Docklands'),
        ('smithfield', 'Smithfield'),
        ('cabra', 'Cabra'),
        ('ashtown', 'Ashtown'),
        ('phibsborough', 'Phibsborough')
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    price = models.TextField(max_length=50, blank=True)
    location = models.TextField(max_length=255, blank=True)
    location_filter = models.CharField(
        max_length=32, choices=location_filter_choices, default='none'
    )

    # class Meta:
    #     ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
