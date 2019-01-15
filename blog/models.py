from django.db import models
from django.core.validators import FileExtensionValidator

# blog model
class Blog(models.Model):
	image = models.ImageField(upload_to='images/')
	title = models.CharField(max_length=100)
	summary = models.CharField(max_length=500)
	content = models.TextField()
	created_on = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "News - {}".format(self.title)

	class Meta:
		verbose_name = "News Post"

class Newsletter(models.Model):
	title = models.CharField(max_length=100)
	file = models.FileField(upload_to='newsletters/', validators=[FileExtensionValidator(allowed_extensions=['pdf'])], help_text="This will only accept PDF files!")
	uploaded_on = models.DateField(auto_now=True)
	vintage = models.DateField(help_text="When was this file created/intended for/relevant? Ex: 05/17/1989")
	brief_summary = models.CharField(max_length=1000)

	def __str__(self):
		return "Newletter - {}".format(self.title)

class ArchivedFile(models.Model):
	title = models.CharField(max_length=100)
	file = models.FileField(upload_to='archives/')
	uploaded_on = models.DateField(auto_now=True)
	vintage = models.DateField(help_text="When was this file created/intended for/relevant? Ex: 05/17/1989")
	brief_summary = models.CharField(max_length=1000)

	def __str__(self):
		return "Archive File - {}".format(self.title)