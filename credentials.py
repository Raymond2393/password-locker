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
