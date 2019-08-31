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
	Function that verifies the existence of the user before creating credentials
	'''
	checking_user = Credential.check_user(first_name, password)
	return checking_user


def generate_password():
	'''
	Function to generate a password automatically
	'''
	password_gen = Credential.generate_password()
	return password_gen


def create_credential(user_name, site_name, account_name, password):
	'''
	Function to create a new credential
	'''
	new_credential = Credential(user_name, site_name, account_name, password)
	return new_credential


def save_credential(credential):
	'''
	Function to save a newly created credential
	'''
	Credential.save_credentials(credential)


def display_credentials(user_name):
	'''
	Function to display credentials saved by a user
	'''
	return Credential.display_credentials(user_name)

