#!/usr/bin/env python3.6
import pyperclip  #importing pyperclip for copying to clipboard
from user_class import User  #imporing user class
from credential_class import Credential #importing credential class

#Built by Joseph Adediji  
#Edit at your own risk! 


def create_user(fname, lname, password):
	'''
	Function to create a new user account
	'''
	new_user = User(fname, lname, password)
	return new_user

