class User:
    '''
    class that generates new instance of user
    '''
    user_list = [] # Empty user list

    def  __init__(self,login_name, password):
    '''
    __init__ method that help us define properties for our objects

    Args:
        login_name: New user login_name.
        password: New user password.
    '''


        self.login_name =login_name
        self.password =password
    def save_user(self):
        '''
        method to save new user_list
        '''
        User.user_list.append(self)
