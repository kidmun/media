from django.contrib import admin
from .models import Account,Project,Group,Follow
admin.site.register(Account)
admin.site.register(Project)
admin.site.register(Group)
admin.site.register(Follow)

# Register your models here.
