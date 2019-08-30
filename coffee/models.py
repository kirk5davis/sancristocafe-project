from django.db import models
from django.core.validators import FileExtensionValidator
from io import BytesIO
from PIL import Image as Img
from django.core.files.uploadedfile import InMemoryUploadedFile

# coffees that san cristobal offers
class Coffee(models.Model):

	image = models.ImageField(upload_to='images/', blank=False)
	coffee_name = models.CharField(max_length=100, blank=False)
	bag_tag = models.CharField(max_length=10, blank=False, help_text="Put the exact bag tag here, it creates button hyperlinks!")
	description = models.TextField(help_text="Write out exactly how you would like it to show on the coffee tile!")

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
		super(Coffee, self).save(*args, **kwargs)

	def __str__(self):
		return "Coffee - {}".format(self.coffee_name)

class OfferingsList(models.Model):
	date_current = models.DateField(blank=False, help_text="This date will show on the web site as the 'current as of' date and the newest file will be linked to on the website.")
	pdf_file = models.FileField(upload_to='offering_lists/', validators=[FileExtensionValidator(allowed_extensions=['pdf'])], help_text="This will only accept PDF files!")

	def __str__(self):
		return "Offering List - {}".format(self.date_current)
