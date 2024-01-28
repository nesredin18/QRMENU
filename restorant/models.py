from django.db import models

from helpers.models import CommenModel
from users.models import User


# Create your models here.
class Restaurant(CommenModel):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='restaurants', null=True, blank=True)
    name = models.CharField(max_length=100)
    address = models.TextField(blank=True)
    contact_info = models.CharField(max_length=100, blank=True)
    logo_url = models.URLField(blank=True)


    def __str__(self):
        return self.name
    
class QRCode(CommenModel):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='qrcodes')
    url = models.URLField()
    generated_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.url