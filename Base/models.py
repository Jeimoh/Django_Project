from django.db import models

# Create your models here.

class Rooms(models.Model):
    host = models.ForeignKey('Users', on_delete = models.CASCADE)
    topic = models.ForeignKey('Topic', on_delete = models.SET_NULL, null = True)
    name = models.CharField(max_length = 200)
    description = models.TextField(null = True, blank = True)
    #participants = models.
    dateModified = models.DateTimeField(auto_now = True)
    dateCreated = models.DateTimeField(auto_now_add = True)
    def __str__ (self):
        return self.name

class Users(models.Model):
    firstName = models.CharField(max_length = 50)
    lastName = models.CharField(max_length = 50)
    lastSeen = models.DateTimeField(auto_now = True)
    Email = models.EmailField(blank = True, null = True)
    phoneNumber = models.IntegerField()

    def __str__(self):
        self.FullNames = self.firstName +" " + self.lastName
        return self.FullNames


class Topic(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name
    
class Message(models.Model):
    User = models.ForeignKey(Users, on_delete = models.SET_NULL, null = True, blank = True)
    room = models.ForeignKey(Rooms, on_delete = models.CASCADE)
    body = models.TextField(max_length = 70)
    dateModified = models.DateTimeField(auto_now = True)
    dateCreated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.body




