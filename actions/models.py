from django.db import models
from users.models import Account,Group
import uuid
class AccountMessage(models.Model):
    sender=models.ForeignKey(Account,on_delete=models.SET_NULL,null=True,blank=True ,related_name="mesg")
    receiver = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True, related_name="messages")
    body = models.CharField(max_length=1000,null=True,blank=True)
    is_read = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.body

    class Meta:
        ordering = ['is_read', '-created']

class GroupMessage(models.Model):
    owner=models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)
    sender = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True, related_name="me")
    body = models.CharField(max_length=1000, null=True, blank=True)
    is_read = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.body

    class Meta:
        ordering = ['is_read', 'created']



# Create your models here.
