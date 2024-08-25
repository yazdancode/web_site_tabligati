from django.core.exceptions import ValidationError
from django.core.validators import validate_email

class FullnameValidator:
	@staticmethod
	def validate(fullname):
		if len(fullname) != 128:
			raise ValidationError("طول نام و نام خانوادگی باید 128 کاراکتر باشد.")
		return fullname
	

class EmailValidator:
	@staticmethod
	def validate(email):
		try:
			validate_email(email)
		except ValidationError:
			raise ValidationError("ایمیل وارد شده معتبر نمی‌باشد.")
		return email
	
	
class Phone_Number:
	@staticmethod
	def validate(phone_number):
		if len(phone_number) != 11:
			raise ValidationError("طول تلفن همراه باید ۱۱ کاراکتر باشد")
		return phone_number
		