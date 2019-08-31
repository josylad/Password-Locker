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


def save_user(user):
	'''
	Function to save a new user account
	'''
	User.save_user(user)


def verify_user(first_name, password):
	'''
	Function that verifies the existance of the user before creating credentials
	'''
	checking_user = Credential.check_user(first_name, password)
	return checking_user

