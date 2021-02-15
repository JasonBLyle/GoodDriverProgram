from django import forms
from .models import Driver, Sponsor,Admin

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

	# overwrite the clean for username and password validation
	def clean(self):
		cleaned_data = self.cleaned_data
		try:
			result = Driver.objects.get(username = cleaned_data.get('username'))
			if result != None:
				raise forms.ValidationError('A user already exists with that username')
		except Driver.DoesNotExist:
			pass
		password1 = cleaned_data.get('password')
		password2 = cleaned_data.get('password2')
		if password1 != password2:
			raise forms.ValidationError('Passwords Must Match')
		return cleaned_data

		# deliver the proper model to the database
	class Meta:
		model = Driver
		fields = ['username', 'first_name', 'last_name', 'phone_num', 'email', 'address', 'password']

# Driver Registration Form
class SponsorRegistrationForm(forms.ModelForm):
		username = forms.CharField(label = 'Username')
		first_name = forms.CharField(label = 'First Name')
		last_name = forms.CharField(label = 'Last Name')
		email = forms.EmailField()
		sponsor_company = forms.CharField(label = 'Company Name')
		password = forms.CharField(label = 'Password')
		password2 = forms.CharField(label = 'Password Verification')

		# overwrite the clean for username and password validation
		def clean(self):
			cleaned_data = self.cleaned_data
			try:
				result = Sponsor.objects.get(username = cleaned_data.get('username'))
				if result != None:
					raise forms.ValidationError('A user already exists with that username')
			except Sponsor.DoesNotExist:
				pass
			password1 = cleaned_data.get('password')
			password2 = cleaned_data.get('password2')
			if password1 != password2:
				raise forms.ValidationError('Passwords Must Match')
			return cleaned_data

			# deliver the proper model to the database
		class Meta:
			model = Sponsor
			fields = ['username', 'first_name', 'last_name', 'email', 'sponsor_company', 'password']

class AdminRegistrationForm(forms.ModelForm):
	username = forms.CharField(label = 'Username')
	first_name = forms.CharField(label = 'First Name')
	last_name = forms.CharField(label = 'Last Name')
	email = forms.EmailField()
	password = forms.CharField(label = 'Password')
	password2 = forms.CharField(label = 'Password Verification')

	# overwrite the clean for username and password validation
	def clean(self):
		cleaned_data = self.cleaned_data
		try:
			result = Admin.objects.get(username = cleaned_data.get('username'))
			if result != None:
				raise forms.ValidationError('A user already exists with that username')
		except Admin.DoesNotExist:
			pass
		password1 = cleaned_data.get('password')
		password2 = cleaned_data.get('password2')
		if password1 != password2:
			raise forms.ValidationError('Passwords Must Match')
		return cleaned_data

		# deliver the proper model to the database
	class Meta:
		model = Admin
		fields = ['username', 'first_name', 'last_name',  'email', 'password']