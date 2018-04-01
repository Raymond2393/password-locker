#!/usr/bin/env python3.6
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
