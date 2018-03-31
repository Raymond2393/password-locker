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

    def test_save_multiple_credentials(self):
        self.new_credentials.save_credentials()
        test_credentials = Credentials("ovo", "Y-Mo", "Y_Mo@gmail", "set")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 2)

    def test_delete_credentials(self):
        '''
        Test if we can remove credentials from our credentials contact_list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("ovo", "Y_Mo", "Y_Mo@gmail", "set")
        test_credentials.save_credentials()
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)







if __name__ == '__main__':
    unittest.main()
