from __future__ import unicode_literals
from django.db import models
from datetime import datetime

class ShowManager(models.Manager):
    def validator(self, postData):
        errors = {} 
        for show in Show.objects.all():
            if postData['title'] == show.title:
                errors['title_has'] = "Title already exists in our database, please enter another!"
        if len(postData['title']) < 2:
            errors['title'] = "Title must be at least 2 characters long"
        if len(postData['network']) < 3:
            errors['network'] = "Network name must be at least 3 characters long"
        if postData['descript']:
            if len(postData['descript']) < 10:
                errors['descript'] = "Optional description must be at least 10 characters long"
        if len(postData['released']) < 10:
            errors['released'] = "Please enter a valid date"
        elif len(postData['released']) == 10:
            input_date = datetime.strptime(postData['released'], '%Y-%m-%d')
            if input_date > datetime.now():
                errors['released_new'] = "Please enter a valid date (must be in past)"
        
        return errors

class Show(models.Model):
    title = models.CharField(max_length = 255)
    network = models.CharField(max_length = 255)
    release_date = models.DateTimeField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()


