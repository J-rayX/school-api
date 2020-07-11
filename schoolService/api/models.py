from django.db import models


# Let models be here
class Student(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	grade = models.CharField(max_length=255)
	age = models.IntegerField()

	def __str__(self):
		return self.first_name