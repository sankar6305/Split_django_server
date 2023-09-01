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
    email = models.EmailField(unique=True, blank=True)
    GroupsInIt = models.ManyToManyField(Group)

    def __str__(self):
        return self.email

    def clean(self):
        if not User.objects.filter(email=self.email).exists():
            raise Exception("Email address must be registered.")

    def save(self, *args, **kwargs):
        self.clean()
        super(MemberInGroups, self).save(*args, **kwargs)





    
    