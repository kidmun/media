from django.db import models
from django.contrib.auth.models import User


import uuid


# Create your models here.
class Group(models.Model):
    name= models.CharField(max_length=20, null=True, blank=True)
    group_profile=models.ImageField(null=True,blank=True,upload_to="project_profiles/", default='project_profiles/default.jpg')
    users=models.ManyToManyField('Account',blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name=models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    username=models.CharField(max_length=200, null=True, blank=True)
    email=models.EmailField(max_length=200)
    location=models.CharField(max_length=200, null=True, blank=True)
    bio=models.TextField(max_length=200, null=True, blank=True)
    job=models.CharField(max_length=200, null=True, blank=True)
    status=models.CharField(max_length=200, null=True, blank=True)
    profile=models.ImageField(null=True, blank=True,upload_to="profiles/",default='profiles/user-default.png')
    groups=models.ManyToManyField('Group',blank=True)
    github_account=models.CharField(max_length=200, null=True, blank=True)
    linkedin_account = models.CharField(max_length=200, null=True, blank=True)
    follower_accounts= models.ManyToManyField('Account', blank=True)
    followed_accounts= models.ManyToManyField('Account', blank=True,related_name="follows")

    followers = models.IntegerField(default=0, null=True, blank=True)
    following = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.username)

    class Meta:
        ordering = ['-followers']


class Follow(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

class Project(models.Model):
    owner=models.ForeignKey(Account, on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    description=models.TextField(max_length=2000, null=True, blank=True)
    project_profile=models.ImageField(null=True,blank=True,upload_to="project_profiles/",default='project_profiles/default.jpg')
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.title)



