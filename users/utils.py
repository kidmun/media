from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .models import Account,Project
from actions.models import UserPost
def search_users(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    accounts = Account.objects.filter(Q(username__icontains=search_query) | Q(first_name__icontains=search_query) | Q(last_name__icontains=search_query) | Q(
        location__icontains=search_query) | Q(job__icontains=search_query))
    return accounts,search_query

def search_projects(request):

    search_query = ''
    accounts = []
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        accounts = Account.objects.filter(Q(last_name__icontains=search_query) | Q(username__icontains=search_query) | Q(first_name__icontains=search_query))
    projects = Project.objects.filter(Q(title__icontains=search_query) |Q(owner__in=accounts))
    return projects,search_query

def search_contacts(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    accounts = Account.objects.filter(Q(username__icontains=search_query) | Q(first_name__icontains=search_query) | Q(last_name__icontains=search_query) | Q(job__icontains=search_query))
    return accounts,search_query

def search_followers(request,pk):
    account = Account.objects.get(id=pk)
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    accounts = account.follower_accounts.filter(Q(first_name__icontains=search_query) | Q(last_name__icontains=search_query) | Q(job__icontains=search_query))
    return accounts,search_query

def search_following(request,pk):
    account = Account.objects.get(id=pk)
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    accounts = account.followed_accounts.filter(Q(first_name__icontains=search_query) | Q(last_name__icontains=search_query) | Q(job__icontains=search_query))
    return accounts,search_query

def pagination(request,accounts,result):
    page = request.GET.get("page")
    paginator = Paginator(accounts, result)
    try:
        accounts = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        accounts = paginator.page(page)


    except EmptyPage:
        page = paginator.num_pages
        accounts = paginator.page(page)

    left_index = int(page) - 2
    if left_index < 1:
        left_index = 1
    right_index = int(page) + 3
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)
    return accounts,custom_range


def search_posts(request):
    search_query = ''
    accounts = []
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        accounts = Account.objects.filter(Q(username__icontains=search_query) | Q(first_name__icontains=search_query) | Q(last_name__icontains=search_query))
    posts = UserPost.objects.filter(Q(body__icontains=search_query) | Q(owner__in=accounts))
    return posts,search_query


