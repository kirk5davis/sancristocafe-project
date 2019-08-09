from django.db import models

# coffees that san cristobal offers
class Coffee(models.Model):

	image = models.ImageField(upload_to='images/', blank=False)
	coffee_name = models.CharField(max_length=100, blank=False)
	bag_tag = models.CharField(max_length=10, blank=False, help_text="Put the exact bag tag here, it creates button hyperlinks!")
	description = models.TextField(help_text="Write out exactly how you would like it to show on the coffee tile!")

	def __str__(self):
		return "Coffee - {}".format(self.coffee_name)


