class credentials:
    '''
    Class that generates new instance of credentials
    '''

    credentials_list = [] # Empty credentials list
    user_pass_list = [] # Empty password list

    def __init__(self, account_name, user_name, password, email):
        '''
        __init__ method that helps us define the properties for our object credentials
        '''

        self.account_name = account_name
        self.user_name = user_name
        self.password = password
        self.email = email


    def save_credentials(self):
        '''
        save_credentials method save credentials object into credentials_list
        '''
        Credentials.credentials_list.append(self)


     def delete_credentials(self):
        '''
        delete_contact method deletes an object from the credentials_list
        '''
        Credentials.credentials_list.remove(self)

    @classmethod
    def display_credentials(cls):

            '''
            method that returns the entire contact_list
            '''

            return cls.credentials_list


    @classmethod
    def find_by_account_name(cls, name):
        '''
        Method that takes in an account name and returns credentials that match that number
        '''
        for credentials in cls.credentials_list:
            if credentials.account_name == name:
                return credentials
    
    # @classmethod
    # def copy_username(cls, account):
    #     credentials_found = Credentials.find_by_account_name(account)
    #     pyperclip.copy(credentials_found.account_name)
    #
    # @classmethod
    # def generate_password(cls, pasword_length):
    #     choice_string = "zxcjklqwe!@#123"
    #     password_generate = ".join(random.sample(choice_string, int(pasword_length)))"
    #     password = password_generate
    #     return password
    #
    #
    # @classmethod
    # def credentials_exist(cls, name):
    #     '''
    #     Method that check if the credentials are already on the contact_list
    #     and return true and false if it exists or not
    #     '''
    #
    #     for credentials in cls.credentials_list:
    #         if credentials.account_name == name:
    #             return True
    #
    #     return False
