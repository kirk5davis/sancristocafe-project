from django.db import models
from django.core.validators import FileExtensionValidator
from io import BytesIO
from PIL import Image as Img
from django.core.files.uploadedfile import InMemoryUploadedFile

# blog model
class Blog(models.Model):
	image = models.ImageField(upload_to='images/')
	title = models.CharField(max_length=100)
	summary = models.CharField(max_length=500)
	content = models.TextField()
	created_on = models.DateTimeField(blank=False, help_text="This will sort the new posts, the newest one will be featured")

	def save(self, *args, **kwargs):
		if self.image:
			img = Img.open(BytesIO(self.image.read()))
			if img.mode != 'RGB':
				img = img.convert('RGB')
			new_width = 800
			img.thumbnail((new_width, new_width * self.image.height / self.image.width), Img.ANTIALIAS)
			output = BytesIO()
			img.save(output, format='JPEG', quality=70)
			output.seek(0)
			self.image= InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.image.name.split('.')[0], 'image/jpeg', output.write, None)
		super(Blog, self).save(*args, **kwargs)

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