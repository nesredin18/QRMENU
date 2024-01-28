from django.db import models


class CommenModel(models.Model):
    # ...
    created_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
        ordering = ['-created_date']
    