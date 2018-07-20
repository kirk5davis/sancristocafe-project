from django.db import models

# coffees that san cristobal offers
class Coffee(models.Model):

	YES = 'yes'
	NO = 'no'
	OTHER = 'other'
	YES_NO_CHOICES = [(YES, 'Yes'), (NO, 'No'), (OTHER, 'Call for more info')]

	SEA = "SEA"
	SF = "SF"
	NJ = "NJ"
	AVAILABILITY_CHOICES = [(SEA, "Seattle"), (SF, "San Francisco"), (NJ, "New Jersey")]

	image = models.ImageField(upload_to='images/', blank=True)
	coffee_name = models.CharField(max_length=100)
	origin = models.CharField(max_length=200)
	description = models.TextField()
	origin_info = models.CharField(choices=YES_NO_CHOICES, default=YES, max_length=5)
	availability = models.CharField(max_length=300, help_text="Where is this coffee available? (SEA, SF, NJ)")

	def __str__(self):
		return "Coffee - {}".format(self.coffee_name)


