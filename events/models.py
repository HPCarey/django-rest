from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):

    """
    Event model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    image_filter_choices = [
        ('_1977', '1977'), ('brannan', 'Brannan'),
        ('earlybird', 'Earlybird'), ('hudson', 'Hudson'),
        ('inkwell', 'Inkwell'), ('lofi', 'Lo-Fi'),
        ('kelvin', 'Kelvin'), ('normal', 'Normal'),
        ('nashville', 'Nashville'), ('rise', 'Rise'),
        ('toaster', 'Toaster'), ('valencia', 'Valencia'),
        ('walden', 'Walden'), ('xpro2', 'X-pro II')
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    event_title = models.CharField(max_length=255)
    event_description = models.TextField(blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    country = models.CharField(max_length=50)
    location = models.CharField(max_length=255, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    difficulty = models.IntegerField()
    rating = models.IntegerField()
    image = models.ImageField(
        upload_to='images/', default='../default_post_cgvnmr', blank=True
    )
    image_filter = models.CharField(
        max_length=32, choices=image_filter_choices, default='normal'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.event_title} {self.date}'
