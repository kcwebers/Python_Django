from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
from datetime import *

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# email must be formatted properly
PASS_REGEX = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,15}$')
# Password matching expression. Password must be between 8 and 15 characters, must include at least one upper case letter, one lower case letter, and one numeric digit.
FNAME_REGEX = re.compile(r'^[A-Z][a-zA-Z]*.{1,45}$')
# First name only letters, min 3 max 45
LNAME_REGEX = re.compile(r'^[A-Z][a-zA-Z]*.{1,45}$')
# last name only letters, min 3 max 45

class UserManager(models.Manager):
    def reg_validator(self, postData):
        errors = {} 
    # ------ Name -----
        if not FNAME_REGEX.match(postData['first_name']):
            errors['first_name'] = "Please enter a valid first name that contains at least 2 characters"
        if not LNAME_REGEX.match(postData['last_name']):
            errors['last_name'] = "Please enter a valid last name that contains at least 2 characters"
    # ------ Email ------
        if not EMAIL_REGEX.match(postData['email']): # does email match email format?
            errors['email'] = "Please enter valid email address"
        if EMAIL_REGEX.match(postData['email']):
            for user in User.objects.all():
                if postData['email'] == user.email:
                    errors['email_made'] = "Email already exists in our database! Please log in"
    # ------ Password -------
        if not PASS_REGEX.match(postData['password']):
            errors['password'] = "Invalid password! Password must be between 8 and 15 characters, must include at least one upper case letter, one lower case letter, and one numeric digit"
        if postData['password'] != postData['conf_pass']:
            errors['conf_pass'] = "Passwords do not match"
        return errors
    # ------- login validations
    def log_validator(self, postData):
        errors = {}
        user_info = User.objects.filter(email = postData['email_input'])
        if len(user_info) < 1:
            errors['not_email'] = "Email not found! Please register for an account before logging in"
    # ------- Password
        if postData['password_input']: # if password has been inputted
            for user in User.objects.filter(email = postData['email_input']): # pulls user with the input email
                if not bcrypt.checkpw(postData['password_input'].encode(), user.password.encode()): # compare the pulled users password with the input password, if not matching then ...
                    errors['wrong_pass'] = "Password does not match our records! Please try again"
        return errors
    # ------ if not logged in
    def not_logged(self, postData):
        errors = {}
        errors['no'] = "Please provide your login info!"
        return errors
    # ------ wish validator
    def wish_validator(self, postData):
        errors = {}
        if len(postData['wish']) < 3:
            errors['wish'] = "Wish must be at least 3 characters long!"
        if len(postData['desc']) < 3:
            errors['desc'] = "Must provide a breif description of you wish! (must be at least 3 characters long)"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    # wishes_made 
    # wishes_granted 
    # likes
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Wish(models.Model):
    wish = models.CharField(max_length=255)
    desc = models.TextField()
    wished_by = models.ForeignKey(User, related_name="wishes_made")
    granted_by = models.ManyToManyField(User, related_name="wish_granted")
    liked_by = models.ManyToManyField(User, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

