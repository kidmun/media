from django.contrib.auth.models import User
from .models import Account
from django.db.models.signals import post_save,post_delete
def createAccount(sender,instance,created,**kwargs):
    if created:
        user=instance
        account=Account.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,

        )

def updateUser(sender,instance,created,**kwargs):
    account = instance
    user = instance.user
    if created == False:
        user.first_name = account.first_name
        user.last_name = account.last_name
        user.username = account.username
        user.email = account.email
        user.save()

def updateAccount(request,sender,instance,created,**kwargs):
    account = instance
    if created:
        account.follower_accounts.add(request.user.account)
        account.save()



post_save.connect(createAccount,sender=User)
post_save.connect(updateUser,sender=Account)
post_save.connect(updateAccount,sender=Account.followed_accounts)