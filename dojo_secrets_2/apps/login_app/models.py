from __future__ import unicode_literals
from django.db import models
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def currentUser(self, request):
        id = request.session['user_id']
        return User.objects.get(id=id)

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField()
    password = models.CharField(max_length = 255)
    friends = models.ManyToManyField('self', related_name = 'friend_by')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()
