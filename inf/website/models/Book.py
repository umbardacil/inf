from django.contrib.auth.models import User
from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class Book(TranslatableModel):
    writer = models.CharField(max_length=128)
    inf_user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now=True)

    translations = TranslatedFields(
        text=models.TextField()
    )
