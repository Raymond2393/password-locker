import unittest # Importing the unittest module
from credentials import Credentials
from user import User

class TestCredentials(unittest.TestCase):
    '''
    Test class  that defines test cases for our credentials class behaviours.
    Args:
        unittest.TestCase: Testcase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        set up method to before each test case.
        '''

        self.new_credentials = Credentials("Raymond", "Okwenda", "rokwenda090@gmail.com", "password")


    def tearDown(self):
        '''
        Method that does clean up after each test case has run
        '''
        Credentials.credentials_list = []


    def test_credentials_init(self):
        '''
        test case to test if the object is initializzed properly
        '''
        self.assertEqual(self.new_credentials.account_name, "Raymond")
        self.assertEqual(self.new_credentials.user_name, "Okwenda")
        self.assertEqual(self.new_credentials.email, "rokwenda090@gmail.com")
        self.assertEqual(self.new_credentials.password, "password")

    def test_save_credentials(self):
        '''
        Test case to test if the contact object is saved into the credentials
        list
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)



if __name__ == '__main__':
    unittest.main()
