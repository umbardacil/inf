from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    writer = models.CharField(max_length=128)
    text = models.TextField()
    inf_user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now=True)
