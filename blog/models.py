from django.db import models

# blog model
class Blog(models.Model):
	image = models.ImageField(upload_to='images/')
	title = models.CharField(max_length=100)
	summary = models.CharField(max_length=500)
	content = models.TextField()
	created_on = models.DateField(auto_now=True)

	def __str__(self):
		return "Blog - {}".format(self.title)

