import pyperclip #importing pyperclip for copying to clipboard
from user_class import User #importing user class 
import random #import random variable generator
import string  #import string constants

#Built by Joseph Adediji 
#Edit at your own risk! 

class Credential:
	'''
	Class to create  account credentials, generate new passwords and save user information
	'''

	credentials_list =[]
	user_credentials_list = []

	@classmethod
	def check_user(cls,first_name,password):
		'''
		Method that checks if the name and password entered exist in the users_list
		'''
		current_user = ''
		for user in User.users_list:
			if (user.first_name == first_name and user.password == password):
				current_user = user.first_name
		return current_user

	def __init__(self,user_name,site_name,account_name,password):
		'''
		Method to define the properties for each user object.
		'''

		self.user_name = user_name
		self.site_name = site_name
		self.account_name = account_name
		self.password = password

	def save_credentials(self):
		'''
		Function to save a newly created user credentials
		'''

		Credential.credentials_list.append(self)
