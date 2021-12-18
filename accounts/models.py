from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	avatar = models.ImageField(upload_to='avatar/', default='avatar_1.png')
	featured = models.BooleanField(default=False)
	joined_date = models.DateTimeField(auto_now_add=True) 

	def __str__(self):
		return str(f"{self.user.username}")

