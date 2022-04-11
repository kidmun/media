from .models import AccountMessage,GroupMessage
from django.contrib.auth.models import User
from django.forms import ModelForm

class AccountMessageForm(ModelForm):

    class Meta:
        model = AccountMessage
        fields = ["body"]

    def __init__(self, *args, **kwargs):
        super(AccountMessageForm, self).__init__(*args, **kwargs)
        for key, value in self.fields.items():
            value.widget.attrs.update({'class': 'wrap','placeholder':'write your message here'})