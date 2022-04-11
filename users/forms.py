from .models import Account,Project,Follow,Group
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from actions.models import GroupMessage


class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2'
        ]


    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for key, value in self.fields.items():
            value.widget.attrs.update({'class': 'form-control'})


class AccountForm(ModelForm):
    class Meta:
        model=Account
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'location',
            'bio',
            'job',
            'status',
            'profile',
            'github_account',
            'linkedin_account',




        ]

    def __init__(self, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs)
        for key, value in self.fields.items():
            value.widget.attrs.update({'class': 'form-control'})


class GroupMessageForm(ModelForm):

    class Meta:
        model = GroupMessage
        fields = ["body"]

    def __init__(self, *args, **kwargs):
        super(GroupMessageForm, self).__init__(*args, **kwargs)
        for key, value in self.fields.items():
            value.widget.attrs.update({'class': 'wrap','placeholder':'write your message here'})


class ProjectCreationForm(ModelForm):

    class Meta:
        model=Project
        fields=["title","description","project_profile","source_link"]

    def __init__(self, *args, **kwargs):
        super(ProjectCreationForm, self).__init__(*args, **kwargs)
        for key, value in self.fields.items():
            value.widget.attrs.update({'class': 'form-control'})


class FollowForm(ModelForm):
    class Meta:
        model=Follow
        fields="__all__"


class GroupForm(ModelForm):

    class Meta:
        model = Group
        fields = "__all__"


