from django.db import models
from django.contrib.auth.models import User


class Details(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """

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
        ('phibsborough', 'Phibsboorough')
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    price = models.TextField(max_length=50, blank=True)
    location = models.TextField(max_length=255, blank=True)
    location_filter = models.CharField(
        max_length=32, choices=location_filter_choices, default='normal'
    )

    # class Meta:
    #     ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
