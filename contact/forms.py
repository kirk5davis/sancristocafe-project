# contact/forms.py
from django import forms
from django.core.exceptions import ValidationError
# from captcha.fields import CaptchaField
from django.conf import settings
import requests

from .models import ContactInfo

def validate_captcha(value):
	data = {'secret': settings.HCAPTCHA_SECRET_KEY, 'response':value}
	response = requests.post('https://hcaptcha.com/siteverify', data)
	if not 'success' in response.json() or not response.json()['success']:
		raise ValidationError('hcaptcha failed')

class ContactForm(forms.ModelForm):
# The dictionary is urlencoded and appended to the reCAPTCHA api url.
	# are_you_a_human = CaptchaField()
	captcha = forms.CharField(max_length=10000, validators=[validate_captcha])

	class Meta:
		model = ContactInfo
		fields = ['name', 'email', 'message']

	#validate = captcha_field.ReCaptchaField()