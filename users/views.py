from django.shortcuts import render
from .models import Account


def index(request):

    content={}
    return render(request,"users/front.html",content)


def account(request,pk):
    accounts=Account.objects.all()
    content={"accounts":accounts}
    return render(request,"users/account.html",content)
# Create your views here.
