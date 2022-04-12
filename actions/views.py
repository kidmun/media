from django.shortcuts import render,redirect
from .models import AccountMessage
from users.models import Account,Group
from .forms import AccountMessageForm
from users.forms import GroupForm
from users.utils import search_contacts
def messsagesPage(request):
    user_send_messages=request.user.account.mesg.all()
    user_received_messages = request.user.account.messages.all()
    message_list = []
    message_list_1 = []
    for message in user_send_messages:
        message_list.append(message.receiver.username)
    for message in user_received_messages:
        message_list_1.append(message.sender.username)

    sender_list=[]
    mes_list=[]

    messages_list=AccountMessage.objects.all()
    for mes in messages_list:
        if mes.sender.username not in sender_list and mes.sender.username != request.user.account.username:
            sender_list.append(mes.sender.username)
            mes_list.append(mes)

        elif mes.sender.username == request.user.account.username and mes.receiver.username not in sender_list:
            sender_list.append(mes.receiver.username)
            mes_list.append(mes)





    messages_list=mes_list
    content={"message_list":message_list,"message_li":message_list_1,"messages_list":messages_list}
    return render(request,"actions/messages.html",content)

def eachMessage(request,pk):
    form = AccountMessageForm()
    sender = Account.objects.get(id=pk)
    messages_list=AccountMessage.objects.all().order_by("created")
    if request.method == "POST":
        form = AccountMessageForm(request.POST)
        if form.is_valid():
            message=form.save(commit=False)
            message.sender = request.user.account
            message.receiver = sender
            message.save()
            return redirect("each_message",pk=sender.id)

    context={"sender":sender,"messages_list":messages_list,"form":form}
    return render(request,"actions/each_message.html",context)
# Create your views here.

def addContact(request,pk1,pk2):
    account = Account.objects.get(id=pk2)

    form = GroupForm()
    group = Group.objects.get(id=pk1)
    users,search_query = search_contacts(request)
    user_list = []
    for user in users:
        if user not in group.users.all():
            user_list.append(user)

    account.groups.add(group)
    account.save()
    group.users.add(account)
    group.save()
    print(account)
    print(account)


    context = {"user_list":user_list,"form":form,"group":group,"search_query":search_query}
    return render(request,"actions/add_contact.html",context)