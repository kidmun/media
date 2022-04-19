from django.shortcuts import render,redirect
from .models import Account,Project,Group,Follow
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm,AccountForm,GroupMessageForm,ProjectCreationForm,FollowForm
from .utils import search_users,search_projects,search_contacts,search_followers,search_following,pagination
from actions.models import UserPost

def loginPage(request):
    if request.method=="POST":
        username = request.POST["username"].lower()
        password = request.POST["password"]
        try:
            User.objects.get(username=username)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "you are successfully logged in")
                return redirect('front')
            else:
                messages.error(request, "username or password incorrect")
        except:
            messages.error(request, "user does not exist")


    return render(request,"users/login.html")

def logoutPage(request):
    logout(request)

    messages.success(request, "you are successfully logged out")
    return redirect('login')

def registerPage(request):
    form=RegisterForm()
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "user account is successfully created")
            login(request, user)
            return redirect('edit_account',pk=user.id)

    content={"form":form}
    return render(request,"users/register.html",content)

def front(request):
    posts = UserPost.objects.all()

    content={"posts":posts}
    return render(request,"users/front.html",content)

@login_required(login_url="login")
def account(request,pk):
    account=request.user.account
    count = len(account.project_set.all())
    content={"account":account,"count":count}
    return render(request,"users/account.html",content)

@login_required(login_url="login")
def editAccount(request,pk):

    account = request.user.account
    form=AccountForm(instance=account)
    if request.method == "POST":
        form=AccountForm(request.POST,request.FILES,instance=account)
        if form.is_valid():
            form.save()
            return redirect('account',pk=account.id)
    context={"form":form}

    return render(request,"users/edit_account.html",context)

def projects(request):

    projects, search_query = search_projects(request)
    projects, custom_range = pagination(request,projects,4)
    context={"projects":projects,"search_query":search_query,"custom_range":custom_range}
    return render(request,"users/projects.html",context)

def addProject(request):
    form = ProjectCreationForm()
    if request.method == "POST":
        form = ProjectCreationForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user.account
            project.save()
            return redirect("account", pk=request.user.account.id)
    context={"form":form}

    return render(request,"users/add_project.html",context)

def editProject(request,pk):
    account =request.user.account
    project = account.project_set.get(id=pk)
    form = ProjectCreationForm(instance=project)
    if request.method == "POST":
        form = ProjectCreationForm(request.POST, request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect("account", pk=request.user.account.id)
    context = {"form": form}

    return render(request, "users/edit_project.html", context)



def groupPage(request):
    account = request.user.account
    users_number = []
    for group in account.groups.all():
        users_number.append(len(group.users.all()))


    content={"account":account,"users_number":users_number}
    return render(request,"users/group.html",content)
def eachGroup(request,pk):
    group=Group.objects.get(id=pk)
    form = GroupMessageForm()
    group_users,search_query = search_contacts(request)
    group_users_list = []
    for user in group_users:
        if user in group.users.all():
            group_users_list.append(user)
    if request.method == "POST":
        form = GroupMessageForm(request.POST)
        if form.is_valid():
            message=form.save(commit=False)
            message.sender = request.user.account
            message.owner = group
            message.save()
            return redirect("each_group",pk=group.id)
    content={"group":group,"form":form,"group_users_list":group_users_list,"search_query":search_query}
    return render(request,"users/each_group.html",content)

@login_required(login_url="login")
def userAccount(request,pk):
    account = Account.objects.get(id=pk)
    form = AccountForm()
    if request.method == "POST":
        if account in request.user.account.followed_accounts.all():
            account.follower_accounts.remove(request.user.account)
            request.user.account.followed_accounts.remove(account)
            if request.user.account.following > 0 and account.followers:
                account.followers -= 1
                request.user.account.following -= 1

        else:
            account.follower_accounts.add(request.user.account)
            request.user.account.followed_accounts.add(account)
            account.followers += 1
            request.user.account.following += 1

        account.save()
        request.user.account.save()
        return redirect('user_account', pk=account.id)

    count=len(account.project_set.all())
    content={"account":account,"count":count,"form":form}
    return render(request,"users/user_account.html",content)

def usersPage(request):
    accounts,search_query = search_users(request)
    accounts,custom_range = pagination(request, accounts, 5)
    content={"users":accounts,"search_query":search_query,"custom_range":custom_range}
    return render(request,"users/users.html",content)

def follwersPage(request,pk):
    accounts,search_query = search_followers(request,pk)
    context = {"accounts":accounts,"search_query":search_query}
    return render(request,"users/followers.html",context)

def followingPage(request,pk):
    accounts,search_query = search_following(request,pk)
    context = {"accounts": accounts, "search_query": search_query}
    return render(request, "users/following.html", context)


# Create your views here.
