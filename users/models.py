from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name=models.CharField(max_length=200)
    username=models.CharField(max_length=200, null=True, blank=True)
    email=models.EmailField(max_length=200)
    location=models.CharField(max_length=200, null=True, blank=True)
    bio=models.TextField(max_length=200, null=True, blank=True)
    job=models.CharField(max_length=200, null=True, blank=True)
    status=models.CharField(max_length=200, null=True, blank=True)
    profile=models.ImageField(null=True, blank=True,upload_to="profiles/",default='profiles/user-default.png')
    github_account=models.CharField(max_length=200, null=True, blank=True)
    github_account = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.username)

class Project(models.Model):
    owner=models.ForeignKey(Account,null=True, blank=True, on_delete=models.SET_NULL)
    title=models.CharField(max_length=200)
    description=models.TextField(max_length=200, null=True, blank=True)
    project_profile=models.ImageField(null=True,blank=True,upload_to="project_profiles/",default='project_profiles/default.png')
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

