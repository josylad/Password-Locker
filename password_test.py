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

    def test__init__(self):
        '''
		Test to check if the initialization/creation of credential instances is properly done
		'''
        self.assertEqual(self.new_credential.username,'Joseph')
        self.assertEqual(self.new_credential.site_name,'FB.com')
        self.assertEqual(self.new_credential.account_name,'Josylad')
        self.assertEqual(self.new_credential.password,'123456')
        
    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credential object is saved into
         the credential list
        '''
        self.new_credential.save_credentials() # saving the new credential
        
        self.assertEqual(len(Credential.credentials_list),1)
        
    def test_save_multiple_credentials(self):
        '''
        test_save_multiple_credential to check if we can save multiple credentials
        objects to our credentials_list
        '''
        self.new_credential.save_credentials()
        test_credential = Credential("Joe","Medium","Josylad","112233") # new credential
        test_credential.save_credentials()
        
        self.assertEqual(len(Credential.credentials_list),2)
  
        
if __name__ == '__main__':
    unittest.main()