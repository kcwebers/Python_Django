from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
from datetime import *

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def reg_validator(self, postData):
        errors = {} 
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters long"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters long"
        if not EMAIL_REGEX.match(postData['email']): # does email match email format?
            errors['email'] = "Please enter valid email address"
        if EMAIL_REGEX.match(postData['email']):
            for user in User.objects.all():
                if postData['email'] == user.email:
                    errors['email_made'] = "Email already exists in our database! Please log in"

        if len(postData['birthday']) < 10:
            errors['birthday'] = "Please enter your birthday"
        elif len(postData['birthday']) == 10:
            input_date = datetime.strptime(postData['birthday'], '%Y-%m-%d')
            age = datetime.now().year - input_date.year
            if datetime.now().month < input_date.month or (datetime.now().month == input_date.month and datetime.now().day < input_date.day):
                age -= 1
            if age < 13:
                errors['too_young'] = "You must be at least 13 years old to register"
        
        
        if len(postData['password']) < 8 or len(postData['password']) > 15:
            errors['password'] = "Password must be between 8 and 15 characters in length"
        if postData['password'] != postData['conf_pass']:
            errors['conf_pass'] = "Passwords do not match"

        return errors

# login validations

    def log_validator(self, postData):
        errors = {}
        user_info = User.objects.filter(email = postData['email_input'])
        if len(postData['email_input']) < 1:
            errors['not_email'] = "Please input valid email"
        elif len(user_info) < 1:
            errors['not_email'] = "Email not found! Please register for an account before logging in"

        if not postData['password_input']:
            errors['wrong_pass'] = "Please input a valid password"
        elif postData['password_input']: # if password has been inputted
            for user in User.objects.filter(email = postData['email_input']): # pulls user with the input email
                if not bcrypt.checkpw(postData['password_input'].encode(), user.password.encode()): # compare the pulled users password with the input password, if not matching then ...
                    errors['wrong_pass'] = "Password does not match our records! Please try again"
        return errors

    def not_logged(self, postData):
        errors = {}
        errors['no'] = "Please provide your login info!"
        return errors

    def success_login_validation(self, postData):
        errors = {}
        errors['success'] = "You have successfully registered!"
        return errors

    def success_reg_validation(self, postData):
        errors = {}
        errors['success'] = "You have successfully logged in!"
        return errors
    
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birthday = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

