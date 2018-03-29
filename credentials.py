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
