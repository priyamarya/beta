from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

GENDER_CHOICES = (('Others','Others'), ('Male','Male'),('Female','Female'))

# Create your models here.

class Users(models.Model):
	u_name = models.OneToOneField(User,
		verbose_name = "User Name"
		)
	
	mob_no = models.PositiveIntegerField(
		null = False,
		blank = False
		)

	email_id = models.EmailField(
		null = False,
		blank = False
		)
	
	joining_date = models.DateTimeField(
		default = timezone.now)

	address = models.TextField(
		null = False,
		blank = False
		)

	password = models.CharField(
		max_length=20,
		null = False,
		blank = False
		)

	
	def __str__(self):
		return str(self.u_name)

	class Meta:
		verbose_name = "Users"
		verbose_name_plural = "Users"

class UserInfo(models.Model):
	user_link = models.OneToOneField(
		Users,
		verbose_name = "of user"
		)

	full_name = models.CharField(
		max_length = 250,
		null = True,
		blank = True
		)

	sex = models.CharField(
		max_length = 30,
		choices = GENDER_CHOICES
		)

	profile_pic = models.ImageField(
		upload_to= 'profile_pic',
		null = True,
		blank = True
		)

	class Meta:
		verbose_name = "Users Info"
		verbose_name_plural = "Users Info"

	def __str__(self):
		return self.full_name
			
	