"""
Diploma in Web Application Development: Backend (Data Centric) Development
Milestone Project 3 :   Custom made decorators for validating log-in
File name:  decorators.py
Created:    April, 2023
Author:     Janet Dornan
Credit:     Flask
Source:     https://flask.palletsprojects.com/en/2.2.x/
"""

from functools import wraps
from flask import (Flask, flash, redirect, render_template, session, url_for)


def login_required_admin(func):
    '''
    This defines the decorator to wrap any function 'func' that follows it.
    In this case, the decorator will wrap any following function
    which requires 'admin' access.
    e.g. functions get_categories() and add_category().
    For more info see:
    https://flask.palletsprojects.com/en/2.2.x/patterns/viewdecorators/
    Tutorial:
    https://pythonprogramming.net/decorator-wrappers-flask-tutorial-login-required/

    :param func:   function 'func' to be wrapped
    :return:    the decorated (or wrapped) function
    '''
    @wraps(func)
    def decorated_function(*args, **kwargs):
        '''
        Defines the wrap that is actually happening, which
        asks if the user is logged in as 'admin'.

        :param args:    multiple arguments or
        :param kwargs:  keyword arguments
        :return:    wrapped function with its args/kwargs if 'admin' logged in,
                    or login route
        '''
        if "user" in session:
            if session["user"] == "admin":
                return func(*args, **kwargs)
            return render_template("404.html"), 404
        flash("Access Denied")
        return redirect(url_for('login'))

    return decorated_function


def login_required_user(func):
    '''
    Defines the decorator will wrap any following function
    which requires current 'user' access.
    e.g. functions add_plant(), profile(username), logout()

    :param func:    function 'func' to be wrapped
    :return:        the decorated (or wrapped) function
    '''
    @wraps(func)
    def decorated_function(*args, **kwargs):
        '''
        Defines the wrap that is actually happening, which
        asks if the user is logged in as current session 'user'.

        :param args: multiple arguments or
        :param kwargs: keyword arguments
        :return:    wrapped function with its args/kwargs if 'user' logged in,
                    or login route
        '''

        if "user" in session:
            return func(*args, **kwargs)
        flash("Access Denied")
        return redirect(url_for('login'))

    return decorated_function
