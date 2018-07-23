from django.db import models

# Create your models here.
class ContactInfo(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	message = models.TextField()
	created_on = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "ContactInfo - {}".format(self.name)
