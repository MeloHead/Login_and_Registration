from django.db import models
import re

class LoginManager(models.Manager):

    def validateRegistration(self,postData):
        errors={}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # if not EMAIL_REGEX.match(postData['user_registered_email_address']):
            # errors['email'] = "Invalid email address!"
            # return errors
        check_email = User.objects.filter(email_address=postData['user_registered_email_address'])
        print("------------>",check_email)

        #first name validation
        if len(postData['user_first_name']) == 0:
            errors['user_first_name'] = 'must enter first name'
        if len(postData['user_first_name']) <= 2:
            errors['user_first_name'] = 'first name must have 2 letters'

        #last name validation
        if len(postData['user_last_name']) == 0:
            errors['user_last_name'] = 'must enter last name'
        if len(postData['user_last_name']) <= 2:
            errors['user_last_name'] = 'last name must have 2 letters'

        #email address validation
        if len(postData['user_registered_email_address']) == 0:
            errors['user_registered_email_address'] = 'must enter email'
        
        if (len(check_email) > 0):
            print("22222222222222222222 THIS IS THE CHECK EMAIL IF STATEMENT!")
            errors['user_registered_email_address'] = "email already exists"
        if not EMAIL_REGEX.match(postData['user_registered_email_address']):
            errors['user_registered_email_address'] = 'need valid email'

        #password validation
        if len(postData['user_registered_password']) == 0:
            errors['user_registered_password'] = 'must enter password'
        if len(postData['user_registered_password']) < 8:
            errors['user_registered_password'] = 'passsword must be at least 8 characters'

        #confirm password validation
        if len(postData['user_registered_confirm_password']) == 0:
            errors['user_registered_confirm_password'] = 'must confirm password'
        
        return errors

    def validateLogin(self,postData):
        errors={}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # get the user from database and compare list
        # userList = User.objects.filter(email_address=request.POST['user_login_email_address'])
        
        #login
        if len(postData['user_login_email_address']) == 0:
            errors['user_login_email_address'] = 'must enter email'
        if not EMAIL_REGEX.match(postData['user_login_email_address']):
            print('login_email does not match')
            errors['user_login_email_address'] = 'need valid email'
    
        # not sure what im doing here

        #password
        if len(postData['user_login_password']) == 0:
            errors['user_login_password'] = 'must enter password'
        
        return errors

# Create your models here.
class User(models.Model):
    first_name = models.TextField(max_length=255)
    last_name = models.TextField(max_length=255)
    email_address = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    objects = LoginManager()