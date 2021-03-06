#!/usr/bin/env python3.6
import getpass
from user import User
from credentials import Credentials


def create_account(username, password):
    '''
    Function to create new account
    '''
    new_user = User(username, password)
    return new_user


def save_new_user(user):
    '''
    Function to save a user
    '''
    user.save_user()


def account_login(login):
    '''
    Function to login
    '''
    return User.user_login(login)


def create_credentials(account, username, email, password):
    '''
    Function to create new credentials
    '''
    new_credentials = Credentials(account, username, email, password)
    return new_credentials


def save_user_credentials(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()


def del_credentials(credentials):
    '''
    Function to delete credentials from list
    '''
    credentials.delete_credentials()


def find_credentials(name):
    '''
    Function that finds a credentials by account name and return details
    '''
    return Credentials.find_by_account_name(name)


def copy_username(name):
    return Credentials.copy_username(name)


def check_credentials_exist(name):
    '''
    Function to check if a credentials exists
    '''
    return Credentials.credentials_exist(name)


def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()


def generate_password(password_length):
    return Credentials.generate_password(password_length)


def main():
    print("Welcome to password locker")
    while True:
        print('''
              ca - create account
              lg - login
              esc - Escape''')
        short_code = input().lower()
        print("_" * 20)
        if short_code == "ca":
            print("Create Acount")
            print("Enter your user name of choice")
            print("_" * 20)
            username = input()
            print("Choose a password")
            print("_" * 20)
            password = getpass.getpass()
            save_new_user(create_account(username, password))
            print(f"""Your user details - Username : {username} Password : {password}""")
            print("")
            print(f"Hi {username} What would you like to do?")
            print("")

            while True:
                print("Use these short codes: cc - create new credentials, dc - display credentials, gp- generate a password, fc - find a credentials, exl - exit credentials list")
                short_code = input().lower()

                if short_code == 'cc':
                        print("New credentials")
                        print("-"*10)

                        print('')

                        print("Account name ...")
                        a_name = input()

                        print('')

                        print("User name ...")
                        u_name = input()

                        print('')

                        print("Email address ...")
                        email = input()

                        print('')

                        print("Account password")
                        acc_password = input()

                        save_user_credentials(create_credentials(a_name, u_name, email, acc_password))
                        print('')

                        print(f"New credential account : {a_name}, User name : {u_name}")
                        print('')
                elif short_code == 'dc':
                        if display_credentials():
                            print("This is a list of all the credentials")
                            print('')
                            for Credentials in display_credentials():
                                print(f"Account : {Credentials.account_name}, User name : {Credentials.user_name} E-mail address : {Credentials.email} Password : {Credentials.password}")

                                print('')
                        else:
                            print('')
                            print("I'm sorry, you seem not to have saved any credentials")
                            print('')
                elif short_code == 'fc':
                        print("Enter the Account you want")
                        search_name = input()
                        if check_credentials_exist(search_name):
                                search_name = find_credentials(search_name)
                                print('')
                                print(f"{search_name.user_name} {search_name.email}")
                                print('-'*20)

                                print('')

                                print(f"Account ... {search_name.account_name}")
                                print(f"Password ... {search_name.password}")
                                print('')

                        else:
                                print('')
                                print("Credentials do not exist")
                                print('')
                elif short_code == "cp":
                        search_name = input()
                        if copy_username(search_name):
                            search_name = find_credentials(search_name)
                            print(f"{search_name.user_name}")

                elif short_code == "gp":
                        print('')
                        print('How long would you like your password to be?')
                        password_length = int(input())
                        password = generate_password(password_length)
                        print(f"Your password is : {password}")
                elif short_code == "exl":
                        print('')
                        print("Goodbye ...")
                        break
                else:
                    print("Please input a valid short code")

        elif short_code == "lg":
            print("Log in")
            print("Enter User Name")
            print("_" * 20)
            username = input()
            print("Enter password")
            print("_" * 20)
            password = getpass.getpass()

            print(f"Hi {username} What would you like to do?")
            print("")
            while True:
                print("Use these short codes: cc - create new credentials, dc - display credentials, gp - generate password, fc - find a credentials, exl - exit credentials list")
                short_code = input().lower()

                if short_code == 'cc':
                        print("New credentials")
                        print("-"*10)

                        print('')

                        print("Account name ...")
                        a_name = input()

                        print('')

                        print("User name ...")
                        u_name = input()

                        print('')

                        print("Email address ...")
                        email = input()

                        print('')

                        print("Account password")
                        acc_password = input()

                        save_user_credentials(create_credentials(a_name, u_name, email, acc_password))
                        print('')

                        print(f"New credential account : {a_name}, User name : {u_name}")
                        print('')
                elif short_code == 'dc':
                        if display_credentials():
                            print("This is a list of all the credentials")
                            print('')
                            for Credentials in display_credentials():
                                print(f"Account : {Credentials.account_name}, User name : {Credentials.user_name} E-mail address : {Credentials.email} Password : {Credentials.password}")

                                print('')
                        else:
                            print('')
                            print("I'm sorry, you seem not to have saved any credentials")
                            print('')
                elif short_code == 'fc':
                        print("Enter the Account you want")
                        search_name = input()
                        if check_credentials_exist(search_name):
                                search_name = find_credentials(search_name)
                                print('')
                                print(f"{search_name.user_name} {search_name.email}")
                                print('-'*20)

                                print('')

                                print(f"Account ... {search_name.account_name}")
                                print(f"Password ... {search_name.password}")
                                print('')

                        else:
                                print('')
                                print("Credentials do not exist")
                                print('')
                elif short_code == "cp":
                        search_name = input()
                        if copy_username(search_name):
                            search_name = find_credentials(search_name)
                            print(f"{search_name.user_name}")

                elif short_code == "gp":
                        print('')
                        print('How long would you like your password to be?')
                        password_length = int(input())
                        password = generate_password(password_length)
                        print(f"Your password is : {password}")

                elif short_code == "exl":
                        print('')
                        print("Goodbye ...")
                        break
                else:
                    print("Please input a valid short code")

        elif short_code == "esc":
            print('')
            print("Exiting")
            break
        else:
            print("I'm sorry, the short code does not seem to exist")


if __name__ == '__main__':
    main()
