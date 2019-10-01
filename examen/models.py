# Create your models here.
from django.db import models

# Create your models here.

class Users(models.Model):
    first_name = models.CharField(max_length=150, db_index=True)
    last_name = models.CharField(max_length=150)
    number_of_login = models.PositiveIntegerField()

    class Meta:
        ordering = ('first_name',)

    def __str__(self):
        return self.first_name
