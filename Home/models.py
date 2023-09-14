from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User, Group
from datetime import date

Group.add_to_class('description', models.CharField(max_length=180,null=True, blank=True))

# Create your models here.
class Snippets(models.Model):
    email = models.EmailField(max_length=300)
    password = models.CharField(max_length=300)
    
class EmailGroup(models.Model):
    name = models.CharField(max_length=400, default='')
    emails = models.ManyToManyField(User)
    created_date = models.DateField(null=False, default=date.today, blank=True)


class MemberInGroups(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    GroupsInIt = models.ManyToManyField(Group)
    
    def DeleteGroupeName(self, group_to_remove):
        self.GroupsInIt.remove(group_to_remove)

#I want to add deleted group usersnames in seperate teble

class DeletedGroups(models.Model):
    username = models.CharField(max_length=100, default='')
    listOfGroups = models.JSONField(null=False, default=dict, blank=True)
        

class Expenses(models.Model):
    group_name = models.CharField(max_length=100, default='')
    listofExpenses = models.JSONField()

    def delete_by_index(self, index):
        index = len(self.listofExpenses) - 1 - index
        del self.listofExpenses[index]
        self.save()




    




    
    