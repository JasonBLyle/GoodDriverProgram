from django import forms
from .models import Driver

# create a custom form for the Driver Model
class UserRegistrationForm(forms.ModelForm):
	username = forms.CharField(label = 'Username')
	first_name = forms.CharField(label = 'First Name')
	last_name = forms.CharField(label = 'Last Name')
	email = forms.EmailField()
	phone_num = forms.CharField(label = 'Phone Number')
	address = forms.CharField(label = 'Address')
	password = forms.CharField(label = 'Password')
	password2 = forms.CharField(label = 'Password Verification')

	# overwrite the clean for password validation
	def clean(self):
		cleaned_data = self.cleaned_data
		password1 = cleaned_data.get('password')
		password2 = cleaned_data.get('password2')
		if password1 != password2:
			raise forms.ValidationError('Passwords Must Match')
		return cleaned_data

		# deliver the proper model to the database
	class Meta:
		model = Driver
		fields = ['username', 'first_name', 'last_name', 'phone_num', 'email', 'address', 'password']