from __future__ import unicode_literals
from django.db import models
from validate_email import validate_email
#Our new manager!
#No methods in our new manager should ever catch the whole request object with a
#parameter!!! (just parts, like request.POST)

class UserManager(models.Manager):
    def login(self, email):
        is_valid = validate_email(email)

        if len(email) > 8:
            if len(email) < 26:
                if is_valid:
                    return True

        # if len(email) > 8:
        #     return ("This is a valid email according to min length(8)")
        # if len(email) < 26:
        #     return ("This is a valid email according to max length(26)")
        # if is_valid:
        #     return ("This is a valid email")
        return False
        # if request.method == "POST" then continue
        # if len(email) > 8 and < 26 then continue, else invalid
        # if email matches some letters + @ + some letters + . + 3 letters then valid


        # print "Running a login function!"
        # print "If successful login occurs, maybe return {'theuser':user} where user is a user object?"
        # print "If unsuccessful, maybe return { 'errors':['Login unsuccessful'] }"
        # print email
        # myString = email + " and more words"

            #return ("This is an invalid email")


    def register(self, postData):
        print ("Register a user here")
        print ("If successful, maybe return {'theuser':user} where user is a user object?")
        print ("If unsuccessful do something like this? return {'errors':['User first name to short', 'Last name too short'] ")

class User(models.Model):
    email = models.CharField(max_length = 45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    userManager = UserManager()
    # *************************
    # Connect an instance of UserManager to our User model overwriting
    # the old hidden objects key with a new one with extra properties!!!
    #objects = UserManager()

# Create your models here.
