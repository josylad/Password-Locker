import unittest
import pyperclip  #importing pyperclip for copying to clipboard
from user_class import User  #imporing user class
from credential_class import Credential #importing credential class

#Built by Joseph Adediji 

class TestContact(unittest.TestCase):

    '''
    Test class that defines the test cases for the the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    
    def setUp(self):
        '''
        Setup method to run before each test case 
        ''' 
        self.new_user = User('Joseph', 'Adediji', '123456')
    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Joseph")
        self.assertEqual(self.new_user.last_name,"Adediji")
        self.assertEqual(self.new_user.password,"123456")
        
    def test_save_user(self):
        '''
		Test to check if the new users info is saved into the users list
		'''
        self.new_user.save_user()
        self.assertEqual(len(User.users_list),1)
        
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.users_list = []

        
class TestCredentials(unittest.TestCase):
    '''
    Test class that defines the test cases for the the credential class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
		Setup method to run before each test case
		'''
        self.new_credential = Credential('Joseph','FB.com','Josylad','123456')
