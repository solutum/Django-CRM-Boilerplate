from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass


class AppSettings(models.Model):
	app_name = models.CharField(max_length=50, blank=False)
	name = models.CharField(max_length=50, blank=False)
	value = models.CharField(max_length=250, blank=True)

	def __str__(self):
		return f'{self.app_name}: {self.name} = {self.value}'


