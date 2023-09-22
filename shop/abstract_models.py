from django.db import models


class Subscribable(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    data_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True