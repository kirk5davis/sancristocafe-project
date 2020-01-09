# contact/forms.py
from django import forms
from captcha.fields import CaptchaField

from .models import ContactInfo

class ContactForm(forms.ModelForm):
# The dictionary is urlencoded and appended to the reCAPTCHA api url.
	are_you_a_human = CaptchaField()
	class Meta:
		model = ContactInfo
		fields = ['name', 'email', 'message']

	#validate = captcha_field.ReCaptchaField()